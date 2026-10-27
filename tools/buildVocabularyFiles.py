#!/usr/bin/env python3
"""
Build the published files for a SKOS vocabulary from its JSON-LD source.

The JSON-LD file is the only file anyone edits. From it this writes:
  - <name>.ttl beside it: the whole scheme in Turtle. This is the input the
    iSamples vocabulary action (isamplesorg/vocabularies) renders to HTML, and
    what w3id serves for the scheme IRI on a text/turtle request.
  - <conceptDir>/<localName>.jsonld and .ttl: one file per concept, holding that
    concept's own statements, with its broader/narrower concepts and its scheme
    as {"@id"} references. w3id serves these for a concept IRI, so each IRI
    dereferences to its own skos:Concept rather than to the whole scheme.

The concept's local name (the part of its IRI after the scheme namespace) must
equal its skos:notation; the build fails otherwise, because the w3id rules map
the IRI's last segment straight onto the file name.

`anchors` patches the HTML the iSamples action renders. That action gives each
concept an anchor made by LOWERCASING its local name (#samplepreparation), but
links "Child of" entries by the local name as written (#samplePreparation), so
for camelCase names those links go nowhere, and a w3id redirect to
page.html#<localName> would miss too. This adds an anchor with the local name as
written next to each lowercased one.

Usage:
    python tools/buildVocabularyFiles.py vocabularies/activityTypes.jsonld
    python tools/buildVocabularyFiles.py vocabularies/activityTypes.jsonld --check
    python tools/buildVocabularyFiles.py vocabularies/activityTypes.jsonld --anchors vocabularies/docs/activityTypes.html
"""

import argparse
import copy
import json
import os
import re
import sys

import rdflib

# The concept files sit in a folder named after the scheme IRI's last segment,
# matching the IRIs: https://w3id.org/cdif/provenance/activityType/<localName>.
# The extra prefix lets the iSamples action name the scheme as a CURIE.
EXTRA_PREFIXES = {"cdifprov": "https://w3id.org/cdif/provenance/"}


def dump_jsonld(x, ind=0):
    """JSON in the source files' style: flat objects and single-item lists inline."""
    def flat(v):
        return not isinstance(v, (dict, list))

    def inline_dict(d):
        return isinstance(d, dict) and all(flat(v) for v in d.values())

    p = '  ' * ind
    if isinstance(x, dict):
        if inline_dict(x):
            return json.dumps(x, ensure_ascii=False)
        items = [f'{p}  {json.dumps(k, ensure_ascii=False)}: {dump_jsonld(v, ind + 1)}' for k, v in x.items()]
        return '{\n' + ',\n'.join(items) + '\n' + p + '}'
    if isinstance(x, list):
        if len(x) <= 1 and all(flat(i) or inline_dict(i) for i in x):
            return '[' + ', '.join(dump_jsonld(i) for i in x) + ']'
        return '[\n' + ',\n'.join(p + '  ' + dump_jsonld(i, ind + 1) for i in x) + '\n' + p + ']'
    return json.dumps(x, ensure_ascii=False)


def to_turtle(doc):
    g = rdflib.Graph()
    g.parse(data=json.dumps(doc), format='json-ld')
    for prefix, ns in list(doc['@context'].items()) + list(EXTRA_PREFIXES.items()):
        if isinstance(ns, str) and ns.endswith(('/', '#')):
            g.bind(prefix, ns, override=True, replace=True)
    return g.serialize(format='turtle')


def concepts(nodes):
    for c in nodes:
        yield c
        yield from concepts(c.get('skos:narrower', []))


def build(source):
    """Return {relative path: file text} for every generated file."""
    doc = json.load(open(source, encoding='utf-8'))
    ctx = doc['@context']
    scheme = doc['@id']
    folder, name = os.path.split(source)
    concept_dir = scheme.rstrip('/').rsplit('/', 1)[1]
    ns_prefix = next(p for p, ns in ctx.items() if ns == scheme + '/')

    out = {os.path.join(folder, os.path.splitext(name)[0] + '.ttl'): to_turtle(doc)}
    for c in concepts(doc['skos:hasTopConcept']):
        local = c['@id'].split(':', 1)[1]
        if not c['@id'].startswith(ns_prefix + ':') or local != c['skos:notation']:
            sys.exit(f"{c['@id']}: local name must equal skos:notation ({c['skos:notation']!r})")
        node = copy.deepcopy(c)
        if 'skos:narrower' in node:
            node['skos:narrower'] = [{'@id': n['@id']} for n in node['skos:narrower']]
        node = {'@context': ctx, **node}
        base = os.path.join(folder, concept_dir, local)
        out[base + '.jsonld'] = dump_jsonld(node) + '\n'
        out[base + '.ttl'] = to_turtle(node)
    return out, os.path.join(folder, concept_dir)


def add_anchors(source, html_path):
    doc = json.load(open(source, encoding='utf-8'))
    html = open(html_path, encoding='utf-8').read()
    for c in concepts(doc['skos:hasTopConcept']):
        local = c['skos:notation']
        if local == local.lower() or f'id="{local}"' in html:
            continue
        html, n = re.subn(f'(<span id="{local.lower()}"></span>)', rf'\1<span id="{local}"></span>', html, count=1)
        if not n:
            sys.exit(f'{html_path}: no anchor #{local.lower()} for {c["@id"]}')
    open(html_path, 'w', encoding='utf-8', newline='\n').write(html)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('source', help='the vocabulary JSON-LD file')
    ap.add_argument('--check', action='store_true', help='fail if the generated files are not up to date')
    ap.add_argument('--anchors', metavar='HTML', help='add case-preserving concept anchors to the rendered HTML')
    a = ap.parse_args()

    if a.anchors:
        add_anchors(a.source, a.anchors)
        return 0

    files, concept_dir = build(a.source)
    existing = {os.path.join(concept_dir, f) for f in os.listdir(concept_dir)} if os.path.isdir(concept_dir) else set()
    stale = sorted(existing - set(files))
    changed = [p for p, text in files.items()
               if not os.path.exists(p) or open(p, encoding='utf-8').read() != text]
    if a.check:
        for p in changed:
            print(f'out of date: {p}')
        for p in stale:
            print(f'no longer generated: {p}')
        if changed or stale:
            print(f'Run: python tools/buildVocabularyFiles.py {a.source}')
            return 1
        print(f'{len(files)} generated files up to date')
        return 0

    os.makedirs(concept_dir, exist_ok=True)
    for p in changed:
        open(p, 'w', encoding='utf-8', newline='\n').write(files[p])
    for p in stale:
        os.remove(p)
    print(f'{len(files)} files: {len(changed)} written, {len(stale)} removed')
    return 0


if __name__ == '__main__':
    sys.exit(main())

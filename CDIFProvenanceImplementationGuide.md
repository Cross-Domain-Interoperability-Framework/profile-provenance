# CDIF Provenance Profile — Implementation Guide

# Purpose and scope

The **CDIF Provenance profile module** (`cdifProvenance`) specifies metadata elements to document the workflow used to create a resource. This is a preliminary draft.

# Conformance

A resource conforms to the CDIF Provenance profile when its catalog record declares conformance to the profile identifier. The catalog record is carried on `schema:subjectOf` as a `dcat:CatalogRecord`:

```json
"schema:subjectOf": {
  "@type": ["schema:CreativeWork", "dcat:CatalogRecord"],
  "dcterms:conformsTo": [
    "https://w3id.org/cdif/provenance/1.0"
  ]
}
```

Other properties added in this profile are optional; conformance requires only that the constraints in the JSON Schema and SHACL rules are satisfied.

## Validation

Two validators ship with this repository:
- **JSON Schema** — `cdifProvenanceStructuredSchema.json` (Draft 2020-12), generated from the source register.
- **SHACL** — `provenanceRules.shacl`, a self-contained shapes graph merged from every composing building block plus the profile-level shapes.

```bash
python FrameAndValidate.py examples/<file>.json --validate \
  --schema cdifProvenanceStructuredSchema.json --frame <frame.jsonld>
```

Validation is **open-world**: properties not described by the profile are allowed.

# Provenance of the artifacts

The schema and SHACL files are generated from the canonical source register, [metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks):

- `cdifProvenanceStructuredSchema.json` ← `tools/resolve_schema.py cdifProvenance`
- `provenanceRules.shacl` ← `tools/validate_shacl.py cdifProvenance --emit-shapes`

Source profile directory: `_sources/profiles/cdifProfile/cdifProvenance/`.

MODEL description is preliminary...

# Dataset Properties added by the CDIF Provenance Profile

## schema:Dataset {#sec-schema-dataset}

Building block that defines the prov:wasGeneratedBy property for CDIF metadata records. Wraps the cdifProvActivity building block as an array of provenance activities that describe how the described resource was generated.

### schema:subjectOf

- **Cardinality:** Optional
- **Content:** —

### prov:wasGeneratedBy

- **Cardinality:** Optional
- **Content:** array of object
- **Description:** Provenance activities describing how the resource was generated, including agents, instruments, methodology, temporal bounds, and action chaining.

# Class Definitions

## Person {#sec-person}

schema for cdif profile of schema.org/Person

### @id

- **Cardinality:** Optional
- **Content:** string

### @type

- **Cardinality:** Optional
- **Content:** array of string

### schema:name

- **Cardinality:** Optional
- **Content:** string
- **Description:** string label for person that is meaningful for human users, should format consistently. Recommend 'Family Name, Given name' format.

### schema:description

- **Cardinality:** Optional
- **Content:** string

### schema:identifier

- **Cardinality:** Optional
- **Content:** one of: [object reference](#/$defs/Identifier), string
- **Description:** identifier for person, recommend ORCID

### schema:alternateName

- **Cardinality:** Optional
- **Content:** string
- **Description:** other labels by which the person might be known

### schema:affiliation

- **Cardinality:** Optional
- **Content:** [object reference](#/$defs/Organization)
- **Description:** if affiliation is present, value must be a schema:Organization.

### schema:contactPoint

- **Cardinality:** Optional
- **Content:** object
- **Description:** restrict to email only. Schema.org allows telephone and postal contacts as well

### schema:sameAs

- **Cardinality:** Optional
- **Content:** array of one of: string, object
- **Description:** other identifiers for the person

## Identifier {#sec-identifier}

Properties for a schema.org identifier (schema:PropertyValue pattern). **Union-type policy:** In CDIF profile UML models an attribute typed as schema:Identifier / schema:PropertyValue is represented by a single attribute of that class type. The JSON Schema implementation permits the property value to be EITHER a plain string (interpreted as the bare identifier value) OR a full schema:PropertyValue object (with explicit @type, propertyID, value). Consumers should accept either form.

### @type

- **Cardinality:** Optional
- **Content:** array of string

### schema:propertyID

- **Cardinality:** Optional
- **Content:** string
- **Description:** In this context for the schema:PropertyValue, this field is an identifier for the identifier schema, e.g. DOI, ARK. Get values from https://registry.identifiers.org/registry/ for interoperability

### schema:value

- **Cardinality:** Optional
- **Content:** string
- **Description:** the identifier string. E.g. 10.5066/F7VX0DMQ

### schema:url

- **Cardinality:** Optional
- **Content:** string
- **Description:** web-resolveable string for the identifier; host name part is location of a resolver that will return some representation for the given identifier value. E.g. https://doi.org/10.5066/F7VX0DMQ

## Organization {#sec-organization}

### @id

- **Cardinality:** Optional
- **Content:** string

### @type

- **Cardinality:** Optional
- **Content:** array of one of: string (`"schema:Organization"` | `"schema:FundingAgency"` | `"schema:Consortium"` | `"schema:Corporation"` | `"schema:EducationalOrganization"` | `"schema:FundingScheme"` | `"schema:GovernmentOrganization"` | `"schema:NGO"` | `"schema:Project"` | `"schema:ResearchOrganization"`)

### schema:additionalType

- **Cardinality:** Optional
- **Content:** array of one of: [object reference](#/$defs/DefinedTerm), string

### schema:name

- **Cardinality:** Optional
- **Content:** string
- **Description:** string label for organization that is meaningful for human users

### schema:alternateName

- **Cardinality:** Optional
- **Content:** string
- **Description:** other labels by which the organization might be known

### schema:description

- **Cardinality:** Optional
- **Content:** string

### schema:identifier

- **Cardinality:** Optional
- **Content:** one of: [object reference](#/$defs/Identifier), string
- **Description:** identifier for organization

### schema:sameAs

- **Cardinality:** Optional
- **Content:** array of one of: string, object
- **Description:** other identifiers for the organization

## DefinedTerm {#sec-definedterm}

schema.org Defined Term schema. **Union-type policy:** In CDIF profile UML models an attribute typed as schema:DefinedTerm is represented by a single attribute of that class type. The JSON Schema implementation permits the property value to be EITHER a plain string (interpreted as schema:name or schema:termCode in the default vocabulary) OR a full schema:DefinedTerm object (with explicit @type, name, identifier, termCode, inDefinedTermSet). Consumers should accept either form. Note that this differs from the cdif Concept policy: a Concept (skos:Concept) in CDIF profiles MUST be a controlled-vocabulary entry (object form or @id-reference) — plain strings are not permitted for Concept-typed values because vocabulary identity cannot be recovered from an unscoped label.

### @type

- **Cardinality:** Optional
- **Content:** array of string

### schema:name

- **Cardinality:** Optional
- **Content:** string
- **Description:** text label for the term that is useful to human user

### schema:identifier

- **Cardinality:** Optional
- **Content:** one of: string, [object reference](#/$defs/Identifier)

### schema:inDefinedTermSet

- **Cardinality:** Optional
- **Content:** string
- **Description:** Name for the controlled vocabulary responsible for this keyword.

### schema:termCode

- **Cardinality:** Optional
- **Content:** string
- **Description:** A representative code for this keyword in the controlled vocabulary. Analogous to skos:Notation

## AgentInRole {#sec-agentinrole}

For more granularity on how a person contributed to a Dataset, use schema:Role. The schema.org documentation does not state that the Role type is an expected data type of author, creator and contributor, but that is addressed in this blog post (http://blog.schema.org/2014/06/introducing-role.html). see https://github.com/ESIPFed/science-on-schema.org/blob/develop/guides/Dataset.md#roles-of-people

### @type

- **Cardinality:** Required
- **Content:** array of string

### schema:roleName

- **Cardinality:** Required
- **Content:** one of: string, [object reference](#/$defs/DefinedTerm)

### schema:contributor

- **Cardinality:** Required
- **Content:** one of: object, [object reference](#/$defs/Person), [object reference](#/$defs/Organization)

## AdditionalProperty {#sec-additionalproperty}

PropertyValue values required to define a soft-typed property with a value.

### @type

- **Cardinality:** Optional
- **Content:** array of string

### schema:propertyID

- **Cardinality:** Optional
- **Content:** array of one of: string, object, [object reference](#/$defs/DefinedTerm)
- **Description:** identifier or name for the property concept quantified by the values in this variable slot. Multiple values can specify the property at different levels of granularity.

### schema:name

- **Cardinality:** Required
- **Content:** string

### schema:value

- **Cardinality:** Required
- **Content:** one of: string, number, boolean, object

### schema:unitCode

- **Cardinality:** Optional
- **Content:** one of: string, [object reference](#/$defs/DefinedTerm)

### schema:unitText

- **Cardinality:** Optional
- **Content:** string

## LanguageTaggedValue {#sec-languagetaggedvalue}

An RDF literal value with a language tag, serialized as a JSON-LD value object. Inlined from skosConcept (the resolver does not preserve cross-file '#/$defs/...' fragment refs).

### @value

- **Cardinality:** Required
- **Content:** string
- **Description:** The text content.

### @language

- **Cardinality:** Optional
- **Content:** string
- **Description:** BCP 47 language tag (e.g. en, fr, de).

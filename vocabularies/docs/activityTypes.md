---
comment: | 
  WARNING: This file is generated. Any edits will be lost!
format:
  html:
    ascii: true
    toc: true
    toc-depth: 4
    number-sections: true
    anchor-sections: false
    number-depth: 8
execute:
  echo: false
---

[]{#CDIFprovenanceactivitytypes}

# **Concept scheme:** CDIF provenance activity types

Vocabulary last modified:  2026-10-27

subtitle: 
  Kinds of activity in a research, laboratory or data workflow. A workflow step (schema:step, or a prov:Activity in a multi-activity chain) is typed with one of these concepts through schema:additionalType, while its schema:name stays free to say what the step specifically did. Each concept is mapped to the provenance activity classes proposed at the Dagstuhl workshop (PROV_Classes.ttl).

Namespace: 
[`https://w3id.org/cdif/provenance/activityType`](https://w3id.org/cdif/provenance/activityType)

**History**


- [Accessing](#accessing)

- [Aggregating](#aggregating)

- [Analysing](#analysing)

- [Archiving](#archiving)

- [Cataloguing](#cataloguing)

- [Consuming](#consuming)

- [Data validating](#datavalidating)

- [Extracting](#extracting)

- [Harmonising](#harmonising)

- [Integrating](#integrating)

- [Conditioning (passive)](#passiveconditioning)

- [Preserving](#preserving)

- [Provisioning](#provisioning)

- [Sampling](#sampling)

- [Calibrating](#calibrating)
    - [Instrument calibration](#instrumentcalibration)

- [Configuring](#configuring)
    - [Instrument tuning](#instrumenttuning)

- [Creating](#creating)
    - [Deriving](#deriving)

- [Conditioning (intentional)](#intentionalconditioning)
    - [Sample preparation](#samplepreparation)
        - [Ion milling](#ionmilling)
        - [Sample digestion](#sampledigestion)

- [Observing / measuring](#observingmeasuring)
    - [Data acquisition](#dataacquisition)

- [Quality controlling](#qualitycontrolling)
    - [Quality control](#qualitycontrol)

- [Data transforming](#datatransforming)
    - [Data cleaning](#datacleaning)
    - [Data processing](#dataprocessing)

**Concepts**

[]{#accessing}

##  Accessing
- An activity during which an agent realises its rights and abilities
to approach and interact with an entity.
- Concept URI: https://w3id.org/cdif/provenance/activityType/accessing



[]{#aggregating}

##  Aggregating
- An activity during which multiple entities are gathered together and
assembled into a whole based on a defined set of criteria.
- Concept URI: https://w3id.org/cdif/provenance/activityType/aggregating



[]{#analysing}

##  Analysing
- An activity during which one or more entities are studied by
examining their constituent parts and the interrelationships between
those parts in order to increase one's knowledge about those entities.
- Concept URI: https://w3id.org/cdif/provenance/activityType/analysing



[]{#archiving}

##  Archiving
- An activity during which an entity is transferred to a facility
charged with its long-term (generally >10 years) preservation.
- Concept URI: https://w3id.org/cdif/provenance/activityType/archiving



[]{#cataloguing}

##  Cataloguing
- An activity during which the existence of an entity is described in
a systematic list.
- Concept URI: https://w3id.org/cdif/provenance/activityType/cataloguing



[]{#consuming}

##  Consuming
- An activity during which an agent acquires and uses an entity.
- Concept URI: https://w3id.org/cdif/provenance/activityType/consuming



[]{#datavalidating}

##  Data validating
- An activity during which a volume of data is evaluated in relation
to some specification or criteria, usually assessing its soundness,
justifiability, or appropriateness for a given purpose.
- Concept URI: https://w3id.org/cdif/provenance/activityType/dataValidating



[]{#extracting}

##  Extracting
- An activity during which an entity is moved to a new location.
- Concept URI: https://w3id.org/cdif/provenance/activityType/extracting



[]{#harmonising}

##  Harmonising
- An activity during which a set of entities are transformed to
regularise their properties, allowing meaningful collective treatment.
- Concept URI: https://w3id.org/cdif/provenance/activityType/harmonising



[]{#integrating}

##  Integrating
- An activity during which multiple entities are unified into a
coherent whole, often losing their distinctiveness.
- Concept URI: https://w3id.org/cdif/provenance/activityType/integrating



[]{#passiveconditioning}

##  Conditioning (passive)
- A non-intentional process in which the state of an entity is
changed, such that it impacts or precipitates a planned and subsequent
activity.
- Concept URI: https://w3id.org/cdif/provenance/activityType/passiveConditioning



[]{#preserving}

##  Preserving
- An activity during which an entity is modified to stabilise its
make-up and properties, facilitating future use.
- Concept URI: https://w3id.org/cdif/provenance/activityType/preserving



[]{#provisioning}

##  Provisioning
- An activity during which an agent supplies an entity to other
agents.
- Concept URI: https://w3id.org/cdif/provenance/activityType/provisioning



[]{#sampling}

##  Sampling
- An activity in which a portion or part of an entity is extracted
from or identified within a whole.
- Concept URI: https://w3id.org/cdif/provenance/activityType/sampling



[]{#calibrating}

##  Calibrating
- An activity during which measurement data produced by an entity are
compared to a reference dataset with known accuracy in order to
establish, verify, or document the accuracy of the entity.
- Concept URI: https://w3id.org/cdif/provenance/activityType/calibrating


[]{#instrumentcalibration}

###  Instrument calibration
- Child of:
 [`calibrating`](#calibrating)
- An activity that measures reference materials or standards of known
value to establish the relationship between the instrument's response
and the quantity being measured.
- Concept URI: https://w3id.org/cdif/provenance/activityType/instrumentCalibration



[]{#configuring}

##  Configuring
- An activity during which an entity is modified to grant it desirable
properties or dispose it to desirable behaviour.
- Concept URI: https://w3id.org/cdif/provenance/activityType/configuring


[]{#instrumenttuning}

###  Instrument tuning
- Child of:
 [`configuring`](#configuring)
- An activity that adjusts instrument settings to optimise performance
for a measurement, judged by the instrument's response rather than
against reference materials of known value.
- Concept URI: https://w3id.org/cdif/provenance/activityType/instrumentTuning



[]{#creating}

##  Creating
- An activity through which an entity is brought into existence.
Serves as a superclass for other more expressive classes that create
entities, such as authoring.
- Concept URI: https://w3id.org/cdif/provenance/activityType/creating


[]{#deriving}

###  Deriving
- Child of:
 [`creating`](#creating)
- A creation process during which a new entity arises from parts or
all of pre-existing entities.
- Concept URI: https://w3id.org/cdif/provenance/activityType/deriving



[]{#intentionalconditioning}

##  Conditioning (intentional)
- An activity in which the state of an entity is intentionally changed
by an agent, in preparation for a specified and subsequent activity.
- Concept URI: https://w3id.org/cdif/provenance/activityType/intentionalConditioning


[]{#samplepreparation}

###  Sample preparation
- Child of:
 [`intentionalConditioning`](#intentionalConditioning)
- An activity that changes the physical or chemical state of a sample
to make it suitable for measurement, for example cutting, mounting,
polishing, coating, crushing, sieving or dissolving it.
- Concept URI: https://w3id.org/cdif/provenance/activityType/samplePreparation


[]{#ionmilling}

####  Ion milling
- Child of:
 [`samplePreparation`](#samplePreparation)
- Sample preparation that thins or shapes a sample by sputtering it
with an ion beam, for example to make an electron-transparent section.
- Concept URI: https://w3id.org/cdif/provenance/activityType/ionMilling


[]{#sampledigestion}

####  Sample digestion
- Child of:
 [`samplePreparation`](#samplePreparation)
- Sample preparation that dissolves a solid sample, typically in acid,
to produce a solution for analysis.
- Concept URI: https://w3id.org/cdif/provenance/activityType/sampleDigestion



[]{#observingmeasuring}

##  Observing / measuring
- An activity during which an entity gathers data or information about
another entity or itself. Measuring is observing during which
reference standards or similar entities are used for the quantitative
comparison of properties.
- Concept URI: https://w3id.org/cdif/provenance/activityType/observingMeasuring


[]{#dataacquisition}

###  Data acquisition
- Child of:
 [`observingMeasuring`](#observingMeasuring)
- An activity in which an instrument or observer measures or observes
the object of study and records the result as data.
- Concept URI: https://w3id.org/cdif/provenance/activityType/dataAcquisition



[]{#qualitycontrolling}

##  Quality controlling
- An activity during which an entity's compliance to a set of defined
criteria is assessed, resulting in acceptance or rejection of that
entity in a set of further activities.
- Concept URI: https://w3id.org/cdif/provenance/activityType/qualityControlling


[]{#qualitycontrol}

###  Quality control
- Child of:
 [`qualityControlling`](#qualityControlling)
- An activity that assesses data or a process against defined
criteria, for example measuring secondary standards, checking
precision and accuracy, or flagging anomalous values.
- Concept URI: https://w3id.org/cdif/provenance/activityType/qualityControl



[]{#datatransforming}

##  Data transforming
- An activity during which a volume of data is modified.
- Concept URI: https://w3id.org/cdif/provenance/activityType/dataTransforming


[]{#datacleaning}

###  Data cleaning
- Child of:
 [`dataTransforming`](#dataTransforming)
- A data transformation during which erroneous, duplicated, or
corrupted data is removed from a volume of data.
- Concept URI: https://w3id.org/cdif/provenance/activityType/dataCleaning


[]{#dataprocessing}

###  Data processing
- Child of:
 [`dataTransforming`](#dataTransforming)
- An activity that transforms acquired data into reported results, for
example background and blank correction, drift correction, matrix
correction, applying a calibration, or converting units.
- **Alternate labels:**
Data reduction
- Concept URI: https://w3id.org/cdif/provenance/activityType/dataProcessing




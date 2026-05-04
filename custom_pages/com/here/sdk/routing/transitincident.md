---
title: "TransitIncident (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttransitincident"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TransitIncident

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TransitIncident
------------------------------------------------------------------------
public final class TransitIncident extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
A transit incident describes disruptions on the transit network. Disruptions scale from delays to service cancellations.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [description](#description)

A human readable description of the incident

[`TransitIncidentEffect`](sdk-for-android-explore-api-reference-latesttransitincidenteffect "enum class in com.here.sdk.routing")

  [effect](#effect)

Effect of the incident.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [summary](#summary)

A human readable summary of the incident.

[`TransitIncidentType`](sdk-for-android-explore-api-reference-latesttransitincidenttype "enum class in com.here.sdk.routing")

  [type](#type)

Type of the incident.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [url](#url)

Link to the original incident published at the agency website.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [validFrom](#validFrom)

Valid from.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [validUntil](#validUntil)

Valid until.

## Constructor Summary

Constructors

Constructor

  Description

  [TransitIncident](#%3Cinit%3E(java.lang.String,java.lang.String,com.here.sdk.routing.TransitIncidentType,com.here.sdk.routing.TransitIncidentEffect,java.util.Date,java.util.Date,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` summary, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` description, `[`TransitIncidentType`](sdk-for-android-explore-api-reference-latesttransitincidenttype "enum class in com.here.sdk.routing")` type, `[`TransitIncidentEffect`](sdk-for-android-explore-api-reference-latesttransitincidenteffect "enum class in com.here.sdk.routing")` effect, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` validFrom, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` validUntil, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` url)`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### summary

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) summary

    A human readable summary of the incident.

### description

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description

    A human readable description of the incident

### type

@Nullable public [TransitIncidentType](sdk-for-android-explore-api-reference-latesttransitincidenttype "enum class in com.here.sdk.routing") type

    Type of the incident.

### effect

@Nullable public [TransitIncidentEffect](sdk-for-android-explore-api-reference-latesttransitincidenteffect "enum class in com.here.sdk.routing") effect

    Effect of the incident.

### validFrom

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) validFrom

    Valid from.

### validUntil

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) validUntil

    Valid until.

### url

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) url

    Link to the original incident published at the agency website.

## Constructor Details

  - (java.lang.String,java.lang.String,com.here.sdk.routing.TransitIncidentType,com.here.sdk.routing.TransitIncidentEffect,java.util.Date,java.util.Date,java.lang.String)" class="section detail">

### TransitIncident

public TransitIncident(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) summary, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description, @Nullable [TransitIncidentType](sdk-for-android-explore-api-reference-latesttransitincidenttype "enum class in com.here.sdk.routing") type, @Nullable [TransitIncidentEffect](sdk-for-android-explore-api-reference-latesttransitincidenteffect "enum class in com.here.sdk.routing") effect, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) validFrom, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) validUntil, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) url)

    Creates a new instance.
Parameters:
    `summary` -

    A human readable summary of the incident.

    `description` -

    A human readable description of the incident

    `type` -

    Type of the incident.

    `effect` -

    Effect of the incident.

    `validFrom` -

    Valid from.

    `validUntil` -

    Valid until.

    `url` -

    Link to the original incident published at the agency website.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

---
title: "Evse (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestevse"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Evse

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.Evse
------------------------------------------------------------------------
public final class Evse extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`EVSEConnector`](sdk-for-android-explore-api-reference-latestevseconnector "class in com.here.sdk.search")`>`

  [connectors](#connectors)

List of connectors of this EVSE.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [cpoEvseEmi3Id](#cpoEvseEmi3Id)

Identifier in Emi3 format of the EVSE within the Charge Point Operator (CPO) platform.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [cpoId](#cpoId)

The unique ID of an EVSE in the system of the CPO.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [id](#id)

HERE ID of the EVSE.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [lastUpdated](#lastUpdated)

Last update of the dynamic connector availability information.

[`EVSEStatus`](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search")

  [status](#status)

EVSE status.

## Constructor Summary

Constructors

Constructor

  Description

  [Evse](#%3Cinit%3E())`()`

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

### id

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id

    HERE ID of the EVSE.

### cpoId

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cpoId

    The unique ID of an EVSE in the system of the CPO. This ID is unique in the system of the CPO but not necessarily globally unique. The format will differ between different CPOs. This ID is always provided.

### cpoEvseEmi3Id

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cpoEvseEmi3Id

    Identifier in Emi3 format of the EVSE within the Charge Point Operator (CPO) platform. This id is not always present. Example of ID format: `DE*ICT*E0001897`.

### status

@Nullable public [EVSEStatus](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search") status

    EVSE status.

### lastUpdated

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) lastUpdated

    Last update of the dynamic connector availability information.

### connectors

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[EVSEConnector](sdk-for-android-explore-api-reference-latestevseconnector "class in com.here.sdk.search")\> connectors

    List of connectors of this EVSE.

## Constructor Details

  - ()" class="section detail">

### Evse

public Evse()

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

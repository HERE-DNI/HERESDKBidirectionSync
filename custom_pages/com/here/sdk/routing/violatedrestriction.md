---
title: "ViolatedRestriction (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestviolatedrestriction"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ViolatedRestriction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.ViolatedRestriction
------------------------------------------------------------------------
public final class ViolatedRestriction extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`ViolatedRestriction` contains all the violated restriction details for the planned trip.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [ViolatedRestriction.Details](sdk-for-android-explore-api-reference-latestviolatedrestriction-details)

Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [cause](#cause)

Cause of the notice.

[`ViolatedRestriction.Details`](sdk-for-android-explore-api-reference-latestviolatedrestriction-details "class in com.here.sdk.routing")

  [details](#details)

The detailed information of restriction depending on the specific violation.

`boolean`

  [timeDependent](#timeDependent)

Indicates that restriction depends on time.

## Constructor Summary

Constructors

Constructor

  Description

  [ViolatedRestriction](#%3Cinit%3E(java.lang.String,boolean))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` cause, boolean timeDependent)`

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

### cause

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cause

    Cause of the notice. Human readable description of the notice, for example "Route violates vehicle restriction". It will be EN-US text only.

### timeDependent

public boolean timeDependent

    Indicates that restriction depends on time.

### details

@Nullable public [ViolatedRestriction.Details](sdk-for-android-explore-api-reference-latestviolatedrestriction-details "class in com.here.sdk.routing") details

    The detailed information of restriction depending on the specific violation. For time dependent restriction or transport mode restriction, this property will be null. For vehicle restriction, the corresponding member will be set, for example, if the vehicle violates the maximum allowed gross weight for a specific route, the max_gross_weight_in_kilograms will be set with the maximum allowed gross weight for this route.

## Constructor Details

  - (java.lang.String,boolean)" class="section detail">

### ViolatedRestriction

public ViolatedRestriction(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cause, boolean timeDependent)

    Creates a new instance.
Parameters:
    `cause` -

    Cause of the notice. Human readable description of the notice, for example "Route violates vehicle restriction". It will be EN-US text only.

    `timeDependent` -

    Indicates that restriction depends on time.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

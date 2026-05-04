---
title: "TransitSectionDetails (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttransitsectiondetails"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TransitSectionDetails

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TransitSectionDetails
------------------------------------------------------------------------
public final class TransitSectionDetails extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Gives the details of a transit section.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`Agency`](sdk-for-android-explore-api-reference-latestagency "class in com.here.sdk.routing")

  [agency](#agency)

Contains information about a particular agency.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Attribution`](sdk-for-android-explore-api-reference-latestattribution "class in com.here.sdk.routing")`>`

  [attributions](#attributions)

List of required attributions to display.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Fare`](sdk-for-android-explore-api-reference-latestfare "class in com.here.sdk.routing")`>`

  [fares](#fares)

List of tickets to pay for this section of the route.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TransitIncident`](sdk-for-android-explore-api-reference-latesttransitincident "class in com.here.sdk.routing")`>`

  [incidents](#incidents)

A list of all incidents that apply to the section.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TransitStop`](sdk-for-android-explore-api-reference-latesttransitstop "class in com.here.sdk.routing")`>`

  [intermediateStops](#intermediateStops)

All the intermediate stops between departure and destination of this section.

[`TransitTransport`](sdk-for-android-explore-api-reference-latesttransittransport "class in com.here.sdk.routing")

  [transport](#transport)

Transit transport information.

## Constructor Summary

Constructors

Constructor

  Description

  [TransitSectionDetails](#%3Cinit%3E(com.here.sdk.routing.Agency))`(`[`Agency`](sdk-for-android-explore-api-reference-latestagency "class in com.here.sdk.routing")` agency)`

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

### transport

@Nullable public [TransitTransport](sdk-for-android-explore-api-reference-latesttransittransport "class in com.here.sdk.routing") transport

    Transit transport information.

### intermediateStops

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TransitStop](sdk-for-android-explore-api-reference-latesttransitstop "class in com.here.sdk.routing")\> intermediateStops

    All the intermediate stops between departure and destination of this section.

### agency

@NonNull public [Agency](sdk-for-android-explore-api-reference-latestagency "class in com.here.sdk.routing") agency

    Contains information about a particular agency.

### attributions

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Attribution](sdk-for-android-explore-api-reference-latestattribution "class in com.here.sdk.routing")\> attributions

    List of required attributions to display.

### fares

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Fare](sdk-for-android-explore-api-reference-latestfare "class in com.here.sdk.routing")\> fares

    List of tickets to pay for this section of the route.

    **Note:** Currently, fare information is not supported and the list will be always empty.

### incidents

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TransitIncident](sdk-for-android-explore-api-reference-latesttransitincident "class in com.here.sdk.routing")\> incidents

    A list of all incidents that apply to the section.

## Constructor Details

  - (com.here.sdk.routing.Agency)" class="section detail">

### TransitSectionDetails

public TransitSectionDetails(@NonNull [Agency](sdk-for-android-explore-api-reference-latestagency "class in com.here.sdk.routing") agency)

    Creates a new instance.
Parameters:
    `agency` -

    Contains information about a particular agency.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

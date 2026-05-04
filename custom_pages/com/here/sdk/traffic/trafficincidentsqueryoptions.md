---
title: "TrafficIncidentsQueryOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficincidentsqueryoptions"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TrafficIncidentsQueryOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.traffic.TrafficIncidentsQueryOptions
------------------------------------------------------------------------
public final class TrafficIncidentsQueryOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The options to specify how incidents should be queried.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [earliestStartTime](#earliestStartTime)

The earliest start time of incidents to be queried.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TrafficIncidentImpact`](sdk-for-android-explore-api-reference-latesttrafficincidentimpact "enum class in com.here.sdk.traffic")`>`

  [impactFilter](#impactFilter)

The list of incident impacts to be queried.

[`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core")

  [languageCode](#languageCode)

The language code of the query.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [latestEndTime](#latestEndTime)

The latest end time of incidents to be queried.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TrafficIncidentType`](sdk-for-android-explore-api-reference-latesttrafficincidenttype "enum class in com.here.sdk.traffic")`>`

  [typeFilter](#typeFilter)

The list of incident types to be queried.

## Constructor Summary

Constructors

Constructor

  Description

  [TrafficIncidentsQueryOptions](#%3Cinit%3E())`()`

Creates a new instance with default values.

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

### typeFilter

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TrafficIncidentType](sdk-for-android-explore-api-reference-latesttrafficincidenttype "enum class in com.here.sdk.traffic")\> typeFilter

    The list of incident types to be queried. If the list is empty, all types will be queried.

### impactFilter

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TrafficIncidentImpact](sdk-for-android-explore-api-reference-latesttrafficincidentimpact "enum class in com.here.sdk.traffic")\> impactFilter

    The list of incident impacts to be queried. If the list is empty, all incident impacts will be queried.

### earliestStartTime

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) earliestStartTime

    The earliest start time of incidents to be queried. If the value is null filtering by the earliest start time is not applied.

### latestEndTime

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) latestEndTime

    The latest end time of incidents to be queried. If the value is null filtering by the latest end time is not applied.

### languageCode

@Nullable public [LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core") languageCode

    The language code of the query. It's the expected language of fields [`TrafficIncidentBase.getDescription()`](sdk-for-android-explore-api-reference-latesttrafficincidentbase#getDescription()) and [`TrafficIncident.getSummary()`](sdk-for-android-explore-api-reference-latesttrafficincident#getSummary()) in the relevant response. However, the language code doesn't impact on [`TrafficLocation.description`](sdk-for-android-explore-api-reference-latesttrafficlocation#description). If the language code is null or not supported then response fields are expected in the original language of the country that the incident belongs to.

## Constructor Details

  - ()" class="section detail">

### TrafficIncidentsQueryOptions

public TrafficIncidentsQueryOptions()

    Creates a new instance with default values.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

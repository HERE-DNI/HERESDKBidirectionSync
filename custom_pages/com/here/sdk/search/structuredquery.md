---
title: "StructuredQuery (API Reference)"
slug: "sdk-for-android-explore-api-reference-lateststructuredquery"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class StructuredQuery

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.StructuredQuery
------------------------------------------------------------------------
public final class StructuredQuery extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The options to specify a structured query. Only supported in `OfflineSearchEngine` (only available for the Navigate license).

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [StructuredQuery.AddressElements](sdk-for-android-explore-api-reference-lateststructuredquery-addresselements)

Defines query address elements which will be used to build address hierarchy during searches.

`static enum `

  [StructuredQuery.ResultType](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype)

Specifies expected result type.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`StructuredQuery.AddressElements`](sdk-for-android-explore-api-reference-lateststructuredquery-addresselements "class in com.here.sdk.search")

  [addressElements](#addressElements)

Query address elements to get the results from a specific geographical area.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [areaCenter](#areaCenter)

Geographic coordinates of the prioritized area center.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [query](#query)

Desired query to search.

[`StructuredQuery.ResultType`](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search")

  [resultType](#resultType)

An optional field to indicates the type of result expected.

## Constructor Summary

Constructors

Constructor

  Description

  [StructuredQuery](#%3Cinit%3E(java.lang.String,com.here.sdk.core.GeoCoordinates))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` query, `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` areaCenter)`

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

### query

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) query

    Desired query to search.

### areaCenter

@NonNull public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") areaCenter

    Geographic coordinates of the prioritized area center.

### addressElements

@NonNull public [StructuredQuery.AddressElements](sdk-for-android-explore-api-reference-lateststructuredquery-addresselements "class in com.here.sdk.search") addressElements

    Query address elements to get the results from a specific geographical area.

### resultType

@Nullable public [StructuredQuery.ResultType](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search") resultType

    An optional field to indicates the type of result expected.

## Constructor Details

  - (java.lang.String,com.here.sdk.core.GeoCoordinates)" class="section detail">

### StructuredQuery

public StructuredQuery(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) query, @NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") areaCenter)

    Creates a new instance.
Parameters:
    `query` -

    Desired query to search.

    `areaCenter` -

    Geographic coordinates of the prioritized area center.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

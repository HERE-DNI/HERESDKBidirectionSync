---
title: "TextQuery (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttextquery"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TextQuery

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.TextQuery
------------------------------------------------------------------------
public final class TextQuery extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The options to specify a text query.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [TextQuery.Area](sdk-for-android-explore-api-reference-latesttextquery-area)

Area to perform search on.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`TextQuery.Area`](sdk-for-android-explore-api-reference-latesttextquery-area "class in com.here.sdk.search")

  [area](#area)

Area which to provide the most relevant places.

[`PlaceFilter`](sdk-for-android-explore-api-reference-latestplacefilter "class in com.here.sdk.search")

  [placeFilter](#placeFilter)

The filter options to specify a place in query.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [query](#query)

Desired query to search.

## Constructor Summary

Constructors

Constructor

  Description

  [TextQuery](#%3Cinit%3E(java.lang.String,com.here.sdk.search.TextQuery.Area))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` query, `[`TextQuery.Area`](sdk-for-android-explore-api-reference-latesttextquery-area "class in com.here.sdk.search")` area)`

Constructs a TextQuery from the provided text query and geographic area.

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

### area

@NonNull public [TextQuery.Area](sdk-for-android-explore-api-reference-latesttextquery-area "class in com.here.sdk.search") area

    Area which to provide the most relevant places.

### placeFilter

@NonNull public [PlaceFilter](sdk-for-android-explore-api-reference-latestplacefilter "class in com.here.sdk.search") placeFilter

    The filter options to specify a place in query. Consists of fuel and truck options.

## Constructor Details

  - (java.lang.String,com.here.sdk.search.TextQuery.Area)" class="section detail">

### TextQuery

public TextQuery(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) query, @NonNull [TextQuery.Area](sdk-for-android-explore-api-reference-latesttextquery-area "class in com.here.sdk.search") area)

    Constructs a TextQuery from the provided text query and geographic area. For Offline Search, search in a given `GeoBox`, `GeoCircle` or `GeoCorridor` restricts the results to only POIs.
Parameters:
    `query` -

    Desired query to search.

    `area` -

    Area which to provide the most relevant places.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

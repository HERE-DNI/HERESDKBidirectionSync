---
title: "AddressQuery (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestaddressquery"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class AddressQuery

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.AddressQuery
------------------------------------------------------------------------
public final class AddressQuery extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The options to specify an address query. A [`query`](#query) can consist of parts of an address or full addresses, optionally comma separated. [`AddressQuery`](sdk-for-android-explore-api-reference-latestaddressquery "class in com.here.sdk.search") should only be used to search for parts of the address, excluding the POI name. For example, "Invalidenstraße 116, Berlin, Germany" is appropriate, whereas "HERE, Invalidenstraße 116, Berlin, Germany" is not. To be able to include the POI name, use [`TextQuery`](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search") instead. [`SearchOptions.languageCode`](sdk-for-android-explore-api-reference-latestsearchoptions#languageCode) specifies the language of the [`query`](#query) and determines the preferred language of the results.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [areaCenter](#areaCenter)

Geographical coordinates of the center around which to provide the most relevant places.

`final `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`CountryCode`](sdk-for-android-explore-api-reference-latestcountrycode "enum class in com.here.sdk.core")`>`

  [countries](#countries)

A list of countries that the query is applied in.

`final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [query](#query)

Desired address query to search.

## Constructor Summary

Constructors

Constructor

  Description

  [AddressQuery](#%3Cinit%3E(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` query)`

Constructs an AddressQuery from the provided text query.

[AddressQuery](#%3Cinit%3E(java.lang.String,com.here.sdk.core.GeoCoordinates))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` query, `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` areaCenter)`

Constructs an AddressQuery from the provided text query and geographical coordinates.

[AddressQuery](#%3Cinit%3E(java.lang.String,com.here.sdk.core.GeoCoordinates,java.util.List))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` query, `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` areaCenter, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`CountryCode`](sdk-for-android-explore-api-reference-latestcountrycode "enum class in com.here.sdk.core")`> countries)`

Constructs an AddressQuery from the provided text query, geographical coordinates and the list of countries the query is applied in.

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

@NonNull public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) query

    Desired address query to search.

### areaCenter

@Nullable public final [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") areaCenter

    Geographical coordinates of the center around which to provide the most relevant places. For Offline Search null value will result in [`SearchError.INVALID_AREA`](sdk-for-android-explore-api-reference-latestsearcherror#INVALID_AREA)

### countries

@NonNull public final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[CountryCode](sdk-for-android-explore-api-reference-latestcountrycode "enum class in com.here.sdk.core")\> countries

    A list of countries that the query is applied in. Not supported in `OfflineSearchEngine` (only available for the Navigate license).

## Constructor Details

  - (java.lang.String,com.here.sdk.core.GeoCoordinates)" class="section detail">

### AddressQuery

public AddressQuery(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) query, @NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") areaCenter)

    Constructs an AddressQuery from the provided text query and geographical coordinates.
Parameters:
    `query` -

    Desired query to search.

    `areaCenter` -

    Geographical coordinates of the center around which to provide the most relevant places.
- (java.lang.String,com.here.sdk.core.GeoCoordinates,java.util.List)" class="section detail">

### AddressQuery

public AddressQuery(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) query, @NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") areaCenter, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[CountryCode](sdk-for-android-explore-api-reference-latestcountrycode "enum class in com.here.sdk.core")\> countries)

    Constructs an AddressQuery from the provided text query, geographical coordinates and the list of countries the query is applied in.
Parameters:
    `query` -

    Desired query to search.

    `areaCenter` -

    Geographical coordinates of the center around which to provide the most relevant places.

    `countries` -

    A list of countries that the query is applied in.
- (java.lang.String)" class="section detail">

### AddressQuery

public AddressQuery(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) query)

    Constructs an AddressQuery from the provided text query. Not supported in `OfflineSearchEngine` (only available for the Navigate license).
Parameters:
    `query` -

    Desired query to search.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

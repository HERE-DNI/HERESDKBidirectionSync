---
title: "GeoPlace (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestgeoplace"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class GeoPlace

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.GeoPlace
------------------------------------------------------------------------
public final class GeoPlace extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
GeoPlace struct represents a location object: such as a country, a city, a point of interest (POI) etc. It can be used for PersonalPlace creation, in order to provide search on custom places.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`Address`](sdk-for-android-explore-api-reference-latestaddress "class in com.here.sdk.search")

  [address](#address)

Address of the place Note: Address can have default value when no data is available.

[`BusinessDetails`](sdk-for-android-explore-api-reference-latestbusinessdetails "class in com.here.sdk.search")

  [business](#business)

Business details Note: BusinessDetails can have default value when no data is available.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`>`

  [categories](#categories)

List of corresponding categories Note: This list can be empty when no data is available.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ExternalID`](sdk-for-android-explore-api-reference-latestexternalid "class in com.here.sdk.core")`>`

  [externalIDs](#externalIDs)

Allows the client to set the id in their own system.

[`LocationDetails`](sdk-for-android-explore-api-reference-latestlocationdetails "class in com.here.sdk.search")

  [location](#location)

Geographical details Note: Can be `null` when retrieved from a suggestion's place property.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [title](#title)

The localized title for the resource.

[`PlaceType`](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search")

  [type](#type)

Specifies place type.

[`WebDetails`](sdk-for-android-explore-api-reference-latestwebdetails "class in com.here.sdk.search")

  [web](#web)

Contains info and direct web links to corresponding items.

## Constructor Summary

Constructors

Constructor

  Description

  [GeoPlace](#%3Cinit%3E())`()`

Creates a new instance.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getID](#getID())`()`

Allow the client to access GeoPlace id.

`int`

  [hashCode](#hashCode())`()`

  `boolean`

  [isMyPlace](#isMyPlace())`()`

Allow the client to access info about is it my place or not.

`static `[`GeoPlace`](sdk-for-android-explore-api-reference-latestgeoplace "class in com.here.sdk.search")

  [makeMyPlace](#makeMyPlace(java.lang.String,com.here.sdk.core.GeoCoordinates))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` title, `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates)`

Creates a new instance of this class.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### title

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title

    The localized title for the resource. Note: This String can be empty when no data is available.

### externalIDs

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ExternalID](sdk-for-android-explore-api-reference-latestexternalid "class in com.here.sdk.core")\> externalIDs

    Allows the client to set the id in their own system. The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

### type

@NonNull public [PlaceType](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search") type

    Specifies place type.

### categories

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories

    List of corresponding categories Note: This list can be empty when no data is available.

### address

@NonNull public [Address](sdk-for-android-explore-api-reference-latestaddress "class in com.here.sdk.search") address

    Address of the place Note: Address can have default value when no data is available.

### location

@Nullable public [LocationDetails](sdk-for-android-explore-api-reference-latestlocationdetails "class in com.here.sdk.search") location

    Geographical details Note: Can be `null` when retrieved from a suggestion's place property.

### business

@NonNull public [BusinessDetails](sdk-for-android-explore-api-reference-latestbusinessdetails "class in com.here.sdk.search") business

    Business details Note: BusinessDetails can have default value when no data is available.

### web

@NonNull public [WebDetails](sdk-for-android-explore-api-reference-latestwebdetails "class in com.here.sdk.search") web

    Contains info and direct web links to corresponding items. Note: WebDetails can have default value when no data is available.

## Constructor Details

  - ()" class="section detail">

### GeoPlace

public GeoPlace()

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

### makeMyPlace

@NonNull public static [GeoPlace](sdk-for-android-explore-api-reference-latestgeoplace "class in com.here.sdk.search") makeMyPlace(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title, @NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates)

    Creates a new instance of this class. All other properties will keep their default value and all properties containing lists will contain empty lists.
Parameters:
    `title` -

    The title.

    `coordinates` -

    The coordinates.

    Returns:
    An instance of [`GeoPlace`](sdk-for-android-explore-api-reference-latestgeoplace "class in com.here.sdk.search").

### getID

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getID()

    Allow the client to access GeoPlace id.
Returns:
    The place id.

### isMyPlace

public boolean isMyPlace()

    Allow the client to access info about is it my place or not.
Returns:
    `True` if it is my place, `false` otherwise.

---
title: "Place (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestplace"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Place

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.search.Place
------------------------------------------------------------------------
public final class Place extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Represents a location object, such as a country, a city, a point of interest (POI) etc.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search")

  [deserialize](#deserialize(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` serializedPlace)`

Returns a [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") created from serialized string.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`>`

  [getAccessPoints](#getAccessPoints())`()`

Gets the access points to the place, such as the points on a road or in a parking lot.

[`Address`](sdk-for-android-explore-api-reference-latestaddress "class in com.here.sdk.search")

  [getAddress](#getAddress())`()`

Gets the address of the place.

[`AreaType`](sdk-for-android-explore-api-reference-latestareatype "enum class in com.here.sdk.search")

  [getAreaType](#getAreaType())`()`

Gets the area type.

[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")

  [getBoundingBox](#getBoundingBox())`()`

Gets the geographic coordinates of the bounding box containing the place.

[`Details`](sdk-for-android-explore-api-reference-latestdetails "class in com.here.sdk.search")

  [getDetails](#getDetails())`()`

Gets the place's detailed information.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [getDistanceInMeters](#getDistanceInMeters())`()`

Gets the distance from the search center to the place in meters.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [getGeoCoordinates](#getGeoCoordinates())`()`

Gets the geographic coordinates of the place.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getId](#getId())`()`

Gets the unique id of this resource.

[`PlaceType`](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search")

  [getPlaceType](#getPlaceType())`()`

Gets the place type.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getPoliticalView](#getPoliticalView())`()`

Gets the geopolitical view, defined as a three letter country code, each disputed territory has international and alternative views.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getTitle](#getTitle())`()`

Gets the localized title for the resource.

`boolean`

  [isCoordinatesInterpolated](#isCoordinatesInterpolated())`()`

Gets the flag saying whether the coordinates of the house number were interpolated or not.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [serializeCompact](#serializeCompact())`()`

Serializes [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") to persist or transfer.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### serializeCompact

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) serializeCompact()

    Serializes [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") to persist or transfer. Preserves limited amount of data:

    - [`getTitle()`](#getTitle())
    - [`getId()`](#getId())
    - [`getGeoCoordinates()`](#getGeoCoordinates())
    - [`getAccessPoints()`](#getAccessPoints())
    - [`getPlaceType()`](#getPlaceType())
    - [`getBoundingBox()`](#getBoundingBox())
    - [`Details.getPrimaryCategories()`](sdk-for-android-explore-api-reference-latestdetails#getPrimaryCategories())
    - [`Address.addressText`](sdk-for-android-explore-api-reference-latestaddress#addressText)
    - [`Address.countryCode`](sdk-for-android-explore-api-reference-latestaddress#countryCode)
Returns:
    The serialized place

### deserialize

@NonNull public static [Place](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") deserialize(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) serializedPlace) throws [PlaceSerializationException](sdk-for-android-explore-api-reference-latestplaceserializationexception "class in com.here.sdk.search")

    Returns a [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") created from serialized string.
Parameters:
    `serializedPlace` -

    The serialized place

    Returns:
    A [`Place`](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search") created from serialized string.

    Throws:
    [`PlaceSerializationException`](sdk-for-android-explore-api-reference-latestplaceserializationexception "class in com.here.sdk.search") -

    Indicates what went wrong during deserialization attempt.

### getTitle

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTitle()

    Gets the localized title for the resource.
Returns:
    The localized title for the resource.

### getId

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getId()

    Gets the unique id of this resource. It can be used to query further information.

    When returned from `OfflineSearchEngine`, `id` is valid only for `Place` objects whose `place_type` is `POI`. Otherwise, it is empty.
Returns:
    The unique id of this resource. It can be used to query further information.

### getPlaceType

@NonNull public [PlaceType](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search") getPlaceType()

    Gets the place type.
Returns:
    The place type.

### getAreaType

@Nullable public [AreaType](sdk-for-android-explore-api-reference-latestareatype "enum class in com.here.sdk.search") getAreaType()

    Gets the area type. It is available only when the [`getPlaceType()`](#getPlaceType()) is [`PlaceType.AREA`](sdk-for-android-explore-api-reference-latestplacetype#AREA).
Returns:
    The area type. It is available only when the [`getPlaceType()`](#getPlaceType()) is [`PlaceType.AREA`](sdk-for-android-explore-api-reference-latestplacetype#AREA).

### getAddress

@NonNull public [Address](sdk-for-android-explore-api-reference-latestaddress "class in com.here.sdk.search") getAddress()

    Gets the address of the place.

    Note that while `OfflineSearchEngine.suggest` and `OfflineSearchEngine.suggestByText` set all available details, `SearchEngine.suggest` and `SearchEngine.suggestByText` set only [`Address.addressText`](sdk-for-android-explore-api-reference-latestaddress#addressText). Complete address details can be obtained by searching with [`PlaceIdQuery`](sdk-for-android-explore-api-reference-latestplaceidquery "class in com.here.sdk.search").
Returns:
    The address of the place.

    Note that while `OfflineSearchEngine.suggest` and `OfflineSearchEngine.suggestByText` set all available details, `SearchEngine.suggest` and `SearchEngine.suggestByText` set only [`Address.addressText`](sdk-for-android-explore-api-reference-latestaddress#addressText). Complete address details can be obtained by searching with [`PlaceIdQuery`](sdk-for-android-explore-api-reference-latestplaceidquery "class in com.here.sdk.search").

### getDetails

@NonNull public [Details](sdk-for-android-explore-api-reference-latestdetails "class in com.here.sdk.search") getDetails()

    Gets the place's detailed information.
Returns:
    The place's detailed information.

### getGeoCoordinates

@Nullable public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") getGeoCoordinates()

    Gets the geographic coordinates of the place.

    Can be `null` when retrieved from a suggestion's place property.
Returns:
    The geographic coordinates of the place.

### isCoordinatesInterpolated

public boolean isCoordinatesInterpolated()

    Gets the flag saying whether the coordinates of the house number were interpolated or not.

    This property is valid only for house number results retrieved using online search. When false, it means [`getGeoCoordinates()`](#getGeoCoordinates()) point to an accurate position of the house. Otherwise coordinates are slightly less accurate, but are based on a highly optimized interpolation algorithm.
Returns:
    A property that says whether the coordinates of the house number were interpolated or not.

### getAccessPoints

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\> getAccessPoints()

    Gets the access points to the place, such as the points on a road or in a parking lot.

    A place can have multiple access points. For example, a large warehouse can have multiple entrances, while the center of the warehouse may not be directly reachable. Note that access points are meant to be reachable by vehicles. For routes it is recommended to navigate to one of the available access points (if any), whereas the `sideOfStreetHint` should be set to the geographic coordinates of the place. The list is empty when no access points are known or when the place is directly reachable. A place can have multiple access points. For example, a large warehouse can have multiple entrances, while the center of the warehouse may not be directly reachable. Note that access points are meant to be reachable by vehicles. For routes it is recommended to navigate to one of the available access points (if any), whereas the `sideOfStreetHint` should be set to the geographic coordinates of the place. The list is empty when no access points are known or when the place is directly reachable.
Returns:
    The access points to the place, such as the points on a road or in a parking lot.

### getBoundingBox

@Nullable public [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") getBoundingBox()

    Gets the geographic coordinates of the bounding box containing the place.
Returns:
    The geographic coordinates of the map bounding box containing the place.

### getDistanceInMeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) getDistanceInMeters()

    Gets the distance from the search center to the place in meters.
Returns:
    The distance from the search center to the place in meters.

### getPoliticalView

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPoliticalView()

    Gets the geopolitical view, defined as a three letter country code, each disputed territory has international and alternative views.

    Populated when the geopolitical view parameter is set in the [`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine") and passed to [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") on instantiation, but only if it is an alternative view. For more details refer to [`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine").
Returns:
    The geopolitical view, defined as a three letter country code, each disputed territory has international and alternative views.

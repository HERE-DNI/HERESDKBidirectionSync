---
title: "MapScene.MapPickFilter.ContentType (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class MapScene.MapPickFilter.ContentType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapScene.MapPickFilter.ContentType](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview")\>
com.here.sdk.mapview.MapScene.MapPickFilter.ContentType
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`MapScene.MapPickFilter.ContentType`](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[MapScene.MapPickFilter](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static enum MapScene.MapPickFilter.ContentType extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapScene.MapPickFilter.ContentType](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview")\>
Type of the map content to be picked.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [CUSTOM_LAYER_DATA](#CUSTOM_LAYER_DATA)

Custom user map content added using custom datasources e.g.

[MAP_CONTENT](#MAP_CONTENT)

Pickable map content currently consists of: Embedded carto POI markers that by default are available on the map. Traffic incidents that are visible when they are enabled using [`MapScene.enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#enableFeatures(java.util.Map)) with [`MapFeatures.TRAFFIC_INCIDENTS`](sdk-for-android-explore-api-reference-latestmapfeatures#TRAFFIC_INCIDENTS). Vehicle restrictions are only available for the Navigate license.

[MAP_ITEMS](#MAP_ITEMS)

Map items added through a [`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") like [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview"), [`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview"), [`MapPolygon`](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview").

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`MapScene.MapPickFilter.ContentType`](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`MapScene.MapPickFilter.ContentType`](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### MAP_ITEMS

public static final [MapScene.MapPickFilter.ContentType](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview") MAP_ITEMS

    Map items added through a [`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") like [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview"), [`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview"), [`MapPolygon`](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview").

### MAP_CONTENT

public static final [MapScene.MapPickFilter.ContentType](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview") MAP_CONTENT

    Pickable map content currently consists of:

    - Embedded carto POI markers that by default are available on the map.
    - Traffic incidents that are visible when they are enabled using [`MapScene.enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#enableFeatures(java.util.Map)) with [`MapFeatures.TRAFFIC_INCIDENTS`](sdk-for-android-explore-api-reference-latestmapfeatures#TRAFFIC_INCIDENTS).
    - Vehicle restrictions are only available for the Navigate license. Vehicle restrictions are enabled using [`MapScene.enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#enableFeatures(java.util.Map)) with `MapFeatures.VEHICLE_RESTRICTIONS`. Please note that the vehicle restriction line marking the affected street is pickable and not the restriction icon itself. Only visible POIs, traffic incidents and vehicle restrictions lines can be picked, i.e. only those categories that are not hidden and those that are not covered by any custom marker.

### CUSTOM_LAYER_DATA

public static final [MapScene.MapPickFilter.ContentType](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview") CUSTOM_LAYER_DATA

    Custom user map content added using custom datasources e.g. [`LineDataSource`](sdk-for-android-explore-api-reference-latestlinedatasource "class in com.here.sdk.mapview.datasource"), [`PolygonDataSource`](sdk-for-android-explore-api-reference-latestpolygondatasource "class in com.here.sdk.mapview.datasource") and layers.

## Method Details

### values

public static [MapScene.MapPickFilter.ContentType](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [MapScene.MapPickFilter.ContentType](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null

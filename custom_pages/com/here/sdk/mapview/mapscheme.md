---
title: "MapScheme (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapscheme"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class MapScheme

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview")\>
com.here.sdk.mapview.MapScheme
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`MapScheme`](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum MapScheme extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview")\>
Represents the preconfigured map schemes bundled with the SDK.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [HYBRID_DAY](#HYBRID_DAY)

Day version of hybrid scheme combining satellite data with vector street network, map labels and POI information.

[HYBRID_NIGHT](#HYBRID_NIGHT)

Night version of hybrid scheme combining satellite data with vector street network, map labels and POI information.

[LITE_DAY](#LITE_DAY)

The day version of lite scheme is a simplified version of the [`NORMAL_DAY`](#NORMAL_DAY), featuring fewer map elements and a more limited color palette.

[LITE_HYBRID_DAY](#LITE_HYBRID_DAY)

The day version of lite hybrid scheme is a simplified version of the [`HYBRID_DAY`](#HYBRID_DAY), featuring fewer map elements and a more limited color palette.

[LITE_HYBRID_NIGHT](#LITE_HYBRID_NIGHT)

The night version of lite hybrid scheme is a simplified version of the [`HYBRID_NIGHT`](#HYBRID_NIGHT), featuring fewer map elements and a more limited color palette.

[LITE_NIGHT](#LITE_NIGHT)

The night version of lite scheme is a simplified version of the [`NORMAL_NIGHT`](#NORMAL_NIGHT), featuring fewer map elements and a more limited color palette.

[LOGISTICS_DAY](#LOGISTICS_DAY)

The day version of the logistics map scheme catering to the needs of dispatchers, fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.

[LOGISTICS_HYBRID_DAY](#LOGISTICS_HYBRID_DAY)

The day version of the logistics hybrid map scheme catering to the needs of dispatchers, fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.

[LOGISTICS_HYBRID_NIGHT](#LOGISTICS_HYBRID_NIGHT)

The night version of the logistics hybrid map scheme catering to the needs of dispatchers, fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.

[LOGISTICS_NIGHT](#LOGISTICS_NIGHT)

The night version of the logistics map scheme catering to the needs of dispatchers, fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.

[NORMAL_DAY](#NORMAL_DAY)

Normal map for day.

[NORMAL_NIGHT](#NORMAL_NIGHT)

Normal map for night.

[ROAD_NETWORK_DAY](#ROAD_NETWORK_DAY)

The day version of a scheme highlighting roads without showing other content such as labels or buildings.

[ROAD_NETWORK_NIGHT](#ROAD_NETWORK_NIGHT)

The night version of a scheme highlighting roads without showing other content such as labels or buildings.

[SATELLITE](#SATELLITE)

Satellite imagery.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`MapScheme`](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`MapScheme`](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### NORMAL_DAY

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") NORMAL_DAY

    Normal map for day.

### NORMAL_NIGHT

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") NORMAL_NIGHT

    Normal map for night.

### SATELLITE

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") SATELLITE

    Satellite imagery.

### HYBRID_DAY

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") HYBRID_DAY

    Day version of hybrid scheme combining satellite data with vector street network, map labels and POI information.

### HYBRID_NIGHT

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") HYBRID_NIGHT

    Night version of hybrid scheme combining satellite data with vector street network, map labels and POI information.

### LITE_DAY

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") LITE_DAY

    The day version of lite scheme is a simplified version of the [`NORMAL_DAY`](#NORMAL_DAY), featuring fewer map elements and a more limited color palette.

### LITE_NIGHT

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") LITE_NIGHT

    The night version of lite scheme is a simplified version of the [`NORMAL_NIGHT`](#NORMAL_NIGHT), featuring fewer map elements and a more limited color palette.

### LITE_HYBRID_DAY

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") LITE_HYBRID_DAY

    The day version of lite hybrid scheme is a simplified version of the [`HYBRID_DAY`](#HYBRID_DAY), featuring fewer map elements and a more limited color palette.

### LITE_HYBRID_NIGHT

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") LITE_HYBRID_NIGHT

    The night version of lite hybrid scheme is a simplified version of the [`HYBRID_NIGHT`](#HYBRID_NIGHT), featuring fewer map elements and a more limited color palette.

### LOGISTICS_DAY

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") LOGISTICS_DAY

    The day version of the logistics map scheme catering to the needs of dispatchers, fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.

### LOGISTICS_NIGHT

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") LOGISTICS_NIGHT

    The night version of the logistics map scheme catering to the needs of dispatchers, fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.

### LOGISTICS_HYBRID_DAY

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") LOGISTICS_HYBRID_DAY

    The day version of the logistics hybrid map scheme catering to the needs of dispatchers, fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.

### LOGISTICS_HYBRID_NIGHT

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") LOGISTICS_HYBRID_NIGHT

    The night version of the logistics hybrid map scheme catering to the needs of dispatchers, fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.

### ROAD_NETWORK_DAY

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") ROAD_NETWORK_DAY

    The day version of a scheme highlighting roads without showing other content such as labels or buildings. It is designed for usage as an additional zoomed-in mini-maps display to help drivers to orientate during navigation and to focus on the maneuver arrows which can be highlighted on top of this map scheme.

### ROAD_NETWORK_NIGHT

public static final [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") ROAD_NETWORK_NIGHT

    The night version of a scheme highlighting roads without showing other content such as labels or buildings. It is designed for usage as an additional zoomed-in mini-maps display to help drivers to orientate during navigation and to focus on the maneuver arrows which can be highlighted on top of this map scheme.

## Method Details

### values

public static [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null

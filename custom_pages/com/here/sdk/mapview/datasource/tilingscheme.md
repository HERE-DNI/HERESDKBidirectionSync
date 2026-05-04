---
title: "TilingScheme (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttilingscheme"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class TilingScheme

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")\>
com.here.sdk.mapview.datasource.TilingScheme
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`TilingScheme`](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum TilingScheme extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")\>
List of available data tiling schemes. X axis has the origin at -180 longitude and is increasing in east direction. Y axis has the origin at max latitude and is increasing in south direction. For half quad tree schemes, only the uppper half of the tree is used.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [HALF_QUAD_TREE_EQUIRECTANGULAR](#HALF_QUAD_TREE_EQUIRECTANGULAR)

A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.

[HALF_QUAD_TREE_IDENTITY](#HALF_QUAD_TREE_IDENTITY)

A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.

[HALF_QUAD_TREE_MERCATOR](#HALF_QUAD_TREE_MERCATOR)

A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.

[QUAD_TREE_EQUIRECTANGULAR](#QUAD_TREE_EQUIRECTANGULAR)

A tiling scheme that splits each level tile into 4 equal-sized subtiles.

[QUAD_TREE_IDENTITY](#QUAD_TREE_IDENTITY)

A tiling scheme that splits each level tile into 4 equal-sized subtiles.

[QUAD_TREE_MERCATOR](#QUAD_TREE_MERCATOR)

A tiling scheme that splits each level tile into 4 equal-sized subtiles.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`TilingScheme`](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`TilingScheme`](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### HALF_QUAD_TREE_IDENTITY

public static final [TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource") HALF_QUAD_TREE_IDENTITY

    A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.

### HALF_QUAD_TREE_MERCATOR

public static final [TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource") HALF_QUAD_TREE_MERCATOR

    A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles. The coordinates of the tile's corners are transformed through the web-mercator projection.

### HALF_QUAD_TREE_EQUIRECTANGULAR

public static final [TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource") HALF_QUAD_TREE_EQUIRECTANGULAR

    A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles. The coordinates of the tile's corners are transformed through the equirectangular (plate carree) projection.

### QUAD_TREE_IDENTITY

public static final [TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource") QUAD_TREE_IDENTITY

    A tiling scheme that splits each level tile into 4 equal-sized subtiles.

### QUAD_TREE_MERCATOR

public static final [TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource") QUAD_TREE_MERCATOR

    A tiling scheme that splits each level tile into 4 equal-sized subtiles. The coordinates of the tile's corners are transformed through the web-mercator projection.

### QUAD_TREE_EQUIRECTANGULAR

public static final [TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource") QUAD_TREE_EQUIRECTANGULAR

    A tiling scheme that splits each level tile into 4 equal-sized subtiles. The coordinates of the tile's corners are transformed through the equirectangular (plate carree) projection.

## Method Details

### values

public static [TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null

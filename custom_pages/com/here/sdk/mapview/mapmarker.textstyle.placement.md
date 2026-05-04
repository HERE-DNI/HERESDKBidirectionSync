---
title: "MapMarker.TextStyle.Placement (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class MapMarker.TextStyle.Placement

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")\>
com.here.sdk.mapview.MapMarker.TextStyle.Placement
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`MapMarker.TextStyle.Placement`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[MapMarker.TextStyle](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static enum MapMarker.TextStyle.Placement extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")\>
Represents text placement with respect to the icon of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [BOTTOM](#BOTTOM)

Text placed below the bottom edge of the image's bounding rectangle.

[BOTTOM_LEFT](#BOTTOM_LEFT)

Text placed at the bottom left corner of the image's bounding rectangle.

[BOTTOM_RIGHT](#BOTTOM_RIGHT)

Text placed at the bottom right corner of the image's bounding rectangle.

[CENTER](#CENTER)

Text placed centered over the image.

[LEFT](#LEFT)

Text placed next to the left edge of the image's bounding rectangle.

[RIGHT](#RIGHT)

Text placed next to the right edge of the image's bounding rectangle.

[TOP](#TOP)

Text placed over the top edge of the image's bounding rectangle.

[TOP_LEFT](#TOP_LEFT)

Text placed at the top left corner of the image's bounding rectangle.

[TOP_RIGHT](#TOP_RIGHT)

Text placed at the top right corner of the image's bounding rectangle.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`MapMarker.TextStyle.Placement`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`MapMarker.TextStyle.Placement`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### CENTER

public static final [MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") CENTER

    Text placed centered over the image.

### TOP

public static final [MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") TOP

    Text placed over the top edge of the image's bounding rectangle.

### TOP_RIGHT

public static final [MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") TOP_RIGHT

    Text placed at the top right corner of the image's bounding rectangle.

### RIGHT

public static final [MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") RIGHT

    Text placed next to the right edge of the image's bounding rectangle.

### BOTTOM_RIGHT

public static final [MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") BOTTOM_RIGHT

    Text placed at the bottom right corner of the image's bounding rectangle.

### BOTTOM

public static final [MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") BOTTOM

    Text placed below the bottom edge of the image's bounding rectangle.

### BOTTOM_LEFT

public static final [MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") BOTTOM_LEFT

    Text placed at the bottom left corner of the image's bounding rectangle.

### LEFT

public static final [MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") LEFT

    Text placed next to the left edge of the image's bounding rectangle.

### TOP_LEFT

public static final [MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") TOP_LEFT

    Text placed at the top left corner of the image's bounding rectangle.

## Method Details

### values

public static [MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null

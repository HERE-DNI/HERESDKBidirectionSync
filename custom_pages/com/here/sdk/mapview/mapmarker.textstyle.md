---
title: "MapMarker.TextStyle (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmarker-textstyle"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapMarker.TextStyle

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapMarker.TextStyle
Enclosing class:
[MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapMarker.TextStyle extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Styling options for the text of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [MapMarker.TextStyle.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode)

Describes a reason for failing to create a [`MapMarker.TextStyle`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview").

`static final class `

  [MapMarker.TextStyle.InstantiationException](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationexception)

Thrown when a problem occurs while trying to create a [`MapMarker.TextStyle`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview") instance.

`static enum `

  [MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement)

Represents text placement with respect to the icon of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

## Constructor Summary

Constructors

Constructor

  Description

  [TextStyle](#%3Cinit%3E())`()`

Creates a default set of styling options for the text of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview") that consists of the following values: Text size: 18 pixels Text color: opaque white Text outline size: 0 pixels Text outline color: opaque black Text placement: [`MapMarker.TextStyle.Placement.BOTTOM`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement#BOTTOM)

[TextStyle](#%3Cinit%3E(double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List))`(double textSize, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` textColor, double textOutlineSize, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` textOutlineColor, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker.TextStyle.Placement`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")`> placements)`

Creates a set of styling options for the text of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

[TextStyle](#%3Cinit%3E(double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List,java.lang.String))`(double textSize, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` textColor, double textOutlineSize, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` textOutlineColor, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker.TextStyle.Placement`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")`> placements, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` fontName)`

Creates a set of styling options for the text of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getFontName](#getFontName())`()`

Gets the font name.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker.TextStyle.Placement`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")`>`

  [getPlacements](#getPlacements())`()`

Gets the possible text placements relative to the icon of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [getTextColor](#getTextColor())`()`

Gets the text color.

[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [getTextOutlineColor](#getTextOutlineColor())`()`

Gets the text outline color.

`double`

  [getTextOutlineSize](#getTextOutlineSize())`()`

Gets the text outline size in pixels.

`double`

  [getTextSize](#getTextSize())`()`

Gets the text size in pixels.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### TextStyle

public TextStyle()

    Creates a default set of styling options for the text of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview") that consists of the following values:

    - Text size: 18 pixels
    - Text color: opaque white
    - Text outline size: 0 pixels
    - Text outline color: opaque black
    - Text placement: [`MapMarker.TextStyle.Placement.BOTTOM`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement#BOTTOM)

    Once the resulting `TextStyle` is applied to a `MapMarker`, its text will be centered over its image. The font will be 18 pixels wide, colored opaque white and will have no visible outline.

  - (double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List)" class="section detail">

### TextStyle

public TextStyle(double textSize, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") textColor, double textOutlineSize, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") textOutlineColor, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")\> placements) throws [MapMarker.TextStyle.InstantiationException](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationexception "class in com.here.sdk.mapview")

    Creates a set of styling options for the text of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

    List of placements is used to specify allowed placement of text relative to the icon. When marker overlapping is allowed as set by [`MapMarker.setOverlapAllowed(boolean)`](sdk-for-android-explore-api-reference-latestmapmarker#setOverlapAllowed(boolean)), only first placement element is considered. Otherwise the placement value is chosen so that the text does not overlap with other `MapMarker` instances.

    Placement values are prioritized according to the order in which they appear in the list. Lists with duplicate entries as well as empty lists are not supported.
Parameters:
    `textSize` -

    The size of the text in pixels. Only positive values are supported.

    `textColor` -

    The text color.

    `textOutlineSize` -

    The size of the text outline in pixels. Only non-negative values are supported.

    `textOutlineColor` -

    The color of the text outline.

    `placements` -

    List of allowed placements of the text relative to the icon of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

    Throws:
    [`MapMarker.TextStyle.InstantiationException`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationexception "class in com.here.sdk.mapview") -

    In case of invalid input parameters.
- (double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List,java.lang.String)" class="section detail">

### TextStyle

public TextStyle(double textSize, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") textColor, double textOutlineSize, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") textOutlineColor, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")\> placements, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fontName) throws [MapMarker.TextStyle.InstantiationException](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationexception "class in com.here.sdk.mapview")

    Creates a set of styling options for the text of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    List of placements is used to specify allowed placement of text relative to the icon. When marker overlapping is allowed as set by [`MapMarker.setOverlapAllowed(boolean)`](sdk-for-android-explore-api-reference-latestmapmarker#setOverlapAllowed(boolean)), only first placement element is considered. Otherwise the placement value is chosen so that the text does not overlap with other `MapMarker` instances.

    Placement values are prioritized according to the order in which they appear in the list. Lists with duplicate entries as well as empty lists are not supported.
Parameters:
    `textSize` -

    The size of the text in pixels. Only positive values are supported.

    `textColor` -

    The text color.

    `textOutlineSize` -

    The size of the text outline in pixels. Only non-negative values are supported.

    `textOutlineColor` -

    The color of the text outline.

    `placements` -

    List of allowed placements of the text relative to the icon of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

    `fontName` -

    Font name, registered with `AssetsManager.registerFont`. If empty string is provided, a default font will be used.

    Throws:
    [`MapMarker.TextStyle.InstantiationException`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationexception "class in com.here.sdk.mapview") -

    In case of invalid input parameters.

## Method Details

### getFontName

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFontName()

    Gets the font name.
Returns:
    The font used in the text style.

### getTextSize

public double getTextSize()

    Gets the text size in pixels.
Returns:
    The text size in pixels.

### getTextColor

@NonNull public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") getTextColor()

    Gets the text color.
Returns:
    The text color.

### getTextOutlineSize

public double getTextOutlineSize()

    Gets the text outline size in pixels.
Returns:
    The text outline size in pixels.

### getTextOutlineColor

@NonNull public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") getTextOutlineColor()

    Gets the text outline color.
Returns:
    The text outline color.

### getPlacements

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")\> getPlacements()

    Gets the possible text placements relative to the icon of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").
Returns:
    List of possible text placements relative to the icon of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

---
title: "MapPolyline.DashImageRepresentation (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmappolyline-dashimagerepresentation"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapPolyline.DashImageRepresentation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
[com.here.sdk.mapview.MapItemRepresentation](sdk-for-android-explore-api-reference-latestmapitemrepresentation "class in com.here.sdk.mapview")
[com.here.sdk.mapview.MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")
com.here.sdk.mapview.MapPolyline.DashImageRepresentation
Enclosing class:
[MapPolyline](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapPolyline.DashImageRepresentation extends [MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")
Represents a dash pattern for the map polyline consisting of images rendered with certain gaps from each other.

This dash pattern representation consists only of images rendered at certain points along the polyline. For rendering them without any distortions, polyline gets sliced into series of straight segments that are multiple of sum of dash and gap lengths. For this reason, the new polyline geometry might not align fully with original geometry.

The [`getDashImage()`](#getDashImage()) is stretched according to [`getDashLength()`](#getDashLength()) and [`getDashWidth()`](#getDashWidth()), with image's width matched to `dashLength` and image's height matched to `dashWidth`. The image is oriented so that its bottom is on the left-hand side between vertices `n` and `n+1`.

The spacing between images is specified by [`getGapLength()`](#getGapLength()).

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

## Nested classes/interfaces inherited from class com.here.sdk.mapview.[MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")

  [`MapPolyline.Representation.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationerrorcode "enum class in com.here.sdk.mapview"), [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

## Constructor Summary

Constructors

Constructor

  Description

  [DashImageRepresentation](#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage))`(`[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` dashLength, `[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` dashWidth, `[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")` image)`

Creates a uniform dash pattern in which the length of a gap is the same as the length of a dash.

[DashImageRepresentation](#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage))`(`[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` dashLength, `[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` gapLength, `[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")` dashWidth, `[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")` image)`

Creates a simple dash pattern in which the lengths of a dash and gap can be different.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")

  [getDashImage](#getDashImage())`()`

Gets the image that is rendered in place of dash space.

[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")

  [getDashLength](#getDashLength())`()`

Gets the map measure dependent length of a dash, to which image width is stretched.

[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")

  [getDashWidth](#getDashWidth())`()`

Gets the map measure dependent width of a dash, to which image height is stretched.

[`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")

  [getGapLength](#getGapLength())`()`

Gets the map measure dependent length of a gap between dash images.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage)" class="section detail">

### DashImageRepresentation

public DashImageRepresentation(@NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") dashLength, @NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") dashWidth, @NonNull [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") image) throws [MapPolyline.Representation.InstantiationException](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    Creates a uniform dash pattern in which the length of a gap is the same as the length of a dash. Dashes are rendered as image.

    This allows for patterns like `' — — — —'` or `' —— —— ——'`.

    For [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") supplied for `dashLength` and `dashWidth`, only [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) is supported for [`MapMeasureDependentRenderSize.measureKind`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize#measureKind) and only [`RenderSize.Unit.METERS`](sdk-for-android-explore-api-reference-latestrendersize-unit#METERS) is supported for [`MapMeasureDependentRenderSize.sizeUnit`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize#sizeUnit).

    Only map measure values in range \[3-19\] are supported.

    The value of the keys in [`MapMeasureDependentRenderSize.sizes`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize#sizes) is truncated to integer values, hence only a single value can be provided per zoom level.

    The values are interpolated linearly between zoom levels.
Parameters:
    `dashLength` -

    The map measure dependent length of a dash, to which image width is stretched.

    `dashWidth` -

    The map measure dependent width of a dash, to which image height is stretched.

    `image` -

    Image to be rendered in place of dash space. It is stretched to match `dashWidth` and `dashLength`.

    Throws:
    [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview") -

    In case of invalid input parameters.
- (com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage)" class="section detail">

### DashImageRepresentation

public DashImageRepresentation(@NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") dashLength, @NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") gapLength, @NonNull [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") dashWidth, @NonNull [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") image) throws [MapPolyline.Representation.InstantiationException](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    Creates a simple dash pattern in which the lengths of a dash and gap can be different. Dashes are rendered as image.

    This allows for patterns like `' — — — —'` or `' ——— ——— ———'`.

    For [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") supplied for `dashLength`, `gapLength` and `dashWidth`, only [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) is supported for [`MapMeasureDependentRenderSize.measureKind`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize#measureKind) and only [`RenderSize.Unit.METERS`](sdk-for-android-explore-api-reference-latestrendersize-unit#METERS) is supported for [`MapMeasureDependentRenderSize.sizeUnit`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize#sizeUnit).

    Only map measure values in range \[3-19\] are supported.

    The value of the keys in [`MapMeasureDependentRenderSize.sizes`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize#sizes) is truncated to integer values, hence only a single value can be provided per zoom level.

    The values are interpolated linearly between zoom levels.
Parameters:
    `dashLength` -

    The map measure dependent length of a dash, to which image width is stretched.

    `gapLength` -

    The map measure dependent length of a gap between dash images.

    `dashWidth` -

    The map measure dependent width of a dash, to which image height is stretched.

    `image` -

    Image to be rendered in place of dash space. It is stretched to match `dashWidth` and `dashLength`.

    Throws:
    [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview") -

    In case of invalid input parameters.

## Method Details

### getDashImage

@NonNull public [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") getDashImage()

    Gets the image that is rendered in place of dash space.

    It is stretched to fill whole polyline width and length of each dash.
Returns:
    Image to be rendered in place of dash space.

### getDashLength

@NonNull public [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") getDashLength()

    Gets the map measure dependent length of a dash, to which image width is stretched.
Returns:
    The map measure dependent length of a dash, to which image width is stretched.

### getGapLength

@NonNull public [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") getGapLength()

    Gets the map measure dependent length of a gap between dash images.
Returns:
    The map measure dependent length of a gap between dash images.

### getDashWidth

@NonNull public [MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview") getDashWidth()

    Gets the map measure dependent width of a dash, to which image height is stretched.
Returns:
    The map measure dependent width of a dash, to which image height is stretched.

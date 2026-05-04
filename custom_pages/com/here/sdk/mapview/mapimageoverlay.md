---
title: "MapImageOverlay (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapimageoverlay"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapImageOverlay

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapImageOverlay
------------------------------------------------------------------------
public final class MapImageOverlay extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
`MapImageOverlay` is used to draw images over the map, at a view coordinate inside the map viewport.

The image to be displayed is represented by a [`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") object. By default, the overlay is centered on the given view coordinate.

The resulting viewport area covered by the overlay is computed out of the overlay's view coordinate, the anchor point and the image size. The overlay subareas that fall outside of the map viewport get clipped.

To display the map overlay, it needs to be added to the scene using [`MapScene.addMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)`](sdk-for-android-explore-api-reference-latestmapscene#addMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)). To stop displaying it, remove it from the scene using [`MapScene.removeMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)`](sdk-for-android-explore-api-reference-latestmapscene#removeMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)).

## Constructor Summary

Constructors

Constructor

  Description

  [MapImageOverlay](#%3Cinit%3E(com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage))`(`[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` viewCoordinates, `[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")` image)`

Creates an instance of an overlay at given view coordinates, represented by specified image.

[MapImageOverlay](#%3Cinit%3E(com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D))`(`[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` viewCoordinates, `[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")` image, `[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` anchor)`

Creates an instance of an overlay at given view coordinates, represented by specified image, with anchor point specifying how the image is positioned relative to the overlay's view coordinates.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")

  [getAnchor](#getAnchor())`()`

Gets current anchor point for the overlay image.

`int`

  [getDrawOrder](#getDrawOrder())`()`

Gets draw order of this `MapImageOverlay`.

[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")

  [getImage](#getImage())`()`

Gets currently used map image.

[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")

  [getViewCoordinates](#getViewCoordinates())`()`

Gets the view point in pixels on the map viewport where the overlay is drawn.

`void`

  [setAnchor](#setAnchor(com.here.sdk.core.Anchor2D))`(`[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` value)`

Sets anchor point of the overlay image which specifies the position offset relative to the overlay's view coordinates.

`void`

  [setDrawOrder](#setDrawOrder(int))`(int value)`

Sets draw order of this `MapImageOverlay`.

`void`

  [setImage](#setImage(com.here.sdk.mapview.MapImage))`(`[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")` value)`

Sets the image overlayed on map.

`void`

  [setViewCoordinates](#setViewCoordinates(com.here.sdk.core.Point2D))`(`[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` value)`

Sets the view point in pixels on the map viewport where the overlay is drawn.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage)" class="section detail">

### MapImageOverlay

public MapImageOverlay(@NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") viewCoordinates, @NonNull [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") image)

    Creates an instance of an overlay at given view coordinates, represented by specified image.
Parameters:
    `viewCoordinates` -

    The overlay's view coordinates in pixels.

    `image` -

    The image to draw on the map.
- (com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D)" class="section detail">

### MapImageOverlay

public MapImageOverlay(@NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") viewCoordinates, @NonNull [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") image, @NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") anchor)

    Creates an instance of an overlay at given view coordinates, represented by specified image, with anchor point specifying how the image is positioned relative to the overlay's view coordinates.

    The anchor is a way of specifying position offset relative to image's dimensions on the view. For example, (0, 0) places the top-left corner of the image at the overlay's view coordinates. (1, 1) would place the bottom-right corner of the image at the overlay's view coordinates. (0.5, 0.5) which is the default value would center the image at the overlay's view coordinates.

    Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image centered horizontally with its bottom edge above the overlay's view coordinates at the distance in pixels that is equal to the height of the image.
Parameters:
    `viewCoordinates` -

    The overlay's view coordinates in pixels.

    `image` -

    The image to draw on the map.

    `anchor` -

    The anchor point for the overlay image which specifies the position offset relative to the overlay's view coordinates.

## Method Details

### getViewCoordinates

@NonNull public [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") getViewCoordinates()

    Gets the view point in pixels on the map viewport where the overlay is drawn.
Returns:
    The view point in pixels on the map viewport where the map overlay is drawn.

### setViewCoordinates

public void setViewCoordinates(@NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") value)

    Sets the view point in pixels on the map viewport where the overlay is drawn.
Parameters:
    `value` -

    The view point in pixels on the map viewport where the map overlay is drawn.

### getDrawOrder

public int getDrawOrder()

    Gets draw order of this `MapImageOverlay`. The default value is 0.
Returns:
    Draw order of this `MapImageOverlay`.

### setDrawOrder

public void setDrawOrder(int value)

    Sets draw order of this `MapImageOverlay`.

    Overlays with higher draw order value are drawn on top of overlays with lower draw order.

    In case multiple overlays have the same draw order value then the order in which they were added to the scene matters. Last added overlay is drawn on top.

    Allowed range is \[0, 1023\]. Values outside this range will be clamped.
Parameters:
    `value` -

    Draw order of this `MapImageOverlay`.

### getImage

@NonNull public [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") getImage()

    Gets currently used map image.
Returns:
    Image overlayed on the map.

### setImage

public void setImage(@NonNull [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") value)

    Sets the image overlayed on map.
Parameters:
    `value` -

    Image overlayed on the map.

### getAnchor

@NonNull public [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") getAnchor()

    Gets current anchor point for the overlay image.
Returns:
    The anchor point for the overlay image which specifies the position offset relative to the overlay's view coordinates.

### setAnchor

public void setAnchor(@NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") value)

    Sets anchor point of the overlay image which specifies the position offset relative to the overlay's view coordinates.

    For example, (0, 0) places the top-left corner of the image at the overlay's view coordinates. (1, 1) would place the bottom-right corner of the image at the overlay's view coordinates. (0.5, 0.5) which is the default value would center the image at the overlay's view coordinates.

    Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image centered horizontally with its bottom edge above the overlay's view coordinates at the distance in pixels that is equal to the height of the image.
Parameters:
    `value` -

    The anchor point for the overlay image which specifies the position offset relative to the overlay's view coordinates.

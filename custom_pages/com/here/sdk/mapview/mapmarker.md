---
title: "MapMarker (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmarker"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapMarker

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapMarker
------------------------------------------------------------------------
public final class MapMarker extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
`MapMarker` is used to draw images on the map, for example to mark a specific location. By default, the marker is centered on the given geographic coordinates. Markers keep their size regardless of the current zoom level of the map view.

The image to be displayed is represented by [`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") object. For performance reasons, it is highly recommended to reuse a single instance of the image when creating multiple identical markers.

To display the map marker, it needs to be added to the scene using [`MapScene.addMapMarker(com.here.sdk.mapview.MapMarker)`](sdk-for-android-explore-api-reference-latestmapscene#addMapMarker(com.here.sdk.mapview.MapMarker)). To stop displaying it, remove it from the scene using [`MapScene.removeMapMarker(com.here.sdk.mapview.MapMarker)`](sdk-for-android-explore-api-reference-latestmapscene#removeMapMarker(com.here.sdk.mapview.MapMarker)).

The display of a map marker is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects map markers which are visually large and cover a sizeable part of the viewport.

**Note:** Due to technical limitations using the MapMarkers API to add a very large number of markers (several thousands, especially 10000+) is not recommended. Adding this many markers will have a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation the following approach can be used: Register to map camera updates using [`MapCamera.addListener(com.here.sdk.mapview.MapCameraListener)`](sdk-for-android-explore-api-reference-latestmapcamera#addListener(com.here.sdk.mapview.MapCameraListener)). Query the bounding box of the camera viewport using [`MapCamera.getBoundingBox()`](sdk-for-android-explore-api-reference-latestmapcamera#getBoundingBox()) (it may be extended) and then use the method [`GeoBox.contains(GeoCoordinates)`](sdk-for-android-explore-api-reference-latestgeobox#contains(com.here.sdk.core.GeoCoordinates)) in combination with [`MapCamera.State.distanceToTargetInMeters`](sdk-for-android-explore-api-reference-latestmapcamera-state#distanceToTargetInMeters) to determine which MapMarkers are actually visible to the user in the current camera viewport and thus need to be added to the map.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [MapMarker.TextStyle](sdk-for-android-explore-api-reference-latestmapmarker-textstyle)

Styling options for the text of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").

## Constructor Summary

Constructors

Constructor

  Description

  [MapMarker](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates, `[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")` image)`

Creates an instance of a marker at given coordinates, represented by specified image.

[MapMarker](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates, `[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")` image, `[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` anchor)`

Creates an instance of a marker at given coordinates, represented by specified image, with anchor point specifying how the image is positioned relative to the marker's coordinates.

[MapMarker](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,java.lang.String))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates, `[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")` image, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` text)`

Creates a `MapMarker` instance at given coordinates with specified image and text and a default text style.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [cancelAnimation](#cancelAnimation(com.here.sdk.animation.MapMarkerAnimation))`(`[`MapMarkerAnimation`](sdk-for-android-explore-api-reference-latestmapmarkeranimation "class in com.here.sdk.animation")` animation)`

Cancels single ongoing animation.

[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")

  [getAnchor](#getAnchor())`()`

Gets current anchor point for the marker image.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [getCoordinates](#getCoordinates())`()`

Gets the point on the map where the marker is drawn.

`int`

  [getDrawOrder](#getDrawOrder())`()`

Gets draw order of this marker relative to other markers.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [getFadeDuration](#getFadeDuration())`()`

Gets the current duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.

[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")

  [getImage](#getImage())`()`

Gets currently used map image.

[`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core")

  [getMetadata](#getMetadata())`()`

Gets the Metadata instance attached to this marker.

`double`

  [getOpacity](#getOpacity())`()`

Gets the current opacity of the marker image.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getText](#getText())`()`

Gets the text drawn on the map by the `MapMarker`.

[`MapMarker.TextStyle`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview")

  [getTextStyle](#getTextStyle())`()`

Gets a copy of the `TextStyle` currently in use by the `MapMarker`.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMeasureRange`](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")`>`

  [getVisibilityRanges](#getVisibilityRanges())`()`

Gets the list of visibility ranges.

`boolean`

  [isOverlapAllowed](#isOverlapAllowed())`()`

Returns `true` if the marker allows overlap with other markers, `false` otherwise.

`boolean`

  [isTextOptional](#isTextOptional())`()`

Returns `true` if the marker allows text to be hidden, `false` otherwise.

`void`

  [setAnchor](#setAnchor(com.here.sdk.core.Anchor2D))`(`[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` value)`

Sets anchor point of the marker image which specifies the position offset relative to the marker's coordinates.

`void`

  [setCoordinates](#setCoordinates(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` value)`

Sets the point on the map where the marker is drawn.

`void`

  [setDrawOrder](#setDrawOrder(int))`(int value)`

Sets draw order of this marker relative to other markers.

`void`

  [setFadeDuration](#setFadeDuration(com.here.time.Duration))`(`[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` value)`

Sets duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.

`void`

  [setImage](#setImage(com.here.sdk.mapview.MapImage))`(`[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")` value)`

Sets map image used to represent the marker on screen.

`void`

  [setMetadata](#setMetadata(com.here.sdk.core.Metadata))`(`[`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core")` value)`

Sets the Metadata instance attached to this marker.

`void`

  [setOpacity](#setOpacity(double))`(double value)`

Sets the opacity of the marker image.

`void`

  [setOverlapAllowed](#setOverlapAllowed(boolean))`(boolean value)`

Sets whether the marker is allowed to overlap with other markers.

`void`

  [setText](#setText(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` value)`

Sets the text to be drawn on the map by the `MapMarker`.

`void`

  [setTextOptional](#setTextOptional(boolean))`(boolean value)`

Sets whether the marker is allowed to appear without text.

`void`

  [setTextStyle](#setTextStyle(com.here.sdk.mapview.MapMarker.TextStyle))`(`[`MapMarker.TextStyle`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview")` value)`

Sets the `TextStyle` to be used by the `MapMarker`.

`void`

  [setVisibilityRanges](#setVisibilityRanges(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMeasureRange`](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")`> value)`

Sets visibility ranges for this map marker.

`void`

  [startAnimation](#startAnimation(com.here.sdk.animation.MapMarkerAnimation,com.here.sdk.animation.AnimationListener))`(`[`MapMarkerAnimation`](sdk-for-android-explore-api-reference-latestmapmarkeranimation "class in com.here.sdk.animation")` animation, `[`AnimationListener`](sdk-for-android-explore-api-reference-latestanimationlistener "interface in com.here.sdk.animation")` animationListener)`

Starts animation of this map marker according to provided [`MapMarkerAnimation`](sdk-for-android-explore-api-reference-latestmapmarkeranimation "class in com.here.sdk.animation").

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage)" class="section detail">

### MapMarker

public MapMarker(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates, @NonNull [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") image)

    Creates an instance of a marker at given coordinates, represented by specified image.

    The altitude component of the coordinates is ignored.
Parameters:
    `coordinates` -

    The marker's geographical coordinates.

    `image` -

    The image to draw on the map.
- (com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,java.lang.String)" class="section detail">

### MapMarker

public MapMarker(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates, @NonNull [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") image, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)

    Creates a `MapMarker` instance at given coordinates with specified image and text and a default text style.

    The altitude component of the coordinates is ignored.
Parameters:
    `coordinates` -

    The marker's geographical coordinates.

    `image` -

    The image to draw on the map.

    `text` -

    The text to draw on the map.
- (com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D)" class="section detail">

### MapMarker

public MapMarker(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates, @NonNull [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") image, @NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") anchor)

    Creates an instance of a marker at given coordinates, represented by specified image, with anchor point specifying how the image is positioned relative to the marker's coordinates.

    The anchor is a way of specifying position offset relative to image's dimensions on the screen. For example, (0, 0) places the top-left corner of the image at the marker's coordinates. (1, 1) would place the bottom-right corner of the image at the marker's coordinates. (0.5, 0.5) which is the default value would center the image at the marker's coordinates. Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image centered horizontally with its bottom edge above the marker's coordinates at the distance in pixels that is equal to the height of the image.
Parameters:
    `coordinates` -

    The marker's geographical coordinates.

    `image` -

    The image to draw on the map.

    `anchor` -

    The anchor point for the marker image which specifies the position offset relative to the marker's coordinates.

## Method Details

### startAnimation

public void startAnimation(@NonNull [MapMarkerAnimation](sdk-for-android-explore-api-reference-latestmapmarkeranimation "class in com.here.sdk.animation") animation, @Nullable [AnimationListener](sdk-for-android-explore-api-reference-latestanimationlistener "interface in com.here.sdk.animation") animationListener)

    Starts animation of this map marker according to provided [`MapMarkerAnimation`](sdk-for-android-explore-api-reference-latestmapmarkeranimation "class in com.here.sdk.animation").

    The `MapMarkerAnimation` may be shared between multiple instances of `MapMarker`.

    Starting animation on one map marker does not influence any ongoing animations on other map markers. Any ongoing animation of this marker instance will get cancelled.
Parameters:
    `animation` -

    The animation to start, may be used for multiple different map markers.

    `animationListener` -

    The listener to receive notifications about animation start, completion or cancellation.

### cancelAnimation

public void cancelAnimation(@NonNull [MapMarkerAnimation](sdk-for-android-explore-api-reference-latestmapmarkeranimation "class in com.here.sdk.animation") animation)

    Cancels single ongoing animation.

    Does nothing if animation was not started for this map marker.

    Does not cancel other animations if the same [`MapMarkerAnimation`](sdk-for-android-explore-api-reference-latestmapmarkeranimation "class in com.here.sdk.animation") object was applied to multiple `MapMarker`s.
Parameters:
    `animation` -

    The animation to cancel.

### getCoordinates

@NonNull public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") getCoordinates()

    Gets the point on the map where the marker is drawn.
Returns:
    The point on the map where the map marker is drawn.

### setCoordinates

public void setCoordinates(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") value)

    Sets the point on the map where the marker is drawn. The altitude component of the coordinates is ignored.
Parameters:
    `value` -

    The point on the map where the map marker is drawn.

### getMetadata

@Nullable public [Metadata](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") getMetadata()

    Gets the Metadata instance attached to this marker. This will be `null` if nothing has been attached before.
Returns:
    The Metadata instance attached to this marker, see [`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core").

### setMetadata

public void setMetadata(@Nullable [Metadata](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") value)

    Sets the Metadata instance attached to this marker.
Parameters:
    `value` -

    The Metadata instance attached to this marker, see [`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core").

### isOverlapAllowed

public boolean isOverlapAllowed()

    Returns `true` if the marker allows overlap with other markers, `false` otherwise. Defaults to `true`.
Returns:
    Determines whether or not the marker can overlap other markers.

### setOverlapAllowed

public void setOverlapAllowed(boolean value)

    Sets whether the marker is allowed to overlap with other markers.

    If `false`, it will disappear the moment it overlaps another marker that has a higher visibility priority. A marker that allows overlap will always be drawn. Among markers that don't allow overlap, the one with the highest draw order has priority. Marker that is hidden due to overlapping with other markers is not pickable.
Parameters:
    `value` -

    Determines whether or not the marker can overlap other markers.

### isTextOptional

public boolean isTextOptional()

    Returns `true` if the marker allows text to be hidden, `false` otherwise. Defaults to `false`.
Returns:
    Determines if the marker can be displayed with icon and without text.

### setTextOptional

public void setTextOptional(boolean value)

    Sets whether the marker is allowed to appear without text.

    Controls whenever `MapMarker` can be shown as icon only when [`isOverlapAllowed()`](#isOverlapAllowed()) is `false`, has no effect otherwise. If `false` then the `MapMarker` will not appear when icon or text are blocked by other labels. If `true`, icon will appear even if the text part is blocked by other labels.
Parameters:
    `value` -

    Determines if the marker can be displayed with icon and without text.

### getDrawOrder

public int getDrawOrder()

    Gets draw order of this marker relative to other markers. The default value is 0.
Returns:
    The draw order of this marker relative to other markers.

### setDrawOrder

public void setDrawOrder(int value)

    Sets draw order of this marker relative to other markers.

    Markers with higher draw order value are drawn on top of markers with lower draw order. In case multiple markers have the same draw order value then the order in which they were added to the scene matters. Last added marker is drawn on top.

    Allowed range is \[0, 1023\]. Values outside this range will be clamped. The default value is 0.
Parameters:
    `value` -

    The draw order of this marker relative to other markers.

### getImage

@NonNull public [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") getImage()

    Gets currently used map image.
Returns:
    Image representing the marker on the screen.

### setImage

public void setImage(@NonNull [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") value)

    Sets map image used to represent the marker on screen.
Parameters:
    `value` -

    Image representing the marker on the screen.

### getAnchor

@NonNull public [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") getAnchor()

    Gets current anchor point for the marker image.
Returns:
    The anchor point for the marker image which specifies the position offset relative to the marker's coordinates.

### setAnchor

public void setAnchor(@NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") value)

    Sets anchor point of the marker image which specifies the position offset relative to the marker's coordinates.

    For example, (0, 0) places the top-left corner of the image at the marker's coordinates. (1, 1) would place the bottom-right corner of the image at the marker's coordinates. (0.5, 0.5) which is the default value would center the image at the marker's coordinates. Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image centered horizontally with its bottom edge above the marker's coordinates at the distance in pixels that is equal to the height of the image.
Parameters:
    `value` -

    The anchor point for the marker image which specifies the position offset relative to the marker's coordinates.

### getOpacity

public double getOpacity()

    Gets the current opacity of the marker image. Value is in the range of \[0.0, 1.0\]. Default value is 1.0.
Returns:
    Opacity, the factor applied to the alpha channel of the marker image.

### setOpacity

public void setOpacity(double value)

    Sets the opacity of the marker image.

    Provided value is clamped to the range of \[0.0, 1.0\]. Default value is 1.0, which means marker is displayed with the default opacity of the image.

    Markers with opacity value set to 0.0 are still on the map and are considered for picking.
Parameters:
    `value` -

    Opacity, the factor applied to the alpha channel of the marker image.

### getFadeDuration

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") getFadeDuration()

    Gets the current duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.
Returns:
    Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.

### setFadeDuration

public void setFadeDuration(@NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") value)

    Sets duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.

    Provided value is clamped in range \[0.0, 10.0\] seconds. Default value is 0 seconds which means the effect is disabled and marker is added/removed immediately without any animation. Fade-in effect is also applied when marker leaves and then re-enters screen area.

    Change to this property is made asynchronously and is not guaranteed to take effect on the next rendered frame. In particular, changing fade duration and removing the marker immediately after may result in the new value being ignored for this removal.
Parameters:
    `value` -

    Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.

### getText

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getText()

    Gets the text drawn on the map by the `MapMarker`.
Returns:
    The text to be drawn on the map along with the image of the `MapMarker`.

### setText

public void setText(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)

    Sets the text to be drawn on the map by the `MapMarker`.
Parameters:
    `value` -

    The text to be drawn on the map along with the image of the `MapMarker`.

### getTextStyle

@NonNull public [MapMarker.TextStyle](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview") getTextStyle()

    Gets a copy of the `TextStyle` currently in use by the `MapMarker`.
Returns:
    The `TextStyle` applied to the text of the `MapMarker`.

### setTextStyle

public void setTextStyle(@NonNull [MapMarker.TextStyle](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview") value)

    Sets the `TextStyle` to be used by the `MapMarker`.
Parameters:
    `value` -

    The `TextStyle` applied to the text of the `MapMarker`.

### getVisibilityRanges

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")\> getVisibilityRanges()

    Gets the list of visibility ranges. The map marker is visible only inside these map measure ranges. When empty (the default), the map marker is visible without map measure restrictions.
Returns:
    The list of visibility ranges. The map marker is visible only inside these map measure ranges.

### setVisibilityRanges

public void setVisibilityRanges(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")\> value)

    Sets visibility ranges for this map marker.

    A range is half open - \[minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range. The map marker is visible only inside these map measure ranges.

    When empty (the default), the map marker is visible without map measure restrictions. Only `MapMeasureRange`(s) of [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) type are supported. `MapMeasureRange`(s) of other unsupported types will be ignored.
Parameters:
    `value` -

    The list of visibility ranges. The map marker is visible only inside these map measure ranges.

---
title: "MapMarker3D (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmarker3d"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapMarker3D

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapMarker3D
------------------------------------------------------------------------
public final class MapMarker3D extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Represents a 3D shape drawn on the map at specified geodetic coordinates.

It can have a solid color or be textured, depending on the data from [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview").

By default, a 3D marker is drawn on top of all map content, including 3D map elements like extruded buildings or 3D landmarks. This can be changed by enabling depth check using [`setDepthCheckEnabled(boolean)`](#setDepthCheckEnabled(boolean)).

The display of a 3D marker is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects a 3D marker that is visually large and covers a sizeable part of the viewport.

# Sizing and scaling

Two aspects determine how big the `MapMarker3D` will be on the screen and how will it behave when the map is zoomed in and out.

The first, and most impactful is [`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview"), which specifies how the vertex coordinates of the 3D model are interpreted. Most importantly, it specifies whether the 3D model is placed in world or screen coordinate space.

[`RenderSize.Unit.METERS`](sdk-for-android-explore-api-reference-latestrendersize-unit#METERS) will make the 3D model use world coordinate space, meaning that it will change size together with the map when it is zoomed in and out.

[`RenderSize.Unit.PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#PIXELS) makes the 3D model use screen coordinate space, meaning that it will have constant size on the screen regardless of how the map zoom changes. So a simple 10 by 10 (in model space) rectangle will have a size of 10 by 10 pixels on the screen.

[`RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#DENSITY_INDEPENDENT_PIXELS) is similar to pixels, but the resulting size will take into account the pixel density of the display, meaning that physical size on the screen will be approximately the same regardless of the size or resolution of the display.

The second aspect that determines size of `MapMarker3D` is scale. It can be specified at construction time and can be changed later at any time using [`setScale(double)`](#setScale(double)).

# Modifying at runtime

A 3D marker can be moved around a map by updating its coordinates using [`setCoordinates(com.here.sdk.core.GeoCoordinates)`](#setCoordinates(com.here.sdk.core.GeoCoordinates)).

Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.

Its orientation is specified by bearing, pitch and roll and can be changed by using [`setBearing(double)`](#setBearing(double)), [`setPitch(double)`](#setPitch(double)) and [`setRoll(double)`](#setRoll(double)).

# Flat marker

A flat marker is a special case of a 3D marker, where the 3D shape being drawn is a simple textured rectangle. In essence it's an image drawn "on the ground". Such 3D marker can be conveniently created using [`MapMarker3D(GeoCoordinates, MapImage, double, RenderSize.Unit)`](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,double,com.here.sdk.mapview.RenderSize.Unit)) constructor. Of course, once created, it can be rotated to face any direction.

## Constructor Summary

Constructors

Constructor

  Description

  [MapMarker3D](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,double,com.here.sdk.mapview.RenderSize.Unit))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` at, `[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")` image, double scale, `[`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview")` unit)`

Creates a flat marker from provided map image.

[MapMarker3D](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` at, `[`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview")` model)`

Creates an instance of a 3D marker.

[MapMarker3D](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` at, `[`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview")` model, double scale)`

Creates an instance of a 3D marker with scale factor.

[MapMarker3D](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.RenderSize.Unit))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` at, `[`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview")` model, double scale, `[`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview")` unit)`

Creates a new 3D marker at given world coordinates, using the supplied 3D model.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `double`

  [getBearing](#getBearing())`()`

Gets the bearing of the 3D model in degrees.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [getCoordinates](#getCoordinates())`()`

Gets the 3D marker's position on the map corresponding to the origin of the 3D marker model coordinate system.

[`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core")

  [getMetadata](#getMetadata())`()`

Gets the [`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") instance attached to this 3D marker.

`double`

  [getOpacity](#getOpacity())`()`

Returns an opacity factor which specifies the translucency of a 3D map marker.

`double`

  [getPitch](#getPitch())`()`

Gets the pitch of the 3D model in degrees.

`double`

  [getRoll](#getRoll())`()`

Gets the roll of the 3D model in degrees.

`double`

  [getScale](#getScale())`()`

Gets the scale factor applied to the 3D model before rendering.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMeasureRange`](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")`>`

  [getVisibilityRanges](#getVisibilityRanges())`()`

Gets the list of visibility ranges.

`boolean`

  [isDepthCheckEnabled](#isDepthCheckEnabled())`()`

Returns `true` if depth check is enabled.

`boolean`

  [isRenderInternalsEnabled](#isRenderInternalsEnabled())`()`

Returns a flag indicating whether to render internal geometry of a 3D marker occluded by its front facing polygons.

`void`

  [setBearing](#setBearing(double))`(double value)`

Sets the bearing of the 3D model in degrees.

`void`

  [setCoordinates](#setCoordinates(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` value)`

Sets the 3D marker's position on the map corresponding to the origin of the 3D marker model coordinate system.

`void`

  [setDepthCheckEnabled](#setDepthCheckEnabled(boolean))`(boolean value)`

Set whether the depth of the 3D marker's vertices is considered during rendering.

`void`

  [setMetadata](#setMetadata(com.here.sdk.core.Metadata))`(`[`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core")` value)`

Sets the [`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") instance attached to this 3D marker.

`void`

  [setOpacity](#setOpacity(double))`(double value)`

Sets an opacity factor which specifies the translucency of a 3D map marker.

`void`

  [setPitch](#setPitch(double))`(double value)`

Sets the pitch of the 3D model in degrees.

`void`

  [setRenderInternalsEnabled](#setRenderInternalsEnabled(boolean))`(boolean value)`

Sets a flag indicating whether to render internal geometry of a 3D marker occluded by its front facing polygons.

`void`

  [setRoll](#setRoll(double))`(double value)`

Sets the roll of the 3D model in degrees.

`void`

  [setScale](#setScale(double))`(double value)`

Sets the scale factor, to be applied to the 3D model before rendering.

`void`

  [setVisibilityRanges](#setVisibilityRanges(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMeasureRange`](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")`> value)`

Sets visibility ranges for this 3D marker.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel)" class="section detail">

### MapMarker3D

public MapMarker3D(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") at, @NonNull [MapMarker3DModel](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview") model)

    Creates an instance of a 3D marker.

    The origin of the 3D model's local coordinate system is placed at the specified geographical coordinates.

    Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.
Parameters:
    `at` -

    The geographical coordinates where the 3D marker is placed corresponding to origin of the 3D model's local coordinate system.

    `model` -

    The 3D model used to draw 3D marker.
- (com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,double,com.here.sdk.mapview.RenderSize.Unit)" class="section detail">

### MapMarker3D

public MapMarker3D(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") at, @NonNull [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") image, double scale, @NonNull [RenderSize.Unit](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") unit)

    Creates a flat marker from provided map image.

    Such map marker is a flat 3D marker of rectangular shape textured with given image. Aspect ratio of the flat marker is determined by aspect ratio of the image.

    Only bitmap images are supported, using a [`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") created from SVG data will result in distorted rendering of the flat marker.

    Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.

    Size of the rendered flat marker can be specified in either world or screen coordinate space.

    For [`RenderSize.Unit.PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#PIXELS), the flat marker will cover `scale` \* image's width pixels horizontally and `scale` \* image's height pixels vertically. The size of the flat marker remains constant on the screen.

    For [`RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#DENSITY_INDEPENDENT_PIXELS) the flat marker will cover `scale` \* image's width density independent pixels horizontally and `scale` \* image's height density independent pixels vertically. The size of the flat marker remains constant on the screen.

    For [`RenderSize.Unit.METERS`](sdk-for-android-explore-api-reference-latestrendersize-unit#METERS) the flat marker will cover `scale` \* image's width meters horizontally and `scale` \* image's height meters vertically. Unlike with pixels or density independent pixels the size of the flat marker will grow and shrink together with regular map content like streets or buildings.
Parameters:
    `at` -

    The geographical coordinates where the flat marker is placed corresponding to center of the provided map image.

    `image` -

    The MapImage containing the texture data of the flat marker. SVG images are not supported.

    `scale` -

    Scale factor applied to the dimensions of the image.

    `unit` -

    Determines whether the size of the flat marker is represented in world or in screen space.
- (com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double)" class="section detail">

### MapMarker3D

public MapMarker3D(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") at, @NonNull [MapMarker3DModel](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview") model, double scale)

    Creates an instance of a 3D marker with scale factor.

    One unit of the 3D marker model will cover `scale` pixels. The size of the 3D marker remains constant on the screen.

    The origin of the 3D model's local coordinate system is placed at the specified geographical coordinates.

    Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.
Parameters:
    `at` -

    The geographical coordinates where the 3D marker is placed corresponding to origin of the 3D model's local coordinate system.

    `model` -

    The 3D model used to render the 3D marker.

    `scale` -

    Scale factor to apply to the 3D model.
- (com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.RenderSize.Unit)" class="section detail">

### MapMarker3D

public MapMarker3D(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") at, @NonNull [MapMarker3DModel](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview") model, double scale, @NonNull [RenderSize.Unit](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") unit)

    Creates a new 3D marker at given world coordinates, using the supplied 3D model.

    The unit specifies how the 3D geometry of the model is interpreted (meters for world space, pixels or density independent pixels for screen space), while scale determines its relative size.

    For [`RenderSize.Unit.PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#PIXELS) one unit of the 3D marker model will cover `scale` pixels. The size of the 3D marker remains constant on the screen.

    For [`RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#DENSITY_INDEPENDENT_PIXELS) one unit of the 3D marker model will cover `scale` density independent pixels. The size of the 3D marker remains constant on the screen.

    For [`RenderSize.Unit.METERS`](sdk-for-android-explore-api-reference-latestrendersize-unit#METERS) one unit of the 3D marker model will cover `scale` meters in the real world. Unlike with pixels or density-independent pixels the size of the 3D marker will grow and shrink together with regular map content like streets or buildings.

    The origin of the 3D model's local coordinate system is placed at the specified geographical coordinates.

    Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.
Parameters:
    `at` -

    The geographical coordinates where the 3D marker is placed corresponding to origin of the 3D model's local coordinate system.

    `model` -

    The 3D model used to render the 3D marker.

    `scale` -

    Scale factor to apply to the 3D model.

    `unit` -

    Determines the unit of the model vertices and whether the size of the 3D marker is expressed in world or screen space.

## Method Details

### getCoordinates

@NonNull public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") getCoordinates()

    Gets the 3D marker's position on the map corresponding to the origin of the 3D marker model coordinate system.

    The altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.
Returns:
    The position of the 3D marker on the map corresponding to the origin of the 3D marker model coordinate system.

### setCoordinates

public void setCoordinates(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") value)

    Sets the 3D marker's position on the map corresponding to the origin of the 3D marker model coordinate system.

    The altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.
Parameters:
    `value` -

    The position of the 3D marker on the map corresponding to the origin of the 3D marker model coordinate system.

### getMetadata

@Nullable public [Metadata](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") getMetadata()

    Gets the [`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") instance attached to this 3D marker. The default value is `null`.
Returns:
    The [`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") instance attached to this 3D marker.

### setMetadata

public void setMetadata(@Nullable [Metadata](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") value)

    Sets the [`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") instance attached to this 3D marker.
Parameters:
    `value` -

    The [`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") instance attached to this 3D marker.

### getBearing

public double getBearing()

    Gets the bearing of the 3D model in degrees.

    The bearing axis is perpendicular to the ground and passes through the 3D marker's location. The Z-axis of the model is aligned with bearing axis.
Returns:
    The bearing of the 3D model in degrees, from the true North in clockwise direction.

### setBearing

public void setBearing(double value)

    Sets the bearing of the 3D model in degrees.

    The bearing axis is perpendicular to the ground and passes through the 3D marker's location. The Z-axis of the model is aligned with bearing axis.
Parameters:
    `value` -

    The bearing of the 3D model in degrees, from the true North in clockwise direction.

### getRoll

public double getRoll()

    Gets the roll of the 3D model in degrees.

    The roll axis is parallel to the ground, passes through the 3D marker's location and is aligned initially with the true North. However, when the bearing changes, it rotates around the bearing axis with the 3D marker. Positive/negative values cause a clockwise/counterclockwise rotation when viewing along the axis in the direction of the true North. The Y-axis of the model is aligned with the roll axis.
Returns:
    The roll angle of the 3D model in degrees.

### setRoll

public void setRoll(double value)

    Sets the roll of the 3D model in degrees.

    The roll axis is parallel to the ground, passes through the 3D marker's location and is aligned initially with the true North. However, when the bearing changes, it rotates around the bearing axis with the 3D marker. Positive/negative values cause a clockwise/counterclockwise rotation when viewing along the axis in the direction of the true North. The Y-axis of the model is aligned with the roll axis.
Parameters:
    `value` -

    The roll angle of the 3D model in degrees.

### getPitch

public double getPitch()

    Gets the pitch of the 3D model in degrees.

    The pitch axis is parallel to the ground, passes through the location of the 3D marker and aligns with the longitude axis if the bearing is 0. However, this axis rotates with the 3D marker according to the bearing value. Negative values cause the top of the 3D marker to lean forward. The X-axis of the model is aligned with pitch axis.
Returns:
    The pitch of the 3D model in degrees.

### setPitch

public void setPitch(double value)

    Sets the pitch of the 3D model in degrees.

    The pitch axis is parallel to the ground, passes through the location of the 3D marker and aligns with the longitude axis if the bearing is 0. However, this axis rotates with the 3D marker according to the bearing value. Negative values cause the top of the 3D marker to lean forward. The X-axis of the model is aligned with pitch axis.
Parameters:
    `value` -

    The pitch of the 3D model in degrees.

### getScale

public double getScale()

    Gets the scale factor applied to the 3D model before rendering.
Returns:
    Scale factor applied to the 3D model before rendering.

### setScale

public void setScale(double value)

    Sets the scale factor, to be applied to the 3D model before rendering.
Parameters:
    `value` -

    Scale factor applied to the 3D model before rendering.

### isDepthCheckEnabled

public boolean isDepthCheckEnabled()

    Returns `true` if depth check is enabled.

    If set to `false`, the 3D marker will always appear in front of any other map objects. If set to `true` the 3D marker might be occluded by other map objects like extruded buildings.

    By default depth check is set to `false`.

    Use the altitude of the [`getCoordinates()`](#getCoordinates()) to position the 3D marker sufficiently high above the surface. Setting depth check to `true` will fix visual glitches where components of the marker 3D model unexpectedly shine through.
Returns:
    Determines whether the depth of the 3D marker's vertices is considered during rendering.

### setDepthCheckEnabled

public void setDepthCheckEnabled(boolean value)

    Set whether the depth of the 3D marker's vertices is considered during rendering.

    If set to `false`, the 3D marker will always appear in front of any other map objects. If set to `true` the 3D marker might be occluded by other map objects like extruded buildings.

    By default depth check is set to `false`.

    Use the altitude of the [`getCoordinates()`](#getCoordinates()) to position the 3D marker sufficiently high above the surface. Setting depth check to `true` will fix visual glitches where components of the marker 3D model unexpectedly shine through.
Parameters:
    `value` -

    Determines whether the depth of the 3D marker's vertices is considered during rendering.

### isRenderInternalsEnabled

public boolean isRenderInternalsEnabled()

    Returns a flag indicating whether to render internal geometry of a 3D marker occluded by its front facing polygons. Default value is `false`.

    Default value is `false`. Can be used with translucent 3D marker.

    Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two passes: first pass with front-face, second pass with back-face culling enabled. With this flag enabled for 3D marker with depth check disabled rendering is performed in a single pass with back-face culling disabled.
Returns:
    Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons.

### setRenderInternalsEnabled

public void setRenderInternalsEnabled(boolean value)

    Sets a flag indicating whether to render internal geometry of a 3D marker occluded by its front facing polygons.

    Default value is `false`. Can be used with translucent 3D marker.

    Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two passes: first pass with front-face, second pass with back-face culling enabled. With this flag enabled for 3D marker with depth check disabled rendering is performed in a single pass with back-face culling disabled.
Parameters:
    `value` -

    Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons.

### getOpacity

public double getOpacity()

    Returns an opacity factor which specifies the translucency of a 3D map marker.

    The factor is applied to the alpha channel of the resulting texture of the marker. Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the specified fill color specified in [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview").
Returns:
    The opacity factor adjusting the opacity of a 3D marker.

### setOpacity

public void setOpacity(double value)

    Sets an opacity factor which specifies the translucency of a 3D map marker.

    Provided value is clamped to the \[0.0, 1.0\] range.

    The factor is applied to the alpha channel of the resulting texture of the marker. Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the specified fill color specified in [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview").
Parameters:
    `value` -

    The opacity factor adjusting the opacity of a 3D marker.

### getVisibilityRanges

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")\> getVisibilityRanges()

    Gets the list of visibility ranges.

    A range is half open - \[minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

    When empty (the default), the 3D marker is visible without map measure restrictions. Only [MapMeasureRange](s) of [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) type are supported. [MapMeasureRange](s) of other unsupported types will be ignored.
Returns:
    The list of visibility ranges. The 3D marker is visible only inside these map measure ranges.

### setVisibilityRanges

public void setVisibilityRanges(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")\> value)

    Sets visibility ranges for this 3D marker.

    A range is half open - \[minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

    When empty (the default), the 3D marker is visible without map measure restrictions. Only [MapMeasureRange](s) of [`MapMeasure.Kind.ZOOM_LEVEL`](sdk-for-android-explore-api-reference-latestmapmeasure-kind#ZOOM_LEVEL) type are supported. [MapMeasureRange](s) of other unsupported types will be ignored.
Parameters:
    `value` -

    The list of visibility ranges. The 3D marker is visible only inside these map measure ranges.

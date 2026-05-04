---
title: "MapCameraLimits (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcameralimits"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapCameraLimits

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapCameraLimits
------------------------------------------------------------------------
public final class MapCameraLimits extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Controls constraints on map camera parameters.

When constraints are set, they are enforced for current camera state and for all future changes to the camera.

When setting, limits are applied on next rendering loop.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `static final double`

  [MAX_TILT](#MAX_TILT)

Absolute maximum possible value of tilt angle.

`static final double`

  [MAX_ZOOM_LEVEL](#MAX_ZOOM_LEVEL)

Absolute maximum possible value of zoom level.

`static final double`

  [MIN_TILT](#MIN_TILT)

Absolute minimum possible value of tilt angle.

`static final double`

  [MIN_ZOOM_LEVEL](#MIN_ZOOM_LEVEL)

Absolute minimum possible value of zoom level.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [clearBearingRanges](#clearBearingRanges())`()`

Clears bearing ranges for all zoom values and resets bearing range to default.

`void`

  [clearTiltRanges](#clearTiltRanges())`()`

Clears tilt ranges for all zoom values and resets tilt range to default.

[`AngleRange`](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core")

  [getBearingRange](#getBearingRange())`()`

Gets the currently set bearing range.

[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")

  [getTargetArea](#getTargetArea())`()`

Gets a GeoBox that limits the camera target to a specific geographical area.

[`AngleRange`](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core")

  [getTiltRange](#getTiltRange())`()`

Gets the current tilt range.

[`MapMeasureRange`](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")

  [getZoomRange](#getZoomRange())`()`

Gets the currently set camera zoom range.

`void`

  [setBearingRange](#setBearingRange(com.here.sdk.core.AngleRange))`(`[`AngleRange`](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core")` value)`

Sets a new bearing range.

`void`

  [setBearingRangeAtZoom](#setBearingRangeAtZoom(com.here.sdk.mapview.MapMeasure,com.here.sdk.core.AngleRange))`(`[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")` zoom, `[`AngleRange`](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core")` bearingRange)`

Sets the bearing range within which the camera can rotate at a given zoom.

`void`

  [setTargetArea](#setTargetArea(com.here.sdk.core.GeoBox))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` value)`

Sets a GeoBox that limits the camera target to a specific geographical area.

`void`

  [setTiltRange](#setTiltRange(com.here.sdk.core.AngleRange))`(`[`AngleRange`](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core")` value)`

Sets a new tilt limit range.

`void`

  [setTiltRangeAtZoom](#setTiltRangeAtZoom(com.here.sdk.mapview.MapMeasure,com.here.sdk.core.AngleRange))`(`[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")` zoom, `[`AngleRange`](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core")` tiltRange)`

Sets tilt ranges that can be set on the camera at given zoom.

`void`

  [setZoomRange](#setZoomRange(com.here.sdk.mapview.MapMeasureRange))`(`[`MapMeasureRange`](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")` value)`

Sets a new camera zoom range.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### MIN_TILT

public static final double MIN_TILT

    Absolute minimum possible value of tilt angle.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapCameraLimits.MIN_TILT)

### MAX_TILT

public static final double MAX_TILT

    Absolute maximum possible value of tilt angle.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapCameraLimits.MAX_TILT)

### MIN_ZOOM_LEVEL

public static final double MIN_ZOOM_LEVEL

    Absolute minimum possible value of zoom level.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapCameraLimits.MIN_ZOOM_LEVEL)

### MAX_ZOOM_LEVEL

public static final double MAX_ZOOM_LEVEL

    Absolute maximum possible value of zoom level.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.mapview.MapCameraLimits.MAX_ZOOM_LEVEL)

## Method Details

### setBearingRangeAtZoom

public void setBearingRangeAtZoom(@NonNull [MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") zoom, @NonNull [AngleRange](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core") bearingRange)

    Sets the bearing range within which the camera can rotate at a given zoom.

    The resulting camera bearing at a zoom is an interpolated value of the ranges set for closest matching zoom values. When no bearing range is specified for [`MIN_ZOOM_LEVEL`](#MIN_ZOOM_LEVEL), the bearing range set through [`setBearingRange(com.here.sdk.core.AngleRange)`](#setBearingRange(com.here.sdk.core.AngleRange)) is used for interpolation.

    Zoom values outside the supported zoom range are ignored. By default, the maximum bearing range for all zoom values is set during initialization.
Parameters:
    `zoom` -

    Zoom at which the range is set.

    `bearingRange` -

    Bearing range.

### clearBearingRanges

public void clearBearingRanges()

    Clears bearing ranges for all zoom values and resets bearing range to default.

### setTiltRangeAtZoom

public void setTiltRangeAtZoom(@NonNull [MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") zoom, @NonNull [AngleRange](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core") tiltRange)

    Sets tilt ranges that can be set on the camera at given zoom.

    The resulting camera tilt at a zoom is an interpolated value of the ranges set for closest matching zoom values. When no tilt range is specified for [`MIN_ZOOM_LEVEL`](#MIN_ZOOM_LEVEL), the tilt range set through [`setTiltRange(com.here.sdk.core.AngleRange)`](#setTiltRange(com.here.sdk.core.AngleRange)) is used for interpolation.

    Zoom or tilt values outside the supported zoom and tilt range are ignored. By default, the maximum tilt range for all zoom values is set during initialization.
Parameters:
    `zoom` -

    Zoom at which the range is set.

    `tiltRange` -

    Tilt range.

### clearTiltRanges

public void clearTiltRanges()

    Clears tilt ranges for all zoom values and resets tilt range to default.

### getTiltRange

@NonNull public [AngleRange](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core") getTiltRange()

    Gets the current tilt range.

    By default, a [`MIN_TILT`](#MIN_TILT)-[`MAX_TILT`](#MAX_TILT) tilt range is set during initialization.

    This range might not be yet active if no rendering loop has been executed since the last call to set the range.
Returns:
    The tilt range that can be applied to the camera.

### setTiltRange

public void setTiltRange(@NonNull [AngleRange](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core") value)

    Sets a new tilt limit range.

    The supported values fall inside [`MIN_TILT`](#MIN_TILT)-[`MAX_TILT`](#MAX_TILT) range. Values outside the supported range are ignored.

    If the current camera tilt exceeds the new limit range, it will immediately be set to minimum or maximum, depending on which is closest.

    This new limit range becomes active during the next rendering loop.

    All previously set tilt ranges are cleared and the new tilt range is applied for all zoom values.
Parameters:
    `value` -

    The tilt range that can be applied to the camera.

### getBearingRange

@NonNull public [AngleRange](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core") getBearingRange()

    Gets the currently set bearing range.

    This may not be active now if no rendering loop has been executed since the last call to set the range.

    By default, range for a full circle is set during initialization.
Returns:
    The bearing range within which the camera can be rotated.

### setBearingRange

public void setBearingRange(@NonNull [AngleRange](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core") value)

    Sets a new bearing range.

    It will be updated during the next rendering loop. All previously set bearing ranges are cleared and the new bearing range is applied for all zoom values.

    If the current camera bearing exceeds the limit range, it will immediately be set to minimum or maximum, depending on which is closest.
Parameters:
    `value` -

    The bearing range within which the camera can be rotated.

### getZoomRange

@NonNull public [MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview") getZoomRange()

    Gets the currently set camera zoom range.

    By default, a [`MIN_ZOOM_LEVEL`](#MIN_ZOOM_LEVEL)-[`MAX_ZOOM_LEVEL`](#MAX_ZOOM_LEVEL) zoom range is set during initialization.
Returns:
    The zoom range that can be applied to the camera.

### setZoomRange

public void setZoomRange(@NonNull [MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview") value)

    Sets a new camera zoom range.

    The supported values fall inside [`MIN_ZOOM_LEVEL`](#MIN_ZOOM_LEVEL)-[`MAX_ZOOM_LEVEL`](#MAX_ZOOM_LEVEL) range. Values outside the supported zoom range are ignored.

    If the current camera zoom exceeds the limit range, it will immediately be set to minimum or maximum, depending on which is closest.

    This new limit range becomes active during the next rendering loop.
Parameters:
    `value` -

    The zoom range that can be applied to the camera.

### getTargetArea

@Nullable public [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") getTargetArea()

    Gets a GeoBox that limits the camera target to a specific geographical area. Absence of a value means that there is no limit.
Returns:
    Geographical area to which the camera target is limited.

### setTargetArea

public void setTargetArea(@Nullable [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") value)

    Sets a GeoBox that limits the camera target to a specific geographical area. Set to `null` to remove the limit.
Parameters:
    `value` -

    Geographical area to which the camera target is limited.

---
title: "LocationIndicator (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlocationindicator"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class LocationIndicator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.LocationIndicator
------------------------------------------------------------------------
public final class LocationIndicator extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Graphical object to represent the location of the user on the map.

It is either a green dot for pedestrian style or a triangular arrow for vehicle navigation style. This style can be changed by [`setLocationIndicatorStyle(com.here.sdk.mapview.LocationIndicator.IndicatorStyle)`](#setLocationIndicatorStyle(com.here.sdk.mapview.LocationIndicator.IndicatorStyle))

The location is made available to an instance of this class by calling [`updateLocation(Location)`](#updateLocation(com.here.sdk.core.Location)) or [`updateLocation(Location, MapCameraUpdate)`](#updateLocation(com.here.sdk.core.Location,com.here.sdk.mapview.MapCameraUpdate)).

Use [`enable(com.here.sdk.mapview.MapViewBase)`](#enable(com.here.sdk.mapview.MapViewBase)) to add this object to the map and [`disable()`](#disable()) to remove it.

Take care that the location indicator is not accidentally added to the map view multiple times for example when the android activity is recreated after an orientation change.

Note: The LocationIndicator is always rendered at a fixed altitude near 0. Changing the MapCamera to look at geographic coordinates with an altitude that is higher can cause the following behavior: If the MapCamera angle is tilted and altitude is too high, the LocationIndicator can unexpectedly disappear from the viewport due to the new perspective.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [LocationIndicator.IndicatorStyle](sdk-for-android-explore-api-reference-latestlocationindicator-indicatorstyle)

The predefined styles for the location indicator which are pedestrian and navigation mode.

`static enum `

  [LocationIndicator.MarkerType](sdk-for-android-explore-api-reference-latestlocationindicator-markertype)

Enum to identify different types of markers of the location indicator.

## Constructor Summary

Constructors

Constructor

  Description

  [LocationIndicator](#%3Cinit%3E())`()`

Creates an instance of LocationIndicator.

[LocationIndicator](#%3Cinit%3E(com.here.sdk.mapview.MapViewBase))`(`[`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")` mapView)`

Creates an instance of LocationIndicator and adds it to provided [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview").

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods
  Deprecated Methods

  Modifier and Type

  Method

  Description

  `void`

  [disable](#disable())`()`

This function removes [`LocationIndicator`](sdk-for-android-explore-api-reference-latestlocationindicator "class in com.here.sdk.mapview") from map view.

`void`

  [enable](#enable(com.here.sdk.mapview.MapViewBase))`(`[`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")` mapView)`

Enables [`LocationIndicator`](sdk-for-android-explore-api-reference-latestlocationindicator "class in com.here.sdk.mapview") for provided [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview").

[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [getHaloColor](#getHaloColor(com.here.sdk.mapview.LocationIndicator.IndicatorStyle))`(`[`LocationIndicator.IndicatorStyle`](sdk-for-android-explore-api-reference-latestlocationindicator-indicatorstyle "enum class in com.here.sdk.mapview")` style)`

Retrieves the color of the accuracy indicator halo for the requested IndicatorStyle.

[`LocationIndicator.IndicatorStyle`](sdk-for-android-explore-api-reference-latestlocationindicator-indicatorstyle "enum class in com.here.sdk.mapview")

  [getLocationIndicatorStyle](#getLocationIndicatorStyle())`()`

Returns visual style of location indicator.

[`MaterialReflectivity`](sdk-for-android-explore-api-reference-latestmaterialreflectivity "class in com.here.sdk.mapview")

  [getMaterialReflectivity](#getMaterialReflectivity())`()`

Retrieves the material reflectivity applied to all markers of location indicator.

`double`

  [getOpacity](#getOpacity())`()`

Gets the current opacity of the location indicator.

`boolean`

  [isAccuracyVisualized](#isAccuracyVisualized())`()`

Returns whether [`Location.horizontalAccuracyInMeters`](sdk-for-android-explore-api-reference-latestlocation#horizontalAccuracyInMeters) is used to scale the accuracy indicator halo.

`boolean`

  [isActive](#isActive())`()`

Returns `true` if active version of the location indicator is shown or `false` when inactive version is shown.

`void`

  [setAccuracyVisualized](#setAccuracyVisualized(boolean))`(boolean value)`

Sets whether [`Location.horizontalAccuracyInMeters`](sdk-for-android-explore-api-reference-latestlocation#horizontalAccuracyInMeters) is used to scale the accuracy indicator halo.

`void`

  [setActive](#setActive(boolean))`(boolean value)`

Sets whether the active or inactive version of location indicator is to be shown.

`void`

  [setHaloColor](#setHaloColor(com.here.sdk.mapview.LocationIndicator.IndicatorStyle,com.here.sdk.core.Color))`(`[`LocationIndicator.IndicatorStyle`](sdk-for-android-explore-api-reference-latestlocationindicator-indicatorstyle "enum class in com.here.sdk.mapview")` style, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` color)`

Sets the color of the accuracy indicator halo for a given style.

`void`

  [setLocationIndicatorStyle](#setLocationIndicatorStyle(com.here.sdk.mapview.LocationIndicator.IndicatorStyle))`(`[`LocationIndicator.IndicatorStyle`](sdk-for-android-explore-api-reference-latestlocationindicator-indicatorstyle "enum class in com.here.sdk.mapview")` value)`

Sets the visual style of location indicator.

`void`

  [setMarker3dModel](#setMarker3dModel(com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.LocationIndicator.MarkerType))`(`[`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview")` model, double scale, `[`LocationIndicator.MarkerType`](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview")` type)`

Deprecated.
Will be removed in v4.27.0.

  `void`

  [setMarker3dModel](#setMarker3dModel(com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.LocationIndicator.MarkerType,com.here.sdk.mapview.RenderSize.Unit))`(`[`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview")` model, double scale, `[`LocationIndicator.MarkerType`](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview")` type, `[`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview")` renderSizeUnit)`

Sets the [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview") asset to be displayed as location indicator for a specified type.

`void`

  [setMaterialReflectivity](#setMaterialReflectivity(com.here.sdk.mapview.MaterialReflectivity))`(`[`MaterialReflectivity`](sdk-for-android-explore-api-reference-latestmaterialreflectivity "class in com.here.sdk.mapview")` value)`

Sets the material reflectivity properties for all markers of location indicator including its halo.

`void`

  [setOpacity](#setOpacity(double))`(double value)`

Sets the opacity of the location indicator.

`void`

  [updateLocation](#updateLocation(com.here.sdk.core.Location))`(`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")` location)`

Updates the indicator to a new location.

`void`

  [updateLocation](#updateLocation(com.here.sdk.core.Location,com.here.sdk.mapview.MapCameraUpdate))`(`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")` location, `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")` cameraUpdate)`

Updates the indicator to a new location and applies a camera update at the same time.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### LocationIndicator

public LocationIndicator()

    Creates an instance of LocationIndicator.

  - (com.here.sdk.mapview.MapViewBase)" class="section detail">

### LocationIndicator

public LocationIndicator(@NonNull [MapViewBase](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview") mapView)

    Creates an instance of LocationIndicator and adds it to provided [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview").
Parameters:
    `mapView` -

    The [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview") instance.

## Method Details

### enable

public void enable(@NonNull [MapViewBase](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview") mapView)

    Enables [`LocationIndicator`](sdk-for-android-explore-api-reference-latestlocationindicator "class in com.here.sdk.mapview") for provided [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview"). If [`LocationIndicator`](sdk-for-android-explore-api-reference-latestlocationindicator "class in com.here.sdk.mapview") is already enabled (added to map view) for passed map view, this function does nothing. If [`LocationIndicator`](sdk-for-android-explore-api-reference-latestlocationindicator "class in com.here.sdk.mapview") is added to different [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview"), this function removes first [`LocationIndicator`](sdk-for-android-explore-api-reference-latestlocationindicator "class in com.here.sdk.mapview") from previous map view before adding to new one.
Parameters:
    `mapView` -

    The [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview") instance.

### disable

public void disable()

    This function removes [`LocationIndicator`](sdk-for-android-explore-api-reference-latestlocationindicator "class in com.here.sdk.mapview") from map view. If [`LocationIndicator`](sdk-for-android-explore-api-reference-latestlocationindicator "class in com.here.sdk.mapview") was not added to any map view yet, this function does nothing.

### updateLocation

public void updateLocation(@NonNull [Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core") location)

    Updates the indicator to a new location. If accuracy visualized is set to `true` the field [`Location.horizontalAccuracyInMeters`](sdk-for-android-explore-api-reference-latestlocation#horizontalAccuracyInMeters) determines the size of the accuracy indicator halo.

    The altitude of the location is ignored.
Parameters:
    `location` -

    The updated location of the user.

### updateLocation

public void updateLocation(@NonNull [Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core") location, @NonNull [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") cameraUpdate)

    Updates the indicator to a new location and applies a camera update at the same time.

    Does nothing if the indicator instance is not enabled. If accuracy visualized is set to `true` the field [`Location.horizontalAccuracyInMeters`](sdk-for-android-explore-api-reference-latestlocation#horizontalAccuracyInMeters) determines the size of the accuracy indicator halo.

    The altitude of the location is ignored.
Parameters:
    `location` -

    The updated location of the user.

    `cameraUpdate` -

    The update to apply to the camera.

### setMarker3dModel

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public void setMarker3dModel(@NonNull [MapMarker3DModel](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview") model, double scale, @NonNull [LocationIndicator.MarkerType](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview") type)

    Deprecated.
Will be removed in v4.27.0. Please use the overloaded method with [`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") instead.

Sets the MapMarker3DModel asset to be displayed as location indicator for a specified type. The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only MapMarker3DModel created from \*.obj files are supported. Models created from Mesh will be ignored.
Parameters:
    `model` -

    The MapMarker3DModel object to be displayed for the specified type. Only models created from obj files are supported. Those created from mesh will be ignored.

    `scale` -

    The scaling which will be applied to the marker model. As the size of the location marker should be aligned on devices with different resolutions the scale factor is applied relative to the ppi value and thus differs from the scale which is passed to [`MapMarker3D`](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview") objects. Meter is used for the unit of the map marker 3d model coordinate system. For historical reason, the scale factor is internally devided by 6. To display a unit qube of 1x1x1 meter as is, please use a scale value of 6.0.

    `type` -

    The type of location marker for which the marker 3d model should be replaced.

### setMarker3dModel

public void setMarker3dModel(@NonNull [MapMarker3DModel](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview") model, double scale, @NonNull [LocationIndicator.MarkerType](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview") type, @NonNull [RenderSize.Unit](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") renderSizeUnit)

    Sets the [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview") asset to be displayed as location indicator for a specified type. The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview") created from `obj` files are supported. Models created from Mesh will be ignored.
Parameters:
    `model` -

    The [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview") object to be displayed for the specified type. Only models created from `obj` files are supported. Those created from mesh will be ignored.

    `scale` -

    A scale factor applied to the marker model.

    `type` -

    The type of location marker for which the marker 3d model should be replaced.

    `renderSizeUnit` -

    The [`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") specifying how the vertex coordinates of the 3D model are being interpreted. It specifies whether the 3D model is placed in world or screen coordinate space.

    [`RenderSize.Unit.METERS`](sdk-for-android-explore-api-reference-latestrendersize-unit#METERS) will make the 3D model use world coordinate space, meaning that it will change size together with the map when it is zoomed in and out. A simple 10 by 10 by 10 (in model space) cube will have a size of 10 by 10 by 10 meters in world space.

    [`RenderSize.Unit.PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#PIXELS) makes the 3D model use screen coordinate space, meaning that it will have constant size on the screen regardless of how the map zoom changes. A simple 10 by 10 (in model space) rectangle will have a size of 10 by 10 pixels on the screen.

    [`RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS`](sdk-for-android-explore-api-reference-latestrendersize-unit#DENSITY_INDEPENDENT_PIXELS) is similar to pixels, but the resulting size will take into account the pixel density of the display, meaning that physical size on the screen will be approximately the same regardless of the size or resolution of the display.

### setHaloColor

public void setHaloColor(@NonNull [LocationIndicator.IndicatorStyle](sdk-for-android-explore-api-reference-latestlocationindicator-indicatorstyle "enum class in com.here.sdk.mapview") style, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") color)

    Sets the color of the accuracy indicator halo for a given style.
Parameters:
    `style` -

    The type of IndicatorStyle for which the color should be assigned.

    `color` -

    The color to be applied to the halo for a specified IndicatorStyle. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### getHaloColor

@NonNull public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") getHaloColor(@NonNull [LocationIndicator.IndicatorStyle](sdk-for-android-explore-api-reference-latestlocationindicator-indicatorstyle "enum class in com.here.sdk.mapview") style)

    Retrieves the color of the accuracy indicator halo for the requested IndicatorStyle. The default color is a translucent turquoise (rgba(0, 199, 194, 76)) for all IndicatorStyle settings.
Parameters:
    `style` -

    The type of IndicatorStyle for which the color should be returned.

    Returns:
    The color of the halo for the specified IndicatorStyle. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### isAccuracyVisualized

public boolean isAccuracyVisualized()

    Returns whether [`Location.horizontalAccuracyInMeters`](sdk-for-android-explore-api-reference-latestlocation#horizontalAccuracyInMeters) is used to scale the accuracy indicator halo. Default is `false`, in which case the halo has a fixed and zoom level independent size.
Returns:
    Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo.

### setAccuracyVisualized

public void setAccuracyVisualized(boolean value)

    Sets whether [`Location.horizontalAccuracyInMeters`](sdk-for-android-explore-api-reference-latestlocation#horizontalAccuracyInMeters) is used to scale the accuracy indicator halo. Default is `false`, in which case the halo has a fixed and zoom level independent size.

    When set to `true`, the radius of the halo corresponds to the value of [`Location.horizontalAccuracyInMeters`](sdk-for-android-explore-api-reference-latestlocation#horizontalAccuracyInMeters) passed to [`updateLocation(Location)`](#updateLocation(com.here.sdk.core.Location)) and scales in world coordinates.

    For values smaller than 20 meters the halo is hidden. The radius of the halo is limited to 500 meters and values higher than that or `null` will keep the halo at that size.

    If the location indicator is set to inactive (which can be checked via [`isActive()`](#isActive()) flag), then the halo is always hidden. The value of this property remains unchanged regardless of the flag's value. If the location indicator is set to active:

    - Built-in location indicators:
      - The halo is always shown.
      - If the accuracy visualization is set to `true`, the size of the halo scales with [`Location.horizontalAccuracyInMeters`](sdk-for-android-explore-api-reference-latestlocation#horizontalAccuracyInMeters) in world coordinates.
      - If the accuracy visualization is set to `false`, halo displays at a default size.
    - Custom location indicator:
      - If the accuracy visualization is set to `true`, halo is shown and the size of the halo scales with [`Location.horizontalAccuracyInMeters`](sdk-for-android-explore-api-reference-latestlocation#horizontalAccuracyInMeters) in world coordinates.
      - If the accuracy visualization is set to `false`, no halo is shown since it might not fit together with the custom 3d model.
Parameters:
    `value` -

    Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo.

### getLocationIndicatorStyle

@NonNull public [LocationIndicator.IndicatorStyle](sdk-for-android-explore-api-reference-latestlocationindicator-indicatorstyle "enum class in com.here.sdk.mapview") getLocationIndicatorStyle()

    Returns visual style of location indicator.

    By default, it is set to [`LocationIndicator.IndicatorStyle.NAVIGATION`](sdk-for-android-explore-api-reference-latestlocationindicator-indicatorstyle#NAVIGATION).
Returns:
    The visual style of location indicator.

### setLocationIndicatorStyle

public void setLocationIndicatorStyle(@NonNull [LocationIndicator.IndicatorStyle](sdk-for-android-explore-api-reference-latestlocationindicator-indicatorstyle "enum class in com.here.sdk.mapview") value)

    Sets the visual style of location indicator.

    By default, it is set to [`LocationIndicator.IndicatorStyle.NAVIGATION`](sdk-for-android-explore-api-reference-latestlocationindicator-indicatorstyle#NAVIGATION).
Parameters:
    `value` -

    The visual style of location indicator.

### isActive

public boolean isActive()

    Returns `true` if active version of the location indicator is shown or `false` when inactive version is shown. By default, it is `true`.
Returns:
    A Boolean value that determines whether the active on inactive version of location indicator is shown.

### setActive

public void setActive(boolean value)

    Sets whether the active or inactive version of location indicator is to be shown. the indicator to active state if `true` is passed and to inactive state when false is passed. By default, it is `true`.
Parameters:
    `value` -

    A Boolean value that determines whether the active on inactive version of location indicator is shown.

### getOpacity

public double getOpacity()

    Gets the current opacity of the location indicator.

    Default value is 1.0 which means location indicator is displayed with the default alpha channel of the texture.
Returns:
    The factor applied to the alpha channel of both the location indicator's texture and the accuracy indicator's halo color.

### setOpacity

public void setOpacity(double value)

    Sets the opacity of the location indicator. Provided value is clamped in range \[0.0, 1.0\].

    Default value is 1.0 which means location indicator is displayed with the default alpha channel of the texture.
Parameters:
    `value` -

    The factor applied to the alpha channel of both the location indicator's texture and the accuracy indicator's halo color.

### getMaterialReflectivity

@Nullable public [MaterialReflectivity](sdk-for-android-explore-api-reference-latestmaterialreflectivity "class in com.here.sdk.mapview") getMaterialReflectivity()

    Retrieves the material reflectivity applied to all markers of location indicator.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    Enables per‑pixel lighting for all internal markers (navigation, pedestrian, inactive variants) and the halo when assigned. While `materialReflectivity` is non‑null the markers are shaded by scene lights using the provided ambient / diffuse factors. When set back to `null`, lighting is disabled and markers revert to unlit (emissive) rendering.

    Default value is `null`.
Returns:
    The material reflectivity properties of the location indicator.

### setMaterialReflectivity

public void setMaterialReflectivity(@Nullable [MaterialReflectivity](sdk-for-android-explore-api-reference-latestmaterialreflectivity "class in com.here.sdk.mapview") value)

    Sets the material reflectivity properties for all markers of location indicator including its halo. This value affects also any custom markers set with `setMarker3dModel`.

    Enables per‑pixel lighting for all internal markers (navigation, pedestrian, inactive variants) and the halo when assigned. While `materialReflectivity` is non‑null the markers are shaded by scene lights using the provided ambient / diffuse factors. When set back to `null`, lighting is disabled and markers revert to unlit (emissive) rendering.

    Default value is `null`.
Parameters:
    `value` -

    The material reflectivity properties of the location indicator.

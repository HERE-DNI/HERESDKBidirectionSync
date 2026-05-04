---
title: "MapScene (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapscene"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapScene

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapScene
------------------------------------------------------------------------
public final class MapScene extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Represents a map scene and exposes the functionality to manipulate its content.

## Map schemes

The content of the displayed map and how it looks is specified by a [`MapScheme`](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") which is set when loading a scene with [`loadScene(MapScheme, MapScene.LoadSceneCallback)`](#loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)). It is also possible to load your own custom map scheme from a file bundled with your application. Supported file formats are:

- JSON (file extension '.json'; e.g. 'my_custom_style.json')
- ZIP archive (file extension '.zip'; e.g. 'my_custom_style.zip'), with the following archive structure:
  - root folder: any, not empty (e.g. 'my_custom_style')
  - JSON configuration: '/style.json'
  - custom assets folder: '/assets'

## Map features

Different map schemes offer different sets of features, for example showing traffic or 3D buildings. Some features have multiple modes of operation, but most have only one. [`getSupportedFeatures()`](#getSupportedFeatures()) can be used to check what features and modes are supported for the current scene. Features can be enabled using [`enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](#enableFeatures(java.util.Map)) and disabled with [`disableFeatures(java.util.List<java.lang.String>)`](#disableFeatures(java.util.List)). Checking which features are currently enabled can be done using [`getActiveFeatures()`](#getActiveFeatures()). For convenience, [`MapFeatures`](sdk-for-android-explore-api-reference-latestmapfeatures "class in com.here.sdk.mapview") and [`MapFeatureModes`](sdk-for-android-explore-api-reference-latestmapfeaturemodes "class in com.here.sdk.mapview") hold constants for feature and mode names.

Since version 4.15.0, map features cannot be controlled using [`setLayerVisibility(java.lang.String, com.here.sdk.mapview.VisibilityState)`](#setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)), since [`setLayerVisibility(java.lang.String, com.here.sdk.mapview.VisibilityState)`](#setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)) controls only visibility of the layers which are corresponding to the features enabled either by [`enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](#enableFeatures(java.util.Map)) or enabled by default for the scene.

## Map layers

A map scheme is organized in layers, which can be controlled using [`setLayerVisibility(java.lang.String, com.here.sdk.mapview.VisibilityState)`](#setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)). It's possible to change the visibility state of any map layer as long as the name is known.

Layer visibility settings persist between scene reloading.

## User content

User generated content can be visualised on the map using [`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview"), [`MapPolygon`](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview"), [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview"), [`MapMarkerCluster`](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview"), [`MapArrow`](sdk-for-android-explore-api-reference-latestmaparrow "class in com.here.sdk.mapview"), [`MapMarker3D`](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview") and [`MapImageOverlay`](sdk-for-android-explore-api-reference-latestmapimageoverlay "class in com.here.sdk.mapview") (collectively referred to as "map items"). Those can be added to and removed from the scene by respective add and remove methods. The render order of the map items is according to the list above. The order of objects within the same type can be controlled using the `setDrawOrder()` method of each object.

Be careful when adding a very large number of map items as this can have a negative impact on the performance of the app. To work around this limitation the following approach can be used: Register to map camera updates using [`MapCamera.addListener(com.here.sdk.mapview.MapCameraListener)`](sdk-for-android-explore-api-reference-latestmapcamera#addListener(com.here.sdk.mapview.MapCameraListener)). Query the bounding box of the camera viewport using [`MapCamera.getBoundingBox()`](sdk-for-android-explore-api-reference-latestmapcamera#getBoundingBox()) (it may be extended) and then use the method [`GeoBox.contains(GeoCoordinates)`](sdk-for-android-explore-api-reference-latestgeobox#contains(com.here.sdk.core.GeoCoordinates)) in combination with [`MapCamera.State.distanceToTargetInMeters`](sdk-for-android-explore-api-reference-latestmapcamera-state#distanceToTargetInMeters) to determine which map items are actually visible to the user in the current camera viewport and thus need to be added to the map.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static interface `

  [MapScene.LoadSceneCallback](sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback)

Called on the main thread after `loadScene()` method finishes loading the scene.

`static final class `

  [MapScene.MapPickFilter](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter)

Filter for the map content to be picked.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [addMapArrow](#addMapArrow(com.here.sdk.mapview.MapArrow))`(`[`MapArrow`](sdk-for-android-explore-api-reference-latestmaparrow "class in com.here.sdk.mapview")` mapArrow)`

Adds a map arrow to this map scene.

`void`

  [addMapImageOverlay](#addMapImageOverlay(com.here.sdk.mapview.MapImageOverlay))`(`[`MapImageOverlay`](sdk-for-android-explore-api-reference-latestmapimageoverlay "class in com.here.sdk.mapview")` overlay)`

Adds a map image overlay to this map scene.

`void`

  [addMapMarker](#addMapMarker(com.here.sdk.mapview.MapMarker))`(`[`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")` marker)`

Adds a map marker to this map scene.

`void`

  [addMapMarker3d](#addMapMarker3d(com.here.sdk.mapview.MapMarker3D))`(`[`MapMarker3D`](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview")` marker)`

Adds a 3D map marker to this map scene.

`void`

  [addMapMarkerCluster](#addMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster))`(`[`MapMarkerCluster`](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview")` cluster)`

Adds a map marker cluster to the map.

`void`

  [addMapMarkers](#addMapMarkers(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")`> markers)`

Adds multiple map markers to this map scene.

`void`

  [addMapMarkers3d](#addMapMarkers3d(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker3D`](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview")`> markers)`

Adds multiple 3D map markers to this map scene.

`void`

  [addMapPolygon](#addMapPolygon(com.here.sdk.mapview.MapPolygon))`(`[`MapPolygon`](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview")` mapPolygon)`

Adds a map polygon to this map scene.

`void`

  [addMapPolygons](#addMapPolygons(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapPolygon`](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview")`> mapPolygons)`

Adds multiple map polygons to this map scene.

`void`

  [addMapPolyline](#addMapPolyline(com.here.sdk.mapview.MapPolyline))`(`[`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")` mapPolyline)`

Adds a map polyline to this map scene.

`void`

  [addMapPolylines](#addMapPolylines(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")`> mapPolylines)`

Adds map polylines to this map scene.

`void`

  [disableFeatures](#disableFeatures(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`> features)`

Disables specified map features.

`void`

  [enableFeatures](#enableFeatures(java.util.Map))`(`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html), [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`> features)`

Enables specified map features.

[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html), [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [getActiveFeatures](#getActiveFeatures())`()`

Gets map features that are currently active.

[`MapSceneLights`](sdk-for-android-explore-api-reference-latestmapscenelights "class in com.here.sdk.mapview")

  [getLights](#getLights())`()`

Gets a MapSceneLights instance that controls lights present in the scene.

[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html), [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>>`

  [getSupportedFeatures](#getSupportedFeatures())`()`

Gets features and all of their modes supported by the currently loaded scene configuration.

`void`

  [loadScene](#loadScene(com.here.sdk.mapview.MapSceneLoadOptions,com.here.sdk.mapview.MapScene.LoadSceneCallback))`(`[`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview")` options, `[`MapScene.LoadSceneCallback`](sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback "interface in com.here.sdk.mapview")` callback)`

Asynchronously loads a map scene using MapSceneLoadOptions.

`void`

  [loadScene](#loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback))`(`[`MapScheme`](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview")` mapScheme, `[`MapScene.LoadSceneCallback`](sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback "interface in com.here.sdk.mapview")` callback)`

Asynchronously loads a map scene described by a specified map scheme.

`void`

  [loadScene](#loadScene(java.lang.String,com.here.sdk.mapview.MapScene.LoadSceneCallback))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` configurationFile, `[`MapScene.LoadSceneCallback`](sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback "interface in com.here.sdk.mapview")` callback)`

Asynchronously loads a map scene described by a specified file in one of the supported formats.

`void`

  [loadScene](#loadScene(java.lang.String,com.here.sdk.mapview.WatermarkStyle,com.here.sdk.mapview.MapScene.LoadSceneCallback))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` configurationFile, `[`WatermarkStyle`](sdk-for-android-explore-api-reference-latestwatermarkstyle "enum class in com.here.sdk.mapview")` watermarkStyle, `[`MapScene.LoadSceneCallback`](sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback "interface in com.here.sdk.mapview")` callback)`

Asynchronously loads a map scene described by a specified file in one of the supported formats.

`void`

  [reloadScene](#reloadScene())`()`

Asynchronously reloads the current map scene from file.

`void`

  [removeAllMapMarkers](#removeAllMapMarkers())`()`

Removes all map markers from this map scene.

`void`

  [removeAllMapMarkers3d](#removeAllMapMarkers3d())`()`

Removes all 3D map markers from this map scene.

`void`

  [removeAllMapPolygons](#removeAllMapPolygons())`()`

Removes all map polygons from this map scene.

`void`

  [removeAllMapPolylines](#removeAllMapPolylines())`()`

Removes all map polylines from this map scene.

`void`

  [removeMapArrow](#removeMapArrow(com.here.sdk.mapview.MapArrow))`(`[`MapArrow`](sdk-for-android-explore-api-reference-latestmaparrow "class in com.here.sdk.mapview")` mapArrow)`

Removes a map arrow from this map scene.

`void`

  [removeMapImageOverlay](#removeMapImageOverlay(com.here.sdk.mapview.MapImageOverlay))`(`[`MapImageOverlay`](sdk-for-android-explore-api-reference-latestmapimageoverlay "class in com.here.sdk.mapview")` overlay)`

Removes a map image overlay from this map scene.

`void`

  [removeMapMarker](#removeMapMarker(com.here.sdk.mapview.MapMarker))`(`[`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")` marker)`

Removes a map marker from this map scene.

`void`

  [removeMapMarker3d](#removeMapMarker3d(com.here.sdk.mapview.MapMarker3D))`(`[`MapMarker3D`](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview")` marker)`

Removes a 3D map marker from this map scene.

`void`

  [removeMapMarkerCluster](#removeMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster))`(`[`MapMarkerCluster`](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview")` cluster)`

Removes a map marker cluster from the map.

`void`

  [removeMapMarkers](#removeMapMarkers(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")`> markers)`

Removes multiple map markers from this map scene.

`void`

  [removeMapMarkers3d](#removeMapMarkers3d(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker3D`](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview")`> markers)`

Removes multiple 3D map markers from this map scene.

`void`

  [removeMapPolygon](#removeMapPolygon(com.here.sdk.mapview.MapPolygon))`(`[`MapPolygon`](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview")` mapPolygon)`

Removes a map polygon from this map scene.

`void`

  [removeMapPolygons](#removeMapPolygons(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapPolygon`](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview")`> mapPolygons)`

Removes multiple map polygon from this map scene.

`void`

  [removeMapPolyline](#removeMapPolyline(com.here.sdk.mapview.MapPolyline))`(`[`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")` mapPolyline)`

Removes a map polyline from this map scene.

`void`

  [removeMapPolylines](#removeMapPolylines(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")`> mapPolylines)`

Removes map polylines from this map scene.

`void`

  [setLayerVisibility](#setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` layerName, `[`VisibilityState`](sdk-for-android-explore-api-reference-latestvisibilitystate "enum class in com.here.sdk.mapview")` visibility)`

Immediately changes the visibility of a specified map layer.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### loadScene

public void loadScene(@NonNull [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") mapScheme, @Nullable [MapScene.LoadSceneCallback](sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback "interface in com.here.sdk.mapview") callback)

    Asynchronously loads a map scene described by a specified map scheme. Any previous map scene config will be replaced. The loaded scene is cached and so any changes made to the scene files on disk might not get reflected on a successive call to this function. Instead the reloadScene API can handle such use-cases to force-update the scene.

    Map features enabled or disabled using [`enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](#enableFeatures(java.util.Map)) and [`disableFeatures(java.util.List<java.lang.String>)`](#disableFeatures(java.util.List)) will be reset to defaults for the new scene configuration.

    The callback is called on the main thread. When recreating an activity following a device rotation, it is not necessary to call this method a second time. The map scheme that was loaded when the map view was initially created will continue to be used.
Parameters:
    `mapScheme` -

    Map scheme.

    `callback` -

    Optional callback that will receive the result of this operation.

### loadScene

public void loadScene(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) configurationFile, @Nullable [MapScene.LoadSceneCallback](sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback "interface in com.here.sdk.mapview") callback)

    Asynchronously loads a map scene described by a specified file in one of the supported formats. Any previous map scene config will be replaced.

    When loading the same file again, consider to call `reloadScene()` instead.

    Map features enabled or disabled using [`enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](#enableFeatures(java.util.Map)) and [`disableFeatures(java.util.List<java.lang.String>)`](#disableFeatures(java.util.List)) will be reset to defaults for the new scene configuration.

    The callback is called on the main thread. When recreating an activity following a device rotation, it is not necessary to call this method a second time. The map scheme that was loaded when the map view was initially created will continue to be used.
Parameters:
    `configurationFile` -

    Map scheme configuration file. It must contain the whole scene configuration. In case it contains references to other files, they have to be reachable under the paths specified in the main configuration file.

    `callback` -

    Optional callback that will receive the result of this operation.

### loadScene

public void loadScene(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) configurationFile, @NonNull [WatermarkStyle](sdk-for-android-explore-api-reference-latestwatermarkstyle "enum class in com.here.sdk.mapview") watermarkStyle, @Nullable [MapScene.LoadSceneCallback](sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback "interface in com.here.sdk.mapview") callback)

    Asynchronously loads a map scene described by a specified file in one of the supported formats. The style of the HERE watermark matching the map scheme is specified. Any previous map scene config will be replaced.

    When loading the same file again, consider to call `reloadScene()` instead.

    Map features enabled or disabled using [`enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](#enableFeatures(java.util.Map)) and [`disableFeatures(java.util.List<java.lang.String>)`](#disableFeatures(java.util.List)) will be reset to defaults for the new scene configuration.

    The callback is called on the main thread. When recreating an activity following a device rotation, it is not necessary to call this method a second time. The map scheme that was loaded when the map view was initially created will continue to be used.
Parameters:
    `configurationFile` -

    Map scheme configuration file. It must contain the whole scene configuration. In case it contains references to other files, they have to be reachable under the paths specified in the main configuration file.

    `watermarkStyle` -

    The style for the HERE watermark, see [`WatermarkStyle`](sdk-for-android-explore-api-reference-latestwatermarkstyle "enum class in com.here.sdk.mapview").

    `callback` -

    Optional callback that will receive the result of this operation.

### loadScene

public void loadScene(@NonNull [MapSceneLoadOptions](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview") options, @Nullable [MapScene.LoadSceneCallback](sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback "interface in com.here.sdk.mapview") callback)

    Asynchronously loads a map scene using MapSceneLoadOptions.

    This is an unified API that supports loading from either a map scheme or configuration file, with optional feature and watermark configuration. It's more efficient to load the scene with this function by specifying the list of enabled features and disabled features, compared to loading the scene first and enabling or disabling map features in the scene loading callback function.

    Configuration defaults are used for features that are not part of the enabled features or disabled features parameters. When a feature is in both the enabled and disabled lists, the feature is considered as requested to be enabled. If the same feature is present multiple times in the enabled list with different modes, then the feature is considered as requested to be enabled, but with an unspecified mode (any of the many specified in the enabled list).

    Any previous map scene config will be replaced. The callback is called on the main thread.

    When recreating an activity following a device rotation, it is not necessary to call this method a second time. The map scheme that was loaded when the map view was initially created will continue to be used.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `options` -

    Scene configuration options created using MapSceneLoadOptionsBuilder.

    `callback` -

    Optional callback that will receive the result of this operation.

### addMapPolyline

public void addMapPolyline(@NonNull [MapPolyline](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview") mapPolyline)

    Adds a map polyline to this map scene.
Parameters:
    `mapPolyline` -

    The map polyline to be added to this map scene.

### addMapPolylines

public void addMapPolylines(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapPolyline](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")\> mapPolylines)

    Adds map polylines to this map scene.

    **Note:** Due to technical limitations using the MapPolyline API to add a very large number of polylines (especially 1000+ also depending on their complexity) is not recommended. Adding this many polylines has a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the [`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") class doc.
Parameters:
    `mapPolylines` -

    The map polylines to be added to this map scene.

### removeMapPolyline

public void removeMapPolyline(@NonNull [MapPolyline](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview") mapPolyline)

    Removes a map polyline from this map scene.
Parameters:
    `mapPolyline` -

    The map polyline to be removed from this map scene.

### removeMapPolylines

public void removeMapPolylines(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapPolyline](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")\> mapPolylines)

    Removes map polylines from this map scene.
Parameters:
    `mapPolylines` -

    The map polylines to be removed from this map scene.

### removeAllMapPolylines

public void removeAllMapPolylines()

    Removes all map polylines from this map scene.

### addMapArrow

public void addMapArrow(@NonNull [MapArrow](sdk-for-android-explore-api-reference-latestmaparrow "class in com.here.sdk.mapview") mapArrow)

    Adds a map arrow to this map scene.

    **Note:** Due to technical limitations using the MapArrow API to add a very large number of arrows (especially 1000+ also depending on their complexity) is not recommended. Adding this many arrows has a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the [`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") class doc.
Parameters:
    `mapArrow` -

    The map arrow to be added to this map scene.

### removeMapArrow

public void removeMapArrow(@NonNull [MapArrow](sdk-for-android-explore-api-reference-latestmaparrow "class in com.here.sdk.mapview") mapArrow)

    Removes a map arrow from this map scene.
Parameters:
    `mapArrow` -

    The map arrow to be removed from this map scene.

### addMapMarker

public void addMapMarker(@NonNull [MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview") marker)

    Adds a map marker to this map scene. Adding the same marker instance multiple times has no effect. Adding a marker that is already part of a map marker cluster has no effect.
Parameters:
    `marker` -

    The marker to be added to this map scene.

### addMapMarkers

public void addMapMarkers(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")\> markers)

    Adds multiple map markers to this map scene. Adding the same marker instances multiple times has no effect. Adding markers that are already part of a map marker cluster has no effect.

    **Note:** Due to technical limitations using the MapMarkers API to add a very large number of markers (several thousands, especially 10000+) is not recommended. Adding this many markers will have a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the [`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") class doc.
Parameters:
    `markers` -

    The list of markers to be added to this map scene.

### removeMapMarker

public void removeMapMarker(@NonNull [MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview") marker)

    Removes a map marker from this map scene. Removing a marker instance that is not a part of this scene or belongs to a marker cluster has no effect.
Parameters:
    `marker` -

    The marker to be removed from this map scene.

### removeMapMarkers

public void removeMapMarkers(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")\> markers)

    Removes multiple map markers from this map scene. Removing marker instances that are not a part of this scene or belong to a marker cluster has no effect.
Parameters:
    `markers` -

    The list of markers to be removed from this map scene.

### removeAllMapMarkers

public void removeAllMapMarkers()

    Removes all map markers from this map scene.

### addMapMarkerCluster

public void addMapMarkerCluster(@NonNull [MapMarkerCluster](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview") cluster)

    Adds a map marker cluster to the map. Either the contained individual map markers or the cluster markers will be displayed. Adding the same map marker cluster instance multiple times has no effect.
Parameters:
    `cluster` -

    The marker cluster to be added to this map scene.

### removeMapMarkerCluster

public void removeMapMarkerCluster(@NonNull [MapMarkerCluster](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview") cluster)

    Removes a map marker cluster from the map. Removing a map marker cluster that is not on this scene has no effect.
Parameters:
    `cluster` -

    The marker cluster to be removed from this map scene.

### addMapMarker3d

public void addMapMarker3d(@NonNull [MapMarker3D](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview") marker)

    Adds a 3D map marker to this map scene. Does nothing if the marker instance was already added to the scene.

    **Note:** Due to technical limitations using the MapMarker3D API to add a very large number of 3D markers (especially 500+ also depending on the complexity of the 3D object) is not recommended. Adding this many 3D markers has a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the [`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") class doc.
Parameters:
    `marker` -

    The marker to be added to this map scene.

### addMapMarkers3d

public void addMapMarkers3d(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker3D](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview")\> markers)

    Adds multiple 3D map markers to this map scene. Adding the same 3D marker instances multiple times has no effect.

    **Note:** Due to technical limitations, using the MapMarkers3D API to add a very large number of 3D markers (especially 500+) is not recommended. Adding this many markers will have a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the [`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") class doc.
Parameters:
    `markers` -

    The list of 3D markers to be added to this map scene.

### removeMapMarker3d

public void removeMapMarker3d(@NonNull [MapMarker3D](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview") marker)

    Removes a 3D map marker from this map scene. Removing a marker instance that is not on this scene has no effect.
Parameters:
    `marker` -

    The marker to be removed from this map scene.

### removeMapMarkers3d

public void removeMapMarkers3d(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker3D](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview")\> markers)

    Removes multiple 3D map markers from this map scene. Removing marker instances that are not a part of this scene has no effect.
Parameters:
    `markers` -

    The list of 3D markers to be removed from this map scene.

### removeAllMapMarkers3d

public void removeAllMapMarkers3d()

    Removes all 3D map markers from this map scene.

### addMapPolygon

public void addMapPolygon(@NonNull [MapPolygon](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview") mapPolygon)

    Adds a map polygon to this map scene.

    **Note:** Due to technical limitations using the MapPolygon API to add a very large number of polygons (especially 1000+ also depending on their complexity) is not recommended. Adding this many polygons has a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the [`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") class doc.
Parameters:
    `mapPolygon` -

    The map polygon to be added to this map scene.

### addMapPolygons

public void addMapPolygons(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapPolygon](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview")\> mapPolygons)

    Adds multiple map polygons to this map scene.

    **Note:** Due to technical limitations using the MapPolygon API to add a very large number of polygons (especially 1000+ also depending on their complexity) is not recommended. Adding this many polygons has a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the [`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") class doc.
Parameters:
    `mapPolygons` -

    The map polygons to be added to this map scene.

### removeMapPolygon

public void removeMapPolygon(@NonNull [MapPolygon](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview") mapPolygon)

    Removes a map polygon from this map scene.
Parameters:
    `mapPolygon` -

    The map polygon to be removed from this map scene.

### removeMapPolygons

public void removeMapPolygons(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapPolygon](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview")\> mapPolygons)

    Removes multiple map polygon from this map scene.
Parameters:
    `mapPolygons` -

    The map polygons to be removed from this map scene.

### removeAllMapPolygons

public void removeAllMapPolygons()

    Removes all map polygons from this map scene.

### addMapImageOverlay

public void addMapImageOverlay(@NonNull [MapImageOverlay](sdk-for-android-explore-api-reference-latestmapimageoverlay "class in com.here.sdk.mapview") overlay)

    Adds a map image overlay to this map scene. Adding the same overlay instance multiple times has no effect.
Parameters:
    `overlay` -

    The overlay to be added to this map scene.

### removeMapImageOverlay

public void removeMapImageOverlay(@NonNull [MapImageOverlay](sdk-for-android-explore-api-reference-latestmapimageoverlay "class in com.here.sdk.mapview") overlay)

    Removes a map image overlay from this map scene. Removing an overlay instance that is not part of this scene has no effect.
Parameters:
    `overlay` -

    The overlay to be removed from this map scene.

### setLayerVisibility

public void setLayerVisibility(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) layerName, @NonNull [VisibilityState](sdk-for-android-explore-api-reference-latestvisibilitystate "enum class in com.here.sdk.mapview") visibility)

    Immediately changes the visibility of a specified map layer.
Parameters:
    `layerName` -

    The name of the map layer to be changed.

    `visibility` -

    The new visibility state of the layer.

### getActiveFeatures

@NonNull public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> getActiveFeatures()

    Gets map features that are currently active. Active features are features that are either enabled via a call to [`enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](#enableFeatures(java.util.Map)) or that are enabled by default in the scene.

    The key to the resulting map is the name of the feature and the value is the active mode.

    Result is empty if scene has not been loaded.
Returns:
    The map of active features.

### getSupportedFeatures

@NonNull public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\>\> getSupportedFeatures()

    Gets features and all of their modes supported by the currently loaded scene configuration.

    The key to the resulting map is the name of the feature and the value is a list of modes for that feature.

    Result is empty if scene has not been loaded.
Returns:
    The map of supported features and all their modes.

### enableFeatures

public void enableFeatures(@NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> features)

    Enables specified map features. Those will become active after next map redraw, meaning that [`getActiveFeatures()`](#getActiveFeatures()) will return updated list of active features only after the redraw happens.

    Does not affect features that were not specified. Unsupported features are ignored.

    May cause the current map configuration to be reloaded.

    See [`MapFeatures`](sdk-for-android-explore-api-reference-latestmapfeatures "class in com.here.sdk.mapview") for feature names and [`MapFeatureModes`](sdk-for-android-explore-api-reference-latestmapfeaturemodes "class in com.here.sdk.mapview") for feature mode names.
Parameters:
    `features` -

    The list of features to enable, key is the name of the feature (see [`MapFeatures`](sdk-for-android-explore-api-reference-latestmapfeatures "class in com.here.sdk.mapview")), value specifies its mode (see [`MapFeatureModes`](sdk-for-android-explore-api-reference-latestmapfeaturemodes "class in com.here.sdk.mapview")).

### disableFeatures

public void disableFeatures(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> features)

    Disables specified map features. Those will become inactive after next map redraw, meaning that [`getActiveFeatures()`](#getActiveFeatures()) will return updated list of active features only after the redraw happens.

    Does not affect features that were not specified. Unsupported features are ignored.

    May cause the current map configuration to be reloaded.

    See [`MapFeatures`](sdk-for-android-explore-api-reference-latestmapfeatures "class in com.here.sdk.mapview") for feature names.
Parameters:
    `features` -

    The names of features to disable (see [`MapFeatures`](sdk-for-android-explore-api-reference-latestmapfeatures "class in com.here.sdk.mapview")).

### reloadScene

public void reloadScene()

    Asynchronously reloads the current map scene from file. This skips any cached data used internally and reloads the scene including any changes made to the (custom) map styles in JSON.

    `MapFeature` settings will be preserved.

    Internal optimization checks will be skipped to ensure all custom style changes are loaded. Therefore, calling this method may take slightly longer than calling one of the `loadScene(..)` overloads.

### getLights

@NonNull public [MapSceneLights](sdk-for-android-explore-api-reference-latestmapscenelights "class in com.here.sdk.mapview") getLights()

    Gets a MapSceneLights instance that controls lights present in the scene.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    Provides access to a MapSceneLights instance that controls the lights in the scene.

    The behavior of the returned MapSceneLights instance depends on the state of the scene:

    - If the scene is not loaded, the returned MapSceneLights instance will not contain any light settings, as lights are not loaded without a scene.
    - If the scene is loaded, the returned MapSceneLights instance reflects the current light settings of the loaded scene.

    Scene Change Behavior:

    - If the scene changes, the MapSceneLights instance will be updated to reflect the light settings of the new scene.
    - Any user-defined settings to MapSceneLights will be overridden by the new scene's light settings when the scene changes.

    Error Handling:

    - If the scene is loaded and the loaded scene does not utilize or specify light settings:
      - If the lights are not present, the error callback may return a NO_LIGHTS state.
Returns:
    Controls lights present in the scene.

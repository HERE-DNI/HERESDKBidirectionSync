---
title: "MapScene Class Reference"
slug: "sdk-for-ios-explore-classes-mapscene"
---

# MapScene

<div class="declaration">

<div class="language">

``` highlight
public class MapScene
```

``` highlight
extension MapScene: NativeBase
```

``` highlight
extension MapScene: Hashable
```

</div>

</div>

Represents a map scene and exposes the functionality to manipulate its content.

## Map schemes

The content of the displayed map and how it looks is specified by a <a href="sdk-for-ios-explore-enums-mapscheme">`MapScheme`</a> which is set when loading a scene with

    MapScene.loadScene(MapScheme, MapScene.LoadSceneCompletionHandler?)

. It is also possible to load your own custom map scheme from a file bundled with your application. Supported file formats are:
</p>

- JSON (file extension ‘.json’; e.g. ‘my_custom_style.json’)
- ZIP archive (file extension ‘.zip’; e.g. ‘my_custom_style.zip’), with the following archive structure:
  - root folder: any, not empty (e.g. ‘my_custom_style’)
  - JSON configuration: ‘<root folder>/style.json’</root>
  - custom assets folder: ‘<root folder>/assets’</root>

## Map features

Different map schemes offer different sets of features, for example showing traffic or 3D buildings. Some features have multiple modes of operation, but most have only one.

    MapScene.getSupportedFeatures(...)

can be used to check what features and modes are supported for the current scene. Features can be enabled using

    MapScene.enableFeatures(...)

and disabled with

    MapScene.disableFeatures(...)

. Checking which features are currently enabled can be done using

    MapScene.getActiveFeatures(...)

. For convenience, <a href="sdk-for-ios-explore-structs-mapfeatures">`MapFeatures`</a> and <a href="sdk-for-ios-explore-structs-mapfeaturemodes">`MapFeatureModes`</a> hold constants for feature and mode names.
</p>

Since version 4.15.0, map features cannot be controlled using

    MapScene.setLayerVisibility(...)

, since

    MapScene.setLayerVisibility(...)

controls only visibility of the layers which are corresponding to the features enabled either by

    MapScene.enableFeatures(...)

or enabled by default for the scene.
</p>

## Map layers

A map scheme is organized in layers, which can be controlled using

    MapScene.setLayerVisibility(...)

. It’s possible to change the visibility state of any map layer as long as the name is known.
</p>

Layer visibility settings persist between scene reloading.

## User content

User generated content can be visualised on the map using <a href="sdk-for-ios-explore-classes-mappolyline">`MapPolyline`</a>, <a href="sdk-for-ios-explore-classes-mappolygon">`MapPolygon`</a>, <a href="sdk-for-ios-explore-classes-mapmarker">`MapMarker`</a>, <a href="sdk-for-ios-explore-classes-mapmarkercluster">`MapMarkerCluster`</a>, <a href="sdk-for-ios-explore-classes-maparrow">`MapArrow`</a>, <a href="sdk-for-ios-explore-classes-mapmarker3d">`MapMarker3D`</a> and <a href="sdk-for-ios-explore-classes-mapimageoverlay">`MapImageOverlay`</a> (collectively referred to as “map items”). Those can be added to and removed from the scene by respective add and remove methods. The render order of the map items is according to the list above. The order of objects within the same type can be controlled using the `drawOrder` property of each object.

Be careful when adding a very large number of map items as this can have a negative impact on the performance of the app. To work around this limitation the following approach can be used: Register to map camera updates using

    MapCamera.addDelegate(...)

. Query the bounding box of the camera viewport using <a href="sdk-for-ios-explore-classes-mapcamera#/s:7heresdk9MapCameraC11boundingBoxAA03GeoE0VSgvp">`MapCamera.boundingBox`</a> (it may be extended) and then use the method

    GeoBox.contains(GeoCoordinates)

in combination with <a href="sdk-for-ios-explore-classes-mapcamera-state#/s:7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp">`MapCamera.State.distanceToTargetInMeters`</a> to determine which map items are actually visible to the user in the current camera viewport and thus need to be added to the map.
</p>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk8MapSceneC04LoadC17CompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/LoadSceneCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapscene#/s:7heresdk8MapSceneC04LoadC17CompletionHandlera" class="token"><code>LoadSceneCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called on the main thread after

      loadScene()

  method finishes loading the scene.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias LoadSceneCompletionHandler = ( _ loadSceneError : MapError ?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>loadSceneError</code></em><code> </code></td>
  <td><div>
  <p>The load scene error</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8MapSceneC6lightsAA0bC6LightsCvp"></span>` `<span id="//apple_ref/swift/Property/lights" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapscene#/s:7heresdk8MapSceneC6lightsAA0bC6LightsCvp" class="token"><code>lights</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Controls lights present in the scene. Provides access to a MapSceneLights instance that controls the lights in the scene.

  The behavior of the returned MapSceneLights instance depends on the state of the scene:

  - If the scene is not loaded, the returned MapSceneLights instance will not contain any light settings, as lights are not loaded without a scene.
  - If the scene is loaded, the returned MapSceneLights instance reflects the current light settings of the loaded scene.

  Scene Change Behavior:

  - If the scene changes, the MapSceneLights instance will be updated to reflect the light settings of the new scene.
  - Any user-defined settings to MapSceneLights will be overridden by the new scene’s light settings when the scene changes.

  Error Handling:

  - If the scene is loaded and the loaded scene does not utilize or specify light settings:
    - If the lights are not present, the error callback may return a NO_LIGHTS state.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lights: MapSceneLights { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8MapSceneC0B10PickFilterC"></span>` `<span id="//apple_ref/swift/Class/MapPickFilter" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapscene#/s:7heresdk8MapSceneC0B10PickFilterC" class="token"><code>MapPickFilter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Filter for the map content to be picked.

  <a href="sdk-for-ios-explore-classes-mapscene-mappickfilter" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapPickFilter
  ```

  ``` highlight
  extension MapScene.MapPickFilter: NativeBase
  ```

  ``` highlight
  extension MapScene.MapPickFilter: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      loadScene(mapScheme: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously loads a map scene described by a specified map scheme. Any previous map scene config will be replaced. The loaded scene is cached and so any changes made to the scene files on disk might not get reflected on a successive call to this function. Instead the reloadScene API can handle such use-cases to force-update the scene.

  Map features enabled or disabled using

      MapScene.enableFeatures(...)

  and
      MapScene.disableFeatures(...)

  will be reset to defaults for the new scene configuration.
  </p>

  The callback is called on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadScene ( mapScheme : MapScheme , completion : MapScene . LoadSceneCompletionHandler ?)
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapScheme</code></em><code> </code></td>
  <td><div>
  <p>Map scheme.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Optional callback that will receive the result of this operation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      loadScene(fromFile: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously loads a map scene described by a specified file in one of the supported formats. Any previous map scene config will be replaced.

  When loading the same file again, consider to call

      reloadScene()

  instead.
  </p>

  Map features enabled or disabled using

      MapScene.enableFeatures(...)

  and
      MapScene.disableFeatures(...)

  will be reset to defaults for the new scene configuration.
  </p>

  The callback is called on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadScene ( fromFile configurationFile : String , completion : MapScene . LoadSceneCompletionHandler ?)
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>configurationFile</code></em><code> </code></td>
  <td><div>
  <p>Map scheme configuration file. It must contain the whole scene configuration. In case it contains references to other files, they have to be reachable under the paths specified in the main configuration file.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Optional callback that will receive the result of this operation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      loadScene(fromFile: watermarkStyle: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously loads a map scene described by a specified file in one of the supported formats. The style of the HERE watermark matching the map scheme is specified. Any previous map scene config will be replaced.

  When loading the same file again, consider to call

      reloadScene()

  instead.
  </p>

  Map features enabled or disabled using

      MapScene.enableFeatures(...)

  and
      MapScene.disableFeatures(...)

  will be reset to defaults for the new scene configuration.
  </p>

  The callback is called on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadScene ( fromFile configurationFile : String , watermarkStyle : WatermarkStyle , completion : MapScene . LoadSceneCompletionHandler ?)
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>configurationFile</code></em><code> </code></td>
  <td><div>
  <p>Map scheme configuration file. It must contain the whole scene configuration. In case it contains references to other files, they have to be reachable under the paths specified in the main configuration file.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>watermarkStyle</code></em><code> </code></td>
  <td><div>
  <p>The style for the HERE watermark, see <a href="sdk-for-ios-explore-enums-watermarkstyle"><code>WatermarkStyle</code></a>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Optional callback that will receive the result of this operation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      loadScene(options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously loads a map scene using MapSceneLoadOptions.

  This is an unified API that supports loading from either a map scheme or configuration file, with optional feature and watermark configuration. It’s more efficient to load the scene with this function by specifying the list of enabled features and disabled features, compared to loading the scene first and enabling or disabling map features in the scene loading callback function.

  Configuration defaults are used for features that are not part of the enabled features or disabled features parameters. When a feature is in both the enabled and disabled lists, the feature is considered as requested to be enabled. If the same feature is present multiple times in the enabled list with different modes, then the feature is considered as requested to be enabled, but with an unspecified mode (any of the many specified in the enabled list).

  Any previous map scene config will be replaced. The callback is called on the main thread.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadScene ( options : MapSceneLoadOptions , completion : MapScene . LoadSceneCompletionHandler ?)
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Scene configuration options created using MapSceneLoadOptionsBuilder.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Optional callback that will receive the result of this operation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      addMapPolyline(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a map polyline to this map scene.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapPolyline ( _ mapPolyline : MapPolyline )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapPolyline</code></em><code> </code></td>
  <td><div>
  <p>The map polyline to be added to this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      addMapPolylines(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds map polylines to this map scene.

  **Note:** Due to technical limitations using the MapPolyline API to add a very large number of polylines (especially 1000+ also depending on their complexity) is not recommended. Adding this many polylines has a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the `MapScene` class doc.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapPolylines ( _ mapPolylines : [ MapPolyline ])
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapPolylines</code></em><code> </code></td>
  <td><div>
  <p>The map polylines to be added to this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMapPolyline(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a map polyline from this map scene.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapPolyline ( _ mapPolyline : MapPolyline )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapPolyline</code></em><code> </code></td>
  <td><div>
  <p>The map polyline to be removed from this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMapPolylines(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes map polylines from this map scene.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapPolylines ( _ mapPolylines : [ MapPolyline ])
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapPolylines</code></em><code> </code></td>
  <td><div>
  <p>The map polylines to be removed from this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeAllMapPolylines()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all map polylines from this map scene.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeAllMapPolylines ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      addMapArrow(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a map arrow to this map scene.

  **Note:** Due to technical limitations using the MapArrow API to add a very large number of arrows (especially 1000+ also depending on their complexity) is not recommended. Adding this many arrows has a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the `MapScene` class doc.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapArrow ( _ mapArrow : MapArrow )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapArrow</code></em><code> </code></td>
  <td><div>
  <p>The map arrow to be added to this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMapArrow(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a map arrow from this map scene.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapArrow ( _ mapArrow : MapArrow )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapArrow</code></em><code> </code></td>
  <td><div>
  <p>The map arrow to be removed from this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      addMapMarker(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a map marker to this map scene. Adding the same marker instance multiple times has no effect. Adding a marker that is already part of a map marker cluster has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapMarker ( _ marker : MapMarker )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>marker</code></em><code> </code></td>
  <td><div>
  <p>The marker to be added to this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      addMapMarkers(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds multiple map markers to this map scene. Adding the same marker instances multiple times has no effect. Adding markers that are already part of a map marker cluster has no effect.

  **Note:** Due to technical limitations using the MapMarkers API to add a very large number of markers (several thousands, especially 10000+) is not recommended. Adding this many markers will have a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the `MapScene` class doc.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapMarkers ( _ markers : [ MapMarker ])
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>markers</code></em><code> </code></td>
  <td><div>
  <p>The list of markers to be added to this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMapMarker(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a map marker from this map scene. Removing a marker instance that is not a part of this scene or belongs to a marker cluster has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapMarker ( _ marker : MapMarker )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>marker</code></em><code> </code></td>
  <td><div>
  <p>The marker to be removed from this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMapMarkers(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes multiple map markers from this map scene. Removing marker instances that are not a part of this scene or belong to a marker cluster has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapMarkers ( _ markers : [ MapMarker ])
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>markers</code></em><code> </code></td>
  <td><div>
  <p>The list of markers to be removed from this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeAllMapMarkers()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all map markers from this map scene.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeAllMapMarkers ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      addMapMarkerCluster(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a map marker cluster to the map. Either the contained individual map markers or the cluster markers will be displayed. Adding the same map marker cluster instance multiple times has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapMarkerCluster ( _ cluster : MapMarkerCluster )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>cluster</code></em><code> </code></td>
  <td><div>
  <p>The marker cluster to be added to this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMapMarkerCluster(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a map marker cluster from the map. Removing a map marker cluster that is not on this scene has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapMarkerCluster ( _ cluster : MapMarkerCluster )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>cluster</code></em><code> </code></td>
  <td><div>
  <p>The marker cluster to be removed from this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      addMapMarker3d(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a 3D map marker to this map scene. Does nothing if the marker instance was already added to the scene.

  **Note:** Due to technical limitations using the MapMarker3D API to add a very large number of 3D markers (especially 500+ also depending on the complexity of the 3D object) is not recommended. Adding this many 3D markers has a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the `MapScene` class doc.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapMarker3d ( _ marker : MapMarker3D )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>marker</code></em><code> </code></td>
  <td><div>
  <p>The marker to be added to this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      addMapMarkers3d(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds multiple 3D map markers to this map scene. Adding the same 3D marker instances multiple times has no effect.

  **Note:** Due to technical limitations, using the MapMarkers3D API to add a very large number of 3D markers (especially 500+) is not recommended. Adding this many markers will have a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the `MapScene` class doc.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapMarkers3d ( _ markers : [ MapMarker3D ])
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>markers</code></em><code> </code></td>
  <td><div>
  <p>The list of 3D markers to be added to this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMapMarker3d(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a 3D map marker from this map scene. Removing a marker instance that is not on this scene has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapMarker3d ( _ marker : MapMarker3D )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>marker</code></em><code> </code></td>
  <td><div>
  <p>The marker to be removed from this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMapMarkers3d(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes multiple 3D map markers from this map scene. Removing marker instances that are not a part of this scene has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapMarkers3d ( _ markers : [ MapMarker3D ])
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>markers</code></em><code> </code></td>
  <td><div>
  <p>The list of 3D markers to be removed from this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeAllMapMarkers3d()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all 3D map markers from this map scene.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeAllMapMarkers3d ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      addMapPolygon(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a map polygon to this map scene.

  **Note:** Due to technical limitations using the MapPolygon API to add a very large number of polygons (especially 1000+ also depending on their complexity) is not recommended. Adding this many polygons has a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the `MapScene` class doc.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapPolygon ( _ mapPolygon : MapPolygon )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapPolygon</code></em><code> </code></td>
  <td><div>
  <p>The map polygon to be added to this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      addMapPolygons(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds multiple map polygons to this map scene.

  **Note:** Due to technical limitations using the MapPolygon API to add a very large number of polygons (especially 1000+ also depending on their complexity) is not recommended. Adding this many polygons has a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the `MapScene` class doc.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapPolygons ( _ mapPolygons : [ MapPolygon ])
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapPolygons</code></em><code> </code></td>
  <td><div>
  <p>The map polygons to be added to this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMapPolygon(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a map polygon from this map scene.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapPolygon ( _ mapPolygon : MapPolygon )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapPolygon</code></em><code> </code></td>
  <td><div>
  <p>The map polygon to be removed from this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMapPolygons(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes multiple map polygon from this map scene.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapPolygons ( _ mapPolygons : [ MapPolygon ])
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapPolygons</code></em><code> </code></td>
  <td><div>
  <p>The map polygons to be removed from this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeAllMapPolygons()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all map polygons from this map scene.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeAllMapPolygons ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      addMapImageOverlay(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a map image overlay to this map scene. Adding the same overlay instance multiple times has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapImageOverlay ( _ overlay : MapImageOverlay )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>overlay</code></em><code> </code></td>
  <td><div>
  <p>The overlay to be added to this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMapImageOverlay(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a map image overlay from this map scene. Removing an overlay instance that is not part of this scene has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapImageOverlay ( _ overlay : MapImageOverlay )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>overlay</code></em><code> </code></td>
  <td><div>
  <p>The overlay to be removed from this map scene.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeAllMapItems()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all map objects from this map scene. This includes polylines, polygons, markers and clusters, arrows, image overlays. It is much faster than removing the objects one by one.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeAllMapItems ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      setLayerVisibility(layerName: visibility: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Immediately changes the visibility of a specified map layer.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setLayerVisibility ( layerName : String , visibility : VisibilityState )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>layerName</code></em><code> </code></td>
  <td><div>
  <p>The name of the map layer to be changed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>visibility</code></em><code> </code></td>
  <td><div>
  <p>The new visibility state of the layer.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      getActiveFeatures()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets map features that are currently active. Active features are features that are either enabled via a call to

      MapScene.enableFeatures(...)

  or that are enabled by default in the scene.
  </p>

  The key to the resulting map is the name of the feature and the value is the active mode.

  Result is empty if scene has not been loaded.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getActiveFeatures () -> [ String : String ]
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  The map of active features.

  </div>

  </div>

  </div>

- <div>

      getSupportedFeatures()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets features and all of their modes supported by the currently loaded scene configuration.

  The key to the resulting map is the name of the feature and the value is a list of modes for that feature.

  Result is empty if scene has not been loaded.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getSupportedFeatures () -> [ String : [ String ]]
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  The map of supported features and all their modes.

  </div>

  </div>

  </div>

- <div>

      enableFeatures(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enables specified map features. Those will become active after next map redraw, meaning that

      MapScene.getActiveFeatures(...)

  will return updated list of active features only after the redraw happens.
  </p>

  Does not affect features that were not specified. Unsupported features are ignored.

  May cause the current map configuration to be reloaded.

  See <a href="sdk-for-ios-explore-structs-mapfeatures">`MapFeatures`</a> for feature names and <a href="sdk-for-ios-explore-structs-mapfeaturemodes">`MapFeatureModes`</a> for feature mode names.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func enableFeatures ( _ features : [ String : String ])
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>features</code></em><code> </code></td>
  <td><div>
  <p>The list of features to enable, key is the name of the feature (see <a href="sdk-for-ios-explore-structs-mapfeatures"><code>MapFeatures</code></a>), value specifies its mode (see <a href="sdk-for-ios-explore-structs-mapfeaturemodes"><code>MapFeatureModes</code></a>).</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      disableFeatures(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Disables specified map features. Those will become inactive after next map redraw, meaning that

      MapScene.getActiveFeatures(...)

  will return updated list of active features only after the redraw happens.
  </p>

  Does not affect features that were not specified. Unsupported features are ignored.

  May cause the current map configuration to be reloaded.

  See <a href="sdk-for-ios-explore-structs-mapfeatures">`MapFeatures`</a> for feature names.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func disableFeatures ( _ features : [ String ])
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>features</code></em><code> </code></td>
  <td><div>
  <p>The names of features to disable (see <a href="sdk-for-ios-explore-structs-mapfeatures"><code>MapFeatures</code></a>).</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      reloadScene()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously reloads the current map scene from file. This skips any cached data used internally and reloads the scene including any changes made to the (custom) map styles in JSON.

  `MapFeature` settings will be preserved.

  Internal optimization checks will be skipped to ensure all custom style changes are loaded. Therefore, calling this method may take slightly longer than calling one of the

      loadScene(..)

  overloads.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func reloadScene ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>


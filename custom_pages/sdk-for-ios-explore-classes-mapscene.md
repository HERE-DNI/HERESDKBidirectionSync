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

Different map schemes offer different sets of features, for example showing traffic or 3D buildings. Some features have multiple modes of operation, but most have only one. <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC20getSupportedFeaturesSDySSSaySSGGyF">`MapScene.getSupportedFeatures(...)`</a> can be used to check what features and modes are supported for the current scene. Features can be enabled using <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">`MapScene.enableFeatures(...)`</a> and disabled with <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC15disableFeaturesyySaySSGF">`MapScene.disableFeatures(...)`</a>. Checking which features are currently enabled can be done using <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF">`MapScene.getActiveFeatures(...)`</a>. For convenience, <a href="sdk-for-ios-explore-structs-mapfeatures">`MapFeatures`</a> and <a href="sdk-for-ios-explore-structs-mapfeaturemodes">`MapFeatureModes`</a> hold constants for feature and mode names.

Since version 4.15.0, map features cannot be controlled using <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF">`MapScene.setLayerVisibility(...)`</a>, since <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF">`MapScene.setLayerVisibility(...)`</a> controls only visibility of the layers which are corresponding to the features enabled either by <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">`MapScene.enableFeatures(...)`</a> or enabled by default for the scene.

## Map layers

A map scheme is organized in layers, which can be controlled using <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF">`MapScene.setLayerVisibility(...)`</a>. It’s possible to change the visibility state of any map layer as long as the name is known.

Layer visibility settings persist between scene reloading.

## User content

User generated content can be visualised on the map using <a href="sdk-for-ios-explore-classes-mappolyline">`MapPolyline`</a>, <a href="sdk-for-ios-explore-classes-mappolygon">`MapPolygon`</a>, <a href="sdk-for-ios-explore-classes-mapmarker">`MapMarker`</a>, <a href="sdk-for-ios-explore-classes-mapmarkercluster">`MapMarkerCluster`</a>, <a href="sdk-for-ios-explore-classes-maparrow">`MapArrow`</a>, <a href="sdk-for-ios-explore-classes-mapmarker3d">`MapMarker3D`</a> and <a href="sdk-for-ios-explore-classes-mapimageoverlay">`MapImageOverlay`</a> (collectively referred to as “map items”). Those can be added to and removed from the scene by respective add and remove methods. The render order of the map items is according to the list above. The order of objects within the same type can be controlled using the `drawOrder` property of each object.

Be careful when adding a very large number of map items as this can have a negative impact on the performance of the app. To work around this limitation the following approach can be used: Register to map camera updates using <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC11addDelegateyyAA0bcE0_pF">`MapCamera.addDelegate(...)`</a>. Query the bounding box of the camera viewport using <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC11boundingBoxAA03GeoE0VSgvp">`MapCamera.boundingBox`</a> (it may be extended) and then use the method

    GeoBox.contains(GeoCoordinates)

in combination with <a href="sdk-for-ios-explore-classes-mapcamera-state#sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp">`MapCamera.State.distanceToTargetInMeters`</a> to determine which map items are actually visible to the user in the current camera viewport and thus need to be added to the map.
</p>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC04LoadC17CompletionHandlera"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Alias-LoadSceneCompletionHandler" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC04LoadC17CompletionHandlera" class="token"><code>LoadSceneCompletionHandler</code></a> 

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
  public typealias LoadSceneCompletionHandler = (_ loadSceneError: MapError?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-maperror">MapError</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC6lightsAA0bC6LightsCvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-lights" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC6lightsAA0bC6LightsCvp" class="token"><code>lights</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapscenelights">MapSceneLights</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC0B10PickFilterC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-MapPickFilter" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC0B10PickFilterC" class="token"><code>MapPickFilter</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapscene">MapScene</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC04loadC09mapScheme10completionyAA0bF0O_yAA0B5ErrorOSgcSgtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-loadScene-mapScheme-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC04loadC09mapScheme10completionyAA0bF0O_yAA0B5ErrorOSgcSgtF" class="token"><code>loadScene(mapScheme:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously loads a map scene described by a specified map scheme. Any previous map scene config will be replaced. The loaded scene is cached and so any changes made to the scene files on disk might not get reflected on a successive call to this function. Instead the reloadScene API can handle such use-cases to force-update the scene.

  Map features enabled or disabled using <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">`MapScene.enableFeatures(...)`</a> and <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC15disableFeaturesyySaySSGF">`MapScene.disableFeatures(...)`</a> will be reset to defaults for the new scene configuration.

  The callback is called on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadScene(mapScheme: MapScheme, completion: MapScene.LoadSceneCompletionHandler?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-mapscheme">MapScheme</a>
  - <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC04LoadC17CompletionHandlera">LoadSceneCompletionHandler</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC04loadC08fromFile10completionySS_yAA0B5ErrorOSgcSgtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-loadScene-fromFile-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC04loadC08fromFile10completionySS_yAA0B5ErrorOSgcSgtF" class="token"><code>loadScene(fromFile:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously loads a map scene described by a specified file in one of the supported formats. Any previous map scene config will be replaced.

  When loading the same file again, consider to call <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06reloadC0yyF">`reloadScene()`</a> instead.

  Map features enabled or disabled using <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">`MapScene.enableFeatures(...)`</a> and <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC15disableFeaturesyySaySSGF">`MapScene.disableFeatures(...)`</a> will be reset to defaults for the new scene configuration.

  The callback is called on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadScene(fromFile configurationFile: String, completion: MapScene.LoadSceneCompletionHandler?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC04LoadC17CompletionHandlera">LoadSceneCompletionHandler</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC04loadC08fromFile14watermarkStyle10completionySS_AA09WatermarkH0OyAA0B5ErrorOSgcSgtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-loadScene-fromFile-watermarkStyle-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC04loadC08fromFile14watermarkStyle10completionySS_AA09WatermarkH0OyAA0B5ErrorOSgcSgtF" class="token"><code>loadScene(fromFile:</code><wbr></wbr><code>watermarkStyle:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously loads a map scene described by a specified file in one of the supported formats. The style of the HERE watermark matching the map scheme is specified. Any previous map scene config will be replaced.

  When loading the same file again, consider to call <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06reloadC0yyF">`reloadScene()`</a> instead.

  Map features enabled or disabled using <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">`MapScene.enableFeatures(...)`</a> and <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC15disableFeaturesyySaySSGF">`MapScene.disableFeatures(...)`</a> will be reset to defaults for the new scene configuration.

  The callback is called on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadScene(fromFile configurationFile: String, watermarkStyle: WatermarkStyle, completion: MapScene.LoadSceneCompletionHandler?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-watermarkstyle">WatermarkStyle</a>
  - <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC04LoadC17CompletionHandlera">LoadSceneCompletionHandler</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC04loadC07options10completionyAA0bC11LoadOptionsC_yAA0B5ErrorOSgcSgtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-loadScene-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC04loadC07options10completionyAA0bC11LoadOptionsC_yAA0B5ErrorOSgcSgtF" class="token"><code>loadScene(options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

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
  public func loadScene(options: MapSceneLoadOptions, completion: MapScene.LoadSceneCompletionHandler?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-maps#sdk-for-ios-explore-s-7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a>
  - <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC04LoadC17CompletionHandlera">LoadSceneCompletionHandler</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC03addB8PolylineyyAA0bE0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addMapPolyline-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC03addB8PolylineyyAA0bE0CF" class="token"><code>addMapPolyline(_:</code><wbr></wbr><code>)</code></a> 

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
  public func addMapPolyline(_ mapPolyline: MapPolyline)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolyline">MapPolyline</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC03addB9PolylinesyySayAA0B8PolylineCGF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addMapPolylines-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC03addB9PolylinesyySayAA0B8PolylineCGF" class="token"><code>addMapPolylines(_:</code><wbr></wbr><code>)</code></a> 

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
  public func addMapPolylines(_ mapPolylines: [MapPolyline])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolyline">MapPolyline</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB8PolylineyyAA0bE0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeMapPolyline-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB8PolylineyyAA0bE0CF" class="token"><code>removeMapPolyline(_:</code><wbr></wbr><code>)</code></a> 

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
  public func removeMapPolyline(_ mapPolyline: MapPolyline)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolyline">MapPolyline</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB9PolylinesyySayAA0B8PolylineCGF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeMapPolylines-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB9PolylinesyySayAA0B8PolylineCGF" class="token"><code>removeMapPolylines(_:</code><wbr></wbr><code>)</code></a> 

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
  public func removeMapPolylines(_ mapPolylines: [MapPolyline])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolyline">MapPolyline</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC09removeAllB9PolylinesyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeAllMapPolylines" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC09removeAllB9PolylinesyyF" class="token"><code>removeAllMapPolylines()</code></a> 

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
  public func removeAllMapPolylines()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC03addB5ArrowyyAA0bE0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addMapArrow-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC03addB5ArrowyyAA0bE0CF" class="token"><code>addMapArrow(_:</code><wbr></wbr><code>)</code></a> 

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
  public func addMapArrow(_ mapArrow: MapArrow)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-maparrow">MapArrow</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB5ArrowyyAA0bE0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeMapArrow-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB5ArrowyyAA0bE0CF" class="token"><code>removeMapArrow(_:</code><wbr></wbr><code>)</code></a> 

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
  public func removeMapArrow(_ mapArrow: MapArrow)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-maparrow">MapArrow</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC03addB6MarkeryyAA0bE0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addMapMarker-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC03addB6MarkeryyAA0bE0CF" class="token"><code>addMapMarker(_:</code><wbr></wbr><code>)</code></a> 

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
  public func addMapMarker(_ marker: MapMarker)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapmarker">MapMarker</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC03addB7MarkersyySayAA0B6MarkerCGF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addMapMarkers-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC03addB7MarkersyySayAA0B6MarkerCGF" class="token"><code>addMapMarkers(_:</code><wbr></wbr><code>)</code></a> 

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
  public func addMapMarkers(_ markers: [MapMarker])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapmarker">MapMarker</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB6MarkeryyAA0bE0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeMapMarker-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB6MarkeryyAA0bE0CF" class="token"><code>removeMapMarker(_:</code><wbr></wbr><code>)</code></a> 

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
  public func removeMapMarker(_ marker: MapMarker)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapmarker">MapMarker</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB7MarkersyySayAA0B6MarkerCGF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeMapMarkers-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB7MarkersyySayAA0B6MarkerCGF" class="token"><code>removeMapMarkers(_:</code><wbr></wbr><code>)</code></a> 

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
  public func removeMapMarkers(_ markers: [MapMarker])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapmarker">MapMarker</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC09removeAllB7MarkersyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeAllMapMarkers" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC09removeAllB7MarkersyyF" class="token"><code>removeAllMapMarkers()</code></a> 

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
  public func removeAllMapMarkers()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC03addB13MarkerClusteryyAA0beF0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addMapMarkerCluster-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC03addB13MarkerClusteryyAA0beF0CF" class="token"><code>addMapMarkerCluster(_:</code><wbr></wbr><code>)</code></a> 

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
  public func addMapMarkerCluster(_ cluster: MapMarkerCluster)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapmarkercluster">MapMarkerCluster</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB13MarkerClusteryyAA0beF0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeMapMarkerCluster-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB13MarkerClusteryyAA0beF0CF" class="token"><code>removeMapMarkerCluster(_:</code><wbr></wbr><code>)</code></a> 

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
  public func removeMapMarkerCluster(_ cluster: MapMarkerCluster)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapmarkercluster">MapMarkerCluster</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC03addB8Marker3dyyAA0B8Marker3DCF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addMapMarker3d-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC03addB8Marker3dyyAA0B8Marker3DCF" class="token"><code>addMapMarker3d(_:</code><wbr></wbr><code>)</code></a> 

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
  public func addMapMarker3d(_ marker: MapMarker3D)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapmarker3d">MapMarker3D</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC03addB9Markers3dyySayAA0B8Marker3DCGF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addMapMarkers3d-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC03addB9Markers3dyySayAA0B8Marker3DCGF" class="token"><code>addMapMarkers3d(_:</code><wbr></wbr><code>)</code></a> 

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
  public func addMapMarkers3d(_ markers: [MapMarker3D])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapmarker3d">MapMarker3D</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB8Marker3dyyAA0B8Marker3DCF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeMapMarker3d-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB8Marker3dyyAA0B8Marker3DCF" class="token"><code>removeMapMarker3d(_:</code><wbr></wbr><code>)</code></a> 

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
  public func removeMapMarker3d(_ marker: MapMarker3D)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapmarker3d">MapMarker3D</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB9Markers3dyySayAA0B8Marker3DCGF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeMapMarkers3d-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB9Markers3dyySayAA0B8Marker3DCGF" class="token"><code>removeMapMarkers3d(_:</code><wbr></wbr><code>)</code></a> 

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
  public func removeMapMarkers3d(_ markers: [MapMarker3D])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapmarker3d">MapMarker3D</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC09removeAllB9Markers3dyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeAllMapMarkers3d" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC09removeAllB9Markers3dyyF" class="token"><code>removeAllMapMarkers3d()</code></a> 

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
  public func removeAllMapMarkers3d()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC03addB7PolygonyyAA0bE0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addMapPolygon-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC03addB7PolygonyyAA0bE0CF" class="token"><code>addMapPolygon(_:</code><wbr></wbr><code>)</code></a> 

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
  public func addMapPolygon(_ mapPolygon: MapPolygon)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolygon">MapPolygon</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC03addB8PolygonsyySayAA0B7PolygonCGF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addMapPolygons-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC03addB8PolygonsyySayAA0B7PolygonCGF" class="token"><code>addMapPolygons(_:</code><wbr></wbr><code>)</code></a> 

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
  public func addMapPolygons(_ mapPolygons: [MapPolygon])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolygon">MapPolygon</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB7PolygonyyAA0bE0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeMapPolygon-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB7PolygonyyAA0bE0CF" class="token"><code>removeMapPolygon(_:</code><wbr></wbr><code>)</code></a> 

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
  public func removeMapPolygon(_ mapPolygon: MapPolygon)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolygon">MapPolygon</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB8PolygonsyySayAA0B7PolygonCGF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeMapPolygons-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB8PolygonsyySayAA0B7PolygonCGF" class="token"><code>removeMapPolygons(_:</code><wbr></wbr><code>)</code></a> 

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
  public func removeMapPolygons(_ mapPolygons: [MapPolygon])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolygon">MapPolygon</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC09removeAllB8PolygonsyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeAllMapPolygons" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC09removeAllB8PolygonsyyF" class="token"><code>removeAllMapPolygons()</code></a> 

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
  public func removeAllMapPolygons()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC03addB12ImageOverlayyyAA0beF0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addMapImageOverlay-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC03addB12ImageOverlayyyAA0beF0CF" class="token"><code>addMapImageOverlay(_:</code><wbr></wbr><code>)</code></a> 

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
  public func addMapImageOverlay(_ overlay: MapImageOverlay)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapimageoverlay">MapImageOverlay</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB12ImageOverlayyyAA0beF0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeMapImageOverlay-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06removeB12ImageOverlayyyAA0beF0CF" class="token"><code>removeMapImageOverlay(_:</code><wbr></wbr><code>)</code></a> 

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
  public func removeMapImageOverlay(_ overlay: MapImageOverlay)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapimageoverlay">MapImageOverlay</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC09removeAllB5ItemsyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeAllMapItems" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC09removeAllB5ItemsyyF" class="token"><code>removeAllMapItems()</code></a> 

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
  public func removeAllMapItems()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setLayerVisibility-layerName-visibility" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF" class="token"><code>setLayerVisibility(layerName:</code><wbr></wbr><code>visibility:</code><wbr></wbr><code>)</code></a> 

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
  public func setLayerVisibility(layerName: String, visibility: VisibilityState)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-visibilitystate">VisibilityState</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getActiveFeatures" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF" class="token"><code>getActiveFeatures()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets map features that are currently active. Active features are features that are either enabled via a call to <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">`MapScene.enableFeatures(...)`</a> or that are enabled by default in the scene.

  The key to the resulting map is the name of the feature and the value is the active mode.

  Result is empty if scene has not been loaded.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getActiveFeatures() -> [String : String]
  ```

  </div>

  </div>

  <div>

  #### Return Value

  The map of active features.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC20getSupportedFeaturesSDySSSaySSGGyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getSupportedFeatures" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC20getSupportedFeaturesSDySSSaySSGGyF" class="token"><code>getSupportedFeatures()</code></a> 

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
  public func getSupportedFeatures() -> [String : [String]]
  ```

  </div>

  </div>

  <div>

  #### Return Value

  The map of supported features and all their modes.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC14enableFeaturesyySDyS2SGF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-enableFeatures-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC14enableFeaturesyySDyS2SGF" class="token"><code>enableFeatures(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enables specified map features. Those will become active after next map redraw, meaning that <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF">`MapScene.getActiveFeatures(...)`</a> will return updated list of active features only after the redraw happens.

  Does not affect features that were not specified. Unsupported features are ignored.

  May cause the current map configuration to be reloaded.

  See <a href="sdk-for-ios-explore-structs-mapfeatures">`MapFeatures`</a> for feature names and <a href="sdk-for-ios-explore-structs-mapfeaturemodes">`MapFeatureModes`</a> for feature mode names.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func enableFeatures(_ features: [String : String])
  ```

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC15disableFeaturesyySaySSGF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-disableFeatures-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC15disableFeaturesyySaySSGF" class="token"><code>disableFeatures(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Disables specified map features. Those will become inactive after next map redraw, meaning that <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF">`MapScene.getActiveFeatures(...)`</a> will return updated list of active features only after the redraw happens.

  Does not affect features that were not specified. Unsupported features are ignored.

  May cause the current map configuration to be reloaded.

  See <a href="sdk-for-ios-explore-structs-mapfeatures">`MapFeatures`</a> for feature names.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func disableFeatures(_ features: [String])
  ```

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

   <span id="sdk-for-ios-explore-s-7heresdk8MapSceneC06reloadC0yyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-reloadScene" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC06reloadC0yyF" class="token"><code>reloadScene()</code></a> 

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
  public func reloadScene()
  ```

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


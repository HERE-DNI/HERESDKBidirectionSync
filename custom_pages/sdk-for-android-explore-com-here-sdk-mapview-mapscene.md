---
title: "MapScene (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapscene"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.mapview.MapScene →
com.here.NativeBase → com.here.sdk.mapview.MapScene

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapScene</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Represents a map scene and exposes the functionality to manipulate its
content. The content of the displayed map and how it looks is specified
by a MapScheme which is set when loading a scene with
loadScene(MapScheme, MapScene.LoadSceneCallback) . It is also possible
to load your own custom map scheme from a file bundled with your
application. Supported file formats are: JSON (file extension '.json';
e.g. 'my_custom_style.json') ZIP archive (file extension '.zip'; e.g.
'my_custom_style.zip'), with the following archive structure: root
folder: any, not empty (e.g. 'my_custom_style') JSON configuration: '
/style.json' custom assets folder: ' /assets' Different map schemes
offer different sets of features, for example showing traffic or 3D
buildings. Some features have multiple modes of operation, but most have
only one. getSupportedFeatures() can be used to check what features and
modes are supported for the current scene. Features can be enabled using
enableFeatures(java.util.Map ) and disabled with
disableFeatures(java.util.List ) . Checking which features are currently
enabled can be done using getActiveFeatures() . For convenience,
MapFeatures and MapFeatureModes hold constants for feature and mode
names. Since version 4.15.0, map features cannot be controlled using
setLayerVisibility(java.lang.String,
com.here.sdk.mapview.VisibilityState) , since
setLayerVisibility(java.lang.String,
com.here.sdk.mapview.VisibilityState) controls only visibility of the
layers which are corresponding to the features enabled either by
enableFeatures(java.util.Map ) or enabled by default for the scene. A
map scheme is organized in layers, which can be controlled using
setLayerVisibility(java.lang.String,
com.here.sdk.mapview.VisibilityState) . It's possible to change the
visibility state of any map layer as long as the name is known. Layer
visibility settings persist between scene reloading. User generated
content can be visualised on the map using MapPolyline , MapPolygon ,
MapMarker , MapMarkerCluster , MapArrow , MapMarker3D and
MapImageOverlay (collectively referred to as "map items"). Those can be
added to and removed from the scene by respective add and remove
methods. The render order of the map items is according to the list
above. The order of objects within the same type can be controlled using
the setDrawOrder() method of each object. Be careful when adding a very
large number of map items as this can have a negative impact on the
performance of the app. To work around this limitation the following
approach can be used: Register to map camera updates using
MapCamera.addListener(com.here.sdk.mapview.MapCameraListener) . Query
the bounding box of the camera viewport using MapCamera.getBoundingBox()
(it may be extended) and then use the method
GeoBox.contains(GeoCoordinates) in combination with
MapCamera.State.distanceToTargetInMeters to determine which map items
are actually visible to the user in the current camera viewport and thus
need to be added to the map.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static interface </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscene-loadscenecallback"
  class="type-name-link"
  title="interface in com.here.sdk.mapview"><code>MapScene.LoadSceneCallback</code></a></td>
  <td><div class="block">
  Called on the main thread after loadScene() method finishes loading the
  scene.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscene-mappickfilter"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapScene.MapPickFilter</code></a></td>
  <td><div class="block">
  Filter for the map content to be picked.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>addMapArrow(MapArrow mapArrow)</code></pre></td>
  <td><div class="block">
  Adds a map arrow to this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>addMapImageOverlay(MapImageOverlay overlay)</code></pre></td>
  <td><div class="block">
  Adds a map image overlay to this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>addMapMarker(MapMarker marker)</code></pre></td>
  <td><div class="block">
  Adds a map marker to this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>addMapMarker3d(MapMarker3D marker)</code></pre></td>
  <td><div class="block">
  Adds a 3D map marker to this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>addMapMarkerCluster(MapMarkerCluster cluster)</code></pre></td>
  <td><div class="block">
  Adds a map marker cluster to the map.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>addMapMarkers(List&lt;MapMarker&gt; markers)</code></pre></td>
  <td><div class="block">
  Adds multiple map markers to this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>addMapMarkers3d(List&lt;MapMarker3D&gt; markers)</code></pre></td>
  <td><div class="block">
  Adds multiple 3D map markers to this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>addMapPolygon(MapPolygon mapPolygon)</code></pre></td>
  <td><div class="block">
  Adds a map polygon to this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>addMapPolygons(List&lt;MapPolygon&gt; mapPolygons)</code></pre></td>
  <td><div class="block">
  Adds multiple map polygons to this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>addMapPolyline(MapPolyline mapPolyline)</code></pre></td>
  <td><div class="block">
  Adds a map polyline to this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>addMapPolylines(List&lt;MapPolyline&gt; mapPolylines)</code></pre></td>
  <td><div class="block">
  Adds map polylines to this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>disableFeatures(List&lt;String&gt; features)</code></pre></td>
  <td><div class="block">
  Disables specified map features.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>enableFeatures(Map&lt;String,String&gt; features)</code></pre></td>
  <td><div class="block">
  Enables specified map features.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a><code>,</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a><code>&gt;</code></td>
  <td><pre><code>getActiveFeatures()</code></pre></td>
  <td><div class="block">
  Gets map features that are currently active.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights"
  title="class in com.here.sdk.mapview"><code>MapSceneLights</code></a></td>
  <td><pre><code>getLights()</code></pre></td>
  <td><div class="block">
  Gets a MapSceneLights instance that controls lights present in the
  scene.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a><code>,</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a><code>&gt;&gt;</code></td>
  <td><pre><code>getSupportedFeatures()</code></pre></td>
  <td><div class="block">
  Gets features and all of their modes supported by the currently loaded
  scene configuration.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>loadScene(MapSceneLoadOptions options,
   MapScene.LoadSceneCallback callback)</code></pre></td>
  <td><div class="block">
  Asynchronously loads a map scene using MapSceneLoadOptions.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>loadScene(MapScheme mapScheme,
   MapScene.LoadSceneCallback callback)</code></pre></td>
  <td><div class="block">
  Asynchronously loads a map scene described by a specified map scheme.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>loadScene(String configurationFile,
   MapScene.LoadSceneCallback callback)</code></pre></td>
  <td><div class="block">
  Asynchronously loads a map scene described by a specified file in one of
  the supported formats.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>loadScene(String configurationFile,
   WatermarkStyle watermarkStyle,
   MapScene.LoadSceneCallback callback)</code></pre></td>
  <td><div class="block">
  Asynchronously loads a map scene described by a specified file in one of
  the supported formats.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>reloadScene()</code></pre></td>
  <td><div class="block">
  Asynchronously reloads the current map scene from file.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeAllMapItems()</code></pre></td>
  <td><div class="block">
  Removes all map objects from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeAllMapMarkers()</code></pre></td>
  <td><div class="block">
  Removes all map markers from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeAllMapMarkers3d()</code></pre></td>
  <td><div class="block">
  Removes all 3D map markers from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeAllMapPolygons()</code></pre></td>
  <td><div class="block">
  Removes all map polygons from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeAllMapPolylines()</code></pre></td>
  <td><div class="block">
  Removes all map polylines from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeMapArrow(MapArrow mapArrow)</code></pre></td>
  <td><div class="block">
  Removes a map arrow from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeMapImageOverlay(MapImageOverlay overlay)</code></pre></td>
  <td><div class="block">
  Removes a map image overlay from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeMapMarker(MapMarker marker)</code></pre></td>
  <td><div class="block">
  Removes a map marker from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeMapMarker3d(MapMarker3D marker)</code></pre></td>
  <td><div class="block">
  Removes a 3D map marker from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeMapMarkerCluster(MapMarkerCluster cluster)</code></pre></td>
  <td><div class="block">
  Removes a map marker cluster from the map.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeMapMarkers(List&lt;MapMarker&gt; markers)</code></pre></td>
  <td><div class="block">
  Removes multiple map markers from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeMapMarkers3d(List&lt;MapMarker3D&gt; markers)</code></pre></td>
  <td><div class="block">
  Removes multiple 3D map markers from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeMapPolygon(MapPolygon mapPolygon)</code></pre></td>
  <td><div class="block">
  Removes a map polygon from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeMapPolygons(List&lt;MapPolygon&gt; mapPolygons)</code></pre></td>
  <td><div class="block">
  Removes multiple map polygon from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeMapPolyline(MapPolyline mapPolyline)</code></pre></td>
  <td><div class="block">
  Removes a map polyline from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeMapPolylines(List&lt;MapPolyline&gt; mapPolylines)</code></pre></td>
  <td><div class="block">
  Removes map polylines from this map scene.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setLayerVisibility(String layerName,
   VisibilityState visibility)</code></pre></td>
  <td><div class="block">
  Immediately changes the visibility of a specified map layer.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)"
    class="section detail">

    ### loadScene

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadScene</span><span class="parameters">(@NonNull
    [MapScheme](sdk-for-android-explore-com-here-sdk-mapview-mapscheme "enum class in com.here.sdk.mapview") mapScheme,
    @Nullable
    [MapScene.LoadSceneCallback](sdk-for-android-explore-com-here-sdk-mapview-mapscene-loadscenecallback "interface in com.here.sdk.mapview") callback)</span>

    </div>

    <div class="block">

    Asynchronously loads a map scene described by a specified map
    scheme. Any previous map scene config will be replaced. The loaded
    scene is cached and so any changes made to the scene files on disk
    might not get reflected on a successive call to this function.
    Instead the reloadScene API can handle such use-cases to
    force-update the scene. Map features enabled or disabled using
    enableFeatures(java.util.Map ) and disableFeatures(java.util.List )
    will be reset to defaults for the new scene configuration. The
    callback is called on the main thread. When recreating an activity
    following a device rotation, it is not necessary to call this method
    a second time. The map scheme that was loaded when the map view was
    initially created will continue to be used.

    </div>

    Parameters:  
    `mapScheme` -

    Map scheme.

    `callback` -

    Optional callback that will receive the result of this operation.

    </div>

  - <div id="loadScene(java.lang.String,com.here.sdk.mapview.MapScene.LoadSceneCallback)"
    class="section detail">

    ### loadScene

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadScene</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> configurationFile,
    @Nullable
    [MapScene.LoadSceneCallback](sdk-for-android-explore-com-here-sdk-mapview-mapscene-loadscenecallback "interface in com.here.sdk.mapview") callback)</span>

    </div>

    <div class="block">

    Asynchronously loads a map scene described by a specified file in
    one of the supported formats. Any previous map scene config will be
    replaced. When loading the same file again, consider to call
    reloadScene() instead. Map features enabled or disabled using
    enableFeatures(java.util.Map ) and disableFeatures(java.util.List )
    will be reset to defaults for the new scene configuration. The
    callback is called on the main thread. When recreating an activity
    following a device rotation, it is not necessary to call this method
    a second time. The map scheme that was loaded when the map view was
    initially created will continue to be used.

    </div>

    Parameters:  
    `configurationFile` -

    Map scheme configuration file. It must contain the whole scene
    configuration. In case it contains references to other files, they
    have to be reachable under the paths specified in the main
    configuration file.

    `callback` -

    Optional callback that will receive the result of this operation.

    </div>

  - <div id="loadScene(java.lang.String,com.here.sdk.mapview.WatermarkStyle,com.here.sdk.mapview.MapScene.LoadSceneCallback)"
    class="section detail">

    ### loadScene

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadScene</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> configurationFile,
    @NonNull
    [WatermarkStyle](sdk-for-android-explore-com-here-sdk-mapview-watermarkstyle "enum class in com.here.sdk.mapview") watermarkStyle,
    @Nullable
    [MapScene.LoadSceneCallback](sdk-for-android-explore-com-here-sdk-mapview-mapscene-loadscenecallback "interface in com.here.sdk.mapview") callback)</span>

    </div>

    <div class="block">

    Asynchronously loads a map scene described by a specified file in
    one of the supported formats. The style of the HERE watermark
    matching the map scheme is specified. Any previous map scene config
    will be replaced. When loading the same file again, consider to call
    reloadScene() instead. Map features enabled or disabled using
    enableFeatures(java.util.Map ) and disableFeatures(java.util.List )
    will be reset to defaults for the new scene configuration. The
    callback is called on the main thread. When recreating an activity
    following a device rotation, it is not necessary to call this method
    a second time. The map scheme that was loaded when the map view was
    initially created will continue to be used.

    </div>

    Parameters:  
    `configurationFile` -

    Map scheme configuration file. It must contain the whole scene
    configuration. In case it contains references to other files, they
    have to be reachable under the paths specified in the main
    configuration file.

    `watermarkStyle` -

    The style for the HERE watermark, see
    [`WatermarkStyle`](sdk-for-android-explore-com-here-sdk-mapview-watermarkstyle "enum class in com.here.sdk.mapview").

    `callback` -

    Optional callback that will receive the result of this operation.

    </div>

  - <div id="loadScene(com.here.sdk.mapview.MapSceneLoadOptions,com.here.sdk.mapview.MapScene.LoadSceneCallback)"
    class="section detail">

    ### loadScene

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadScene</span><span class="parameters">(@NonNull
    [MapSceneLoadOptions](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptions "class in com.here.sdk.mapview") options,
    @Nullable
    [MapScene.LoadSceneCallback](sdk-for-android-explore-com-here-sdk-mapview-mapscene-loadscenecallback "interface in com.here.sdk.mapview") callback)</span>

    </div>

    <div class="block">

    Asynchronously loads a map scene using MapSceneLoadOptions. This is
    an unified API that supports loading from either a map scheme or
    configuration file, with optional feature and watermark
    configuration. It's more efficient to load the scene with this
    function by specifying the list of enabled features and disabled
    features, compared to loading the scene first and enabling or
    disabling map features in the scene loading callback function.
    Configuration defaults are used for features that are not part of
    the enabled features or disabled features parameters. When a feature
    is in both the enabled and disabled lists, the feature is considered
    as requested to be enabled. If the same feature is present multiple
    times in the enabled list with different modes, then the feature is
    considered as requested to be enabled, but with an unspecified mode
    (any of the many specified in the enabled list). Any previous map
    scene config will be replaced. The callback is called on the main
    thread. When recreating an activity following a device rotation, it
    is not necessary to call this method a second time. The map scheme
    that was loaded when the map view was initially created will
    continue to be used. Note: This is a beta release of this feature,
    so there could be a few bugs and unexpected behaviors. Related APIs
    may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `options` -

    Scene configuration options created using
    MapSceneLoadOptionsBuilder.

    `callback` -

    Optional callback that will receive the result of this operation.

    </div>

  - <div id="addMapPolyline(com.here.sdk.mapview.MapPolyline)"
    class="section detail">

    ### addMapPolyline

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapPolyline</span><span class="parameters">(@NonNull
    [MapPolyline](sdk-for-android-explore-com-here-sdk-mapview-mappolyline "class in com.here.sdk.mapview") mapPolyline)</span>

    </div>

    <div class="block">

    Adds a map polyline to this map scene.

    </div>

    Parameters:  
    `mapPolyline` -

    The map polyline to be added to this map scene.

    </div>

  - <div id="addMapPolylines(java.util.List)" class="section detail">

    ### addMapPolylines

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapPolylines</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapPolyline](sdk-for-android-explore-com-here-sdk-mapview-mappolyline "class in com.here.sdk.mapview")> mapPolylines)</span>

    </div>

    <div class="block">

    Adds map polylines to this map scene. Note: Due to technical
    limitations using the MapPolyline API to add a very large number of
    polylines (especially 1000+ also depending on their complexity) is
    not recommended. Adding this many polylines has a negative impact on
    the performance leading to stuttering of the app and lower frame
    rates. To work around this limitation add only map items which are
    in the current camera viewport. A guide on how to achieve this can
    be found towards the end of the MapScene class doc.

    </div>

    Parameters:  
    `mapPolylines` -

    The map polylines to be added to this map scene.

    </div>

  - <div id="removeMapPolyline(com.here.sdk.mapview.MapPolyline)"
    class="section detail">

    ### removeMapPolyline

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapPolyline</span><span class="parameters">(@NonNull
    [MapPolyline](sdk-for-android-explore-com-here-sdk-mapview-mappolyline "class in com.here.sdk.mapview") mapPolyline)</span>

    </div>

    <div class="block">

    Removes a map polyline from this map scene.

    </div>

    Parameters:  
    `mapPolyline` -

    The map polyline to be removed from this map scene.

    </div>

  - <div id="removeMapPolylines(java.util.List)" class="section detail">

    ### removeMapPolylines

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapPolylines</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapPolyline](sdk-for-android-explore-com-here-sdk-mapview-mappolyline "class in com.here.sdk.mapview")> mapPolylines)</span>

    </div>

    <div class="block">

    Removes map polylines from this map scene.

    </div>

    Parameters:  
    `mapPolylines` -

    The map polylines to be removed from this map scene.

    </div>

  - <div id="removeAllMapPolylines()" class="section detail">

    ### removeAllMapPolylines

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllMapPolylines</span>()

    </div>

    <div class="block">

    Removes all map polylines from this map scene.

    </div>

    </div>

  - <div id="addMapArrow(com.here.sdk.mapview.MapArrow)"
    class="section detail">

    ### addMapArrow

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapArrow</span><span class="parameters">(@NonNull
    [MapArrow](sdk-for-android-explore-com-here-sdk-mapview-maparrow "class in com.here.sdk.mapview") mapArrow)</span>

    </div>

    <div class="block">

    Adds a map arrow to this map scene. Note: Due to technical
    limitations using the MapArrow API to add a very large number of
    arrows (especially 1000+ also depending on their complexity) is not
    recommended. Adding this many arrows has a negative impact on the
    performance leading to stuttering of the app and lower frame rates.
    To work around this limitation add only map items which are in the
    current camera viewport. A guide on how to achieve this can be found
    towards the end of the MapScene class doc.

    </div>

    Parameters:  
    `mapArrow` -

    The map arrow to be added to this map scene.

    </div>

  - <div id="removeMapArrow(com.here.sdk.mapview.MapArrow)"
    class="section detail">

    ### removeMapArrow

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapArrow</span><span class="parameters">(@NonNull
    [MapArrow](sdk-for-android-explore-com-here-sdk-mapview-maparrow "class in com.here.sdk.mapview") mapArrow)</span>

    </div>

    <div class="block">

    Removes a map arrow from this map scene.

    </div>

    Parameters:  
    `mapArrow` -

    The map arrow to be removed from this map scene.

    </div>

  - <div id="addMapMarker(com.here.sdk.mapview.MapMarker)"
    class="section detail">

    ### addMapMarker

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarker</span><span class="parameters">(@NonNull
    [MapMarker](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview") marker)</span>

    </div>

    <div class="block">

    Adds a map marker to this map scene. Adding the same marker instance
    multiple times has no effect. Adding a marker that is already part
    of a map marker cluster has no effect.

    </div>

    Parameters:  
    `marker` -

    The marker to be added to this map scene.

    </div>

  - <div id="addMapMarkers(java.util.List)" class="section detail">

    ### addMapMarkers

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarkers</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapMarker](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview")> markers)</span>

    </div>

    <div class="block">

    Adds multiple map markers to this map scene. Adding the same marker
    instances multiple times has no effect. Adding markers that are
    already part of a map marker cluster has no effect. Note: Due to
    technical limitations using the MapMarkers API to add a very large
    number of markers (several thousands, especially 10000+) is not
    recommended. Adding this many markers will have a negative impact on
    the performance leading to stuttering of the app and lower frame
    rates. To work around this limitation add only map items which are
    in the current camera viewport. A guide on how to achieve this can
    be found towards the end of the MapScene class doc.

    </div>

    Parameters:  
    `markers` -

    The list of markers to be added to this map scene.

    </div>

  - <div id="removeMapMarker(com.here.sdk.mapview.MapMarker)"
    class="section detail">

    ### removeMapMarker

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarker</span><span class="parameters">(@NonNull
    [MapMarker](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview") marker)</span>

    </div>

    <div class="block">

    Removes a map marker from this map scene. Removing a marker instance
    that is not a part of this scene or belongs to a marker cluster has
    no effect.

    </div>

    Parameters:  
    `marker` -

    The marker to be removed from this map scene.

    </div>

  - <div id="removeMapMarkers(java.util.List)" class="section detail">

    ### removeMapMarkers

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarkers</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapMarker](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview")> markers)</span>

    </div>

    <div class="block">

    Removes multiple map markers from this map scene. Removing marker
    instances that are not a part of this scene or belong to a marker
    cluster has no effect.

    </div>

    Parameters:  
    `markers` -

    The list of markers to be removed from this map scene.

    </div>

  - <div id="removeAllMapMarkers()" class="section detail">

    ### removeAllMapMarkers

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllMapMarkers</span>()

    </div>

    <div class="block">

    Removes all map markers from this map scene.

    </div>

    </div>

  - <div id="addMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)"
    class="section detail">

    ### addMapMarkerCluster

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarkerCluster</span><span class="parameters">(@NonNull
    [MapMarkerCluster](sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster "class in com.here.sdk.mapview") cluster)</span>

    </div>

    <div class="block">

    Adds a map marker cluster to the map. Either the contained
    individual map markers or the cluster markers will be displayed.
    Adding the same map marker cluster instance multiple times has no
    effect.

    </div>

    Parameters:  
    `cluster` -

    The marker cluster to be added to this map scene.

    </div>

  - <div id="removeMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)"
    class="section detail">

    ### removeMapMarkerCluster

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarkerCluster</span><span class="parameters">(@NonNull
    [MapMarkerCluster](sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster "class in com.here.sdk.mapview") cluster)</span>

    </div>

    <div class="block">

    Removes a map marker cluster from the map. Removing a map marker
    cluster that is not on this scene has no effect.

    </div>

    Parameters:  
    `cluster` -

    The marker cluster to be removed from this map scene.

    </div>

  - <div id="addMapMarker3d(com.here.sdk.mapview.MapMarker3D)"
    class="section detail">

    ### addMapMarker3d

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarker3d</span><span class="parameters">(@NonNull
    [MapMarker3D](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3d "class in com.here.sdk.mapview") marker)</span>

    </div>

    <div class="block">

    Adds a 3D map marker to this map scene. Does nothing if the marker
    instance was already added to the scene. Note: Due to technical
    limitations using the MapMarker3D API to add a very large number of
    3D markers (especially 500+ also depending on the complexity of the
    3D object) is not recommended. Adding this many 3D markers has a
    negative impact on the performance leading to stuttering of the app
    and lower frame rates. To work around this limitation add only map
    items which are in the current camera viewport. A guide on how to
    achieve this can be found towards the end of the MapScene class doc.

    </div>

    Parameters:  
    `marker` -

    The marker to be added to this map scene.

    </div>

  - <div id="addMapMarkers3d(java.util.List)" class="section detail">

    ### addMapMarkers3d

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarkers3d</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapMarker3D](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3d "class in com.here.sdk.mapview")> markers)</span>

    </div>

    <div class="block">

    Adds multiple 3D map markers to this map scene. Adding the same 3D
    marker instances multiple times has no effect. Note: Due to
    technical limitations, using the MapMarkers3D API to add a very
    large number of 3D markers (especially 500+) is not recommended.
    Adding this many markers will have a negative impact on the
    performance leading to stuttering of the app and lower frame rates.
    To work around this limitation add only map items which are in the
    current camera viewport. A guide on how to achieve this can be found
    towards the end of the MapScene class doc.

    </div>

    Parameters:  
    `markers` -

    The list of 3D markers to be added to this map scene.

    </div>

  - <div id="removeMapMarker3d(com.here.sdk.mapview.MapMarker3D)"
    class="section detail">

    ### removeMapMarker3d

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarker3d</span><span class="parameters">(@NonNull
    [MapMarker3D](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3d "class in com.here.sdk.mapview") marker)</span>

    </div>

    <div class="block">

    Removes a 3D map marker from this map scene. Removing a marker
    instance that is not on this scene has no effect.

    </div>

    Parameters:  
    `marker` -

    The marker to be removed from this map scene.

    </div>

  - <div id="removeMapMarkers3d(java.util.List)" class="section detail">

    ### removeMapMarkers3d

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarkers3d</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapMarker3D](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3d "class in com.here.sdk.mapview")> markers)</span>

    </div>

    <div class="block">

    Removes multiple 3D map markers from this map scene. Removing marker
    instances that are not a part of this scene has no effect.

    </div>

    Parameters:  
    `markers` -

    The list of 3D markers to be removed from this map scene.

    </div>

  - <div id="removeAllMapMarkers3d()" class="section detail">

    ### removeAllMapMarkers3d

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllMapMarkers3d</span>()

    </div>

    <div class="block">

    Removes all 3D map markers from this map scene.

    </div>

    </div>

  - <div id="addMapPolygon(com.here.sdk.mapview.MapPolygon)"
    class="section detail">

    ### addMapPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapPolygon</span><span class="parameters">(@NonNull
    [MapPolygon](sdk-for-android-explore-com-here-sdk-mapview-mappolygon "class in com.here.sdk.mapview") mapPolygon)</span>

    </div>

    <div class="block">

    Adds a map polygon to this map scene. Note: Due to technical
    limitations using the MapPolygon API to add a very large number of
    polygons (especially 1000+ also depending on their complexity) is
    not recommended. Adding this many polygons has a negative impact on
    the performance leading to stuttering of the app and lower frame
    rates. To work around this limitation add only map items which are
    in the current camera viewport. A guide on how to achieve this can
    be found towards the end of the MapScene class doc.

    </div>

    Parameters:  
    `mapPolygon` -

    The map polygon to be added to this map scene.

    </div>

  - <div id="addMapPolygons(java.util.List)" class="section detail">

    ### addMapPolygons

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapPolygons</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapPolygon](sdk-for-android-explore-com-here-sdk-mapview-mappolygon "class in com.here.sdk.mapview")> mapPolygons)</span>

    </div>

    <div class="block">

    Adds multiple map polygons to this map scene. Note: Due to technical
    limitations using the MapPolygon API to add a very large number of
    polygons (especially 1000+ also depending on their complexity) is
    not recommended. Adding this many polygons has a negative impact on
    the performance leading to stuttering of the app and lower frame
    rates. To work around this limitation add only map items which are
    in the current camera viewport. A guide on how to achieve this can
    be found towards the end of the MapScene class doc.

    </div>

    Parameters:  
    `mapPolygons` -

    The map polygons to be added to this map scene.

    </div>

  - <div id="removeMapPolygon(com.here.sdk.mapview.MapPolygon)"
    class="section detail">

    ### removeMapPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapPolygon</span><span class="parameters">(@NonNull
    [MapPolygon](sdk-for-android-explore-com-here-sdk-mapview-mappolygon "class in com.here.sdk.mapview") mapPolygon)</span>

    </div>

    <div class="block">

    Removes a map polygon from this map scene.

    </div>

    Parameters:  
    `mapPolygon` -

    The map polygon to be removed from this map scene.

    </div>

  - <div id="removeMapPolygons(java.util.List)" class="section detail">

    ### removeMapPolygons

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapPolygons</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapPolygon](sdk-for-android-explore-com-here-sdk-mapview-mappolygon "class in com.here.sdk.mapview")> mapPolygons)</span>

    </div>

    <div class="block">

    Removes multiple map polygon from this map scene.

    </div>

    Parameters:  
    `mapPolygons` -

    The map polygons to be removed from this map scene.

    </div>

  - <div id="removeAllMapPolygons()" class="section detail">

    ### removeAllMapPolygons

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllMapPolygons</span>()

    </div>

    <div class="block">

    Removes all map polygons from this map scene.

    </div>

    </div>

  - <div id="addMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)"
    class="section detail">

    ### addMapImageOverlay

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapImageOverlay</span><span class="parameters">(@NonNull
    [MapImageOverlay](sdk-for-android-explore-com-here-sdk-mapview-mapimageoverlay "class in com.here.sdk.mapview") overlay)</span>

    </div>

    <div class="block">

    Adds a map image overlay to this map scene. Adding the same overlay
    instance multiple times has no effect.

    </div>

    Parameters:  
    `overlay` -

    The overlay to be added to this map scene.

    </div>

  - <div id="removeMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)"
    class="section detail">

    ### removeMapImageOverlay

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapImageOverlay</span><span class="parameters">(@NonNull
    [MapImageOverlay](sdk-for-android-explore-com-here-sdk-mapview-mapimageoverlay "class in com.here.sdk.mapview") overlay)</span>

    </div>

    <div class="block">

    Removes a map image overlay from this map scene. Removing an overlay
    instance that is not part of this scene has no effect.

    </div>

    Parameters:  
    `overlay` -

    The overlay to be removed from this map scene.

    </div>

  - <div id="removeAllMapItems()" class="section detail">

    ### removeAllMapItems

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllMapItems</span>()

    </div>

    <div class="block">

    Removes all map objects from this map scene. This includes
    polylines, polygons, markers and clusters, arrows, image overlays.
    It is much faster than removing the objects one by one.

    </div>

    </div>

  - <div id="setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)"
    class="section detail">

    ### setLayerVisibility

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayerVisibility</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> layerName,
    @NonNull
    [VisibilityState](sdk-for-android-explore-com-here-sdk-mapview-visibilitystate "enum class in com.here.sdk.mapview") visibility)</span>

    </div>

    <div class="block">

    Immediately changes the visibility of a specified map layer.

    </div>

    Parameters:  
    `layerName` -

    The name of the map layer to be changed.

    `visibility` -

    The new visibility state of the layer.

    </div>

  - <div id="getActiveFeatures()" class="section detail">

    ### getActiveFeatures

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>></span> <span class="element-name">getActiveFeatures</span>()

    </div>

    <div class="block">

    Gets map features that are currently active. Active features are
    features that are either enabled via a call to
    enableFeatures(java.util.Map ) or that are enabled by default in the
    scene. The key to the resulting map is the name of the feature and
    the value is the active mode. Result is empty if scene has not been
    loaded.

    </div>

    Returns:  
    The map of active features.

    </div>

  - <div id="getSupportedFeatures()" class="section detail">

    ### getSupportedFeatures

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>>></span> <span class="element-name">getSupportedFeatures</span>()

    </div>

    <div class="block">

    Gets features and all of their modes supported by the currently
    loaded scene configuration. The key to the resulting map is the name
    of the feature and the value is a list of modes for that feature.
    Result is empty if scene has not been loaded.

    </div>

    Returns:  
    The map of supported features and all their modes.

    </div>

  - <div id="enableFeatures(java.util.Map)" class="section detail">

    ### enableFeatures

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">enableFeatures</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>> features)</span>

    </div>

    <div class="block">

    Enables specified map features. Those will become active after next
    map redraw, meaning that getActiveFeatures() will return updated
    list of active features only after the redraw happens. Does not
    affect features that were not specified. Unsupported features are
    ignored. May cause the current map configuration to be reloaded. See
    MapFeatures for feature names and MapFeatureModes for feature mode
    names.

    </div>

    Parameters:  
    `features` -

    The list of features to enable, key is the name of the feature (see
    [`MapFeatures`](sdk-for-android-explore-com-here-sdk-mapview-mapfeatures "class in com.here.sdk.mapview")),
    value specifies its mode (see
    [`MapFeatureModes`](sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes "class in com.here.sdk.mapview")).

    </div>

  - <div id="disableFeatures(java.util.List)" class="section detail">

    ### disableFeatures

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disableFeatures</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>> features)</span>

    </div>

    <div class="block">

    Disables specified map features. Those will become inactive after
    next map redraw, meaning that getActiveFeatures() will return
    updated list of active features only after the redraw happens. Does
    not affect features that were not specified. Unsupported features
    are ignored. May cause the current map configuration to be reloaded.
    See MapFeatures for feature names.

    </div>

    Parameters:  
    `features` -

    The names of features to disable (see
    [`MapFeatures`](sdk-for-android-explore-com-here-sdk-mapview-mapfeatures "class in com.here.sdk.mapview")).

    </div>

  - <div id="reloadScene()" class="section detail">

    ### reloadScene

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reloadScene</span>()

    </div>

    <div class="block">

    Asynchronously reloads the current map scene from file. This skips
    any cached data used internally and reloads the scene including any
    changes made to the (custom) map styles in JSON. MapFeature settings
    will be preserved. Internal optimization checks will be skipped to
    ensure all custom style changes are loaded. Therefore, calling this
    method may take slightly longer than calling one of the
    loadScene(..) overloads.

    </div>

    </div>

  - <div id="getLights()" class="section detail">

    ### getLights

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapSceneLights](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights "class in com.here.sdk.mapview")</span> <span class="element-name">getLights</span>()

    </div>

    <div class="block">

    Gets a MapSceneLights instance that controls lights present in the
    scene. Note: This is a beta release of this feature, so there could
    be a few bugs and unexpected behaviors. Related APIs may change for
    new releases without a deprecation process. Provides access to a
    MapSceneLights instance that controls the lights in the scene. The
    behavior of the returned MapSceneLights instance depends on the
    state of the scene: If the scene is not loaded, the returned
    MapSceneLights instance will not contain any light settings, as
    lights are not loaded without a scene. If the scene is loaded, the
    returned MapSceneLights instance reflects the current light settings
    of the loaded scene. Scene Change Behavior: If the scene changes,
    the MapSceneLights instance will be updated to reflect the light
    settings of the new scene. Any user-defined settings to
    MapSceneLights will be overridden by the new scene's light settings
    when the scene changes. Error Handling: If the scene is loaded and
    the loaded scene does not utilize or specify light settings: If the
    lights are not present, the error callback may return a NO_LIGHTS
    state.

    </div>

    Returns:  
    Controls lights present in the scene.

    </div>

  </div>

</div>


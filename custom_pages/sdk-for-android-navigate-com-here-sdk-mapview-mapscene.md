---
title: "MapScene (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapscene"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapScene.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapScene</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapScene</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents a map scene and exposes the functionality to manipulate its content.
 
The content of the displayed map and how it looks is specified by a
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscheme" title="enum class in com.here.sdk.mapview"><code>MapScheme</code></a> which is set when loading a scene with <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)"><code>loadScene(MapScheme, MapScene.LoadSceneCallback)</code></a>.
 It is also possible to load your own custom map scheme from a file bundled
 with your application. Supported file formats are:
 <ul>
<li>JSON (file extension '.json'; e.g. 'my_custom_style.json')</li>
<li>ZIP archive (file extension '.zip'; e.g. 'my_custom_style.zip'), with the following archive structure:
 <ul>
<li>root folder: any, not empty (e.g. 'my_custom_style')</li>
<li>JSON configuration: '<root folder="">/style.json'</root></li>
<li>custom assets folder: '<root folder="">/assets'</root></li>
</ul>
</li>
</ul>

Different map schemes offer different sets of features, for example showing traffic or 3D buildings.
 Some features have multiple modes of operation, but most have only one.
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#getSupportedFeatures()"><code>getSupportedFeatures()</code></a> can be used to check what features and modes are supported
 for the current scene. Features can be enabled using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#enableFeatures(java.util.Map)"><code>enableFeatures(java.util.Map<java.lang.string, java.lang.string="">)</java.lang.string,></code></a> and disabled
 with <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#disableFeatures(java.util.List)"><code>disableFeatures(java.util.List<java.lang.string>)</java.lang.string></code></a>. Checking which features are currently enabled can be done using
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#getActiveFeatures()"><code>getActiveFeatures()</code></a>. For convenience, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures" title="class in com.here.sdk.mapview"><code>MapFeatures</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes" title="class in com.here.sdk.mapview"><code>MapFeatureModes</code></a> hold
 constants for feature and mode names.
 Since version 4.15.0, map features cannot be controlled using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)"><code>setLayerVisibility(java.lang.String, com.here.sdk.mapview.VisibilityState)</code></a>, since <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)"><code>setLayerVisibility(java.lang.String, com.here.sdk.mapview.VisibilityState)</code></a> controls
 only visibility of the layers which are corresponding to the features enabled either by <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#enableFeatures(java.util.Map)"><code>enableFeatures(java.util.Map<java.lang.string, java.lang.string="">)</java.lang.string,></code></a>
 or enabled by default for the scene.
 
A map scheme is organized in layers, which can be controlled using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)"><code>setLayerVisibility(java.lang.String, com.here.sdk.mapview.VisibilityState)</code></a>.
 It's possible to change the visibility state of any map layer as long as the name is known.
 Layer visibility settings persist between scene reloading.
 
User generated content can be visualised on the map using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview"><code>MapPolyline</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolygon" title="class in com.here.sdk.mapview"><code>MapPolygon</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster" title="class in com.here.sdk.mapview"><code>MapMarkerCluster</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-maparrow" title="class in com.here.sdk.mapview"><code>MapArrow</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d" title="class in com.here.sdk.mapview"><code>MapMarker3D</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimageoverlay" title="class in com.here.sdk.mapview"><code>MapImageOverlay</code></a>
 (collectively referred to as "map items"). Those can be added to and removed
 from the scene by respective add and remove methods. The render order of the map items
 is according to the list above. The order of objects within the same type can be controlled using
 the <code>setDrawOrder()</code> method of each object.
 Be careful when adding a very large number of map items as this can have a negative impact on
 the performance of the app.
 To work around this limitation the following approach can be used:
 Register to map camera updates using <a href="sdk-for-android-navigate-mapcamera#addListener(com.here.sdk.mapview.MapCameraListener)"><code>MapCamera.addListener(com.here.sdk.mapview.MapCameraListener)</code></a>. Query the bounding box of the
 camera viewport using <a href="sdk-for-android-navigate-mapcamera#getBoundingBox()"><code>MapCamera.getBoundingBox()</code></a> (it may be extended) and then use the method
 <a href="sdk-for-android-navigate-geobox#contains(com.here.sdk.core.GeoCoordinates)"><code>GeoBox.contains(GeoCoordinates)</code></a> in combination with <a href="sdk-for-android-navigate-mapcamera-state#distanceToTargetInMeters"><code>MapCamera.State.distanceToTargetInMeters</code></a> to
 determine which map items are actually visible to the user in the current camera viewport and
 thus need to be added to the map.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static interface </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a></code></div>
<div className="col-last even-row-color">
<div className="block">Called on the main thread after <code>loadScene()</code> method finishes loading
 the scene.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter" title="class in com.here.sdk.mapview">MapScene.MapPickFilter</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Filter for the map content to be picked.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)">
<h3>loadScene</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">loadScene</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously loads a map scene described by a specified map scheme.
 Any previous map scene config will be replaced. The loaded scene is cached and so any changes
 made to the scene files on disk might not get reflected on a successive call to this function.
 Instead the reloadScene API can handle such use-cases to force-update the scene.
 Map features enabled or disabled using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#enableFeatures(java.util.Map)"><code>enableFeatures(java.util.Map<java.lang.string, java.lang.string="">)</java.lang.string,></code></a>
 and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#disableFeatures(java.util.List)"><code>disableFeatures(java.util.List<java.lang.string>)</java.lang.string></code></a> will be reset to defaults for the new
 scene configuration.
 The callback is called on the main thread.
 When recreating an activity following a device rotation, it is not necessary to call this
 method a second time. The map scheme that was loaded when the map view was initially
 created will continue to be used.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapScheme</code> - <p>Map scheme.</p></dd>
<dd><code>callback</code> - <p>Optional callback that will receive the result of this operation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="loadScene(java.lang.String,com.here.sdk.mapview.MapScene.LoadSceneCallback)">
<h3>loadScene</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">loadScene</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> configurationFile,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously loads a map scene described by a specified file in one of the supported formats.
 Any previous map scene config will be replaced.
 When loading the same file again, consider to call <code>reloadScene()</code> instead.
 Map features enabled or disabled using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#enableFeatures(java.util.Map)"><code>enableFeatures(java.util.Map<java.lang.string, java.lang.string="">)</java.lang.string,></code></a>
 and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#disableFeatures(java.util.List)"><code>disableFeatures(java.util.List<java.lang.string>)</java.lang.string></code></a> will be reset to defaults for the new
 scene configuration.
 The callback is called on the main thread.
 When recreating an activity following a device rotation, it is not necessary to call this
 method a second time. The map scheme that was loaded when the map view was initially
 created will continue to be used.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>configurationFile</code> - <p>Map scheme configuration file. It must contain the whole scene configuration.
     In case it contains references to other files, they have to be reachable under
     the paths specified in the main configuration file.</p></dd>
<dd><code>callback</code> - <p>Optional callback that will receive the result of this operation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="loadScene(java.lang.String,com.here.sdk.mapview.WatermarkStyle,com.here.sdk.mapview.MapScene.LoadSceneCallback)">
<h3>loadScene</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">loadScene</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> configurationFile,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-watermarkstyle" title="enum class in com.here.sdk.mapview">WatermarkStyle</a> watermarkStyle,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously loads a map scene described by a specified file in one of the supported formats.
 The style of the HERE watermark matching the map scheme is specified. Any previous map scene
 config will be replaced.
 When loading the same file again, consider to call <code>reloadScene()</code> instead.
 Map features enabled or disabled using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#enableFeatures(java.util.Map)"><code>enableFeatures(java.util.Map<java.lang.string, java.lang.string="">)</java.lang.string,></code></a>
 and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#disableFeatures(java.util.List)"><code>disableFeatures(java.util.List<java.lang.string>)</java.lang.string></code></a> will be reset to defaults for the new
 scene configuration.
 The callback is called on the main thread.
 When recreating an activity following a device rotation, it is not necessary to call this
 method a second time. The map scheme that was loaded when the map view was initially
 created will continue to be used.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>configurationFile</code> - <p>Map scheme configuration file. It must contain the whole scene configuration.
     In case it contains references to other files, they have to be reachable under
     the paths specified in the main configuration file.</p></dd>
<dd><code>watermarkStyle</code> - <p>The style for the HERE watermark, see <a href="sdk-for-android-navigate-com-here-sdk-mapview-watermarkstyle" title="enum class in com.here.sdk.mapview"><code>WatermarkStyle</code></a>.</p></dd>
<dd><code>callback</code> - <p>Optional callback that will receive the result of this operation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="loadScene(com.here.sdk.mapview.MapSceneLoadOptions,com.here.sdk.mapview.MapScene.LoadSceneCallback)">
<h3>loadScene</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">loadScene</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptions" title="class in com.here.sdk.mapview">MapSceneLoadOptions</a> options,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously loads a map scene using MapSceneLoadOptions.
 This is an unified API that supports loading from either a map scheme or configuration file,
 with optional feature and watermark configuration. It's more efficient to load the scene with
 this function by specifying the list of enabled features and disabled features, compared to
 loading the scene first and enabling or disabling map features in the scene loading callback
 function.
 Configuration defaults are used for features that are not part of the enabled features or
 disabled features parameters. When a feature is in both the enabled and disabled lists,
 the feature is considered as requested to be enabled. If the same feature is present multiple
 times in the enabled list with different modes, then the feature is considered as requested
 to be enabled, but with an unspecified mode (any of the many specified in the enabled list).
 Any previous map scene config will be replaced. The callback is called on the main thread.
 When recreating an activity following a device rotation, it is not necessary
 to call this
 method a second time. The map scheme that was loaded when the map view was
 initially
 created will continue to be used.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - <p>Scene configuration options created using MapSceneLoadOptionsBuilder.</p></dd>
<dd><code>callback</code> - <p>Optional callback that will receive the result of this operation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addMapPolyline(com.here.sdk.mapview.MapPolyline)">
<h3>addMapPolyline</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapPolyline</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a> mapPolyline)</span></div>
<div className="block"><p>Adds a map polyline to this map scene.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapPolyline</code> - <p>The map polyline to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addMapPolylines(java.util.List)">
<h3>addMapPolylines</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapPolylines</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a>&gt; mapPolylines)</span></div>
<div className="block"><p>Adds map polylines to this map scene.
 <strong>Note:</strong>
 Due to technical limitations using the MapPolyline API to add a very large number of
 polylines (especially 1000+ also depending on their complexity) is not recommended.
 Adding this many polylines has a negative impact on the performance leading to
 stuttering of the app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapPolylines</code> - <p>The map polylines to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapPolyline(com.here.sdk.mapview.MapPolyline)">
<h3>removeMapPolyline</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapPolyline</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a> mapPolyline)</span></div>
<div className="block"><p>Removes a map polyline from this map scene.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapPolyline</code> - <p>The map polyline to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapPolylines(java.util.List)">
<h3>removeMapPolylines</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapPolylines</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a>&gt; mapPolylines)</span></div>
<div className="block"><p>Removes map polylines from this map scene.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapPolylines</code> - <p>The map polylines to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeAllMapPolylines()">
<h3>removeAllMapPolylines</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeAllMapPolylines</span>()</div>
<div className="block"><p>Removes all map polylines from this map scene.</p></div>
</section>
</li>
<li>
<section className="detail" id="addMapArrow(com.here.sdk.mapview.MapArrow)">
<h3>addMapArrow</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapArrow</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-maparrow" title="class in com.here.sdk.mapview">MapArrow</a> mapArrow)</span></div>
<div className="block"><p>Adds a map arrow to this map scene.
 <strong>Note:</strong>
 Due to technical limitations using the MapArrow API to add a very large number of arrows
 (especially 1000+ also depending on their complexity) is not recommended.
 Adding this many arrows has a negative impact on the performance leading to stuttering of the
 app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapArrow</code> - <p>The map arrow to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapArrow(com.here.sdk.mapview.MapArrow)">
<h3>removeMapArrow</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapArrow</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-maparrow" title="class in com.here.sdk.mapview">MapArrow</a> mapArrow)</span></div>
<div className="block"><p>Removes a map arrow from this map scene.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapArrow</code> - <p>The map arrow to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addMapMarker(com.here.sdk.mapview.MapMarker)">
<h3>addMapMarker</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapMarker</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> marker)</span></div>
<div className="block"><p>Adds a map marker to this map scene. Adding the same marker instance multiple times
 has no effect. Adding a marker that is already part of a map marker cluster has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>marker</code> - <p>The marker to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addMapMarkers(java.util.List)">
<h3>addMapMarkers</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapMarkers</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers)</span></div>
<div className="block"><p>Adds multiple map markers to this map scene. Adding the same marker instances multiple times
 has no effect. Adding markers that are already part of a map marker cluster has no effect.
 <strong>Note:</strong>
 Due to technical limitations using the MapMarkers API to add a very large number of markers
 (several thousands, especially 10000+) is not recommended. Adding this many markers will have
 a negative impact on the performance leading to stuttering of the app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>markers</code> - <p>The list of markers to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapMarker(com.here.sdk.mapview.MapMarker)">
<h3>removeMapMarker</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapMarker</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> marker)</span></div>
<div className="block"><p>Removes a map marker from this map scene. Removing a marker instance that is not
 a part of this scene or belongs to a marker cluster has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>marker</code> - <p>The marker to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapMarkers(java.util.List)">
<h3>removeMapMarkers</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapMarkers</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers)</span></div>
<div className="block"><p>Removes multiple map markers from this map scene. Removing marker instances that are not
 a part of this scene or belong to a marker cluster has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>markers</code> - <p>The list of markers to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeAllMapMarkers()">
<h3>removeAllMapMarkers</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeAllMapMarkers</span>()</div>
<div className="block"><p>Removes all map markers from this map scene.</p></div>
</section>
</li>
<li>
<section className="detail" id="addMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)">
<h3>addMapMarkerCluster</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapMarkerCluster</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a> cluster)</span></div>
<div className="block"><p>Adds a map marker cluster to the map. Either the contained individual map markers or the
 cluster markers will be displayed. Adding the same map marker cluster instance multiple times
 has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>cluster</code> - <p>The marker cluster to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)">
<h3>removeMapMarkerCluster</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapMarkerCluster</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a> cluster)</span></div>
<div className="block"><p>Removes a map marker cluster from the map. Removing a map marker cluster that is not on this
 scene has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>cluster</code> - <p>The marker cluster to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addMapMarker3d(com.here.sdk.mapview.MapMarker3D)">
<h3>addMapMarker3d</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapMarker3d</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d" title="class in com.here.sdk.mapview">MapMarker3D</a> marker)</span></div>
<div className="block"><p>Adds a 3D map marker to this map scene.
 Does nothing if the marker instance was already added to the scene.
 <strong>Note:</strong>
 Due to technical limitations using the MapMarker3D API to add a very large number of 3D
 markers (especially 500+ also depending on the complexity of the 3D object) is not
 recommended. Adding this many 3D markers has a negative impact on the performance leading to
 stuttering of the app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>marker</code> - <p>The marker to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addMapMarkers3d(java.util.List)">
<h3>addMapMarkers3d</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapMarkers3d</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d" title="class in com.here.sdk.mapview">MapMarker3D</a>&gt; markers)</span></div>
<div className="block"><p>Adds multiple 3D map markers to this map scene. Adding the same 3D marker instances multiple
 times has no effect.
 <strong>Note:</strong>
 Due to technical limitations, using the MapMarkers3D API to add a very large number of 3D
 markers (especially 500+) is not recommended. Adding this many markers will have a
 negative impact on the performance leading to stuttering of the app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>markers</code> - <p>The list of 3D markers to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapMarker3d(com.here.sdk.mapview.MapMarker3D)">
<h3>removeMapMarker3d</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapMarker3d</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d" title="class in com.here.sdk.mapview">MapMarker3D</a> marker)</span></div>
<div className="block"><p>Removes a 3D map marker from this map scene. Removing a marker instance that is not on this
 scene has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>marker</code> - <p>The marker to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapMarkers3d(java.util.List)">
<h3>removeMapMarkers3d</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapMarkers3d</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d" title="class in com.here.sdk.mapview">MapMarker3D</a>&gt; markers)</span></div>
<div className="block"><p>Removes multiple 3D map markers from this map scene. Removing marker instances that are not
 a part of this scene has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>markers</code> - <p>The list of 3D markers to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeAllMapMarkers3d()">
<h3>removeAllMapMarkers3d</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeAllMapMarkers3d</span>()</div>
<div className="block"><p>Removes all 3D map markers from this map scene.</p></div>
</section>
</li>
<li>
<section className="detail" id="addMapPolygon(com.here.sdk.mapview.MapPolygon)">
<h3>addMapPolygon</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapPolygon</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolygon" title="class in com.here.sdk.mapview">MapPolygon</a> mapPolygon)</span></div>
<div className="block"><p>Adds a map polygon to this map scene.
 <strong>Note:</strong>
 Due to technical limitations using the MapPolygon API to add a very large number of polygons
 (especially 1000+ also depending on their complexity) is not recommended.
 Adding this many polygons has a negative impact on the performance leading to stuttering of
 the app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapPolygon</code> - <p>The map polygon to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addMapPolygons(java.util.List)">
<h3>addMapPolygons</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapPolygons</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolygon" title="class in com.here.sdk.mapview">MapPolygon</a>&gt; mapPolygons)</span></div>
<div className="block"><p>Adds multiple map polygons to this map scene.
 <strong>Note:</strong>
 Due to technical limitations using the MapPolygon API to add a very large number of polygons
 (especially 1000+ also depending on their complexity) is not recommended.
 Adding this many polygons has a negative impact on the performance leading to stuttering of
 the app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapPolygons</code> - <p>The map polygons to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapPolygon(com.here.sdk.mapview.MapPolygon)">
<h3>removeMapPolygon</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapPolygon</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolygon" title="class in com.here.sdk.mapview">MapPolygon</a> mapPolygon)</span></div>
<div className="block"><p>Removes a map polygon from this map scene.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapPolygon</code> - <p>The map polygon to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapPolygons(java.util.List)">
<h3>removeMapPolygons</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapPolygons</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolygon" title="class in com.here.sdk.mapview">MapPolygon</a>&gt; mapPolygons)</span></div>
<div className="block"><p>Removes multiple map polygon from this map scene.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapPolygons</code> - <p>The map polygons to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeAllMapPolygons()">
<h3>removeAllMapPolygons</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeAllMapPolygons</span>()</div>
<div className="block"><p>Removes all map polygons from this map scene.</p></div>
</section>
</li>
<li>
<section className="detail" id="addMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)">
<h3>addMapImageOverlay</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addMapImageOverlay</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimageoverlay" title="class in com.here.sdk.mapview">MapImageOverlay</a> overlay)</span></div>
<div className="block"><p>Adds a map image overlay to this map scene.
 Adding the same overlay instance multiple times has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>overlay</code> - <p>The overlay to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)">
<h3>removeMapImageOverlay</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeMapImageOverlay</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimageoverlay" title="class in com.here.sdk.mapview">MapImageOverlay</a> overlay)</span></div>
<div className="block"><p>Removes a map image overlay from this map scene.
 Removing an overlay instance that is not part of this scene has no effect.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>overlay</code> - <p>The overlay to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeAllMapItems()">
<h3>removeAllMapItems</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeAllMapItems</span>()</div>
<div className="block"><p>Removes all map objects from this map scene.
 This includes polylines, polygons, markers and clusters, arrows, image overlays.
 It is much faster than removing the objects one by one.</p></div>
</section>
</li>
<li>
<section className="detail" id="setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)">
<h3>setLayerVisibility</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setLayerVisibility</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> layerName,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-visibilitystate" title="enum class in com.here.sdk.mapview">VisibilityState</a> visibility)</span></div>
<div className="block"><p>Immediately changes the visibility of a specified map layer.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>layerName</code> - <p>The name of the map layer to be changed.</p></dd>
<dd><code>visibility</code> - <p>The new visibility state of the layer.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getActiveFeatures()">
<h3>getActiveFeatures</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span className="element-name">getActiveFeatures</span>()</div>
<div className="block"><p>Gets map features that are currently active. Active features are features that are either
 enabled via a call to <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#enableFeatures(java.util.Map)"><code>enableFeatures(java.util.Map<java.lang.string, java.lang.string="">)</java.lang.string,></code></a> or that are enabled by default in the scene.
 The key to the resulting map is the name of the feature
 and the value is the active mode.
 Result is empty if scene has not been loaded.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The map of active features.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSupportedFeatures()">
<h3>getSupportedFeatures</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;&gt;</span> <span className="element-name">getSupportedFeatures</span>()</div>
<div className="block"><p>Gets features and all of their modes supported by the currently
 loaded scene configuration.
 The key to the resulting map is the name of the feature
 and the value is a list of modes for that feature.
 Result is empty if scene has not been loaded.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The map of supported features and all their modes.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="enableFeatures(java.util.Map)">
<h3>enableFeatures</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">enableFeatures</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; features)</span></div>
<div className="block"><p>Enables specified map features. Those will become active
 after next map redraw, meaning that <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#getActiveFeatures()"><code>getActiveFeatures()</code></a> will
 return updated list of active features only after the redraw happens.
 Does not affect features that were not specified.
 Unsupported features are ignored.
 May cause the current map configuration to be reloaded.
 See <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures" title="class in com.here.sdk.mapview"><code>MapFeatures</code></a> for feature names and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes" title="class in com.here.sdk.mapview"><code>MapFeatureModes</code></a> for
 feature mode names.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>features</code> - <p>The list of features to enable, key is the name of the feature
     (see <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures" title="class in com.here.sdk.mapview"><code>MapFeatures</code></a>), value specifies its mode (see <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes" title="class in com.here.sdk.mapview"><code>MapFeatureModes</code></a>).</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="disableFeatures(java.util.List)">
<h3>disableFeatures</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">disableFeatures</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; features)</span></div>
<div className="block"><p>Disables specified map features. Those will become inactive
 after next map redraw, meaning that <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene#getActiveFeatures()"><code>getActiveFeatures()</code></a> will
 return updated list of active features only after the redraw happens.
 Does not affect features that were not specified.
 Unsupported features are ignored.
 May cause the current map configuration to be reloaded.
 See <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures" title="class in com.here.sdk.mapview"><code>MapFeatures</code></a> for feature names.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>features</code> - <p>The names of features to disable (see <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures" title="class in com.here.sdk.mapview"><code>MapFeatures</code></a>).</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="reloadScene()">
<h3>reloadScene</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">reloadScene</span>()</div>
<div className="block"><p>Asynchronously reloads the current map scene from file. This skips any cached data used internally and reloads the
 scene including any changes made to the (custom) map styles in JSON.
 <code>MapFeature</code> settings will be preserved.
 Internal optimization checks will be skipped to ensure all custom style changes are loaded. Therefore,
 calling this method may take slightly longer than calling one of the <code>loadScene(..)</code> overloads.</p></div>
</section>
</li>
<li>
<section className="detail" id="getLights()">
<h3>getLights</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights" title="class in com.here.sdk.mapview">MapSceneLights</a></span> <span className="element-name">getLights</span>()</div>
<div className="block"><p>Gets a MapSceneLights instance that controls lights present in the scene.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.
 Provides access to a MapSceneLights instance that controls the lights in the scene.
 The behavior of the returned MapSceneLights instance depends on the state of the scene:
 <ul>
<li>If the scene is not loaded, the returned MapSceneLights instance will not contain any light settings, as lights are not loaded without a scene.</li>
<li>If the scene is loaded, the returned MapSceneLights instance reflects the current light settings of the loaded scene.</li>
</ul>
Scene Change Behavior:
 <ul>
<li>If the scene changes, the MapSceneLights instance will be updated to reflect the light settings of the new scene.</li>
<li>Any user-defined settings to MapSceneLights will be overridden by the new scene's light settings when the scene changes.</li>
</ul>
Error Handling:
 <ul>
<li>If the scene is loaded and the loaded scene does not utilize or specify light settings:
 <ul>
<li>If the lights are not present, the error callback may return a NO_LIGHTS state.</li>
</ul>
</li>
</ul></p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Controls lights present in the scene.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>

---
title: "MapScene (API Reference)"
slug: "sdk-for-android-navigate-mapscene"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapScene.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li><a href="#nested-class-summary">Nested</a> | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapScene</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapScene</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Represents a map scene and exposes the functionality to manipulate its content.
 
</p><p>The content of the displayed map and how it looks is specified by a
 <a href="sdk-for-android-navigate-mapscheme" title="enum class in com.here.sdk.mapview"><code>MapScheme</code></a> which is set when loading a scene with <a href="#loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)"><code>loadScene(MapScheme, MapScene.LoadSceneCallback)</code></a>.
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

</p><p>Different map schemes offer different sets of features, for example showing traffic or 3D buildings.
 Some features have multiple modes of operation, but most have only one.
 <a href="#getSupportedFeatures()"><code>getSupportedFeatures()</code></a> can be used to check what features and modes are supported
 for the current scene. Features can be enabled using <a href="#enableFeatures(java.util.Map)"><code>enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a> and disabled
 with <a href="#disableFeatures(java.util.List)"><code>disableFeatures(java.util.List&lt;java.lang.String&gt;)</code></a>. Checking which features are currently enabled can be done using
 <a href="#getActiveFeatures()"><code>getActiveFeatures()</code></a>. For convenience, <a href="sdk-for-android-navigate-mapfeatures" title="class in com.here.sdk.mapview"><code>MapFeatures</code></a> and <a href="sdk-for-android-navigate-mapfeaturemodes" title="class in com.here.sdk.mapview"><code>MapFeatureModes</code></a> hold
 constants for feature and mode names.
 </p><p>Since version 4.15.0, map features cannot be controlled using <a href="#setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)"><code>setLayerVisibility(java.lang.String, com.here.sdk.mapview.VisibilityState)</code></a>, since <a href="#setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)"><code>setLayerVisibility(java.lang.String, com.here.sdk.mapview.VisibilityState)</code></a> controls
 only visibility of the layers which are corresponding to the features enabled either by <a href="#enableFeatures(java.util.Map)"><code>enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a>
 or enabled by default for the scene.
 
</p><p>A map scheme is organized in layers, which can be controlled using <a href="#setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)"><code>setLayerVisibility(java.lang.String, com.here.sdk.mapview.VisibilityState)</code></a>.
 It's possible to change the visibility state of any map layer as long as the name is known.
 </p><p>Layer visibility settings persist between scene reloading.
 
</p><p>User generated content can be visualised on the map using <a href="sdk-for-android-navigate-mappolyline" title="class in com.here.sdk.mapview"><code>MapPolyline</code></a>, <a href="sdk-for-android-navigate-mappolygon" title="class in com.here.sdk.mapview"><code>MapPolygon</code></a>, <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>,
 <a href="sdk-for-android-navigate-mapmarkercluster" title="class in com.here.sdk.mapview"><code>MapMarkerCluster</code></a>, <a href="sdk-for-android-navigate-maparrow" title="class in com.here.sdk.mapview"><code>MapArrow</code></a>, <a href="sdk-for-android-navigate-mapmarker3d" title="class in com.here.sdk.mapview"><code>MapMarker3D</code></a> and <a href="sdk-for-android-navigate-mapimageoverlay" title="class in com.here.sdk.mapview"><code>MapImageOverlay</code></a>
 (collectively referred to as "map items"). Those can be added to and removed
 from the scene by respective add and remove methods. The render order of the map items
 is according to the list above. The order of objects within the same type can be controlled using
 the <code>setDrawOrder()</code> method of each object.
 </p><p>Be careful when adding a very large number of map items as this can have a negative impact on
 the performance of the app.
 To work around this limitation the following approach can be used:
 Register to map camera updates using <a href="sdk-for-android-navigate-mapcamera#addListener(com.here.sdk.mapview.MapCameraListener)"><code>MapCamera.addListener(com.here.sdk.mapview.MapCameraListener)</code></a>. Query the bounding box of the
 camera viewport using <a href="sdk-for-android-navigate-mapcamera#getBoundingBox()"><code>MapCamera.getBoundingBox()</code></a> (it may be extended) and then use the method
 <a href="sdk-for-android-navigate-core-geobox#contains(com.here.sdk.core.GeoCoordinates)"><code>GeoBox.contains(GeoCoordinates)</code></a> in combination with <a href="sdk-for-android-navigate-mapcamera.state#distanceToTargetInMeters"><code>MapCamera.State.distanceToTargetInMeters</code></a> to
 determine which map items are actually visible to the user in the current camera viewport and
 thus need to be added to the map.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-mapscene.loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a></code></div>
<div class="col-last even-row-color">
<div class="block">Called on the main thread after <code>loadScene()</code> method finishes loading
 the scene.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-mapscene.mappickfilter" title="class in com.here.sdk.mapview">MapScene.MapPickFilter</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Filter for the map content to be picked.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMapArrow(com.here.sdk.mapview.MapArrow)">addMapArrow</a><wbr/>(<a href="sdk-for-android-navigate-maparrow" title="class in com.here.sdk.mapview">MapArrow</a> mapArrow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a map arrow to this map scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)">addMapImageOverlay</a><wbr/>(<a href="sdk-for-android-navigate-mapimageoverlay" title="class in com.here.sdk.mapview">MapImageOverlay</a> overlay)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a map image overlay to this map scene.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMapMarker(com.here.sdk.mapview.MapMarker)">addMapMarker</a><wbr/>(<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> marker)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a map marker to this map scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMapMarker3d(com.here.sdk.mapview.MapMarker3D)">addMapMarker3d</a><wbr/>(<a href="sdk-for-android-navigate-mapmarker3d" title="class in com.here.sdk.mapview">MapMarker3D</a> marker)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a 3D map marker to this map scene.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)">addMapMarkerCluster</a><wbr/>(<a href="sdk-for-android-navigate-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a> cluster)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a map marker cluster to the map.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMapMarkers(java.util.List)">addMapMarkers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds multiple map markers to this map scene.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMapMarkers3d(java.util.List)">addMapMarkers3d</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker3d" title="class in com.here.sdk.mapview">MapMarker3D</a>&gt; markers)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds multiple 3D map markers to this map scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMapPolygon(com.here.sdk.mapview.MapPolygon)">addMapPolygon</a><wbr/>(<a href="sdk-for-android-navigate-mappolygon" title="class in com.here.sdk.mapview">MapPolygon</a> mapPolygon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a map polygon to this map scene.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMapPolygons(java.util.List)">addMapPolygons</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mappolygon" title="class in com.here.sdk.mapview">MapPolygon</a>&gt; mapPolygons)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds multiple map polygons to this map scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMapPolyline(com.here.sdk.mapview.MapPolyline)">addMapPolyline</a><wbr/>(<a href="sdk-for-android-navigate-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a> mapPolyline)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a map polyline to this map scene.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addMapPolylines(java.util.List)">addMapPolylines</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a>&gt; mapPolylines)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds map polylines to this map scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#disableFeatures(java.util.List)">disableFeatures</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; features)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Disables specified map features.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#enableFeatures(java.util.Map)">enableFeatures</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; features)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Enables specified map features.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveFeatures()">getActiveFeatures</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets map features that are currently active.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapscenelights" title="class in com.here.sdk.mapview">MapSceneLights</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLights()">getLights</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a MapSceneLights instance that controls lights present in the scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupportedFeatures()">getSupportedFeatures</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets features and all of their modes supported by the currently
 loaded scene configuration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadScene(com.here.sdk.mapview.MapSceneLoadOptions,com.here.sdk.mapview.MapScene.LoadSceneCallback)">loadScene</a><wbr/>(<a href="sdk-for-android-navigate-mapsceneloadoptions" title="class in com.here.sdk.mapview">MapSceneLoadOptions</a> options,
 <a href="sdk-for-android-navigate-mapscene.loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously loads a map scene using MapSceneLoadOptions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)">loadScene</a><wbr/>(<a href="sdk-for-android-navigate-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme,
 <a href="sdk-for-android-navigate-mapscene.loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously loads a map scene described by a specified map scheme.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadScene(java.lang.String,com.here.sdk.mapview.MapScene.LoadSceneCallback)">loadScene</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> configurationFile,
 <a href="sdk-for-android-navigate-mapscene.loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously loads a map scene described by a specified file in one of the supported formats.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadScene(java.lang.String,com.here.sdk.mapview.WatermarkStyle,com.here.sdk.mapview.MapScene.LoadSceneCallback)">loadScene</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> configurationFile,
 <a href="sdk-for-android-navigate-watermarkstyle" title="enum class in com.here.sdk.mapview">WatermarkStyle</a> watermarkStyle,
 <a href="sdk-for-android-navigate-mapscene.loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously loads a map scene described by a specified file in one of the supported formats.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reloadScene()">reloadScene</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously reloads the current map scene from file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAllMapItems()">removeAllMapItems</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all map objects from this map scene.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAllMapMarkers()">removeAllMapMarkers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all map markers from this map scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAllMapMarkers3d()">removeAllMapMarkers3d</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all 3D map markers from this map scene.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAllMapPolygons()">removeAllMapPolygons</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all map polygons from this map scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAllMapPolylines()">removeAllMapPolylines</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all map polylines from this map scene.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMapArrow(com.here.sdk.mapview.MapArrow)">removeMapArrow</a><wbr/>(<a href="sdk-for-android-navigate-maparrow" title="class in com.here.sdk.mapview">MapArrow</a> mapArrow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a map arrow from this map scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)">removeMapImageOverlay</a><wbr/>(<a href="sdk-for-android-navigate-mapimageoverlay" title="class in com.here.sdk.mapview">MapImageOverlay</a> overlay)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a map image overlay from this map scene.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMapMarker(com.here.sdk.mapview.MapMarker)">removeMapMarker</a><wbr/>(<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> marker)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a map marker from this map scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMapMarker3d(com.here.sdk.mapview.MapMarker3D)">removeMapMarker3d</a><wbr/>(<a href="sdk-for-android-navigate-mapmarker3d" title="class in com.here.sdk.mapview">MapMarker3D</a> marker)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a 3D map marker from this map scene.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)">removeMapMarkerCluster</a><wbr/>(<a href="sdk-for-android-navigate-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a> cluster)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a map marker cluster from the map.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMapMarkers(java.util.List)">removeMapMarkers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes multiple map markers from this map scene.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMapMarkers3d(java.util.List)">removeMapMarkers3d</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker3d" title="class in com.here.sdk.mapview">MapMarker3D</a>&gt; markers)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes multiple 3D map markers from this map scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMapPolygon(com.here.sdk.mapview.MapPolygon)">removeMapPolygon</a><wbr/>(<a href="sdk-for-android-navigate-mappolygon" title="class in com.here.sdk.mapview">MapPolygon</a> mapPolygon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a map polygon from this map scene.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMapPolygons(java.util.List)">removeMapPolygons</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mappolygon" title="class in com.here.sdk.mapview">MapPolygon</a>&gt; mapPolygons)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes multiple map polygon from this map scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMapPolyline(com.here.sdk.mapview.MapPolyline)">removeMapPolyline</a><wbr/>(<a href="sdk-for-android-navigate-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a> mapPolyline)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a map polyline from this map scene.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeMapPolylines(java.util.List)">removeMapPolylines</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a>&gt; mapPolylines)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes map polylines from this map scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)">setLayerVisibility</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> layerName,
 <a href="sdk-for-android-navigate-visibilitystate" title="enum class in com.here.sdk.mapview">VisibilityState</a> visibility)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Immediately changes the visibility of a specified map layer.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)">
<h3>loadScene</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadScene</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme,
 @Nullable
 <a href="sdk-for-android-navigate-mapscene.loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously loads a map scene described by a specified map scheme.
 Any previous map scene config will be replaced. The loaded scene is cached and so any changes
 made to the scene files on disk might not get reflected on a successive call to this function.
 Instead the reloadScene API can handle such use-cases to force-update the scene.
 </p><p>Map features enabled or disabled using <a href="#enableFeatures(java.util.Map)"><code>enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a>
 and <a href="#disableFeatures(java.util.List)"><code>disableFeatures(java.util.List&lt;java.lang.String&gt;)</code></a> will be reset to defaults for the new
 scene configuration.
 </p><p>The callback is called on the main thread.
 When recreating an activity following a device rotation, it is not necessary to call this
 method a second time. The map scheme that was loaded when the map view was initially
 created will continue to be used.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapScheme</code> - <p>Map scheme.</p></dd>
<dd><code>callback</code> - <p>Optional callback that will receive the result of this operation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadScene(java.lang.String,com.here.sdk.mapview.MapScene.LoadSceneCallback)">
<h3>loadScene</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadScene</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> configurationFile,
 @Nullable
 <a href="sdk-for-android-navigate-mapscene.loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously loads a map scene described by a specified file in one of the supported formats.
 Any previous map scene config will be replaced.
 </p><p>When loading the same file again, consider to call <code>reloadScene()</code> instead.
 </p><p>Map features enabled or disabled using <a href="#enableFeatures(java.util.Map)"><code>enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a>
 and <a href="#disableFeatures(java.util.List)"><code>disableFeatures(java.util.List&lt;java.lang.String&gt;)</code></a> will be reset to defaults for the new
 scene configuration.
 </p><p>The callback is called on the main thread.
 When recreating an activity following a device rotation, it is not necessary to call this
 method a second time. The map scheme that was loaded when the map view was initially
 created will continue to be used.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurationFile</code> - <p>Map scheme configuration file. It must contain the whole scene configuration.
     In case it contains references to other files, they have to be reachable under
     the paths specified in the main configuration file.</p></dd>
<dd><code>callback</code> - <p>Optional callback that will receive the result of this operation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadScene(java.lang.String,com.here.sdk.mapview.WatermarkStyle,com.here.sdk.mapview.MapScene.LoadSceneCallback)">
<h3>loadScene</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadScene</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> configurationFile,
 @NonNull
 <a href="sdk-for-android-navigate-watermarkstyle" title="enum class in com.here.sdk.mapview">WatermarkStyle</a> watermarkStyle,
 @Nullable
 <a href="sdk-for-android-navigate-mapscene.loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously loads a map scene described by a specified file in one of the supported formats.
 The style of the HERE watermark matching the map scheme is specified. Any previous map scene
 config will be replaced.
 </p><p>When loading the same file again, consider to call <code>reloadScene()</code> instead.
 </p><p>Map features enabled or disabled using <a href="#enableFeatures(java.util.Map)"><code>enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a>
 and <a href="#disableFeatures(java.util.List)"><code>disableFeatures(java.util.List&lt;java.lang.String&gt;)</code></a> will be reset to defaults for the new
 scene configuration.
 </p><p>The callback is called on the main thread.
 When recreating an activity following a device rotation, it is not necessary to call this
 method a second time. The map scheme that was loaded when the map view was initially
 created will continue to be used.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurationFile</code> - <p>Map scheme configuration file. It must contain the whole scene configuration.
     In case it contains references to other files, they have to be reachable under
     the paths specified in the main configuration file.</p></dd>
<dd><code>watermarkStyle</code> - <p>The style for the HERE watermark, see <a href="sdk-for-android-navigate-watermarkstyle" title="enum class in com.here.sdk.mapview"><code>WatermarkStyle</code></a>.</p></dd>
<dd><code>callback</code> - <p>Optional callback that will receive the result of this operation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadScene(com.here.sdk.mapview.MapSceneLoadOptions,com.here.sdk.mapview.MapScene.LoadSceneCallback)">
<h3>loadScene</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadScene</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapsceneloadoptions" title="class in com.here.sdk.mapview">MapSceneLoadOptions</a> options,
 @Nullable
 <a href="sdk-for-android-navigate-mapscene.loadscenecallback" title="interface in com.here.sdk.mapview">MapScene.LoadSceneCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously loads a map scene using MapSceneLoadOptions.
 </p><p>This is an unified API that supports loading from either a map scheme or configuration file,
 with optional feature and watermark configuration. It's more efficient to load the scene with
 this function by specifying the list of enabled features and disabled features, compared to
 loading the scene first and enabling or disabling map features in the scene loading callback
 function.
 </p><p>Configuration defaults are used for features that are not part of the enabled features or
 disabled features parameters. When a feature is in both the enabled and disabled lists,
 the feature is considered as requested to be enabled. If the same feature is present multiple
 times in the enabled list with different modes, then the feature is considered as requested
 to be enabled, but with an unspecified mode (any of the many specified in the enabled list).
 </p><p>Any previous map scene config will be replaced. The callback is called on the main thread.
 </p><p>When recreating an activity following a device rotation, it is not necessary
 to call this
 method a second time. The map scheme that was loaded when the map view was
 initially
 created will continue to be used.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - <p>Scene configuration options created using MapSceneLoadOptionsBuilder.</p></dd>
<dd><code>callback</code> - <p>Optional callback that will receive the result of this operation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addMapPolyline(com.here.sdk.mapview.MapPolyline)">
<h3>addMapPolyline</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapPolyline</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a> mapPolyline)</span></div>
<div class="block"><p>Adds a map polyline to this map scene.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapPolyline</code> - <p>The map polyline to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addMapPolylines(java.util.List)">
<h3>addMapPolylines</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapPolylines</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a>&gt; mapPolylines)</span></div>
<div class="block"><p>Adds map polylines to this map scene.
 </p><p><strong>Note:</strong>
 Due to technical limitations using the MapPolyline API to add a very large number of
 polylines (especially 1000+ also depending on their complexity) is not recommended.
 Adding this many polylines has a negative impact on the performance leading to
 stuttering of the app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapPolylines</code> - <p>The map polylines to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMapPolyline(com.here.sdk.mapview.MapPolyline)">
<h3>removeMapPolyline</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapPolyline</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a> mapPolyline)</span></div>
<div class="block"><p>Removes a map polyline from this map scene.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapPolyline</code> - <p>The map polyline to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMapPolylines(java.util.List)">
<h3>removeMapPolylines</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapPolylines</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a>&gt; mapPolylines)</span></div>
<div class="block"><p>Removes map polylines from this map scene.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapPolylines</code> - <p>The map polylines to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAllMapPolylines()">
<h3>removeAllMapPolylines</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllMapPolylines</span>()</div>
<div class="block"><p>Removes all map polylines from this map scene.</p></div>
</section>
</li>
<li>
<section class="detail" id="addMapArrow(com.here.sdk.mapview.MapArrow)">
<h3>addMapArrow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapArrow</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-maparrow" title="class in com.here.sdk.mapview">MapArrow</a> mapArrow)</span></div>
<div class="block"><p>Adds a map arrow to this map scene.
 </p><p><strong>Note:</strong>
 Due to technical limitations using the MapArrow API to add a very large number of arrows
 (especially 1000+ also depending on their complexity) is not recommended.
 Adding this many arrows has a negative impact on the performance leading to stuttering of the
 app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapArrow</code> - <p>The map arrow to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMapArrow(com.here.sdk.mapview.MapArrow)">
<h3>removeMapArrow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapArrow</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-maparrow" title="class in com.here.sdk.mapview">MapArrow</a> mapArrow)</span></div>
<div class="block"><p>Removes a map arrow from this map scene.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapArrow</code> - <p>The map arrow to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addMapMarker(com.here.sdk.mapview.MapMarker)">
<h3>addMapMarker</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarker</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> marker)</span></div>
<div class="block"><p>Adds a map marker to this map scene. Adding the same marker instance multiple times
 has no effect. Adding a marker that is already part of a map marker cluster has no effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>marker</code> - <p>The marker to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addMapMarkers(java.util.List)">
<h3>addMapMarkers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarkers</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers)</span></div>
<div class="block"><p>Adds multiple map markers to this map scene. Adding the same marker instances multiple times
 has no effect. Adding markers that are already part of a map marker cluster has no effect.
 </p><p><strong>Note:</strong>
 Due to technical limitations using the MapMarkers API to add a very large number of markers
 (several thousands, especially 10000+) is not recommended. Adding this many markers will have
 a negative impact on the performance leading to stuttering of the app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>markers</code> - <p>The list of markers to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMapMarker(com.here.sdk.mapview.MapMarker)">
<h3>removeMapMarker</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarker</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> marker)</span></div>
<div class="block"><p>Removes a map marker from this map scene. Removing a marker instance that is not
 a part of this scene or belongs to a marker cluster has no effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>marker</code> - <p>The marker to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMapMarkers(java.util.List)">
<h3>removeMapMarkers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarkers</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers)</span></div>
<div class="block"><p>Removes multiple map markers from this map scene. Removing marker instances that are not
 a part of this scene or belong to a marker cluster has no effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>markers</code> - <p>The list of markers to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAllMapMarkers()">
<h3>removeAllMapMarkers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllMapMarkers</span>()</div>
<div class="block"><p>Removes all map markers from this map scene.</p></div>
</section>
</li>
<li>
<section class="detail" id="addMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)">
<h3>addMapMarkerCluster</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarkerCluster</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a> cluster)</span></div>
<div class="block"><p>Adds a map marker cluster to the map. Either the contained individual map markers or the
 cluster markers will be displayed. Adding the same map marker cluster instance multiple times
 has no effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cluster</code> - <p>The marker cluster to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)">
<h3>removeMapMarkerCluster</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarkerCluster</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a> cluster)</span></div>
<div class="block"><p>Removes a map marker cluster from the map. Removing a map marker cluster that is not on this
 scene has no effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cluster</code> - <p>The marker cluster to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addMapMarker3d(com.here.sdk.mapview.MapMarker3D)">
<h3>addMapMarker3d</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarker3d</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapmarker3d" title="class in com.here.sdk.mapview">MapMarker3D</a> marker)</span></div>
<div class="block"><p>Adds a 3D map marker to this map scene.
 Does nothing if the marker instance was already added to the scene.
 </p><p><strong>Note:</strong>
 Due to technical limitations using the MapMarker3D API to add a very large number of 3D
 markers (especially 500+ also depending on the complexity of the 3D object) is not
 recommended. Adding this many 3D markers has a negative impact on the performance leading to
 stuttering of the app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>marker</code> - <p>The marker to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addMapMarkers3d(java.util.List)">
<h3>addMapMarkers3d</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapMarkers3d</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker3d" title="class in com.here.sdk.mapview">MapMarker3D</a>&gt; markers)</span></div>
<div class="block"><p>Adds multiple 3D map markers to this map scene. Adding the same 3D marker instances multiple
 times has no effect.
 </p><p><strong>Note:</strong>
 Due to technical limitations, using the MapMarkers3D API to add a very large number of 3D
 markers (especially 500+) is not recommended. Adding this many markers will have a
 negative impact on the performance leading to stuttering of the app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>markers</code> - <p>The list of 3D markers to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMapMarker3d(com.here.sdk.mapview.MapMarker3D)">
<h3>removeMapMarker3d</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarker3d</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapmarker3d" title="class in com.here.sdk.mapview">MapMarker3D</a> marker)</span></div>
<div class="block"><p>Removes a 3D map marker from this map scene. Removing a marker instance that is not on this
 scene has no effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>marker</code> - <p>The marker to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMapMarkers3d(java.util.List)">
<h3>removeMapMarkers3d</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapMarkers3d</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker3d" title="class in com.here.sdk.mapview">MapMarker3D</a>&gt; markers)</span></div>
<div class="block"><p>Removes multiple 3D map markers from this map scene. Removing marker instances that are not
 a part of this scene has no effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>markers</code> - <p>The list of 3D markers to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAllMapMarkers3d()">
<h3>removeAllMapMarkers3d</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllMapMarkers3d</span>()</div>
<div class="block"><p>Removes all 3D map markers from this map scene.</p></div>
</section>
</li>
<li>
<section class="detail" id="addMapPolygon(com.here.sdk.mapview.MapPolygon)">
<h3>addMapPolygon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapPolygon</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mappolygon" title="class in com.here.sdk.mapview">MapPolygon</a> mapPolygon)</span></div>
<div class="block"><p>Adds a map polygon to this map scene.
 </p><p><strong>Note:</strong>
 Due to technical limitations using the MapPolygon API to add a very large number of polygons
 (especially 1000+ also depending on their complexity) is not recommended.
 Adding this many polygons has a negative impact on the performance leading to stuttering of
 the app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapPolygon</code> - <p>The map polygon to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addMapPolygons(java.util.List)">
<h3>addMapPolygons</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapPolygons</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mappolygon" title="class in com.here.sdk.mapview">MapPolygon</a>&gt; mapPolygons)</span></div>
<div class="block"><p>Adds multiple map polygons to this map scene.
 </p><p><strong>Note:</strong>
 Due to technical limitations using the MapPolygon API to add a very large number of polygons
 (especially 1000+ also depending on their complexity) is not recommended.
 Adding this many polygons has a negative impact on the performance leading to stuttering of
 the app and lower frame rates.
 To work around this limitation add only map items which are in the current camera viewport.
 A guide on how to achieve this can be found towards the end of the <a href="sdk-for-android-navigate-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> class doc.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapPolygons</code> - <p>The map polygons to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMapPolygon(com.here.sdk.mapview.MapPolygon)">
<h3>removeMapPolygon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapPolygon</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mappolygon" title="class in com.here.sdk.mapview">MapPolygon</a> mapPolygon)</span></div>
<div class="block"><p>Removes a map polygon from this map scene.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapPolygon</code> - <p>The map polygon to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMapPolygons(java.util.List)">
<h3>removeMapPolygons</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapPolygons</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mappolygon" title="class in com.here.sdk.mapview">MapPolygon</a>&gt; mapPolygons)</span></div>
<div class="block"><p>Removes multiple map polygon from this map scene.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapPolygons</code> - <p>The map polygons to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAllMapPolygons()">
<h3>removeAllMapPolygons</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllMapPolygons</span>()</div>
<div class="block"><p>Removes all map polygons from this map scene.</p></div>
</section>
</li>
<li>
<section class="detail" id="addMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)">
<h3>addMapImageOverlay</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMapImageOverlay</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapimageoverlay" title="class in com.here.sdk.mapview">MapImageOverlay</a> overlay)</span></div>
<div class="block"><p>Adds a map image overlay to this map scene.
 Adding the same overlay instance multiple times has no effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>overlay</code> - <p>The overlay to be added to this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)">
<h3>removeMapImageOverlay</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMapImageOverlay</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapimageoverlay" title="class in com.here.sdk.mapview">MapImageOverlay</a> overlay)</span></div>
<div class="block"><p>Removes a map image overlay from this map scene.
 Removing an overlay instance that is not part of this scene has no effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>overlay</code> - <p>The overlay to be removed from this map scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAllMapItems()">
<h3>removeAllMapItems</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllMapItems</span>()</div>
<div class="block"><p>Removes all map objects from this map scene.
 This includes polylines, polygons, markers and clusters, arrows, image overlays.
 It is much faster than removing the objects one by one.</p></div>
</section>
</li>
<li>
<section class="detail" id="setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)">
<h3>setLayerVisibility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayerVisibility</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> layerName,
 @NonNull
 <a href="sdk-for-android-navigate-visibilitystate" title="enum class in com.here.sdk.mapview">VisibilityState</a> visibility)</span></div>
<div class="block"><p>Immediately changes the visibility of a specified map layer.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>layerName</code> - <p>The name of the map layer to be changed.</p></dd>
<dd><code>visibility</code> - <p>The new visibility state of the layer.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActiveFeatures()">
<h3>getActiveFeatures</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getActiveFeatures</span>()</div>
<div class="block"><p>Gets map features that are currently active. Active features are features that are either
 enabled via a call to <a href="#enableFeatures(java.util.Map)"><code>enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a> or that are enabled by default in the scene.
 </p><p>The key to the resulting map is the name of the feature
 and the value is the active mode.
 </p><p>Result is empty if scene has not been loaded.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The map of active features.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupportedFeatures()">
<h3>getSupportedFeatures</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;&gt;</span> <span class="element-name">getSupportedFeatures</span>()</div>
<div class="block"><p>Gets features and all of their modes supported by the currently
 loaded scene configuration.
 </p><p>The key to the resulting map is the name of the feature
 and the value is a list of modes for that feature.
 </p><p>Result is empty if scene has not been loaded.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The map of supported features and all their modes.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="enableFeatures(java.util.Map)">
<h3>enableFeatures</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">enableFeatures</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; features)</span></div>
<div class="block"><p>Enables specified map features. Those will become active
 after next map redraw, meaning that <a href="#getActiveFeatures()"><code>getActiveFeatures()</code></a> will
 return updated list of active features only after the redraw happens.
 </p><p>Does not affect features that were not specified.
 Unsupported features are ignored.
 </p><p>May cause the current map configuration to be reloaded.
 </p><p>See <a href="sdk-for-android-navigate-mapfeatures" title="class in com.here.sdk.mapview"><code>MapFeatures</code></a> for feature names and <a href="sdk-for-android-navigate-mapfeaturemodes" title="class in com.here.sdk.mapview"><code>MapFeatureModes</code></a> for
 feature mode names.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>features</code> - <p>The list of features to enable, key is the name of the feature
     (see <a href="sdk-for-android-navigate-mapfeatures" title="class in com.here.sdk.mapview"><code>MapFeatures</code></a>), value specifies its mode (see <a href="sdk-for-android-navigate-mapfeaturemodes" title="class in com.here.sdk.mapview"><code>MapFeatureModes</code></a>).</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disableFeatures(java.util.List)">
<h3>disableFeatures</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disableFeatures</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; features)</span></div>
<div class="block"><p>Disables specified map features. Those will become inactive
 after next map redraw, meaning that <a href="#getActiveFeatures()"><code>getActiveFeatures()</code></a> will
 return updated list of active features only after the redraw happens.
 </p><p>Does not affect features that were not specified.
 Unsupported features are ignored.
 </p><p>May cause the current map configuration to be reloaded.
 </p><p>See <a href="sdk-for-android-navigate-mapfeatures" title="class in com.here.sdk.mapview"><code>MapFeatures</code></a> for feature names.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>features</code> - <p>The names of features to disable (see <a href="sdk-for-android-navigate-mapfeatures" title="class in com.here.sdk.mapview"><code>MapFeatures</code></a>).</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reloadScene()">
<h3>reloadScene</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reloadScene</span>()</div>
<div class="block"><p>Asynchronously reloads the current map scene from file. This skips any cached data used internally and reloads the
 scene including any changes made to the (custom) map styles in JSON.
 </p><p><code>MapFeature</code> settings will be preserved.
 </p><p>Internal optimization checks will be skipped to ensure all custom style changes are loaded. Therefore,
 calling this method may take slightly longer than calling one of the <code>loadScene(..)</code> overloads.</p></div>
</section>
</li>
<li>
<section class="detail" id="getLights()">
<h3>getLights</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapscenelights" title="class in com.here.sdk.mapview">MapSceneLights</a></span> <span class="element-name">getLights</span>()</div>
<div class="block"><p>Gets a MapSceneLights instance that controls lights present in the scene.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.
 </p><p>Provides access to a MapSceneLights instance that controls the lights in the scene.
 </p><p>The behavior of the returned MapSceneLights instance depends on the state of the scene:
 <ul>
<li>If the scene is not loaded, the returned MapSceneLights instance will not contain any light settings, as lights are not loaded without a scene.</li>
<li>If the scene is loaded, the returned MapSceneLights instance reflects the current light settings of the loaded scene.</li>
</ul>
</p><p>Scene Change Behavior:
 <ul>
<li>If the scene changes, the MapSceneLights instance will be updated to reflect the light settings of the new scene.</li>
<li>Any user-defined settings to MapSceneLights will be overridden by the new scene's light settings when the scene changes.</li>
</ul>
</p><p>Error Handling:
 <ul>
<li>If the scene is loaded and the loaded scene does not utilize or specify light settings:
 <ul>
<li>If the lights are not present, the error callback may return a NO_LIGHTS state.</li>
</ul>
</li>
</ul></p></div>
<dl class="notes">
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
</main>
</div>
</div>



</div>
`
}</HTMLBlock>

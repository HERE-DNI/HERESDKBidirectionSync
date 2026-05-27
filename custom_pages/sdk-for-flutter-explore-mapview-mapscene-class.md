---
title: "Map schemes"
slug: "sdk-for-flutter-explore-mapview-mapscene-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapScene-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapScene-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapScene/MapScene.html">MapScene</a></li>
<li class="section-title">
<a href="mapview/MapScene-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapScene/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapScene/lights.html">lights</a></li>
<li class="inherited"><a href="mapview/MapScene/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/MapScene-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MapScene/addMapArrow.html">addMapArrow</a></li>
<li><a href="mapview/MapScene/addMapImageOverlay.html">addMapImageOverlay</a></li>
<li><a href="mapview/MapScene/addMapMarker.html">addMapMarker</a></li>
<li><a href="mapview/MapScene/addMapMarker3d.html">addMapMarker3d</a></li>
<li><a href="mapview/MapScene/addMapMarkerCluster.html">addMapMarkerCluster</a></li>
<li><a href="mapview/MapScene/addMapMarkers.html">addMapMarkers</a></li>
<li><a href="mapview/MapScene/addMapMarkers3d.html">addMapMarkers3d</a></li>
<li><a href="mapview/MapScene/addMapPolygon.html">addMapPolygon</a></li>
<li><a href="mapview/MapScene/addMapPolygons.html">addMapPolygons</a></li>
<li><a href="mapview/MapScene/addMapPolyline.html">addMapPolyline</a></li>
<li><a href="mapview/MapScene/addMapPolylines.html">addMapPolylines</a></li>
<li><a href="mapview/MapScene/disableFeatures.html">disableFeatures</a></li>
<li><a href="mapview/MapScene/enableFeatures.html">enableFeatures</a></li>
<li><a href="mapview/MapScene/getActiveFeatures.html">getActiveFeatures</a></li>
<li><a href="mapview/MapScene/getSupportedFeatures.html">getSupportedFeatures</a></li>
<li><a href="mapview/MapScene/loadScene.html">loadScene</a></li>
<li><a href="mapview/MapScene/loadSceneForMapScheme.html">loadSceneForMapScheme</a></li>
<li><a href="mapview/MapScene/loadSceneFromConfigurationFile.html">loadSceneFromConfigurationFile</a></li>
<li><a href="mapview/MapScene/loadSceneFromConfigurationFileWithWatermarkStyle.html">loadSceneFromConfigurationFileWithWatermarkStyle</a></li>
<li class="inherited"><a href="mapview/MapScene/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MapScene/reloadScene.html">reloadScene</a></li>
<li><a href="mapview/MapScene/removeAllMapItems.html">removeAllMapItems</a></li>
<li><a href="mapview/MapScene/removeAllMapMarkers.html">removeAllMapMarkers</a></li>
<li><a href="mapview/MapScene/removeAllMapMarkers3d.html">removeAllMapMarkers3d</a></li>
<li><a href="mapview/MapScene/removeAllMapPolygons.html">removeAllMapPolygons</a></li>
<li><a href="mapview/MapScene/removeAllMapPolylines.html">removeAllMapPolylines</a></li>
<li><a href="mapview/MapScene/removeMapArrow.html">removeMapArrow</a></li>
<li><a href="mapview/MapScene/removeMapImageOverlay.html">removeMapImageOverlay</a></li>
<li><a href="mapview/MapScene/removeMapMarker.html">removeMapMarker</a></li>
<li><a href="mapview/MapScene/removeMapMarker3d.html">removeMapMarker3d</a></li>
<li><a href="mapview/MapScene/removeMapMarkerCluster.html">removeMapMarkerCluster</a></li>
<li><a href="mapview/MapScene/removeMapMarkers.html">removeMapMarkers</a></li>
<li><a href="mapview/MapScene/removeMapMarkers3d.html">removeMapMarkers3d</a></li>
<li><a href="mapview/MapScene/removeMapPolygon.html">removeMapPolygon</a></li>
<li><a href="mapview/MapScene/removeMapPolygons.html">removeMapPolygons</a></li>
<li><a href="mapview/MapScene/removeMapPolyline.html">removeMapPolyline</a></li>
<li><a href="mapview/MapScene/removeMapPolylines.html">removeMapPolylines</a></li>
<li><a href="mapview/MapScene/setLayerVisibility.html">setLayerVisibility</a></li>
<li class="inherited"><a href="mapview/MapScene/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapScene-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapScene/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapScene class</li>
</ol>
<div class="self-name">MapScene</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapScene-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapScene class abstract</h1></div>
<section class="desc markdown">
<p>Represents a map scene and exposes the functionality to manipulate its content.</p>
<h2 id="map-schemes">Map schemes</h2>
<p>The content of the displayed map and how it looks is specified by a
<a href="../mapview/MapScheme.html">/sdk-for-flutter-explore-mapview-mapscheme</a> which is set when loading a scene with <a href="../mapview/MapScene/loadSceneForMapScheme.html">/sdk-for-flutter-explore-mapview-mapscene-loadsceneformapscheme</a>.
It is also possible to load your own custom map scheme from a file bundled
with your application. Supported file formats are:</p>
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
<h2 id="map-features">Map features</h2>
<p>Different map schemes offer different sets of features, for example showing traffic or 3D buildings.
Some features have multiple modes of operation, but most have only one.
<a href="../mapview/MapScene/getSupportedFeatures.html">/sdk-for-flutter-explore-mapview-mapscene-getsupportedfeatures</a> can be used to check what features and modes are supported
for the current scene. Features can be enabled using <a href="../mapview/MapScene/enableFeatures.html">/sdk-for-flutter-explore-mapview-mapscene-enablefeatures</a> and disabled
with <a href="../mapview/MapScene/disableFeatures.html">/sdk-for-flutter-explore-mapview-mapscene-disablefeatures</a>. Checking which features are currently enabled can be done using
<a href="../mapview/MapScene/getActiveFeatures.html">/sdk-for-flutter-explore-mapview-mapscene-getactivefeatures</a>. For convenience, <a href="../mapview/MapFeatures-class.html">/sdk-for-flutter-explore-mapview-mapfeatures-class</a> and <a href="../mapview/MapFeatureModes-class.html">/sdk-for-flutter-explore-mapview-mapfeaturemodes-class</a> hold
constants for feature and mode names.</p>
<p>Since version 4.15.0, map features cannot be controlled using <a href="../mapview/MapScene/setLayerVisibility.html">/sdk-for-flutter-explore-mapview-mapscene-setlayervisibility</a>, since <a href="../mapview/MapScene/setLayerVisibility.html">/sdk-for-flutter-explore-mapview-mapscene-setlayervisibility</a> controls
only visibility of the layers which are corresponding to the features enabled either by <a href="../mapview/MapScene/enableFeatures.html">/sdk-for-flutter-explore-mapview-mapscene-enablefeatures</a>
or enabled by default for the scene.</p>
<h2 id="map-layers">Map layers</h2>
<p>A map scheme is organized in layers, which can be controlled using <a href="../mapview/MapScene/setLayerVisibility.html">/sdk-for-flutter-explore-mapview-mapscene-setlayervisibility</a>.
It's possible to change the visibility state of any map layer as long as the name is known.</p>
<p>Layer visibility settings persist between scene reloading.</p>
<h2 id="user-content">User content</h2>
<p>User generated content can be visualised on the map using <a href="../mapview/MapPolyline-class.html">/sdk-for-flutter-explore-mapview-mappolyline-class</a>, <a href="../mapview/MapPolygon-class.html">/sdk-for-flutter-explore-mapview-mappolygon-class</a>, <a href="../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a>,
<a href="../mapview/MapMarkerCluster-class.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-class</a>, <a href="../mapview/MapArrow-class.html">/sdk-for-flutter-explore-mapview-maparrow-class</a>, <a href="../mapview/MapMarker3D-class.html">/sdk-for-flutter-explore-mapview-mapmarker3d-class</a> and <a href="../mapview/MapImageOverlay-class.html">/sdk-for-flutter-explore-mapview-mapimageoverlay-class</a>
(collectively referred to as "map items"). Those can be added to and removed
from the scene by respective add and remove methods. The render order of the map items
is according to the list above. The order of objects within the same type can be controlled using
the <code>drawOrder</code> property of each object.</p>
<p>Be careful when adding a very large number of map items as this can have a negative impact on
the performance of the app.
To work around this limitation the following approach can be used:
Register to map camera updates using <a href="../mapview/MapCamera/addListener.html">/sdk-for-flutter-explore-mapview-mapcamera-addlistener</a>. Query the bounding box of the
camera viewport using <a href="../mapview/MapCamera/boundingBox.html">/sdk-for-flutter-explore-mapview-mapcamera-boundingbox</a> (it may be extended) and then use the method
<a href="../core/GeoBox/containsGeoCoordinates.html">/sdk-for-flutter-explore-core-geobox-containsgeocoordinates</a> in combination with <a href="../mapview/MapCameraState/distanceToTargetInMeters.html">/sdk-for-flutter-explore-mapview-mapcamerastate-distancetotargetinmeters</a> to
determine which map items are actually visible to the user in the current camera viewport and
thus need to be added to the map.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapScene">
<a href="../mapview/MapScene/MapScene.html">/sdk-for-flutter-explore-mapview-mapscene-mapscene</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapScene/hashCode.html">/sdk-for-flutter-explore-mapview-mapscene-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="lights">
<a href="../mapview/MapScene/lights.html">/sdk-for-flutter-explore-mapview-mapscene-lights</a>
→ <a href="../mapview/MapSceneLights-class.html">/sdk-for-flutter-explore-mapview-mapscenelights-class</a>
</dt>
<dd>
  Controls lights present in the scene.
Provides access to a MapSceneLights instance that controls the lights in the scene.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapScene/runtimeType.html">/sdk-for-flutter-explore-mapview-mapscene-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="addMapArrow">
<a href="../mapview/MapScene/addMapArrow.html">/sdk-for-flutter-explore-mapview-mapscene-addmaparrow</a>(<wbr/><a href="../mapview/MapArrow-class.html">/sdk-for-flutter-explore-mapview-maparrow-class</a> mapArrow)
    → void

</dt>
<dd>
  Adds a map arrow to this map scene.
  

</dd>
<dt class="callable" id="addMapImageOverlay">
<a href="../mapview/MapScene/addMapImageOverlay.html">/sdk-for-flutter-explore-mapview-mapscene-addmapimageoverlay</a>(<wbr/><a href="../mapview/MapImageOverlay-class.html">/sdk-for-flutter-explore-mapview-mapimageoverlay-class</a> overlay)
    → void

</dt>
<dd>
  Adds a map image overlay to this map scene.
  

</dd>
<dt class="callable" id="addMapMarker">
<a href="../mapview/MapScene/addMapMarker.html">/sdk-for-flutter-explore-mapview-mapscene-addmapmarker</a>(<wbr/><a href="../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a> marker)
    → void

</dt>
<dd>
  Adds a map marker to this map scene.
  

</dd>
<dt class="callable" id="addMapMarker3d">
<a href="../mapview/MapScene/addMapMarker3d.html">/sdk-for-flutter-explore-mapview-mapscene-addmapmarker3d</a>(<wbr/><a href="../mapview/MapMarker3D-class.html">/sdk-for-flutter-explore-mapview-mapmarker3d-class</a> marker)
    → void

</dt>
<dd>
  Adds a 3D map marker to this map scene.
  

</dd>
<dt class="callable" id="addMapMarkerCluster">
<a href="../mapview/MapScene/addMapMarkerCluster.html">/sdk-for-flutter-explore-mapview-mapscene-addmapmarkercluster</a>(<wbr/><a href="../mapview/MapMarkerCluster-class.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-class</a> cluster)
    → void

</dt>
<dd>
  Adds a map marker cluster to the map.
  

</dd>
<dt class="callable" id="addMapMarkers">
<a href="../mapview/MapScene/addMapMarkers.html">/sdk-for-flutter-explore-mapview-mapscene-addmapmarkers</a>(<wbr/>List&lt;<wbr/><a href="../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a>&gt; markers)
    → void

</dt>
<dd>
  Adds multiple map markers to this map scene.
  

</dd>
<dt class="callable" id="addMapMarkers3d">
<a href="../mapview/MapScene/addMapMarkers3d.html">/sdk-for-flutter-explore-mapview-mapscene-addmapmarkers3d</a>(<wbr/>List&lt;<wbr/><a href="../mapview/MapMarker3D-class.html">/sdk-for-flutter-explore-mapview-mapmarker3d-class</a>&gt; markers)
    → void

</dt>
<dd>
  Adds multiple 3D map markers to this map scene.
  

</dd>
<dt class="callable" id="addMapPolygon">
<a href="../mapview/MapScene/addMapPolygon.html">/sdk-for-flutter-explore-mapview-mapscene-addmappolygon</a>(<wbr/><a href="../mapview/MapPolygon-class.html">/sdk-for-flutter-explore-mapview-mappolygon-class</a> mapPolygon)
    → void

</dt>
<dd>
  Adds a map polygon to this map scene.
  

</dd>
<dt class="callable" id="addMapPolygons">
<a href="../mapview/MapScene/addMapPolygons.html">/sdk-for-flutter-explore-mapview-mapscene-addmappolygons</a>(<wbr/>List&lt;<wbr/><a href="../mapview/MapPolygon-class.html">/sdk-for-flutter-explore-mapview-mappolygon-class</a>&gt; mapPolygons)
    → void

</dt>
<dd>
  Adds multiple map polygons to this map scene.
  

</dd>
<dt class="callable" id="addMapPolyline">
<a href="../mapview/MapScene/addMapPolyline.html">/sdk-for-flutter-explore-mapview-mapscene-addmappolyline</a>(<wbr/><a href="../mapview/MapPolyline-class.html">/sdk-for-flutter-explore-mapview-mappolyline-class</a> mapPolyline)
    → void

</dt>
<dd>
  Adds a map polyline to this map scene.
  

</dd>
<dt class="callable" id="addMapPolylines">
<a href="../mapview/MapScene/addMapPolylines.html">/sdk-for-flutter-explore-mapview-mapscene-addmappolylines</a>(<wbr/>List&lt;<wbr/><a href="../mapview/MapPolyline-class.html">/sdk-for-flutter-explore-mapview-mappolyline-class</a>&gt; mapPolylines)
    → void

</dt>
<dd>
  Adds map polylines to this map scene.
  

</dd>
<dt class="callable" id="disableFeatures">
<a href="../mapview/MapScene/disableFeatures.html">/sdk-for-flutter-explore-mapview-mapscene-disablefeatures</a>(<wbr/>List&lt;<wbr/>String&gt; features)
    → void

</dt>
<dd>
  Disables specified map features.
  

</dd>
<dt class="callable" id="enableFeatures">
<a href="../mapview/MapScene/enableFeatures.html">/sdk-for-flutter-explore-mapview-mapscene-enablefeatures</a>(<wbr/>Map&lt;<wbr/>String, String&gt; features)
    → void

</dt>
<dd>
  Enables specified map features.
  

</dd>
<dt class="callable" id="getActiveFeatures">
<a href="../mapview/MapScene/getActiveFeatures.html">/sdk-for-flutter-explore-mapview-mapscene-getactivefeatures</a>(<wbr/>)
    → Map&lt;<wbr/>String, String&gt;

</dt>
<dd>
  Gets map features that are currently active.
  

</dd>
<dt class="callable" id="getSupportedFeatures">
<a href="../mapview/MapScene/getSupportedFeatures.html">/sdk-for-flutter-explore-mapview-mapscene-getsupportedfeatures</a>(<wbr/>)
    → Map&lt;<wbr/>String, List&lt;<wbr/>String&gt;&gt;

</dt>
<dd>
  Gets features and all of their modes supported by the currently
loaded scene configuration.
  

</dd>
<dt class="callable" id="loadScene">
<a href="../mapview/MapScene/loadScene.html">/sdk-for-flutter-explore-mapview-mapscene-loadscene</a>(<wbr/><a href="../mapview/MapSceneLoadOptions-class.html">/sdk-for-flutter-explore-mapview-mapsceneloadoptions-class</a> options, <a href="../mapview/MapSceneLoadSceneCallback.html">/sdk-for-flutter-explore-mapview-mapsceneloadscenecallback</a>? callback)
    → void

</dt>
<dd>
  Asynchronously loads a map scene using MapSceneLoadOptions.
  

</dd>
<dt class="callable" id="loadSceneForMapScheme">
<a href="../mapview/MapScene/loadSceneForMapScheme.html">/sdk-for-flutter-explore-mapview-mapscene-loadsceneformapscheme</a>(<wbr/><a href="../mapview/MapScheme.html">/sdk-for-flutter-explore-mapview-mapscheme</a> mapScheme, <a href="../mapview/MapSceneLoadSceneCallback.html">/sdk-for-flutter-explore-mapview-mapsceneloadscenecallback</a>? callback)
    → void

</dt>
<dd>
  Asynchronously loads a map scene described by a specified map scheme.
  

</dd>
<dt class="callable" id="loadSceneFromConfigurationFile">
<a href="../mapview/MapScene/loadSceneFromConfigurationFile.html">/sdk-for-flutter-explore-mapview-mapscene-loadscenefromconfigurationfile</a>(<wbr/>String configurationFile, <a href="../mapview/MapSceneLoadSceneCallback.html">/sdk-for-flutter-explore-mapview-mapsceneloadscenecallback</a>? callback)
    → void

</dt>
<dd>
  Asynchronously loads a map scene described by a specified file in one of the supported formats.
  

</dd>
<dt class="callable" id="loadSceneFromConfigurationFileWithWatermarkStyle">
<a href="../mapview/MapScene/loadSceneFromConfigurationFileWithWatermarkStyle.html">/sdk-for-flutter-explore-mapview-mapscene-loadscenefromconfigurationfilewithwatermarkstyle</a>(<wbr/>String configurationFile, <a href="../mapview/WatermarkStyle.html">/sdk-for-flutter-explore-mapview-watermarkstyle</a> watermarkStyle, <a href="../mapview/MapSceneLoadSceneCallback.html">/sdk-for-flutter-explore-mapview-mapsceneloadscenecallback</a>? callback)
    → void

</dt>
<dd>
  Asynchronously loads a map scene described by a specified file in one of the supported formats.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapScene/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mapscene-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="reloadScene">
<a href="../mapview/MapScene/reloadScene.html">/sdk-for-flutter-explore-mapview-mapscene-reloadscene</a>(<wbr/>)
    → void

</dt>
<dd>
  Asynchronously reloads the current map scene from file.
  

</dd>
<dt class="callable" id="removeAllMapItems">
<a href="../mapview/MapScene/removeAllMapItems.html">/sdk-for-flutter-explore-mapview-mapscene-removeallmapitems</a>(<wbr/>)
    → void

</dt>
<dd>
  Removes all map objects from this map scene.
  

</dd>
<dt class="callable" id="removeAllMapMarkers">
<a href="../mapview/MapScene/removeAllMapMarkers.html">/sdk-for-flutter-explore-mapview-mapscene-removeallmapmarkers</a>(<wbr/>)
    → void

</dt>
<dd>
  Removes all map markers from this map scene.
  

</dd>
<dt class="callable" id="removeAllMapMarkers3d">
<a href="../mapview/MapScene/removeAllMapMarkers3d.html">/sdk-for-flutter-explore-mapview-mapscene-removeallmapmarkers3d</a>(<wbr/>)
    → void

</dt>
<dd>
  Removes all 3D map markers from this map scene.
  

</dd>
<dt class="callable" id="removeAllMapPolygons">
<a href="../mapview/MapScene/removeAllMapPolygons.html">/sdk-for-flutter-explore-mapview-mapscene-removeallmappolygons</a>(<wbr/>)
    → void

</dt>
<dd>
  Removes all map polygons from this map scene.
  

</dd>
<dt class="callable" id="removeAllMapPolylines">
<a href="../mapview/MapScene/removeAllMapPolylines.html">/sdk-for-flutter-explore-mapview-mapscene-removeallmappolylines</a>(<wbr/>)
    → void

</dt>
<dd>
  Removes all map polylines from this map scene.
  

</dd>
<dt class="callable" id="removeMapArrow">
<a href="../mapview/MapScene/removeMapArrow.html">/sdk-for-flutter-explore-mapview-mapscene-removemaparrow</a>(<wbr/><a href="../mapview/MapArrow-class.html">/sdk-for-flutter-explore-mapview-maparrow-class</a> mapArrow)
    → void

</dt>
<dd>
  Removes a map arrow from this map scene.
  

</dd>
<dt class="callable" id="removeMapImageOverlay">
<a href="../mapview/MapScene/removeMapImageOverlay.html">/sdk-for-flutter-explore-mapview-mapscene-removemapimageoverlay</a>(<wbr/><a href="../mapview/MapImageOverlay-class.html">/sdk-for-flutter-explore-mapview-mapimageoverlay-class</a> overlay)
    → void

</dt>
<dd>
  Removes a map image overlay from this map scene.
  

</dd>
<dt class="callable" id="removeMapMarker">
<a href="../mapview/MapScene/removeMapMarker.html">/sdk-for-flutter-explore-mapview-mapscene-removemapmarker</a>(<wbr/><a href="../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a> marker)
    → void

</dt>
<dd>
  Removes a map marker from this map scene.
  

</dd>
<dt class="callable" id="removeMapMarker3d">
<a href="../mapview/MapScene/removeMapMarker3d.html">/sdk-for-flutter-explore-mapview-mapscene-removemapmarker3d</a>(<wbr/><a href="../mapview/MapMarker3D-class.html">/sdk-for-flutter-explore-mapview-mapmarker3d-class</a> marker)
    → void

</dt>
<dd>
  Removes a 3D map marker from this map scene.
  

</dd>
<dt class="callable" id="removeMapMarkerCluster">
<a href="../mapview/MapScene/removeMapMarkerCluster.html">/sdk-for-flutter-explore-mapview-mapscene-removemapmarkercluster</a>(<wbr/><a href="../mapview/MapMarkerCluster-class.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-class</a> cluster)
    → void

</dt>
<dd>
  Removes a map marker cluster from the map.
  

</dd>
<dt class="callable" id="removeMapMarkers">
<a href="../mapview/MapScene/removeMapMarkers.html">/sdk-for-flutter-explore-mapview-mapscene-removemapmarkers</a>(<wbr/>List&lt;<wbr/><a href="../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a>&gt; markers)
    → void

</dt>
<dd>
  Removes multiple map markers from this map scene.
  

</dd>
<dt class="callable" id="removeMapMarkers3d">
<a href="../mapview/MapScene/removeMapMarkers3d.html">/sdk-for-flutter-explore-mapview-mapscene-removemapmarkers3d</a>(<wbr/>List&lt;<wbr/><a href="../mapview/MapMarker3D-class.html">/sdk-for-flutter-explore-mapview-mapmarker3d-class</a>&gt; markers)
    → void

</dt>
<dd>
  Removes multiple 3D map markers from this map scene.
  

</dd>
<dt class="callable" id="removeMapPolygon">
<a href="../mapview/MapScene/removeMapPolygon.html">/sdk-for-flutter-explore-mapview-mapscene-removemappolygon</a>(<wbr/><a href="../mapview/MapPolygon-class.html">/sdk-for-flutter-explore-mapview-mappolygon-class</a> mapPolygon)
    → void

</dt>
<dd>
  Removes a map polygon from this map scene.
  

</dd>
<dt class="callable" id="removeMapPolygons">
<a href="../mapview/MapScene/removeMapPolygons.html">/sdk-for-flutter-explore-mapview-mapscene-removemappolygons</a>(<wbr/>List&lt;<wbr/><a href="../mapview/MapPolygon-class.html">/sdk-for-flutter-explore-mapview-mappolygon-class</a>&gt; mapPolygons)
    → void

</dt>
<dd>
  Removes multiple map polygon from this map scene.
  

</dd>
<dt class="callable" id="removeMapPolyline">
<a href="../mapview/MapScene/removeMapPolyline.html">/sdk-for-flutter-explore-mapview-mapscene-removemappolyline</a>(<wbr/><a href="../mapview/MapPolyline-class.html">/sdk-for-flutter-explore-mapview-mappolyline-class</a> mapPolyline)
    → void

</dt>
<dd>
  Removes a map polyline from this map scene.
  

</dd>
<dt class="callable" id="removeMapPolylines">
<a href="../mapview/MapScene/removeMapPolylines.html">/sdk-for-flutter-explore-mapview-mapscene-removemappolylines</a>(<wbr/>List&lt;<wbr/><a href="../mapview/MapPolyline-class.html">/sdk-for-flutter-explore-mapview-mappolyline-class</a>&gt; mapPolylines)
    → void

</dt>
<dd>
  Removes map polylines from this map scene.
  

</dd>
<dt class="callable" id="setLayerVisibility">
<a href="../mapview/MapScene/setLayerVisibility.html">/sdk-for-flutter-explore-mapview-mapscene-setlayervisibility</a>(<wbr/>String layerName, <a href="../mapview/VisibilityState.html">/sdk-for-flutter-explore-mapview-visibilitystate</a> visibility)
    → void

</dt>
<dd>
  Immediately changes the visibility of a specified map layer.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapScene/toString.html">/sdk-for-flutter-explore-mapview-mapscene-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../mapview/MapScene/operator_equals.html">/sdk-for-flutter-explore-mapview-mapscene-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapScene class</li>
</ol>
<h5>mapview library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>

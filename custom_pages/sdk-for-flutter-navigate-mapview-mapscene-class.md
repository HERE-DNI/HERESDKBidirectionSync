---
title: "MapScene class abstract"
slug: "sdk-for-flutter-navigate-mapview-mapscene-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapScene-class.html -->


<div>
<h1>MapScene class abstract</h1></div>

<p>Represents a map scene and exposes the functionality to manipulate its content.</p>
<h2 id="map-schemes">Map schemes</h2>
<p>The content of the displayed map and how it looks is specified by a
<a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme</a> which is set when loading a scene with <a href="sdk-for-flutter-navigate-mapview-mapscene-loadsceneformapscheme">MapScene.loadSceneForMapScheme</a>.
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
<a href="sdk-for-flutter-navigate-mapview-mapscene-getsupportedfeatures">MapScene.getSupportedFeatures</a> can be used to check what features and modes are supported
for the current scene. Features can be enabled using <a href="sdk-for-flutter-navigate-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> and disabled
with <a href="sdk-for-flutter-navigate-mapview-mapscene-disablefeatures">MapScene.disableFeatures</a>. Checking which features are currently enabled can be done using
<a href="sdk-for-flutter-navigate-mapview-mapscene-getactivefeatures">MapScene.getActiveFeatures</a>. For convenience, <a href="sdk-for-flutter-navigate-mapview-mapfeatures-class">MapFeatures</a> and <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-class">MapFeatureModes</a> hold
constants for feature and mode names.</p>
<p>Since version 4.15.0, map features cannot be controlled using <a href="sdk-for-flutter-navigate-mapview-mapscene-setlayervisibility">MapScene.setLayerVisibility</a>, since <a href="sdk-for-flutter-navigate-mapview-mapscene-setlayervisibility">MapScene.setLayerVisibility</a> controls
only visibility of the layers which are corresponding to the features enabled either by <a href="sdk-for-flutter-navigate-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a>
or enabled by default for the scene.</p>
<h2 id="map-layers">Map layers</h2>
<p>A map scheme is organized in layers, which can be controlled using <a href="sdk-for-flutter-navigate-mapview-mapscene-setlayervisibility">MapScene.setLayerVisibility</a>.
It's possible to change the visibility state of any map layer as long as the name is known.</p>
<p>Layer visibility settings persist between scene reloading.</p>
<h2 id="user-content">User content</h2>
<p>User generated content can be visualised on the map using <a href="sdk-for-flutter-navigate-mapview-mappolyline-class">MapPolyline</a>, <a href="sdk-for-flutter-navigate-mapview-mappolygon-class">MapPolygon</a>, <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>,
<a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-class">MapMarkerCluster</a>, <a href="sdk-for-flutter-navigate-mapview-maparrow-class">MapArrow</a>, <a href="sdk-for-flutter-navigate-mapview-mapmarker3d-class">MapMarker3D</a> and <a href="sdk-for-flutter-navigate-mapview-mapimageoverlay-class">MapImageOverlay</a>
(collectively referred to as "map items"). Those can be added to and removed
from the scene by respective add and remove methods. The render order of the map items
is according to the list above. The order of objects within the same type can be controlled using
the <code>drawOrder</code> property of each object.</p>
<p>Be careful when adding a very large number of map items as this can have a negative impact on
the performance of the app.
To work around this limitation the following approach can be used:
Register to map camera updates using <a href="sdk-for-flutter-navigate-mapview-mapcamera-addlistener">MapCamera.addListener</a>. Query the bounding box of the
camera viewport using <a href="sdk-for-flutter-navigate-mapview-mapcamera-boundingbox">MapCamera.boundingBox</a> (it may be extended) and then use the method
<a href="sdk-for-flutter-navigate-core-geobox-containsgeocoordinates">GeoBox.containsGeoCoordinates</a> in combination with <a href="sdk-for-flutter-navigate-mapview-mapcamerastate-distancetotargetinmeters">MapCameraState.distanceToTargetInMeters</a> to
determine which map items are actually visible to the user in the current camera viewport and
thus need to be added to the map.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-mapscene-mapscene">MapScene</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-mapscene-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-lights">lights</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-mapscene-addmaparrow">addMapArrow</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-addmapimageoverlay">addMapImageOverlay</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-addmapmarker">addMapMarker</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-addmapmarker3d">addMapMarker3d</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-addmapmarkercluster">addMapMarkerCluster</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-addmapmarkers">addMapMarkers</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-addmapmarkers3d">addMapMarkers3d</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-addmappolygon">addMapPolygon</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-addmappolygons">addMapPolygons</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-addmappolyline">addMapPolyline</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-addmappolylines">addMapPolylines</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-disablefeatures">disableFeatures</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-enablefeatures">enableFeatures</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-getactivefeatures">getActiveFeatures</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-getsupportedfeatures">getSupportedFeatures</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-loadscene">loadScene</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-loadsceneformapscheme">loadSceneForMapScheme</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-loadscenefromconfigurationfile">loadSceneFromConfigurationFile</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-loadscenefromconfigurationfilewithwatermarkstyle">loadSceneFromConfigurationFileWithWatermarkStyle</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-reloadscene">reloadScene</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removeallmapitems">removeAllMapItems</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removeallmapmarkers">removeAllMapMarkers</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removeallmapmarkers3d">removeAllMapMarkers3d</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removeallmappolygons">removeAllMapPolygons</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removeallmappolylines">removeAllMapPolylines</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removemaparrow">removeMapArrow</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removemapimageoverlay">removeMapImageOverlay</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removemapmarker">removeMapMarker</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removemapmarker3d">removeMapMarker3d</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removemapmarkercluster">removeMapMarkerCluster</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removemapmarkers">removeMapMarkers</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removemapmarkers3d">removeMapMarkers3d</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removemappolygon">removeMapPolygon</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removemappolygons">removeMapPolygons</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removemappolyline">removeMapPolyline</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-removemappolylines">removeMapPolylines</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-setlayervisibility">setLayerVisibility</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapscene-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-mapscene-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>

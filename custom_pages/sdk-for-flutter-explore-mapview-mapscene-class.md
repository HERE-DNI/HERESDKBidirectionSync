---
title: "MapScene class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscene-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapScene-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapScene-class-sidebar.html">

<div>

# <span class="kind-class">MapScene</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents a map scene and exposes the functionality to manipulate its content.

## Map schemes

The content of the displayed map and how it looks is specified by a <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme</a> which is set when loading a scene with <a href="sdk-for-flutter-explore-mapview-mapscene-loadsceneformapscheme">MapScene.loadSceneForMapScheme</a>. It is also possible to load your own custom map scheme from a file bundled with your application. Supported file formats are:

- JSON (file extension '.json'; e.g. 'my_custom_style.json')
- ZIP archive (file extension '.zip'; e.g. 'my_custom_style.zip'), with the following archive structure:
  - root folder: any, not empty (e.g. 'my_custom_style')
  - JSON configuration: '<root folder>/style.json'</root>
  - custom assets folder: '<root folder>/assets'</root>

## Map features

Different map schemes offer different sets of features, for example showing traffic or 3D buildings. Some features have multiple modes of operation, but most have only one. <a href="sdk-for-flutter-explore-mapview-mapscene-getsupportedfeatures">MapScene.getSupportedFeatures</a> can be used to check what features and modes are supported for the current scene. Features can be enabled using <a href="sdk-for-flutter-explore-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> and disabled with <a href="sdk-for-flutter-explore-mapview-mapscene-disablefeatures">MapScene.disableFeatures</a>. Checking which features are currently enabled can be done using <a href="sdk-for-flutter-explore-mapview-mapscene-getactivefeatures">MapScene.getActiveFeatures</a>. For convenience, <a href="sdk-for-flutter-explore-mapview-mapfeatures-class">MapFeatures</a> and <a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-class">MapFeatureModes</a> hold constants for feature and mode names.

Since version 4.15.0, map features cannot be controlled using <a href="sdk-for-flutter-explore-mapview-mapscene-setlayervisibility">MapScene.setLayerVisibility</a>, since <a href="sdk-for-flutter-explore-mapview-mapscene-setlayervisibility">MapScene.setLayerVisibility</a> controls only visibility of the layers which are corresponding to the features enabled either by <a href="sdk-for-flutter-explore-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> or enabled by default for the scene.

## Map layers

A map scheme is organized in layers, which can be controlled using <a href="sdk-for-flutter-explore-mapview-mapscene-setlayervisibility">MapScene.setLayerVisibility</a>. It's possible to change the visibility state of any map layer as long as the name is known.

Layer visibility settings persist between scene reloading.

## User content

User generated content can be visualised on the map using <a href="sdk-for-flutter-explore-mapview-mappolyline-class">MapPolyline</a>, <a href="sdk-for-flutter-explore-mapview-mappolygon-class">MapPolygon</a>, <a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a>, <a href="sdk-for-flutter-explore-mapview-mapmarkercluster-class">MapMarkerCluster</a>, <a href="sdk-for-flutter-explore-mapview-maparrow-class">MapArrow</a>, <a href="sdk-for-flutter-explore-mapview-mapmarker3d-class">MapMarker3D</a> and <a href="sdk-for-flutter-explore-mapview-mapimageoverlay-class">MapImageOverlay</a> (collectively referred to as "map items"). Those can be added to and removed from the scene by respective add and remove methods. The render order of the map items is according to the list above. The order of objects within the same type can be controlled using the `drawOrder` property of each object.

Be careful when adding a very large number of map items as this can have a negative impact on the performance of the app. To work around this limitation the following approach can be used: Register to map camera updates using <a href="sdk-for-flutter-explore-mapview-mapcamera-addlistener">MapCamera.addListener</a>. Query the bounding box of the camera viewport using <a href="sdk-for-flutter-explore-mapview-mapcamera-boundingbox">MapCamera.boundingBox</a> (it may be extended) and then use the method <a href="sdk-for-flutter-explore-core-geobox-containsgeocoordinates">GeoBox.containsGeoCoordinates</a> in combination with <a href="sdk-for-flutter-explore-mapview-mapcamerastate-distancetotargetinmeters">MapCameraState.distanceToTargetInMeters</a> to determine which map items are actually visible to the user in the current camera viewport and thus need to be added to the map.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-mapscene">MapScene</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-lights">lights</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-mapview-mapscenelights-class">MapSceneLights</a></span>  
Controls lights present in the scene. Provides access to a MapSceneLights instance that controls the lights in the scene.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-addmaparrow">addMapArrow</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapArrow-param-mapArrow" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-maparrow-class">MapArrow</a></span> <span class="parameter-name">mapArrow</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a map arrow to this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-addmapimageoverlay">addMapImageOverlay</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapImageOverlay-param-overlay" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapimageoverlay-class">MapImageOverlay</a></span> <span class="parameter-name">overlay</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a map image overlay to this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-addmapmarker">addMapMarker</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapMarker-param-marker" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a></span> <span class="parameter-name">marker</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a map marker to this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-addmapmarker3d">addMapMarker3d</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapMarker3d-param-marker" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-class">MapMarker3D</a></span> <span class="parameter-name">marker</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a 3D map marker to this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-addmapmarkercluster">addMapMarkerCluster</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapMarkerCluster-param-cluster" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-class">MapMarkerCluster</a></span> <span class="parameter-name">cluster</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a map marker cluster to the map.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-addmapmarkers">addMapMarkers</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapMarkers-param-markers" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a></span>\></span></span> <span class="parameter-name">markers</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds multiple map markers to this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-addmapmarkers3d">addMapMarkers3d</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapMarkers3d-param-markers" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-class">MapMarker3D</a></span>\></span></span> <span class="parameter-name">markers</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds multiple 3D map markers to this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-addmappolygon">addMapPolygon</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapPolygon-param-mapPolygon" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mappolygon-class">MapPolygon</a></span> <span class="parameter-name">mapPolygon</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a map polygon to this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-addmappolygons">addMapPolygons</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapPolygons-param-mapPolygons" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mappolygon-class">MapPolygon</a></span>\></span></span> <span class="parameter-name">mapPolygons</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds multiple map polygons to this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-addmappolyline">addMapPolyline</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapPolyline-param-mapPolyline" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mappolyline-class">MapPolyline</a></span> <span class="parameter-name">mapPolyline</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a map polyline to this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-addmappolylines">addMapPolylines</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapPolylines-param-mapPolylines" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mappolyline-class">MapPolyline</a></span>\></span></span> <span class="parameter-name">mapPolylines</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds map polylines to this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-disablefeatures">disableFeatures</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-disableFeatures-param-features" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">features</span></span>) <span class="returntype parameter">→ void</span> </span>  
Disables specified map features.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-enablefeatures">enableFeatures</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-enableFeatures-param-features" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>, <span class="type-parameter">String</span>\></span></span> <span class="parameter-name">features</span></span>) <span class="returntype parameter">→ void</span> </span>  
Enables specified map features.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-getactivefeatures">getActiveFeatures</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ Map<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>, <span class="type-parameter">String</span>\></span></span> </span>  
Gets map features that are currently active.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-getsupportedfeatures">getSupportedFeatures</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ Map<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>, <span class="type-parameter">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>\></span></span> </span>  
Gets features and all of their modes supported by the currently loaded scene configuration.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-loadscene">loadScene</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-loadScene-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptions-class">MapSceneLoadOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-explore-loadScene-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapsceneloadscenecallback">MapSceneLoadSceneCallback</a>?</span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Asynchronously loads a map scene using MapSceneLoadOptions.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-loadsceneformapscheme">loadSceneForMapScheme</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-loadSceneForMapScheme-param-mapScheme" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme</a></span> <span class="parameter-name">mapScheme</span>, </span><span id="sdk-for-flutter-explore-loadSceneForMapScheme-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapsceneloadscenecallback">MapSceneLoadSceneCallback</a>?</span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Asynchronously loads a map scene described by a specified map scheme.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-loadscenefromconfigurationfile">loadSceneFromConfigurationFile</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-loadSceneFromConfigurationFile-param-configurationFile" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">configurationFile</span>, </span><span id="sdk-for-flutter-explore-loadSceneFromConfigurationFile-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapsceneloadscenecallback">MapSceneLoadSceneCallback</a>?</span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Asynchronously loads a map scene described by a specified file in one of the supported formats.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-loadscenefromconfigurationfilewithwatermarkstyle">loadSceneFromConfigurationFileWithWatermarkStyle</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-loadSceneFromConfigurationFileWithWatermarkStyle-param-configurationFile" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">configurationFile</span>, </span><span id="sdk-for-flutter-explore-loadSceneFromConfigurationFileWithWatermarkStyle-param-watermarkStyle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-watermarkstyle">WatermarkStyle</a></span> <span class="parameter-name">watermarkStyle</span>, </span><span id="sdk-for-flutter-explore-loadSceneFromConfigurationFileWithWatermarkStyle-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapsceneloadscenecallback">MapSceneLoadSceneCallback</a>?</span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Asynchronously loads a map scene described by a specified file in one of the supported formats.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-reloadscene">reloadScene</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Asynchronously reloads the current map scene from file.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removeallmapitems">removeAllMapItems</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Removes all map objects from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removeallmapmarkers">removeAllMapMarkers</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Removes all map markers from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removeallmapmarkers3d">removeAllMapMarkers3d</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Removes all 3D map markers from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removeallmappolygons">removeAllMapPolygons</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Removes all map polygons from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removeallmappolylines">removeAllMapPolylines</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Removes all map polylines from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removemaparrow">removeMapArrow</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapArrow-param-mapArrow" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-maparrow-class">MapArrow</a></span> <span class="parameter-name">mapArrow</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a map arrow from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removemapimageoverlay">removeMapImageOverlay</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapImageOverlay-param-overlay" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapimageoverlay-class">MapImageOverlay</a></span> <span class="parameter-name">overlay</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a map image overlay from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removemapmarker">removeMapMarker</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapMarker-param-marker" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a></span> <span class="parameter-name">marker</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a map marker from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removemapmarker3d">removeMapMarker3d</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapMarker3d-param-marker" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-class">MapMarker3D</a></span> <span class="parameter-name">marker</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a 3D map marker from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removemapmarkercluster">removeMapMarkerCluster</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapMarkerCluster-param-cluster" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-class">MapMarkerCluster</a></span> <span class="parameter-name">cluster</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a map marker cluster from the map.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removemapmarkers">removeMapMarkers</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapMarkers-param-markers" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a></span>\></span></span> <span class="parameter-name">markers</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes multiple map markers from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removemapmarkers3d">removeMapMarkers3d</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapMarkers3d-param-markers" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-class">MapMarker3D</a></span>\></span></span> <span class="parameter-name">markers</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes multiple 3D map markers from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removemappolygon">removeMapPolygon</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapPolygon-param-mapPolygon" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mappolygon-class">MapPolygon</a></span> <span class="parameter-name">mapPolygon</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a map polygon from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removemappolygons">removeMapPolygons</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapPolygons-param-mapPolygons" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mappolygon-class">MapPolygon</a></span>\></span></span> <span class="parameter-name">mapPolygons</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes multiple map polygon from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removemappolyline">removeMapPolyline</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapPolyline-param-mapPolyline" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mappolyline-class">MapPolyline</a></span> <span class="parameter-name">mapPolyline</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a map polyline from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-removemappolylines">removeMapPolylines</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapPolylines-param-mapPolylines" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mappolyline-class">MapPolyline</a></span>\></span></span> <span class="parameter-name">mapPolylines</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes map polylines from this map scene.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-setlayervisibility">setLayerVisibility</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setLayerVisibility-param-layerName" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">layerName</span>, </span><span id="sdk-for-flutter-explore-setLayerVisibility-param-visibility" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-visibilitystate">VisibilityState</a></span> <span class="parameter-name">visibility</span></span>) <span class="returntype parameter">→ void</span> </span>  
Immediately changes the visibility of a specified map layer.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscene-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

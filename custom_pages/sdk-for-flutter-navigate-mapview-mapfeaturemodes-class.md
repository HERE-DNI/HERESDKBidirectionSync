---
title: "MapFeatureModes class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapfeaturemodes-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapFeatureModes-class-sidebar.html">

<div>

# <span class="kind-class">MapFeatureModes</span> class

</div>

<div class="section desc markdown">

Holds constants for map feature modes, to be used with <a href="sdk-for-flutter-navigate-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a>.

Use <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-defaultmode">MapFeatureModes.defaultMode</a> to enable a feature with its default mode.

Note: The default mode is defined by the currently loaded map scene configuration and may vary per <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme</a>. The currently active features and modes can be inspected using <a href="sdk-for-flutter-navigate-mapview-mapscene-getactivefeatures">MapScene.getActiveFeatures</a> after the scene is loaded.

See <a href="sdk-for-flutter-navigate-mapview-mapfeatures-class">MapFeatures</a> for constants representing the feature names.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-mapfeaturemodes">MapFeatureModes</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-ambientocclusionall">ambientOcclusionAll</a></span> <span class="signature">→ String</span>  
Ambient occlusion effect is shown for extruded buildings and landmarks.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-buildingfootprintsall">buildingFootprintsAll</a></span> <span class="signature">→ String</span>  
All building footprints are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-congestionzonesall">congestionZonesAll</a></span> <span class="signature">→ String</span>  
All congestion zones are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-contoursall">contoursAll</a></span> <span class="signature">→ String</span>  
Contour lines indicating representing elevation changes are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-defaultmode">defaultMode</a></span> <span class="signature">→ String</span>  
Enables the default mode of a map feature. Can be used with any map feature.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-environmentalzonesall">environmentalZonesAll</a></span> <span class="signature">→ String</span>  
All environmental zones are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-extrudedbuildingsall">extrudedBuildingsAll</a></span> <span class="signature">→ String</span>  
All extruded buildings are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-landmarksgrayscale">landmarksGrayscale</a></span> <span class="signature">→ String</span>  
3D landmarks are textured with grayscale filter.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-landmarkstextured">landmarksTextured</a></span> <span class="signature">→ String</span>  
3D landmarks are textured.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-landmarkstextureless">landmarksTextureless</a></span> <span class="signature">→ String</span>  
3D landmarks have solid color.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-lowspeedzonesall">lowSpeedZonesAll</a></span> <span class="signature">→ String</span>  
All low speed zones are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-publictransitall">publicTransitAll</a></span> <span class="signature">→ String</span>  
Line geometry for all available public transit systems is shown; including subway, tram, train, monorail, ferry and more.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-publictransitasia">publicTransitAsia</a></span> <span class="signature">→ String</span>  
Line geometry for selected public transit systems is shown: subway lines in Japan. Only available when Japan map is used.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-roadexitlabelsall">roadExitLabelsAll</a></span> <span class="signature">→ String</span>  
Road exit labels are shown with numbers and names, if available.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-roadexitlabelsnumbersonly">roadExitLabelsNumbersOnly</a></span> <span class="signature">→ String</span>  
Road exit labels are shown with numbers, if available.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-safetycamerasall">safetyCamerasAll</a></span> <span class="signature">→ String</span>  
All types of safety cameras are shown. Includes speed, red light, red light + speed, bus lane, distance and speed section cameras.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-shadowsall">shadowsAll</a></span> <span class="signature">→ String</span>  
Shadows are shown for extruded buildings and landmarks.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-terrain3d">terrain3d</a></span> <span class="signature">→ String</span>  
Topography-shading is shown on 3d terrain.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-terrainhillshade">terrainHillshade</a></span> <span class="signature">→ String</span>  
Topography-shading is shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficflowjapanwithoutfreeflow">trafficFlowJapanWithoutFreeFlow</a></span> <span class="signature">→ String</span>  
Only available when Japan map is used.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficflowwithfreeflow">trafficFlowWithFreeFlow</a></span> <span class="signature">→ String</span>  
Traffic flow shows green lines when there is no traffic congestion.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficflowwithoutfreeflow">trafficFlowWithoutFreeFlow</a></span> <span class="signature">→ String</span>  
Traffic flow does not show green lines when there is no traffic congestion.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficincidentsall">trafficIncidentsAll</a></span> <span class="signature">→ String</span>  
All available traffic incidents are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficlightsall">trafficLightsAll</a></span> <span class="signature">→ String</span>  
All available traffic lights are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-truckpreferredroadsall">truckPreferredRoadsAll</a></span> <span class="signature">→ String</span>  
Display truck preferred roads

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-vehiclerestrictionsactive">vehicleRestrictionsActive</a></span> <span class="signature">→ String</span>  
Inactive time-based restrictions are not shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-vehiclerestrictionsactiveandinactive">vehicleRestrictionsActiveAndInactive</a></span> <span class="signature">→ String</span>  
Both active and inactive time-based restrictions are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-vehiclerestrictionsactiveandinactivedifferentiated">vehicleRestrictionsActiveAndInactiveDifferentiated</a></span> <span class="signature">→ String</span>  
Both active and inactive restrictions are shown, but inactive time-based restrictions are shown as faded.

<div class="features">

<span class="feature">final</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


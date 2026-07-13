---
title: "MapFeatureModes class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapfeaturemodes-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapFeatureModes-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapFeatureModes-class-sidebar.html">

<div>

# <span class="kind-class">MapFeatureModes</span> class

</div>

<div class="section desc markdown">

Holds constants for map feature modes, to be used with <a href="sdk-for-flutter-explore-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a>.

Use <a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-defaultmode">MapFeatureModes.defaultMode</a> to enable a feature with its default mode.

Note: The default mode is defined by the currently loaded map scene configuration and may vary per <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme</a>. The currently active features and modes can be inspected using <a href="sdk-for-flutter-explore-mapview-mapscene-getactivefeatures">MapScene.getActiveFeatures</a> after the scene is loaded.

See <a href="sdk-for-flutter-explore-mapview-mapfeatures-class">MapFeatures</a> for constants representing the feature names.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-mapfeaturemodes">MapFeatureModes</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-ambientocclusionall">ambientOcclusionAll</a></span> <span class="signature">→ String</span>  
Ambient occlusion effect is shown for extruded buildings and landmarks.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-buildingfootprintsall">buildingFootprintsAll</a></span> <span class="signature">→ String</span>  
All building footprints are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-congestionzonesall">congestionZonesAll</a></span> <span class="signature">→ String</span>  
All congestion zones are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-defaultmode">defaultMode</a></span> <span class="signature">→ String</span>  
Enables the default mode of a map feature. Can be used with any map feature.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-environmentalzonesall">environmentalZonesAll</a></span> <span class="signature">→ String</span>  
All environmental zones are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-extrudedbuildingsall">extrudedBuildingsAll</a></span> <span class="signature">→ String</span>  
All extruded buildings are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-lowspeedzonesall">lowSpeedZonesAll</a></span> <span class="signature">→ String</span>  
All low speed zones are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-roadexitlabelsall">roadExitLabelsAll</a></span> <span class="signature">→ String</span>  
Road exit labels are shown with numbers and names, if available.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-roadexitlabelsnumbersonly">roadExitLabelsNumbersOnly</a></span> <span class="signature">→ String</span>  
Road exit labels are shown with numbers, if available.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-shadowsall">shadowsAll</a></span> <span class="signature">→ String</span>  
Shadows are shown for extruded buildings and landmarks.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-trafficflowjapanwithoutfreeflow">trafficFlowJapanWithoutFreeFlow</a></span> <span class="signature">→ String</span>  
Only available when Japan map is used.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-trafficflowwithfreeflow">trafficFlowWithFreeFlow</a></span> <span class="signature">→ String</span>  
Traffic flow shows green lines when there is no traffic congestion.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-trafficflowwithoutfreeflow">trafficFlowWithoutFreeFlow</a></span> <span class="signature">→ String</span>  
Traffic flow does not show green lines when there is no traffic congestion.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-trafficincidentsall">trafficIncidentsAll</a></span> <span class="signature">→ String</span>  
All available traffic incidents are shown.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-trafficlightsall">trafficLightsAll</a></span> <span class="signature">→ String</span>  
All available traffic lights are shown.

<div class="features">

<span class="feature">final</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

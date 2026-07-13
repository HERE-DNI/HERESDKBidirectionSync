---
title: "MapCameraLimits class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameralimits-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraLimits-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCameraLimits-class-sidebar.html">

<div>

# <span class="kind-class">MapCameraLimits</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Controls constraints on map camera parameters.

When constraints are set, they are enforced for current camera state and for all future changes to the camera.

When setting, limits are applied on next rendering loop.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-mapcameralimits">MapCameraLimits</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-bearingrange">bearingRange</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a></span>  
The bearing range within which the camera can be rotated. Gets the currently set bearing range.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-targetarea">targetArea</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>?</span>  
Geographical area to which the camera target is limited. Gets a GeoBox that limits the camera target to a specific geographical area. Absence of a value means that there is no limit.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-tiltrange">tiltRange</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a></span>  
The tilt range that can be applied to the camera. Gets the current tilt range.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-zoomrange">zoomRange</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-mapview-mapmeasurerange-class">MapMeasureRange</a></span>  
The zoom range that can be applied to the camera. Gets the currently set camera zoom range.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-clearbearingranges">clearBearingRanges</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Clears bearing ranges for all zoom values and resets <a href="sdk-for-flutter-explore-mapview-mapcameralimits-bearingrange">MapCameraLimits.bearingRange</a> to default.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-cleartiltranges">clearTiltRanges</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Clears tilt ranges for all zoom values and resets <a href="sdk-for-flutter-explore-mapview-mapcameralimits-tiltrange">MapCameraLimits.tiltRange</a> to default.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-setbearingrangeatzoom">setBearingRangeAtZoom</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setBearingRangeAtZoom-param-zoom" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">zoom</span>, </span><span id="sdk-for-flutter-explore-setBearingRangeAtZoom-param-bearingRange" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a></span> <span class="parameter-name">bearingRange</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the bearing range within which the camera can rotate at a given zoom.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-settiltrangeatzoom">setTiltRangeAtZoom</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setTiltRangeAtZoom-param-zoom" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">zoom</span>, </span><span id="sdk-for-flutter-explore-setTiltRangeAtZoom-param-tiltRange" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a></span> <span class="parameter-name">tiltRange</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets tilt ranges that can be set on the camera at given zoom.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-maxtilt">maxTilt</a></span> <span class="signature">→ double</span>  
Absolute maximum possible value of tilt angle.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-maxzoomlevel">maxZoomLevel</a></span> <span class="signature">→ double</span>  
Absolute maximum possible value of zoom level.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-mintilt">minTilt</a></span> <span class="signature">→ double</span>  
Absolute minimum possible value of tilt angle.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameralimits-minzoomlevel">minZoomLevel</a></span> <span class="signature">→ double</span>  
Absolute minimum possible value of zoom level.

<div class="features">

<span class="feature">final</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "MapCameraAnimationFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameraanimationfactory-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraAnimationFactory-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCameraAnimationFactory-class-sidebar.html">

<div>

# <span class="kind-class">MapCameraAnimationFactory</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Factory for creating MapCameraAnimation objects to change map's camera over time.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-mapcameraanimationfactory">MapCameraAnimationFactory</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-createanimationfromkeyframetrack">createAnimationFromKeyframeTrack</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-createAnimationFromKeyframeTrack-param-track" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span> <span class="parameter-name">track</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> </span>  
Creates a MapCameraAnimation for a movement defined by the supplied `MapCameraAnimationFactory.createAnimationFromKeyframeTrack.track`.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-createanimationfromkeyframetracks">createAnimationFromKeyframeTracks</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-createAnimationFromKeyframeTracks-param-tracks" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span>\></span></span> <span class="parameter-name">tracks</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> </span>  
Creates a MapCameraAnimation for a movement defined by the supplied list of `MapCameraAnimationFactory.createAnimationFromKeyframeTracks.tracks`.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-createanimationfromupdatewitheasing">createAnimationFromUpdateWithEasing</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-createAnimationFromUpdateWithEasing-param-cameraUpdate" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="parameter-name">cameraUpdate</span>, </span><span id="sdk-for-flutter-explore-createAnimationFromUpdateWithEasing-param-duration" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">duration</span>, </span><span id="sdk-for-flutter-explore-createAnimationFromUpdateWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> </span>  
Creates a <a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a> to gradually update the camera properties within a specified duration from its current values to the ones defined in the `MapCameraAnimationFactory.createAnimationFromUpdateWithEasing.cameraUpdate`.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-flyto">flyTo</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-flyTo-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-explore-flyTo-param-bowFactor" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">bowFactor</span>, </span><span id="sdk-for-flutter-explore-flyTo-param-duration" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">duration</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> </span>  
Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-flytowithorientation">flyToWithOrientation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-flyToWithOrientation-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-explore-flyToWithOrientation-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span><span id="sdk-for-flutter-explore-flyToWithOrientation-param-bowFactor" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">bowFactor</span>, </span><span id="sdk-for-flutter-explore-flyToWithOrientation-param-duration" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">duration</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> </span>  
Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-flytowithorientationandzoom">flyToWithOrientationAndZoom</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-flyToWithOrientationAndZoom-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-explore-flyToWithOrientationAndZoom-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span><span id="sdk-for-flutter-explore-flyToWithOrientationAndZoom-param-zoom" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">zoom</span>, </span><span id="sdk-for-flutter-explore-flyToWithOrientationAndZoom-param-bowFactor" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">bowFactor</span>, </span><span id="sdk-for-flutter-explore-flyToWithOrientationAndZoom-param-duration" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">duration</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> </span>  
Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcameraanimationfactory-flytowithzoom">flyToWithZoom</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-flyToWithZoom-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-explore-flyToWithZoom-param-zoom" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">zoom</span>, </span><span id="sdk-for-flutter-explore-flyToWithZoom-param-bowFactor" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">bowFactor</span>, </span><span id="sdk-for-flutter-explore-flyToWithZoom-param-duration" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">duration</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> </span>  
Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

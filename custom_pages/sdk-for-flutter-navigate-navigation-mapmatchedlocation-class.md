---
title: "MapMatchedLocation class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-mapmatchedlocation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMatchedLocation-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/MapMatchedLocation-class-sidebar.html">

<div>

# <span class="kind-class">MapMatchedLocation</span> class

</div>

<div class="section desc markdown">

Describes a map-matched location in the world at a given time.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-mapmatchedlocation">MapMatchedLocation</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span><span id="sdk-for-flutter-navigate-param-bearingInDegrees" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">bearingInDegrees</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-bearingindegrees">bearingInDegrees</a></span> <span class="signature">↔ double?</span>  
The bearing orientation points to the direction of travel, and has the same angle as the street where it is matched to. Therefore, it must not necessarily be the same as the bearing of a location source. Starts at 0 in the geographic north and rotates in a clockwise direction around the compass. It means that for going north it's equal to 0, for northeast it's equal to 45, for east it's equal to 90, and so on. If it cannot be determined, the value is `null`. Otherwise, it is guaranteed to be in the range \<a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-confidence">0, 360).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name">[confidence</a></span> <span class="signature">↔ double</span>  
Confidence level (between 0 and 1) of the matched location. A low confidence value means that the map-matched vehicle location is not reliable and it may not be clear which part of the road the vehicle has taken. This can happen when the accuracy or frequency of the provided location updates is poor. If the confidence level is too small then, for example, overspeed warnings may be also inaccurate.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-coordinates">coordinates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>  
The geographic coordinates of the map-matched location.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-horizontalaccuracyinmeters">horizontalAccuracyInMeters</a></span> <span class="signature">↔ double?</span>  
Horizontal accuracy measure of location. Estimated based on accuracy of input location and confidence of this map-matched location. Currently this value is not being provided by the Navigator.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-isdrivinginthewrongway">isDrivingInTheWrongWay</a></span> <span class="signature">↔ bool</span>  
Determines if the travel direction on a one-way street is against the allowed traffic direction. For two-way streets, this value is always `false`. This feature is supported in tracking mode and when deviating from a route. Note that the travel direction is determined based on the map-matched location.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-segmentoffsetincentimeters">segmentOffsetInCentimeters</a></span> <span class="signature">↔ int</span>  
Offset from start of segment in centimeters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-segmentreference">segmentReference</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a></span>  
Reference to the current segment. The ratio of <a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-segmentoffsetincentimeters">MapMatchedLocation.segmentOffsetInCentimeters</a> to the segment length is between <a href="sdk-for-flutter-navigate-routing-segmentreference-offsetstart">SegmentReference.offsetStart</a> and <a href="sdk-for-flutter-navigate-routing-segmentreference-offsetend">SegmentReference.offsetEnd</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-speedinmeterspersecond">speedInMetersPerSecond</a></span> <span class="signature">↔ double?</span>  
Speed in meters per second.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-timestamp">timestamp</a></span> <span class="signature">↔ DateTime?</span>  
Timestamp of the map matched position.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

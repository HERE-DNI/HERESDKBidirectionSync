---
title: "GeoCoordinates class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-geocoordinates-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/GeoCoordinates-class-sidebar.html">

<div>

# <span class="kind-class">GeoCoordinates</span> class

</div>

<div class="section desc markdown">

Represents geographical coordinates in 3D space.

</div>

<div class="section">

Annotations  
- @<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-geocoordinates-geocoordinates">GeoCoordinates</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-latitude" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">latitude</span>, </span><span id="sdk-for-flutter-navigate-param-longitude" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">longitude</span></span>)</span>  
Constructs a GeoCoordinates from the provided latitude and longitude values.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-geocoordinates-geocoordinates-withaltitude">GeoCoordinates.withAltitude</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withAltitude-param-latitude" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">latitude</span>, </span><span id="sdk-for-flutter-navigate-withAltitude-param-longitude" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">longitude</span>, </span><span id="sdk-for-flutter-navigate-withAltitude-param-altitude" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">altitude</span></span>)</span>  
Constructs a GeoCoordinates from the provided latitude, longitude and altitude values.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-geocoordinates-altitude">altitude</a></span> <span class="signature">→ double?</span>  
Optional altitude in meters. By convention, on iOS devices, altitude is set as meters relative to the mean sea level. On Android devices, altitude is set as meters relative to the WGS 84 reference ellipsoid.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-geocoordinates-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-geocoordinates-latitude">latitude</a></span> <span class="signature">→ double</span>  
Latitude in degrees.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-geocoordinates-longitude">longitude</a></span> <span class="signature">→ double</span>  
Longitude in degrees.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-geocoordinates-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-geocoordinates-distanceto">distanceTo</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-distanceTo-param-point" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">point</span></span>) <span class="returntype parameter">→ double</span> </span>  
Computes distance (in meters) along the great circle between two coordinates.

<span class="name"><a href="sdk-for-flutter-navigate-core-geocoordinates-interpolate">interpolate</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-interpolate-param-towardCoords" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">towardCoords</span>, </span><span id="sdk-for-flutter-navigate-interpolate-param-factor" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">factor</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> </span>  
Computes the coordinates of the interpolated location along the great circle between the two coordinates.

<span class="name"><a href="sdk-for-flutter-navigate-core-geocoordinates-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-geocoordinates-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-geocoordinates-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-geocoordinates-fromstring">fromString</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-fromString-param-input" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">input</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span> </span>  
Constructs GeoCoordinates from the provided string in specified format.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "GeoPolyline class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-geopolyline-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/GeoPolyline-class-sidebar.html">

<div>

# <span class="kind-class">GeoPolyline</span> class

</div>

<div class="section desc markdown">

A list of geographic coordinates representing the vertices of a polyline.

An instance of this class, initialized with appropriate vertices. Represents a `GeoPolyline` as a series of geographic coordinates.

</div>

<div class="section">

Annotations  
- @<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-geopolyline-geopolyline">GeoPolyline</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-vertices" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">vertices</span></span>)</span>  
Constructs a GeoPolyline from the provided vertices.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-geopolyline-geopolyline-withgeobox">GeoPolyline.withGeoBox</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withGeoBox-param-geoBox" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span> <span class="parameter-name">geoBox</span></span>)</span>  
Constructs an instance of this class from <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-geopolyline-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-geopolyline-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-geopolyline-vertices">vertices</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span>  
The list of vertices representing the polyline.

<div class="features">

<span class="feature">final</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-geopolyline-coordinatesatoffsetinmeters">coordinatesAtOffsetInMeters</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-coordinatesAtOffsetInMeters-param-offsetInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">offsetInMeters</span>, </span><span id="sdk-for-flutter-navigate-coordinatesAtOffsetInMeters-param-direction" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolylinedirection">GeoPolylineDirection</a></span> <span class="parameter-name">direction</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> </span>  
Returns the coordinates at the given distance along the polyline.

<span class="name"><a href="sdk-for-flutter-navigate-core-geopolyline-getnearestindexto">getNearestIndexTo</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getNearestIndexTo-param-point" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">point</span></span>) <span class="returntype parameter">→ int</span> </span>  
Returns the index of the nearest vertex to the given point.

<span class="name"><a href="sdk-for-flutter-navigate-core-geopolyline-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-geopolyline-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-geopolyline-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


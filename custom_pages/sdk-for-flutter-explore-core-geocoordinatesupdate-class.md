---
title: "GeoCoordinatesUpdate class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-geocoordinatesupdate-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoCoordinatesUpdate-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/GeoCoordinatesUpdate-class-sidebar.html">

<div>

# <span class="kind-class">GeoCoordinatesUpdate</span> class

</div>

<div class="section desc markdown">

Represents geographical coordinates in 3D space.

Unlike <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>, its members can be undefined, allowing for APIs that update only the specified parts of geo coordinates.

</div>

<div class="section">

Annotations  
- @<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-geocoordinatesupdate">GeoCoordinatesUpdate</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-latitude" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">latitude</span>, </span><span id="sdk-for-flutter-explore-param-longitude" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">longitude</span></span>)</span>  
Constructs a GeoCoordinatesUpdate from the provided latitude and longitude values.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-geocoordinatesupdate-fromgeocoordinates">GeoCoordinatesUpdate.fromGeoCoordinates</a></span><span class="signature">(<span id="sdk-for-flutter-explore-fromGeoCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span></span>)</span>  
Constructs a GeoCoordinatesUpdate from GeoCoordinates

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-geocoordinatesupdate-withaltitude">GeoCoordinatesUpdate.withAltitude</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withAltitude-param-latitude" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">latitude</span>, </span><span id="sdk-for-flutter-explore-withAltitude-param-longitude" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">longitude</span>, </span><span id="sdk-for-flutter-explore-withAltitude-param-altitude" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">altitude</span></span>)</span>  
Constructs a GeoCoordinatesUpdate from the provided latitude, longitude and alt values.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-altitude">altitude</a></span> <span class="signature">→ double?</span>  
Optional altitude in meters.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-latitude">latitude</a></span> <span class="signature">→ double?</span>  
Optional latitude in degrees.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-longitude">longitude</a></span> <span class="signature">→ double?</span>  
Optional longitude in degrees.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-geocoordinatesupdate-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

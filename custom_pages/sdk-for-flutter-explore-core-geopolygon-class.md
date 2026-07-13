---
title: "GeoPolygon class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-geopolygon-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoPolygon-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/GeoPolygon-class-sidebar.html">

<div>

# <span class="kind-class">GeoPolygon</span> class

</div>

<div class="section desc markdown">

Represents a `GeoPolygon` area as a series of geographic coordinates, and optionally, a list of inner boundaries (also known as holes).

An instance of this class, initialized with appropriate vertices.

</div>

<div class="section">

Annotations  
- @<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-geopolygon-geopolygon">GeoPolygon</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-vertices" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">vertices</span></span>)</span>  
Constructs an instance of this class from the provided vertices.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geopolygon-geopolygon-withgeobox">GeoPolygon.withGeoBox</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withGeoBox-param-geoBox" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="parameter-name">geoBox</span></span>)</span>  
Constructs an instance of this class from <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geopolygon-geopolygon-withgeocircle">GeoPolygon.withGeoCircle</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withGeoCircle-param-geoCircle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a></span> <span class="parameter-name">geoCircle</span></span>)</span>  
Constructs an instance of this class from <a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a>.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geopolygon-geopolygon-withinnerboundaries">GeoPolygon.withInnerBoundaries</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withInnerBoundaries-param-vertices" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">vertices</span>, </span><span id="sdk-for-flutter-explore-withInnerBoundaries-param-innerBoundaries" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span>\></span></span> <span class="parameter-name">innerBoundaries</span></span>)</span>  
Constructs an instance of this class from the provided vertices and inner boundaries (holes).

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-geopolygon-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geopolygon-innerboundaries">innerBoundaries</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span>\></span></span>  
The list of polygon inner boundaries (holes), each defined as a list of geographic coordinates.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geopolygon-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geopolygon-vertices">vertices</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span>  
The list of geographic coordinates representing the outer boundary vertices of polygon.

<div class="features">

<span class="feature">final</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-geopolygon-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geopolygon-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-geopolygon-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

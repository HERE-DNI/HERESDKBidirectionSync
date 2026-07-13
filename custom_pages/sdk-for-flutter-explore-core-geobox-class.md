---
title: "GeoBox class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-geobox-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/GeoBox-class-sidebar.html">

<div>

# <span class="kind-class">GeoBox</span> class

</div>

<div class="section desc markdown">

Represents a bounding rectangle aligned with latitude and longitude.

Geographic area represented by this would be visualised as a rectangle when using a normal cylindrical projection (such as Mercator). The box has a maximum span of 360 degrees in longitude and 180 degrees in latitude direction. The box with equal values in longitude for the corners is considered as a span of 360 degrees. The box is considered empty if the latitude of the `GeoBox.southWestCorner` is larger than the the latitude of the `GeoBox.northEastCorner`.

</div>

<div class="section">

Annotations  
- @<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-geobox">GeoBox</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-southWestCorner" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">southWestCorner</span>, </span><span id="sdk-for-flutter-explore-param-northEastCorner" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">northEastCorner</span></span>)</span>  
Creates a new instance.

<div class="constructor-modifier features">

const

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-northeastcorner">northEastCorner</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>  
North east corner coordinates.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-southwestcorner">southWestCorner</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>  
South west corner coordinates.

<div class="features">

<span class="feature">final</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-containsgeobox">containsGeoBox</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-containsGeoBox-param-geoBox" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="parameter-name">geoBox</span></span>) <span class="returntype parameter">→ bool</span> </span>  
Determines whether the specified `GeoBox` is covered entirely by this `GeoBox`.

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-containsgeocoordinates">containsGeoCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-containsGeoCoordinates-param-geoCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">geoCoordinates</span></span>) <span class="returntype parameter">→ bool</span> </span>  
Determines whether the specified GeoCoordinates is contained within this `GeoBox`.

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-envelope">envelope</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-envelope-param-geoBox" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="parameter-name">geoBox</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> </span>  
Envelopes two `GeoBox` areas by returning the smallest `GeoBox` covering both this GeoBox and the specified `GeoBox`.

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-expandedby">expandedBy</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-expandedBy-param-southMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">southMeters</span>, </span><span id="sdk-for-flutter-explore-expandedBy-param-westMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">westMeters</span>, </span><span id="sdk-for-flutter-explore-expandedBy-param-northMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">northMeters</span>, </span><span id="sdk-for-flutter-explore-expandedBy-param-eastMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">eastMeters</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> </span>  
Creates a `GeoBox` which is expanded by a fixed distance.

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-intersection">intersection</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-intersection-param-geoBox" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="parameter-name">geoBox</span></span>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span>\></span></span> </span>  
Computes the intersection with the passed <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>.

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-intersects">intersects</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-intersects-param-geoBox" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="parameter-name">geoBox</span></span>) <span class="returntype parameter">→ bool</span> </span>  
Determines whether this `GeoBox` intersects with the passed `GeoBox`.

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

## Static Methods

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-containinggeocoordinates">containingGeoCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-containingGeoCoordinates-param-geoCoordinates" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">geoCoordinates</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>?</span> </span>  
Creates a `GeoBox` which encompases all coordinates from the list.

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-envelopegeoboxes">envelopeGeoBoxes</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-envelopeGeoBoxes-param-geoBoxes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span>\></span></span> <span class="parameter-name">geoBoxes</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>?</span> </span>  
Envelopes the list of `GeoBox` areas by returning the smallest `GeoBox` covering all specified `GeoBox` objects.

<span class="name"><a href="sdk-for-flutter-explore-core-geobox-intersectiongeoboxes">intersectionGeoBoxes</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-intersectionGeoBoxes-param-geoBoxes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span>\></span></span> <span class="parameter-name">geoBoxes</span></span>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span>\></span></span> </span>  
Computes intersection of list of <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a> instances.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


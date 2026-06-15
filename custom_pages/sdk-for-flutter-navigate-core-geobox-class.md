---
title: "GeoBox class"
slug: "sdk-for-flutter-navigate-core-geobox-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoBox-class.html -->


<div>
<h1>GeoBox class</h1></div>

<p>Represents a bounding rectangle aligned with latitude and longitude.</p>
<p>Geographic area represented by this would be visualised as a rectangle
when using a normal cylindrical projection (such as Mercator).
The box has a maximum span of 360 degrees in longitude and 180 degrees in latitude direction.
The box with equal values in longitude for the corners is considered as a span of 360 degrees.
The box is considered empty if the latitude of the <code>GeoBox.southWestCorner</code> is larger than the the
latitude of the <code>GeoBox.northEastCorner</code>.</p>


<ul><li>Annotations</li></ul>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-geobox-geobox">GeoBox</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-geobox-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-core-geobox-northeastcorner">northEastCorner</a></li><li><a href="sdk-for-flutter-navigate-core-geobox-runtimetype">runtimeType</a></li><li><a href="sdk-for-flutter-navigate-core-geobox-southwestcorner">southWestCorner</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-geobox-containsgeobox">containsGeoBox</a></li><li><a href="sdk-for-flutter-navigate-core-geobox-containsgeocoordinates">containsGeoCoordinates</a></li><li><a href="sdk-for-flutter-navigate-core-geobox-envelope">envelope</a></li><li><a href="sdk-for-flutter-navigate-core-geobox-expandedby">expandedBy</a></li><li><a href="sdk-for-flutter-navigate-core-geobox-intersection">intersection</a></li><li><a href="sdk-for-flutter-navigate-core-geobox-intersects">intersects</a></li><li><a href="sdk-for-flutter-navigate-core-geobox-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-core-geobox-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-geobox-operator-equals">operator ==</a></li></ul>


<h2>Static Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-geobox-containinggeocoordinates">containingGeoCoordinates</a></li><li><a href="sdk-for-flutter-navigate-core-geobox-envelopegeoboxes">envelopeGeoBoxes</a></li><li><a href="sdk-for-flutter-navigate-core-geobox-intersectiongeoboxes">intersectionGeoBoxes</a></li></ul>

 



</div>
`
}</HTMLBlock>

---
title: "VenueGeometry class - venue.data library - Dart API"
slug: "sdk-for-flutter-navigate-venue.data-venuegeometry-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueGeometry-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.data/venue.data-library-sidebar.html" data-below-sidebar="venue.data/VenueGeometry-class-sidebar.html">

<div>

# <span class="kind-class">VenueGeometry</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents a geometry inside the <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>.

The geometry can be any object inside the level, like a room, a wall or a table. Also the geometry can represent virtual objects, like a team area in an open space.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-venuegeometry">VenueGeometry</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-boundingbox">boundingBox</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span>  
The `GeoBox` of the bounding area of the geometry. Gets a bounding box of the geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-center">center</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>  
The geographic coordinates of the center of the geometry. Gets a center of the geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-geometrytype">geometryType</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuegeometrygeometrytype">VenueGeometryGeometryType</a></span>  
The type of the geometry. Gets a type of the geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-identifier">identifier</a></span> <span class="signature">→ String</span>  
The `id` of the geometry. Gets an id of the geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-internaladdress">internalAddress</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuegeometryinternaladdress-class">VenueGeometryInternalAddress</a>?</span>  
The internal address of the geometry. Gets an internal address of the geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-labelname">labelName</a></span> <span class="signature">→ String</span>  
The label name of the geometry. Gets a label name of the geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-labelstyle">labelStyle</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-style-venuelabelstyle-class">VenueLabelStyle</a>?</span>  
The label style of the geometry. Gets a label style of the geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-level">level</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a></span>  
The parent level of the geometry. Gets a parent level of the geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-levelid">levelID</a></span> <span class="signature">→ String</span>  
The level ID of geometry. Gets level ID of the geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-lookuptype">lookupType</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuegeometrylookuptype">VenueGeometryLookupType</a></span>  
The lookup type of the geometry. Gets a lookup type of the geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-name">name</a></span> <span class="signature">→ String</span>  
The name of the geometry. If no name has been set, returns a label name. Gets a name of the geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-parentgeometry">parentGeometry</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a></span>  
The parent geometry. Defaults to `null`, if the geometry represents a base shape. Gets a parent geometry on which the current geometry is located.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-properties">properties</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuegeometrystringtopropertymap">VenueGeometryStringToPropertyMap</a></span>  
The properties of the geometry. Gets the properties of the geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-style">style</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-style-venuegeometrystyle-class">VenueGeometryStyle</a>?</span>  
The style of the geometry. Gets a style of the geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuegeometry-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

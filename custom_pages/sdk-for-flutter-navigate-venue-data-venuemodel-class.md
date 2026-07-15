---
title: "VenueModel class - venue.data library - Dart API"
slug: "sdk-for-flutter-navigate-venue-data-venuemodel-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.data/venue.data-library-sidebar.html" data-below-sidebar="venue.data/VenueModel-class-sidebar.html">

<div>

# <span class="kind-class">VenueModel</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents a building or a complex of buildings, like airports or universities.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-venuemodel">VenueModel</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-boundingbox">boundingBox</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span>  
The `GeoBox` of the bounding area of the venue model. Gets a bounding box of the venue model.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-center">center</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>  
The geographic coordinates of the center of the venue model. Gets a center of the venue model.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-drawings">drawings</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuemodeldrawingarray">VenueModelDrawingArray</a></span>  
The array of the Drawing objects. Gets the drawings of the venue model.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-geometries">geometries</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuemodelgeometryarray">VenueModelGeometryArray</a></span>  
The list of geometries of the venue or an empty list if no geometry present for venue. Gets a list of geometries of the venue.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-geometriesbyiconnames">geometriesByIconNames</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuemodelstringtogeometryarraymap">VenueModelStringToGeometryArrayMap</a></span>  
The map from the icon names to the geometries in the drawing. Gets geometries mapped by icon names.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-geometriesbyname">geometriesByName</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuemodelgeometryarray">VenueModelGeometryArray</a></span>  
The geometries ordered by the name in an ascending order. Gets the geometries ordered by the name in an ascending order.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-id">id</a></span> <span class="signature">→ int</span>  
The `id` of the venue model. Gets an `id` of the venue model.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-identifier">identifier</a></span> <span class="signature">→ String</span>  
The `id` of the venue model. Gets an `id` of the venue model.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-language">language</a></span> <span class="signature">→ String</span>  
The language of the venue model. Gets a language of the venue model.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-properties">properties</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuemodelstringtopropertymap">VenueModelStringToPropertyMap</a></span>  
The properties of the venue model. Gets properties of the venue model.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-topologies">topologies</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuemodeltopologyarray">VenueModelTopologyArray</a></span>  
The list of topologies of the drawing. Gets a list of topologies of the drawing.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-filtergeometry">filterGeometry</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-filterGeometry-param-filter" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">filter</span>, </span><span id="sdk-for-flutter-navigate-filterGeometry-param-filterType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuegeometryfiltertype">VenueGeometryFilterType</a></span> <span class="parameter-name">filterType</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuemodelgeometryarray">VenueModelGeometryArray</a></span> </span>  
Gets the filtered geometries in an ascending order.

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-getdrawing">getDrawing</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getDrawing-param-drawingId" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">drawingId</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a></span> </span>  
Gets a drawing for a given drawing id.

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-getdrawingbyidentifier">getDrawingByIdentifier</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getDrawingByIdentifier-param-drawingId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">drawingId</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a></span> </span>  
Gets a drawing for a given drawing id.

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "VenueDrawing class - venue.data library - Dart API"
slug: "sdk-for-flutter-navigate-venue-data-venuedrawing-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.data/venue.data-library-sidebar.html" data-below-sidebar="venue.data/VenueDrawing-class-sidebar.html">

<div>

# <span class="kind-class">VenueDrawing</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents a drawing inside the <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a>.

The drawing can be a separate building in a complex of buildings, or show a different view of a venue. For example, in an airport, one drawing can be used as an overview of all buildings in this venue, while other drawings contains details for each terminal in this airport.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-venuedrawing">VenueDrawing</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-boundingbox">boundingBox</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span>  
The `GeoBox` of the bounding area of the drawing. This is used to check if at certain zoom level and inside view this GeoBox belongs, then need to render. Gets a bounding box of the drawing.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-center">center</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>  
The Geographic coordinates of the center of the drawing. It can be used to get center coordinates of drawing. Gets a center of the drawing.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-geometriesbyiconnames">geometriesByIconNames</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuedrawingstringtogeometryarraymap">VenueDrawingStringToGeometryArrayMap</a></span>  
The map from the icon names to the geometries in the drawing. This can be used to search the geometries by icon names. Gets geometries mapped by icon names.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-geometriesbyname">geometriesByName</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuedrawinggeometryarray">VenueDrawingGeometryArray</a></span>  
The geometries ordered by the name. This can be used to search geometries by name. Gets geometries ordered by a name in an ascending order.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-identifier">identifier</a></span> <span class="signature">→ String</span>  
The `id` of the drawing. This describes the identifier for drawing. Gets an id of the drawing.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-isisroot">isIsRoot</a></span> <span class="signature">→ bool</span>  
`True` if this is the root drawing and `false` otherwise. This can be used to check if this is top level drawing in venue. Checks if this is a root drawing of the venue.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-levels">levels</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuedrawinglevelarray">VenueDrawingLevelArray</a></span>  
The array with Level objects. This describes for which all level this drawing belongs. Gets levels of the drawing.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-properties">properties</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuedrawingstringtopropertymap">VenueDrawingStringToPropertyMap</a></span>  
The key-value pairs of properties. This can be used to get different properties like name belonging to Drawing. Gets properties of the drawing.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-topologies">topologies</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuedrawingtopologyarray">VenueDrawingTopologyArray</a></span>  
The list of topologies of the drawing. This can be used to check for which all topologies are realted to Drawing. Gets a list of topologies of the drawing.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-venuemodel">venueModel</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a></span>  
The parent venue model. It can be used to get the <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> where this Drawing belong. Gets a parent venue model.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-filtergeometry">filterGeometry</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-filterGeometry-param-filter" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">filter</span>, </span><span id="sdk-for-flutter-navigate-filterGeometry-param-filterType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuegeometryfiltertype">VenueGeometryFilterType</a></span> <span class="parameter-name">filterType</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuedrawinggeometryarray">VenueDrawingGeometryArray</a></span> </span>  
Gets filtered geometries in an ascending order.

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-getgeometrybyaddress">getGeometryByAddress</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getGeometryByAddress-param-geometryAddress" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">geometryAddress</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a>?</span> </span>  
Gets a geometry by the <a href="sdk-for-flutter-navigate-venue-data-venuegeometryinternaladdress-class">VenueGeometryInternalAddress</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-getgeometrybyidentifier">getGeometryByIdentifier</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getGeometryByIdentifier-param-geometryId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">geometryId</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a>?</span> </span>  
Gets a geometry by an id.

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


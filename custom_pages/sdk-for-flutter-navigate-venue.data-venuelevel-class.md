---
title: "VenueLevel class - venue.data library - Dart API"
slug: "sdk-for-flutter-navigate-venue.data-venuelevel-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueLevel-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.data/venue.data-library-sidebar.html" data-below-sidebar="venue.data/VenueLevel-class-sidebar.html">

<div>

# <span class="kind-class">VenueLevel</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents one level of a building or a complex of buildings inside the <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-venuelevel">VenueLevel</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-boundingbox">boundingBox</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span>  
The `GeoBox` of the bounding area. Gets a bounding box of the level.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-center">center</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>  
The geographic coordinates of the center of the level. Gets a center of the level.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-crosswalks">crosswalks</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuelevelcrosswalkarray">VenueLevelCrosswalkArray</a></span>  
The list of crosswalks of the level. Gets a list of crosswalks of the level.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-drawing">drawing</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a></span>  
The parent drawing of the level. Gets a parent drawing of the level.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-drawingid">drawingID</a></span> <span class="signature">→ String</span>  
The drawing ID of level. Gets drawing ID of the level.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-geometries">geometries</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuelevelgeometryarray">VenueLevelGeometryArray</a></span>  
The list of geometries of the level. Gets a list of geometries of the level.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-geometriesbyiconnames">geometriesByIconNames</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuelevelstringtogeometryarraymap">VenueLevelStringToGeometryArrayMap</a></span>  
The map from the icon names to the geometries in the drawing. Gets the geometries mapped by icon names.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-geometriesbyname">geometriesByName</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuelevelgeometryarray">VenueLevelGeometryArray</a></span>  
The geometries ordered by the name in an ascending order. Gets the geometries ordered by a name in an ascending order.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-identifier">identifier</a></span> <span class="signature">→ String</span>  
The `id` of the level. Gets an id of the level.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-isismainlevel">isIsMainLevel</a></span> <span class="signature">→ bool</span>  
`True` if this is the main level and `false` otherwise. Indicates if this level is the main level.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-name">name</a></span> <span class="signature">→ String</span>  
The name property of the level. If the 'name' property is missing in the properties, the string will be empty. Gets a 'name' property of the level from the level properties.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-properties">properties</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venuelevelstringtopropertymap">VenueLevelStringToPropertyMap</a></span>  
The properties of the level. Gets properties of the level.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-shortname">shortName</a></span> <span class="signature">→ String</span>  
The short name of the level. Gets a short name of the level.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-topologies">topologies</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-data-venueleveltopologyarray">VenueLevelTopologyArray</a></span>  
The list of topologies of the level. Gets a list of topologies of the level.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-zindex">zIndex</a></span> <span class="signature">→ int</span>  
The Z index of the level, an order in the z direction (altitude). Z index 0 represents a ground level, negative values represent underground levels, positive values - levels above ground. Gets an order in the z direction (altitude).

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-filtergeometry">filterGeometry</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-filterGeometry-param-filter" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">filter</span>, </span><span id="sdk-for-flutter-navigate-filterGeometry-param-filterType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuegeometryfiltertype">VenueGeometryFilterType</a></span> <span class="parameter-name">filterType</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuelevelgeometryarray">VenueLevelGeometryArray</a></span> </span>  
Gets the filtered geometries in an ascending order.

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-getcrosswalkbycoordinates">getCrosswalkByCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getCrosswalkByCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-crosswalk-class">Crosswalk</a>?</span> </span>  
Gets a crosswalk by coordinates.

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-getgeometriesbycoordinates">getGeometriesByCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getGeometriesByCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuelevelgeometryarray">VenueLevelGeometryArray</a></span> </span>  
Gets geometries by coordinates.

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-getgeometrybyaddress">getGeometryByAddress</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getGeometryByAddress-param-geometryAddress" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">geometryAddress</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a>?</span> </span>  
Gets a geometry by the <a href="sdk-for-flutter-navigate-venue-data-venuegeometryinternaladdress-class">VenueGeometryInternalAddress</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-getgeometrybycoordinates">getGeometryByCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getGeometryByCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a>?</span> </span>  
Gets a geometry by coordinates.

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-getgeometrybyidentifier">getGeometryByIdentifier</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getGeometryByIdentifier-param-geometryId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">geometryId</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a>?</span> </span>  
Gets a geometry by an id.

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-gettopologybycoordinates">getTopologyByCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getTopologyByCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuetopology-class">VenueTopology</a>?</span> </span>  
Gets a topology by coordinates.

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

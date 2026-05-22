---
title: "Untitled"
slug: "sdk-for-flutter-navigate-venue-data-venuelevel-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueLevel-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-data-venue-data-library</li>
<li class="self-crumb">VenueLevel class</li>
</ol>
<div class="self-name">VenueLevel</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="venue.data/venue.data-library-sidebar.html" data-below-sidebar="venue.data/VenueLevel-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VenueLevel class abstract</h1></div>
<section class="desc markdown">
<p>Represents one level of a building or a complex of buildings inside the /sdk-for-flutter-navigate-venue-data-venuedrawing-class.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VenueLevel">
/sdk-for-flutter-navigate-venue-data-venuelevel-venuelevel()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="boundingBox">
/sdk-for-flutter-navigate-venue-data-venuelevel-boundingbox
→ /sdk-for-flutter-navigate-core-geobox-class
</dt>
<dd>
  The <code>GeoBox</code> of the bounding area.
Gets a bounding box of the level.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="center">
/sdk-for-flutter-navigate-venue-data-venuelevel-center
→ /sdk-for-flutter-navigate-core-geocoordinates-class
</dt>
<dd>
  The geographic coordinates of the center of the level.
Gets a center of the level.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="crosswalks">
/sdk-for-flutter-navigate-venue-data-venuelevel-crosswalks
→ /sdk-for-flutter-navigate-venue-data-venuelevelcrosswalkarray
</dt>
<dd>
  The list of crosswalks of the level.
Gets a list of crosswalks of the level.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="drawing">
/sdk-for-flutter-navigate-venue-data-venuelevel-drawing
→ /sdk-for-flutter-navigate-venue-data-venuedrawing-class
</dt>
<dd>
  The parent drawing of the level.
Gets a parent drawing of the level.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="drawingID">
/sdk-for-flutter-navigate-venue-data-venuelevel-drawingid
→ String
</dt>
<dd>
  The drawing ID of level.
Gets drawing ID of the level.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geometries">
/sdk-for-flutter-navigate-venue-data-venuelevel-geometries
→ /sdk-for-flutter-navigate-venue-data-venuelevelgeometryarray
</dt>
<dd>
  The list of geometries of the level.
Gets a list of geometries of the level.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geometriesByIconNames">
/sdk-for-flutter-navigate-venue-data-venuelevel-geometriesbyiconnames
→ /sdk-for-flutter-navigate-venue-data-venuelevelstringtogeometryarraymap
</dt>
<dd>
  The map from the icon names to the geometries in the drawing.
Gets the geometries mapped by icon names.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geometriesByName">
/sdk-for-flutter-navigate-venue-data-venuelevel-geometriesbyname
→ /sdk-for-flutter-navigate-venue-data-venuelevelgeometryarray
</dt>
<dd>
  The geometries ordered by the name in an ascending order.
Gets the geometries ordered by a name in an ascending order.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-venue-data-venuelevel-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="identifier">
/sdk-for-flutter-navigate-venue-data-venuelevel-identifier
→ String
</dt>
<dd>
  The <code>id</code> of the level.
Gets an id of the level.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isIsMainLevel">
/sdk-for-flutter-navigate-venue-data-venuelevel-isismainlevel
→ bool
</dt>
<dd>
<code>True</code> if this is the main level and <code>false</code> otherwise.
Indicates if this level is the main level.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="name">
/sdk-for-flutter-navigate-venue-data-venuelevel-name
→ String
</dt>
<dd>
  The name property of the level.
If the 'name' property is missing in the properties, the string will be empty.
Gets a 'name' property of the level from the level properties.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="properties">
/sdk-for-flutter-navigate-venue-data-venuelevel-properties
→ /sdk-for-flutter-navigate-venue-data-venuelevelstringtopropertymap
</dt>
<dd>
  The properties of the level.
Gets properties of the level.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-venue-data-venuelevel-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="shortName">
/sdk-for-flutter-navigate-venue-data-venuelevel-shortname
→ String
</dt>
<dd>
  The short name of the level.
Gets a short name of the level.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="topologies">
/sdk-for-flutter-navigate-venue-data-venuelevel-topologies
→ /sdk-for-flutter-navigate-venue-data-venueleveltopologyarray
</dt>
<dd>
  The list of topologies of the level.
Gets a list of topologies of the level.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="zIndex">
/sdk-for-flutter-navigate-venue-data-venuelevel-zindex
→ int
</dt>
<dd>
  The Z index of the level, an order in the z direction (altitude).
Z index 0 represents
a ground level, negative values represent underground levels,
positive values - levels above ground.
Gets an order in the z direction (altitude).
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="filterGeometry">
/sdk-for-flutter-navigate-venue-data-venuelevel-filtergeometry(<wbr/>String filter, /sdk-for-flutter-navigate-venue-data-venuegeometryfiltertype filterType)
    → /sdk-for-flutter-navigate-venue-data-venuelevelgeometryarray

</dt>
<dd>
  Gets the filtered geometries in an ascending order.
  

</dd>
<dt class="callable" id="getCrosswalkByCoordinates">
/sdk-for-flutter-navigate-venue-data-venuelevel-getcrosswalkbycoordinates(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates)
    → /sdk-for-flutter-navigate-venue-data-crosswalk-class?

</dt>
<dd>
  Gets a crosswalk by coordinates.
  

</dd>
<dt class="callable" id="getGeometriesByCoordinates">
/sdk-for-flutter-navigate-venue-data-venuelevel-getgeometriesbycoordinates(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates)
    → /sdk-for-flutter-navigate-venue-data-venuelevelgeometryarray

</dt>
<dd>
  Gets geometries by coordinates.
  

</dd>
<dt class="callable" id="getGeometryByAddress">
/sdk-for-flutter-navigate-venue-data-venuelevel-getgeometrybyaddress(<wbr/>String geometryAddress)
    → /sdk-for-flutter-navigate-venue-data-venuegeometry-class?

</dt>
<dd>
  Gets a geometry by the /sdk-for-flutter-navigate-venue-data-venuegeometryinternaladdress-class.
  

</dd>
<dt class="callable" id="getGeometryByCoordinates">
/sdk-for-flutter-navigate-venue-data-venuelevel-getgeometrybycoordinates(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates)
    → /sdk-for-flutter-navigate-venue-data-venuegeometry-class?

</dt>
<dd>
  Gets a geometry by coordinates.
  

</dd>
<dt class="callable" id="getGeometryByIdentifier">
/sdk-for-flutter-navigate-venue-data-venuelevel-getgeometrybyidentifier(<wbr/>String geometryId)
    → /sdk-for-flutter-navigate-venue-data-venuegeometry-class?

</dt>
<dd>
  Gets a geometry by an id.
  

</dd>
<dt class="callable" id="getTopologyByCoordinates">
/sdk-for-flutter-navigate-venue-data-venuelevel-gettopologybycoordinates(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates)
    → /sdk-for-flutter-navigate-venue-data-venuetopology-class?

</dt>
<dd>
  Gets a topology by coordinates.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-venue-data-venuelevel-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-venue-data-venuelevel-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-venue-data-venuelevel-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-data-venue-data-library</li>
<li class="self-crumb">VenueLevel class</li>
</ol>
<h5>venue.data library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>

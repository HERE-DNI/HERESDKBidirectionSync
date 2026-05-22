---
title: "Untitled"
slug: "sdk-for-flutter-navigate-venue-data-venuemodel-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueModel-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-data-venue-data-library</li>
<li class="self-crumb">VenueModel class</li>
</ol>
<div class="self-name">VenueModel</div>
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
<div class="main-content" data-above-sidebar="venue.data/venue.data-library-sidebar.html" data-below-sidebar="venue.data/VenueModel-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VenueModel class abstract</h1></div>
<section class="desc markdown">
<p>Represents a building or a complex of buildings, like airports or universities.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VenueModel">
/sdk-for-flutter-navigate-venue-data-venuemodel-venuemodel()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="boundingBox">
/sdk-for-flutter-navigate-venue-data-venuemodel-boundingbox
→ /sdk-for-flutter-navigate-core-geobox-class
</dt>
<dd>
  The <code>GeoBox</code> of the bounding area of the venue model.
Gets a bounding box of the venue model.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="center">
/sdk-for-flutter-navigate-venue-data-venuemodel-center
→ /sdk-for-flutter-navigate-core-geocoordinates-class
</dt>
<dd>
  The geographic coordinates of the center of the venue model.
Gets a center of the venue model.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="drawings">
/sdk-for-flutter-navigate-venue-data-venuemodel-drawings
→ /sdk-for-flutter-navigate-venue-data-venuemodeldrawingarray
</dt>
<dd>
  The array of the Drawing objects.
Gets the drawings of the venue model.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geometries">
/sdk-for-flutter-navigate-venue-data-venuemodel-geometries
→ /sdk-for-flutter-navigate-venue-data-venuemodelgeometryarray
</dt>
<dd>
  The list of geometries of the venue or an empty list if no geometry present for venue.
Gets a list of geometries of the venue.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geometriesByIconNames">
/sdk-for-flutter-navigate-venue-data-venuemodel-geometriesbyiconnames
→ /sdk-for-flutter-navigate-venue-data-venuemodelstringtogeometryarraymap
</dt>
<dd>
  The map from the icon names to the geometries in the drawing.
Gets geometries mapped by icon names.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geometriesByName">
/sdk-for-flutter-navigate-venue-data-venuemodel-geometriesbyname
→ /sdk-for-flutter-navigate-venue-data-venuemodelgeometryarray
</dt>
<dd>
  The geometries ordered by the name in an ascending order.
Gets the geometries ordered by the name in an ascending order.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-venue-data-venuemodel-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-venue-data-venuemodel-id
→ int
</dt>
<dd>
  The <code>id</code> of the venue model.
Gets an <code>id</code> of the venue model.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="identifier">
/sdk-for-flutter-navigate-venue-data-venuemodel-identifier
→ String
</dt>
<dd>
  The <code>id</code> of the venue model.
Gets an <code>id</code> of the venue model.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="language">
/sdk-for-flutter-navigate-venue-data-venuemodel-language
→ String
</dt>
<dd>
  The language of the venue model.
Gets a language of the venue model.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="properties">
/sdk-for-flutter-navigate-venue-data-venuemodel-properties
→ /sdk-for-flutter-navigate-venue-data-venuemodelstringtopropertymap
</dt>
<dd>
  The properties of the venue model.
Gets properties of the venue model.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-venue-data-venuemodel-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="topologies">
/sdk-for-flutter-navigate-venue-data-venuemodel-topologies
→ /sdk-for-flutter-navigate-venue-data-venuemodeltopologyarray
</dt>
<dd>
  The list of topologies of the drawing.
Gets a list of topologies of the drawing.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="filterGeometry">
/sdk-for-flutter-navigate-venue-data-venuemodel-filtergeometry(<wbr/>String filter, /sdk-for-flutter-navigate-venue-data-venuegeometryfiltertype filterType)
    → /sdk-for-flutter-navigate-venue-data-venuemodelgeometryarray

</dt>
<dd>
  Gets the filtered geometries in an ascending order.
  

</dd>
<dt class="callable" id="getDrawing">
/sdk-for-flutter-navigate-venue-data-venuemodel-getdrawing(<wbr/>int drawingId)
    → /sdk-for-flutter-navigate-venue-data-venuedrawing-class

</dt>
<dd>
  Gets a drawing for a given drawing id.
  

</dd>
<dt class="callable" id="getDrawingByIdentifier">
/sdk-for-flutter-navigate-venue-data-venuemodel-getdrawingbyidentifier(<wbr/>String drawingId)
    → /sdk-for-flutter-navigate-venue-data-venuedrawing-class

</dt>
<dd>
  Gets a drawing for a given drawing id.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-venue-data-venuemodel-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-venue-data-venuemodel-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-venue-data-venuemodel-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">VenueModel class</li>
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

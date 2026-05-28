---
title: "VenueDrawing class abstract"
slug: "sdk-for-flutter-navigate-venue-data-venuedrawing-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueDrawing-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="venue.data/VenueDrawing-class.html#constructors">Constructors</a></li>
<li><a href="venue.data/VenueDrawing/VenueDrawing.html">VenueDrawing</a></li>
<li class="section-title">
<a href="venue.data/VenueDrawing-class.html#instance-properties">Properties</a>
</li>
<li><a href="venue.data/VenueDrawing/boundingBox.html">boundingBox</a></li>
<li><a href="venue.data/VenueDrawing/center.html">center</a></li>
<li><a href="venue.data/VenueDrawing/geometriesByIconNames.html">geometriesByIconNames</a></li>
<li><a href="venue.data/VenueDrawing/geometriesByName.html">geometriesByName</a></li>
<li class="inherited"><a href="venue.data/VenueDrawing/hashCode.html">hashCode</a></li>
<li><a href="venue.data/VenueDrawing/identifier.html">identifier</a></li>
<li><a href="venue.data/VenueDrawing/isIsRoot.html">isIsRoot</a></li>
<li><a href="venue.data/VenueDrawing/levels.html">levels</a></li>
<li><a href="venue.data/VenueDrawing/properties.html">properties</a></li>
<li class="inherited"><a href="venue.data/VenueDrawing/runtimeType.html">runtimeType</a></li>
<li><a href="venue.data/VenueDrawing/topologies.html">topologies</a></li>
<li><a href="venue.data/VenueDrawing/venueModel.html">venueModel</a></li>
<li class="section-title"><a href="venue.data/VenueDrawing-class.html#instance-methods">Methods</a></li>
<li><a href="venue.data/VenueDrawing/filterGeometry.html">filterGeometry</a></li>
<li><a href="venue.data/VenueDrawing/getGeometryByAddress.html">getGeometryByAddress</a></li>
<li><a href="venue.data/VenueDrawing/getGeometryByIdentifier.html">getGeometryByIdentifier</a></li>
<li class="inherited"><a href="venue.data/VenueDrawing/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="venue.data/VenueDrawing/toString.html">toString</a></li>
<li class="section-title inherited"><a href="venue.data/VenueDrawing-class.html#operators">Operators</a></li>
<li class="inherited"><a href="venue.data/VenueDrawing/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-data-venue-data-library</li>
<li class="self-crumb">VenueDrawing class</li>
</ol>
<div class="self-name">VenueDrawing</div>
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
<div class="main-content" data-above-sidebar="venue.data/venue.data-library-sidebar.html" data-below-sidebar="venue.data/VenueDrawing-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VenueDrawing class abstract</h1></div>
<section class="desc markdown">
<p>Represents a drawing inside the /sdk-for-flutter-navigate-venue-data-venuemodel-class.</p>
<p>The drawing can be
a separate building in a complex of buildings, or show a different
view of a venue. For example, in an airport, one drawing can be used
as an overview of all buildings in this venue, while other drawings
contains details for each terminal in this airport.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VenueDrawing">
/sdk-for-flutter-navigate-venue-data-venuedrawing-venuedrawing()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="boundingBox">
/sdk-for-flutter-navigate-venue-data-venuedrawing-boundingbox
→ /sdk-for-flutter-navigate-core-geobox-class
</dt>
<dd>
  The <code>GeoBox</code> of the bounding area of the drawing.
This is used to check if at certain zoom level
and inside view this GeoBox belongs, then need to render.
Gets a bounding box of the drawing.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="center">
/sdk-for-flutter-navigate-venue-data-venuedrawing-center
→ /sdk-for-flutter-navigate-core-geocoordinates-class
</dt>
<dd>
  The Geographic coordinates of the center of the drawing.
It can be used to get center coordinates of drawing.
Gets a center of the drawing.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geometriesByIconNames">
/sdk-for-flutter-navigate-venue-data-venuedrawing-geometriesbyiconnames
→ /sdk-for-flutter-navigate-venue-data-venuedrawingstringtogeometryarraymap
</dt>
<dd>
  The map from the icon names to the geometries in the drawing.
This can be used to search the geometries by icon names.
Gets geometries mapped by icon names.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geometriesByName">
/sdk-for-flutter-navigate-venue-data-venuedrawing-geometriesbyname
→ /sdk-for-flutter-navigate-venue-data-venuedrawinggeometryarray
</dt>
<dd>
  The geometries ordered by the name.
This can be used to search geometries by name.
Gets geometries ordered by a name in an ascending order.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-venue-data-venuedrawing-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="identifier">
/sdk-for-flutter-navigate-venue-data-venuedrawing-identifier
→ String
</dt>
<dd>
  The <code>id</code> of the drawing.
This describes the identifier for drawing.
Gets an id of the drawing.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isIsRoot">
/sdk-for-flutter-navigate-venue-data-venuedrawing-isisroot
→ bool
</dt>
<dd>
<code>True</code> if this is the root drawing and <code>false</code> otherwise.
This can be used to check if this is top level
drawing in venue.
Checks if this is a root drawing of the venue.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="levels">
/sdk-for-flutter-navigate-venue-data-venuedrawing-levels
→ /sdk-for-flutter-navigate-venue-data-venuedrawinglevelarray
</dt>
<dd>
  The array with Level objects.
This describes for which all level this
drawing belongs.
Gets levels of the drawing.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="properties">
/sdk-for-flutter-navigate-venue-data-venuedrawing-properties
→ /sdk-for-flutter-navigate-venue-data-venuedrawingstringtopropertymap
</dt>
<dd>
  The key-value pairs of properties.
This can be used to get different properties
like name belonging to Drawing.
Gets properties of the drawing.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-venue-data-venuedrawing-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="topologies">
/sdk-for-flutter-navigate-venue-data-venuedrawing-topologies
→ /sdk-for-flutter-navigate-venue-data-venuedrawingtopologyarray
</dt>
<dd>
  The list of topologies of the drawing.
This can be used to check for which
all topologies are realted to Drawing.
Gets a list of topologies of the drawing.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="venueModel">
/sdk-for-flutter-navigate-venue-data-venuedrawing-venuemodel
→ /sdk-for-flutter-navigate-venue-data-venuemodel-class
</dt>
<dd>
  The parent venue model.
It can be used to get the /sdk-for-flutter-navigate-venue-data-venuemodel-class
where this Drawing belong.
Gets a parent venue model.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="filterGeometry">
/sdk-for-flutter-navigate-venue-data-venuedrawing-filtergeometry(<wbr/>String filter, /sdk-for-flutter-navigate-venue-data-venuegeometryfiltertype filterType)
    → /sdk-for-flutter-navigate-venue-data-venuedrawinggeometryarray

</dt>
<dd>
  Gets filtered geometries in an ascending order.
  

</dd>
<dt class="callable" id="getGeometryByAddress">
/sdk-for-flutter-navigate-venue-data-venuedrawing-getgeometrybyaddress(<wbr/>String geometryAddress)
    → /sdk-for-flutter-navigate-venue-data-venuegeometry-class?

</dt>
<dd>
  Gets a geometry by the /sdk-for-flutter-navigate-venue-data-venuegeometryinternaladdress-class.
  

</dd>
<dt class="callable" id="getGeometryByIdentifier">
/sdk-for-flutter-navigate-venue-data-venuedrawing-getgeometrybyidentifier(<wbr/>String geometryId)
    → /sdk-for-flutter-navigate-venue-data-venuegeometry-class?

</dt>
<dd>
  Gets a geometry by an id.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-venue-data-venuedrawing-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-venue-data-venuedrawing-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-venue-data-venuedrawing-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">VenueDrawing class</li>
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
</div></div>
</div>
`
}</HTMLBlock>

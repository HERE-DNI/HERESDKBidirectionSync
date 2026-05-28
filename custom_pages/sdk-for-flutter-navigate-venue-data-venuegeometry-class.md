---
title: "VenueGeometry class abstract"
slug: "sdk-for-flutter-navigate-venue-data-venuegeometry-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueGeometry-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="venue.data/VenueGeometry-class.html#constructors">Constructors</a></li>
<li><a href="venue.data/VenueGeometry/VenueGeometry.html">VenueGeometry</a></li>
<li class="section-title">
<a href="venue.data/VenueGeometry-class.html#instance-properties">Properties</a>
</li>
<li><a href="venue.data/VenueGeometry/boundingBox.html">boundingBox</a></li>
<li><a href="venue.data/VenueGeometry/center.html">center</a></li>
<li><a href="venue.data/VenueGeometry/geometryType.html">geometryType</a></li>
<li class="inherited"><a href="venue.data/VenueGeometry/hashCode.html">hashCode</a></li>
<li><a href="venue.data/VenueGeometry/identifier.html">identifier</a></li>
<li><a href="venue.data/VenueGeometry/internalAddress.html">internalAddress</a></li>
<li><a href="venue.data/VenueGeometry/labelName.html">labelName</a></li>
<li><a href="venue.data/VenueGeometry/labelStyle.html">labelStyle</a></li>
<li><a href="venue.data/VenueGeometry/level.html">level</a></li>
<li><a href="venue.data/VenueGeometry/levelID.html">levelID</a></li>
<li><a href="venue.data/VenueGeometry/lookupType.html">lookupType</a></li>
<li><a href="venue.data/VenueGeometry/name.html">name</a></li>
<li><a href="venue.data/VenueGeometry/parentGeometry.html">parentGeometry</a></li>
<li><a href="venue.data/VenueGeometry/properties.html">properties</a></li>
<li class="inherited"><a href="venue.data/VenueGeometry/runtimeType.html">runtimeType</a></li>
<li><a href="venue.data/VenueGeometry/style.html">style</a></li>
<li class="section-title inherited"><a href="venue.data/VenueGeometry-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="venue.data/VenueGeometry/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="venue.data/VenueGeometry/toString.html">toString</a></li>
<li class="section-title inherited"><a href="venue.data/VenueGeometry-class.html#operators">Operators</a></li>
<li class="inherited"><a href="venue.data/VenueGeometry/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-data-venue-data-library</li>
<li class="self-crumb">VenueGeometry class</li>
</ol>
<div class="self-name">VenueGeometry</div>
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
<div class="main-content" data-above-sidebar="venue.data/venue.data-library-sidebar.html" data-below-sidebar="venue.data/VenueGeometry-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VenueGeometry class abstract</h1></div>
<section class="desc markdown">
<p>Represents a geometry inside the /sdk-for-flutter-navigate-venue-data-venuelevel-class.</p>
<p>The geometry can be any object
inside the level, like a room, a wall or a table. Also the geometry can represent virtual
objects, like a team area in an open space.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VenueGeometry">
/sdk-for-flutter-navigate-venue-data-venuegeometry-venuegeometry()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="boundingBox">
/sdk-for-flutter-navigate-venue-data-venuegeometry-boundingbox
→ /sdk-for-flutter-navigate-core-geobox-class
</dt>
<dd>
  The <code>GeoBox</code> of the bounding area of the geometry.
Gets a bounding box of the geometry.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="center">
/sdk-for-flutter-navigate-venue-data-venuegeometry-center
→ /sdk-for-flutter-navigate-core-geocoordinates-class
</dt>
<dd>
  The geographic coordinates of the center of the geometry.
Gets a center of the geometry.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geometryType">
/sdk-for-flutter-navigate-venue-data-venuegeometry-geometrytype
→ /sdk-for-flutter-navigate-venue-data-venuegeometrygeometrytype
</dt>
<dd>
  The type of the geometry.
Gets a type of the geometry.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-venue-data-venuegeometry-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="identifier">
/sdk-for-flutter-navigate-venue-data-venuegeometry-identifier
→ String
</dt>
<dd>
  The <code>id</code> of the geometry.
Gets an id of the geometry.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="internalAddress">
/sdk-for-flutter-navigate-venue-data-venuegeometry-internaladdress
→ /sdk-for-flutter-navigate-venue-data-venuegeometryinternaladdress-class?
</dt>
<dd>
  The internal address of the geometry.
Gets an internal address of the geometry.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="labelName">
/sdk-for-flutter-navigate-venue-data-venuegeometry-labelname
→ String
</dt>
<dd>
  The label name of the geometry.
Gets a label name of the geometry.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="labelStyle">
/sdk-for-flutter-navigate-venue-data-venuegeometry-labelstyle
→ /sdk-for-flutter-navigate-venue-style-venuelabelstyle-class?
</dt>
<dd>
  The label style of the geometry.
Gets a label style of the geometry.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="level">
/sdk-for-flutter-navigate-venue-data-venuegeometry-level
→ /sdk-for-flutter-navigate-venue-data-venuelevel-class
</dt>
<dd>
  The parent level of the geometry.
Gets a parent level of the geometry.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="levelID">
/sdk-for-flutter-navigate-venue-data-venuegeometry-levelid
→ String
</dt>
<dd>
  The level ID of geometry.
Gets level ID of the geometry.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lookupType">
/sdk-for-flutter-navigate-venue-data-venuegeometry-lookuptype
→ /sdk-for-flutter-navigate-venue-data-venuegeometrylookuptype
</dt>
<dd>
  The lookup type of the geometry.
Gets a lookup type of the geometry.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="name">
/sdk-for-flutter-navigate-venue-data-venuegeometry-name
→ String
</dt>
<dd>
  The name of the geometry.
If no name has been set, returns a label name.
Gets a name of the geometry.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="parentGeometry">
/sdk-for-flutter-navigate-venue-data-venuegeometry-parentgeometry
→ /sdk-for-flutter-navigate-venue-data-venuegeometry-class
</dt>
<dd>
  The parent geometry.
Defaults to <code>null</code>, if the geometry represents a base shape.
Gets a parent geometry on which the current geometry is located.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="properties">
/sdk-for-flutter-navigate-venue-data-venuegeometry-properties
→ /sdk-for-flutter-navigate-venue-data-venuegeometrystringtopropertymap
</dt>
<dd>
  The properties of the geometry.
Gets the properties of the geometry.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-venue-data-venuegeometry-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="style">
/sdk-for-flutter-navigate-venue-data-venuegeometry-style
→ /sdk-for-flutter-navigate-venue-style-venuegeometrystyle-class?
</dt>
<dd>
  The style of the geometry.
Gets a style of the geometry.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-venue-data-venuegeometry-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-venue-data-venuegeometry-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-venue-data-venuegeometry-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">VenueGeometry class</li>
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

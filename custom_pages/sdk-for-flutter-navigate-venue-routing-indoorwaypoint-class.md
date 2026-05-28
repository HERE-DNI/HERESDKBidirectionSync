---
title: "IndoorWaypoint class abstract"
slug: "sdk-for-flutter-navigate-venue-routing-indoorwaypoint-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IndoorWaypoint-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="venue.routing/IndoorWaypoint-class.html#constructors">Constructors</a></li>
<li><a href="venue.routing/IndoorWaypoint/IndoorWaypoint.html">IndoorWaypoint</a></li>
<li><a href="venue.routing/IndoorWaypoint/IndoorWaypoint.withOutdoorCoordinates.html">withOutdoorCoordinates</a></li>
<li class="section-title">
<a href="venue.routing/IndoorWaypoint-class.html#instance-properties">Properties</a>
</li>
<li><a href="venue.routing/IndoorWaypoint/coordinates.html">coordinates</a></li>
<li class="inherited"><a href="venue.routing/IndoorWaypoint/hashCode.html">hashCode</a></li>
<li><a href="venue.routing/IndoorWaypoint/levelId.html">levelId</a></li>
<li class="inherited"><a href="venue.routing/IndoorWaypoint/runtimeType.html">runtimeType</a></li>
<li><a href="venue.routing/IndoorWaypoint/venueId.html">venueId</a></li>
<li class="section-title inherited"><a href="venue.routing/IndoorWaypoint-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="venue.routing/IndoorWaypoint/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="venue.routing/IndoorWaypoint/toString.html">toString</a></li>
<li class="section-title inherited"><a href="venue.routing/IndoorWaypoint-class.html#operators">Operators</a></li>
<li class="inherited"><a href="venue.routing/IndoorWaypoint/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li class="self-crumb">IndoorWaypoint class</li>
</ol>
<div class="self-name">IndoorWaypoint</div>
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
<div class="main-content" data-above-sidebar="venue.routing/venue.routing-library-sidebar.html" data-below-sidebar="venue.routing/IndoorWaypoint-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>IndoorWaypoint class abstract</h1></div>
<section class="desc markdown">
<p>Represents an indoor waypoint, used as input for indoor route calculation.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="IndoorWaypoint">
/sdk-for-flutter-navigate-venue-routing-indoorwaypoint-indoorwaypoint(/sdk-for-flutter-navigate-core-geocoordinates-class coordinates, String venueId, String levelId)
</dt>
<dd>
          Creates an indoor waypoint.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="IndoorWaypoint.withOutdoorCoordinates">
/sdk-for-flutter-navigate-venue-routing-indoorwaypoint-indoorwaypoint-withoutdoorcoordinates(/sdk-for-flutter-navigate-core-geocoordinates-class coordinates)
</dt>
<dd>
          Creates an outdoor waypoint.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="coordinates">
/sdk-for-flutter-navigate-venue-routing-indoorwaypoint-coordinates
→ /sdk-for-flutter-navigate-core-geocoordinates-class
</dt>
<dd>
  The waypoint's geographic coordinates.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-venue-routing-indoorwaypoint-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="levelId">
/sdk-for-flutter-navigate-venue-routing-indoorwaypoint-levelid
→ String?
</dt>
<dd>
  The ID of the level where the waypoint is located, if applicable.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-venue-routing-indoorwaypoint-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="venueId">
/sdk-for-flutter-navigate-venue-routing-indoorwaypoint-venueid
→ String?
</dt>
<dd>
  The ID of the venue where the waypoint is located, if applicable.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-venue-routing-indoorwaypoint-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-venue-routing-indoorwaypoint-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-venue-routing-indoorwaypoint-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li class="self-crumb">IndoorWaypoint class</li>
</ol>
<h5>venue.routing library</h5>
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

---
title: "Untitled"
slug: "sdk-for-flutter-explore-core-geocoordinates-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoCoordinates-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li class="self-crumb">GeoCoordinates class</li>
</ol>
<div class="self-name">GeoCoordinates</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/GeoCoordinates-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>GeoCoordinates class</h1></div>
<section class="desc markdown">
<p>Represents geographical coordinates in 3D space.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Annotations</dt>
<dd>
<ul class="annotation-list clazz-relationships">
<li>@<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="GeoCoordinates">
/sdk-for-flutter-explore-core-geocoordinates-geocoordinates(double latitude, double longitude)
</dt>
<dd>
          Constructs a GeoCoordinates from the provided latitude and longitude values.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoCoordinates.withAltitude">
/sdk-for-flutter-explore-core-geocoordinates-geocoordinates-withaltitude(double latitude, double longitude, double altitude)
</dt>
<dd>
          Constructs a GeoCoordinates from the provided latitude, longitude and altitude values.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="altitude">
/sdk-for-flutter-explore-core-geocoordinates-altitude
→ double?
</dt>
<dd>
  Optional altitude in meters.
By convention, on iOS devices, altitude is set as meters relative to the
mean sea level.
On Android devices, altitude is set as meters relative to the WGS 84
reference ellipsoid.
  <div class="features">final</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-core-geocoordinates-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="latitude">
/sdk-for-flutter-explore-core-geocoordinates-latitude
→ double
</dt>
<dd>
  Latitude in degrees.
  <div class="features">final</div>
</dd>
<dt class="property" id="longitude">
/sdk-for-flutter-explore-core-geocoordinates-longitude
→ double
</dt>
<dd>
  Longitude in degrees.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-core-geocoordinates-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="distanceTo">
/sdk-for-flutter-explore-core-geocoordinates-distanceto(<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class point)
    → double

</dt>
<dd>
  Computes distance (in meters) along the great circle between two coordinates.
  

</dd>
<dt class="callable" id="interpolate">
/sdk-for-flutter-explore-core-geocoordinates-interpolate(<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class towardCoords, double factor)
    → /sdk-for-flutter-explore-core-geocoordinates-class

</dt>
<dd>
  Computes the coordinates of the interpolated location along the great circle between
the two coordinates.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-core-geocoordinates-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-core-geocoordinates-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-explore-core-geocoordinates-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="fromString">
/sdk-for-flutter-explore-core-geocoordinates-fromstring(<wbr/>String input)
    → /sdk-for-flutter-explore-core-geocoordinates-class?

</dt>
<dd>
  Constructs GeoCoordinates from the provided string in specified format.
  

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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li class="self-crumb">GeoCoordinates class</li>
</ol>
<h5>core library</h5>
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

---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-geocoordinates-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- GeoCoordinates-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/GeoCoordinates-class.html#constructors">Constructors</a></li>
<li><a href="core/GeoCoordinates/GeoCoordinates.html">GeoCoordinates</a></li>
<li><a href="core/GeoCoordinates/GeoCoordinates.withAltitude.html">withAltitude</a></li>
<li class="section-title">
<a href="core/GeoCoordinates-class.html#instance-properties">Properties</a>
</li>
<li><a href="core/GeoCoordinates/altitude.html">altitude</a></li>
<li><a href="core/GeoCoordinates/hashCode.html">hashCode</a></li>
<li><a href="core/GeoCoordinates/latitude.html">latitude</a></li>
<li><a href="core/GeoCoordinates/longitude.html">longitude</a></li>
<li class="inherited"><a href="core/GeoCoordinates/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="core/GeoCoordinates-class.html#instance-methods">Methods</a></li>
<li><a href="core/GeoCoordinates/distanceTo.html">distanceTo</a></li>
<li><a href="core/GeoCoordinates/interpolate.html">interpolate</a></li>
<li class="inherited"><a href="core/GeoCoordinates/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/GeoCoordinates/toString.html">toString</a></li>
<li class="section-title"><a href="core/GeoCoordinates-class.html#operators">Operators</a></li>
<li><a href="core/GeoCoordinates/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="core/GeoCoordinates-class.html#static-methods">Static methods</a></li>
<li><a href="core/GeoCoordinates/fromString.html">fromString</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
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
<a href="../core/GeoCoordinates/GeoCoordinates.html">/sdk-for-flutter-explore-core-geocoordinates-geocoordinates</a>(double latitude, double longitude)
</dt>
<dd>
          Constructs a GeoCoordinates from the provided latitude and longitude values.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoCoordinates.withAltitude">
<a href="../core/GeoCoordinates/GeoCoordinates.withAltitude.html">/sdk-for-flutter-explore-core-geocoordinates-geocoordinates-withaltitude</a>(double latitude, double longitude, double altitude)
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
<a href="../core/GeoCoordinates/altitude.html">/sdk-for-flutter-explore-core-geocoordinates-altitude</a>
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
<a href="../core/GeoCoordinates/hashCode.html">/sdk-for-flutter-explore-core-geocoordinates-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="latitude">
<a href="../core/GeoCoordinates/latitude.html">/sdk-for-flutter-explore-core-geocoordinates-latitude</a>
→ double
</dt>
<dd>
  Latitude in degrees.
  <div class="features">final</div>
</dd>
<dt class="property" id="longitude">
<a href="../core/GeoCoordinates/longitude.html">/sdk-for-flutter-explore-core-geocoordinates-longitude</a>
→ double
</dt>
<dd>
  Longitude in degrees.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core/GeoCoordinates/runtimeType.html">/sdk-for-flutter-explore-core-geocoordinates-runtimetype</a>
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
<a href="../core/GeoCoordinates/distanceTo.html">/sdk-for-flutter-explore-core-geocoordinates-distanceto</a>(<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> point)
    → double

</dt>
<dd>
  Computes distance (in meters) along the great circle between two coordinates.
  

</dd>
<dt class="callable" id="interpolate">
<a href="../core/GeoCoordinates/interpolate.html">/sdk-for-flutter-explore-core-geocoordinates-interpolate</a>(<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> towardCoords, double factor)
    → <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>
</dt>
<dd>
  Computes the coordinates of the interpolated location along the great circle between
the two coordinates.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../core/GeoCoordinates/noSuchMethod.html">/sdk-for-flutter-explore-core-geocoordinates-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core/GeoCoordinates/toString.html">/sdk-for-flutter-explore-core-geocoordinates-tostring</a>(<wbr/>)
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
<a href="../core/GeoCoordinates/operator_equals.html">/sdk-for-flutter-explore-core-geocoordinates-operator-equals</a>(<wbr/>Object other)
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
<a href="../core/GeoCoordinates/fromString.html">/sdk-for-flutter-explore-core-geocoordinates-fromstring</a>(<wbr/>String input)
    → <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>?

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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
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
</div></div>
</div>
</HTMLBlock>

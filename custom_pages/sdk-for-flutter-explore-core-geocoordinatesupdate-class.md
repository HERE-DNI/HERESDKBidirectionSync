---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-geocoordinatesupdate-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- GeoCoordinatesUpdate-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/GeoCoordinatesUpdate-class.html#constructors">Constructors</a></li>
<li><a href="core/GeoCoordinatesUpdate/GeoCoordinatesUpdate.html">GeoCoordinatesUpdate</a></li>
<li><a href="core/GeoCoordinatesUpdate/GeoCoordinatesUpdate.fromGeoCoordinates.html">fromGeoCoordinates</a></li>
<li><a href="core/GeoCoordinatesUpdate/GeoCoordinatesUpdate.withAltitude.html">withAltitude</a></li>
<li class="section-title">
<a href="core/GeoCoordinatesUpdate-class.html#instance-properties">Properties</a>
</li>
<li><a href="core/GeoCoordinatesUpdate/altitude.html">altitude</a></li>
<li><a href="core/GeoCoordinatesUpdate/hashCode.html">hashCode</a></li>
<li><a href="core/GeoCoordinatesUpdate/latitude.html">latitude</a></li>
<li><a href="core/GeoCoordinatesUpdate/longitude.html">longitude</a></li>
<li class="inherited"><a href="core/GeoCoordinatesUpdate/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="core/GeoCoordinatesUpdate-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core/GeoCoordinatesUpdate/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/GeoCoordinatesUpdate/toString.html">toString</a></li>
<li class="section-title"><a href="core/GeoCoordinatesUpdate-class.html#operators">Operators</a></li>
<li><a href="core/GeoCoordinatesUpdate/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li class="self-crumb">GeoCoordinatesUpdate class</li>
</ol>
<div class="self-name">GeoCoordinatesUpdate</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/GeoCoordinatesUpdate-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>GeoCoordinatesUpdate class</h1></div>
<section class="desc markdown">
<p>Represents geographical coordinates in 3D space.</p>
<p>Unlike <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>, its members can be undefined, allowing for APIs
that update only the specified parts of geo coordinates.</p>
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
<dt class="callable" id="GeoCoordinatesUpdate">
<a href="../core/GeoCoordinatesUpdate/GeoCoordinatesUpdate.html">/sdk-for-flutter-explore-core-geocoordinatesupdate-geocoordinatesupdate</a>(double? latitude, double? longitude)
</dt>
<dd>
          Constructs a GeoCoordinatesUpdate from the provided latitude and
longitude values.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoCoordinatesUpdate.fromGeoCoordinates">
<a href="../core/GeoCoordinatesUpdate/GeoCoordinatesUpdate.fromGeoCoordinates.html">/sdk-for-flutter-explore-core-geocoordinatesupdate-geocoordinatesupdate-fromgeocoordinates</a>(<a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> coordinates)
</dt>
<dd>
          Constructs a GeoCoordinatesUpdate from GeoCoordinates
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoCoordinatesUpdate.withAltitude">
<a href="../core/GeoCoordinatesUpdate/GeoCoordinatesUpdate.withAltitude.html">/sdk-for-flutter-explore-core-geocoordinatesupdate-geocoordinatesupdate-withaltitude</a>(double? latitude, double? longitude, double? altitude)
</dt>
<dd>
          Constructs a GeoCoordinatesUpdate from the provided latitude, longitude
and alt values.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="altitude">
<a href="../core/GeoCoordinatesUpdate/altitude.html">/sdk-for-flutter-explore-core-geocoordinatesupdate-altitude</a>
→ double?
</dt>
<dd>
  Optional altitude in meters.
  <div class="features">final</div>
</dd>
<dt class="property" id="hashCode">
<a href="../core/GeoCoordinatesUpdate/hashCode.html">/sdk-for-flutter-explore-core-geocoordinatesupdate-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="latitude">
<a href="../core/GeoCoordinatesUpdate/latitude.html">/sdk-for-flutter-explore-core-geocoordinatesupdate-latitude</a>
→ double?
</dt>
<dd>
  Optional latitude in degrees.
  <div class="features">final</div>
</dd>
<dt class="property" id="longitude">
<a href="../core/GeoCoordinatesUpdate/longitude.html">/sdk-for-flutter-explore-core-geocoordinatesupdate-longitude</a>
→ double?
</dt>
<dd>
  Optional longitude in degrees.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core/GeoCoordinatesUpdate/runtimeType.html">/sdk-for-flutter-explore-core-geocoordinatesupdate-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../core/GeoCoordinatesUpdate/noSuchMethod.html">/sdk-for-flutter-explore-core-geocoordinatesupdate-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core/GeoCoordinatesUpdate/toString.html">/sdk-for-flutter-explore-core-geocoordinatesupdate-tostring</a>(<wbr/>)
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
<a href="../core/GeoCoordinatesUpdate/operator_equals.html">/sdk-for-flutter-explore-core-geocoordinatesupdate-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

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
<li class="self-crumb">GeoCoordinatesUpdate class</li>
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

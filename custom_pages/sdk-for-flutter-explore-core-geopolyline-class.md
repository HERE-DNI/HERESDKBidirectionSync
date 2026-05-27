---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-geopolyline-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- GeoPolyline-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/GeoPolyline-class.html#constructors">Constructors</a></li>
<li><a href="core/GeoPolyline/GeoPolyline.html">GeoPolyline</a></li>
<li><a href="core/GeoPolyline/GeoPolyline.withGeoBox.html">withGeoBox</a></li>
<li class="section-title">
<a href="core/GeoPolyline-class.html#instance-properties">Properties</a>
</li>
<li><a href="core/GeoPolyline/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="core/GeoPolyline/runtimeType.html">runtimeType</a></li>
<li><a href="core/GeoPolyline/vertices.html">vertices</a></li>
<li class="section-title"><a href="core/GeoPolyline-class.html#instance-methods">Methods</a></li>
<li><a href="core/GeoPolyline/coordinatesAtOffsetInMeters.html">coordinatesAtOffsetInMeters</a></li>
<li><a href="core/GeoPolyline/getNearestIndexTo.html">getNearestIndexTo</a></li>
<li class="inherited"><a href="core/GeoPolyline/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/GeoPolyline/toString.html">toString</a></li>
<li class="section-title"><a href="core/GeoPolyline-class.html#operators">Operators</a></li>
<li><a href="core/GeoPolyline/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li class="self-crumb">GeoPolyline class</li>
</ol>
<div class="self-name">GeoPolyline</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/GeoPolyline-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>GeoPolyline class</h1></div>
<section class="desc markdown">
<p>A list of geographic coordinates representing the vertices of a polyline.</p>
<p>An instance of this class, initialized with appropriate vertices.
Represents a <code>GeoPolyline</code> as a series of geographic coordinates.</p>
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
<dt class="callable" id="GeoPolyline">
<a href="../core/GeoPolyline/GeoPolyline.html">/sdk-for-flutter-explore-core-geopolyline-geopolyline</a>(List&lt;<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>&gt; vertices)
</dt>
<dd>
          Constructs a GeoPolyline from the provided vertices.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoPolyline.withGeoBox">
<a href="../core/GeoPolyline/GeoPolyline.withGeoBox.html">/sdk-for-flutter-explore-core-geopolyline-geopolyline-withgeobox</a>(<a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> geoBox)
</dt>
<dd>
          Constructs an instance of this class from <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
<a href="../core/GeoPolyline/hashCode.html">/sdk-for-flutter-explore-core-geopolyline-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core/GeoPolyline/runtimeType.html">/sdk-for-flutter-explore-core-geopolyline-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="vertices">
<a href="../core/GeoPolyline/vertices.html">/sdk-for-flutter-explore-core-geopolyline-vertices</a>
→ List&lt;<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>&gt;
</dt>
<dd>
  The list of vertices representing the polyline.
  <div class="features">final</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="coordinatesAtOffsetInMeters">
<a href="../core/GeoPolyline/coordinatesAtOffsetInMeters.html">/sdk-for-flutter-explore-core-geopolyline-coordinatesatoffsetinmeters</a>(<wbr/>double offsetInMeters, <a href="../core/GeoPolylineDirection.html">/sdk-for-flutter-explore-core-geopolylinedirection</a> direction)
    → <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>
</dt>
<dd>
  Returns the coordinates at the given distance along the polyline.
  

</dd>
<dt class="callable" id="getNearestIndexTo">
<a href="../core/GeoPolyline/getNearestIndexTo.html">/sdk-for-flutter-explore-core-geopolyline-getnearestindexto</a>(<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> point)
    → int

</dt>
<dd>
  Returns the index of the nearest vertex to the given point.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../core/GeoPolyline/noSuchMethod.html">/sdk-for-flutter-explore-core-geopolyline-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core/GeoPolyline/toString.html">/sdk-for-flutter-explore-core-geopolyline-tostring</a>(<wbr/>)
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
<a href="../core/GeoPolyline/operator_equals.html">/sdk-for-flutter-explore-core-geopolyline-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">GeoPolyline class</li>
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

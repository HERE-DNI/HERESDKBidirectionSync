---
title: "GeoPolyline class"
slug: "sdk-for-flutter-navigate-core-geopolyline-class"
---

<HTMLBlock>{
`
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
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
/sdk-for-flutter-navigate-core-geopolyline-geopolyline(List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt; vertices)
</dt>
<dd>
          Constructs a GeoPolyline from the provided vertices.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoPolyline.withGeoBox">
/sdk-for-flutter-navigate-core-geopolyline-geopolyline-withgeobox(/sdk-for-flutter-navigate-core-geobox-class geoBox)
</dt>
<dd>
          Constructs an instance of this class from /sdk-for-flutter-navigate-core-geobox-class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-core-geopolyline-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-geopolyline-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="vertices">
/sdk-for-flutter-navigate-core-geopolyline-vertices
→ List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt;
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
/sdk-for-flutter-navigate-core-geopolyline-coordinatesatoffsetinmeters(<wbr/>double offsetInMeters, /sdk-for-flutter-navigate-core-geopolylinedirection direction)
    → /sdk-for-flutter-navigate-core-geocoordinates-class

</dt>
<dd>
  Returns the coordinates at the given distance along the polyline.
  

</dd>
<dt class="callable" id="getNearestIndexTo">
/sdk-for-flutter-navigate-core-geopolyline-getnearestindexto(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class point)
    → int

</dt>
<dd>
  Returns the index of the nearest vertex to the given point.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-core-geopolyline-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-core-geopolyline-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-core-geopolyline-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
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
`
}</HTMLBlock>

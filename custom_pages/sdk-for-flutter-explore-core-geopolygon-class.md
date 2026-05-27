---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-geopolygon-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- GeoPolygon-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/GeoPolygon-class.html#constructors">Constructors</a></li>
<li><a href="core/GeoPolygon/GeoPolygon.html">GeoPolygon</a></li>
<li><a href="core/GeoPolygon/GeoPolygon.withGeoBox.html">withGeoBox</a></li>
<li><a href="core/GeoPolygon/GeoPolygon.withGeoCircle.html">withGeoCircle</a></li>
<li><a href="core/GeoPolygon/GeoPolygon.withInnerBoundaries.html">withInnerBoundaries</a></li>
<li class="section-title">
<a href="core/GeoPolygon-class.html#instance-properties">Properties</a>
</li>
<li><a href="core/GeoPolygon/hashCode.html">hashCode</a></li>
<li><a href="core/GeoPolygon/innerBoundaries.html">innerBoundaries</a></li>
<li class="inherited"><a href="core/GeoPolygon/runtimeType.html">runtimeType</a></li>
<li><a href="core/GeoPolygon/vertices.html">vertices</a></li>
<li class="section-title inherited"><a href="core/GeoPolygon-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core/GeoPolygon/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/GeoPolygon/toString.html">toString</a></li>
<li class="section-title"><a href="core/GeoPolygon-class.html#operators">Operators</a></li>
<li><a href="core/GeoPolygon/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li class="self-crumb">GeoPolygon class</li>
</ol>
<div class="self-name">GeoPolygon</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/GeoPolygon-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>GeoPolygon class</h1></div>
<section class="desc markdown">
<p>Represents a <code>GeoPolygon</code> area as a series of geographic coordinates, and optionally,
a list of inner boundaries (also known as holes).</p>
<p>An instance of this class, initialized with appropriate vertices.</p>
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
<dt class="callable" id="GeoPolygon">
<a href="../core/GeoPolygon/GeoPolygon.html">/sdk-for-flutter-explore-core-geopolygon-geopolygon</a>(List&lt;<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>&gt; vertices)
</dt>
<dd>
          Constructs an instance of this class from the provided vertices.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoPolygon.withGeoBox">
<a href="../core/GeoPolygon/GeoPolygon.withGeoBox.html">/sdk-for-flutter-explore-core-geopolygon-geopolygon-withgeobox</a>(<a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> geoBox)
</dt>
<dd>
          Constructs an instance of this class from <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoPolygon.withGeoCircle">
<a href="../core/GeoPolygon/GeoPolygon.withGeoCircle.html">/sdk-for-flutter-explore-core-geopolygon-geopolygon-withgeocircle</a>(<a href="../core/GeoCircle-class.html">/sdk-for-flutter-explore-core-geocircle-class</a> geoCircle)
</dt>
<dd>
          Constructs an instance of this class from <a href="../core/GeoCircle-class.html">/sdk-for-flutter-explore-core-geocircle-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoPolygon.withInnerBoundaries">
<a href="../core/GeoPolygon/GeoPolygon.withInnerBoundaries.html">/sdk-for-flutter-explore-core-geopolygon-geopolygon-withinnerboundaries</a>(List&lt;<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>&gt; vertices, List&lt;<wbr/>List&lt;<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>&gt;&gt; innerBoundaries)
</dt>
<dd>
          Constructs an instance of this class from the provided vertices and inner boundaries (holes).
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
<a href="../core/GeoPolygon/hashCode.html">/sdk-for-flutter-explore-core-geopolygon-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="innerBoundaries">
<a href="../core/GeoPolygon/innerBoundaries.html">/sdk-for-flutter-explore-core-geopolygon-innerboundaries</a>
→ List&lt;<wbr/>List&lt;<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>&gt;&gt;
</dt>
<dd>
  The list of polygon inner boundaries (holes), each defined as a list of geographic coordinates.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core/GeoPolygon/runtimeType.html">/sdk-for-flutter-explore-core-geopolygon-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="vertices">
<a href="../core/GeoPolygon/vertices.html">/sdk-for-flutter-explore-core-geopolygon-vertices</a>
→ List&lt;<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>&gt;
</dt>
<dd>
  The list of geographic coordinates representing the outer boundary vertices of polygon.
  <div class="features">final</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../core/GeoPolygon/noSuchMethod.html">/sdk-for-flutter-explore-core-geopolygon-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core/GeoPolygon/toString.html">/sdk-for-flutter-explore-core-geopolygon-tostring</a>(<wbr/>)
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
<a href="../core/GeoPolygon/operator_equals.html">/sdk-for-flutter-explore-core-geopolygon-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">GeoPolygon class</li>
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

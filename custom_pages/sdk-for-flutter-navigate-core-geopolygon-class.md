---
title: "Untitled"
slug: "sdk-for-flutter-navigate-core-geopolygon-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoPolygon-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
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
/sdk-for-flutter-navigate-core-geopolygon-geopolygon(List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt; vertices)
</dt>
<dd>
          Constructs an instance of this class from the provided vertices.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoPolygon.withGeoBox">
/sdk-for-flutter-navigate-core-geopolygon-geopolygon-withgeobox(/sdk-for-flutter-navigate-core-geobox-class geoBox)
</dt>
<dd>
          Constructs an instance of this class from /sdk-for-flutter-navigate-core-geobox-class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoPolygon.withGeoCircle">
/sdk-for-flutter-navigate-core-geopolygon-geopolygon-withgeocircle(/sdk-for-flutter-navigate-core-geocircle-class geoCircle)
</dt>
<dd>
          Constructs an instance of this class from /sdk-for-flutter-navigate-core-geocircle-class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoPolygon.withInnerBoundaries">
/sdk-for-flutter-navigate-core-geopolygon-geopolygon-withinnerboundaries(List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt; vertices, List&lt;<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt;&gt; innerBoundaries)
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
/sdk-for-flutter-navigate-core-geopolygon-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="innerBoundaries">
/sdk-for-flutter-navigate-core-geopolygon-innerboundaries
→ List&lt;<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt;&gt;
</dt>
<dd>
  The list of polygon inner boundaries (holes), each defined as a list of geographic coordinates.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-geopolygon-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="vertices">
/sdk-for-flutter-navigate-core-geopolygon-vertices
→ List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt;
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
/sdk-for-flutter-navigate-core-geopolygon-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-core-geopolygon-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-core-geopolygon-operator-equals(<wbr/>Object other)
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



</div>
`
}</HTMLBlock>

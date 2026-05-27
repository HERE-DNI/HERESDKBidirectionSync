---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-geobox-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- GeoBox-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/GeoBox-class.html#constructors">Constructors</a></li>
<li><a href="core/GeoBox/GeoBox.html">GeoBox</a></li>
<li class="section-title">
<a href="core/GeoBox-class.html#instance-properties">Properties</a>
</li>
<li><a href="core/GeoBox/hashCode.html">hashCode</a></li>
<li><a href="core/GeoBox/northEastCorner.html">northEastCorner</a></li>
<li class="inherited"><a href="core/GeoBox/runtimeType.html">runtimeType</a></li>
<li><a href="core/GeoBox/southWestCorner.html">southWestCorner</a></li>
<li class="section-title"><a href="core/GeoBox-class.html#instance-methods">Methods</a></li>
<li><a href="core/GeoBox/containsGeoBox.html">containsGeoBox</a></li>
<li><a href="core/GeoBox/containsGeoCoordinates.html">containsGeoCoordinates</a></li>
<li><a href="core/GeoBox/envelope.html">envelope</a></li>
<li><a href="core/GeoBox/expandedBy.html">expandedBy</a></li>
<li><a href="core/GeoBox/intersection.html">intersection</a></li>
<li><a href="core/GeoBox/intersects.html">intersects</a></li>
<li class="inherited"><a href="core/GeoBox/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/GeoBox/toString.html">toString</a></li>
<li class="section-title"><a href="core/GeoBox-class.html#operators">Operators</a></li>
<li><a href="core/GeoBox/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="core/GeoBox-class.html#static-methods">Static methods</a></li>
<li><a href="core/GeoBox/containingGeoCoordinates.html">containingGeoCoordinates</a></li>
<li><a href="core/GeoBox/envelopeGeoBoxes.html">envelopeGeoBoxes</a></li>
<li><a href="core/GeoBox/intersectionGeoBoxes.html">intersectionGeoBoxes</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li class="self-crumb">GeoBox class</li>
</ol>
<div class="self-name">GeoBox</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/GeoBox-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>GeoBox class</h1></div>
<section class="desc markdown">
<p>Represents a bounding rectangle aligned with latitude and longitude.</p>
<p>Geographic area represented by this would be visualised as a rectangle
when using a normal cylindrical projection (such as Mercator).
The box has a maximum span of 360 degrees in longitude and 180 degrees in latitude direction.
The box with equal values in longitude for the corners is considered as a span of 360 degrees.
The box is considered empty if the latitude of the <code>GeoBox.southWestCorner</code> is larger than the the
latitude of the <code>GeoBox.northEastCorner</code>.</p>
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
<dt class="callable" id="GeoBox">
<a href="../core/GeoBox/GeoBox.html">/sdk-for-flutter-explore-core-geobox-geobox</a>(<a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> southWestCorner, <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> northEastCorner)
</dt>
<dd>
          Creates a new instance.
            <div class="constructor-modifier features">const</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
<a href="../core/GeoBox/hashCode.html">/sdk-for-flutter-explore-core-geobox-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="northEastCorner">
<a href="../core/GeoBox/northEastCorner.html">/sdk-for-flutter-explore-core-geobox-northeastcorner</a>
→ <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>
</dt>
<dd>
  North east corner coordinates.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core/GeoBox/runtimeType.html">/sdk-for-flutter-explore-core-geobox-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="southWestCorner">
<a href="../core/GeoBox/southWestCorner.html">/sdk-for-flutter-explore-core-geobox-southwestcorner</a>
→ <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>
</dt>
<dd>
  South west corner coordinates.
  <div class="features">final</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="containsGeoBox">
<a href="../core/GeoBox/containsGeoBox.html">/sdk-for-flutter-explore-core-geobox-containsgeobox</a>(<wbr/><a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> geoBox)
    → bool

</dt>
<dd>
  Determines whether the specified <code>GeoBox</code> is covered entirely by this <code>GeoBox</code>.
  

</dd>
<dt class="callable" id="containsGeoCoordinates">
<a href="../core/GeoBox/containsGeoCoordinates.html">/sdk-for-flutter-explore-core-geobox-containsgeocoordinates</a>(<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> geoCoordinates)
    → bool

</dt>
<dd>
  Determines whether the specified GeoCoordinates is contained within this <code>GeoBox</code>.
  

</dd>
<dt class="callable" id="envelope">
<a href="../core/GeoBox/envelope.html">/sdk-for-flutter-explore-core-geobox-envelope</a>(<wbr/><a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> geoBox)
    → <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>
</dt>
<dd>
  Envelopes two <code>GeoBox</code> areas by returning the smallest <code>GeoBox</code> covering both this
GeoBox and the specified <code>GeoBox</code>.
  

</dd>
<dt class="callable" id="expandedBy">
<a href="../core/GeoBox/expandedBy.html">/sdk-for-flutter-explore-core-geobox-expandedby</a>(<wbr/>double southMeters, double westMeters, double northMeters, double eastMeters)
    → <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>
</dt>
<dd>
  Creates a <code>GeoBox</code> which is expanded by a fixed distance.
  

</dd>
<dt class="callable" id="intersection">
<a href="../core/GeoBox/intersection.html">/sdk-for-flutter-explore-core-geobox-intersection</a>(<wbr/><a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> geoBox)
    → List&lt;<wbr/><a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>&gt;

</dt>
<dd>
  Computes the intersection with the passed <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>.
  

</dd>
<dt class="callable" id="intersects">
<a href="../core/GeoBox/intersects.html">/sdk-for-flutter-explore-core-geobox-intersects</a>(<wbr/><a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> geoBox)
    → bool

</dt>
<dd>
  Determines whether this <code>GeoBox</code> intersects with the passed <code>GeoBox</code>.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../core/GeoBox/noSuchMethod.html">/sdk-for-flutter-explore-core-geobox-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core/GeoBox/toString.html">/sdk-for-flutter-explore-core-geobox-tostring</a>(<wbr/>)
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
<a href="../core/GeoBox/operator_equals.html">/sdk-for-flutter-explore-core-geobox-operator-equals</a>(<wbr/>Object other)
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
<dt class="callable" id="containingGeoCoordinates">
<a href="../core/GeoBox/containingGeoCoordinates.html">/sdk-for-flutter-explore-core-geobox-containinggeocoordinates</a>(<wbr/>List&lt;<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>&gt; geoCoordinates)
    → <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>?

</dt>
<dd>
  Creates a <code>GeoBox</code> which encompases all coordinates from the list.
  

</dd>
<dt class="callable" id="envelopeGeoBoxes">
<a href="../core/GeoBox/envelopeGeoBoxes.html">/sdk-for-flutter-explore-core-geobox-envelopegeoboxes</a>(<wbr/>List&lt;<wbr/><a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>&gt; geoBoxes)
    → <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>?

</dt>
<dd>
  Envelopes the list of <code>GeoBox</code> areas by returning the smallest
<code>GeoBox</code> covering all specified <code>GeoBox</code> objects.
  

</dd>
<dt class="callable" id="intersectionGeoBoxes">
<a href="../core/GeoBox/intersectionGeoBoxes.html">/sdk-for-flutter-explore-core-geobox-intersectiongeoboxes</a>(<wbr/>List&lt;<wbr/><a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>&gt; geoBoxes)
    → List&lt;<wbr/><a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>&gt;

</dt>
<dd>
  Computes intersection of list of <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> instances.
  

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
<li class="self-crumb">GeoBox class</li>
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

---
title: "GeoBox class"
slug: "sdk-for-flutter-navigate-core-geobox-class"
---

<HTMLBlock>{
`
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
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
/sdk-for-flutter-navigate-core-geobox-geobox(/sdk-for-flutter-navigate-core-geocoordinates-class southWestCorner, /sdk-for-flutter-navigate-core-geocoordinates-class northEastCorner)
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
/sdk-for-flutter-navigate-core-geobox-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="northEastCorner">
/sdk-for-flutter-navigate-core-geobox-northeastcorner
→ /sdk-for-flutter-navigate-core-geocoordinates-class
</dt>
<dd>
  North east corner coordinates.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-geobox-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="southWestCorner">
/sdk-for-flutter-navigate-core-geobox-southwestcorner
→ /sdk-for-flutter-navigate-core-geocoordinates-class
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
/sdk-for-flutter-navigate-core-geobox-containsgeobox(<wbr/>/sdk-for-flutter-navigate-core-geobox-class geoBox)
    → bool

</dt>
<dd>
  Determines whether the specified <code>GeoBox</code> is covered entirely by this <code>GeoBox</code>.
  

</dd>
<dt class="callable" id="containsGeoCoordinates">
/sdk-for-flutter-navigate-core-geobox-containsgeocoordinates(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class geoCoordinates)
    → bool

</dt>
<dd>
  Determines whether the specified GeoCoordinates is contained within this <code>GeoBox</code>.
  

</dd>
<dt class="callable" id="envelope">
/sdk-for-flutter-navigate-core-geobox-envelope(<wbr/>/sdk-for-flutter-navigate-core-geobox-class geoBox)
    → /sdk-for-flutter-navigate-core-geobox-class

</dt>
<dd>
  Envelopes two <code>GeoBox</code> areas by returning the smallest <code>GeoBox</code> covering both this
GeoBox and the specified <code>GeoBox</code>.
  

</dd>
<dt class="callable" id="expandedBy">
/sdk-for-flutter-navigate-core-geobox-expandedby(<wbr/>double southMeters, double westMeters, double northMeters, double eastMeters)
    → /sdk-for-flutter-navigate-core-geobox-class

</dt>
<dd>
  Creates a <code>GeoBox</code> which is expanded by a fixed distance.
  

</dd>
<dt class="callable" id="intersection">
/sdk-for-flutter-navigate-core-geobox-intersection(<wbr/>/sdk-for-flutter-navigate-core-geobox-class geoBox)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-core-geobox-class&gt;

</dt>
<dd>
  Computes the intersection with the passed /sdk-for-flutter-navigate-core-geobox-class.
  

</dd>
<dt class="callable" id="intersects">
/sdk-for-flutter-navigate-core-geobox-intersects(<wbr/>/sdk-for-flutter-navigate-core-geobox-class geoBox)
    → bool

</dt>
<dd>
  Determines whether this <code>GeoBox</code> intersects with the passed <code>GeoBox</code>.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-core-geobox-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-core-geobox-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-core-geobox-operator-equals(<wbr/>Object other)
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
/sdk-for-flutter-navigate-core-geobox-containinggeocoordinates(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt; geoCoordinates)
    → /sdk-for-flutter-navigate-core-geobox-class?

</dt>
<dd>
  Creates a <code>GeoBox</code> which encompases all coordinates from the list.
  

</dd>
<dt class="callable" id="envelopeGeoBoxes">
/sdk-for-flutter-navigate-core-geobox-envelopegeoboxes(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-geobox-class&gt; geoBoxes)
    → /sdk-for-flutter-navigate-core-geobox-class?

</dt>
<dd>
  Envelopes the list of <code>GeoBox</code> areas by returning the smallest
<code>GeoBox</code> covering all specified <code>GeoBox</code> objects.
  

</dd>
<dt class="callable" id="intersectionGeoBoxes">
/sdk-for-flutter-navigate-core-geobox-intersectiongeoboxes(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-geobox-class&gt; geoBoxes)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-core-geobox-class&gt;

</dt>
<dd>
  Computes intersection of list of /sdk-for-flutter-navigate-core-geobox-class instances.
  

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
`
}</HTMLBlock>

---
title: "GeoCorridor class"
slug: "sdk-for-flutter-explore-core-geocorridor-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoCorridor-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/GeoCorridor-class.html#constructors">Constructors</a></li>
<li><a href="core/GeoCorridor/GeoCorridor.html">GeoCorridor</a></li>
<li><a href="core/GeoCorridor/GeoCorridor.withPolyline.html">withPolyline</a></li>
<li class="section-title">
<a href="core/GeoCorridor-class.html#instance-properties">Properties</a>
</li>
<li><a href="core/GeoCorridor/halfWidthInMeters.html">halfWidthInMeters</a></li>
<li><a href="core/GeoCorridor/hashCode.html">hashCode</a></li>
<li><a href="core/GeoCorridor/polyline.html">polyline</a></li>
<li class="inherited"><a href="core/GeoCorridor/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="core/GeoCorridor-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core/GeoCorridor/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/GeoCorridor/toString.html">toString</a></li>
<li class="section-title"><a href="core/GeoCorridor-class.html#operators">Operators</a></li>
<li><a href="core/GeoCorridor/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li class="self-crumb">GeoCorridor class</li>
</ol>
<div class="self-name">GeoCorridor</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/GeoCorridor-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>GeoCorridor class</h1></div>
<section class="desc markdown">
<p>A geographical area that wraps around a geographical polyline with a given distance.</p>
<p>The corridor has round edges at the endpoints of the polyline. The distance from
any point of the polyline to the closest border of the corridor is always the same.</p>
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
<dt class="callable" id="GeoCorridor">
/sdk-for-flutter-explore-core-geocorridor-geocorridor(List&lt;<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class&gt; polyline, int halfWidthInMeters)
</dt>
<dd>
          Constructs a GeoCorridor from the provided polyline and half-width in meters.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoCorridor.withPolyline">
/sdk-for-flutter-explore-core-geocorridor-geocorridor-withpolyline(List&lt;<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class&gt; polyline)
</dt>
<dd>
          Constructs a GeoCorridor from the provided polyline.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="halfWidthInMeters">
/sdk-for-flutter-explore-core-geocorridor-halfwidthinmeters
→ int?
</dt>
<dd>
  The shortest distance from any point on the polyline to the border of the corridor.
  <div class="features">final</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-core-geocorridor-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="polyline">
/sdk-for-flutter-explore-core-geocorridor-polyline
→ List&lt;<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class&gt;
</dt>
<dd>
  The polyline passing through the middle of the corridor.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-core-geocorridor-runtimetype
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
/sdk-for-flutter-explore-core-geocorridor-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-core-geocorridor-tostring(<wbr/>)
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
/sdk-for-flutter-explore-core-geocorridor-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li class="self-crumb">GeoCorridor class</li>
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

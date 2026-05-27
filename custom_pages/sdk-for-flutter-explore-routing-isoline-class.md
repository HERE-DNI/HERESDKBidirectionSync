---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-isoline-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- Isoline-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/Isoline-class.html#constructors">Constructors</a></li>
<li><a href="routing/Isoline/Isoline.html">Isoline</a></li>
<li class="section-title">
<a href="routing/Isoline-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/Isoline/center.html">center</a></li>
<li class="inherited"><a href="routing/Isoline/hashCode.html">hashCode</a></li>
<li><a href="routing/Isoline/polygons.html">polygons</a></li>
<li><a href="routing/Isoline/rangeType.html">rangeType</a></li>
<li><a href="routing/Isoline/rangeValue.html">rangeValue</a></li>
<li class="inherited"><a href="routing/Isoline/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="routing/Isoline-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/Isoline/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/Isoline/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/Isoline-class.html#operators">Operators</a></li>
<li class="inherited"><a href="routing/Isoline/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">Isoline class</li>
</ol>
<div class="self-name">Isoline</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Isoline-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Isoline class abstract</h1></div>
<section class="desc markdown">
<p>Represents an isoline polygon around a center point.</p>
<p>Any possible route between
the center and any point on the edges of the polygon can be travelled within the
given range restriction. The edges of the polygon are not guaranteed to be on the road as
all reachable road endpoints are smoothened to fit into one polygon shape. This
process can be influenced by setting <a href="../routing/IsolineOptionsCalculation/maxPoints.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-maxpoints</a>.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Isoline">
<a href="../routing/Isoline/Isoline.html">/sdk-for-flutter-explore-routing-isoline-isoline</a>(<a href="../routing/IsolineRangeType.html">/sdk-for-flutter-explore-routing-isolinerangetype</a> rangeType, double rangeValue, <a href="../routing/MapMatchedCoordinates-class.html">/sdk-for-flutter-explore-routing-mapmatchedcoordinates-class</a> center, List&lt;<wbr/><a href="../core/GeoPolygon-class.html">/sdk-for-flutter-explore-core-geopolygon-class</a>&gt; polygons)
</dt>
<dd>
          Constructs an isoline instance.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="center">
<a href="../routing/Isoline/center.html">/sdk-for-flutter-explore-routing-isoline-center</a>
→ <a href="../routing/MapMatchedCoordinates-class.html">/sdk-for-flutter-explore-routing-mapmatchedcoordinates-class</a>
</dt>
<dd>
  The center point that was used to calculate this isoline.
Specifies the center point that was used to calculate this isoline.
This includes the original center that was passed to the RoutingEngine.
Gets the center point that was used to calculate this isoline.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../routing/Isoline/hashCode.html">/sdk-for-flutter-explore-routing-isoline-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="polygons">
<a href="../routing/Isoline/polygons.html">/sdk-for-flutter-explore-routing-isoline-polygons</a>
→ List&lt;<wbr/><a href="../core/GeoPolygon-class.html">/sdk-for-flutter-explore-core-geopolygon-class</a>&gt;
</dt>
<dd>
  A list of polygons that belong to this isoline. An isoline can consist of multiple
polygons. For example, islands that can be reached by a ferry are included.
Each island is then represented as a separate polygon. However, in most cases
only a single polygon is included.
Gets a list of polygons that belong to this isoline. An isoline can consist of multiple
polygons. For example, islands that can be reached by a ferry are included.
Each island is then represented as a separate polygon. However, in most cases
only a single polygon is included.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="rangeType">
<a href="../routing/Isoline/rangeType.html">/sdk-for-flutter-explore-routing-isoline-rangetype</a>
→ <a href="../routing/IsolineRangeType.html">/sdk-for-flutter-explore-routing-isolinerangetype</a>
</dt>
<dd>
  Specifies the type of the restriction that was used to calculate this isoline.
Gets the type of the restriction that was used to calculate this isoline.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="rangeValue">
<a href="../routing/Isoline/rangeValue.html">/sdk-for-flutter-explore-routing-isoline-rangevalue</a>
→ double
</dt>
<dd>
  Specifies the numerical value of the restriction that was used to calculate this isoline.
Gets the numerical value of the restriction that was used to calculate this isoline.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/Isoline/runtimeType.html">/sdk-for-flutter-explore-routing-isoline-runtimetype</a>
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
<a href="../routing/Isoline/noSuchMethod.html">/sdk-for-flutter-explore-routing-isoline-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/Isoline/toString.html">/sdk-for-flutter-explore-routing-isoline-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../routing/Isoline/operator_equals.html">/sdk-for-flutter-explore-routing-isoline-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
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
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">Isoline class</li>
</ol>
<h5>routing library</h5>
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

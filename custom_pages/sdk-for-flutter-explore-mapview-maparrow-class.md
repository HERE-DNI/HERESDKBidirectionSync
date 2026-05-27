---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-maparrow-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapArrow-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapArrow-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapArrow/MapArrow.html">MapArrow</a></li>
<li class="section-title">
<a href="mapview/MapArrow-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapArrow/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapArrow/measureDependentTailWidth.html">measureDependentTailWidth</a></li>
<li class="inherited"><a href="mapview/MapArrow/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/MapArrow/visibilityRanges.html">visibilityRanges</a></li>
<li class="section-title inherited"><a href="mapview/MapArrow-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapArrow/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapArrow/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapArrow-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapArrow/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapArrow class</li>
</ol>
<div class="self-name">MapArrow</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapArrow-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapArrow class abstract</h1></div>
<section class="desc markdown">
<p>A visual representation of an arrow on the map.</p>
<p>It consists of a tail - a polyline with an arbitrary
number of points - and a head at its end.</p>
<p>The map arrows are only visible on zoom levels &gt;= 13.</p>
<p>Altitude component of <code>GeoPolyline</code>'s vertices is ignored.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapArrow">
<a href="../mapview/MapArrow/MapArrow.html">/sdk-for-flutter-explore-mapview-maparrow-maparrow</a>(<a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a> geometry, double widthInPixels, Color color)
</dt>
<dd>
          Creates a new <code>MapArrow</code> instance.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapArrow/hashCode.html">/sdk-for-flutter-explore-mapview-maparrow-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="measureDependentTailWidth">
<a href="../mapview/MapArrow/measureDependentTailWidth.html">/sdk-for-flutter-explore-mapview-maparrow-measuredependenttailwidth</a>
↔ Map&lt;<wbr/><a href="../mapview/MapMeasure-class.html">/sdk-for-flutter-explore-mapview-mapmeasure-class</a>, double&gt;
</dt>
<dd>
  The width of the arrow tail in pixels, where the key is a <a href="../mapview/MapMeasure-class.html">/sdk-for-flutter-explore-mapview-mapmeasure-class</a> and the value is
a tail width in pixels at this <a href="../mapview/MapMeasure-class.html">/sdk-for-flutter-explore-mapview-mapmeasure-class</a>.
Gets the <a href="../mapview/MapMeasure-class.html">/sdk-for-flutter-explore-mapview-mapmeasure-class</a> dependent arrow tail width in pixels.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapArrow/runtimeType.html">/sdk-for-flutter-explore-mapview-maparrow-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="visibilityRanges">
<a href="../mapview/MapArrow/visibilityRanges.html">/sdk-for-flutter-explore-mapview-maparrow-visibilityranges</a>
↔ List&lt;<wbr/><a href="../mapview/MapMeasureRange-class.html">/sdk-for-flutter-explore-mapview-mapmeasurerange-class</a>&gt;
</dt>
<dd>
  The list of visibility ranges, in which the map arrow is visible.
A range is half-open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
is not contained in the range.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapArrow/noSuchMethod.html">/sdk-for-flutter-explore-mapview-maparrow-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapArrow/toString.html">/sdk-for-flutter-explore-mapview-maparrow-tostring</a>(<wbr/>)
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
<a href="../mapview/MapArrow/operator_equals.html">/sdk-for-flutter-explore-mapview-maparrow-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapArrow class</li>
</ol>
<h5>mapview library</h5>
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

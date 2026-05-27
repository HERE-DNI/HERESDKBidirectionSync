---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-polylinesimplifieroptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- PolylineSimplifierOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/PolylineSimplifierOptions-class.html#constructors">Constructors</a></li>
<li><a href="core/PolylineSimplifierOptions/PolylineSimplifierOptions.html">PolylineSimplifierOptions</a></li>
<li><a href="core/PolylineSimplifierOptions/PolylineSimplifierOptions.withMaxPointsAndTolerance.html">withMaxPointsAndTolerance</a></li>
<li class="section-title">
<a href="core/PolylineSimplifierOptions-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="core/PolylineSimplifierOptions/hashCode.html">hashCode</a></li>
<li><a href="core/PolylineSimplifierOptions/maxPoints.html">maxPoints</a></li>
<li class="inherited"><a href="core/PolylineSimplifierOptions/runtimeType.html">runtimeType</a></li>
<li><a href="core/PolylineSimplifierOptions/simplificationToleranceInMeters.html">simplificationToleranceInMeters</a></li>
<li class="section-title inherited"><a href="core/PolylineSimplifierOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core/PolylineSimplifierOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/PolylineSimplifierOptions/toString.html">toString</a></li>
<li class="section-title inherited"><a href="core/PolylineSimplifierOptions-class.html#operators">Operators</a></li>
<li class="inherited"><a href="core/PolylineSimplifierOptions/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="core/PolylineSimplifierOptions-class.html#static-properties">Static properties</a></li>
<li><a href="core/PolylineSimplifierOptions/simplificationInMeters14ZoomLevel.html">simplificationInMeters14ZoomLevel</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li class="self-crumb">PolylineSimplifierOptions class</li>
</ol>
<div class="self-name">PolylineSimplifierOptions</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/PolylineSimplifierOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PolylineSimplifierOptions class</h1></div>
<section class="desc markdown">
<p>Controls the strategy of <a href="../core/PolylineSimplifier/simplify.html">/sdk-for-flutter-explore-core-polylinesimplifier-simplify</a>
when reducing a size of polyline.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PolylineSimplifierOptions">
<a href="../core/PolylineSimplifierOptions/PolylineSimplifierOptions.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-polylinesimplifieroptions</a>()
</dt>
<dd>
          Creates default options with <a href="../core/PolylineSimplifierOptions/maxPoints.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-maxpoints</a> equal to 0 and
<a href="../core/PolylineSimplifierOptions/simplificationToleranceInMeters.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters</a> equal to <a href="../core/PolylineSimplifierOptions/simplificationInMeters14ZoomLevel.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationinmeters14zoomlevel</a>.
        </dd>
<dt class="callable" id="PolylineSimplifierOptions.withMaxPointsAndTolerance">
<a href="../core/PolylineSimplifierOptions/PolylineSimplifierOptions.withMaxPointsAndTolerance.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-polylinesimplifieroptions-withmaxpointsandtolerance</a>(int maxPoints, int simplificationToleranceInMeters)
</dt>
<dd>
          Creates options with explicitly specified <a href="../core/PolylineSimplifierOptions/maxPoints.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-maxpoints</a> and <a href="../core/PolylineSimplifierOptions/simplificationToleranceInMeters.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters</a>.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../core/PolylineSimplifierOptions/hashCode.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="maxPoints">
<a href="../core/PolylineSimplifierOptions/maxPoints.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-maxpoints</a>
↔ int
</dt>
<dd>
  Sets the upper limit on the resulting collection for
the <a href="../core/PolylineSimplifier/simplify.html">/sdk-for-flutter-explore-core-polylinesimplifier-simplify</a>. Lower
value results in the lower accuracy of the resulting
polyline. If <code>maxPoints</code> is less than <code>2</code>
then resulting polyline will not have an upper limit
on the size and only <a href="../core/PolylineSimplifierOptions/simplificationToleranceInMeters.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters</a>
will be considered. When <code>maxPoints</code> is greater than
size of the passed polyline then simplification algorithm
will take into account only <a href="../core/PolylineSimplifierOptions/simplificationToleranceInMeters.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core/PolylineSimplifierOptions/runtimeType.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="simplificationToleranceInMeters">
<a href="../core/PolylineSimplifierOptions/simplificationToleranceInMeters.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters</a>
↔ int
</dt>
<dd>
  Sets the accuracy limit for the <a href="../core/PolylineSimplifier/simplify.html">/sdk-for-flutter-explore-core-polylinesimplifier-simplify</a>:
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../core/PolylineSimplifierOptions/noSuchMethod.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core/PolylineSimplifierOptions/toString.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-tostring</a>(<wbr/>)
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
<a href="../core/PolylineSimplifierOptions/operator_equals.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-properties">
<h2>Static Properties</h2>
<dl class="properties">
<dt class="property" id="simplificationInMeters14ZoomLevel">
<a href="../core/PolylineSimplifierOptions/simplificationInMeters14ZoomLevel.html">/sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationinmeters14zoomlevel</a>
→ int
</dt>
<dd>
  Value for simplification tolerance for 14 zoom level without significant artifacts.
  <div class="features">final</div>
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
<li class="self-crumb">PolylineSimplifierOptions class</li>
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

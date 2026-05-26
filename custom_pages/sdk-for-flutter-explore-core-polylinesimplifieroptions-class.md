---
title: "PolylineSimplifierOptions class"
slug: "sdk-for-flutter-explore-core-polylinesimplifieroptions-class"
---

<HTMLBlock>{
`
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
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
<p>Controls the strategy of /sdk-for-flutter-explore-core-polylinesimplifier-simplify
when reducing a size of polyline.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PolylineSimplifierOptions">
/sdk-for-flutter-explore-core-polylinesimplifieroptions-polylinesimplifieroptions()
</dt>
<dd>
          Creates default options with /sdk-for-flutter-explore-core-polylinesimplifieroptions-maxpoints equal to 0 and
/sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters equal to /sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationinmeters14zoomlevel.
        </dd>
<dt class="callable" id="PolylineSimplifierOptions.withMaxPointsAndTolerance">
/sdk-for-flutter-explore-core-polylinesimplifieroptions-polylinesimplifieroptions-withmaxpointsandtolerance(int maxPoints, int simplificationToleranceInMeters)
</dt>
<dd>
          Creates options with explicitly specified /sdk-for-flutter-explore-core-polylinesimplifieroptions-maxpoints and /sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-core-polylinesimplifieroptions-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="maxPoints">
/sdk-for-flutter-explore-core-polylinesimplifieroptions-maxpoints
↔ int
</dt>
<dd>
  Sets the upper limit on the resulting collection for
the /sdk-for-flutter-explore-core-polylinesimplifier-simplify. Lower
value results in the lower accuracy of the resulting
polyline. If <code>maxPoints</code> is less than <code>2</code>
then resulting polyline will not have an upper limit
on the size and only /sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters
will be considered. When <code>maxPoints</code> is greater than
size of the passed polyline then simplification algorithm
will take into account only /sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-core-polylinesimplifieroptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="simplificationToleranceInMeters">
/sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters
↔ int
</dt>
<dd>
  Sets the accuracy limit for the /sdk-for-flutter-explore-core-polylinesimplifier-simplify:
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-core-polylinesimplifieroptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-core-polylinesimplifieroptions-tostring(<wbr/>)
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
/sdk-for-flutter-explore-core-polylinesimplifieroptions-operator-equals(<wbr/>Object other)
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
/sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationinmeters14zoomlevel
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
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
`
}</HTMLBlock>

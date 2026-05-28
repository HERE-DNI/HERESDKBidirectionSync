---
title: "PolylineSimplifier class abstract"
slug: "sdk-for-flutter-navigate-core-polylinesimplifier-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolylineSimplifier-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/PolylineSimplifier-class.html#constructors">Constructors</a></li>
<li><a href="core/PolylineSimplifier/PolylineSimplifier.html">PolylineSimplifier</a></li>
<li class="section-title inherited">
<a href="core/PolylineSimplifier-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="core/PolylineSimplifier/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="core/PolylineSimplifier/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="core/PolylineSimplifier-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core/PolylineSimplifier/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="core/PolylineSimplifier/simplify.html">simplify</a></li>
<li class="inherited"><a href="core/PolylineSimplifier/toString.html">toString</a></li>
<li class="section-title inherited"><a href="core/PolylineSimplifier-class.html#operators">Operators</a></li>
<li class="inherited"><a href="core/PolylineSimplifier/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li class="self-crumb">PolylineSimplifier class</li>
</ol>
<div class="self-name">PolylineSimplifier</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/PolylineSimplifier-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PolylineSimplifier class abstract</h1></div>
<section class="desc markdown">
<p>PolylineSimplifier helps to reduce the number of points
in the polyline by removing redundant elements using
Douglas–Peucker algorithm, so that result stays
within /sdk-for-flutter-navigate-core-polylinesimplifieroptions-class.</p>
<p>Typical use case is to perform input preparation step
before invoking computationally heavy API. Such API
have an upper limit on the input collection size
and is subject to reduced performance when collection
is huge. Examples of such API are:</p>
<ul>
<li><code>TrafficEngine</code> methods which accept a <code>GeoCorridor</code>;</li>
<li><code>RoutePrefetcher.prefetchGeoCorridor</code>.</li>
</ul>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PolylineSimplifier">
/sdk-for-flutter-navigate-core-polylinesimplifier-polylinesimplifier()
</dt>
<dd>
          Creates a new instance of /sdk-for-flutter-navigate-core-polylinesimplifier-class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-core-polylinesimplifier-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-polylinesimplifier-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-core-polylinesimplifier-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="simplify">
/sdk-for-flutter-navigate-core-polylinesimplifier-simplify(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt; polyline, /sdk-for-flutter-navigate-core-polylinesimplifieroptions-class simplificationParameters, /sdk-for-flutter-navigate-core-polylinesimplificationcallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Reduces the number of points in the input polyline.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-core-polylinesimplifier-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-core-polylinesimplifier-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li class="self-crumb">PolylineSimplifier class</li>
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

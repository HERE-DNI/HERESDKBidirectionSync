---
title: "RouteOffset class"
slug: "sdk-for-flutter-navigate-routing-routeoffset-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RouteOffset-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/RouteOffset-class.html#constructors">Constructors</a></li>
<li><a href="routing/RouteOffset/RouteOffset.html">RouteOffset</a></li>
<li class="section-title">
<a href="routing/RouteOffset-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="routing/RouteOffset/hashCode.html">hashCode</a></li>
<li><a href="routing/RouteOffset/offsetInMeters.html">offsetInMeters</a></li>
<li class="inherited"><a href="routing/RouteOffset/runtimeType.html">runtimeType</a></li>
<li><a href="routing/RouteOffset/sectionIndex.html">sectionIndex</a></li>
<li class="section-title inherited"><a href="routing/RouteOffset-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/RouteOffset/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/RouteOffset/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/RouteOffset-class.html#operators">Operators</a></li>
<li class="inherited"><a href="routing/RouteOffset/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">RouteOffset class</li>
</ol>
<div class="self-name">RouteOffset</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RouteOffset-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RouteOffset class</h1></div>
<section class="desc markdown">
<p>Represents a specific location along the route.</p>
<p>A <code>RouteOffset</code> is a location on the route defined by the section index and the distance in meters from the start of that section to the specified location on the route.
An offset in meters indicates the distance that needs to be traveled to reach a specific location along the route, such as a railway crossing.
For the latter case, the location of a railway crossing can be retrieved from <code>RouteRailwayCrossing.coordinates</code>.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RouteOffset">
/sdk-for-flutter-navigate-routing-routeoffset-routeoffset(int sectionIndex, double offsetInMeters)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-routing-routeoffset-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="offsetInMeters">
/sdk-for-flutter-navigate-routing-routeoffset-offsetinmeters
↔ double
</dt>
<dd>
  Offset from the start of the indexed /sdk-for-flutter-navigate-routing-section-class to the specified location along the route.
The maximum possible offset is limited by the length of the section and cannot exceed it.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-routeoffset-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sectionIndex">
/sdk-for-flutter-navigate-routing-routeoffset-sectionindex
↔ int
</dt>
<dd>
  Index of the corresponding route /sdk-for-flutter-navigate-routing-section-class. The start of the section indicates the start of the offset.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-routeoffset-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-routeoffset-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-routeoffset-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">RouteOffset class</li>
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
`
}</HTMLBlock>

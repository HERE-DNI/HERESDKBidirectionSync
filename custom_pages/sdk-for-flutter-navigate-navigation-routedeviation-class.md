---
title: "RouteDeviation class"
slug: "sdk-for-flutter-navigate-navigation-routedeviation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RouteDeviation-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/RouteDeviation-class.html#constructors">Constructors</a></li>
<li><a href="navigation/RouteDeviation/RouteDeviation.withTraveledDistance.html">withTraveledDistance</a></li>
<li class="section-title">
<a href="navigation/RouteDeviation-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/RouteDeviation/currentLocation.html">currentLocation</a></li>
<li><a href="navigation/RouteDeviation/hashCode.html">hashCode</a></li>
<li><a href="navigation/RouteDeviation/lastLocationOnRoute.html">lastLocationOnRoute</a></li>
<li><a href="navigation/RouteDeviation/lastTraveledSectionIndex.html">lastTraveledSectionIndex</a></li>
<li class="inherited"><a href="navigation/RouteDeviation/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/RouteDeviation/traveledDistanceOnLastSectionInMeters.html">traveledDistanceOnLastSectionInMeters</a></li>
<li class="section-title inherited"><a href="navigation/RouteDeviation-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/RouteDeviation/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/RouteDeviation/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/RouteDeviation-class.html#operators">Operators</a></li>
<li><a href="navigation/RouteDeviation/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">RouteDeviation class</li>
</ol>
<div class="self-name">RouteDeviation</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RouteDeviation-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RouteDeviation class</h1></div>
<section class="desc markdown">
<p>Contains all the relevant information on a deviation from the route.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RouteDeviation.withTraveledDistance">
/sdk-for-flutter-navigate-navigation-routedeviation-routedeviation-withtraveleddistance(/sdk-for-flutter-navigate-navigation-navigablelocation-class? lastLocationOnRoute, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, /sdk-for-flutter-navigate-navigation-navigablelocation-class currentLocation)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="currentLocation">
/sdk-for-flutter-navigate-navigation-routedeviation-currentlocation
↔ /sdk-for-flutter-navigate-navigation-navigablelocation-class
</dt>
<dd>
  The current location.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-routedeviation-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lastLocationOnRoute">
/sdk-for-flutter-navigate-navigation-routedeviation-lastlocationonroute
↔ /sdk-for-flutter-navigate-navigation-navigablelocation-class?
</dt>
<dd>
  The last known location on the route.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lastTraveledSectionIndex">
/sdk-for-flutter-navigate-navigation-routedeviation-lasttraveledsectionindex
↔ int
</dt>
<dd>
  Indicates the index of the last traveled route section.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-routedeviation-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="traveledDistanceOnLastSectionInMeters">
/sdk-for-flutter-navigate-navigation-routedeviation-traveleddistanceonlastsectioninmeters
↔ int
</dt>
<dd>
  Offset in meter to the last visited position on the route section defined by the last traveled section index.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-routedeviation-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-routedeviation-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-routedeviation-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">RouteDeviation class</li>
</ol>
<h5>navigation library</h5>
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

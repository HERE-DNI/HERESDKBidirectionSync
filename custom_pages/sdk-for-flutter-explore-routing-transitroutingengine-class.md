---
title: "TransitRoutingEngine class abstract"
slug: "sdk-for-flutter-explore-routing-transitroutingengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TransitRoutingEngine-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/TransitRoutingEngine-class.html#constructors">Constructors</a></li>
<li><a href="routing/TransitRoutingEngine/TransitRoutingEngine.html">TransitRoutingEngine</a></li>
<li><a href="routing/TransitRoutingEngine/TransitRoutingEngine.withSdkEngine.html">withSdkEngine</a></li>
<li class="section-title inherited">
<a href="routing/TransitRoutingEngine-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="routing/TransitRoutingEngine/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="routing/TransitRoutingEngine/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="routing/TransitRoutingEngine-class.html#instance-methods">Methods</a></li>
<li><a href="routing/TransitRoutingEngine/calculateRoute.html">calculateRoute</a></li>
<li class="inherited"><a href="routing/TransitRoutingEngine/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/TransitRoutingEngine/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/TransitRoutingEngine-class.html#operators">Operators</a></li>
<li class="inherited"><a href="routing/TransitRoutingEngine/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">TransitRoutingEngine class</li>
</ol>
<div class="self-name">TransitRoutingEngine</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TransitRoutingEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TransitRoutingEngine class abstract</h1></div>
<section class="desc markdown">
<p>Use the TransitRoutingEngine to calculate a public transit route from A to B with
a number of waypoints in between.</p>
<p>Route calculation is done asynchronously and requires an
online connection. The resulting route contains various
information such as the polyline, route length in meters,
estimated time to traverse along the route and maneuver data.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TransitRoutingEngine">
/sdk-for-flutter-explore-routing-transitroutingengine-transitroutingengine()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="TransitRoutingEngine.withSdkEngine">
/sdk-for-flutter-explore-routing-transitroutingengine-transitroutingengine-withsdkengine(/sdk-for-flutter-explore-core-engine-sdknativeengine-class sdkEngine)
</dt>
<dd>
          Creates a new instance of TransitRoutingEngine.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-routing-transitroutingengine-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-transitroutingengine-runtimetype
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
<dt class="callable" id="calculateRoute">
/sdk-for-flutter-explore-routing-transitroutingengine-calculateroute(<wbr/>/sdk-for-flutter-explore-routing-transitwaypoint-class startingPoint, /sdk-for-flutter-explore-routing-transitwaypoint-class destination, /sdk-for-flutter-explore-routing-transitrouteoptions-class routeOptions, /sdk-for-flutter-explore-routing-calculateroutecallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates a public transit route from the origin to the destination.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-routing-transitroutingengine-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-transitroutingengine-tostring(<wbr/>)
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
/sdk-for-flutter-explore-routing-transitroutingengine-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">TransitRoutingEngine class</li>
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

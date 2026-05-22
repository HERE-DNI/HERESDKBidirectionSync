---
title: "Untitled"
slug: "sdk-for-flutter-navigate-venue-routing-indoorroutingengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IndoorRoutingEngine-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li class="self-crumb">IndoorRoutingEngine class</li>
</ol>
<div class="self-name">IndoorRoutingEngine</div>
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
<div class="main-content" data-above-sidebar="venue.routing/venue.routing-library-sidebar.html" data-below-sidebar="venue.routing/IndoorRoutingEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>IndoorRoutingEngine class abstract</h1></div>
<section class="desc markdown">
<p>Use the IndoorRoutingEngine to calculate a route inside a venue.</p>
<br/>
Route calculation is done asynchronously and requires an
internet connection. The resulting route contains various
information such as the polyline, route length in meters,
estimated time to traverse along the route and maneuver data.
<br/>
Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.
Currently, the indoor route calculation may not be accurate so that e.g. a pedestrian
end user might be routed via a vehicle access and route or similar. Therefore end users
must use this feature with caution and always be aware of the surroundings. The signs
and instructions given at the premises must be observed. You are required to inform
the end user about this in an appropriate manner, whether in the UI of your application,
your end user terms or similar.
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="IndoorRoutingEngine">
/sdk-for-flutter-navigate-venue-routing-indoorroutingengine-indoorroutingengine(/sdk-for-flutter-navigate-venue-service-venueservice-class venueService)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-venue-routing-indoorroutingengine-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-venue-routing-indoorroutingengine-runtimetype
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
/sdk-for-flutter-navigate-venue-routing-indoorroutingengine-calculateroute(<wbr/>/sdk-for-flutter-navigate-venue-routing-indoorwaypoint-class from, /sdk-for-flutter-navigate-venue-routing-indoorwaypoint-class to, /sdk-for-flutter-navigate-venue-routing-indoorrouteoptions-class routeOptions, /sdk-for-flutter-navigate-venue-routing-calculateindoorroutecallback callback)
    → void

</dt>
<dd>
  Asynchronously calculates a route inside a venue.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-venue-routing-indoorroutingengine-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-venue-routing-indoorroutingengine-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-venue-routing-indoorroutingengine-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li class="self-crumb">IndoorRoutingEngine class</li>
</ol>
<h5>venue.routing library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>

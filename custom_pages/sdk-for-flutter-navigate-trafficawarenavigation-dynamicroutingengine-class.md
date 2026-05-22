---
title: "Untitled"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DynamicRoutingEngine-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li class="self-crumb">DynamicRoutingEngine class</li>
</ol>
<div class="self-name">DynamicRoutingEngine</div>
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
<div class="main-content" data-above-sidebar="trafficawarenavigation/trafficawarenavigation-library-sidebar.html" data-below-sidebar="trafficawarenavigation/DynamicRoutingEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>DynamicRoutingEngine class abstract</h1></div>
<section class="desc markdown">
<p>This class queries the HERE routing backend
to find routes with less traffic and therefore an earlier remaining estimated time of arrival.</p>
<p>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class polls the HERE routing backend periodically to find the best new route out
of a given initial route.
For initial route calculation it is recommended to use the /sdk-for-flutter-navigate-routing-routingengine-class
as it already requests traffic-optimized routes.</p>
<p>When a better route is found, it is recommended to follow these steps to set the new route:</p>
<ol>
<li>Stop the /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class.</li>
<li>Update the currently active <code>Navigator</code>instance with the newly found route.</li>
<li>Restart the /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class. This should be done outside of the <code>onBetterRouteFound()</code> callback.</li>
</ol>
<p>For both /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class and /sdk-for-flutter-navigate-routing-routingengine-class,
the resulting routes are optimized based on speed flow changes such as traffic jams,
street closures or road accidents.
To get the best result, it is recommended to not specify the
/sdk-for-flutter-navigate-routing-routeoptions-departuretime as then the current time is used by default.</p>
<p>The poll interval is defined by
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-pollinterval and
triggered by /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-updatecurrentlocation.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="DynamicRoutingEngine">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-dynamicroutingengine(/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class? options)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="DynamicRoutingEngine.withSdkEngine">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-dynamicroutingengine-withsdkengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class? options)
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
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-runtimetype
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
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="start">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-start(<wbr/>/sdk-for-flutter-navigate-routing-route-class route, /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class listener)
    → void

</dt>
<dd>
  Starts polling the HERE backend services to find a better route,
as defined by the DynamicRoutingEngineOptions.
  

</dd>
<dt class="callable" id="startWithWaypoints">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-startwithwaypoints(<wbr/>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-refreshrouteoptions-class refreshRouteOptions, /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class listener)
    → void

</dt>
<dd>
  Starts polling the HERE backend services to find a better route,
as defined by the /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class.
  

</dd>
<dt class="callable" id="startWithWaypointsAndRoutingOptions">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-startwithwaypointsandroutingoptions(<wbr/>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-routingoptions-class routingOptions, /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class listener)
    → void

</dt>
<dd>
  Starts polling the HERE backend services to find a better route,
as defined by the /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class.
  

</dd>
<dt class="callable" id="stop">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-stop(<wbr/>)
    → void

</dt>
<dd>
  Stops polling the HERE backend services.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="updateCurrentLocation">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-updatecurrentlocation(<wbr/>/sdk-for-flutter-navigate-navigation-mapmatchedlocation-class mapMatchedLocation, int sectionIndex)
    → void

</dt>
<dd>
  Updates the current location.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li class="self-crumb">DynamicRoutingEngine class</li>
</ol>
<h5>trafficawarenavigation library</h5>
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

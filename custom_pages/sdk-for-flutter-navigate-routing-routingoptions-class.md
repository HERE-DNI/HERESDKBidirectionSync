---
title: "RoutingOptions class"
slug: "sdk-for-flutter-navigate-routing-routingoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoutingOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/RoutingOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/RoutingOptions/RoutingOptions.html">RoutingOptions</a></li>
<li class="section-title">
<a href="routing/RoutingOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/RoutingOptions/allowOptions.html">allowOptions</a></li>
<li><a href="routing/RoutingOptions/avoidanceOptions.html">avoidanceOptions</a></li>
<li><a href="routing/RoutingOptions/evOptions.html">evOptions</a></li>
<li><a href="routing/RoutingOptions/hashCode.html">hashCode</a></li>
<li><a href="routing/RoutingOptions/maxSpeedOnSegments.html">maxSpeedOnSegments</a></li>
<li><a href="routing/RoutingOptions/routeOptions.html">routeOptions</a></li>
<li class="inherited"><a href="routing/RoutingOptions/runtimeType.html">runtimeType</a></li>
<li><a href="routing/RoutingOptions/textOptions.html">textOptions</a></li>
<li><a href="routing/RoutingOptions/tollOptions.html">tollOptions</a></li>
<li><a href="routing/RoutingOptions/transportSpecification.html">transportSpecification</a></li>
<li class="section-title inherited"><a href="routing/RoutingOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/RoutingOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/RoutingOptions/toString.html">toString</a></li>
<li class="section-title"><a href="routing/RoutingOptions-class.html#operators">Operators</a></li>
<li><a href="routing/RoutingOptions/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="routing/RoutingOptions-class.html#static-methods">Static methods</a></li>
<li><a href="routing/RoutingOptions/fromDefaultParameterConfiguration.html">fromDefaultParameterConfiguration</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">RoutingOptions class</li>
</ol>
<div class="self-name">RoutingOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RoutingOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RoutingOptions class</h1></div>
<section class="desc markdown">
<p>The options defines how a route should be calculated.</p>
<p>The options are used for all transport modes and engines.</p>
<p>** Electric vehicle specific requirements **
Electric vehicle consumption are estimated when at least one consumption model is defined.
Currently two models are supported:</p>
<ul>
<li>PhysicalConsumptionModel
Aside from the values in PhysicalConsumptionModel additionally these values needs to be defined:
<ul>
<li>/sdk-for-flutter-navigate-transport-vehiclespecification-currentweightinkilograms from /sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification
from /sdk-for-flutter-navigate-routing-routingoptions-transportspecification</li>
<li>Additionally /sdk-for-flutter-navigate-routing-waypoint-currentweightchangeinkilograms can be defined.</li>
</ul>
</li>
<li>EmpiricalConsumptionModel</li>
</ul>
<p>By setting /sdk-for-flutter-navigate-routing-electricvehicleoptions-ensurereachability the <code>RoutingEngine</code> inserts additional charging stations
to reach the waypoints.
This feature requires setting the /sdk-for-flutter-navigate-routing-batteryspecifications-class.
By default a vehicle might not reach the waypoint, when the initial charge is not enough to reach all waypoints.
See the parameter description below for more details.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RoutingOptions">
/sdk-for-flutter-navigate-routing-routingoptions-routingoptions()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="allowOptions">
/sdk-for-flutter-navigate-routing-routingoptions-allowoptions
↔ /sdk-for-flutter-navigate-routing-allowoptions-class
</dt>
<dd>
  The options explicitly allowed by user for route calculations.
By default no options are opt in.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidanceOptions">
/sdk-for-flutter-navigate-routing-routingoptions-avoidanceoptions
↔ /sdk-for-flutter-navigate-routing-avoidanceoptions-class
</dt>
<dd>
  Options to specify restrictions for route calculations.
By default no restrictions are applied.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="evOptions">
/sdk-for-flutter-navigate-routing-routingoptions-evoptions
↔ /sdk-for-flutter-navigate-routing-electricvehicleoptions-class?
</dt>
<dd>
  Defines the electric vehicle (EV) related parameters to calculate the consumption and reachability.
When no EV options are defined an internal combustion engine is assumed.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-routing-routingoptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="maxSpeedOnSegments">
/sdk-for-flutter-navigate-routing-routingoptions-maxspeedonsegments
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-maxspeedonsegment-class&gt;
</dt>
<dd>
  Segments with restriction on maximum /sdk-for-flutter-navigate-routing-dynamicspeedinfo-basespeedinmeterspersecond.
<strong>Note</strong> Not used for offline calculations.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routeOptions">
/sdk-for-flutter-navigate-routing-routingoptions-routeoptions
↔ /sdk-for-flutter-navigate-routing-routeoptions-class
</dt>
<dd>
  Specifies the common route calculation options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-routingoptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="textOptions">
/sdk-for-flutter-navigate-routing-routingoptions-textoptions
↔ /sdk-for-flutter-navigate-routing-routetextoptions-class
</dt>
<dd>
  Customize textual content returned from the route calculation, such
as localization, format, and unit system.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tollOptions">
/sdk-for-flutter-navigate-routing-routingoptions-tolloptions
↔ /sdk-for-flutter-navigate-routing-tolloptions-class
</dt>
<dd>
  Options to specify how the tolls should be calculated,
such as transponders, vehicle category, and emission type.
<strong>Note</strong> Not used for offline calculations.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="transportSpecification">
/sdk-for-flutter-navigate-routing-routingoptions-transportspecification
↔ /sdk-for-flutter-navigate-transport-transportspecification-class
</dt>
<dd>
  Defines the transport specification which contains the transport mode and the vehicle specifications
for the transport mode chosen.
<strong>Notes:</strong>
<div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-routingoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-routingoptions-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-routingoptions-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="fromDefaultParameterConfiguration">
/sdk-for-flutter-navigate-routing-routingoptions-fromdefaultparameterconfiguration(<wbr/>)
    → /sdk-for-flutter-navigate-routing-routingoptions-class

</dt>
<dd>
  Returns the default configuration for the transport specification selected in /sdk-for-flutter-navigate-core-parameterconfiguration-transportspecification
from /sdk-for-flutter-navigate-core-engine-sdknativeengine-parameterconfig.
  

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
<li class="self-crumb">RoutingOptions class</li>
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

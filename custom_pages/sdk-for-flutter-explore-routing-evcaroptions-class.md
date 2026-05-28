---
title: "EVCarOptions class"
slug: "sdk-for-flutter-explore-routing-evcaroptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVCarOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/EVCarOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/EVCarOptions/EVCarOptions.html">EVCarOptions</a></li>
<li class="section-title">
<a href="routing/EVCarOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/EVCarOptions/allowOptions.html">allowOptions</a></li>
<li><a href="routing/EVCarOptions/avoidanceOptions.html">avoidanceOptions</a></li>
<li><a href="routing/EVCarOptions/batterySpecifications.html">batterySpecifications</a></li>
<li><a href="routing/EVCarOptions/carSpecifications.html">carSpecifications</a></li>
<li><a href="routing/EVCarOptions/consumptionModel.html">consumptionModel</a></li>
<li><a href="routing/EVCarOptions/ensureReachability.html">ensureReachability</a></li>
<li><a href="routing/EVCarOptions/evMobilityServiceProviderPreferences.html">evMobilityServiceProviderPreferences</a></li>
<li><a href="routing/EVCarOptions/hashCode.html">hashCode</a></li>
<li><a href="routing/EVCarOptions/lastCharacterOfLicensePlate.html">lastCharacterOfLicensePlate</a></li>
<li><a href="routing/EVCarOptions/maxSpeedOnSegments.html">maxSpeedOnSegments</a></li>
<li><a href="routing/EVCarOptions/occupantsNumber.html">occupantsNumber</a></li>
<li><a href="routing/EVCarOptions/routeOptions.html">routeOptions</a></li>
<li class="inherited"><a href="routing/EVCarOptions/runtimeType.html">runtimeType</a></li>
<li><a href="routing/EVCarOptions/textOptions.html">textOptions</a></li>
<li><a href="routing/EVCarOptions/tollOptions.html">tollOptions</a></li>
<li class="section-title inherited"><a href="routing/EVCarOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/EVCarOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/EVCarOptions/toString.html">toString</a></li>
<li class="section-title"><a href="routing/EVCarOptions-class.html#operators">Operators</a></li>
<li><a href="routing/EVCarOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">EVCarOptions class</li>
</ol>
<div class="self-name">EVCarOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/EVCarOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVCarOptions class</h1></div>
<section class="desc markdown">
<p>All the options to specify how a route for an electric car should be calculated.</p>
<p>At minimum, a valid /sdk-for-flutter-explore-routing-evconsumptionmodel-class must be set or the route calculation will fail.
<br/>
Note: /sdk-for-flutter-explore-routing-evcaroptions-ensurereachability must be <code>true</code> to make sure that all stopovers are reachable. For this,
charging stations may be added to the route. If /sdk-for-flutter-explore-routing-evcaroptions-ensurereachability is true, you need to
specify the required route options and battery specifications that include the current charge level
of the battery (/sdk-for-flutter-explore-routing-batteryspecifications-initialchargeinkilowatthours).
See the parameter description below for more details.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Annotations</dt>
<dd>
<ul class="annotation-list clazz-relationships">
<li>@Deprecated("Will be removed in v4.28.0. Use RoutingOptions class instead.")</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVCarOptions">
/sdk-for-flutter-explore-routing-evcaroptions-evcaroptions()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="allowOptions">
/sdk-for-flutter-explore-routing-evcaroptions-allowoptions
↔ /sdk-for-flutter-explore-routing-allowoptions-class
</dt>
<dd>
  The options explicitly allowed by user for route calculations. By default
no options are opt in.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidanceOptions">
/sdk-for-flutter-explore-routing-evcaroptions-avoidanceoptions
↔ /sdk-for-flutter-explore-routing-avoidanceoptions-class
</dt>
<dd>
  Options to specify restrictions for route calculations. By default
no restrictions are applied.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="batterySpecifications">
/sdk-for-flutter-explore-routing-evcaroptions-batteryspecifications
↔ /sdk-for-flutter-explore-routing-batteryspecifications-class
</dt>
<dd>
  Parameters that describe the electric vehicle's battery.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="carSpecifications">
/sdk-for-flutter-explore-routing-evcaroptions-carspecifications
↔ /sdk-for-flutter-explore-transport-carspecifications-class
</dt>
<dd>
  Detailed car specifications such as dimensions and weight.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="consumptionModel">
/sdk-for-flutter-explore-routing-evcaroptions-consumptionmodel
↔ /sdk-for-flutter-explore-routing-evconsumptionmodel-class
</dt>
<dd>
  Vehicle specific parameters, which are then used to calculate energy consumption
for the vehicle on a given route.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="ensureReachability">
/sdk-for-flutter-explore-routing-evcaroptions-ensurereachability
↔ bool
</dt>
<dd>
  Ensure that the vehicle does not run out of energy along the way.
Requires valid /sdk-for-flutter-explore-routing-evcaroptions-batteryspecifications.
It also requires that
/sdk-for-flutter-explore-routing-routeoptions-optimizationmode = /sdk-for-flutter-explore-routing-optimizationmode,
/sdk-for-flutter-explore-routing-routeoptions-speedcapinmeterspersecond is not set, and
/sdk-for-flutter-explore-routing-avoidanceoptions-class is empty. Otherwise, this object is considered invalid.
Setting this flag enables calculation of a route optimized for electric vehicles.
Charging stations may be added along the route to ensure that the vehicle does
not run out of energy along the way.
It is especially useful for longer routes, because after all, charging stations are much
less common than petrol stations.
<strong>Note</strong> An <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> is generated when
the <code>sdk.routing.EVCarOptions.ensure_reachability</code> is set to <code>true</code> in case <code>sdk.routing.RoutingEngine.import_route</code> is called.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="evMobilityServiceProviderPreferences">
/sdk-for-flutter-explore-routing-evcaroptions-evmobilityserviceproviderpreferences
↔ /sdk-for-flutter-explore-routing-evmobilityserviceproviderpreferences-class
</dt>
<dd>
  Defines the preferred E-Mobility Service Providers.
The The E-Mobility Service Provider Partner Ids can be received from
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html</a>
An alternative way to get <code>partnerId</code> is the <code>eMobilityServiceProviders.partnerId</code> as part of <code>HERE SDK Search</code>.
Maximum number of E-Mobility Service Providers is limited to 10.
By default, all providers are used.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-routing-evcaroptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lastCharacterOfLicensePlate">
/sdk-for-flutter-explore-routing-evcaroptions-lastcharacteroflicenseplate
↔ String?
</dt>
<dd>
  Specifies the last character of a vehicle's license plate, typically used to
evaluate traffic restrictions in certain environmental or low-emission zones.
In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may
be restricted on certain days or in certain areas to reduce congestion and emissions.
When this value is provided, the HERE SDK considers it during route calculation to
avoid roads or areas where your vehicle may be restricted based on local regulations.
Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxSpeedOnSegments">
/sdk-for-flutter-explore-routing-evcaroptions-maxspeedonsegments
↔ List&lt;<wbr/>/sdk-for-flutter-explore-routing-maxspeedonsegment-class&gt;
</dt>
<dd>
  Segments with restriction on maximum /sdk-for-flutter-explore-routing-dynamicspeedinfo-basespeedinmeterspersecond.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="occupantsNumber">
/sdk-for-flutter-explore-routing-evcaroptions-occupantsnumber
↔ int
</dt>
<dd>
  Specifies the number of occupants in the vehicle, including driver,
can affect the vehicle's ability to use HOV/carpool restricted lanes.
Shouldn't be less than 1 or greater than 255. Defaults to 1.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routeOptions">
/sdk-for-flutter-explore-routing-evcaroptions-routeoptions
↔ /sdk-for-flutter-explore-routing-routeoptions-class
</dt>
<dd>
  Specifies the common route calculation options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-evcaroptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="textOptions">
/sdk-for-flutter-explore-routing-evcaroptions-textoptions
↔ /sdk-for-flutter-explore-routing-routetextoptions-class
</dt>
<dd>
  Customize textual content returned from the route calculation, such
as localization, format, and unit system.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tollOptions">
/sdk-for-flutter-explore-routing-evcaroptions-tolloptions
↔ /sdk-for-flutter-explore-routing-tolloptions-class
</dt>
<dd>
  Options to specify how the tolls should be calculated,
such as transponders, vehicle category, and emission type.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-routing-evcaroptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-evcaroptions-tostring(<wbr/>)
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
/sdk-for-flutter-explore-routing-evcaroptions-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">EVCarOptions class</li>
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

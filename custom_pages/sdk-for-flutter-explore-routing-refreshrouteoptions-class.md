---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-refreshrouteoptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- RefreshRouteOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/RefreshRouteOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/RefreshRouteOptions/RefreshRouteOptions.withBicycleOptions.html">withBicycleOptions</a></li>
<li><a href="routing/RefreshRouteOptions/RefreshRouteOptions.withBusOptions.html">withBusOptions</a></li>
<li><a href="routing/RefreshRouteOptions/RefreshRouteOptions.withCarOptions.html">withCarOptions</a></li>
<li><a href="routing/RefreshRouteOptions/RefreshRouteOptions.withEVCarOptions.html">withEVCarOptions</a></li>
<li><a href="routing/RefreshRouteOptions/RefreshRouteOptions.withEVTruckOptions.html">withEVTruckOptions</a></li>
<li><a href="routing/RefreshRouteOptions/RefreshRouteOptions.withPedestrianOptions.html">withPedestrianOptions</a></li>
<li><a href="routing/RefreshRouteOptions/RefreshRouteOptions.withPrivateBusOptions.html">withPrivateBusOptions</a></li>
<li><a href="routing/RefreshRouteOptions/RefreshRouteOptions.withScooterOptions.html">withScooterOptions</a></li>
<li><a href="routing/RefreshRouteOptions/RefreshRouteOptions.withTaxiOptions.html">withTaxiOptions</a></li>
<li><a href="routing/RefreshRouteOptions/RefreshRouteOptions.withTransportMode.html">withTransportMode</a></li>
<li><a href="routing/RefreshRouteOptions/RefreshRouteOptions.withTruckOptions.html">withTruckOptions</a></li>
<li class="section-title inherited">
<a href="routing/RefreshRouteOptions-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="routing/RefreshRouteOptions/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="routing/RefreshRouteOptions/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="routing/RefreshRouteOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/RefreshRouteOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/RefreshRouteOptions/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/RefreshRouteOptions-class.html#operators">Operators</a></li>
<li class="inherited"><a href="routing/RefreshRouteOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">RefreshRouteOptions class</li>
</ol>
<div class="self-name">RefreshRouteOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RefreshRouteOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RefreshRouteOptions class abstract</h1></div>
<section class="desc markdown">
<p>The options to specify how to refresh an already calculated route identified by a <a href="../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a>.</p>
<p>All the
options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that
accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored:
<a href="../routing/RouteOptions/alternatives.html">/sdk-for-flutter-explore-routing-routeoptions-alternatives</a>, <a href="../routing/RouteOptions/arrivalTime.html">/sdk-for-flutter-explore-routing-routeoptions-arrivaltime</a>, and <a href="../routing/RouteOptions/optimizationMode.html">/sdk-for-flutter-explore-routing-routeoptions-optimizationmode</a>.
If new <a href="../routing/AvoidanceOptions-class.html">/sdk-for-flutter-explore-routing-avoidanceoptions-class</a> are specified, they are ignored as well and instead new <a href="../routing/SectionNotice-class.html">/sdk-for-flutter-explore-routing-sectionnotice-class</a>'s
are generated that indicate where the requested <a href="../routing/AvoidanceOptions-class.html">/sdk-for-flutter-explore-routing-avoidanceoptions-class</a> are violated. Note that when
<a href="../routing/EVCarOptions/ensureReachability.html">/sdk-for-flutter-explore-routing-evcaroptions-ensurereachability</a> is set to true, the route refresh request will fail as this option
is incompatible with a fixed route shape.
If any of the ignored options are important, consider calculating a new route instead.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Annotations</dt>
<dd>
<ul class="annotation-list clazz-relationships">
<li>@Deprecated("Will be removed in v4.28.0. Use the `RoutingOptions` class instead.")</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RefreshRouteOptions.withBicycleOptions">
<a href="../routing/RefreshRouteOptions/RefreshRouteOptions.withBicycleOptions.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withbicycleoptions</a>(<a class="deprecated" href="../routing/BicycleOptions-class.html">/sdk-for-flutter-explore-routing-bicycleoptions-class</a> bicycleOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with <a class="deprecated" href="../routing/BicycleOptions-class.html">/sdk-for-flutter-explore-routing-bicycleoptions-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withBusOptions">
<a href="../routing/RefreshRouteOptions/RefreshRouteOptions.withBusOptions.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withbusoptions</a>(<a class="deprecated" href="../routing/BusOptions-class.html">/sdk-for-flutter-explore-routing-busoptions-class</a> busOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with <a class="deprecated" href="../routing/BusOptions-class.html">/sdk-for-flutter-explore-routing-busoptions-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withCarOptions">
<a href="../routing/RefreshRouteOptions/RefreshRouteOptions.withCarOptions.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withcaroptions</a>(<a class="deprecated" href="../routing/CarOptions-class.html">/sdk-for-flutter-explore-routing-caroptions-class</a> carOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with <a class="deprecated" href="../routing/CarOptions-class.html">/sdk-for-flutter-explore-routing-caroptions-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withEVCarOptions">
<a href="../routing/RefreshRouteOptions/RefreshRouteOptions.withEVCarOptions.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withevcaroptions</a>(<a class="deprecated" href="../routing/EVCarOptions-class.html">/sdk-for-flutter-explore-routing-evcaroptions-class</a> evCarOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with <a class="deprecated" href="../routing/EVCarOptions-class.html">/sdk-for-flutter-explore-routing-evcaroptions-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withEVTruckOptions">
<a href="../routing/RefreshRouteOptions/RefreshRouteOptions.withEVTruckOptions.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withevtruckoptions</a>(<a class="deprecated" href="../routing/EVTruckOptions-class.html">/sdk-for-flutter-explore-routing-evtruckoptions-class</a> evTruckOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with <a class="deprecated" href="../routing/EVTruckOptions-class.html">/sdk-for-flutter-explore-routing-evtruckoptions-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withPedestrianOptions">
<a href="../routing/RefreshRouteOptions/RefreshRouteOptions.withPedestrianOptions.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withpedestrianoptions</a>(<a class="deprecated" href="../routing/PedestrianOptions-class.html">/sdk-for-flutter-explore-routing-pedestrianoptions-class</a> pedestrianOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with <a class="deprecated" href="../routing/PedestrianOptions-class.html">/sdk-for-flutter-explore-routing-pedestrianoptions-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withPrivateBusOptions">
<a href="../routing/RefreshRouteOptions/RefreshRouteOptions.withPrivateBusOptions.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withprivatebusoptions</a>(<a class="deprecated" href="../routing/PrivateBusOptions-class.html">/sdk-for-flutter-explore-routing-privatebusoptions-class</a> privateBusOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with <a class="deprecated" href="../routing/PrivateBusOptions-class.html">/sdk-for-flutter-explore-routing-privatebusoptions-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withScooterOptions">
<a href="../routing/RefreshRouteOptions/RefreshRouteOptions.withScooterOptions.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withscooteroptions</a>(<a class="deprecated" href="../routing/ScooterOptions-class.html">/sdk-for-flutter-explore-routing-scooteroptions-class</a> scooterOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with <a class="deprecated" href="../routing/ScooterOptions-class.html">/sdk-for-flutter-explore-routing-scooteroptions-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withTaxiOptions">
<a href="../routing/RefreshRouteOptions/RefreshRouteOptions.withTaxiOptions.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withtaxioptions</a>(<a class="deprecated" href="../routing/TaxiOptions-class.html">/sdk-for-flutter-explore-routing-taxioptions-class</a> taxiOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with <a class="deprecated" href="../routing/TaxiOptions-class.html">/sdk-for-flutter-explore-routing-taxioptions-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withTransportMode">
<a href="../routing/RefreshRouteOptions/RefreshRouteOptions.withTransportMode.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withtransportmode</a>(<a href="../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a> transportMode)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with <a href="../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withTruckOptions">
<a href="../routing/RefreshRouteOptions/RefreshRouteOptions.withTruckOptions.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withtruckoptions</a>(<a class="deprecated" href="../routing/TruckOptions-class.html">/sdk-for-flutter-explore-routing-truckoptions-class</a> truckOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with <a class="deprecated" href="../routing/TruckOptions-class.html">/sdk-for-flutter-explore-routing-truckoptions-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../routing/RefreshRouteOptions/hashCode.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/RefreshRouteOptions/runtimeType.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/RefreshRouteOptions/noSuchMethod.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/RefreshRouteOptions/toString.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-tostring</a>(<wbr/>)
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
<a href="../routing/RefreshRouteOptions/operator_equals.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">RefreshRouteOptions class</li>
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
</HTMLBlock>

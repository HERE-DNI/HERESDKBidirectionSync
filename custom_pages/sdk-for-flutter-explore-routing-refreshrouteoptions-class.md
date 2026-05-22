---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-refreshrouteoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RefreshRouteOptions-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
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
<p>The options to specify how to refresh an already calculated route identified by a /sdk-for-flutter-explore-routing-routehandle-class.</p>
<p>All the
options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that
accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored:
/sdk-for-flutter-explore-routing-routeoptions-alternatives, /sdk-for-flutter-explore-routing-routeoptions-arrivaltime, and /sdk-for-flutter-explore-routing-routeoptions-optimizationmode.
If new /sdk-for-flutter-explore-routing-avoidanceoptions-class are specified, they are ignored as well and instead new /sdk-for-flutter-explore-routing-sectionnotice-class's
are generated that indicate where the requested /sdk-for-flutter-explore-routing-avoidanceoptions-class are violated. Note that when
/sdk-for-flutter-explore-routing-evcaroptions-ensurereachability is set to true, the route refresh request will fail as this option
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
<li>@Deprecated("Will be removed in v4.28.0. Use the <code>RoutingOptions</code> class instead.")</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RefreshRouteOptions.withBicycleOptions">
/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withbicycleoptions(/sdk-for-flutter-explore-routing-bicycleoptions-class bicycleOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-routing-bicycleoptions-class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withBusOptions">
/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withbusoptions(/sdk-for-flutter-explore-routing-busoptions-class busOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-routing-busoptions-class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withCarOptions">
/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withcaroptions(/sdk-for-flutter-explore-routing-caroptions-class carOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-routing-caroptions-class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withEVCarOptions">
/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withevcaroptions(/sdk-for-flutter-explore-routing-evcaroptions-class evCarOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-routing-evcaroptions-class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withEVTruckOptions">
/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withevtruckoptions(/sdk-for-flutter-explore-routing-evtruckoptions-class evTruckOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-routing-evtruckoptions-class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withPedestrianOptions">
/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withpedestrianoptions(/sdk-for-flutter-explore-routing-pedestrianoptions-class pedestrianOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-routing-pedestrianoptions-class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withPrivateBusOptions">
/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withprivatebusoptions(/sdk-for-flutter-explore-routing-privatebusoptions-class privateBusOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-routing-privatebusoptions-class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withScooterOptions">
/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withscooteroptions(/sdk-for-flutter-explore-routing-scooteroptions-class scooterOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-routing-scooteroptions-class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withTaxiOptions">
/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withtaxioptions(/sdk-for-flutter-explore-routing-taxioptions-class taxiOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-routing-taxioptions-class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withTransportMode">
/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withtransportmode(/sdk-for-flutter-explore-transport-transportmode transportMode)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-transport-transportmode.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteOptions.withTruckOptions">
/sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withtruckoptions(/sdk-for-flutter-explore-routing-truckoptions-class truckOptions)
</dt>
<dd>
          Constructs a RefreshRouteOptions object with /sdk-for-flutter-explore-routing-truckoptions-class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-routing-refreshrouteoptions-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-refreshrouteoptions-runtimetype
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
/sdk-for-flutter-explore-routing-refreshrouteoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-refreshrouteoptions-tostring(<wbr/>)
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
/sdk-for-flutter-explore-routing-refreshrouteoptions-operator-equals(<wbr/>Object other)
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



</div>
`
}</HTMLBlock>

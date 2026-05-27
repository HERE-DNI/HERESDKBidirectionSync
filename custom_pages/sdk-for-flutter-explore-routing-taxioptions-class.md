---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-taxioptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- TaxiOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/TaxiOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/TaxiOptions/TaxiOptions.html">TaxiOptions</a></li>
<li><a href="routing/TaxiOptions/TaxiOptions.withDefaults.html">withDefaults</a></li>
<li class="section-title">
<a href="routing/TaxiOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/TaxiOptions/allowDriveThroughTaxiRoads.html">allowDriveThroughTaxiRoads</a></li>
<li><a href="routing/TaxiOptions/avoidanceOptions.html">avoidanceOptions</a></li>
<li><a href="routing/TaxiOptions/carSpecifications.html">carSpecifications</a></li>
<li><a href="routing/TaxiOptions/hashCode.html">hashCode</a></li>
<li><a href="routing/TaxiOptions/lastCharacterOfLicensePlate.html">lastCharacterOfLicensePlate</a></li>
<li><a href="routing/TaxiOptions/maxSpeedOnSegments.html">maxSpeedOnSegments</a></li>
<li><a href="routing/TaxiOptions/routeOptions.html">routeOptions</a></li>
<li class="inherited"><a href="routing/TaxiOptions/runtimeType.html">runtimeType</a></li>
<li><a href="routing/TaxiOptions/textOptions.html">textOptions</a></li>
<li><a href="routing/TaxiOptions/tollOptions.html">tollOptions</a></li>
<li class="section-title inherited"><a href="routing/TaxiOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/TaxiOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/TaxiOptions/toString.html">toString</a></li>
<li class="section-title"><a href="routing/TaxiOptions-class.html#operators">Operators</a></li>
<li><a href="routing/TaxiOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">TaxiOptions class</li>
</ol>
<div class="self-name">TaxiOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TaxiOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TaxiOptions class</h1></div>
<section class="desc markdown">
<p>All the options to specify how a taxi route should be calculated.</p>
<p>See, <a href="../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a>.</p>
<p><strong>Note:</strong> Specify the optional <a href="../routing/Waypoint/sideOfStreetHint.html">/sdk-for-flutter-explore-routing-waypoint-sideofstreethint</a> to indicate at which side of
the street a passenger wants to leave the taxi.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Annotations</dt>
<dd>
<ul class="annotation-list clazz-relationships">
<li>@Deprecated("Will be removed in v4.28.0. Use `RoutingOptions` class instead.")</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TaxiOptions">
<a href="../routing/TaxiOptions/TaxiOptions.html">/sdk-for-flutter-explore-routing-taxioptions-taxioptions</a>(<a href="../routing/RouteOptions-class.html">/sdk-for-flutter-explore-routing-routeoptions-class</a> routeOptions, <a href="../routing/RouteTextOptions-class.html">/sdk-for-flutter-explore-routing-routetextoptions-class</a> textOptions, <a href="../routing/AvoidanceOptions-class.html">/sdk-for-flutter-explore-routing-avoidanceoptions-class</a> avoidanceOptions)
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="TaxiOptions.withDefaults">
<a href="../routing/TaxiOptions/TaxiOptions.withDefaults.html">/sdk-for-flutter-explore-routing-taxioptions-taxioptions-withdefaults</a>()
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="allowDriveThroughTaxiRoads">
<a href="../routing/TaxiOptions/allowDriveThroughTaxiRoads.html">/sdk-for-flutter-explore-routing-taxioptions-allowdrivethroughtaxiroads</a>
↔ bool
</dt>
<dd>
  Specifies if a vehicle is allowed to drive through the taxi-only roads and lanes.
When set to <code>false</code>, it is still allowed on taxi roads after the route start and
before the route destination.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidanceOptions">
<a href="../routing/TaxiOptions/avoidanceOptions.html">/sdk-for-flutter-explore-routing-taxioptions-avoidanceoptions</a>
↔ <a href="../routing/AvoidanceOptions-class.html">/sdk-for-flutter-explore-routing-avoidanceoptions-class</a>
</dt>
<dd>
  Options to specify restrictions for route calculations. By default
no restrictions are applied.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="carSpecifications">
<a href="../routing/TaxiOptions/carSpecifications.html">/sdk-for-flutter-explore-routing-taxioptions-carspecifications</a>
↔ <a class="deprecated" href="../transport/CarSpecifications-class.html">/sdk-for-flutter-explore-transport-carspecifications-class</a>
</dt>
<dd>
  Detailed car specifications such as dimensions and weight.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/TaxiOptions/hashCode.html">/sdk-for-flutter-explore-routing-taxioptions-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lastCharacterOfLicensePlate">
<a href="../routing/TaxiOptions/lastCharacterOfLicensePlate.html">/sdk-for-flutter-explore-routing-taxioptions-lastcharacteroflicenseplate</a>
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
<a href="../routing/TaxiOptions/maxSpeedOnSegments.html">/sdk-for-flutter-explore-routing-taxioptions-maxspeedonsegments</a>
↔ List&lt;<wbr/><a href="../routing/MaxSpeedOnSegment-class.html">/sdk-for-flutter-explore-routing-maxspeedonsegment-class</a>&gt;
</dt>
<dd>
  Segments with restriction on maximum <a href="../routing/DynamicSpeedInfo/baseSpeedInMetersPerSecond.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-basespeedinmeterspersecond</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routeOptions">
<a href="../routing/TaxiOptions/routeOptions.html">/sdk-for-flutter-explore-routing-taxioptions-routeoptions</a>
↔ <a href="../routing/RouteOptions-class.html">/sdk-for-flutter-explore-routing-routeoptions-class</a>
</dt>
<dd>
  Specifies the common route calculation options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/TaxiOptions/runtimeType.html">/sdk-for-flutter-explore-routing-taxioptions-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="textOptions">
<a href="../routing/TaxiOptions/textOptions.html">/sdk-for-flutter-explore-routing-taxioptions-textoptions</a>
↔ <a href="../routing/RouteTextOptions-class.html">/sdk-for-flutter-explore-routing-routetextoptions-class</a>
</dt>
<dd>
  Customize textual content returned from the route calculation, such
as localization, format, and unit system.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tollOptions">
<a href="../routing/TaxiOptions/tollOptions.html">/sdk-for-flutter-explore-routing-taxioptions-tolloptions</a>
↔ <a href="../routing/TollOptions-class.html">/sdk-for-flutter-explore-routing-tolloptions-class</a>
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
<a href="../routing/TaxiOptions/noSuchMethod.html">/sdk-for-flutter-explore-routing-taxioptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/TaxiOptions/toString.html">/sdk-for-flutter-explore-routing-taxioptions-tostring</a>(<wbr/>)
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
<a href="../routing/TaxiOptions/operator_equals.html">/sdk-for-flutter-explore-routing-taxioptions-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">TaxiOptions class</li>
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

---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-caroptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- CarOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/CarOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/CarOptions/CarOptions.html">CarOptions</a></li>
<li class="section-title">
<a href="routing/CarOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/CarOptions/allowOptions.html">allowOptions</a></li>
<li><a href="routing/CarOptions/avoidanceOptions.html">avoidanceOptions</a></li>
<li><a href="routing/CarOptions/carSpecifications.html">carSpecifications</a></li>
<li><a href="routing/CarOptions/hashCode.html">hashCode</a></li>
<li><a href="routing/CarOptions/lastCharacterOfLicensePlate.html">lastCharacterOfLicensePlate</a></li>
<li><a href="routing/CarOptions/maxSpeedOnSegments.html">maxSpeedOnSegments</a></li>
<li><a href="routing/CarOptions/occupantsNumber.html">occupantsNumber</a></li>
<li><a href="routing/CarOptions/routeOptions.html">routeOptions</a></li>
<li class="inherited"><a href="routing/CarOptions/runtimeType.html">runtimeType</a></li>
<li><a href="routing/CarOptions/textOptions.html">textOptions</a></li>
<li><a href="routing/CarOptions/tollOptions.html">tollOptions</a></li>
<li class="section-title inherited"><a href="routing/CarOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/CarOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/CarOptions/toString.html">toString</a></li>
<li class="section-title"><a href="routing/CarOptions-class.html#operators">Operators</a></li>
<li><a href="routing/CarOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">CarOptions class</li>
</ol>
<div class="self-name">CarOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/CarOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>CarOptions class</h1></div>
<section class="desc markdown">
<p>All the options to specify how a car route should be calculated.</p>
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
<dt class="callable" id="CarOptions">
<a href="../routing/CarOptions/CarOptions.html">/sdk-for-flutter-explore-routing-caroptions-caroptions</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="allowOptions">
<a href="../routing/CarOptions/allowOptions.html">/sdk-for-flutter-explore-routing-caroptions-allowoptions</a>
↔ <a href="../routing/AllowOptions-class.html">/sdk-for-flutter-explore-routing-allowoptions-class</a>
</dt>
<dd>
  The options explicitly allowed by user for route calculations. By default
no options are opt in.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidanceOptions">
<a href="../routing/CarOptions/avoidanceOptions.html">/sdk-for-flutter-explore-routing-caroptions-avoidanceoptions</a>
↔ <a href="../routing/AvoidanceOptions-class.html">/sdk-for-flutter-explore-routing-avoidanceoptions-class</a>
</dt>
<dd>
  Options to specify restrictions for route calculations. By default
no restrictions are applied.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="carSpecifications">
<a href="../routing/CarOptions/carSpecifications.html">/sdk-for-flutter-explore-routing-caroptions-carspecifications</a>
↔ <a class="deprecated" href="../transport/CarSpecifications-class.html">/sdk-for-flutter-explore-transport-carspecifications-class</a>
</dt>
<dd>
  Detailed car specifications such as dimensions and weight.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/CarOptions/hashCode.html">/sdk-for-flutter-explore-routing-caroptions-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lastCharacterOfLicensePlate">
<a href="../routing/CarOptions/lastCharacterOfLicensePlate.html">/sdk-for-flutter-explore-routing-caroptions-lastcharacteroflicenseplate</a>
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
<a href="../routing/CarOptions/maxSpeedOnSegments.html">/sdk-for-flutter-explore-routing-caroptions-maxspeedonsegments</a>
↔ List&lt;<wbr/><a href="../routing/MaxSpeedOnSegment-class.html">/sdk-for-flutter-explore-routing-maxspeedonsegment-class</a>&gt;
</dt>
<dd>
  Segments with restriction on maximum <a href="../routing/DynamicSpeedInfo/baseSpeedInMetersPerSecond.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-basespeedinmeterspersecond</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="occupantsNumber">
<a href="../routing/CarOptions/occupantsNumber.html">/sdk-for-flutter-explore-routing-caroptions-occupantsnumber</a>
↔ int
</dt>
<dd>
  Specifies the number of occupants in the vehicle, including driver,
can affect the vehicle's ability to use HOV/carpool restricted lanes.
Shouldn't be less than 1 or greater than 255. Defaults to 1.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routeOptions">
<a href="../routing/CarOptions/routeOptions.html">/sdk-for-flutter-explore-routing-caroptions-routeoptions</a>
↔ <a href="../routing/RouteOptions-class.html">/sdk-for-flutter-explore-routing-routeoptions-class</a>
</dt>
<dd>
  Specifies the common route calculation options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/CarOptions/runtimeType.html">/sdk-for-flutter-explore-routing-caroptions-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="textOptions">
<a href="../routing/CarOptions/textOptions.html">/sdk-for-flutter-explore-routing-caroptions-textoptions</a>
↔ <a href="../routing/RouteTextOptions-class.html">/sdk-for-flutter-explore-routing-routetextoptions-class</a>
</dt>
<dd>
  Customize textual content returned from the route calculation, such
as localization, format, and unit system.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tollOptions">
<a href="../routing/CarOptions/tollOptions.html">/sdk-for-flutter-explore-routing-caroptions-tolloptions</a>
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
<a href="../routing/CarOptions/noSuchMethod.html">/sdk-for-flutter-explore-routing-caroptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/CarOptions/toString.html">/sdk-for-flutter-explore-routing-caroptions-tostring</a>(<wbr/>)
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
<a href="../routing/CarOptions/operator_equals.html">/sdk-for-flutter-explore-routing-caroptions-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">CarOptions class</li>
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

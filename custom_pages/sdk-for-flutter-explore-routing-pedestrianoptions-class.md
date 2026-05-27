---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-pedestrianoptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- PedestrianOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/PedestrianOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/PedestrianOptions/PedestrianOptions.html">PedestrianOptions</a></li>
<li class="section-title">
<a href="routing/PedestrianOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/PedestrianOptions/avoidanceOptions.html">avoidanceOptions</a></li>
<li><a href="routing/PedestrianOptions/hashCode.html">hashCode</a></li>
<li><a href="routing/PedestrianOptions/routeOptions.html">routeOptions</a></li>
<li class="inherited"><a href="routing/PedestrianOptions/runtimeType.html">runtimeType</a></li>
<li><a href="routing/PedestrianOptions/textOptions.html">textOptions</a></li>
<li><a href="routing/PedestrianOptions/walkSpeedInMetersPerSecond.html">walkSpeedInMetersPerSecond</a></li>
<li class="section-title inherited"><a href="routing/PedestrianOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/PedestrianOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/PedestrianOptions/toString.html">toString</a></li>
<li class="section-title"><a href="routing/PedestrianOptions-class.html#operators">Operators</a></li>
<li><a href="routing/PedestrianOptions/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="routing/PedestrianOptions-class.html#static-methods">Static methods</a></li>
<li><a href="routing/PedestrianOptions/fromDefaultParameterConfiguration.html">fromDefaultParameterConfiguration</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">PedestrianOptions class</li>
</ol>
<div class="self-name">PedestrianOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/PedestrianOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PedestrianOptions class</h1></div>
<section class="desc markdown">
<p>All the options to specify how a pedestrian route should be calculated.</p>
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
<dt class="callable" id="PedestrianOptions">
<a href="../routing/PedestrianOptions/PedestrianOptions.html">/sdk-for-flutter-explore-routing-pedestrianoptions-pedestrianoptions</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="avoidanceOptions">
<a href="../routing/PedestrianOptions/avoidanceOptions.html">/sdk-for-flutter-explore-routing-pedestrianoptions-avoidanceoptions</a>
↔ <a href="../routing/AvoidanceOptions-class.html">/sdk-for-flutter-explore-routing-avoidanceoptions-class</a>
</dt>
<dd>
  Options to specify restrictions for route calculations. By default
no restrictions are applied.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/PedestrianOptions/hashCode.html">/sdk-for-flutter-explore-routing-pedestrianoptions-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="routeOptions">
<a href="../routing/PedestrianOptions/routeOptions.html">/sdk-for-flutter-explore-routing-pedestrianoptions-routeoptions</a>
↔ <a href="../routing/RouteOptions-class.html">/sdk-for-flutter-explore-routing-routeoptions-class</a>
</dt>
<dd>
  Specifies the common route calculation options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/PedestrianOptions/runtimeType.html">/sdk-for-flutter-explore-routing-pedestrianoptions-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="textOptions">
<a href="../routing/PedestrianOptions/textOptions.html">/sdk-for-flutter-explore-routing-pedestrianoptions-textoptions</a>
↔ <a href="../routing/RouteTextOptions-class.html">/sdk-for-flutter-explore-routing-routetextoptions-class</a>
</dt>
<dd>
  Customize textual content returned from the route calculation, such
as localization, format, and unit system.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="walkSpeedInMetersPerSecond">
<a href="../routing/PedestrianOptions/walkSpeedInMetersPerSecond.html">/sdk-for-flutter-explore-routing-pedestrianoptions-walkspeedinmeterspersecond</a>
↔ double
</dt>
<dd>
  Specifies the speed that will be used by the service as the walking speed
for pedestrian routing in meters per second. It influences the duration of
walking segments along the route. The provided value must be in the range
[0.5, 2.0]. When the value is outside this range, an invalid parameter
error is raised. Refer to <a href="../routing/RoutingError.html">/sdk-for-flutter-explore-routing-routingerror</a> for details. The default
speed is 1 meter per second.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/PedestrianOptions/noSuchMethod.html">/sdk-for-flutter-explore-routing-pedestrianoptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/PedestrianOptions/toString.html">/sdk-for-flutter-explore-routing-pedestrianoptions-tostring</a>(<wbr/>)
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
<a href="../routing/PedestrianOptions/operator_equals.html">/sdk-for-flutter-explore-routing-pedestrianoptions-operator-equals</a>(<wbr/>Object other)
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
<a href="../routing/PedestrianOptions/fromDefaultParameterConfiguration.html">/sdk-for-flutter-explore-routing-pedestrianoptions-fromdefaultparameterconfiguration</a>(<wbr/>)
    → <a class="deprecated" href="../routing/PedestrianOptions-class.html">/sdk-for-flutter-explore-routing-pedestrianoptions-class</a>
</dt>
<dd>
  Returns PedestrianOptions instance with default values used in SDK.
  

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
<li class="self-crumb">PedestrianOptions class</li>
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

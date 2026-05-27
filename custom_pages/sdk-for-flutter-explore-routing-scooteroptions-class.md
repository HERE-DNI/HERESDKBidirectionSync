---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-scooteroptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- ScooterOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/ScooterOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/ScooterOptions/ScooterOptions.html">ScooterOptions</a></li>
<li class="section-title">
<a href="routing/ScooterOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/ScooterOptions/allowHighway.html">allowHighway</a></li>
<li><a href="routing/ScooterOptions/avoidanceOptions.html">avoidanceOptions</a></li>
<li><a href="routing/ScooterOptions/engineSizeInCubicCentimeters.html">engineSizeInCubicCentimeters</a></li>
<li><a href="routing/ScooterOptions/hashCode.html">hashCode</a></li>
<li><a href="routing/ScooterOptions/lastCharacterOfLicensePlate.html">lastCharacterOfLicensePlate</a></li>
<li><a href="routing/ScooterOptions/maxSpeedOnSegments.html">maxSpeedOnSegments</a></li>
<li><a href="routing/ScooterOptions/occupantsNumber.html">occupantsNumber</a></li>
<li><a href="routing/ScooterOptions/routeOptions.html">routeOptions</a></li>
<li class="inherited"><a href="routing/ScooterOptions/runtimeType.html">runtimeType</a></li>
<li><a href="routing/ScooterOptions/textOptions.html">textOptions</a></li>
<li><a href="routing/ScooterOptions/tollOptions.html">tollOptions</a></li>
<li class="section-title inherited"><a href="routing/ScooterOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/ScooterOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/ScooterOptions/toString.html">toString</a></li>
<li class="section-title"><a href="routing/ScooterOptions-class.html#operators">Operators</a></li>
<li><a href="routing/ScooterOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">ScooterOptions class</li>
</ol>
<div class="self-name">ScooterOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/ScooterOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ScooterOptions class</h1></div>
<section class="desc markdown">
<p>All the options to specify how a scooter route should be calculated.</p>
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
<dt class="callable" id="ScooterOptions">
<a href="../routing/ScooterOptions/ScooterOptions.html">/sdk-for-flutter-explore-routing-scooteroptions-scooteroptions</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="allowHighway">
<a href="../routing/ScooterOptions/allowHighway.html">/sdk-for-flutter-explore-routing-scooteroptions-allowhighway</a>
↔ bool
</dt>
<dd>
  Specifies whether scooter is allowed on highway or not. <code>True</code> means scooter is
allowed to use highways and <code>false</code> means otherwise. By default it is set to <code>false</code>.
Note that there is a similar parameter in <a href="../routing/AvoidanceOptions-class.html">/sdk-for-flutter-explore-routing-avoidanceoptions-class</a>, to
disallow highway usage, see <a href="../routing/RoadFeatures.html">/sdk-for-flutter-explore-routing-roadfeatures</a>.
As the avoidance options takes precedence, if this parameter is also used, then
scooters are not allowed to use highways even if <code>allowHighway</code> is set to <code>true</code>.
However, if no alternative route is possible, the calculated route may use highways.
In such a case, a <a href="../routing/SectionNotice-class.html">/sdk-for-flutter-explore-routing-sectionnotice-class</a> will be provided in the related <a href="../routing/Section-class.html">/sdk-for-flutter-explore-routing-section-class</a>
to indicate that the highway usage restriction is violated on this route.
A few examples:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidanceOptions">
<a href="../routing/ScooterOptions/avoidanceOptions.html">/sdk-for-flutter-explore-routing-scooteroptions-avoidanceoptions</a>
↔ <a href="../routing/AvoidanceOptions-class.html">/sdk-for-flutter-explore-routing-avoidanceoptions-class</a>
</dt>
<dd>
  Options to specify restrictions for route calculations. By default
no restrictions are applied.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="engineSizeInCubicCentimeters">
<a href="../routing/ScooterOptions/engineSizeInCubicCentimeters.html">/sdk-for-flutter-explore-routing-scooteroptions-enginesizeincubiccentimeters</a>
↔ int?
</dt>
<dd>
  Engine size of the scooter in cubic centimeters. Shouldn't be less than 1 or greater than 65535. Default value
is <code>null</code>, which means the scooter route calculation ignores all engine size limits on the road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/ScooterOptions/hashCode.html">/sdk-for-flutter-explore-routing-scooteroptions-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lastCharacterOfLicensePlate">
<a href="../routing/ScooterOptions/lastCharacterOfLicensePlate.html">/sdk-for-flutter-explore-routing-scooteroptions-lastcharacteroflicenseplate</a>
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
<a href="../routing/ScooterOptions/maxSpeedOnSegments.html">/sdk-for-flutter-explore-routing-scooteroptions-maxspeedonsegments</a>
↔ List&lt;<wbr/><a href="../routing/MaxSpeedOnSegment-class.html">/sdk-for-flutter-explore-routing-maxspeedonsegment-class</a>&gt;
</dt>
<dd>
  Segments with restriction on maximum <a href="../routing/DynamicSpeedInfo/baseSpeedInMetersPerSecond.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-basespeedinmeterspersecond</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="occupantsNumber">
<a href="../routing/ScooterOptions/occupantsNumber.html">/sdk-for-flutter-explore-routing-scooteroptions-occupantsnumber</a>
↔ int
</dt>
<dd>
  Specifies the number of occupants in the vehicle, including driver.
Shouldn't be less than 1 or greater than 255. Defaults to 1.
This option is only relevant for Japan and will be ignored for other countries.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routeOptions">
<a href="../routing/ScooterOptions/routeOptions.html">/sdk-for-flutter-explore-routing-scooteroptions-routeoptions</a>
↔ <a href="../routing/RouteOptions-class.html">/sdk-for-flutter-explore-routing-routeoptions-class</a>
</dt>
<dd>
  Specifies the common route calculation options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/ScooterOptions/runtimeType.html">/sdk-for-flutter-explore-routing-scooteroptions-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="textOptions">
<a href="../routing/ScooterOptions/textOptions.html">/sdk-for-flutter-explore-routing-scooteroptions-textoptions</a>
↔ <a href="../routing/RouteTextOptions-class.html">/sdk-for-flutter-explore-routing-routetextoptions-class</a>
</dt>
<dd>
  Customize textual content returned from the route calculation, such
as localization, format, and unit system.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tollOptions">
<a href="../routing/ScooterOptions/tollOptions.html">/sdk-for-flutter-explore-routing-scooteroptions-tolloptions</a>
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
<a href="../routing/ScooterOptions/noSuchMethod.html">/sdk-for-flutter-explore-routing-scooteroptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/ScooterOptions/toString.html">/sdk-for-flutter-explore-routing-scooteroptions-tostring</a>(<wbr/>)
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
<a href="../routing/ScooterOptions/operator_equals.html">/sdk-for-flutter-explore-routing-scooteroptions-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">ScooterOptions class</li>
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

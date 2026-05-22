---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-scooteroptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ScooterOptions-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
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
<li>@Deprecated("Will be removed in v4.28.0. Use <code>RoutingOptions</code> class instead.")</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ScooterOptions">
/sdk-for-flutter-explore-routing-scooteroptions-scooteroptions()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="allowHighway">
/sdk-for-flutter-explore-routing-scooteroptions-allowhighway
↔ bool
</dt>
<dd>
  Specifies whether scooter is allowed on highway or not. <code>True</code> means scooter is
allowed to use highways and <code>false</code> means otherwise. By default it is set to <code>false</code>.
Note that there is a similar parameter in /sdk-for-flutter-explore-routing-avoidanceoptions-class, to
disallow highway usage, see /sdk-for-flutter-explore-routing-roadfeatures.
As the avoidance options takes precedence, if this parameter is also used, then
scooters are not allowed to use highways even if <code>allowHighway</code> is set to <code>true</code>.
However, if no alternative route is possible, the calculated route may use highways.
In such a case, a /sdk-for-flutter-explore-routing-sectionnotice-class will be provided in the related /sdk-for-flutter-explore-routing-section-class
to indicate that the highway usage restriction is violated on this route.
A few examples:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidanceOptions">
/sdk-for-flutter-explore-routing-scooteroptions-avoidanceoptions
↔ /sdk-for-flutter-explore-routing-avoidanceoptions-class
</dt>
<dd>
  Options to specify restrictions for route calculations. By default
no restrictions are applied.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="engineSizeInCubicCentimeters">
/sdk-for-flutter-explore-routing-scooteroptions-enginesizeincubiccentimeters
↔ int?
</dt>
<dd>
  Engine size of the scooter in cubic centimeters. Shouldn't be less than 1 or greater than 65535. Default value
is <code>null</code>, which means the scooter route calculation ignores all engine size limits on the road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-routing-scooteroptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lastCharacterOfLicensePlate">
/sdk-for-flutter-explore-routing-scooteroptions-lastcharacteroflicenseplate
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
/sdk-for-flutter-explore-routing-scooteroptions-maxspeedonsegments
↔ List&lt;<wbr/>/sdk-for-flutter-explore-routing-maxspeedonsegment-class&gt;
</dt>
<dd>
  Segments with restriction on maximum /sdk-for-flutter-explore-routing-dynamicspeedinfo-basespeedinmeterspersecond.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="occupantsNumber">
/sdk-for-flutter-explore-routing-scooteroptions-occupantsnumber
↔ int
</dt>
<dd>
  Specifies the number of occupants in the vehicle, including driver.
Shouldn't be less than 1 or greater than 255. Defaults to 1.
This option is only relevant for Japan and will be ignored for other countries.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routeOptions">
/sdk-for-flutter-explore-routing-scooteroptions-routeoptions
↔ /sdk-for-flutter-explore-routing-routeoptions-class
</dt>
<dd>
  Specifies the common route calculation options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-scooteroptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="textOptions">
/sdk-for-flutter-explore-routing-scooteroptions-textoptions
↔ /sdk-for-flutter-explore-routing-routetextoptions-class
</dt>
<dd>
  Customize textual content returned from the route calculation, such
as localization, format, and unit system.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tollOptions">
/sdk-for-flutter-explore-routing-scooteroptions-tolloptions
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
/sdk-for-flutter-explore-routing-scooteroptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-scooteroptions-tostring(<wbr/>)
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
/sdk-for-flutter-explore-routing-scooteroptions-operator-equals(<wbr/>Object other)
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



</div>
`
}</HTMLBlock>

---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-truckoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TruckOptions-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">TruckOptions class</li>
</ol>
<div class="self-name">TruckOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TruckOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TruckOptions class</h1></div>
<section class="desc markdown">
<p>All the options to specify how a truck route should be calculated.</p>
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
<dt class="callable" id="TruckOptions">
/sdk-for-flutter-explore-routing-truckoptions-truckoptions()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="allowOptions">
/sdk-for-flutter-explore-routing-truckoptions-allowoptions
↔ /sdk-for-flutter-explore-routing-allowoptions-class
</dt>
<dd>
  The options explicitly allowed by user for route calculations. By default
no options are opt in.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidanceOptions">
/sdk-for-flutter-explore-routing-truckoptions-avoidanceoptions
↔ /sdk-for-flutter-explore-routing-avoidanceoptions-class
</dt>
<dd>
  Options to specify restrictions for route calculations. By default
no restrictions are applied.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidedTruckRoadTypes">
/sdk-for-flutter-explore-routing-truckoptions-avoidedtruckroadtypes
↔ List&lt;<wbr/>/sdk-for-flutter-explore-transport-truckroadtype&gt;
</dt>
<dd>
  Specifies a list of avoided truck road types for vehicle.
Refer to /sdk-for-flutter-explore-transport-truckroadtype for the available options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-routing-truckoptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="hazardousMaterials">
/sdk-for-flutter-explore-routing-truckoptions-hazardousmaterials
↔ List&lt;<wbr/>/sdk-for-flutter-explore-transport-hazardousmaterial&gt;
</dt>
<dd>
  Specifies a list of hazardous materials shipped in the vehicle.
Refer to /sdk-for-flutter-explore-transport-hazardousmaterial for the available options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lastCharacterOfLicensePlate">
/sdk-for-flutter-explore-routing-truckoptions-lastcharacteroflicenseplate
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
<dt class="property" id="linkTunnelCategory">
/sdk-for-flutter-explore-routing-truckoptions-linktunnelcategory
↔ /sdk-for-flutter-explore-transport-tunnelcategory?
</dt>
<dd>
  Specifies the tunnel categories to restrict certain route links.
The route will pass only through tunnels of a less strict category.
Refer to /sdk-for-flutter-explore-transport-tunnelcategory for the available options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxSpeedOnSegments">
/sdk-for-flutter-explore-routing-truckoptions-maxspeedonsegments
↔ List&lt;<wbr/>/sdk-for-flutter-explore-routing-maxspeedonsegment-class&gt;
</dt>
<dd>
  Segments with restriction on maximum /sdk-for-flutter-explore-routing-dynamicspeedinfo-basespeedinmeterspersecond.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="occupantsNumber">
/sdk-for-flutter-explore-routing-truckoptions-occupantsnumber
↔ int
</dt>
<dd>
  Specifies the number of occupants in the vehicle, including driver,
can affect the vehicle's ability to use HOV/carpool restricted lanes.
Shouldn't be less than 1 or greater than 255. Defaults to 1.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routeOptions">
/sdk-for-flutter-explore-routing-truckoptions-routeoptions
↔ /sdk-for-flutter-explore-routing-routeoptions-class
</dt>
<dd>
  Specifies the common route calculation options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-truckoptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="textOptions">
/sdk-for-flutter-explore-routing-truckoptions-textoptions
↔ /sdk-for-flutter-explore-routing-routetextoptions-class
</dt>
<dd>
  Customize textual content returned from the route calculation, such
as localization, format, and unit system.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tollOptions">
/sdk-for-flutter-explore-routing-truckoptions-tolloptions
↔ /sdk-for-flutter-explore-routing-tolloptions-class
</dt>
<dd>
  Options to specify how the tolls should be calculated,
such as transponders, vehicle category, and emission type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckSpecifications">
/sdk-for-flutter-explore-routing-truckoptions-truckspecifications
↔ /sdk-for-flutter-explore-transport-truckspecifications-class
</dt>
<dd>
  Detailed truck specifications such as dimensions and weight.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-routing-truckoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-truckoptions-tostring(<wbr/>)
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
/sdk-for-flutter-explore-routing-truckoptions-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">TruckOptions class</li>
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

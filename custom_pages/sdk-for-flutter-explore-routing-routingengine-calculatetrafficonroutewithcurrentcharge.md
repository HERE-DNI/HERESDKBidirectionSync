---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-routingengine-calculatetrafficonroutewithcurrentcharge"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- calculateTrafficOnRouteWithCurrentCharge.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/RoutingEngine-class.html">/sdk-for-flutter-explore-routing-routingengine-class</a></li>
<li class="self-crumb">calculateTrafficOnRouteWithCurrentCharge abstract method</li>
</ol>
<div class="self-name">calculateTrafficOnRouteWithCurrentCharge</div>
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
<div class="main-content" data-above-sidebar="routing/RoutingEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>calculateTrafficOnRouteWithCurrentCharge abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
calculateTrafficOnRouteWithCurrentCharge(<wbr/><ol class="parameter-list"> <li><a href="../../routing/Route-class.html">/sdk-for-flutter-explore-routing-route-class</a> route, </li>
<li>int lastTraveledSectionIndex, </li>
<li>int traveledDistanceOnLastSectionInMeters, </li>
<li>double currentChargeInKilowattHours, </li>
<li><a href="../../routing/CalculateTrafficOnRouteCallback.html">/sdk-for-flutter-explore-routing-calculatetrafficonroutecallback</a> callback, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously calculates the traffic along an EV car route starting from the index of the
last traveled route section and an offset in meters from the last visited position on the
section.</p>
<p>The field <a href="../../routing/TrafficOnSpan/consumptionInKilowattHours.html">/sdk-for-flutter-explore-routing-trafficonspan-consumptioninkilowatthours</a> will contain the power consumption
in kilowatt-hours (kWh) necessary to traverse the span, and
<a href="../../routing/RoutePlace/chargeInKilowattHours.html">/sdk-for-flutter-explore-routing-routeplace-chargeinkilowatthours</a>, inside <a href="../../routing/TrafficOnSection/departurePlace.html">/sdk-for-flutter-explore-routing-trafficonsection-departureplace</a> and
<a href="../../routing/TrafficOnSection/arrivalPlace.html">/sdk-for-flutter-explore-routing-trafficonsection-arrivalplace</a>, the estimated battery charge in kilowatt-hours (kWh) when
leaving/arriving to a section.
<strong>Note:</strong> Only EV cars are supported.</p>
<ul>
<li>
<p><code>route</code> A <a href="../../routing/Route-class.html">/sdk-for-flutter-explore-routing-route-class</a> calculated using the online routing engine. Its
<a href="../../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a> and the original route calculation options, along with EV
related information like <a href="../../routing/BatterySpecifications-class.html">/sdk-for-flutter-explore-routing-batteryspecifications-class</a>, will be used to
compute the traffic on the route. The original route remains untouched.</p>
</li>
<li>
<p><code>lastTraveledSectionIndex</code> Indicates the index of the last traveled route section. Traveled part of the route won't
be reused.</p>
</li>
<li>
<p><code>traveledDistanceOnLastSectionInMeters</code> Offset, in meters, to the last visited position on the route section defined by the last
traveled section index.</p>
</li>
<li>
<p><code>currentChargeInKilowattHours</code> Charge level of the vehicle's battery at the current location (in kWh).
It must be non-negative and less than or equal to the value of
<a href="../../routing/BatterySpecifications/totalCapacityInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours</a>,
otherwise the <a href="../../routing/BatterySpecifications-class.html">/sdk-for-flutter-explore-routing-batteryspecifications-class</a> instance is considered invalid.
Sets <a href="../../routing/BatterySpecifications/initialChargeInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-initialchargeinkilowatthours</a> to the given value.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route traffic has been calculated.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle calculateTrafficOnRouteWithCurrentCharge(Route route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, double currentChargeInKilowattHours, CalculateTrafficOnRouteCallback callback);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/RoutingEngine-class.html">/sdk-for-flutter-explore-routing-routingengine-class</a></li>
<li class="self-crumb">calculateTrafficOnRouteWithCurrentCharge abstract method</li>
</ol>
<h5>RoutingEngine class</h5>
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

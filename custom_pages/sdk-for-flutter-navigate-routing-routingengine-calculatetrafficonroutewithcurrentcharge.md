---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-routingengine-calculatetrafficonroutewithcurrentcharge"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateTrafficOnRouteWithCurrentCharge.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-routingengine-class</li>
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
/sdk-for-flutter-navigate-core-threading-taskhandle-class
calculateTrafficOnRouteWithCurrentCharge(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-routing-route-class route, </li>
<li>int lastTraveledSectionIndex, </li>
<li>int traveledDistanceOnLastSectionInMeters, </li>
<li>double currentChargeInKilowattHours, </li>
<li>/sdk-for-flutter-navigate-routing-calculatetrafficonroutecallback callback, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously calculates the traffic along an EV car route starting from the index of the
last traveled route section and an offset in meters from the last visited position on the
section.</p>
<p>The field /sdk-for-flutter-navigate-routing-trafficonspan-consumptioninkilowatthours will contain the power consumption
in kilowatt-hours (kWh) necessary to traverse the span, and
/sdk-for-flutter-navigate-routing-routeplace-chargeinkilowatthours, inside /sdk-for-flutter-navigate-routing-trafficonsection-departureplace and
/sdk-for-flutter-navigate-routing-trafficonsection-arrivalplace, the estimated battery charge in kilowatt-hours (kWh) when
leaving/arriving to a section.
<strong>Note:</strong> Only EV cars are supported.</p>
<ul>
<li>
<p><code>route</code> A /sdk-for-flutter-navigate-routing-route-class calculated using the online routing engine. Its
/sdk-for-flutter-navigate-routing-routehandle-class and the original route calculation options, along with EV
related information like /sdk-for-flutter-navigate-routing-batteryspecifications-class, will be used to
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
/sdk-for-flutter-navigate-routing-batteryspecifications-totalcapacityinkilowatthours,
otherwise the /sdk-for-flutter-navigate-routing-batteryspecifications-class instance is considered invalid.
Sets /sdk-for-flutter-navigate-routing-batteryspecifications-initialchargeinkilowatthours to the given value.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route traffic has been calculated.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-routingengine-class</li>
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



</div>
`
}</HTMLBlock>

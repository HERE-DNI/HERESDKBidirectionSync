---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-routinginterface-routinginterface"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- RoutingInterface.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/RoutingInterface-class.html">/sdk-for-flutter-explore-routing-routinginterface-class</a></li>
<li class="self-crumb">RoutingInterface factory constructor</li>
</ol>
<div class="self-name">RoutingInterface</div>
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
<div class="main-content" data-above-sidebar="routing/RoutingInterface-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>RoutingInterface constructor</h1></div>
<section class="multi-line-signature">
RoutingInterface(<wbr/><ol class="parameter-list"> <li><a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateRouteWithRoutingOptionsLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, </li>
<li><a href="../../routing/RoutingOptions-class.html">/sdk-for-flutter-explore-routing-routingoptions-class</a>, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> </li>
</ol>), </li>
<li><a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateCarRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, </li>
<li><a class="deprecated" href="../../routing/CarOptions-class.html">/sdk-for-flutter-explore-routing-caroptions-class</a>, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> </li>
</ol>), </li>
<li><a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculatePedestrianRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, </li>
<li><a class="deprecated" href="../../routing/PedestrianOptions-class.html">/sdk-for-flutter-explore-routing-pedestrianoptions-class</a>, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> </li>
</ol>), </li>
<li><a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateTruckRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, </li>
<li><a class="deprecated" href="../../routing/TruckOptions-class.html">/sdk-for-flutter-explore-routing-truckoptions-class</a>, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> </li>
</ol>), </li>
<li><a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateScooterRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, </li>
<li><a class="deprecated" href="../../routing/ScooterOptions-class.html">/sdk-for-flutter-explore-routing-scooteroptions-class</a>, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> </li>
</ol>), </li>
<li><a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateBicycleRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, </li>
<li><a class="deprecated" href="../../routing/BicycleOptions-class.html">/sdk-for-flutter-explore-routing-bicycleoptions-class</a>, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> </li>
</ol>), </li>
<li><a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateTaxiRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, </li>
<li><a class="deprecated" href="../../routing/TaxiOptions-class.html">/sdk-for-flutter-explore-routing-taxioptions-class</a>, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> </li>
</ol>), </li>
<li><a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateEVCarRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, </li>
<li><a class="deprecated" href="../../routing/EVCarOptions-class.html">/sdk-for-flutter-explore-routing-evcaroptions-class</a>, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> </li>
</ol>), </li>
<li><a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateEVTruckRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, </li>
<li><a class="deprecated" href="../../routing/EVTruckOptions-class.html">/sdk-for-flutter-explore-routing-evtruckoptions-class</a>, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> </li>
</ol>), </li>
<li><a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateBusRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, </li>
<li><a class="deprecated" href="../../routing/BusOptions-class.html">/sdk-for-flutter-explore-routing-busoptions-class</a>, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> </li>
</ol>), </li>
<li><a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculatePrivateBusRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, </li>
<li><a class="deprecated" href="../../routing/PrivateBusOptions-class.html">/sdk-for-flutter-explore-routing-privatebusoptions-class</a>, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> </li>
</ol>), </li>
<li><a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> returnToRouteWithTraveledDistanceLambda(<ol class="parameter-list"> <li><a href="../../routing/Route-class.html">/sdk-for-flutter-explore-routing-route-class</a>, </li>
<li><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>, </li>
<li>int, </li>
<li>int, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> , </li>
</ol>), </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Provides the abstract class for the online and offline
routing engines.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RoutingInterface(
  TaskHandle Function(List&lt;Waypoint&gt;, RoutingOptions, CalculateRouteCallback) calculateRouteWithRoutingOptionsLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, CarOptions, CalculateRouteCallback) calculateCarRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, PedestrianOptions, CalculateRouteCallback) calculatePedestrianRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, TruckOptions, CalculateRouteCallback) calculateTruckRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, ScooterOptions, CalculateRouteCallback) calculateScooterRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, BicycleOptions, CalculateRouteCallback) calculateBicycleRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, TaxiOptions, CalculateRouteCallback) calculateTaxiRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, EVCarOptions, CalculateRouteCallback) calculateEVCarRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, EVTruckOptions, CalculateRouteCallback) calculateEVTruckRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, BusOptions, CalculateRouteCallback) calculateBusRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, PrivateBusOptions, CalculateRouteCallback) calculatePrivateBusRouteLambda,
  TaskHandle Function(Route, Waypoint, int, int, CalculateRouteCallback) returnToRouteWithTraveledDistanceLambda,

) =&gt; RoutingInterface$Lambdas(
  calculateRouteWithRoutingOptionsLambda,
  calculateCarRouteLambda,
  calculatePedestrianRouteLambda,
  calculateTruckRouteLambda,
  calculateScooterRouteLambda,
  calculateBicycleRouteLambda,
  calculateTaxiRouteLambda,
  calculateEVCarRouteLambda,
  calculateEVTruckRouteLambda,
  calculateBusRouteLambda,
  calculatePrivateBusRouteLambda,
  returnToRouteWithTraveledDistanceLambda,

);</code></pre>
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
<li><a href="../../routing/RoutingInterface-class.html">/sdk-for-flutter-explore-routing-routinginterface-class</a></li>
<li class="self-crumb">RoutingInterface factory constructor</li>
</ol>
<h5>RoutingInterface class</h5>
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

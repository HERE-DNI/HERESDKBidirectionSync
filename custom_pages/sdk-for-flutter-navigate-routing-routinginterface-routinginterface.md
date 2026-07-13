---
title: "RoutingInterface constructor - RoutingInterface - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-routinginterface-routinginterface"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RoutingInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RoutingInterface</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RoutingInterface</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-calculateRouteWithRoutingOptionsLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">calculateRouteWithRoutingOptionsLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
2.  <span id="sdk-for-flutter-navigate-param-calculateCarRouteLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">calculateCarRouteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-caroptions-class" class="deprecated">CarOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
3.  <span id="sdk-for-flutter-navigate-param-calculatePedestrianRouteLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">calculatePedestrianRouteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-class" class="deprecated">PedestrianOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
4.  <span id="sdk-for-flutter-navigate-param-calculateTruckRouteLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">calculateTruckRouteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-truckoptions-class" class="deprecated">TruckOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
5.  <span id="sdk-for-flutter-navigate-param-calculateScooterRouteLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">calculateScooterRouteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-scooteroptions-class" class="deprecated">ScooterOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
6.  <span id="sdk-for-flutter-navigate-param-calculateBicycleRouteLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">calculateBicycleRouteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-bicycleoptions-class" class="deprecated">BicycleOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
7.  <span id="sdk-for-flutter-navigate-param-calculateTaxiRouteLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">calculateTaxiRouteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-taxioptions-class" class="deprecated">TaxiOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
8.  <span id="sdk-for-flutter-navigate-param-calculateEVCarRouteLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">calculateEVCarRouteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-evcaroptions-class" class="deprecated">EVCarOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
9.  <span id="sdk-for-flutter-navigate-param-calculateEVTruckRouteLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">calculateEVTruckRouteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-class" class="deprecated">EVTruckOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
10. <span id="sdk-for-flutter-navigate-param-calculateBusRouteLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">calculateBusRouteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-busoptions-class" class="deprecated">BusOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
11. <span id="sdk-for-flutter-navigate-param-calculatePrivateBusRouteLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">calculatePrivateBusRouteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-privatebusoptions-class" class="deprecated">PrivateBusOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
12. <span id="sdk-for-flutter-navigate-param-returnToRouteWithTraveledDistanceLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">returnToRouteWithTraveledDistanceLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span>, </span>
    4.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span>, </span>
    5.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name"></span>, </span>

    ), </span>

)

</div>

<div class="section desc markdown">

Provides the abstract class for the online and offline routing engines.

</div>

## Implementation

``` dart
factory RoutingInterface(
  TaskHandle Function(List<Waypoint>, RoutingOptions, CalculateRouteCallback) calculateRouteWithRoutingOptionsLambda,
  TaskHandle Function(List<Waypoint>, CarOptions, CalculateRouteCallback) calculateCarRouteLambda,
  TaskHandle Function(List<Waypoint>, PedestrianOptions, CalculateRouteCallback) calculatePedestrianRouteLambda,
  TaskHandle Function(List<Waypoint>, TruckOptions, CalculateRouteCallback) calculateTruckRouteLambda,
  TaskHandle Function(List<Waypoint>, ScooterOptions, CalculateRouteCallback) calculateScooterRouteLambda,
  TaskHandle Function(List<Waypoint>, BicycleOptions, CalculateRouteCallback) calculateBicycleRouteLambda,
  TaskHandle Function(List<Waypoint>, TaxiOptions, CalculateRouteCallback) calculateTaxiRouteLambda,
  TaskHandle Function(List<Waypoint>, EVCarOptions, CalculateRouteCallback) calculateEVCarRouteLambda,
  TaskHandle Function(List<Waypoint>, EVTruckOptions, CalculateRouteCallback) calculateEVTruckRouteLambda,
  TaskHandle Function(List<Waypoint>, BusOptions, CalculateRouteCallback) calculateBusRouteLambda,
  TaskHandle Function(List<Waypoint>, PrivateBusOptions, CalculateRouteCallback) calculatePrivateBusRouteLambda,
  TaskHandle Function(Route, Waypoint, int, int, CalculateRouteCallback) returnToRouteWithTraveledDistanceLambda,

) => RoutingInterface$Lambdas(
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

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


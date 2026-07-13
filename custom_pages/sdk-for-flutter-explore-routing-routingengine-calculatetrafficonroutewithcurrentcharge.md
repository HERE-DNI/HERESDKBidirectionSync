---
title: "calculateTrafficOnRouteWithCurrentCharge method - RoutingEngine class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routingengine-calculatetrafficonroutewithcurrentcharge"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">calculateTrafficOnRouteWithCurrentCharge</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">calculateTrafficOnRouteWithCurrentCharge</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-calculateTrafficOnRouteWithCurrentCharge-param-route" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-route-class">Route</a></span> <span class="parameter-name">route</span>, </span>
2.  <span id="sdk-for-flutter-explore-calculateTrafficOnRouteWithCurrentCharge-param-lastTraveledSectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">lastTraveledSectionIndex</span>, </span>
3.  <span id="sdk-for-flutter-explore-calculateTrafficOnRouteWithCurrentCharge-param-traveledDistanceOnLastSectionInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">traveledDistanceOnLastSectionInMeters</span>, </span>
4.  <span id="sdk-for-flutter-explore-calculateTrafficOnRouteWithCurrentCharge-param-currentChargeInKilowattHours" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">currentChargeInKilowattHours</span>, </span>
5.  <span id="sdk-for-flutter-explore-calculateTrafficOnRouteWithCurrentCharge-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-calculatetrafficonroutecallback">CalculateTrafficOnRouteCallback</a></span> <span class="parameter-name">callback</span>, </span>

)

</div>

<div class="section desc markdown">

Asynchronously calculates the traffic along an EV car route starting from the index of the last traveled route section and an offset in meters from the last visited position on the section.

The field <a href="sdk-for-flutter-explore-routing-trafficonspan-consumptioninkilowatthours">TrafficOnSpan.consumptionInKilowattHours</a> will contain the power consumption in kilowatt-hours (kWh) necessary to traverse the span, and <a href="sdk-for-flutter-explore-routing-routeplace-chargeinkilowatthours">RoutePlace.chargeInKilowattHours</a>, inside <a href="sdk-for-flutter-explore-routing-trafficonsection-departureplace">TrafficOnSection.departurePlace</a> and <a href="sdk-for-flutter-explore-routing-trafficonsection-arrivalplace">TrafficOnSection.arrivalPlace</a>, the estimated battery charge in kilowatt-hours (kWh) when leaving/arriving to a section. **Note:** Only EV cars are supported.

- `route` A <a href="sdk-for-flutter-explore-routing-route-class">Route</a> calculated using the online routing engine. Its <a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a> and the original route calculation options, along with EV related information like <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a>, will be used to compute the traffic on the route. The original route remains untouched.

- `lastTraveledSectionIndex` Indicates the index of the last traveled route section. Traveled part of the route won't be reused.

- `traveledDistanceOnLastSectionInMeters` Offset, in meters, to the last visited position on the route section defined by the last traveled section index.

- `currentChargeInKilowattHours` Charge level of the vehicle's battery at the current location (in kWh). It must be non-negative and less than or equal to the value of <a href="sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours">BatterySpecifications.totalCapacityInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. Sets <a href="sdk-for-flutter-explore-routing-batteryspecifications-initialchargeinkilowatthours">BatterySpecifications.initialChargeInKilowattHours</a> to the given value.

- `callback` Callback object that will be invoked after route traffic has been calculated. It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle calculateTrafficOnRouteWithCurrentCharge(Route route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, double currentChargeInKilowattHours, CalculateTrafficOnRouteCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


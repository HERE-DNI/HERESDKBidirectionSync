---
title: "LaneAccess constructor - LaneAccess - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-laneaccess-laneaccess"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LaneAccess.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/LaneAccess-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">LaneAccess</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">LaneAccess</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-automobiles" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">automobiles</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-buses" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">buses</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-taxis" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">taxis</span>, </span>
4.  <span id="sdk-for-flutter-navigate-param-carpools" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">carpools</span>, </span>
5.  <span id="sdk-for-flutter-navigate-param-pedestrians" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">pedestrians</span>, </span>
6.  <span id="sdk-for-flutter-navigate-param-trucks" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">trucks</span>, </span>
7.  <span id="sdk-for-flutter-navigate-param-throughTraffic" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">throughTraffic</span>, </span>
8.  <span id="sdk-for-flutter-navigate-param-deliveryVehicles" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">deliveryVehicles</span>, </span>
9.  <span id="sdk-for-flutter-navigate-param-emergencyVehicles" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">emergencyVehicles</span>, </span>
10. <span id="sdk-for-flutter-navigate-param-motorcycles" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">motorcycles</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `automobiles` Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.
- `buses` Buses that are used for public transportation.
- `taxis` Four-wheel vehicles that are usually fitted with a taximeter, that may be hired, along with their driver, to carry passengers to any specified destination.
- `carpools` Represents the sharing of car journeys so that more than one person travels in a car, and prevents the need for others to have to drive to a location themselves.
- `pedestrians` Persons traveling on foot, whether walking or running.
- `trucks` Large vehicles that range from medium to heavy duty trucks.
- `throughTraffic` Passenger vehicles (i.e., those defined as passenger car/automobiles) that are allowed to access roads that have traffic restrictions.
- `deliveryVehicles` Delivery <a href="sdk-for-flutter-navigate-navigation-laneaccess-trucks">LaneAccess.trucks</a> that are permitted to enter the city proper to unload goods at businesses.
- `emergencyVehicles` Any vehicle that is designated and authorized to respond to an emergency in a life-threatening situation.
- `motorcycles` Motorized two-wheeled passenger vehicles. Generally, mopeds are considered motorcycles.

</div>

## Implementation

``` dart
LaneAccess(this.automobiles, this.buses, this.taxis, this.carpools, this.pedestrians, this.trucks, this.throughTraffic, this.deliveryVehicles, this.emergencyVehicles, this.motorcycles);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

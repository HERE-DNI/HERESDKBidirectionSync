---
title: "TaxiOptions constructor - TaxiOptions - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-taxioptions-taxioptions"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/TaxiOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TaxiOptions</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TaxiOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-routeOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routeoptions-class">RouteOptions</a></span> <span class="parameter-name">routeOptions</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-textOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routetextoptions-class">RouteTextOptions</a></span> <span class="parameter-name">textOptions</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-avoidanceOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a></span> <span class="parameter-name">avoidanceOptions</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `routeOptions` Specifies the common route calculation options.
- `textOptions` Customize textual content returned from the route calculation, such as localization, format, and unit system.
- `avoidanceOptions` Options to specify restrictions for route calculations. By default no restrictions are applied.

</div>

## Implementation

``` dart
TaxiOptions(this.routeOptions, this.textOptions, this.avoidanceOptions)
    : tollOptions = TollOptions(), lastCharacterOfLicensePlate = null, maxSpeedOnSegments = [], allowDriveThroughTaxiRoads = true, carSpecifications = CarSpecifications();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


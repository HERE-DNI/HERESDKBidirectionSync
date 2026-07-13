---
title: "calculateIsoline method - IsolineRoutingEngine class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-isolineroutingengine-calculateisoline"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateIsoline.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/IsolineRoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">calculateIsoline</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">calculateIsoline</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-calculateIsoline-param-center" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span> <span class="parameter-name">center</span>, </span>
2.  <span id="sdk-for-flutter-navigate-calculateIsoline-param-isolineOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-isolineoptions-class">IsolineOptions</a></span> <span class="parameter-name">isolineOptions</span>, </span>
3.  <span id="sdk-for-flutter-navigate-calculateIsoline-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateisolinecallback">CalculateIsolineCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously calculates isolines to indicate the reachable area from a center point.

This finds all destinations that can be reached in a specific amount of time, a maximum travel distance, or even the charge level available in an electric vehicle. The result is a polygon area where each point is reachable within the provided limit.

- `center` Center point from which isolines are calculated. At minimum, the waypoint must contain the coordinates as point of origin.

- `isolineOptions` Options for isoline calculation.

- `callback` Callback object that will be invoked after isoline calculation. It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle calculateIsoline(Waypoint center, IsolineOptions isolineOptions, CalculateIsolineCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

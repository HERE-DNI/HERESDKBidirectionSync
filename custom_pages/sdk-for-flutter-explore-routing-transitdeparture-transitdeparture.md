---
title: "TransitDeparture constructor - TransitDeparture - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-transitdeparture-transitdeparture"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/TransitDeparture-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TransitDeparture</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TransitDeparture</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-place" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-routeplace-class">RoutePlace</a></span> <span class="parameter-name">place</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-time" class="parameter"><span class="type-annotation">DateTime?</span> <span class="parameter-name">time</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-delay" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">delay</span>, </span>
4.  <span id="sdk-for-flutter-explore-param-status" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-transitdeparturestatus">TransitDepartureStatus</a>?</span> <span class="parameter-name">status</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `place` The departure or arrival place.
- `time` Expected departure or arrival time of the event.
- `delay` The accumulated delay in seconds from the scheduled time of the event.
- `status` Status of the departure.

</div>

## Implementation

``` dart
TransitDeparture(this.place, this.time, this.delay, this.status);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


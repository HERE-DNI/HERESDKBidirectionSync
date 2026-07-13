---
title: "minTimeDifference property - DynamicRoutingEngineOptions class - trafficawarenavigation library - Dart API"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-mintimedifference"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- minTimeDifference.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficawarenavigation/DynamicRoutingEngineOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">minTimeDifference</span> property

</div>

<div class="section multi-line-signature">

Duration? <span class="name">minTimeDifference</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The minimum time difference, before notifying the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class">DynamicRoutingListener</a>. To get notified, the following check must be true: oldEstimatedTimeOfArrival - newEstimatedTimeOfArrival \> <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-mintimedifference">DynamicRoutingEngineOptions.minTimeDifference</a>. A value of 0 will be treated as `null` meaning no event will be sent. In order to receive events the difference needs to be greater than 0. Defaults to `null`.

</div>

## Implementation

``` dart
Duration? minTimeDifference;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

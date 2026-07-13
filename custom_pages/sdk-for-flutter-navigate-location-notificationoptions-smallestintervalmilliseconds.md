---
title: "smallestIntervalMilliseconds property - NotificationOptions class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-notificationoptions-smallestintervalmilliseconds"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- smallestIntervalMilliseconds.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/NotificationOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">smallestIntervalMilliseconds</span> property

</div>

<div class="section multi-line-signature">

int <span class="name">smallestIntervalMilliseconds</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Smallest allowed interval for position updates in milliseconds. It is guaranteed that positions are not provided more often than this value. Smallest interval could be used for throttling position updates, e.g. when each position update triggers CPU intensive calculations in the client application. This value is used as a minimum update interval when requesting GNSS location updates from the operating system. When hdEnabled is set to `true` in SatellitePositioningOptions, the smallest_interval_milliseconds value has a limited range. The SDK will adjust the value to allow location updates with a frequency of 1Hz to 10Hz (1000 ms to 100 ms, respectively). Default interval is 900 milliseconds.

</div>

## Implementation

``` dart
int smallestIntervalMilliseconds;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "verticalAccuracyInMeters property - Location class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-location-verticalaccuracyinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- verticalAccuracyInMeters.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/Location-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">verticalAccuracyInMeters</span> property

</div>

<div class="section multi-line-signature">

double? <span class="name">verticalAccuracyInMeters</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Estimated vertical accuracy. Given that the received Location contains the altitude, the real value of the altitude is estimated to lie within the following range: \[altitude - vertical accuracy, altitude + vertical accuracy\]. For example, when the altitude is equal to 50 and the vertical accuracy is 8, then the actual value is most likely in the range \[42, 58\].

</div>

## Implementation

``` dart
double? verticalAccuracyInMeters;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "axleCount property - TruckSpecifications class - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-truckspecifications-axlecount"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- axleCount.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/TruckSpecifications-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">axleCount</span> property

</div>

<div class="section multi-line-signature">

int? <span class="name">axleCount</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. Rendering `sdk.mapview.TruckProfile`: When set, truck restriction icons for an axle count greater than <a href="sdk-for-flutter-navigate-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a> will not be displayed. When specifying <a href="sdk-for-flutter-navigate-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a>, then <a href="sdk-for-flutter-navigate-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a> is required and must be greater than <a href="sdk-for-flutter-navigate-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a>.

</div>

## Implementation

``` dart
int? axleCount;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

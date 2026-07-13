---
title: "axleCount property - VehicleRestriction class - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-vehiclerestriction-axlecount"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- axleCount.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/VehicleRestriction-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">axleCount</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-core-integerrange-class">IntegerRange</a>? <span class="name">axleCount</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The axle count for which the current restriction applies. Can be used in conjunction with <a href="sdk-for-flutter-navigate-transport-restrictiontype">RestrictionType.weightPerAxleCount</a> to specify restriction based on weight per number of axles. The `axleCount` considers total number of axles on the whole vehicle (truck + trailers). This can be used to limit the weight per axle for the whole truck. If `axleCount` is null, the restriction is general and applies regardless of axle count. If the upper limit of the `axleCount` range is 0 or `null` then it means the restriction applies for values \>= lower limit, i.e. the upper limit of range if infinite or unbound. When a user taps the icon, the allowed `axleCount` range can be retrieved directly from `VehicleRestriction.axleCount`. Examples:

- (2,2) → Restriction applies to vehicles with exactly 2 axles.
- (2,4) → Restriction applies to vehicles with 2, 3, or 4 axles.
- (2, 0) → Restriction applies to vehicles with 2 or more axles (equivalent to 2...∞)

</div>

## Implementation

``` dart
IntegerRange? axleCount;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

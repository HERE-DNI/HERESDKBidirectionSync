---
title: "axleCountInGroup property - VehicleRestriction class - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-vehiclerestriction-axlecountingroup"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/VehicleRestriction-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">axleCountInGroup</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-core-integerrange-class">IntegerRange</a>? <span class="name">axleCountInGroup</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Number of axles in a group for which the current restriction applies. `axleCountInGroup` is a set of axles close together: single, tandem (2), triple (3), etc. Can be used in conjunction with <a href="sdk-for-flutter-navigate-transport-restrictiontype">RestrictionType.weightPerAxleGroup</a> to specify restriction based on weight per axle group. The `axleCountInGroup` considers number of axles in a specific axle group (usually rear axles on the truck or trailer). This can be used to limit weight for a tandem/triple rear axle group. If the upper limit of the `axleCountInGroup` range is 0 or `null` then it means the restriction applies for values \>= lower limit, i.e. the upper limit of range if infinite or unbound. Examples:

- (1,1) → Restriction applies to single axle group.
- (2,2) → Restriction applies to tandem axle group.
- (2,4) → Restriction applies to any axle group from 2 to 4 axles.
- (2,0) → Restriction applies to axle groups with 2 or more axles.

</div>

## Implementation

``` dart
IntegerRange? axleCountInGroup;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "details property - ViolatedRestriction class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-violatedrestriction-details"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/ViolatedRestriction-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">details</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-explore-routing-violatedrestrictiondetails-class">ViolatedRestrictionDetails</a>? <span class="name">details</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The detailed information of restriction depending on the specific violation. For time dependent restriction or transport mode restriction, this property will be null. For vehicle restriction, the corresponding member will be set, for example, if the vehicle violates the maximum allowed gross weight for a specific route, the max_gross_weight_in_kilograms will be set with the maximum allowed gross weight for this route.

</div>

## Implementation

``` dart
ViolatedRestrictionDetails? details;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "segments property - AvoidanceOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-avoidanceoptions-segments"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- segments.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/AvoidanceOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">segments</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-segmentreference-class">SegmentReference</a></span>\></span> <span class="name">segments</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Segments that routes will avoid going through. Violations are reported as <a href="sdk-for-flutter-explore-routing-sectionnoticecode">SectionNoticeCode.violatedBlockedRoad</a>.

**Notes:**

- This avoidance option is not supported in `IsolineOptions` for isoline calculation.
- The engine does not support an unlimited number of segments to avoid. The limit is defined by the HERE backend services and may change. For now, the maximum number of segments to avoid should be below 250. This value may change on the backend and it is therefore not guaranteed to be stable.

</div>

## Implementation

``` dart
List<SegmentReference> segments;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

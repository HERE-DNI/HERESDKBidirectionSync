---
title: "segmentHint property - Waypoint class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-waypoint-segmenthint"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Waypoint-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">segmentHint</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a>? <span class="name">segmentHint</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Optional segment hint causes the router to try and match to the specified segment. Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint. This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. Only topology segment id and travel direction are used to define the segment hint

**Note:** The feature is not supported by the `OfflineRoutingEngine`.

</div>

## Implementation

``` dart
SegmentReference? segmentHint;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


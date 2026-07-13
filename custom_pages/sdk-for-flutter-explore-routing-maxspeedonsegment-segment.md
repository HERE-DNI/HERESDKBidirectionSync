---
title: "segment property - MaxSpeedOnSegment class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-maxspeedonsegment-segment"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- segment.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/MaxSpeedOnSegment-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">segment</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-explore-routing-segmentreference-class">SegmentReference</a> <span class="name">segment</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A segment for which the new base speed is specified. Only the `segmendId` and `travelDirection` parameters are used, other parameters are ignored. Setting a `segmendId` is mandatory.

**Note:** The `SegmentReference` is not directly accessible from the map via the HERE SDK. Although, after route calculation you can retrieve the related segments for each <a href="sdk-for-flutter-explore-routing-span-class">Span</a>. The segment IDs are the same that are also used by, for example, the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/use-cases/avoid-segments.html">Routing REST API</a>. These IDs are mostly stable and only change when the underlying map data changes due to a new road or similar changes in the real world.

</div>

## Implementation

``` dart
SegmentReference segment;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

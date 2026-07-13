---
title: "MaxSpeedOnSegment constructor - MaxSpeedOnSegment - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-maxspeedonsegment-maxspeedonsegment"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MaxSpeedOnSegment.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/MaxSpeedOnSegment-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MaxSpeedOnSegment</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MaxSpeedOnSegment</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-segment" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-segmentreference-class">SegmentReference</a></span> <span class="parameter-name">segment</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-baseSpeedInMetersPerSecond" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">baseSpeedInMetersPerSecond</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `segment` A segment for which the new base speed is specified. Only the `segmendId` and `travelDirection` parameters are used, other parameters are ignored. Setting a `segmendId` is mandatory.

**Note:** The `SegmentReference` is not directly accessible from the map via the HERE SDK. Although, after route calculation you can retrieve the related segments for each <a href="sdk-for-flutter-explore-routing-span-class">Span</a>. The segment IDs are the same that are also used by, for example, the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/use-cases/avoid-segments.html">Routing REST API</a>. These IDs are mostly stable and only change when the underlying map data changes due to a new road or similar changes in the real world.

- `baseSpeedInMetersPerSecond` New maximum value in m/s of baseSpeed on segment. The provided value must be in the range \[1.0, 70.0\]. Cannot increase base speed on segment. If the value is greater than the default base speed, then such penalty will have no effect.

</div>

## Implementation

``` dart
MaxSpeedOnSegment(this.segment, this.baseSpeedInMetersPerSecond);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

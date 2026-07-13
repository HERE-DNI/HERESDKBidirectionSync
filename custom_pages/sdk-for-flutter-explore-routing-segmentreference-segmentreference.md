---
title: "SegmentReference constructor - SegmentReference - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-segmentreference-segmentreference"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/SegmentReference-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">SegmentReference</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">SegmentReference</span>(<wbr></wbr>\<a href="sdk-for-flutter-explore-routing-traveldirection">

1.  <span id="sdk-for-flutter-explore-param-segmentId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">segmentId</span> = <span class="default-value">""</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-travelDirection" class="parameter"><span class="type-annotation">[TravelDirection</a></span> <span class="parameter-name">travelDirection</span> = <span class="default-value">TravelDirection.bidirectional</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-offsetStart" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">offsetStart</span> = <span class="default-value">0.0</span>, </span>
4.  <span id="sdk-for-flutter-explore-param-offsetEnd" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">offsetEnd</span> = <span class="default-value">1.0</span>, </span>
5.  <span id="sdk-for-flutter-explore-param-tilePartitionId" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">tilePartitionId</span> = <span class="default-value">0</span>, </span>
6.  <span id="sdk-for-flutter-explore-param-localId" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">localId</span> = <span class="default-value">0</span>, </span>

\])

</div>

<div class="section desc markdown">

Creates a new instance.

- `segmentId` Topology segment id representing a unique identifier within the HERE platform catalogs.
- `travelDirection` Travel direction of the segment.
- `offsetStart` The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)
- `offsetEnd` The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)
- `tilePartitionId` HERE tile partition id (Morton-encoding + level indicator) of the segment. As in HERE Map Content.
- `localId` Local ID of the segment inside the OCM tile.

</div>

## Implementation

``` dart
SegmentReference([String segmentId = "", TravelDirection travelDirection = TravelDirection.bidirectional, double offsetStart = 0.0, double offsetEnd = 1.0, int tilePartitionId = 0, int? localId = 0])
  : segmentId = segmentId, travelDirection = travelDirection, offsetStart = offsetStart, offsetEnd = offsetEnd, tilePartitionId = tilePartitionId, localId = localId;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


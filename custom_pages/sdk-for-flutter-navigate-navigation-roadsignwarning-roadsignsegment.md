---
title: "roadSignSegment property - RoadSignWarning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-roadsignwarning-roadsignsegment"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RoadSignWarning-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">roadSignSegment</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a> <span class="name">roadSignSegment</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The reference to the segment where the road sign is located. It can be used to identify the location of the road sign. It allows to compare the road sign location with the `MapMatchedLocation.segment_reference` provided by the `NavigableLocationListener` or with the <a href="sdk-for-flutter-navigate-routing-span-segmentreference">Span.segmentReference</a> available in the Route's Span. By combining it with the geometry of the segment, that can be loaded using <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-class">SegmentDataLoader</a>, it is possible to identify the road sign's coordinates.

</div>

## Implementation

``` dart
SegmentReference roadSignSegment;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


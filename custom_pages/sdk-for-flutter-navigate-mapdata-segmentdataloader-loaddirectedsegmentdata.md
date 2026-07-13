---
title: "loadDirectedSegmentData method - SegmentDataLoader class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/SegmentDataLoader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">loadDirectedSegmentData</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a></span> <span class="name">loadDirectedSegmentData</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-loadDirectedSegmentData-param-segment" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-directedocmsegmentid-class">DirectedOCMSegmentId</a></span> <span class="parameter-name">segment</span>, </span>
2.  <span id="sdk-for-flutter-navigate-loadDirectedSegmentData-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a></span> <span class="parameter-name">options</span></span>

)

</div>

<div class="section desc markdown">

Synchronously load the data for the given map directed segment.

- `segment` The directed segment to load.

- `options` Request options

Returns <a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a>. Requested data of a segment.

Throws <a href="sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class">MapDataLoaderExceptionException</a>. Specifies reason, why list of data of a segment is not returned.

</div>

## Implementation

``` dart
SegmentData loadDirectedSegmentData(DirectedOCMSegmentId segment, SegmentDataLoaderOptions options);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


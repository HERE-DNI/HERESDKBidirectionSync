---
title: "getSegmentsAroundCoordinates method - SegmentDataLoader class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-segmentdataloader-getsegmentsaroundcoordinates"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/SegmentDataLoader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getSegmentsAroundCoordinates</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-ocmsegmentid-class">OCMSegmentId</a></span>\></span></span> <span class="name">getSegmentsAroundCoordinates</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getSegmentsAroundCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span>
2.  <span id="sdk-for-flutter-navigate-getSegmentsAroundCoordinates-param-radiusInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">radiusInMeters</span></span>

)

</div>

<div class="section desc markdown">

Loads the segments around a certain coordinates.

Returns an empty list in case no segments could be found around the coordinates.

- `coordinates` The location to explore

- `radiusInMeters` The radius of the search. Only values between 1m and 5000m are accepted.

Returns `List<OCMSegmentId>`. The list of segments around the given position.

The segments are sorted by distance from the point. Throws if it's not possible to return list of a list of segments.

Throws <a href="sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class">MapDataLoaderExceptionException</a>. Specifies reason, why list of a list of segments is not returned.

</div>

## Implementation

``` dart
List<OCMSegmentId> getSegmentsAroundCoordinates(GeoCoordinates coordinates, double radiusInMeters);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


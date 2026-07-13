---
title: "trafficSignals property - SegmentData class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-segmentdata-trafficsignals"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trafficSignals.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/SegmentData-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">trafficSignals</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-trafficsignal-class">TrafficSignal</a></span>\></span>?</span> <span class="name">trafficSignals</span>

</div>

<div class="section desc markdown">

The list of <a href="sdk-for-flutter-navigate-mapdata-trafficsignal-class">TrafficSignal</a> of the given segment. Returns an empty list if no data is found. Returns `null` if <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtrafficsignals">SegmentDataLoaderOptions.loadTrafficSignals</a> is set to `false`. The <a href="sdk-for-flutter-navigate-mapdata-trafficsignallocation">TrafficSignalLocation</a> indicates the location of a single traffic signal, which can be any combination of left, right and overhead. The <a href="sdk-for-flutter-navigate-mapdata-trafficsignal-offsetinmeters">TrafficSignal.offsetInMeters</a> is the location along the segment, while the traffic signal location have details on how the traffic signal is display/deploy in that specific location in the segment. Gets the list of <a href="sdk-for-flutter-navigate-mapdata-trafficsignal-class">TrafficSignal</a>.

</div>

## Implementation

``` dart
List<TrafficSignal>? get trafficSignals;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "TrafficLocation constructor - TrafficLocation - traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-trafficlocation-trafficlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficLocation.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/TrafficLocation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TrafficLocation</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TrafficLocation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-polyline" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geopolyline-class">GeoPolyline</a></span> <span class="parameter-name">polyline</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-additionalPolylines" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geopolyline-class">GeoPolyline</a></span>\></span></span> <span class="parameter-name">additionalPolylines</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-lengthInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">lengthInMeters</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `polyline` The polyline representing the traffic entity shape. The current field contains a continuous polyline with no gaps between geo-coordinates. All others following the gap are present in the `additional_polylines` field.
- `additionalPolylines` List of polylines that were not included in continuous polyline. Use this to fill any gaps in the continuous polyline.
- `lengthInMeters` The affected road length in meters. The length can be 0 only if the incident supplier has provided incomplete data.

</div>

## Implementation

``` dart
TrafficLocation(this.polyline, this.additionalPolylines, this.lengthInMeters)
    : description = "";
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "visibilityRanges property - MapMarker3D class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmarker3d-visibilityranges"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker3D-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">visibilityRanges</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapmeasurerange-class">MapMeasureRange</a></span>\></span></span> <span class="name">visibilityRanges</span>

</div>

<div class="section desc markdown">

The list of visibility ranges. The 3D marker is visible only inside these map measure ranges. A range is half open - \<a href="sdk-for-flutter-explore-mapview-mapmarker3d-s">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

When empty (the default), the 3D marker is visible without map measure restrictions. Only [MapMeasureRange</a> of <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> type are supported. <a href="sdk-for-flutter-explore-mapview-mapmarker3d-s">MapMeasureRange</a> of other unsupported types will be ignored. Gets the list of visibility ranges.

</div>

## Implementation

``` dart
List<MapMeasureRange> get visibilityRanges;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">visibilityRanges=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-visibilityRanges-param-value" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapmeasurerange-class">MapMeasureRange</a></span>\></span></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The list of visibility ranges. The 3D marker is visible only inside these map measure ranges. A range is half open - \<a href="sdk-for-flutter-explore-mapview-mapmarker3d-s">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

When empty (the default), the 3D marker is visible without map measure restrictions. Only [MapMeasureRange</a> of <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> type are supported. <a href="sdk-for-flutter-explore-mapview-mapmarker3d-s">MapMeasureRange</a> of other unsupported types will be ignored. Sets visibility ranges for this 3D marker.

</div>

## Implementation

``` dart
set visibilityRanges(List<MapMeasureRange> value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


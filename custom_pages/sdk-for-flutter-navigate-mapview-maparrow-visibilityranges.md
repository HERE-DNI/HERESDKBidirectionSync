---
title: "visibilityRanges property - MapArrow class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-maparrow-visibilityranges"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- visibilityRanges.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapArrow-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">visibilityRanges</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmeasurerange-class">MapMeasureRange</a></span>\></span></span> <span class="name">visibilityRanges</span>

</div>

<div class="section desc markdown">

The list of visibility ranges, in which the map arrow is visible. A range is half-open - \<a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

When empty (the default), the map arrows are visible without map measure restrictions. Only `MapMeasureRange`(s) of [MapMeasureKind.zoomLevel</a> type are supported. `MapMeasureRange`(s) of other unsupported types will be ignored.} Gets the list of visibility ranges.

</div>

## Implementation

``` dart
List<MapMeasureRange> get visibilityRanges;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">visibilityRanges=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-visibilityRanges-param-value" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmeasurerange-class">MapMeasureRange</a></span>\></span></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The list of visibility ranges, in which the map arrow is visible. A range is half-open - \<a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

When empty (the default), the map arrows are visible without map measure restrictions. Only `MapMeasureRange`(s) of [MapMeasureKind.zoomLevel</a> type are supported. `MapMeasureRange`(s) of other unsupported types will be ignored.} Sets visibility ranges for this map arrow.

</div>

## Implementation

``` dart
set visibilityRanges(List<MapMeasureRange> value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "measureDependentTailWidth property - MapArrow class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-maparrow-measuredependenttailwidth"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapArrow-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">measureDependentTailWidth</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a></span>, <span class="type-parameter">double</span>\></span></span> <span class="name">measureDependentTailWidth</span>

</div>

<div class="section desc markdown">

The width of the arrow tail in pixels, where the key is a <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> and the value is a tail width in pixels at this <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a>. Gets the <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> dependent arrow tail width in pixels.

If tail width was configured without <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> dependency, then `measureDependentTailWidth` contains single entry with measure 0 of type <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> and width value equal to `widthInPixels`.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
Map<MapMeasure, double> get measureDependentTailWidth;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">measureDependentTailWidth=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-measureDependentTailWidth-param-value" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a></span>, <span class="type-parameter">double</span>\></span></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The width of the arrow tail in pixels, where the key is a <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> and the value is a tail width in pixels at this <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a>. Sets the <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> dependent arrow tail width in pixels.

The width values are linearly interpolated between nearest map entries. Width values for <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> outside the map entries are kept constant, using the value of the largest/smallest key.

Only <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> of <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> type is supported. Other <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> types are unsupported and hence, will be ignored.

Map with a single entry is equivalent to use of the `widthInPixels` value in the constructor, so a constant width setting, independent of camera.

Empty input is ignored and existing width is maintained.

The width values should be positive. Map entries with width values less than or equal to 0 are ignored.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
set measureDependentTailWidth(Map<MapMeasure, double> value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


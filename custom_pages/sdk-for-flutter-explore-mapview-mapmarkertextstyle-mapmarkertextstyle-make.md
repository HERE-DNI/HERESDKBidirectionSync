---
title: "MapMarkerTextStyle.make constructor - MapMarkerTextStyle - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmarkertextstyle-mapmarkertextstyle-make"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarkerTextStyle.make.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarkerTextStyle-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMarkerTextStyle.make</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMarkerTextStyle.make</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-make-param-textSize" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">textSize</span>, </span>
2.  <span id="sdk-for-flutter-explore-make-param-textColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">textColor</span>, </span>
3.  <span id="sdk-for-flutter-explore-make-param-textOutlineSize" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">textOutlineSize</span>, </span>
4.  <span id="sdk-for-flutter-explore-make-param-textOutlineColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">textOutlineColor</span>, </span>
5.  <span id="sdk-for-flutter-explore-make-param-placements" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapmarkertextstyleplacement">MapMarkerTextStylePlacement</a></span>\></span></span> <span class="parameter-name">placements</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a set of styling options for the text of a <a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a>.

List of placements is used to specify allowed placement of text relative to the icon. When marker overlapping is allowed as set by <a href="sdk-for-flutter-explore-mapview-mapmarker-isoverlapallowed">MapMarker.isOverlapAllowed</a>, only first placement element is considered. Otherwise the placement value is chosen so that the text does not overlap with other `MapMarker` instances.

Placement values are prioritized according to the order in which they appear in the list. Lists with duplicate entries as well as empty lists are not supported.

- `textSize` The size of the text in pixels. Only positive values are supported.

- `textColor` The text color.

- `textOutlineSize` The size of the text outline in pixels. Only non-negative values are supported.

- `textOutlineColor` The color of the text outline.

- `placements` List of allowed placements of the text relative to the icon of a <a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a>.

Throws <a href="sdk-for-flutter-explore-mapview-mapmarkertextstyleinstantiationexception-class">MapMarkerTextStyleInstantiationException</a>. In case of invalid input parameters.

</div>

## Implementation

``` dart
factory MapMarkerTextStyle.make(double textSize, ui.Color textColor, double textOutlineSize, ui.Color textOutlineColor, List<MapMarkerTextStylePlacement> placements) => $prototype.make(textSize, textColor, textOutlineSize, textOutlineColor, placements);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "MapMarkerTextStyle.withFont constructor - MapMarkerTextStyle - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarkertextstyle-mapmarkertextstyle-withfont"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarkerTextStyle.withFont.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarkerTextStyle-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMarkerTextStyle.withFont</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMarkerTextStyle.withFont</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withFont-param-textSize" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">textSize</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withFont-param-textColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">textColor</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withFont-param-textOutlineSize" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">textOutlineSize</span>, </span>
4.  <span id="sdk-for-flutter-navigate-withFont-param-textOutlineColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">textOutlineColor</span>, </span>
5.  <span id="sdk-for-flutter-navigate-withFont-param-placements" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmarkertextstyleplacement">MapMarkerTextStylePlacement</a></span>\></span></span> <span class="parameter-name">placements</span>, </span>
6.  <span id="sdk-for-flutter-navigate-withFont-param-fontName" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">fontName</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a set of styling options for the text of a <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

List of placements is used to specify allowed placement of text relative to the icon. When marker overlapping is allowed as set by <a href="sdk-for-flutter-navigate-mapview-mapmarker-isoverlapallowed">MapMarker.isOverlapAllowed</a>, only first placement element is considered. Otherwise the placement value is chosen so that the text does not overlap with other `MapMarker` instances.

Placement values are prioritized according to the order in which they appear in the list. Lists with duplicate entries as well as empty lists are not supported.

- `textSize` The size of the text in pixels. Only positive values are supported.

- `textColor` The text color.

- `textOutlineSize` The size of the text outline in pixels. Only non-negative values are supported.

- `textOutlineColor` The color of the text outline.

- `placements` List of allowed placements of the text relative to the icon of a <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>.

- `fontName` Font name, registered with `AssetsManager.registerFont`. If empty string is provided, a default font will be used.

Throws <a href="sdk-for-flutter-navigate-mapview-mapmarkertextstyleinstantiationexception-class">MapMarkerTextStyleInstantiationException</a>. In case of invalid input parameters.

</div>

## Implementation

``` dart
factory MapMarkerTextStyle.withFont(double textSize, ui.Color textColor, double textOutlineSize, ui.Color textOutlineColor, List<MapMarkerTextStylePlacement> placements, String fontName) => $prototype.withFont(textSize, textColor, textOutlineSize, textOutlineColor, placements, fontName);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

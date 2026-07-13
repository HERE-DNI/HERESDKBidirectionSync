---
title: "setMultiColors method - MapPolylineSolidMultiColorRepresentation class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolylinesolidmulticolorrepresentation-setmulticolors"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolylineSolidMultiColorRepresentation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setMultiColors</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">setMultiColors</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setMultiColors-param-colorStops" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>\></span></span> <span class="parameter-name">colorStops</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setMultiColors-param-colorIndices" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">colorIndices</span>, </span>
3.  <span id="sdk-for-flutter-navigate-setMultiColors-param-colors" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">Color</span>\></span></span> <span class="parameter-name">colors</span></span>

)

</div>

<div class="section desc markdown">

Sets lists of colors and multiple color segment stops for the polyline to be colored in.

When this representation is already set on any `MapPolyline`, values will be applied on that `MapPolyline` right away. If this representation is not set on any `MapPolyline`, values will be applied once representation is set on a `MapPolyline`.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

- `colorStops` List containing color stop values indicating a change of color on a polyline. Color stops must be in the range of \[0.0, 1.0\]. Color stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3, 1.0). Duplicate values are not allowed. Color stop list must be of the same size as color indices list. Maximum size is 100 color stops. An empty list is not allowed. The first color stop value in the list must be 0.0.

- `colorIndices` List of color indices (from the color list) corresponding to the color stops. Value range is: \[0, (color list size - 1)\]. Values outside of the range are not allowed. Color indices list must be of the same size as color stop list. Maximum size is 100 color indices.

- `colors` List of colors. Maximum size is 16 colors. An empty list is not allowed.

Returns `bool`. Value indicating whether parameters are valid and can be applied.

</div>

## Implementation

``` dart
bool setMultiColors(List<double> colorStops, List<int> colorIndices, List<ui.Color> colors);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


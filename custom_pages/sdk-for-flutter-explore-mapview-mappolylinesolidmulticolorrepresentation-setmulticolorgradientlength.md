---
title: "setMultiColorGradientLength method - MapPolylineSolidMultiColorRepresentation class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-setmulticolorgradientlength"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolylineSolidMultiColorRepresentation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setMultiColorGradientLength</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">setMultiColorGradientLength</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-setMultiColorGradientLength-param-length" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">length</span></span>

)

</div>

<div class="section desc markdown">

Sets the multiple color segment gradient length.

Colors of two adjacent color segments can be blended to have a nicer visual appeal. Blending produces color gradient of specific length which is part of the color segment being blended.

Start of the segment is blended with a color from the previous segment. Blending length is specified as a ratio of the smallest color segment length (from the list of color stops). E.g. a value of '0.1' means 10% of the length of the smallest segment will be blended with a color from its previous segment. For this smallest segment gradient length is applied as-is, for all other segments it is scaled proportionally based on the smallest segment's size to other segment size ratio.

Length of '0.0' is the default value which means blending will not be applied. Valid value range is \[0.0, 1.0\]. Out of range values are not supported. When this representation is already set on any `MapPolyline`, value will be applied on that `MapPolyline` right away. If this representation is not set on any `MapPolyline`, value will be applied once representation is set on a `MapPolyline`.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

- `length` Multiple color segment gradient length. Length of '0.0' is the default value which means blending will not be applied. Valid value range is \[0.0, 1.0\]. Out of range values are not supported.

Returns `bool`. Value indicating whether specified value is valid and can be applied.

</div>

## Implementation

``` dart
bool setMultiColorGradientLength(double length);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


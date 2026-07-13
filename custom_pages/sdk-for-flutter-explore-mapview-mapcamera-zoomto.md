---
title: "zoomTo method - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcamera-zoomto"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- zoomTo.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">zoomTo</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">zoomTo</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-zoomTo-param-zoomLevel" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">zoomLevel</span></span>

)

</div>

<div class="section desc markdown">

Zooms to the specified zoom level.

The supplied value will be clamped to the range of \[0, 22\], where 0 is a view of whole globe and 22 is street level.

This effectively changes the distance from the camera to the target. The zooming occurs around the current target point.

- `zoomLevel` The zoom level to set, clamped to the range of \[0, 22\].

</div>

## Implementation

``` dart
void zoomTo(double zoomLevel);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

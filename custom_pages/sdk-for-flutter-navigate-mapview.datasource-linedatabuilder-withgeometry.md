---
title: "withGeometry method - LineDataBuilder class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-linedatabuilder-withgeometry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withGeometry.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/LineDataBuilder-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">withGeometry</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-datasource-linedatabuilder-class">LineDataBuilder</a></span> <span class="name">withGeometry</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withGeometry-param-geometry" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a></span> <span class="parameter-name">geometry</span></span>

)

</div>

<div class="section desc markdown">

Configures the builder with geometry for line to be created.

- `geometry` Geometry of the polyline. Each vertex defines two line segments: one with a previous vertex and one with a next vertex. First and last vertices don't have resp. previous and next vertices and thus belong to single line segments. Consecutive duplicate vertices are ignored. Altitude of polyline vertices is ignored.

Returns <a href="sdk-for-flutter-navigate-mapview-datasource-linedatabuilder-class">LineDataBuilder</a>. The builder.

</div>

## Implementation

``` dart
LineDataBuilder withGeometry(GeoPolyline geometry);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

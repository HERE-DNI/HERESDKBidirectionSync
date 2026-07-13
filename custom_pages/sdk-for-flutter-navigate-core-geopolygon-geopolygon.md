---
title: "GeoPolygon constructor - GeoPolygon - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-geopolygon-geopolygon"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoPolygon.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoPolygon-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">GeoPolygon</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">GeoPolygon</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-vertices" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">vertices</span></span>

)

</div>

<div class="section desc markdown">

Constructs an instance of this class from the provided vertices.

Throws InstantiationError if the number of vertices is less than three.

- `vertices` List of vertices representing the polygon outer boundary in clockwise order.

Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. Instantiation error.

</div>

## Implementation

``` dart
factory GeoPolygon(List<GeoCoordinates> vertices) => $prototype.$init(vertices);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

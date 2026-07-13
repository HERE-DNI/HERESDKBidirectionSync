---
title: "triangle method - MeshBuilder class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-meshbuilder-triangle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- triangle.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MeshBuilder-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">triangle</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-trianglemeshbuilder-class">TriangleMeshBuilder</a></span> <span class="name">triangle</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-triangle-param-a" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">a</span>, </span>
2.  <span id="sdk-for-flutter-navigate-triangle-param-b" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">b</span>, </span>
3.  <span id="sdk-for-flutter-navigate-triangle-param-c" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">c</span></span>

)

</div>

<div class="section desc markdown">

Adds a triangle.

Triangle visibility is determined via back-face culling. Front-facing triangles are expected to have counter-clockwise winding.

- `a` First vertex of the triangle.

- `b` Second vertex of the triangle.

- `c` Third vertex of the triangle.

Returns <a href="sdk-for-flutter-navigate-mapview-trianglemeshbuilder-class">TriangleMeshBuilder</a>. A <a href="sdk-for-flutter-navigate-mapview-trianglemeshbuilder-class">TriangleMeshBuilder</a> instance.

</div>

## Implementation

``` dart
TriangleMeshBuilder triangle(Point3D a, Point3D b, Point3D c);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

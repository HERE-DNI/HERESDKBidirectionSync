---
title: "quad method - MeshBuilder class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-meshbuilder-quad"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- quad.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MeshBuilder-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">quad</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-quadmeshbuilder-class">QuadMeshBuilder</a></span> <span class="name">quad</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-quad-param-a" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">a</span>, </span>
2.  <span id="sdk-for-flutter-navigate-quad-param-b" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">b</span>, </span>
3.  <span id="sdk-for-flutter-navigate-quad-param-c" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">c</span>, </span>
4.  <span id="sdk-for-flutter-navigate-quad-param-d" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">d</span>, </span>

)

</div>

<div class="section desc markdown">

Adds a quad.

Internally, this will be transformed into triangles abc and bdc.

Triangle visibility is determined via back-face culling. Front-facing triangles are expected to have counter-clockwise winding.

- `a` First vertex of quad.

- `b` Second vertex of the quad.

- `c` Third vertex of the quad.

- `d` Fourth vertex of the quad.

Returns <a href="sdk-for-flutter-navigate-mapview-quadmeshbuilder-class">QuadMeshBuilder</a>. A <a href="sdk-for-flutter-navigate-mapview-quadmeshbuilder-class">QuadMeshBuilder</a> instance.

</div>

## Implementation

``` dart
QuadMeshBuilder quad(Point3D a, Point3D b, Point3D c, Point3D d);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

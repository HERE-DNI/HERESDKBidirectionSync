---
title: "withTextureCoordinates method - TriangleMeshBuilder class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-trianglemeshbuilder-withtexturecoordinates"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/TriangleMeshBuilder-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">withTextureCoordinates</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-meshbuilder-class">MeshBuilder</a></span> <span class="name">withTextureCoordinates</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withTextureCoordinates-param-a" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">a</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withTextureCoordinates-param-b" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">b</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withTextureCoordinates-param-c" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">c</span></span>

)

</div>

<div class="section desc markdown">

Adds texture coordinates to a triangle.

Coordinates are specified as `<u,v>` with `<0,0>` representing the bottom-left and `<1,1>` upper-right corner.

- `a` Texture coordinate for vertex a. See <a href="sdk-for-flutter-navigate-mapview-meshbuilder-triangle">MeshBuilder.triangle</a>

- `b` Texture coordinate for vertex b. See <a href="sdk-for-flutter-navigate-mapview-meshbuilder-triangle">MeshBuilder.triangle</a>

- `c` Texture coordinate for vertex c. See <a href="sdk-for-flutter-navigate-mapview-meshbuilder-triangle">MeshBuilder.triangle</a>

Returns <a href="sdk-for-flutter-navigate-mapview-meshbuilder-class">MeshBuilder</a>. A <a href="sdk-for-flutter-navigate-mapview-meshbuilder-class">MeshBuilder</a> instance.

</div>

## Implementation

``` dart
MeshBuilder withTextureCoordinates(Anchor2D a, Anchor2D b, Anchor2D c);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


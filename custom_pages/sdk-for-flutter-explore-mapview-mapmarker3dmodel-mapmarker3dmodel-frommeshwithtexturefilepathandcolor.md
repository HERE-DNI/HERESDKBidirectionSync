---
title: "MapMarker3DModel.fromMeshWithTextureFilePathAndColor constructor - MapMarker3DModel - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmarker3dmodel-mapmarker3dmodel-frommeshwithtexturefilepathandcolor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3DModel.fromMeshWithTextureFilePathAndColor.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker3DModel-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMarker3DModel.fromMeshWithTextureFilePathAndColor</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMarker3DModel.fromMeshWithTextureFilePathAndColor</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-fromMeshWithTextureFilePathAndColor-param-mesh" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mesh-class">Mesh</a></span> <span class="parameter-name">mesh</span>, </span>
2.  <span id="sdk-for-flutter-explore-fromMeshWithTextureFilePathAndColor-param-textureFilePath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">textureFilePath</span>, </span>
3.  <span id="sdk-for-flutter-explore-fromMeshWithTextureFilePathAndColor-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span></span>

)

</div>

<div class="section desc markdown">

Creates a new 3D model from mesh, texture and color.

- `mesh` Mesh containing the 3d geometry together with texture coordinates.

- `textureFilePath` Absolute path to texture file.

- `color` Color to be blend with texture. This color is multiplied with color of texture.

Throws <a href="sdk-for-flutter-explore-mapview-mapmarker3dmodelinstantiationexception-class">MapMarker3DModelInstantiationException</a>. Indicates what went wrong when the instantiation was attempted.

</div>

## Implementation

``` dart
factory MapMarker3DModel.fromMeshWithTextureFilePathAndColor(Mesh mesh, String textureFilePath, ui.Color color) => $prototype.fromMeshWithTextureFilePathAndColor(mesh, textureFilePath, color);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

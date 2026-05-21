---
title: "Map Marker3DModel"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapMarker3DModel///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/MapMarker3DModel</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Marker3DModel</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">Represents a 3D model that can be used by a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d to be shown on the map. Geometry of 3D marker can be provided in form of a Wavefront OBJ file as specified in http://www.martinreddy.net/gfx/3d/OBJ.spec or as mesh built via /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder.</p><h1 class="">1. Creating <code class="lang-kotlin">MapMarker3DModel</code> from OBJ file</h1><p class="paragraph">For OBJ files, HERE SDK only supports the following set of features of the OBJ specification:</p><ul><li><p class="paragraph">Triangle Meshes</p></li><li><p class="paragraph">Following vertex attributes must be present:</p></li><li><p class="paragraph">Vertex Position</p></li><li><p class="paragraph">Vertex Normal</p></li><li><p class="paragraph">Texture Coordinates</p></li><li><p class="paragraph">Geometry must be indexed (contain an Index Buffer)</p></li><li><p class="paragraph">Face element</p></li></ul><p class="paragraph">HERE SDK does not support:</p><ul><li><p class="paragraph">Multi Texturing</p></li><li><p class="paragraph">Materials (mtllib \[external .mtl file name\] )</p></li><li><p class="paragraph">Lines</p></li><li><p class="paragraph">Higher Order Surfaces</p></li><li><p class="paragraph">Vendor specific extensions</p></li></ul><p class="paragraph">For supported texture formats, HERE SDK allows the following formats to be specified: JPG, PNG, GPU compressed texture formats: ECT1 (OpenGL only), YUV, ASTC, KTX.</p><h1 class="">2. Creating <code class="lang-kotlin">MapMarker3DModel</code> programatically</h1><p class="paragraph">A 3D mesh can be specified programatically using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder and passed to <code class="lang-kotlin">MapMarker3DModel</code> constructor. This method supports creating a mesh from quads and triangles. Textured geometry is also supported, the mesh faces need to have texture coordinates and a texture file needs to be passed along with the mesh to <code class="lang-kotlin">MapMarker3DModel</code> constructor.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="MapMarker3DModel" data-filterable-set=":modules:dokkaHtml/release" data-name="451140155%2FConstructors%2F1617540583" id="451140155%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model-map-marker3-d-model</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(geometryFilePath: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, textureFilePath: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, color: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color)</div><div class="brief"><p class="paragraph">Creates a new 3D model from path to .obj file, texture and color.</p></div><div class="symbol monospace">constructor(mesh: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh, textureFilePath: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, color: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color)</div><div class="brief"><p class="paragraph">Creates a new 3D model from mesh, texture and color.</p></div><div class="symbol monospace">constructor(geometryFilePath: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, textureFilePath: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>)</div><div class="brief"><p class="paragraph">Creates a new 3D model from path to .obj file and texture.</p></div><div class="symbol monospace">constructor(mesh: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh, textureFilePath: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>)</div><div class="brief"><p class="paragraph">Creates a new 3D model from mesh and texture.</p></div><div class="symbol monospace">constructor(geometryFilePath: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>)</div><div class="brief"><p class="paragraph">Creates a new 3D model from path to .obj file.</p></div><div class="symbol monospace">constructor(mesh: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh)</div><div class="brief"><p class="paragraph">Creates a new 3D model from a mesh.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="574327262%2FClasslikes%2F1617540583" id="574327262%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model-companion</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="InstantiationErrorCode" data-filterable-set=":modules:dokkaHtml/release" data-name="-17325744%2FClasslikes%2F1617540583" id="-17325744%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model-instantiation-error-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">enum /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model-instantiation-error-code : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model-instantiation-error-code&gt; </div><div class="brief"><p class="paragraph">Indicates the reason for a failure to create /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="InstantiationException" data-filterable-set=":modules:dokkaHtml/release" data-name="-280668586%2FClasslikes%2F1617540583" id="-280668586%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model-instantiation-exception</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model-instantiation-exception(val error: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model-instantiation-error-code) : <a href="https://developer.android.com/reference/kotlin/java/lang/Exception.html">Exception</a></div><div class="brief"><p class="paragraph">Thrown when a problem occurs while trying to create /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker3-d-model.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="footer">
<a class="footer--button footer--button_go-to-top" href="#content" id="go-to-top-link"></a>
© 2026 Copyright

Generated by 
<a class="footer--link footer--link_external" href="https://github.com/Kotlin/dokka">
dokka
</a>

</div>
</div>

</div>

</div>
`
}</HTMLBlock>

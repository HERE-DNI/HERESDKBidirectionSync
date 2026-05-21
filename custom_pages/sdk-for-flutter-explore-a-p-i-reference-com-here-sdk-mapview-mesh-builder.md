---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MeshBuilder///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/MeshBuilder</div>
<div class="cover">
<h1 class="cover">Mesh<wbr/>Builder</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">Builder for meshes. Such meshes can contain different kinds of primitives, like quads or triangles. Both primitives support adding texture coordinates that are mapped to the corners of the primitives. See /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-triangle-mesh-builder and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-quad-mesh-builder for more details.</p><p class="paragraph">Note: Normals cannot be set as they are not necessary when using the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder.</p><p class="paragraph"><strong>Example how to build a cube using </strong>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-quad-mesh-builder</p><div class="sample-container"><pre><code class="block lang-kotlin" theme="idea">Mesh cube = new MeshBuilder()<br/>    .quad(new Point3D(0.5, 0.5, 0.5),<br/>        new Point3D(-0.5, 0.5, 0.5),<br/>        new Point3D(0.5, -0.5, 0.5),<br/>        new Point3D(-0.5, -0.5, 0.5))<br/>    .quad(new Point3D(-0.5, 0.5, -0.5),<br/>        new Point3D(0.5, 0.5, -0.5),<br/>        new Point3D(-0.5, -0.5, -0.5),<br/>        new Point3D(0.5, -0.5, -0.5))<br/>    .quad(new Point3D(0.5, 0.5, -0.5),<br/>        new Point3D(0.5, 0.5, 0.5),<br/>        new Point3D(0.5, -0.5, -0.5),<br/>        new Point3D(0.5, -0.5, 0.5))<br/>    .quad(new Point3D(-0.5, 0.5, 0.5),<br/>        new Point3D(-0.5, 0.5, -0.5),<br/>        new Point3D(-0.5, -0.5, 0.5),<br/>        new Point3D(-0.5, -0.5, -0.5))<br/>    .quad(new Point3D(-0.5, 0.5, 0.5),<br/>        new Point3D(0.5, 0.5, 0.5),<br/>        new Point3D(-0.5, 0.5, -0.5),<br/>        new Point3D(0.5, 0.5, -0.5))<br/>    .quad(new Point3D(0.5, -0.5, 0.5),<br/>        new Point3D(-0.5, -0.5, 0.5),<br/>        new Point3D(0.5, -0.5, -0.5),<br/>        new Point3D(-0.5, -0.5, -0.5))<br/>    .build();</code></pre><div class="copy-popup-wrapper popup-to-left">Content copied to clipboard</div></div><h4 class="">Inheritors</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-quad-mesh-builder</div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-triangle-mesh-builder</div></div></div></div></div></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="MeshBuilder" data-filterable-set=":modules:dokkaHtml/release" data-name="-450595613%2FConstructors%2F1617540583" id="-450595613%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder-mesh-builder</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Constructs an instance of MeshBuilder.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="1363862584%2FClasslikes%2F1617540583" id="1363862584%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="build" data-filterable-set=":modules:dokkaHtml/release" data-name="-274825661%2FFunctions%2F1617540583" id="-274825661%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder-build</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder-build(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh?</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="quad" data-filterable-set=":modules:dokkaHtml/release" data-name="1268032301%2FFunctions%2F1617540583" id="1268032301%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder-quad</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder-quad(a: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point3-d, b: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point3-d, c: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point3-d, d: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point3-d): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-quad-mesh-builder</div><div class="brief"><p class="paragraph">Adds a quad. Internally, this will be transformed into triangles abc and bdc.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="triangle" data-filterable-set=":modules:dokkaHtml/release" data-name="-843619262%2FFunctions%2F1617540583" id="-843619262%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder-triangle</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder-triangle(a: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point3-d, b: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point3-d, c: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point3-d): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-triangle-mesh-builder</div><div class="brief"><p class="paragraph">Adds a triangle.</p></div></div></div>
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

---
title: "MapMarker3DModel (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapMarker3DModel.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapMarker3DModel</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapMarker3DModel</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Represents a 3D model that can be used by a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d" title="class in com.here.sdk.mapview"><code>MapMarker3D</code></a> to be shown on the map.
 Geometry of 3D marker can be provided in form of a Wavefront OBJ file as specified in
 http://www.martinreddy.net/gfx/3d/OBJ.spec or as mesh built via <a href="sdk-for-android-navigate-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview"><code>MeshBuilder</code></a>.
 
For OBJ files, HERE SDK only supports the following set of features of the OBJ specification:
 <ul>
<li>Triangle Meshes</li>
<li>Following vertex attributes must be present:
 <ul>
<li>Vertex Position</li>
<li>Vertex Normal</li>
<li>Texture Coordinates</li>
<li>Geometry must be indexed (contain an Index Buffer)</li>
<li>Face element</li>
</ul>
</li>
</ul>
HERE SDK does not support:
 <ul>
<li>Multi Texturing</li>
<li>Materials (mtllib [external .mtl file name] )
 <ul>
<li>Lines</li>
<li>Higher Order Surfaces</li>
<li>Vendor specific extensions</li>
</ul>
</li>
</ul>
For supported texture formats, HERE SDK allows the following formats to be specified:
 JPG, PNG, GPU compressed texture formats: ECT1 (OpenGL only), YUV, ASTC, KTX.
 
A 3D mesh can be specified programatically using <a href="sdk-for-android-navigate-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview"><code>MeshBuilder</code></a> and passed to
 <code>MapMarker3DModel</code> constructor. This method supports creating a mesh from
 quads and triangles. Textured geometry is also supported, the mesh faces
 need to have texture coordinates and a texture file needs to be passed
 along with the mesh to <code>MapMarker3DModel</code> constructor.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel-instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapMarker3DModel.InstantiationErrorCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates the reason for a failure to create <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview"><code>MapMarker3DModel</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel-instantiationexception" title="class in com.here.sdk.mapview">MapMarker3DModel.InstantiationException</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Thrown when a problem occurs while trying to create <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview"><code>MapMarker3DModel</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel#%3Cinit%3E(com.here.sdk.mapview.Mesh)">MapMarker3DModel</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mesh" title="class in com.here.sdk.mapview">Mesh</a> mesh)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new 3D model from a mesh.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel#%3Cinit%3E(com.here.sdk.mapview.Mesh,java.lang.String)">MapMarker3DModel</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mesh" title="class in com.here.sdk.mapview">Mesh</a> mesh,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> textureFilePath)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new 3D model from mesh and texture.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel#%3Cinit%3E(com.here.sdk.mapview.Mesh,java.lang.String,com.here.sdk.core.Color)">MapMarker3DModel</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mesh" title="class in com.here.sdk.mapview">Mesh</a> mesh,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> textureFilePath,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new 3D model from mesh, texture and color.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel#%3Cinit%3E(java.lang.String)">MapMarker3DModel</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> geometryFilePath)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new 3D model from path to .obj file.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel#%3Cinit%3E(java.lang.String,java.lang.String)">MapMarker3DModel</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> geometryFilePath,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> textureFilePath)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new 3D model from path to .obj file and texture.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel#%3Cinit%3E(java.lang.String,java.lang.String,com.here.sdk.core.Color)">MapMarker3DModel</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> geometryFilePath,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> textureFilePath,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new 3D model from path to .obj file, texture and color.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,com.here.sdk.core.Color)">
<h3>MapMarker3DModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarker3DModel</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> geometryFilePath,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> textureFilePath,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color)</span></div>
<div class="block"><p>Creates a new 3D model from path to .obj file, texture and color.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geometryFilePath</code> - <p>Absolute path to obj file.</p></dd>
<dd><code>textureFilePath</code> - <p>Absolute path to texture file.</p></dd>
<dd><code>color</code> - <p>Color to be blend with texture.
     This color is multiplied with color of texture.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.Mesh,java.lang.String,com.here.sdk.core.Color)">
<h3>MapMarker3DModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarker3DModel</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mesh" title="class in com.here.sdk.mapview">Mesh</a> mesh,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> textureFilePath,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color)</span>
                 throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel-instantiationexception" title="class in com.here.sdk.mapview">MapMarker3DModel.InstantiationException</a></span></div>
<div class="block"><p>Creates a new 3D model from mesh, texture and color.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mesh</code> - <p>Mesh containing the 3d geometry together with texture coordinates.</p></dd>
<dd><code>textureFilePath</code> - <p>Absolute path to texture file.</p></dd>
<dd><code>color</code> - <p>Color to be blend with texture.
     This color is multiplied with color of texture.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel-instantiationexception" title="class in com.here.sdk.mapview">MapMarker3DModel.InstantiationException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String)">
<h3>MapMarker3DModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarker3DModel</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> geometryFilePath,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> textureFilePath)</span></div>
<div class="block"><p>Creates a new 3D model from path to .obj file and texture.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geometryFilePath</code> - <p>Absolute path to obj file.</p></dd>
<dd><code>textureFilePath</code> - <p>Absolute path to texture file.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.Mesh,java.lang.String)">
<h3>MapMarker3DModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarker3DModel</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mesh" title="class in com.here.sdk.mapview">Mesh</a> mesh,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> textureFilePath)</span>
                 throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel-instantiationexception" title="class in com.here.sdk.mapview">MapMarker3DModel.InstantiationException</a></span></div>
<div class="block"><p>Creates a new 3D model from mesh and texture.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mesh</code> - <p>Mesh containing the 3d geometry together with texture coordinates.</p></dd>
<dd><code>textureFilePath</code> - <p>Absolute path to texture file.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel-instantiationexception" title="class in com.here.sdk.mapview">MapMarker3DModel.InstantiationException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>MapMarker3DModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarker3DModel</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> geometryFilePath)</span></div>
<div class="block"><p>Creates a new 3D model from path to .obj file.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geometryFilePath</code> - <p>Absolute path to obj file.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.Mesh)">
<h3>MapMarker3DModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarker3DModel</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mesh" title="class in com.here.sdk.mapview">Mesh</a> mesh)</span></div>
<div class="block"><p>Creates a new 3D model from a mesh.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mesh</code> - <p>Mesh containing the 3d geometry 3D data.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>

---
title: "MeshBuilder Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-meshbuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MeshBuilder.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/MeshBuilder"></a>
<a title="MeshBuilder Class Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Maps.html">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MeshBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class MeshBuilder</code></pre>
<pre><code>extension MeshBuilder: NativeBase</code></pre>
<pre><code>extension MeshBuilder: Hashable</code></pre>
</div>
</div>
<p>Builder for meshes. Such meshes can contain different kinds of primitives, like quads or
triangles. Both primitives support adding texture coordinates that are mapped to the
corners of the primitives. See <code><a href="../Classes/TriangleMeshBuilder.html">TriangleMeshBuilder</a></code> and <code><a href="../Classes/QuadMeshBuilder.html">QuadMeshBuilder</a></code> for more details.</p>
<p>Note: Normals cannot be set as they are not necessary when using the <code>MeshBuilder</code>.</p>
<p><strong>Example how to build a cube using <code><a href="../Classes/QuadMeshBuilder.html">QuadMeshBuilder</a></code></strong></p>
<pre><code>let cube = MeshBuilder()
.quad(a: Point3D(x: 0.5, y: 0.5, z: 0.5),
b: Point3D(x: -0.5, y: 0.5, z: 0.5),
c: Point3D(x: 0.5, y: -0.5, z: 0.5),
d: Point3D(x: -0.5, y: -0.5, z: 0.5))
.quad(a: Point3D(x: -0.5, y: 0.5, z: -0.5),
b: Point3D(x: 0.5, y: 0.5, z: -0.5),
c: Point3D(x: -0.5, y: -0.5, z: -0.5),
d: Point3D(x: 0.5, y: -0.5, z: -0.5))
.quad(a: Point3D(x: 0.5, y: 0.5, z: -0.5),
b: Point3D(x: 0.5, y: 0.5, z: 0.5),
c: Point3D(x: 0.5, y: -0.5, z: -0.5),
d: Point3D(x: 0.5, y: -0.5, z: 0.5))
.quad(a: Point3D(x: -0.5, y: 0.5, z: 0.5),
b: Point3D(x: -0.5, y: 0.5, z: -0.5),
c: Point3D(x: -0.5, y: -0.5, z: 0.5),
d: Point3D(x: -0.5, y: -0.5, z: -0.5))
.quad(a: Point3D(x: -0.5, y: 0.5, z: 0.5),
b: Point3D(x: 0.5, y: 0.5, z: 0.5),
c: Point3D(x: -0.5, y: 0.5, z: -0.5),
d: Point3D(x: 0.5, y: 0.5, z: -0.5))
.quad(a: Point3D(x: 0.5, y: -0.5, z: 0.5),
b: Point3D(x: -0.5, y: -0.5, z: 0.5),
c: Point3D(x: 0.5, y: -0.5, z: -0.5),
d: Point3D(x: -0.5, y: -0.5, z: -0.5))
.build()</code></pre>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MeshBuilderCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk11MeshBuilderCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs an instance of MeshBuilder.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init()</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MeshBuilderC8triangle1a1b1cAA08TrianglebC0CAA7Point3DV_A2KtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/triangle(a:b:c:)"></a>
<a class="token" href="#/s:7heresdk11MeshBuilderC8triangle1a1b1cAA08TrianglebC0CAA7Point3DV_A2KtF">triangle(a:<wbr/>b:<wbr/>c:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a triangle.</p>
<p>Triangle visibility is determined via back-face culling. Front-facing
triangles are expected to have counter-clockwise winding.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func triangle(a: Point3D, b: Point3D, c: Point3D) -&gt; TriangleMeshBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>a</em>
</code>
</td>
<td>
<div>
<p>First vertex of the triangle.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>b</em>
</code>
</td>
<td>
<div>
<p>Second vertex of the triangle.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>c</em>
</code>
</td>
<td>
<div>
<p>Third vertex of the triangle.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>A <code><a href="../Classes/TriangleMeshBuilder.html">TriangleMeshBuilder</a></code> instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MeshBuilderC4quad1a1b1c1dAA04QuadbC0CAA7Point3DV_A3LtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/quad(a:b:c:d:)"></a>
<a class="token" href="#/s:7heresdk11MeshBuilderC4quad1a1b1c1dAA04QuadbC0CAA7Point3DV_A3LtF">quad(a:<wbr/>b:<wbr/>c:<wbr/>d:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a quad. Internally, this will be transformed into triangles abc and bdc.</p>
<p>Triangle visibility is determined via back-face culling. Front-facing triangles are expected to have
counter-clockwise winding.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func quad(a: Point3D, b: Point3D, c: Point3D, d: Point3D) -&gt; QuadMeshBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>a</em>
</code>
</td>
<td>
<div>
<p>First vertex of quad.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>b</em>
</code>
</td>
<td>
<div>
<p>Second vertex of the quad.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>c</em>
</code>
</td>
<td>
<div>
<p>Third vertex of the quad.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>d</em>
</code>
</td>
<td>
<div>
<p>Fourth vertex of the quad.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>A <code><a href="../Classes/QuadMeshBuilder.html">QuadMeshBuilder</a></code> instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MeshBuilderC5buildAA0B0CSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk11MeshBuilderC5buildAA0B0CSgyF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func build() -&gt; Mesh?</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>mesh containing added geometry or ‘null’ if no geometry was added.</p>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>



</div>
`
}</HTMLBlock>

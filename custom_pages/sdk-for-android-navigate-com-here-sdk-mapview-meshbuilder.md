---
title: "MeshBuilder (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-meshbuilder"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MeshBuilder.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MeshBuilder</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-quadmeshbuilder" title="class in com.here.sdk.mapview">QuadMeshBuilder</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-trianglemeshbuilder" title="class in com.here.sdk.mapview">TriangleMeshBuilder</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public class </span><span className="element-name type-name-label">MeshBuilder</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Builder for meshes. Such meshes can contain different kinds of primitives, like quads or
 triangles. Both primitives support adding texture coordinates that are mapped to the
 corners of the primitives. See <a href="sdk-for-android-navigate-com-here-sdk-mapview-trianglemeshbuilder" title="class in com.here.sdk.mapview"><code>TriangleMeshBuilder</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-mapview-quadmeshbuilder" title="class in com.here.sdk.mapview"><code>QuadMeshBuilder</code></a> for more details.
 Note: Normals cannot be set as they are not necessary when using the <a href="sdk-for-android-navigate-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview"><code>MeshBuilder</code></a>.
 <strong>Example how to build a cube using <a href="sdk-for-android-navigate-com-here-sdk-mapview-quadmeshbuilder" title="class in com.here.sdk.mapview"><code>QuadMeshBuilder</code></a></strong>
<pre><code>    Mesh cube = new MeshBuilder()
         .quad(new Point3D(0.5, 0.5, 0.5),
             new Point3D(-0.5, 0.5, 0.5),
             new Point3D(0.5, -0.5, 0.5),
             new Point3D(-0.5, -0.5, 0.5))
         .quad(new Point3D(-0.5, 0.5, -0.5),
             new Point3D(0.5, 0.5, -0.5),
             new Point3D(-0.5, -0.5, -0.5),
             new Point3D(0.5, -0.5, -0.5))
         .quad(new Point3D(0.5, 0.5, -0.5),
             new Point3D(0.5, 0.5, 0.5),
             new Point3D(0.5, -0.5, -0.5),
             new Point3D(0.5, -0.5, 0.5))
         .quad(new Point3D(-0.5, 0.5, 0.5),
             new Point3D(-0.5, 0.5, -0.5),
             new Point3D(-0.5, -0.5, 0.5),
             new Point3D(-0.5, -0.5, -0.5))
         .quad(new Point3D(-0.5, 0.5, 0.5),
             new Point3D(0.5, 0.5, 0.5),
             new Point3D(-0.5, 0.5, -0.5),
             new Point3D(0.5, 0.5, -0.5))
         .quad(new Point3D(0.5, -0.5, 0.5),
             new Point3D(-0.5, -0.5, 0.5),
             new Point3D(0.5, -0.5, -0.5),
             new Point3D(-0.5, -0.5, -0.5))
         .build();
 </code></pre></p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-meshbuilder#%3Cinit%3E()">MeshBuilder</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs an instance of MeshBuilder.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>MeshBuilder</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MeshBuilder</span>()</div>
<div className="block"><p>Constructs an instance of MeshBuilder.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)">
<h3>triangle</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-trianglemeshbuilder" title="class in com.here.sdk.mapview">TriangleMeshBuilder</a></span> <span className="element-name">triangle</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point3d" title="class in com.here.sdk.core">Point3D</a> a,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point3d" title="class in com.here.sdk.core">Point3D</a> b,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point3d" title="class in com.here.sdk.core">Point3D</a> c)</span></div>
<div className="block"><p>Adds a triangle.
 Triangle visibility is determined via back-face culling. Front-facing
 triangles are expected to have counter-clockwise winding.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - <p>First vertex of the triangle.</p></dd>
<dd><code>b</code> - <p>Second vertex of the triangle.</p></dd>
<dd><code>c</code> - <p>Third vertex of the triangle.</p></dd>
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-trianglemeshbuilder" title="class in com.here.sdk.mapview"><code>TriangleMeshBuilder</code></a> instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)">
<h3>quad</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-quadmeshbuilder" title="class in com.here.sdk.mapview">QuadMeshBuilder</a></span> <span className="element-name">quad</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point3d" title="class in com.here.sdk.core">Point3D</a> a,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point3d" title="class in com.here.sdk.core">Point3D</a> b,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point3d" title="class in com.here.sdk.core">Point3D</a> c,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point3d" title="class in com.here.sdk.core">Point3D</a> d)</span></div>
<div className="block"><p>Adds a quad. Internally, this will be transformed into triangles abc and bdc.
 Triangle visibility is determined via back-face culling. Front-facing triangles are expected to have
 counter-clockwise winding.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - <p>First vertex of quad.</p></dd>
<dd><code>b</code> - <p>Second vertex of the quad.</p></dd>
<dd><code>c</code> - <p>Third vertex of the quad.</p></dd>
<dd><code>d</code> - <p>Fourth vertex of the quad.</p></dd>
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-quadmeshbuilder" title="class in com.here.sdk.mapview"><code>QuadMeshBuilder</code></a> instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="build()">
<h3>build</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mesh" title="class in com.here.sdk.mapview">Mesh</a></span> <span className="element-name">build</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>mesh containing added geometry or 'null' if no geometry was added.</p></dd>
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

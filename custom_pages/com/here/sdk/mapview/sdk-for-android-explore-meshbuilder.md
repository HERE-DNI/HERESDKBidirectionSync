---
title: "MeshBuilder (API Reference)"
slug: "sdk-for-android-explore-meshbuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MeshBuilder.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="../../../../index.html">Overview</a></li>
<li><a href="package-summary.html">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="package-tree.html">Tree</a></li>
<li><a href="../../../../deprecated-list.html">Deprecated</a></li>
<li><a href="../../../../index-all.html">Index</a></li>
<li><a href="../../../../help-doc.html#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../NativeBase.html" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MeshBuilder</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="QuadMeshBuilder.html" title="class in com.here.sdk.mapview">QuadMeshBuilder</a></code>, <code><a href="TriangleMeshBuilder.html" title="class in com.here.sdk.mapview">TriangleMeshBuilder</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">MeshBuilder</span>
<span class="extends-implements">extends <a href="../../NativeBase.html" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Builder for meshes. Such meshes can contain different kinds of primitives, like quads or
 triangles. Both primitives support adding texture coordinates that are mapped to the
 corners of the primitives. See <a href="TriangleMeshBuilder.html" title="class in com.here.sdk.mapview"><code>TriangleMeshBuilder</code></a> and <a href="QuadMeshBuilder.html" title="class in com.here.sdk.mapview"><code>QuadMeshBuilder</code></a> for more details.
 <p>Note: Normals cannot be set as they are not necessary when using the <a href="MeshBuilder.html" title="class in com.here.sdk.mapview"><code>MeshBuilder</code></a>.
 <p><strong>Example how to build a cube using <a href="QuadMeshBuilder.html" title="class in com.here.sdk.mapview"><code>QuadMeshBuilder</code></a></strong>
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
 </code></pre></p></p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MeshBuilder</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs an instance of MeshBuilder.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Mesh.html" title="class in com.here.sdk.mapview">Mesh</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#build()">build</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="QuadMeshBuilder.html" title="class in com.here.sdk.mapview">QuadMeshBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)">quad</a><wbr/>(<a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> a,
 <a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> b,
 <a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> c,
 <a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a quad.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="TriangleMeshBuilder.html" title="class in com.here.sdk.mapview">TriangleMeshBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)">triangle</a><wbr/>(<a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> a,
 <a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> b,
 <a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> c)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a triangle.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>MeshBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MeshBuilder</span>()</div>
<div class="block"><p>Constructs an instance of MeshBuilder.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)">
<h3>triangle</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="TriangleMeshBuilder.html" title="class in com.here.sdk.mapview">TriangleMeshBuilder</a></span> <span class="element-name">triangle</span><wbr/><span class="parameters">(@NonNull
 <a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> a,
 @NonNull
 <a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> b,
 @NonNull
 <a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> c)</span></div>
<div class="block"><p>Adds a triangle.
 <p>Triangle visibility is determined via back-face culling. Front-facing
 triangles are expected to have counter-clockwise winding.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - <p>First vertex of the triangle.</p></dd>
<dd><code>b</code> - <p>Second vertex of the triangle.</p></dd>
<dd><code>c</code> - <p>Third vertex of the triangle.</p></dd>
<dt>Returns:</dt>
<dd><p>A <a href="TriangleMeshBuilder.html" title="class in com.here.sdk.mapview"><code>TriangleMeshBuilder</code></a> instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)">
<h3>quad</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="QuadMeshBuilder.html" title="class in com.here.sdk.mapview">QuadMeshBuilder</a></span> <span class="element-name">quad</span><wbr/><span class="parameters">(@NonNull
 <a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> a,
 @NonNull
 <a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> b,
 @NonNull
 <a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> c,
 @NonNull
 <a href="../core/Point3D.html" title="class in com.here.sdk.core">Point3D</a> d)</span></div>
<div class="block"><p>Adds a quad. Internally, this will be transformed into triangles abc and bdc.
 <p>Triangle visibility is determined via back-face culling. Front-facing triangles are expected to have
 counter-clockwise winding.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - <p>First vertex of quad.</p></dd>
<dd><code>b</code> - <p>Second vertex of the quad.</p></dd>
<dd><code>c</code> - <p>Third vertex of the quad.</p></dd>
<dd><code>d</code> - <p>Fourth vertex of the quad.</p></dd>
<dt>Returns:</dt>
<dd><p>A <a href="QuadMeshBuilder.html" title="class in com.here.sdk.mapview"><code>QuadMeshBuilder</code></a> instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="build()">
<h3>build</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="Mesh.html" title="class in com.here.sdk.mapview">Mesh</a></span> <span class="element-name">build</span>()</div>
<dl class="notes">
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
</main>
</div>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>

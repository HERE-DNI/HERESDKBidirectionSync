---
title: "QuadMeshBuilder (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-mapview-quadmeshbuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- QuadMeshBuilder.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-..-..-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance"><a href="sdk-for-android-navigate-meshbuilder" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MeshBuilder</a>
<div class="inheritance">com.here.sdk.mapview.QuadMeshBuilder</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">QuadMeshBuilder</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a></span></div>
<div class="block"><p>Builder for a single quad.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#withTextureCoordinates(com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D)">withTextureCoordinates</a><wbr/>(<a href="sdk-for-android-navigate-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> a,
 <a href="sdk-for-android-navigate-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> b,
 <a href="sdk-for-android-navigate-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> c,
 <a href="sdk-for-android-navigate-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> d)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds texture coordinates to a quad.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.here.sdk.mapview.MeshBuilder">Methods inherited from class com.here.sdk.mapview.<a href="sdk-for-android-navigate-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a></h3>
<code><a href="sdk-for-android-navigate-meshbuilder#build()">build</a>, <a href="sdk-for-android-navigate-meshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)">quad</a>, <a href="sdk-for-android-navigate-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)">triangle</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="withTextureCoordinates(com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D)">
<h3>withTextureCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a></span> <span class="element-name">withTextureCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> a,
 @NonNull
 <a href="sdk-for-android-navigate-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> b,
 @NonNull
 <a href="sdk-for-android-navigate-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> c,
 @NonNull
 <a href="sdk-for-android-navigate-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> d)</span></div>
<div class="block"><p>Adds texture coordinates to a quad. Coordinates are specified as <code>&lt;u,v&gt;</code> with <code>&lt;0,0&gt;</code>
 representing the bottom-left and <code>&lt;1,1&gt;</code> upper-right corner.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - <p>Texture coordinate for vertex a. See <a href="sdk-for-android-navigate-meshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)"><code>MeshBuilder.quad(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)</code></a></p></dd>
<dd><code>b</code> - <p>Texture coordinate for vertex b. See <a href="sdk-for-android-navigate-meshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)"><code>MeshBuilder.quad(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)</code></a></p></dd>
<dd><code>c</code> - <p>Texture coordinate for vertex c. See <a href="sdk-for-android-navigate-meshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)"><code>MeshBuilder.quad(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)</code></a></p></dd>
<dd><code>d</code> - <p>Texture coordinate for vertex d. See <a href="sdk-for-android-navigate-meshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)"><code>MeshBuilder.quad(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)</code></a></p></dd>
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-meshbuilder" title="class in com.here.sdk.mapview"><code>MeshBuilder</code></a> instance.</p></dd>
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



</div>
`
}</HTMLBlock>

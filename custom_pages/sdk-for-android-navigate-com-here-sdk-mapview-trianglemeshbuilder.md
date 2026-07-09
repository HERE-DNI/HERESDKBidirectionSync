---
title: "TriangleMeshBuilder (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-trianglemeshbuilder"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TriangleMeshBuilder.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MeshBuilder</a>
<div className="inheritance">com.here.sdk.mapview.TriangleMeshBuilder</div>
</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TriangleMeshBuilder</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a></span></div>
<div className="block"><p>Builder for a single triangle.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-com.here.sdk.mapview.MeshBuilder">Methods inherited from class com.here.sdk.mapview.<a href="sdk-for-android-navigate-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a></h3>
<code><a href="sdk-for-android-navigate-meshbuilder#build()">build</a>, <a href="sdk-for-android-navigate-meshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)">quad</a>, <a href="sdk-for-android-navigate-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)">triangle</a></code></div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="withTextureCoordinates(com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D)">
<h3>withTextureCoordinates</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a></span> <span className="element-name">withTextureCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> a,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> b,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> c)</span></div>
<div className="block"><p>Adds texture coordinates to a triangle. Coordinates are specified as <code><u,v></u,v></code> with <code>&lt;0,0&gt;</code>
 representing the bottom-left and <code>&lt;1,1&gt;</code> upper-right corner.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - <p>Texture coordinate for vertex a. See <a href="sdk-for-android-navigate-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)"><code>MeshBuilder.triangle(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)</code></a></p></dd>
<dd><code>b</code> - <p>Texture coordinate for vertex b. See <a href="sdk-for-android-navigate-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)"><code>MeshBuilder.triangle(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)</code></a></p></dd>
<dd><code>c</code> - <p>Texture coordinate for vertex c. See <a href="sdk-for-android-navigate-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)"><code>MeshBuilder.triangle(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)</code></a></p></dd>
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview"><code>MeshBuilder</code></a> instance.</p></dd>
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

---
title: "TriangleMeshBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-trianglemeshbuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TriangleMeshBuilder.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-meshbuilder" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MeshBuilder</a>
<div class="inheritance">com.here.sdk.mapview.TriangleMeshBuilder</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">TriangleMeshBuilder</span>
<span class="extends-implements">extends <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a></span></div>
<div class="block"><p>Builder for a single triangle.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#withTextureCoordinates(com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D)">withTextureCoordinates</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> a,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> b,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> c)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds texture coordinates to a triangle.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.here.sdk.mapview.MeshBuilder">Methods inherited from class com.here.sdk.mapview.<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a></h3>
<code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-meshbuilder#build()">build</a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-meshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)">quad</a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)">triangle</a></code></div>
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
<section class="detail" id="withTextureCoordinates(com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D)">
<h3>withTextureCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a></span> <span class="element-name">withTextureCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> a,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> b,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> c)</span></div>
<div class="block"><p>Adds texture coordinates to a triangle. Coordinates are specified as <code>&lt;u,v&gt;</code> with <code>&lt;0,0&gt;</code>
 representing the bottom-left and <code>&lt;1,1&gt;</code> upper-right corner.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - <p>Texture coordinate for vertex a. See <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)"><code>MeshBuilder.triangle(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)</code></a></p></dd>
<dd><code>b</code> - <p>Texture coordinate for vertex b. See <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)"><code>MeshBuilder.triangle(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)</code></a></p></dd>
<dd><code>c</code> - <p>Texture coordinate for vertex c. See <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)"><code>MeshBuilder.triangle(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)</code></a></p></dd>
<dt>Returns:</dt>
<dd><p>A <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-meshbuilder" title="class in com.here.sdk.mapview"><code>MeshBuilder</code></a> instance.</p></dd>
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
`
}</HTMLBlock>

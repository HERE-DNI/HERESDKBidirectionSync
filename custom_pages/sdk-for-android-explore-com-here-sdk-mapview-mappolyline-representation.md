---
title: "MapPolyline.Representation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapPolyline.Representation.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance"><a href="sdk-for-android-explore-com-here-sdk-mapview-mapitemrepresentation" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MapItemRepresentation</a>
<div class="inheritance">com.here.sdk.mapview.MapPolyline.Representation</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline.dashimagerepresentation" title="class in com.here.sdk.mapview">MapPolyline.DashImageRepresentation</a></code>, <code><a href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline.dashrepresentation" title="class in com.here.sdk.mapview">MapPolyline.DashRepresentation</a></code>, <code><a href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline.solidmulticolorrepresentation" title="class in com.here.sdk.mapview">MapPolyline.SolidMultiColorRepresentation</a></code>, <code><a href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline.solidrepresentation" title="class in com.here.sdk.mapview">MapPolyline.SolidRepresentation</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a></dd>
</dl>

<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">MapPolyline.Representation</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-com-here-sdk-mapview-mapitemrepresentation" title="class in com.here.sdk.mapview">MapItemRepresentation</a></span></div>
<div class="block"><p>Base class to represent the visual appearance of a <a href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview"><code>MapPolyline</code></a>.</p></div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline.representation.instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationErrorCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Describes a reason for failing to create a <a href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline.representation" title="class in com.here.sdk.mapview"><code>MapPolyline.Representation</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Thrown when a problem occurs while trying to create <a href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline.representation" title="class in com.here.sdk.mapview"><code>MapPolyline.Representation</code></a>.</div>
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
<!-- ========= END OF CLASS DATA ========= -->






</div>
`
}</HTMLBlock>

---
title: "MapPolyline.Representation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapPolyline.Representation.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapitemrepresentation" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MapItemRepresentation</a>
<div className="inheritance">com.here.sdk.mapview.MapPolyline.Representation</div>
</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashimagerepresentation" title="class in com.here.sdk.mapview">MapPolyline.DashImageRepresentation</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashrepresentation" title="class in com.here.sdk.mapview">MapPolyline.DashRepresentation</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation" title="class in com.here.sdk.mapview">MapPolyline.SolidMultiColorRepresentation</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-solidrepresentation" title="class in com.here.sdk.mapview">MapPolyline.SolidRepresentation</a></code></dd>
</dl>
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static class </span><span className="element-name type-name-label">MapPolyline.Representation</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapitemrepresentation" title="class in com.here.sdk.mapview">MapItemRepresentation</a></span></div>
<div className="block"><p>Base class to represent the visual appearance of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview"><code>MapPolyline</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationErrorCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">Describes a reason for failing to create a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation" title="class in com.here.sdk.mapview"><code>MapPolyline.Representation</code></a>.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Thrown when a problem occurs while trying to create <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation" title="class in com.here.sdk.mapview"><code>MapPolyline.Representation</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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

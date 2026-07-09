---
title: "PolylineSimplificationCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-polylinesimplificationcallback"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PolylineSimplificationCallback.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span className="modifiers">public interface </span><span className="element-name type-name-label">PolylineSimplificationCallback</span></div>
<div className="block"><p>The method will be called on the main thread when
 <a href="sdk-for-android-navigate-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.geocoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</com.here.sdk.core.geocoordinates></code></a> is finished.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
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
<section className="detail" id="onPolylineSimplified(com.here.sdk.core.PolylineSimplificationError,java.util.List)">
<h3>onPolylineSimplified</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onPolylineSimplified</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplificationerror" title="enum class in com.here.sdk.core">PolylineSimplificationError</a> queryError,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; result)</span></div>
<div className="block"><p>The method will be called on the main thread when
 <a href="sdk-for-android-navigate-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.geocoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</com.here.sdk.core.geocoordinates></code></a> is finished.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>queryError</code> - <p>The optional error, which occurred during
     simplification.</p></dd>
<dd><code>result</code> - <p>The simplified polyline with number of
     points less or equal to the input polyline
     of <a href="sdk-for-android-navigate-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.geocoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</com.here.sdk.core.geocoordinates></code></a>.</p></dd>
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

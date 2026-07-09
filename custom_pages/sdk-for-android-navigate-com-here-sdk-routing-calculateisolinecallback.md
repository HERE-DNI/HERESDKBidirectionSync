---
title: "CalculateIsolineCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-calculateisolinecallback"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- CalculateIsolineCallback.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span className="modifiers">public interface </span><span className="element-name type-name-label">CalculateIsolineCallback</span></div>
<div className="block"><p>A function which is called by the RoutingEngine after isoline calculation has completed.
 It is always called on the main thread.
 The first argument is the error in case of a failure. It is <code>null</code> for an operation that succeeds.
 The second argument holds a list of calculated isolines. The list is <code>null</code> in case of an error.
 The size of the list matches the size of the provided sdk.routing.IsolineOptions.range_values:
 For each range limit, one isoline is calculated.</p></div>
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
<section className="detail" id="onIsolineCalculated(com.here.sdk.routing.RoutingError,java.util.List)">
<h3>onIsolineCalculated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onIsolineCalculated</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a> routingError,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-isoline" title="class in com.here.sdk.routing">Isoline</a>&gt; isolines)</span></div>
<div className="block"><p>A function which is called by the RoutingEngine after isoline calculation has completed.
 It is always called on the main thread.
 The first argument is the error in case of a failure. It is <code>null</code> for an operation that succeeds.
 The second argument holds a list of calculated isolines. The list is <code>null</code> in case of an error.
 The size of the list matches the size of the provided sdk.routing.IsolineOptions.range_values:
 For each range limit, one isoline is calculated.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>routingError</code> - <p>The error in case of a failure. It is <code>null</code> for an operation that succeeds.</p></dd>
<dd><code>isolines</code> - <p>Holds a list of calculated isolines. The list is <code>null</code> in case of an error.</p></dd>
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

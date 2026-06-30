---
title: "PolylineSimplificationCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-polylinesimplificationcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PolylineSimplificationCallback.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">PolylineSimplificationCallback</span></div>
<div class="block"><p>The method will be called on the main thread when
 <a href="sdk-for-android-explore-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List&lt;com.here.sdk.core.GeoCoordinates&gt;, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</code></a> is finished.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-polylinesimplificationcallback#onPolylineSimplified(com.here.sdk.core.PolylineSimplificationError,java.util.List)">onPolylineSimplified</a><wbr/>(<a href="sdk-for-android-explore-polylinesimplificationerror" title="enum class in com.here.sdk.core">PolylineSimplificationError</a> queryError,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; result)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The method will be called on the main thread when
 <a href="sdk-for-android-explore-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List&lt;com.here.sdk.core.GeoCoordinates&gt;, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</code></a> is finished.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="onPolylineSimplified(com.here.sdk.core.PolylineSimplificationError,java.util.List)">
<h3>onPolylineSimplified</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onPolylineSimplified</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-explore-polylinesimplificationerror" title="enum class in com.here.sdk.core">PolylineSimplificationError</a> queryError,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; result)</span></div>
<div class="block"><p>The method will be called on the main thread when
 <a href="sdk-for-android-explore-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List&lt;com.here.sdk.core.GeoCoordinates&gt;, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</code></a> is finished.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>queryError</code> - <p>The optional error, which occurred during
     simplification.</p></dd>
<dd><code>result</code> - <p>The simplified polyline with number of
     points less or equal to the input polyline
     of <a href="sdk-for-android-explore-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)"><code>PolylineSimplifier.simplify(java.util.List&lt;com.here.sdk.core.GeoCoordinates&gt;, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)</code></a>.</p></dd>
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
`
}</HTMLBlock>

---
title: "SegmentReferenceConverter (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentreferenceconverter"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SegmentReferenceConverter.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapdata.SegmentReferenceConverter</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SegmentReferenceConverter</span>
<span class="extends-implements">extends <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>A SegmentReferenceConverter provides possibility to convert mapmatched instances of
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing"><code>SegmentReference</code></a> to corresponding instances of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-directedocmsegmentid" title="class in com.here.sdk.mapdata"><code>DirectedOCMSegmentId</code></a>.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">SegmentReferenceConverter</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-directedocmsegmentid" title="class in com.here.sdk.mapdata">DirectedOCMSegmentId</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getOCMSegmentId(com.here.sdk.routing.SegmentReference)">getOCMSegmentId</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a> segmentReference)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-directedocmsegmentid" title="class in com.here.sdk.mapdata"><code>DirectedOCMSegmentId</code></a> for provided <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing"><code>SegmentReference</code></a>.</div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>SegmentReferenceConverter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SegmentReferenceConverter</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
                          throws <span class="exceptions"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
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
<section class="detail" id="getOCMSegmentId(com.here.sdk.routing.SegmentReference)">
<h3>getOCMSegmentId</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-directedocmsegmentid" title="class in com.here.sdk.mapdata">DirectedOCMSegmentId</a></span> <span class="element-name">getOCMSegmentId</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a> segmentReference)</span></div>
<div class="block"><p>The <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-directedocmsegmentid" title="class in com.here.sdk.mapdata"><code>DirectedOCMSegmentId</code></a> for provided <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing"><code>SegmentReference</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>segmentReference</code> - <p><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing"><code>SegmentReference</code></a> to convert.</p></dd>
<dt>Returns:</dt>
<dd><p><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-directedocmsegmentid" title="class in com.here.sdk.mapdata"><code>DirectedOCMSegmentId</code></a> corresponding to provided <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing"><code>SegmentReference</code></a>.</p></dd>
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

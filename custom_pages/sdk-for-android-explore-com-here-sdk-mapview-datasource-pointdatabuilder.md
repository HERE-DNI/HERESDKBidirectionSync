---
title: "PointDataBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PointDataBuilder.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.datasource.PointDataBuilder</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">PointDataBuilder</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Builder of <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdata" title="class in com.here.sdk.mapview.datasource"><code>PointData</code></a> instances.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder#%3Cinit%3E()">PointDataBuilder</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a builder instance.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdata" title="class in com.here.sdk.mapview.datasource">PointData</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder#build()">build</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Builds an instance of <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdata" title="class in com.here.sdk.mapview.datasource"><code>PointData</code></a> and resets the builder instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder" title="class in com.here.sdk.mapview.datasource">PointDataBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder#withAttributes(com.here.sdk.mapview.datasource.DataAttributes)">withAttributes</a><wbr/>(<a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributes" title="class in com.here.sdk.mapview.datasource">DataAttributes</a> attributes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures the builder with custom attributes for point to be created.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder" title="class in com.here.sdk.mapview.datasource">PointDataBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder#withCoordinates(com.here.sdk.core.GeoCoordinates)">withCoordinates</a><wbr/>(<a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures the builder with geodetic coordinates for point to be created.</div>
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
<h3>PointDataBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PointDataBuilder</span>()</div>
<div class="block"><p>Creates a builder instance.</p></div>
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
<section class="detail" id="withCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>withCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder" title="class in com.here.sdk.mapview.datasource">PointDataBuilder</a></span> <span class="element-name">withCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div class="block"><p>Configures the builder with geodetic coordinates for point to be created.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>Geodetic coordinates of the point.
     Altitude of coordinates is ignored.</p></dd>
<dt>Returns:</dt>
<dd><p>The builder.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withAttributes(com.here.sdk.mapview.datasource.DataAttributes)">
<h3>withAttributes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder" title="class in com.here.sdk.mapview.datasource">PointDataBuilder</a></span> <span class="element-name">withAttributes</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributes" title="class in com.here.sdk.mapview.datasource">DataAttributes</a> attributes)</span></div>
<div class="block"><p>Configures the builder with custom attributes for point to be created.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attributes</code> - <p>Custom data attributes to be associated with the point.</p></dd>
<dt>Returns:</dt>
<dd><p>The builder.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="build()">
<h3>build</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdata" title="class in com.here.sdk.mapview.datasource">PointData</a></span> <span class="element-name">build</span>()</div>
<div class="block"><p>Builds an instance of <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdata" title="class in com.here.sdk.mapview.datasource"><code>PointData</code></a> and resets the builder instance.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Instance of <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdata" title="class in com.here.sdk.mapview.datasource"><code>PointData</code></a> created with the configured parameters.</p></dd>
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

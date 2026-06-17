---
title: "DataAttributesBase (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbase"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- DataAttributesBase.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-dataattributes" title="class in com.here.sdk.mapview.datasource">DataAttributes</a></code>, <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-dataattributesaccessor" title="class in com.here.sdk.mapview.datasource">DataAttributesAccessor</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">DataAttributesBase</span></div>
<div class="block"><p>Interface for a collection of data attributes.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getAsString(java.lang.String)">getAsString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the value of an attribute as a string or <code>null</code> if it is not contained.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getAttributeNames()">getAttributeNames</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a list of attribute names.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getBoolean(java.lang.String)">getBoolean</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the value of a boolean attribute or <code>null</code> if it is not contained or the type doesn't match.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getDouble(java.lang.String)">getDouble</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the value of a double precision floating decimal attribute or <code>null</code> if it is not contained or the type doesn't match.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getFloat(java.lang.String)">getFloat</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the value of a single precision floating decimal attribute or <code>null</code> if it is not contained or the type doesn't match.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getInt64(java.lang.String)">getInt64</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the value of a 64-bits integer attribute or <code>null</code> if it is not contained or the type doesn't match.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getString(java.lang.String)">getString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the value of a string attribute or <code>null</code> if it is not contained or the type doesn't match.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getValue(java.lang.String)">getValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the DataAttributeValue or <code>null</code> if it is not contained.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-dataattributevalue.valuetype" title="enum class in com.here.sdk.mapview.datasource">DataAttributeValue.ValueType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getValueType(java.lang.String)">getValueType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value type of an attribute or <code>null</code> if it is not contained.</div>
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
<section class="detail" id="getAttributeNames()">
<h3>getAttributeNames</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAttributeNames</span>()</div>
<div class="block"><p>Returns a list of attribute names.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of attribute names.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueType(java.lang.String)">
<h3>getValueType</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-dataattributevalue.valuetype" title="enum class in com.here.sdk.mapview.datasource">DataAttributeValue.ValueType</a></span> <span class="element-name">getValueType</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block"><p>Returns the value type of an attribute or <code>null</code> if it is not contained.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value type or <code>null</code> if it is not contained.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAsString(java.lang.String)">
<h3>getAsString</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAsString</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block"><p>Gets the value of an attribute as a string or <code>null</code> if it is not contained.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getString(java.lang.String)">
<h3>getString</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getString</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block"><p>Gets the value of a string attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInt64(java.lang.String)">
<h3>getInt64</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a></span> <span class="element-name">getInt64</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block"><p>Gets the value of a 64-bits integer attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFloat(java.lang.String)">
<h3>getFloat</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a></span> <span class="element-name">getFloat</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block"><p>Gets the value of a single precision floating decimal attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDouble(java.lang.String)">
<h3>getDouble</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getDouble</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block"><p>Gets the value of a double precision floating decimal attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBoolean(java.lang.String)">
<h3>getBoolean</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">getBoolean</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block"><p>Gets the value of a boolean attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(java.lang.String)">
<h3>getValue</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block"><p>Gets the DataAttributeValue or <code>null</code> if it is not contained.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
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

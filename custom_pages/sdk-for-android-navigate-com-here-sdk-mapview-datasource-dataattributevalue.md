---
title: "DataAttributeValue (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- DataAttributeValue.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.datasource.DataAttributeValue</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">DataAttributeValue</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Encapsulates a data attribute value.
 Supports basic types and arrays of basic types.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-dataattributevalue.valuetype" title="enum class in com.here.sdk.mapview.datasource">DataAttributeValue.ValueType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Supported types of the data attribute values.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(boolean)">DataAttributeValue</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a boolean data attribute value.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(double)">DataAttributeValue</a><wbr/>(double value)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a double precision floating decimal data attribute value.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(float)">DataAttributeValue</a><wbr/>(float value)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a single precision floating decimal data attribute value.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(long)">DataAttributeValue</a><wbr/>(long value)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a 64-bit integer data attribute value.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(com.here.sdk.core.Color)">DataAttributeValue</a><wbr/>(<a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a> value)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a color data attribute value.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(java.lang.String)">DataAttributeValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a string data attribute value.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(java.util.List)">DataAttributeValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a>&gt; value)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an aggregated data attribute value.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#getArray()">getArray</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the array value or <code>null</code> if the type doesn't match.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#getAsString()">getAsString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a string representation of the contained value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#getBoolean()">getBoolean</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the boolean value or <code>null</code> if the type doesn't match.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#getColor()">getColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the color value or <code>null</code> if the type doesn't match.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#getDouble()">getDouble</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the double precision floating decimal value or <code>null</code> if the type doesn't match.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#getFloat()">getFloat</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the single precision floating decimal value or <code>null</code> if the type doesn't match.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#getInt64()">getInt64</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets 64-bits integer value or <code>null</code> if the type doesn't match.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#getString()">getString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the string value or <code>null</code> if the type doesn't match.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-dataattributevalue.valuetype" title="enum class in com.here.sdk.mapview.datasource">DataAttributeValue.ValueType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the type of the value.</div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>DataAttributeValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>Creates a string data attribute value.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(long)">
<h3>DataAttributeValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><wbr/><span class="parameters">(long value)</span></div>
<div class="block"><p>Creates a 64-bit integer data attribute value.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(float)">
<h3>DataAttributeValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><wbr/><span class="parameters">(float value)</span></div>
<div class="block"><p>Creates a single precision floating decimal data attribute value.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double)">
<h3>DataAttributeValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Creates a double precision floating decimal data attribute value.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(boolean)">
<h3>DataAttributeValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Creates a boolean data attribute value.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.Color)">
<h3>DataAttributeValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div class="block"><p>Creates a color data attribute value.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.List)">
<h3>DataAttributeValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a>&gt; value)</span></div>
<div class="block"><p>Creates an aggregated data attribute value.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Attribute value.</p></dd>
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
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-dataattributevalue.valuetype" title="enum class in com.here.sdk.mapview.datasource">DataAttributeValue.ValueType</a></span> <span class="element-name">getType</span>()</div>
<div class="block"><p>Returns the type of the value.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The type of the value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getString()">
<h3>getString</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getString</span>()</div>
<div class="block"><p>Gets the string value or <code>null</code> if the type doesn't match.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInt64()">
<h3>getInt64</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a></span> <span class="element-name">getInt64</span>()</div>
<div class="block"><p>Gets 64-bits integer value or <code>null</code> if the type doesn't match.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFloat()">
<h3>getFloat</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a></span> <span class="element-name">getFloat</span>()</div>
<div class="block"><p>Gets the single precision floating decimal value or <code>null</code> if the type doesn't match.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDouble()">
<h3>getDouble</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getDouble</span>()</div>
<div class="block"><p>Gets the double precision floating decimal value or <code>null</code> if the type doesn't match.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBoolean()">
<h3>getBoolean</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">getBoolean</span>()</div>
<div class="block"><p>Gets the boolean value or <code>null</code> if the type doesn't match.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColor()">
<h3>getColor</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getColor</span>()</div>
<div class="block"><p>Gets the color value or <code>null</code> if the type doesn't match.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getArray()">
<h3>getArray</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a>&gt;</span> <span class="element-name">getArray</span>()</div>
<div class="block"><p>Gets the array value or <code>null</code> if the type doesn't match.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAsString()">
<h3>getAsString</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAsString</span>()</div>
<div class="block"><p>Returns a string representation of the contained value.</p></div>
<dl class="notes">
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






</div>
`
}</HTMLBlock>

---
title: "DataAttributeValue (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- DataAttributeValue.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.datasource.DataAttributeValue</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">DataAttributeValue</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Encapsulates a data attribute value.
 Supports basic types and arrays of basic types.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue-valuetype" title="enum class in com.here.sdk.mapview.datasource">DataAttributeValue.ValueType</a></code></div>
<div className="col-last even-row-color">
<div className="block">Supported types of the data attribute values.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(boolean)">DataAttributeValue</a><wbr/>(boolean value)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a boolean data attribute value.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(double)">DataAttributeValue</a><wbr/>(double value)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a double precision floating decimal data attribute value.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(float)">DataAttributeValue</a><wbr/>(float value)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a single precision floating decimal data attribute value.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(long)">DataAttributeValue</a><wbr/>(long value)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a 64-bit integer data attribute value.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(com.here.sdk.core.Color)">DataAttributeValue</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a color data attribute value.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(java.lang.String)">DataAttributeValue</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a string data attribute value.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue#%3Cinit%3E(java.util.List)">DataAttributeValue</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a>&gt; value)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates an aggregated data attribute value.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String)">
<h3>DataAttributeValue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DataAttributeValue</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div className="block"><p>Creates a string data attribute value.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(long)">
<h3>DataAttributeValue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DataAttributeValue</span><wbr/><span className="parameters">(long value)</span></div>
<div className="block"><p>Creates a 64-bit integer data attribute value.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(float)">
<h3>DataAttributeValue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DataAttributeValue</span><wbr/><span className="parameters">(float value)</span></div>
<div className="block"><p>Creates a single precision floating decimal data attribute value.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(double)">
<h3>DataAttributeValue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DataAttributeValue</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Creates a double precision floating decimal data attribute value.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(boolean)">
<h3>DataAttributeValue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DataAttributeValue</span><wbr/><span className="parameters">(boolean value)</span></div>
<div className="block"><p>Creates a boolean data attribute value.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.Color)">
<h3>DataAttributeValue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DataAttributeValue</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div className="block"><p>Creates a color data attribute value.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.util.List)">
<h3>DataAttributeValue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DataAttributeValue</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a>&gt; value)</span></div>
<div className="block"><p>Creates an aggregated data attribute value.</p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getType()">
<h3>getType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue-valuetype" title="enum class in com.here.sdk.mapview.datasource">DataAttributeValue.ValueType</a></span> <span className="element-name">getType</span>()</div>
<div className="block"><p>Returns the type of the value.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The type of the value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getString()">
<h3>getString</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getString</span>()</div>
<div className="block"><p>Gets the string value or <code>null</code> if the type doesn't match.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getInt64()">
<h3>getInt64</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a></span> <span className="element-name">getInt64</span>()</div>
<div className="block"><p>Gets 64-bits integer value or <code>null</code> if the type doesn't match.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getFloat()">
<h3>getFloat</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a></span> <span className="element-name">getFloat</span>()</div>
<div className="block"><p>Gets the single precision floating decimal value or <code>null</code> if the type doesn't match.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDouble()">
<h3>getDouble</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getDouble</span>()</div>
<div className="block"><p>Gets the double precision floating decimal value or <code>null</code> if the type doesn't match.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBoolean()">
<h3>getBoolean</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span className="element-name">getBoolean</span>()</div>
<div className="block"><p>Gets the boolean value or <code>null</code> if the type doesn't match.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getColor()">
<h3>getColor</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getColor</span>()</div>
<div className="block"><p>Gets the color value or <code>null</code> if the type doesn't match.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getArray()">
<h3>getArray</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a>&gt;</span> <span className="element-name">getArray</span>()</div>
<div className="block"><p>Gets the array value or <code>null</code> if the type doesn't match.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getAsString()">
<h3>getAsString</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getAsString</span>()</div>
<div className="block"><p>Returns a string representation of the contained value.</p></div>
<dl className="notes">
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
</div>



</div>
`
}</HTMLBlock>

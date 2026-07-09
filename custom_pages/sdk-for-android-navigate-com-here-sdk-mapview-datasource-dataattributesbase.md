---
title: "DataAttributesBase (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- DataAttributesBase.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributes" title="class in com.here.sdk.mapview.datasource">DataAttributes</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesaccessor" title="class in com.here.sdk.mapview.datasource">DataAttributesAccessor</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">DataAttributesBase</span></div>
<div className="block"><p>Interface for a collection of data attributes.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
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
<section className="detail" id="getAttributeNames()">
<h3>getAttributeNames</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span className="element-name">getAttributeNames</span>()</div>
<div className="block"><p>Returns a list of attribute names.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of attribute names.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getValueType(java.lang.String)">
<h3>getValueType</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue-valuetype" title="enum class in com.here.sdk.mapview.datasource">DataAttributeValue.ValueType</a></span> <span className="element-name">getValueType</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Returns the value type of an attribute or <code>null</code> if it is not contained.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value type or <code>null</code> if it is not contained.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getAsString(java.lang.String)">
<h3>getAsString</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getAsString</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the value of an attribute as a string or <code>null</code> if it is not contained.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getString(java.lang.String)">
<h3>getString</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getString</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the value of a string attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getInt64(java.lang.String)">
<h3>getInt64</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a></span> <span className="element-name">getInt64</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the value of a 64-bits integer attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getFloat(java.lang.String)">
<h3>getFloat</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a></span> <span className="element-name">getFloat</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the value of a single precision floating decimal attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDouble(java.lang.String)">
<h3>getDouble</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getDouble</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the value of a double precision floating decimal attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBoolean(java.lang.String)">
<h3>getBoolean</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span className="element-name">getBoolean</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the value of a boolean attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dt>Returns:</dt>
<dd><p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getValue(java.lang.String)">
<h3>getValue</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a></span> <span className="element-name">getValue</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the DataAttributeValue or <code>null</code> if it is not contained.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>

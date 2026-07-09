---
title: "DataAttributesAccessor (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesaccessor"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- DataAttributesAccessor.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.datasource.DataAttributesAccessor</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">DataAttributesBase</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">DataAttributesAccessor</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">DataAttributesBase</a></span></div>
<div className="block"><p>Accessor used for manipulating data attributes.
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
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section className="detail" id="addOrReplace(java.lang.String,java.lang.String)">
<h3>addOrReplace</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addOrReplace</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div className="block"><p>Adds or replaces a string attribute.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addOrReplace(java.lang.String,long)">
<h3>addOrReplace</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addOrReplace</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 long value)</span></div>
<div className="block"><p>Adds or replaces a 64-bits integer attribute.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addOrReplace(java.lang.String,float)">
<h3>addOrReplace</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addOrReplace</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 float value)</span></div>
<div className="block"><p>Adds or replaces a single precision floating decimal attribute.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addOrReplace(java.lang.String,double)">
<h3>addOrReplace</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addOrReplace</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 double value)</span></div>
<div className="block"><p>Adds or replaces a double precision floating decimal attribute.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addOrReplace(java.lang.String,boolean)">
<h3>addOrReplace</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addOrReplace</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean value)</span></div>
<div className="block"><p>Adds or replaces a boolean attribute.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addOrReplace(java.lang.String,com.here.sdk.core.Color)">
<h3>addOrReplace</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addOrReplace</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div className="block"><p>Adds or replaces a color attribute.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addOrReplace(java.lang.String,com.here.sdk.mapview.datasource.DataAttributeValue)">
<h3>addOrReplace</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addOrReplace</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a> value)</span></div>
<div className="block"><p>Adds or replaces an attribute.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
<dd><code>value</code> - <p>Attribute value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="remove(java.lang.String)">
<h3>remove</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">remove</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Removes an attribute by name.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Attribute name.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeAll()">
<h3>removeAll</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeAll</span>()</div>
<div className="block"><p>Removes all attributes.</p></div>
</section>
</li>
<li>
<section className="detail" id="getAttributeNames()">
<h3>getAttributeNames</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span className="element-name">getAttributeNames</span>()</div>
<div className="block"><p>Returns a list of attribute names.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-dataattributesbase#getAttributeNames()">getAttributeNames</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">DataAttributesBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>The list of attribute names.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getValueType(java.lang.String)">
<h3>getValueType</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue-valuetype" title="enum class in com.here.sdk.mapview.datasource">DataAttributeValue.ValueType</a></span> <span className="element-name">getValueType</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Returns the value type of an attribute or <code>null</code> if it is not contained.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-dataattributesbase#getValueType(java.lang.String)">getValueType</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">DataAttributesBase</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getAsString</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the value of an attribute as a string or <code>null</code> if it is not contained.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-dataattributesbase#getAsString(java.lang.String)">getAsString</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">DataAttributesBase</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getString</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the value of a string attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-dataattributesbase#getString(java.lang.String)">getString</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">DataAttributesBase</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a></span> <span className="element-name">getInt64</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the value of a 64-bits integer attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-dataattributesbase#getInt64(java.lang.String)">getInt64</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">DataAttributesBase</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a></span> <span className="element-name">getFloat</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the value of a single precision floating decimal attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-dataattributesbase#getFloat(java.lang.String)">getFloat</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">DataAttributesBase</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getDouble</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the value of a double precision floating decimal attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-dataattributesbase#getDouble(java.lang.String)">getDouble</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">DataAttributesBase</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span className="element-name">getBoolean</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the value of a boolean attribute or <code>null</code> if it is not contained or the type doesn't match.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-dataattributesbase#getBoolean(java.lang.String)">getBoolean</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">DataAttributesBase</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a></span> <span className="element-name">getValue</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block"><p>Gets the DataAttributeValue or <code>null</code> if it is not contained.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-dataattributesbase#getValue(java.lang.String)">getValue</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">DataAttributesBase</a></code></dd>
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

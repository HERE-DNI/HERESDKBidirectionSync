---
title: "Metadata (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-metadata"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Metadata.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.core.Metadata</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Metadata</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Holds metadata on behalf of a map item.
 An instance of this class can contain metadata items of varying types, such as
 String, Integer, Double, GeoCoordinates etc. and can also hold arbitrary metadata
 types by the use of the CustomMetadataValue interface.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-metadata#%3Cinit%3E()">Metadata</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates an instance of this class.</div>
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
<section className="detail" id="&lt;init&gt;()">
<h3>Metadata</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Metadata</span>()</div>
<div className="block"><p>Creates an instance of this class.</p></div>
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
<section className="detail" id="getCustomValue(java.lang.String)">
<h3>getCustomValue</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-custommetadatavalue" title="interface in com.here.sdk.core">CustomMetadataValue</a></span> <span className="element-name">getCustomValue</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div className="block"><p>Obtains an instance of the CustomMetadataValue class associated with a given key.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>The name of the key for which to obtain the value.</p></dd>
<dt>Returns:</dt>
<dd><p>The value associated with the key.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDouble(java.lang.String)">
<h3>getDouble</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getDouble</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div className="block"><p>Obtains a Double value associated with a given key.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>The name of the key for which to obtain the value.</p></dd>
<dt>Returns:</dt>
<dd><p>The value associated with the key.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeoCoordinates(java.lang.String)">
<h3>getGeoCoordinates</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">getGeoCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div className="block"><p>Obtains a GeoCoordinates value associated with a given key.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>The name of the key for which to obtain the value.</p></dd>
<dt>Returns:</dt>
<dd><p>The value associated with the key.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getInteger(java.lang.String)">
<h3>getInteger</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">getInteger</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div className="block"><p>Obtains an Integer value associated with a given key.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>The name of the key for which to obtain the value.</p></dd>
<dt>Returns:</dt>
<dd><p>The value associated with the key.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getString(java.lang.String)">
<h3>getString</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getString</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div className="block"><p>Obtains a String value associated with a given key.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>The name of the key for which to obtain the value.</p></dd>
<dt>Returns:</dt>
<dd><p>The value associated with the key.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getType(java.lang.String)">
<h3>getType</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-metadatatype" title="enum class in com.here.sdk.core">MetadataType</a></span> <span className="element-name">getType</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div className="block"><p>Determines the type of a metadata value.
 If the type of a metadata value associated with a key is not known, this
 method will enable the type to be queried, in order to know which get method
 to call. i.e. getDouble(), getInteger() etc.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>The name of the key for which to obtain the type.</p></dd>
<dt>Returns:</dt>
<dd><p>An enumeration describing the type of the value associated with the key.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeValue(java.lang.String)">
<h3>removeValue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeValue</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div className="block"><p>Removes a metadata key and its associated value.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>The name of the key to be removed.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCustomValue(java.lang.String,com.here.sdk.core.CustomMetadataValue)">
<h3>setCustomValue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCustomValue</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-custommetadatavalue" title="interface in com.here.sdk.core">CustomMetadataValue</a> value)</span></div>
<div className="block"><p>Creates a key:value pair, where the value is a type derived from CustomMetadataValue.
 If the given key already exists, its value will be replaced by the new one.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>The name of the key to be created or replaced.</p></dd>
<dd><code>value</code> - <p>The value to be assigned to the key.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDouble(java.lang.String,double)">
<h3>setDouble</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDouble</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 double value)</span></div>
<div className="block"><p>Creates a key:value pair, where the value is of type Double.
 If the given key already exists, its value will be replaced by the new one.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>The name of the key to be created or replaced.</p></dd>
<dd><code>value</code> - <p>The value to be assigned to the key.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setGeoCoordinates(java.lang.String,com.here.sdk.core.GeoCoordinates)">
<h3>setGeoCoordinates</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setGeoCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> value)</span></div>
<div className="block"><p>Creates a key:value pair, where the value is of type GeoCoordinates.
 If the given key already exists, its value will be replaced by the new one.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>The name of the key to be created or replaced.</p></dd>
<dd><code>value</code> - <p>The value to be assigned to the key.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setInteger(java.lang.String,int)">
<h3>setInteger</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setInteger</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 int value)</span></div>
<div className="block"><p>Creates a key:value pair, where the value is of type Integer.
 If the given key already exists, its value will be replaced by the new one.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>The name of the key to be created or replaced.</p></dd>
<dd><code>value</code> - <p>The value to be assigned to the key.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setString(java.lang.String,java.lang.String)">
<h3>setString</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setString</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div className="block"><p>Creates a key:value pair, where the value is of type String.
 If the given key already exists, its value will be replaced by the new one.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>The name of the key to be created or replaced.</p></dd>
<dd><code>value</code> - <p>The value to be assigned to the key.</p></dd>
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

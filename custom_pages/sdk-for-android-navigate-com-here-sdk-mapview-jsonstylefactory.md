---
title: "JsonStyleFactory (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-jsonstylefactory"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- JsonStyleFactory.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.JsonStyleFactory</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">JsonStyleFactory</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>A factory of <a href="sdk-for-android-navigate-com-here-sdk-mapview-style" title="class in com.here.sdk.mapview"><code>Style</code></a> objects from styles defined in JSON format.
 For more details see Custom Layer Style Reference in the documentation.
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
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-jsonstylefactory-instantiationerrorcode" title="enum class in com.here.sdk.mapview">JsonStyleFactory.InstantiationErrorCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">Describes reasons for failing to create a <a href="sdk-for-android-navigate-com-here-sdk-mapview-style" title="class in com.here.sdk.mapview"><code>Style</code></a> from a JSON source.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-jsonstylefactory-instantiationerrordetails" title="class in com.here.sdk.mapview">JsonStyleFactory.InstantiationErrorDetails</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Describes the reason for failing to create a <a href="sdk-for-android-navigate-com-here-sdk-mapview-style" title="class in com.here.sdk.mapview"><code>Style</code></a> from a JSON source.</div>
</div>
<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-jsonstylefactory-instantiationexception" title="class in com.here.sdk.mapview">JsonStyleFactory.InstantiationException</a></code></div>
<div className="col-last even-row-color">
<div className="block">Thrown when failing to create a <a href="sdk-for-android-navigate-com-here-sdk-mapview-style" title="class in com.here.sdk.mapview"><code>Style</code></a> from a JSON source.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="createFromString(java.lang.String)">
<h3>createFromString</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-style" title="class in com.here.sdk.mapview">Style</a></span> <span className="element-name">createFromString</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> styleString)</span>
                              throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-jsonstylefactory-instantiationexception" title="class in com.here.sdk.mapview">JsonStyleFactory.InstantiationException</a></span></div>
<div className="block"><p>Creates an instance of Style from a JSON string.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>styleString</code> - <p>JSON style string.</p></dd>
<dt>Returns:</dt>
<dd><p>Style instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-jsonstylefactory-instantiationexception" title="class in com.here.sdk.mapview">JsonStyleFactory.InstantiationException</a></code> - <p>Indicates failure to create <a href="sdk-for-android-navigate-com-here-sdk-mapview-style" title="class in com.here.sdk.mapview"><code>Style</code></a> from JSON string.</p></dd>
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

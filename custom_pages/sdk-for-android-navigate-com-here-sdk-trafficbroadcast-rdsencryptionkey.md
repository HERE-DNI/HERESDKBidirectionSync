---
title: "RDSEncryptionKey (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RDSEncryptionKey.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.trafficbroadcast</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.trafficbroadcast.RDSEncryptionKey</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RDSEncryptionKey</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents the RDS encryption key.
 Fields allocation information is described in CEN ISO/CD 14819-6.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>short</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey#encryptionId">encryptionId</a></code></div>
<div className="col-last even-row-color">
<div className="block">Id of encryption key within the list.</div>
</div>
<div className="col-first odd-row-color"><code>short</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey#rotateRight">rotateRight</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Rotate Right used for bit manipulations as a part of encryption process.</div>
</div>
<div className="col-first even-row-color"><code>short</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey#startBit">startBit</a></code></div>
<div className="col-last even-row-color">
<div className="block">Start Bit used for bit manipulations as a part of encryption process.</div>
</div>
<div className="col-first odd-row-color"><code>short</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey#xorValue">xorValue</a></code></div>
<div className="col-last odd-row-color">
<div className="block">XOR Value used for bit manipulations as a part of encryption process.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey#%3Cinit%3E(short,short,short,short)">RDSEncryptionKey</a><wbr/>(short encryptionId,
 short rotateRight,
 short startBit,
 short xorValue)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="encryptionId">
<h3>encryptionId</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">encryptionId</span></div>
<div className="block"><p>Id of encryption key within the list.</p></div>
</section>
</li>
<li>
<section className="detail" id="rotateRight">
<h3>rotateRight</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">rotateRight</span></div>
<div className="block"><p>Rotate Right used for bit manipulations as a part of encryption process.</p></div>
</section>
</li>
<li>
<section className="detail" id="startBit">
<h3>startBit</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">startBit</span></div>
<div className="block"><p>Start Bit used for bit manipulations as a part of encryption process.</p></div>
</section>
</li>
<li>
<section className="detail" id="xorValue">
<h3>xorValue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">xorValue</span></div>
<div className="block"><p>XOR Value used for bit manipulations as a part of encryption process.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(short,short,short,short)">
<h3>RDSEncryptionKey</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RDSEncryptionKey</span><wbr/><span className="parameters">(short encryptionId,
 short rotateRight,
 short startBit,
 short xorValue)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>encryptionId</code> - <p>Id of encryption key within the list.</p></dd>
<dd><code>rotateRight</code> - <p>Rotate Right used for bit manipulations as a part of encryption process.</p></dd>
<dd><code>startBit</code> - <p>Start Bit used for bit manipulations as a part of encryption process.</p></dd>
<dd><code>xorValue</code> - <p>XOR Value used for bit manipulations as a part of encryption process.</p></dd>
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

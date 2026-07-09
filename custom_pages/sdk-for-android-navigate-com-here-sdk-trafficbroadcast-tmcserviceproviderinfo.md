---
title: "TMCServiceProviderInfo (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TMCServiceProviderInfo.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.trafficbroadcast</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.trafficbroadcast.TMCServiceProviderInfo</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TMCServiceProviderInfo</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents the service prodiver info in RDS-TMC format.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>short</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#countryCode">countryCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">Service provider country code.</div>
</div>
<div className="col-first odd-row-color"><code>short</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#encryptionId">encryptionId</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Encryption key index.</div>
</div>
<div className="col-first even-row-color"><code>short</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#encryptionTestMode">encryptionTestMode</a></code></div>
<div className="col-last even-row-color">
<div className="block">Encryption mode test flag.</div>
</div>
<div className="col-first odd-row-color"><code>short</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#ltnBeforeEncryption">ltnBeforeEncryption</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Location table number before encryption.</div>
</div>
<div className="col-first even-row-color"><code>short</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#ltnNumber">ltnNumber</a></code></div>
<div className="col-last even-row-color">
<div className="block">Location table number.</div>
</div>
<div className="col-first odd-row-color"><code>short</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#sid">sid</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Service id.</div>
</div>
<div className="col-first even-row-color"><code>short</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#status">status</a></code></div>
<div className="col-last even-row-color">
<div className="block">Service provider status.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#%3Cinit%3E(short,short,short,short,short,short,short)">TMCServiceProviderInfo</a><wbr/>(short status,
 short countryCode,
 short sid,
 short ltnNumber,
 short encryptionTestMode,
 short encryptionId,
 short ltnBeforeEncryption)</code></div>
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
<section className="detail" id="status">
<h3>status</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">status</span></div>
<div className="block"><p>Service provider status.</p></div>
</section>
</li>
<li>
<section className="detail" id="countryCode">
<h3>countryCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">countryCode</span></div>
<div className="block"><p>Service provider country code.</p></div>
</section>
</li>
<li>
<section className="detail" id="sid">
<h3>sid</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">sid</span></div>
<div className="block"><p>Service id.</p></div>
</section>
</li>
<li>
<section className="detail" id="ltnNumber">
<h3>ltnNumber</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">ltnNumber</span></div>
<div className="block"><p>Location table number.</p></div>
</section>
</li>
<li>
<section className="detail" id="encryptionTestMode">
<h3>encryptionTestMode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">encryptionTestMode</span></div>
<div className="block"><p>Encryption mode test flag.</p></div>
</section>
</li>
<li>
<section className="detail" id="encryptionId">
<h3>encryptionId</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">encryptionId</span></div>
<div className="block"><p>Encryption key index.</p></div>
</section>
</li>
<li>
<section className="detail" id="ltnBeforeEncryption">
<h3>ltnBeforeEncryption</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">short</span> <span className="element-name">ltnBeforeEncryption</span></div>
<div className="block"><p>Location table number before encryption.</p></div>
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
<section className="detail" id="&lt;init&gt;(short,short,short,short,short,short,short)">
<h3>TMCServiceProviderInfo</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TMCServiceProviderInfo</span><wbr/><span className="parameters">(short status,
 short countryCode,
 short sid,
 short ltnNumber,
 short encryptionTestMode,
 short encryptionId,
 short ltnBeforeEncryption)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>status</code> - <p>Service provider status.</p></dd>
<dd><code>countryCode</code> - <p>Service provider country code.</p></dd>
<dd><code>sid</code> - <p>Service id.</p></dd>
<dd><code>ltnNumber</code> - <p>Location table number.</p></dd>
<dd><code>encryptionTestMode</code> - <p>Encryption mode test flag.</p></dd>
<dd><code>encryptionId</code> - <p>Encryption key index.</p></dd>
<dd><code>ltnBeforeEncryption</code> - <p>Location table number before encryption.</p></dd>
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

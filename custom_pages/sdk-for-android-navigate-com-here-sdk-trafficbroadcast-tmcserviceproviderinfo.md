---
title: "TMCServiceProviderInfo (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TMCServiceProviderInfo.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.trafficbroadcast</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.trafficbroadcast.TMCServiceProviderInfo</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">TMCServiceProviderInfo</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents the service prodiver info in RDS-TMC format.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>short</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#countryCode">countryCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Service provider country code.</div>
</div>
<div class="col-first odd-row-color"><code>short</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#encryptionId">encryptionId</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Encryption key index.</div>
</div>
<div class="col-first even-row-color"><code>short</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#encryptionTestMode">encryptionTestMode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Encryption mode test flag.</div>
</div>
<div class="col-first odd-row-color"><code>short</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#ltnBeforeEncryption">ltnBeforeEncryption</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Location table number before encryption.</div>
</div>
<div class="col-first even-row-color"><code>short</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#ltnNumber">ltnNumber</a></code></div>
<div class="col-last even-row-color">
<div class="block">Location table number.</div>
</div>
<div class="col-first odd-row-color"><code>short</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#sid">sid</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Service id.</div>
</div>
<div class="col-first even-row-color"><code>short</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#status">status</a></code></div>
<div class="col-last even-row-color">
<div class="block">Service provider status.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo#%3Cinit%3E(short,short,short,short,short,short,short)">TMCServiceProviderInfo</a><wbr/>(short status,
 short countryCode,
 short sid,
 short ltnNumber,
 short encryptionTestMode,
 short encryptionId,
 short ltnBeforeEncryption)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="status">
<h3>status</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">status</span></div>
<div class="block"><p>Service provider status.</p></div>
</section>
</li>
<li>
<section class="detail" id="countryCode">
<h3>countryCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">countryCode</span></div>
<div class="block"><p>Service provider country code.</p></div>
</section>
</li>
<li>
<section class="detail" id="sid">
<h3>sid</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">sid</span></div>
<div class="block"><p>Service id.</p></div>
</section>
</li>
<li>
<section class="detail" id="ltnNumber">
<h3>ltnNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">ltnNumber</span></div>
<div class="block"><p>Location table number.</p></div>
</section>
</li>
<li>
<section class="detail" id="encryptionTestMode">
<h3>encryptionTestMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">encryptionTestMode</span></div>
<div class="block"><p>Encryption mode test flag.</p></div>
</section>
</li>
<li>
<section class="detail" id="encryptionId">
<h3>encryptionId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">encryptionId</span></div>
<div class="block"><p>Encryption key index.</p></div>
</section>
</li>
<li>
<section class="detail" id="ltnBeforeEncryption">
<h3>ltnBeforeEncryption</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">ltnBeforeEncryption</span></div>
<div class="block"><p>Location table number before encryption.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(short,short,short,short,short,short,short)">
<h3>TMCServiceProviderInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TMCServiceProviderInfo</span><wbr/><span class="parameters">(short status,
 short countryCode,
 short sid,
 short ltnNumber,
 short encryptionTestMode,
 short encryptionId,
 short ltnBeforeEncryption)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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

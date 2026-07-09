---
title: "TMCServiceInterface (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceinterface"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TMCServiceInterface.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.trafficbroadcast</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">TMCServiceInterface</span></div>
<div className="block"><p>Contains all outgoing dependencies to the client side.</p></div>
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
<section className="detail" id="requestTMCService(com.here.sdk.trafficbroadcast.TMCServiceRequest)">
<h3>requestTMCService</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">requestTMCService</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcservicerequest" title="class in com.here.sdk.trafficbroadcast">TMCServiceRequest</a> tmcServiceRequest)</span></div>
<div className="block"><p>Called whenever the traffic broadcast needs to be activated.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>tmcServiceRequest</code> - <p>Parameters used to request the traffic broadcast.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTMCPreferredSids(com.here.sdk.trafficbroadcast.TMCPreferredSidsRequest)">
<h3>getTMCPreferredSids</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Short.html" title="class or interface in java.lang">Short</a>&gt;</span> <span className="element-name">getTMCPreferredSids</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcpreferredsidsrequest" title="class in com.here.sdk.trafficbroadcast">TMCPreferredSidsRequest</a> tmcPreferredSidsRequest)</span></div>
<div className="block"><p>Called whenever there is a need to get a list of preferred SIDs for a specific area.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>tmcPreferredSidsRequest</code> - <p>Specifies the area to request the preferred SIDs.</p></dd>
<dt>Returns:</dt>
<dd><p>List of preferred SIDs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRDSEncryptionKeys(com.here.sdk.trafficbroadcast.RDSEncryptionKeysRequest)">
<h3>getRDSEncryptionKeys</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey" title="class in com.here.sdk.trafficbroadcast">RDSEncryptionKey</a>&gt;</span> <span className="element-name">getRDSEncryptionKeys</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkeysrequest" title="class in com.here.sdk.trafficbroadcast">RDSEncryptionKeysRequest</a> rdsEncryptionKeysRequest)</span></div>
<div className="block"><p>Called whenever there is a need to get RDS encryption keys.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>rdsEncryptionKeysRequest</code> - <p>Input data to search for keys.</p></dd>
<dt>Returns:</dt>
<dd><p>RDS encryption keys.</p></dd>
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

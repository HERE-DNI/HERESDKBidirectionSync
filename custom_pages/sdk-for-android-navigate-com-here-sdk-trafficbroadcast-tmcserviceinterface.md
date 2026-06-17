---
title: "TMCServiceInterface (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceinterface"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TMCServiceInterface.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.trafficbroadcast</a></div>

</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">TMCServiceInterface</span></div>
<div class="block"><p>Contains all outgoing dependencies to the client side.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-rdsencryptionkey" title="class in com.here.sdk.trafficbroadcast">RDSEncryptionKey</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getRDSEncryptionKeys(com.here.sdk.trafficbroadcast.RDSEncryptionKeysRequest)">getRDSEncryptionKeys</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-rdsencryptionkeysrequest" title="class in com.here.sdk.trafficbroadcast">RDSEncryptionKeysRequest</a> rdsEncryptionKeysRequest)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever there is a need to get RDS encryption keys.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Short.html" title="class or interface in java.lang">Short</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getTMCPreferredSids(com.here.sdk.trafficbroadcast.TMCPreferredSidsRequest)">getTMCPreferredSids</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-tmcpreferredsidsrequest" title="class in com.here.sdk.trafficbroadcast">TMCPreferredSidsRequest</a> tmcPreferredSidsRequest)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever there is a need to get a list of preferred SIDs for a specific area.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#requestTMCService(com.here.sdk.trafficbroadcast.TMCServiceRequest)">requestTMCService</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-tmcservicerequest" title="class in com.here.sdk.trafficbroadcast">TMCServiceRequest</a> tmcServiceRequest)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever the traffic broadcast needs to be activated.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="requestTMCService(com.here.sdk.trafficbroadcast.TMCServiceRequest)">
<h3>requestTMCService</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">requestTMCService</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-tmcservicerequest" title="class in com.here.sdk.trafficbroadcast">TMCServiceRequest</a> tmcServiceRequest)</span></div>
<div class="block"><p>Called whenever the traffic broadcast needs to be activated.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tmcServiceRequest</code> - <p>Parameters used to request the traffic broadcast.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTMCPreferredSids(com.here.sdk.trafficbroadcast.TMCPreferredSidsRequest)">
<h3>getTMCPreferredSids</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Short.html" title="class or interface in java.lang">Short</a>&gt;</span> <span class="element-name">getTMCPreferredSids</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-tmcpreferredsidsrequest" title="class in com.here.sdk.trafficbroadcast">TMCPreferredSidsRequest</a> tmcPreferredSidsRequest)</span></div>
<div class="block"><p>Called whenever there is a need to get a list of preferred SIDs for a specific area.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tmcPreferredSidsRequest</code> - <p>Specifies the area to request the preferred SIDs.</p></dd>
<dt>Returns:</dt>
<dd><p>List of preferred SIDs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRDSEncryptionKeys(com.here.sdk.trafficbroadcast.RDSEncryptionKeysRequest)">
<h3>getRDSEncryptionKeys</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-rdsencryptionkey" title="class in com.here.sdk.trafficbroadcast">RDSEncryptionKey</a>&gt;</span> <span class="element-name">getRDSEncryptionKeys</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-rdsencryptionkeysrequest" title="class in com.here.sdk.trafficbroadcast">RDSEncryptionKeysRequest</a> rdsEncryptionKeysRequest)</span></div>
<div class="block"><p>Called whenever there is a need to get RDS encryption keys.</p></div>
<dl class="notes">
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
</main>





</div>
`
}</HTMLBlock>

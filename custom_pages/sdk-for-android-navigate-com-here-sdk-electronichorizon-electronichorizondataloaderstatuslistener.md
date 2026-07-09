---
title: "ElectronicHorizonDataLoaderStatusListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderstatuslistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ElectronicHorizonDataLoaderStatusListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.electronichorizon</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">ElectronicHorizonDataLoaderStatusListener</span></div>
<div className="block"><p>Provides a listener for status updates from the <a href="sdk-for-android-navigate-electronichorizondataloader#loadData(com.here.sdk.electronichorizon.ElectronicHorizonUpdate)"><code>ElectronicHorizonDataLoader.loadData(com.here.sdk.electronichorizon.ElectronicHorizonUpdate)</code></a> method.
 The listener receives the current state for different levels of the paths as <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloadedstatus" title="enum class in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoadedStatus</code></a>.
 Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.
 Offline availability: This property is available online and offline.</p></div>
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
<section className="detail" id="onElectronicHorizonDataLoaderStatusUpdated(java.util.Map)">
<h3>onElectronicHorizonDataLoaderStatusUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onElectronicHorizonDataLoaderStatusUpdated</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>,<wbr/><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloadedstatus" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoadedStatus</a>&gt; electronicHorizonDataLoaderStatuses)</span></div>
<div className="block"><p>Called whenever there is a change in the status of the loaded data from <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloader" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoader</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>electronicHorizonDataLoaderStatuses</code> - <p>The updated statuses of the loaded data from <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloader" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoader</code></a>.
     The key is the level of a <code>ElectronicHorizonPath</code>, the value is the current status.</p></dd>
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

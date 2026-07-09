---
title: "ElectronicHorizonListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ElectronicHorizonListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.electronichorizon</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine" title="class in com.here.sdk.warner">WarnerEngine</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">ElectronicHorizonListener</span></div>
<div className="block"><p>Provides a listener for receiving updates during execution of the <a href="sdk-for-android-navigate-electronichorizonengine#update(com.here.sdk.navigation.MapMatchedLocation)"><code>ElectronicHorizonEngine.update(com.here.sdk.navigation.MapMatchedLocation)</code></a> method.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.
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
<section className="detail" id="onElectronicHorizonUpdated(com.here.sdk.electronichorizon.ElectronicHorizonErrorCode,com.here.sdk.electronichorizon.ElectronicHorizonUpdate)">
<h3>onElectronicHorizonUpdated</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onElectronicHorizonUpdated</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonerrorcode" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonErrorCode</a> errorCode,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a> update)</span></div>
<div className="block"><p>Called whenever the electronic horizon subsystem produces:
 <ul>
<li>a new update,</li>
<li>an error,</li>
</ul>
The client must inspect <code>error_code</code> to determine whether the call
 represents an error or a valid update.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>errorCode</code> - <p>The error associated with the horizon computation.
     <code>null</code> means no error.</p></dd>
<dd><code>update</code> - <p>The update describing the current electronic horizon state.
     May be <code>null</code> if an update could not be produced.
     <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></dd>
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

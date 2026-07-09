---
title: "LocationStatusListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationstatuslistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LocationStatusListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.location</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">LocationStatusListener</span></div>
<div className="block"><p>Interface for listening the
 LocationEngine status updates.</p></div>
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
<section className="detail" id="onStatusChanged(com.here.sdk.location.LocationEngineStatus)">
<h3>onStatusChanged</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onStatusChanged</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a> locationEngineStatus)</span></div>
<div className="block"><p>Called each time the status of the LocationEngine has changed.
 Invoked on the main thread.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>locationEngineStatus</code> - <p>The new status.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onFeaturesNotAvailable(java.util.List)">
<h3>onFeaturesNotAvailable</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onFeaturesNotAvailable</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationfeature" title="enum class in com.here.sdk.location">LocationFeature</a>&gt; features)</span></div>
<div className="block"><p>Called after start() if any requested location feature is not available
 for the application. Typically all features are enabled by default, but in
 certain variants some features may be disabled, e.g. to reduce binary size.
 If a feature that you need is not available, contact your HERE representative
 for more information.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>features</code> - <p>List of unavailable location features.</p></dd>
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

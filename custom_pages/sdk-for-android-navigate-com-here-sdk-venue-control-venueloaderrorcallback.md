---
title: "VenueLoadErrorCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VenueLoadErrorCallback.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.control</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span className="modifiers">public interface </span><span className="element-name type-name-label">VenueLoadErrorCallback</span></div>
<div className="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-venuemap#selectVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)"><code>VenueMap.selectVenueAsync(String, VenueLoadErrorCallback)</code></a> has been completed.</p></div>
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
<section className="detail" id="onVenueLoadError(com.here.sdk.venue.control.VenueErrorCode)">
<h3>onVenueLoadError</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onVenueLoadError</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueerrorcode" title="enum class in com.here.sdk.venue.control">VenueErrorCode</a> error)</span></div>
<div className="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-venuemap#selectVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)"><code>VenueMap.selectVenueAsync(String, VenueLoadErrorCallback)</code></a> has been completed.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Represents an error in case of a failure. It is <code>null</code> for an operation that succeeds.</p></dd>
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

---
title: "VenueListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-service-venuelistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VenueListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.service</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">VenueListener</span></div>
<div className="block"><p>The interface for listeners for
 venue loading events in <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a>.</p></div>
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
<section className="detail" id="onGetVenueCompleted(int,com.here.sdk.venue.data.VenueModel,boolean,com.here.sdk.venue.style.VenueStyle)">
<h3>onGetVenueCompleted</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onGetVenueCompleted</span><wbr/><span className="parameters">(int venueId,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data">VenueModel</a> venueModel,
 boolean online,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuestyle" title="class in com.here.sdk.venue.style">VenueStyle</a> venueStyle)</span></div>
<div className="block"><p>Called when loading of a venue or its retrieval from the cache is completed.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venueId</code> - <p>The id of the venue.</p></dd>
<dd><code>venueModel</code> - <p>The venue model.</p></dd>
<dd><code>online</code> - <p><code>True</code> if a new venue was loaded from the server and <code>false</code> otherwise.</p></dd>
<dd><code>venueStyle</code> - <p>The style associated with the venue.</p></dd>
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

---
title: "VenueLifecycleListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venuelifecyclelistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VenueLifecycleListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.control</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">VenueLifecycleListener</span></div>
<div className="block"><p>The interface for listeners for
 the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> lifecycle events. Use the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>
 to add and remove the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuelifecyclelistener" title="interface in com.here.sdk.venue.control"><code>VenueLifecycleListener</code></a>.</p></div>
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
<section className="detail" id="onVenueAdded(com.here.sdk.venue.control.Venue)">
<h3>onVenueAdded</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onVenueAdded</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> venue)</span></div>
<div className="block"><p>Indicates that a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> was added to the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venue</code> - <p>The created <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onVenueRemoved(int)">
<h3>onVenueRemoved</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onVenueRemoved</span><wbr/><span className="parameters">(int venueId)</span></div>
<div className="block"><p>Indicates that a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> was removed from the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venueId</code> - <p>The destroyed venue id, that can be obtained from the <a href="sdk-for-android-navigate-venuemodel#getId()"><code>VenueModel.getId()</code></a>.</p></dd>
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

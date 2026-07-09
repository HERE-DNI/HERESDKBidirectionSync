---
title: "VenueLevelSelectionListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venuelevelselectionlistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VenueLevelSelectionListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.control</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">VenueLevelSelectionListener</span></div>
<div className="block"><p>The interface for listeners for
 the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> selection event. Use the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>
 to add and remove the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuelevelselectionlistener" title="interface in com.here.sdk.venue.control"><code>VenueLevelSelectionListener</code></a>.</p></div>
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
<section className="detail" id="onLevelSelected(com.here.sdk.venue.control.Venue,com.here.sdk.venue.data.VenueDrawing,com.here.sdk.venue.data.VenueLevel,com.here.sdk.venue.data.VenueLevel)">
<h3>onLevelSelected</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onLevelSelected</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> venue,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> drawing,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a> deselectedLevel,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a> selectedLevel)</span></div>
<div className="block"><p>Indicates that the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> of a venue changed.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venue</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> where the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> changed.</p></dd>
<dd><code>drawing</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> where the selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> changed.</p></dd>
<dd><code>deselectedLevel</code> - <p>The previously selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> or <code>null</code>
     if there was no selected level before.</p></dd>
<dd><code>selectedLevel</code> - <p>The new selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.</p></dd>
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

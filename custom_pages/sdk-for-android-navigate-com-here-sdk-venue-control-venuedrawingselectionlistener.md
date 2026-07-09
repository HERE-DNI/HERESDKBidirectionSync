---
title: "VenueDrawingSelectionListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venuedrawingselectionlistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VenueDrawingSelectionListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.control</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">VenueDrawingSelectionListener</span></div>
<div className="block"><p>The interface for listeners for
 the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> selection event. Use the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>
 to add and remove the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuedrawingselectionlistener" title="interface in com.here.sdk.venue.control"><code>VenueDrawingSelectionListener</code></a>.</p></div>
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
<section className="detail" id="onDrawingSelected(com.here.sdk.venue.control.Venue,com.here.sdk.venue.data.VenueDrawing,com.here.sdk.venue.data.VenueDrawing)">
<h3>onDrawingSelected</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onDrawingSelected</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> venue,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> deselectedDrawing,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> selectedDrawing)</span></div>
<div className="block"><p>Indicates that new <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> has been selected.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venue</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> where a selected drawing was changed.</p></dd>
<dd><code>deselectedDrawing</code> - <p>The previously selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> object or <code>null</code>
     if there was no selected drawing before.</p></dd>
<dd><code>selectedDrawing</code> - <p>The new selected <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> object.</p></dd>
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

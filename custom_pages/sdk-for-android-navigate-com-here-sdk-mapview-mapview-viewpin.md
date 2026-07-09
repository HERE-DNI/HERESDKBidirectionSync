---
title: "MapView.ViewPin (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapview-viewpin"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapView.ViewPin.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview" title="class in com.here.sdk.mapview">MapView</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static interface </span><span className="element-name type-name-label">MapView.ViewPin</span></div>
<div className="block">A ViewPin is used to display Android views at a fixed location on the map.
<p>
 The pinned view will automatically be repositioned on the screen as the map moves.
 There is more performance overhead involved in positioning a pinned view as
 compared to a map marker, so for use cases which only require static images,
 markers should be used.</p></div>
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
<section className="detail" id="unpin()">
<h3>unpin</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">unpin</span>()</div>
<div className="block">Removes the view from the <code>MapView</code> it was pinned to.</div>
</section>
</li>
<li>
<section className="detail" id="getGeoCoordinates()">
<h3>getGeoCoordinates</h3>
<div className="member-signature"><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">getGeoCoordinates</span>()</div>
<div className="block">Returns the current GeoCoordinates on the map.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The current GeoCoordinates.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setGeoCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>setGeoCoordinates</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">setGeoCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoCoordinates)</span></div>
<div className="block">Sets the GeoCoordinates on the map.
 <p>
 The altitude component of the coordinates, if set, is interpreted as above sea level.
 When not set, the coordinates are interpreted as at ground level.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoCoordinates</code> - Desired GeoCoordinates for this view pin.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setAnchorPoint(com.here.sdk.core.Anchor2D)">
<h3>setAnchorPoint</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">setAnchorPoint</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> anchorPoint)</span></div>
<div className="block">Sets an anchor point for this instance.
 <p>
 The anchor value has valid range from 0 to 1. Zero (0) for x and y means the view pin's
 upper left corner is located at the geographical location, whereas one (1) for x and y
 means that the pin will have its right bottom corner attached to the geographical
 location instead. The default value used is 0.5, 0.5, causing the view to be centered.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>anchorPoint</code> - A <code>Anchor2D</code> relative to the top-left corner of the
                    <code>ViewPin</code>.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getAnchorPoint()">
<h3>getAnchorPoint</h3>
<div className="member-signature"><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></span> <span className="element-name">getAnchorPoint</span>()</div>
<div className="block">Gets anchor point for this instance.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>anchorPoint A <code>Anchor2D</code> relative to the top-left corner of the <code>
 ViewPin</code>.</dd>
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

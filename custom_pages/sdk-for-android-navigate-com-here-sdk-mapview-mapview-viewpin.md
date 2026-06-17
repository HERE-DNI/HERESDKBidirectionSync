---
title: "MapView.ViewPin (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapview-viewpin"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapView.ViewPin.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-mapview" title="class in com.here.sdk.mapview">MapView</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static interface </span><span class="element-name type-name-label">MapView.ViewPin</span></div>
<div class="block">A ViewPin is used to display Android views at a fixed location on the map.
<p>
 The pinned view will automatically be repositioned on the screen as the map moves.
 There is more performance overhead involved in positioning a pinned view as
 compared to a map marker, so for use cases which only require static images,
 markers should be used.</p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getAnchorPoint()">getAnchorPoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets anchor point for this instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getGeoCoordinates()">getGeoCoordinates</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the current GeoCoordinates on the map.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#setAnchorPoint(com.here.sdk.core.Anchor2D)">setAnchorPoint</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> anchorPoint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets an anchor point for this instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#setGeoCoordinates(com.here.sdk.core.GeoCoordinates)">setGeoCoordinates</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoCoordinates)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the GeoCoordinates on the map.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#unpin()">unpin</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes the view from the <code>MapView</code> it was pinned to.</div>
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
<section class="detail" id="unpin()">
<h3>unpin</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">unpin</span>()</div>
<div class="block">Removes the view from the <code>MapView</code> it was pinned to.</div>
</section>
</li>
<li>
<section class="detail" id="getGeoCoordinates()">
<h3>getGeoCoordinates</h3>
<div class="member-signature"><span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">getGeoCoordinates</span>()</div>
<div class="block">Returns the current GeoCoordinates on the map.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The current GeoCoordinates.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGeoCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>setGeoCoordinates</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setGeoCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoCoordinates)</span></div>
<div class="block">Sets the GeoCoordinates on the map.
 <p>
 The altitude component of the coordinates, if set, is interpreted as above sea level.
 When not set, the coordinates are interpreted as at ground level.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoCoordinates</code> - Desired GeoCoordinates for this view pin.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAnchorPoint(com.here.sdk.core.Anchor2D)">
<h3>setAnchorPoint</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setAnchorPoint</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> anchorPoint)</span></div>
<div class="block">Sets an anchor point for this instance.
 <p>
 The anchor value has valid range from 0 to 1. Zero (0) for x and y means the view pin's
 upper left corner is located at the geographical location, whereas one (1) for x and y
 means that the pin will have its right bottom corner attached to the geographical
 location instead. The default value used is 0.5, 0.5, causing the view to be centered.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>anchorPoint</code> - A <code>Anchor2D</code> relative to the top-left corner of the
                    <code>ViewPin</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnchorPoint()">
<h3>getAnchorPoint</h3>
<div class="member-signature"><span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></span> <span class="element-name">getAnchorPoint</span>()</div>
<div class="block">Gets anchor point for this instance.</div>
<dl class="notes">
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
</main>





</div>
`
}</HTMLBlock>

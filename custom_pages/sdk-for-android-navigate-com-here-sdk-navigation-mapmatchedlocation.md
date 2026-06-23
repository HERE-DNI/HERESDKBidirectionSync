---
title: "MapMatchedLocation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapMatchedLocation.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.MapMatchedLocation</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapMatchedLocation</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Describes a map-matched location in the world at a given time.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#bearingInDegrees">bearingInDegrees</a></code></div>
<div class="col-last even-row-color">
<div class="block">The bearing orientation points to the direction of travel, and has the same angle as the
 street where it is matched to.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#confidence">confidence</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Confidence level (between 0 and 1) of the matched location.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#coordinates">coordinates</a></code></div>
<div class="col-last even-row-color">
<div class="block">The geographic coordinates of the map-matched location.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#horizontalAccuracyInMeters">horizontalAccuracyInMeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Horizontal accuracy measure of location.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isDrivingInTheWrongWay">isDrivingInTheWrongWay</a></code></div>
<div class="col-last even-row-color">
<div class="block">Determines if the travel direction on a one-way street is against the allowed traffic direction.</div>
</div>
<div class="col-first odd-row-color"><code>long</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#segmentOffsetInCentimeters">segmentOffsetInCentimeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Offset from start of segment in centimeters.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#segmentReference">segmentReference</a></code></div>
<div class="col-last even-row-color">
<div class="block">Reference to the current segment.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#speedInMetersPerSecond">speedInMetersPerSecond</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Speed in meters per second.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#timestamp">timestamp</a></code></div>
<div class="col-last even-row-color">
<div class="block">Timestamp of the map matched position.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,java.lang.Double)">MapMatchedLocation</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> bearingInDegrees)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>

</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="coordinates">
<h3>coordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">coordinates</span></div>
<div class="block"><p>The geographic coordinates of the map-matched location.</p></div>
</section>
</li>
<li>
<section class="detail" id="bearingInDegrees">
<h3>bearingInDegrees</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">bearingInDegrees</span></div>
<div class="block"><p>The bearing orientation points to the direction of travel, and has the same angle as the
 street where it is matched to. Therefore, it must not necessarily be the same as the
 bearing of a location source.
 Starts at 0 in the geographic north and rotates in a clockwise direction around the
 compass. It means that for going north it's equal to 0, for northeast it's equal to 45,
 for east it's equal to 90, and so on.
 If it cannot be determined, the value is <code>null</code>. Otherwise, it is guaranteed to be in the
 range [0, 360).</p></div>
</section>
</li>
<li>
<section class="detail" id="segmentReference">
<h3>segmentReference</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span class="element-name">segmentReference</span></div>
<div class="block"><p>Reference to the current segment.
 The ratio of <a href="sdk-for-android-navigate-index#segmentOffsetInCentimeters"><code>segmentOffsetInCentimeters</code></a> to the segment length is
 between <a href="sdk-for-android-navigate-segmentreference#offsetStart"><code>SegmentReference.offsetStart</code></a> and <a href="sdk-for-android-navigate-segmentreference#offsetEnd"><code>SegmentReference.offsetEnd</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="segmentOffsetInCentimeters">
<h3>segmentOffsetInCentimeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">segmentOffsetInCentimeters</span></div>
<div class="block"><p>Offset from start of segment in centimeters.</p></div>
</section>
</li>
<li>
<section class="detail" id="confidence">
<h3>confidence</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">confidence</span></div>
<div class="block"><p>Confidence level (between 0 and 1) of the matched location.
 A low confidence value means that the map-matched vehicle location is not reliable and it may
 not be clear which part of the road the vehicle has taken. This can happen when the accuracy
 or frequency of the provided location updates is poor. If the confidence level is too small
 then, for example, overspeed warnings may be also inaccurate.</p></div>
</section>
</li>
<li>
<section class="detail" id="isDrivingInTheWrongWay">
<h3>isDrivingInTheWrongWay</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDrivingInTheWrongWay</span></div>
<div class="block"><p>Determines if the travel direction on a one-way street is against the allowed traffic direction.
 For two-way streets, this value is always <code>false</code>.
 This feature is supported in tracking mode and when deviating from a route.
 Note that the travel direction is determined based on the map-matched location.</p></div>
</section>
</li>
<li>
<section class="detail" id="horizontalAccuracyInMeters">
<h3>horizontalAccuracyInMeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">horizontalAccuracyInMeters</span></div>
<div class="block"><p>Horizontal accuracy measure of location.
 Estimated based on accuracy of input location and confidence of this map-matched location.
 Currently this value is not being provided by the Navigator.</p></div>
</section>
</li>
<li>
<section class="detail" id="speedInMetersPerSecond">
<h3>speedInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">speedInMetersPerSecond</span></div>
<div class="block"><p>Speed in meters per second.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section class="detail" id="timestamp">
<h3>timestamp</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">timestamp</span></div>
<div class="block"><p>Timestamp of the map matched position.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,java.lang.Double)">
<h3>MapMatchedLocation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMatchedLocation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> bearingInDegrees)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The geographic coordinates of the map-matched location.</p></dd>
<dd><code>bearingInDegrees</code> - <p>The bearing orientation points to the direction of travel, and has the same angle as the
 street where it is matched to. Therefore, it must not necessarily be the same as the
 bearing of a location source.
 Starts at 0 in the geographic north and rotates in a clockwise direction around the
 compass. It means that for going north it's equal to 0, for northeast it's equal to 45,
 for east it's equal to 90, and so on.
 If it cannot be determined, the value is <code>null</code>. Otherwise, it is guaranteed to be in the
 range [0, 360).</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
`
}</HTMLBlock>

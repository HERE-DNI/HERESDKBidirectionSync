---
title: "MapMatchedLocation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapMatchedLocation.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.MapMatchedLocation</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapMatchedLocation</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Describes a map-matched location in the world at a given time.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#bearingInDegrees">bearingInDegrees</a></code></div>
<div className="col-last even-row-color">
<div className="block">The bearing orientation points to the direction of travel, and has the same angle as the
 street where it is matched to.</div>
</div>
<div className="col-first odd-row-color"><code>double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#confidence">confidence</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Confidence level (between 0 and 1) of the matched location.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#coordinates">coordinates</a></code></div>
<div className="col-last even-row-color">
<div className="block">The geographic coordinates of the map-matched location.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#horizontalAccuracyInMeters">horizontalAccuracyInMeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Horizontal accuracy measure of location.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#isDrivingInTheWrongWay">isDrivingInTheWrongWay</a></code></div>
<div className="col-last even-row-color">
<div className="block">Determines if the travel direction on a one-way street is against the allowed traffic direction.</div>
</div>
<div className="col-first odd-row-color"><code>long</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#segmentOffsetInCentimeters">segmentOffsetInCentimeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Offset from start of segment in centimeters.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#segmentReference">segmentReference</a></code></div>
<div className="col-last even-row-color">
<div className="block">Reference to the current segment.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#speedInMetersPerSecond">speedInMetersPerSecond</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Speed in meters per second.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#timestamp">timestamp</a></code></div>
<div className="col-last even-row-color">
<div className="block">Timestamp of the map matched position.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,java.lang.Double)">MapMatchedLocation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> bearingInDegrees)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="coordinates">
<h3>coordinates</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">coordinates</span></div>
<div className="block"><p>The geographic coordinates of the map-matched location.</p></div>
</section>
</li>
<li>
<section className="detail" id="bearingInDegrees">
<h3>bearingInDegrees</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">bearingInDegrees</span></div>
<div className="block"><p>The bearing orientation points to the direction of travel, and has the same angle as the
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
<section className="detail" id="segmentReference">
<h3>segmentReference</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span className="element-name">segmentReference</span></div>
<div className="block"><p>Reference to the current segment.
 The ratio of <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation#segmentOffsetInCentimeters"><code>segmentOffsetInCentimeters</code></a> to the segment length is
 between <a href="sdk-for-android-navigate-segmentreference#offsetStart"><code>SegmentReference.offsetStart</code></a> and <a href="sdk-for-android-navigate-segmentreference#offsetEnd"><code>SegmentReference.offsetEnd</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="segmentOffsetInCentimeters">
<h3>segmentOffsetInCentimeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">segmentOffsetInCentimeters</span></div>
<div className="block"><p>Offset from start of segment in centimeters.</p></div>
</section>
</li>
<li>
<section className="detail" id="confidence">
<h3>confidence</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">confidence</span></div>
<div className="block"><p>Confidence level (between 0 and 1) of the matched location.
 A low confidence value means that the map-matched vehicle location is not reliable and it may
 not be clear which part of the road the vehicle has taken. This can happen when the accuracy
 or frequency of the provided location updates is poor. If the confidence level is too small
 then, for example, overspeed warnings may be also inaccurate.</p></div>
</section>
</li>
<li>
<section className="detail" id="isDrivingInTheWrongWay">
<h3>isDrivingInTheWrongWay</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isDrivingInTheWrongWay</span></div>
<div className="block"><p>Determines if the travel direction on a one-way street is against the allowed traffic direction.
 For two-way streets, this value is always <code>false</code>.
 This feature is supported in tracking mode and when deviating from a route.
 Note that the travel direction is determined based on the map-matched location.</p></div>
</section>
</li>
<li>
<section className="detail" id="horizontalAccuracyInMeters">
<h3>horizontalAccuracyInMeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">horizontalAccuracyInMeters</span></div>
<div className="block"><p>Horizontal accuracy measure of location.
 Estimated based on accuracy of input location and confidence of this map-matched location.
 Currently this value is not being provided by the Navigator.</p></div>
</section>
</li>
<li>
<section className="detail" id="speedInMetersPerSecond">
<h3>speedInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">speedInMetersPerSecond</span></div>
<div className="block"><p>Speed in meters per second.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section className="detail" id="timestamp">
<h3>timestamp</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">timestamp</span></div>
<div className="block"><p>Timestamp of the map matched position.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,java.lang.Double)">
<h3>MapMatchedLocation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapMatchedLocation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> bearingInDegrees)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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

---
title: "Location (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-location"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Location.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.Location</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Location</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Describes a location in the world at a given time.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#bearingAccuracyInDegrees">bearingAccuracyInDegrees</a></code></div>
<div className="col-last even-row-color">
<div className="block">Estimated bearing accuracy for this location, in degrees.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#bearingInDegrees">bearingInDegrees</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Bearing (also known as course) is the device's horizontal direction of travel.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#coordinates">coordinates</a></code></div>
<div className="col-last even-row-color">
<div className="block">The geographic coordinates of the location.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#gnssTime">gnssTime</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Optional gnss time at which the location was determined.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#horizontalAccuracyInMeters">horizontalAccuracyInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">The estimated horizontal accuracy.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-locationtechnology" title="enum class in com.here.sdk.core">LocationTechnology</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#locationTechnology">locationTechnology</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Optional technology or provider of this location.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#pitchInDegrees">pitchInDegrees</a></code></div>
<div className="col-last even-row-color">
<div className="block">Pitch of this location, in degrees.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-locationsource" title="enum class in com.here.sdk.core">LocationSource</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#source">source</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Optional source of this location.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#speedAccuracyInMetersPerSecond">speedAccuracyInMetersPerSecond</a></code></div>
<div className="col-last even-row-color">
<div className="block">Estimated speed accuracy of this location, in meters per second.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#speedInMetersPerSecond">speedInMetersPerSecond</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Current speed of the device.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#time">time</a></code></div>
<div className="col-last even-row-color">
<div className="block">The time at which the location was determined.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#timestampSinceBoot">timestampSinceBoot</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The time at which the location was determined, relative to device
 boot time.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#verticalAccuracyInMeters">verticalAccuracyInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">Estimated vertical accuracy.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#%3Cinit%3E(com.here.sdk.core.GeoCoordinates)">Location</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new Location instance from the provided GeoCoordinates value.</div>
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
<div className="block"><p>The geographic coordinates of the location.</p></div>
</section>
</li>
<li>
<section className="detail" id="bearingInDegrees">
<h3>bearingInDegrees</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">bearingInDegrees</span></div>
<div className="block"><p>Bearing (also known as course) is the device's horizontal direction of travel.
 Starts at 0 in the geographical north and rotates around the compass in a clockwise
 direction. This means for going north it is equal to 0, for northeast it is 45,
 for east it is 90 and so on. Note that this may be different from the orientation of
 the device. If it cannot be determined, the value is <code>null</code>. Otherwise, it is
 guaranteed to be in the range [0, 360).</p></div>
</section>
</li>
<li>
<section className="detail" id="speedInMetersPerSecond">
<h3>speedInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">speedInMetersPerSecond</span></div>
<div className="block"><p>Current speed of the device. If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="time">
<h3>time</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">time</span></div>
<div className="block"><p>The time at which the location was determined.</p></div>
</section>
</li>
<li>
<section className="detail" id="horizontalAccuracyInMeters">
<h3>horizontalAccuracyInMeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">horizontalAccuracyInMeters</span></div>
<div className="block"><p>The estimated horizontal accuracy. The actual location will lie within this radius of uncertainty.</p></div>
</section>
</li>
<li>
<section className="detail" id="verticalAccuracyInMeters">
<h3>verticalAccuracyInMeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">verticalAccuracyInMeters</span></div>
<div className="block"><p>Estimated vertical accuracy.
 Given that the received Location contains the altitude, the real value of the altitude
 is estimated to lie within the following range:
 [altitude - vertical accuracy, altitude + vertical accuracy].
 For example, when the altitude is equal to 50 and the vertical accuracy
 is 8, then the actual value is most likely in the range [42, 58].</p></div>
</section>
</li>
<li>
<section className="detail" id="bearingAccuracyInDegrees">
<h3>bearingAccuracyInDegrees</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">bearingAccuracyInDegrees</span></div>
<div className="block"><p>Estimated bearing accuracy for this location, in degrees.
 If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="speedAccuracyInMetersPerSecond">
<h3>speedAccuracyInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">speedAccuracyInMetersPerSecond</span></div>
<div className="block"><p>Estimated speed accuracy of this location, in meters per second.
 If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="timestampSinceBoot">
<h3>timestampSinceBoot</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">timestampSinceBoot</span></div>
<div className="block"><p>The time at which the location was determined, relative to device
 boot time. This time is monotonic and not affected by leap time or other system
 time adjustments, so this is the recommended basis for general purpose interval timing
 between location updates.
 If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="locationTechnology">
<h3>locationTechnology</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-locationtechnology" title="enum class in com.here.sdk.core">LocationTechnology</a></span> <span className="element-name">locationTechnology</span></div>
<div className="block"><p>Optional technology or provider of this location.
 If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="source">
<h3>source</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-locationsource" title="enum class in com.here.sdk.core">LocationSource</a></span> <span className="element-name">source</span></div>
<div className="block"><p>Optional source of this location.
 If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="gnssTime">
<h3>gnssTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">gnssTime</span></div>
<div className="block"><p>Optional gnss time at which the location was determined.
 It is a time interval from the Unix time epoch in milliseconds.
 If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="pitchInDegrees">
<h3>pitchInDegrees</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">pitchInDegrees</span></div>
<div className="block"><p>Pitch of this location, in degrees.
 If it cannot be determined, the value is <code>null</code>.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates)">
<h3>Location</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Location</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div className="block"><p>Creates a new Location instance from the provided GeoCoordinates value.
 timestamp is initialized with <code>January 1, 1970, 00:00:00 GMT</code> value.
 The rest of the fields will be initialized to null.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The geographic coordinates of the location.</p></dd>
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

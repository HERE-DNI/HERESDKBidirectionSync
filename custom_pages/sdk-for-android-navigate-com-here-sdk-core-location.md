---
title: "Location (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-location"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Location.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.core.Location</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Location</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Describes a location in the world at a given time.</p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#bearingAccuracyInDegrees">bearingAccuracyInDegrees</a></code></div>
<div class="col-last even-row-color">
<div class="block">Estimated bearing accuracy for this location, in degrees.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#bearingInDegrees">bearingInDegrees</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Bearing (also known as course) is the device's horizontal direction of travel.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#coordinates">coordinates</a></code></div>
<div class="col-last even-row-color">
<div class="block">The geographic coordinates of the location.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#gnssTime">gnssTime</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional gnss time at which the location was determined.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#horizontalAccuracyInMeters">horizontalAccuracyInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">The estimated horizontal accuracy.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-locationtechnology" title="enum class in com.here.sdk.core">LocationTechnology</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#locationTechnology">locationTechnology</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional technology or provider of this location.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#pitchInDegrees">pitchInDegrees</a></code></div>
<div class="col-last even-row-color">
<div class="block">Pitch of this location, in degrees.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-locationsource" title="enum class in com.here.sdk.core">LocationSource</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#source">source</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional source of this location.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#speedAccuracyInMetersPerSecond">speedAccuracyInMetersPerSecond</a></code></div>
<div class="col-last even-row-color">
<div class="block">Estimated speed accuracy of this location, in meters per second.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#speedInMetersPerSecond">speedInMetersPerSecond</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Current speed of the device.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#time">time</a></code></div>
<div class="col-last even-row-color">
<div class="block">The time at which the location was determined.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#timestampSinceBoot">timestampSinceBoot</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The time at which the location was determined, relative to device
 boot time.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#verticalAccuracyInMeters">verticalAccuracyInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Estimated vertical accuracy.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#%3Cinit%3E(com.here.sdk.core.GeoCoordinates)">Location</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new Location instance from the provided GeoCoordinates value.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-location#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">coordinates</span></div>
<div class="block"><p>The geographic coordinates of the location.</p></div>
</section>
</li>
<li>
<section class="detail" id="bearingInDegrees">
<h3>bearingInDegrees</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">bearingInDegrees</span></div>
<div class="block"><p>Bearing (also known as course) is the device's horizontal direction of travel.
 Starts at 0 in the geographical north and rotates around the compass in a clockwise
 direction. This means for going north it is equal to 0, for northeast it is 45,
 for east it is 90 and so on. Note that this may be different from the orientation of
 the device. If it cannot be determined, the value is <code>null</code>. Otherwise, it is
 guaranteed to be in the range [0, 360).</p></div>
</section>
</li>
<li>
<section class="detail" id="speedInMetersPerSecond">
<h3>speedInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">speedInMetersPerSecond</span></div>
<div class="block"><p>Current speed of the device. If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="time">
<h3>time</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">time</span></div>
<div class="block"><p>The time at which the location was determined.</p></div>
</section>
</li>
<li>
<section class="detail" id="horizontalAccuracyInMeters">
<h3>horizontalAccuracyInMeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">horizontalAccuracyInMeters</span></div>
<div class="block"><p>The estimated horizontal accuracy. The actual location will lie within this radius of uncertainty.</p></div>
</section>
</li>
<li>
<section class="detail" id="verticalAccuracyInMeters">
<h3>verticalAccuracyInMeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">verticalAccuracyInMeters</span></div>
<div class="block"><p>Estimated vertical accuracy.
 Given that the received Location contains the altitude, the real value of the altitude
 is estimated to lie within the following range:
 [altitude - vertical accuracy, altitude + vertical accuracy].
 For example, when the altitude is equal to 50 and the vertical accuracy
 is 8, then the actual value is most likely in the range [42, 58].</p></div>
</section>
</li>
<li>
<section class="detail" id="bearingAccuracyInDegrees">
<h3>bearingAccuracyInDegrees</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">bearingAccuracyInDegrees</span></div>
<div class="block"><p>Estimated bearing accuracy for this location, in degrees.
 If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="speedAccuracyInMetersPerSecond">
<h3>speedAccuracyInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">speedAccuracyInMetersPerSecond</span></div>
<div class="block"><p>Estimated speed accuracy of this location, in meters per second.
 If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="timestampSinceBoot">
<h3>timestampSinceBoot</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">timestampSinceBoot</span></div>
<div class="block"><p>The time at which the location was determined, relative to device
 boot time. This time is monotonic and not affected by leap time or other system
 time adjustments, so this is the recommended basis for general purpose interval timing
 between location updates.
 If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="locationTechnology">
<h3>locationTechnology</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-locationtechnology" title="enum class in com.here.sdk.core">LocationTechnology</a></span> <span class="element-name">locationTechnology</span></div>
<div class="block"><p>Optional technology or provider of this location.
 If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="source">
<h3>source</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-locationsource" title="enum class in com.here.sdk.core">LocationSource</a></span> <span class="element-name">source</span></div>
<div class="block"><p>Optional source of this location.
 If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="gnssTime">
<h3>gnssTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">gnssTime</span></div>
<div class="block"><p>Optional gnss time at which the location was determined.
 It is a time interval from the Unix time epoch in milliseconds.
 If it cannot be determined, the value is <code>null</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="pitchInDegrees">
<h3>pitchInDegrees</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">pitchInDegrees</span></div>
<div class="block"><p>Pitch of this location, in degrees.
 If it cannot be determined, the value is <code>null</code>.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates)">
<h3>Location</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Location</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div class="block"><p>Creates a new Location instance from the provided GeoCoordinates value.
 timestamp is initialized with <code>January 1, 1970, 00:00:00 GMT</code> value.
 The rest of the fields will be initialized to null.</p></div>
<dl class="notes">
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
</div>



</div>
`
}</HTMLBlock>

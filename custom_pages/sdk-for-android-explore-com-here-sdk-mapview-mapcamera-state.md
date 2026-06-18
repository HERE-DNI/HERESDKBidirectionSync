---
title: "MapCamera.State (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapCamera.State.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapview.MapCamera.State</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-explore-mapcamera" title="class in com.here.sdk.mapview">MapCamera</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">MapCamera.State</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Encapsulates state of the camera.</p></div>
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
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#distanceToTargetInMeters">distanceToTargetInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Distance from the camera to the target point in meters.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-explore-geoorientation" title="class in com.here.sdk.core">GeoOrientation</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#orientationAtTarget">orientationAtTarget</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Camera's orientation at target point.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#targetCoordinates">targetCoordinates</a></code></div>
<div class="col-last even-row-color">
<div class="block">Camera's 'LookAt' target position in geodetic space.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#zoomLevel">zoomLevel</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Zoom level corresponding to the current distance to target.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoOrientation,double,double)">State</a><wbr/>(<a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> targetCoordinates,
 <a href="sdk-for-android-explore-geoorientation" title="class in com.here.sdk.core">GeoOrientation</a> orientationAtTarget,
 double distanceToTargetInMeters,
 double zoomLevel)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="targetCoordinates">
<h3>targetCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">targetCoordinates</span></div>
<div class="block"><p>Camera's 'LookAt' target position in geodetic space.
 </p><p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
</section>
</li>
<li>
<section class="detail" id="orientationAtTarget">
<h3>orientationAtTarget</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-geoorientation" title="class in com.here.sdk.core">GeoOrientation</a></span> <span class="element-name">orientationAtTarget</span></div>
<div class="block"><p>Camera's orientation at target point.</p></div>
</section>
</li>
<li>
<section class="detail" id="distanceToTargetInMeters">
<h3>distanceToTargetInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceToTargetInMeters</span></div>
<div class="block"><p>Distance from the camera to the target point in meters.</p></div>
</section>
</li>
<li>
<section class="detail" id="zoomLevel">
<h3>zoomLevel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">zoomLevel</span></div>
<div class="block"><p>Zoom level corresponding to the current distance to target.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoOrientation,double,double)">
<h3>State</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">State</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> targetCoordinates,
 @NonNull
 <a href="sdk-for-android-explore-geoorientation" title="class in com.here.sdk.core">GeoOrientation</a> orientationAtTarget,
 double distanceToTargetInMeters,
 double zoomLevel)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetCoordinates</code> - <p>Camera's 'LookAt' target position in geodetic space.
 </p><p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></dd>
<dd><code>orientationAtTarget</code> - <p>Camera's orientation at target point.</p></dd>
<dd><code>distanceToTargetInMeters</code> - <p>Distance from the camera to the target point in meters.</p></dd>
<dd><code>zoomLevel</code> - <p>Zoom level corresponding to the current distance to target.</p></dd>
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

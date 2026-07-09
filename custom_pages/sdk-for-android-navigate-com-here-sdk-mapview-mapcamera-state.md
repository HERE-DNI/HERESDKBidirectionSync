---
title: "MapCamera.State (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapcamera-state"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapCamera.State.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapview.MapCamera.State</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera" title="class in com.here.sdk.mapview">MapCamera</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">MapCamera.State</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Encapsulates state of the camera.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera-state#distanceToTargetInMeters">distanceToTargetInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">Distance from the camera to the target point in meters.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geoorientation" title="class in com.here.sdk.core">GeoOrientation</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera-state#orientationAtTarget">orientationAtTarget</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Camera's orientation at target point.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera-state#targetCoordinates">targetCoordinates</a></code></div>
<div className="col-last even-row-color">
<div className="block">Camera's 'LookAt' target position in geodetic space.</div>
</div>
<div className="col-first odd-row-color"><code>double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera-state#zoomLevel">zoomLevel</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Zoom level corresponding to the current distance to target.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera-state#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoOrientation,double,double)">State</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> targetCoordinates,
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientation" title="class in com.here.sdk.core">GeoOrientation</a> orientationAtTarget,
 double distanceToTargetInMeters,
 double zoomLevel)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section className="detail" id="targetCoordinates">
<h3>targetCoordinates</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">targetCoordinates</span></div>
<div className="block"><p>Camera's 'LookAt' target position in geodetic space.
 Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
</section>
</li>
<li>
<section className="detail" id="orientationAtTarget">
<h3>orientationAtTarget</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geoorientation" title="class in com.here.sdk.core">GeoOrientation</a></span> <span className="element-name">orientationAtTarget</span></div>
<div className="block"><p>Camera's orientation at target point.</p></div>
</section>
</li>
<li>
<section className="detail" id="distanceToTargetInMeters">
<h3>distanceToTargetInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">distanceToTargetInMeters</span></div>
<div className="block"><p>Distance from the camera to the target point in meters.</p></div>
</section>
</li>
<li>
<section className="detail" id="zoomLevel">
<h3>zoomLevel</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">zoomLevel</span></div>
<div className="block"><p>Zoom level corresponding to the current distance to target.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoOrientation,double,double)">
<h3>State</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">State</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> targetCoordinates,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientation" title="class in com.here.sdk.core">GeoOrientation</a> orientationAtTarget,
 double distanceToTargetInMeters,
 double zoomLevel)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>targetCoordinates</code> - <p>Camera's 'LookAt' target position in geodetic space.
 Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
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

</div>
</div>



</div>
`
}</HTMLBlock>

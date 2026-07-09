---
title: "FixedCameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- FixedCameraBehavior.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.navigation.FixedCameraBehavior</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">FixedCameraBehavior</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></span></div>
<div className="block"><p>Use this class to follow the current location of the user: The camera will permanently look at
 the target location that was fed into the navigator instance. Since location updates happen in
 discrete intervals, locations in-between will be interpolated to achieve a smooth camera
 movement.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#%3Cinit%3E()">FixedCameraBehavior</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>FixedCameraBehavior</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">FixedCameraBehavior</span>()</div>
<div className="block"><p>Creates a new instance of this class.</p></div>
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
<section className="detail" id="getCameraDistanceInMeters()">
<h3>getCameraDistanceInMeters</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getCameraDistanceInMeters</span>()</div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use <a href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#getZoom()"><code>getZoom()</code></a> instead.</p></div>
</div>
<div className="block"><p>Gets the currently set camera distance to current location. The default value is 150 meters.
 Camera distance to current location. The default value is 150 meters.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Camera distance in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCameraDistanceInMeters(double)">
<h3>setCameraDistanceInMeters</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCameraDistanceInMeters</span><wbr/><span className="parameters">(double value)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use <a href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#getZoom()"><code>getZoom()</code></a> instead.</p></div>
</div>
<div className="block"><p>Sets the camera distance to current location. The default value is 150 meters.
 Camera distance to current location. The default value is 150 meters.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Camera distance in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getZoom()">
<h3>getZoom</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a></span> <span className="element-name">getZoom</span>()</div>
<div className="block"><p>Gets the current camera's zoom configuration.
 Camera zoom configuration. The default value is 150 meters.
 Note: <a href="sdk-for-android-navigate-mapmeasure-kind#SCALE"><code>MapMeasure.Kind.SCALE</code></a> is not supported.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Zoom configuration. The default value is 150 meters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setZoom(com.here.sdk.mapview.MapMeasure)">
<h3>setZoom</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setZoom</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> value)</span></div>
<div className="block"><p>Sets the current camera's zoom configuration.
 Camera zoom configuration. The default value is 150 meters.
 Note: <a href="sdk-for-android-navigate-mapmeasure-kind#SCALE"><code>MapMeasure.Kind.SCALE</code></a> is not supported.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Zoom configuration. The default value is 150 meters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCameraTiltInDegrees()">
<h3>getCameraTiltInDegrees</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getCameraTiltInDegrees</span>()</div>
<div className="block"><p>Gets the currently set camera tilt with axis parallel to the ground. The default value is 50 degrees.
 The default value is 50 degrees.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Camera tilt with axis parallel to the ground.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCameraTiltInDegrees(double)">
<h3>setCameraTiltInDegrees</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCameraTiltInDegrees</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets camera tilt with axis parallel to the ground.
 The default value is 50 degrees.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Camera tilt with axis parallel to the ground.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCameraBearingInDegrees()">
<h3>getCameraBearingInDegrees</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getCameraBearingInDegrees</span>()</div>
<div className="block"><p>Gets the currently set fixed bearing.
 Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range
 is [0, 360].
 If set, it will prevent the map from rotating to the direction of travel. For example, a
 value of zero results in "north up" mode.
 Defaults to <code>null</code>, which means the camera derives the bearing from the <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core"><code>Location</code></a>,
 so that it points to the direction of travel.
 If this property is <code>null</code> and the device does not provide bearing, the last known value is
 used or zero otherwise.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Camera bearing in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCameraBearingInDegrees(java.lang.Double)">
<h3>setCameraBearingInDegrees</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCameraBearingInDegrees</span><wbr/><span className="parameters">(@Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value)</span></div>
<div className="block"><p>Sets an optional fixed bearing value, from true North (0 degrees) in clockwise direction.
 Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range
 is [0, 360].
 If set, it will prevent the map from rotating to the direction of travel. For example, a
 value of zero results in "north up" mode.
 Defaults to <code>null</code>, which means the camera derives the bearing from the <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core"><code>Location</code></a>,
 so that it points to the direction of travel.
 If this property is <code>null</code> and the device does not provide bearing, the last known value is
 used or zero otherwise.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Camera bearing in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getNormalizedPrincipalPoint()">
<h3>getNormalizedPrincipalPoint</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></span> <span className="element-name">getNormalizedPrincipalPoint</span>()</div>
<div className="block"><p>Gets the currently set normalized principal point to be used during navigation.
 Normalized principal point to be used during navigation.
 Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
 of the mapview.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-camerabehavior#getNormalizedPrincipalPoint()">getNormalizedPrincipalPoint</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></code></dd>
<dt>Returns:</dt>
<dd><p>The normalized principal point.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">
<h3>setNormalizedPrincipalPoint</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setNormalizedPrincipalPoint</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</span></div>
<div className="block"><p>Sets a normalized principal point to be used during navigation.
 Normalized principal point to be used during navigation.
 Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
 of the mapview.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-camerabehavior#setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">setNormalizedPrincipalPoint</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The normalized principal point.</p></dd>
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

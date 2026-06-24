---
title: "FixedCameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- FixedCameraBehavior.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.navigation.FixedCameraBehavior</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">FixedCameraBehavior</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></span></div>
<div class="block"><p>Use this class to follow the current location of the user: The camera will permanently look at
 the target location that was fed into the navigator instance. Since location updates happen in
 discrete intervals, locations in-between will be interpolated to achieve a smooth camera
 movement.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#%3Cinit%3E()">FixedCameraBehavior</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#getCameraBearingInDegrees()">getCameraBearingInDegrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently set fixed bearing.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#getCameraDistanceInMeters()">getCameraDistanceInMeters</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#getCameraTiltInDegrees()">getCameraTiltInDegrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently set camera tilt with axis parallel to the ground.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#getNormalizedPrincipalPoint()">getNormalizedPrincipalPoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently set normalized principal point to be used during navigation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#getZoom()">getZoom</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current camera's zoom configuration.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#setCameraBearingInDegrees(java.lang.Double)">setCameraBearingInDegrees</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets an optional fixed bearing value, from true North (0 degrees) in clockwise direction.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#setCameraDistanceInMeters(double)">setCameraDistanceInMeters</a><wbr/>(double value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#setCameraTiltInDegrees(double)">setCameraTiltInDegrees</a><wbr/>(double value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets camera tilt with axis parallel to the ground.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">setNormalizedPrincipalPoint</a><wbr/>(<a href="sdk-for-android-navigate-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a normalized principal point to be used during navigation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#setZoom(com.here.sdk.mapview.MapMeasure)">setZoom</a><wbr/>(<a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the current camera's zoom configuration.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>FixedCameraBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">FixedCameraBehavior</span>()</div>
<div class="block"><p>Creates a new instance of this class.</p></div>
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
<section class="detail" id="getCameraDistanceInMeters()">
<h3>getCameraDistanceInMeters</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getCameraDistanceInMeters</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use <a href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#getZoom()"><code>getZoom()</code></a> instead.</p></div>
</div>
<div class="block"><p>Gets the currently set camera distance to current location. The default value is 150 meters.
 </p><p>Camera distance to current location. The default value is 150 meters.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Camera distance in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCameraDistanceInMeters(double)">
<h3>setCameraDistanceInMeters</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraDistanceInMeters</span><wbr/><span class="parameters">(double value)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use <a href="sdk-for-android-navigate-com-here-sdk-navigation-fixedcamerabehavior#getZoom()"><code>getZoom()</code></a> instead.</p></div>
</div>
<div class="block"><p>Sets the camera distance to current location. The default value is 150 meters.
 </p><p>Camera distance to current location. The default value is 150 meters.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Camera distance in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getZoom()">
<h3>getZoom</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a></span> <span class="element-name">getZoom</span>()</div>
<div class="block"><p>Gets the current camera's zoom configuration.
 </p><p>Camera zoom configuration. The default value is 150 meters.
 Note: <a href="sdk-for-android-navigate-mapmeasure.kind#SCALE"><code>MapMeasure.Kind.SCALE</code></a> is not supported.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Zoom configuration. The default value is 150 meters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setZoom(com.here.sdk.mapview.MapMeasure)">
<h3>setZoom</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setZoom</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> value)</span></div>
<div class="block"><p>Sets the current camera's zoom configuration.
 </p><p>Camera zoom configuration. The default value is 150 meters.
 Note: <a href="sdk-for-android-navigate-mapmeasure.kind#SCALE"><code>MapMeasure.Kind.SCALE</code></a> is not supported.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Zoom configuration. The default value is 150 meters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCameraTiltInDegrees()">
<h3>getCameraTiltInDegrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getCameraTiltInDegrees</span>()</div>
<div class="block"><p>Gets the currently set camera tilt with axis parallel to the ground. The default value is 50 degrees.
 </p><p>The default value is 50 degrees.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Camera tilt with axis parallel to the ground.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCameraTiltInDegrees(double)">
<h3>setCameraTiltInDegrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraTiltInDegrees</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets camera tilt with axis parallel to the ground.
 </p><p>The default value is 50 degrees.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Camera tilt with axis parallel to the ground.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCameraBearingInDegrees()">
<h3>getCameraBearingInDegrees</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getCameraBearingInDegrees</span>()</div>
<div class="block"><p>Gets the currently set fixed bearing.
 </p><p>Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range
 is [0, 360].
 If set, it will prevent the map from rotating to the direction of travel. For example, a
 value of zero results in "north up" mode.
 Defaults to <code>null</code>, which means the camera derives the bearing from the <a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core"><code>Location</code></a>,
 so that it points to the direction of travel.
 If this property is <code>null</code> and the device does not provide bearing, the last known value is
 used or zero otherwise.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Camera bearing in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCameraBearingInDegrees(java.lang.Double)">
<h3>setCameraBearingInDegrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraBearingInDegrees</span><wbr/><span class="parameters">(@Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value)</span></div>
<div class="block"><p>Sets an optional fixed bearing value, from true North (0 degrees) in clockwise direction.
 </p><p>Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range
 is [0, 360].
 If set, it will prevent the map from rotating to the direction of travel. For example, a
 value of zero results in "north up" mode.
 Defaults to <code>null</code>, which means the camera derives the bearing from the <a href="sdk-for-android-navigate-location" title="class in com.here.sdk.core"><code>Location</code></a>,
 so that it points to the direction of travel.
 If this property is <code>null</code> and the device does not provide bearing, the last known value is
 used or zero otherwise.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Camera bearing in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNormalizedPrincipalPoint()">
<h3>getNormalizedPrincipalPoint</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></span> <span class="element-name">getNormalizedPrincipalPoint</span>()</div>
<div class="block"><p>Gets the currently set normalized principal point to be used during navigation.
 </p><p>Normalized principal point to be used during navigation.
 Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
 of the mapview.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-camerabehavior#getNormalizedPrincipalPoint()">getNormalizedPrincipalPoint</a></code> in interface <code><a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></code></dd>
<dt>Returns:</dt>
<dd><p>The normalized principal point.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">
<h3>setNormalizedPrincipalPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNormalizedPrincipalPoint</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</span></div>
<div class="block"><p>Sets a normalized principal point to be used during navigation.
 </p><p>Normalized principal point to be used during navigation.
 Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
 of the mapview.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-camerabehavior#setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">setNormalizedPrincipalPoint</a></code> in interface <code><a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></code></dd>
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
`
}</HTMLBlock>

---
title: "AreaCameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-areacamerabehavior"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- AreaCameraBehavior.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.navigation.AreaCameraBehavior</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">AreaCameraBehavior</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></span></div>
<div class="block"><p>Use this class to show an overview of geo points. By default, the orientation of the camera will be
 perpendicular to the Earth's surface (ie. looking towards the center of the Earth),
 while bearing will be towards north.
 </p><p>Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are
 subject to change without a deprecation process.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AreaCameraBehavior</a>()</code></div>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCameraAnimationDuration()">getCameraAnimationDuration</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current animation duration in milliseconds.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCameraBearingInDegrees()">getCameraBearingInDegrees</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current camera bearing.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCameraTiltInDegrees()">getCameraTiltInDegrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current camera tilt.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMaxZoom()">getMaxZoom</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets maximal allowed zoom.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNormalizedPrincipalPoint()">getNormalizedPrincipalPoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently set normalized principal point to be used during navigation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPrincipalPointAnimationDuration()">getPrincipalPointAnimationDuration</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current principal point animation duration in milliseconds.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getViewRectangle()">getViewRectangle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current view rectangle, if it's set.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisiblePoints()">getVisiblePoints</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets configured visible geo points.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCurrentPositionIncluded()">isCurrentPositionIncluded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets whether to include the current position.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCameraAnimationDuration(com.here.time.Duration)">setCameraAnimationDuration</a><wbr/>(<a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the current animation duration in milliseconds.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCameraBearingInDegrees(double)">setCameraBearingInDegrees</a><wbr/>(double value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets camera bearing.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCameraTiltInDegrees(double)">setCameraTiltInDegrees</a><wbr/>(double value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets camera tilt.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCurrentPositionIncluded(boolean)">setCurrentPositionIncluded</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether to include the current position.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMaxZoom(com.here.sdk.mapview.MapMeasure)">setMaxZoom</a><wbr/>(<a href="sdk-for-android-navigate-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets maximal allowed zoom.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">setNormalizedPrincipalPoint</a><wbr/>(<a href="sdk-for-android-navigate-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a normalized principal point to be used during navigation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPrincipalPointAnimationDuration(com.here.time.Duration)">setPrincipalPointAnimationDuration</a><wbr/>(<a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the current principal point animation in milliseconds.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setViewRectangle(com.here.sdk.core.Rectangle2D)">setViewRectangle</a><wbr/>(<a href="sdk-for-android-navigate-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets view rectangle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVisiblePoints(java.util.List)">setVisiblePoints</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; visiblePoints)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the list of geo points to show in the camera view.</div>
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
<h3>AreaCameraBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AreaCameraBehavior</span>()</div>
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
<section class="detail" id="setVisiblePoints(java.util.List)">
<h3>setVisiblePoints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisiblePoints</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; visiblePoints)</span></div>
<div class="block"><p>Sets the list of geo points to show in the camera view.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visiblePoints</code> - <p>The list of geo points to visualize. The list can be empty.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisiblePoints()">
<h3>getVisiblePoints</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;</span> <span class="element-name">getVisiblePoints</span>()</div>
<div class="block"><p>Gets configured visible geo points.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of geo points to show in the camera view. The list can be empty.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getViewRectangle()">
<h3>getViewRectangle</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a></span> <span class="element-name">getViewRectangle</span>()</div>
<div class="block"><p>Gets the current view rectangle, if it's set.
 </p><p>Defines a sub-space of the screen that the behavior should consider
 for camera updates.
 Defaults to <code>null</code>. If not set, it uses the viewport bounds of the underlying map view.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The view rectangle for camera updates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setViewRectangle(com.here.sdk.core.Rectangle2D)">
<h3>setViewRectangle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setViewRectangle</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> value)</span></div>
<div class="block"><p>Sets view rectangle.
 </p><p>Defines a sub-space of the screen that the behavior should consider
 for camera updates.
 Defaults to <code>null</code>. If not set, it uses the viewport bounds of the underlying map view.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The view rectangle for camera updates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCameraAnimationDuration()">
<h3>getCameraAnimationDuration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getCameraAnimationDuration</span>()</div>
<div class="block"><p>Gets the current animation duration in milliseconds.
 </p><p>If there is an animation, it will last for specified period of time.
 Defaults to 500 milliseconds, or half a second.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The duration of camera animation in milliseconds.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCameraAnimationDuration(com.here.time.Duration)">
<h3>setCameraAnimationDuration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraAnimationDuration</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a> value)</span></div>
<div class="block"><p>Sets the current animation duration in milliseconds.
 </p><p>If there is an animation, it will last for specified period of time.
 Defaults to 500 milliseconds, or half a second.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The duration of camera animation in milliseconds.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrincipalPointAnimationDuration()">
<h3>getPrincipalPointAnimationDuration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getPrincipalPointAnimationDuration</span>()</div>
<div class="block"><p>Gets the current principal point animation duration in milliseconds.
 </p><p>If the principal point is changed, the change will be animated
 over this duration.
 Defaults to 500 milliseconds, or half a second.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The duration of principal point animation in milliseconds.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPrincipalPointAnimationDuration(com.here.time.Duration)">
<h3>setPrincipalPointAnimationDuration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPrincipalPointAnimationDuration</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a> value)</span></div>
<div class="block"><p>Sets the current principal point animation in milliseconds.
 </p><p>If the principal point is changed, the change will be animated
 over this duration.
 Defaults to 500 milliseconds, or half a second.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The duration of principal point animation in milliseconds.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMaxZoom()">
<h3>getMaxZoom</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a></span> <span class="element-name">getMaxZoom</span>()</div>
<div class="block"><p>Gets maximal allowed zoom.
 </p><p>Defines maximal zoom level to be applied to enclose geodetic bounding box.
 Defaults to a <a href="sdk-for-android-navigate-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> with kind <a href="sdk-for-android-navigate-mapview-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> and value 20.0.
 Note: <a href="sdk-for-android-navigate-mapview-mapmeasure.kind#SCALE"><code>MapMeasure.Kind.SCALE</code></a> is not supported.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Maximal allowed zoom.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMaxZoom(com.here.sdk.mapview.MapMeasure)">
<h3>setMaxZoom</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMaxZoom</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> value)</span></div>
<div class="block"><p>Sets maximal allowed zoom.
 </p><p>Defines maximal zoom level to be applied to enclose geodetic bounding box.
 Defaults to a <a href="sdk-for-android-navigate-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> with kind <a href="sdk-for-android-navigate-mapview-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> and value 20.0.
 Note: <a href="sdk-for-android-navigate-mapview-mapmeasure.kind#SCALE"><code>MapMeasure.Kind.SCALE</code></a> is not supported.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Maximal allowed zoom.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCameraBearingInDegrees()">
<h3>getCameraBearingInDegrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getCameraBearingInDegrees</span>()</div>
<div class="block"><p>Gets the current camera bearing.
 </p><p>The direction in which the camera will point in degrees clockwise, relative to
 true North. The input should range between [0, 360]. Defaults to true North (0 degrees).</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Camera bearing in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCameraBearingInDegrees(double)">
<h3>setCameraBearingInDegrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraBearingInDegrees</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets camera bearing.
 </p><p>The direction in which the camera will point in degrees clockwise, relative to
 true North. The input should range between [0, 360]. Defaults to true North (0 degrees).</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Camera bearing in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCameraTiltInDegrees()">
<h3>getCameraTiltInDegrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getCameraTiltInDegrees</span>()</div>
<div class="block"><p>Gets the current camera tilt.
 </p><p>The tilt of the camera relative to the axis perpendicular to the ground. Defaults to
 0 degrees, meaning that it will look straight down into the ground.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Camera tilt in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCameraTiltInDegrees(double)">
<h3>setCameraTiltInDegrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCameraTiltInDegrees</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets camera tilt.
 </p><p>The tilt of the camera relative to the axis perpendicular to the ground. Defaults to
 0 degrees, meaning that it will look straight down into the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Camera tilt in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCurrentPositionIncluded()">
<h3>isCurrentPositionIncluded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCurrentPositionIncluded</span>()</div>
<div class="block"><p>Gets whether to include the current position.
 </p><p>Decides if the current position should be added to the set of visible points.
 Note that if the current position is in the vicinity of any of the visible points, setting this to
 <code>false</code> will not explicitly exclude the current position from the camera view. However if displaying
 an area potentially away from the current position, this does need to be explicitly set to <code>false</code>
 or it will try to include the current position. Defaults to false.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Include current position in camera view.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCurrentPositionIncluded(boolean)">
<h3>setCurrentPositionIncluded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCurrentPositionIncluded</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether to include the current position.
 </p><p>Decides if the current position should be added to the set of visible points.
 Note that if the current position is in the vicinity of any of the visible points, setting this to
 <code>false</code> will not explicitly exclude the current position from the camera view. However if displaying
 an area potentially away from the current position, this does need to be explicitly set to <code>false</code>
 or it will try to include the current position. Defaults to false.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Include current position in camera view.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNormalizedPrincipalPoint()">
<h3>getNormalizedPrincipalPoint</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></span> <span class="element-name">getNormalizedPrincipalPoint</span>()</div>
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
 <a href="sdk-for-android-navigate-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</span></div>
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
</main>
</div>
</div>



</div>
`
}</HTMLBlock>

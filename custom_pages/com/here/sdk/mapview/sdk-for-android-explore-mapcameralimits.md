---
title: "MapCameraLimits (API Reference)"
slug: "sdk-for-android-explore-mapcameralimits"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapCameraLimits.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li><a href="#field-summary">Field</a> | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#field-detail">Field</a> | </li>
<li>Constr | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapCameraLimits</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapCameraLimits</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Controls constraints on map camera parameters.
 </p><p>When constraints are set, they are enforced for current camera state
 and for all future changes to the camera.
 </p><p>When setting, limits are applied on next rendering loop.</p></div>
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
<div class="col-first even-row-color"><code>static final double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MAX_TILT">MAX_TILT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Absolute maximum possible value of tilt angle.</div>
</div>
<div class="col-first odd-row-color"><code>static final double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MAX_ZOOM_LEVEL">MAX_ZOOM_LEVEL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Absolute maximum possible value of zoom level.</div>
</div>
<div class="col-first even-row-color"><code>static final double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MIN_TILT">MIN_TILT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Absolute minimum possible value of tilt angle.</div>
</div>
<div class="col-first odd-row-color"><code>static final double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MIN_ZOOM_LEVEL">MIN_ZOOM_LEVEL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Absolute minimum possible value of zoom level.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearBearingRanges()">clearBearingRanges</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clears bearing ranges for all zoom values and resets
 bearing range to default.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearTiltRanges()">clearTiltRanges</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clears tilt ranges for all zoom values and resets  tilt range to default.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-core-anglerange" title="class in com.here.sdk.core">AngleRange</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBearingRange()">getBearingRange</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently set bearing range.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-core-geobox" title="class in com.here.sdk.core">GeoBox</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetArea()">getTargetArea</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a GeoBox that limits the camera target to a specific geographical area.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-core-anglerange" title="class in com.here.sdk.core">AngleRange</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTiltRange()">getTiltRange</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current tilt range.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getZoomRange()">getZoomRange</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently set camera zoom range.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBearingRange(com.here.sdk.core.AngleRange)">setBearingRange</a><wbr/>(<a href="sdk-for-android-explore-core-anglerange" title="class in com.here.sdk.core">AngleRange</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a new bearing range.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBearingRangeAtZoom(com.here.sdk.mapview.MapMeasure,com.here.sdk.core.AngleRange)">setBearingRangeAtZoom</a><wbr/>(<a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 <a href="sdk-for-android-explore-core-anglerange" title="class in com.here.sdk.core">AngleRange</a> bearingRange)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the bearing range within which the camera can rotate at a given zoom.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTargetArea(com.here.sdk.core.GeoBox)">setTargetArea</a><wbr/>(<a href="sdk-for-android-explore-core-geobox" title="class in com.here.sdk.core">GeoBox</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a GeoBox that limits the camera target to a specific geographical area.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTiltRange(com.here.sdk.core.AngleRange)">setTiltRange</a><wbr/>(<a href="sdk-for-android-explore-core-anglerange" title="class in com.here.sdk.core">AngleRange</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a new tilt limit range.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTiltRangeAtZoom(com.here.sdk.mapview.MapMeasure,com.here.sdk.core.AngleRange)">setTiltRangeAtZoom</a><wbr/>(<a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 <a href="sdk-for-android-explore-core-anglerange" title="class in com.here.sdk.core">AngleRange</a> tiltRange)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets tilt ranges that can be set on the camera at given zoom.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setZoomRange(com.here.sdk.mapview.MapMeasureRange)">setZoomRange</a><wbr/>(<a href="sdk-for-android-explore-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a new camera zoom range.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="MIN_TILT">
<h3>MIN_TILT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">double</span> <span class="element-name">MIN_TILT</span></div>
<div class="block"><p>Absolute minimum possible value of tilt angle.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapCameraLimits.MIN_TILT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MAX_TILT">
<h3>MAX_TILT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">double</span> <span class="element-name">MAX_TILT</span></div>
<div class="block"><p>Absolute maximum possible value of tilt angle.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapCameraLimits.MAX_TILT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MIN_ZOOM_LEVEL">
<h3>MIN_ZOOM_LEVEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">double</span> <span class="element-name">MIN_ZOOM_LEVEL</span></div>
<div class="block"><p>Absolute minimum possible value of zoom level.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapCameraLimits.MIN_ZOOM_LEVEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MAX_ZOOM_LEVEL">
<h3>MAX_ZOOM_LEVEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">double</span> <span class="element-name">MAX_ZOOM_LEVEL</span></div>
<div class="block"><p>Absolute maximum possible value of zoom level.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapCameraLimits.MAX_ZOOM_LEVEL">Constant Field Values</a></li>
</ul>
</dd>
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
<section class="detail" id="setBearingRangeAtZoom(com.here.sdk.mapview.MapMeasure,com.here.sdk.core.AngleRange)">
<h3>setBearingRangeAtZoom</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBearingRangeAtZoom</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 @NonNull
 <a href="sdk-for-android-explore-core-anglerange" title="class in com.here.sdk.core">AngleRange</a> bearingRange)</span></div>
<div class="block"><p>Sets the bearing range within which the camera can rotate at a given zoom.
 </p><p>The resulting camera bearing at a zoom is an interpolated value of the ranges set for closest matching zoom values.
 When no bearing range is specified for <a href="#MIN_ZOOM_LEVEL"><code>MIN_ZOOM_LEVEL</code></a>, the bearing range set through
 <a href="#setBearingRange(com.here.sdk.core.AngleRange)"><code>setBearingRange(com.here.sdk.core.AngleRange)</code></a> is used for interpolation.
 </p><p>Zoom values outside the supported zoom range are ignored.
 By default, the maximum bearing range for all zoom values is set during initialization.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>zoom</code> - <p>Zoom at which the range is set.</p></dd>
<dd><code>bearingRange</code> - <p>Bearing range.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearBearingRanges()">
<h3>clearBearingRanges</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearBearingRanges</span>()</div>
<div class="block"><p>Clears bearing ranges for all zoom values and resets
 bearing range to default.</p></div>
</section>
</li>
<li>
<section class="detail" id="setTiltRangeAtZoom(com.here.sdk.mapview.MapMeasure,com.here.sdk.core.AngleRange)">
<h3>setTiltRangeAtZoom</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTiltRangeAtZoom</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 @NonNull
 <a href="sdk-for-android-explore-core-anglerange" title="class in com.here.sdk.core">AngleRange</a> tiltRange)</span></div>
<div class="block"><p>Sets tilt ranges that can be set on the camera at given zoom.
 </p><p>The resulting camera tilt at a zoom is an interpolated value of the ranges set for closest matching zoom values.
 When no tilt range is specified for <a href="#MIN_ZOOM_LEVEL"><code>MIN_ZOOM_LEVEL</code></a>, the tilt range set through <a href="#setTiltRange(com.here.sdk.core.AngleRange)"><code>setTiltRange(com.here.sdk.core.AngleRange)</code></a> is used for interpolation.
 </p><p>Zoom or tilt values outside the supported zoom and tilt range are ignored.
 By default, the maximum tilt range for all zoom values is set during initialization.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>zoom</code> - <p>Zoom at which the range is set.</p></dd>
<dd><code>tiltRange</code> - <p>Tilt range.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearTiltRanges()">
<h3>clearTiltRanges</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearTiltRanges</span>()</div>
<div class="block"><p>Clears tilt ranges for all zoom values and resets  tilt range to default.</p></div>
</section>
</li>
<li>
<section class="detail" id="getTiltRange()">
<h3>getTiltRange</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-core-anglerange" title="class in com.here.sdk.core">AngleRange</a></span> <span class="element-name">getTiltRange</span>()</div>
<div class="block"><p>Gets the current tilt range.
 </p><p>By default, a <a href="#MIN_TILT"><code>MIN_TILT</code></a>-<a href="#MAX_TILT"><code>MAX_TILT</code></a> tilt range is set during initialization.
 </p><p>This range might not be yet active if no rendering loop has been executed since the last call to set the range.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The tilt range that can be applied to the camera.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTiltRange(com.here.sdk.core.AngleRange)">
<h3>setTiltRange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTiltRange</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-anglerange" title="class in com.here.sdk.core">AngleRange</a> value)</span></div>
<div class="block"><p>Sets a new tilt limit range.
 </p><p>The supported values fall inside <a href="#MIN_TILT"><code>MIN_TILT</code></a>-<a href="#MAX_TILT"><code>MAX_TILT</code></a> range.
 Values outside the supported range are ignored.
 </p><p>If the current camera tilt exceeds the new limit range, it will immediately be set to minimum or maximum,
 depending on which is closest.
 </p><p>This new limit range becomes active during the next rendering loop.
 </p><p>All previously set tilt ranges are cleared and the new tilt range is applied for all zoom values.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The tilt range that can be applied to the camera.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBearingRange()">
<h3>getBearingRange</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-core-anglerange" title="class in com.here.sdk.core">AngleRange</a></span> <span class="element-name">getBearingRange</span>()</div>
<div class="block"><p>Gets the currently set bearing range.
 </p><p>This may not be active now if no rendering loop has been executed since
 the last call to set the range.
 </p><p>By default, range for a full circle is set during initialization.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The bearing range within which the camera can be rotated.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBearingRange(com.here.sdk.core.AngleRange)">
<h3>setBearingRange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBearingRange</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-anglerange" title="class in com.here.sdk.core">AngleRange</a> value)</span></div>
<div class="block"><p>Sets a new bearing range.
 </p><p>It will be updated during the next rendering loop.
 All previously set bearing ranges are cleared and the new bearing range is applied for all zoom values.
 </p><p>If the current camera bearing exceeds the limit range, it will immediately be set to minimum or
 maximum, depending on which is closest.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The bearing range within which the camera can be rotated.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getZoomRange()">
<h3>getZoomRange</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a></span> <span class="element-name">getZoomRange</span>()</div>
<div class="block"><p>Gets the currently set camera zoom range.
 </p><p>By default, a <a href="#MIN_ZOOM_LEVEL"><code>MIN_ZOOM_LEVEL</code></a>-<a href="#MAX_ZOOM_LEVEL"><code>MAX_ZOOM_LEVEL</code></a> zoom range is set during initialization.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The zoom range that can be applied to the camera.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setZoomRange(com.here.sdk.mapview.MapMeasureRange)">
<h3>setZoomRange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setZoomRange</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a> value)</span></div>
<div class="block"><p>Sets a new camera zoom range.
 </p><p>The supported values fall inside <a href="#MIN_ZOOM_LEVEL"><code>MIN_ZOOM_LEVEL</code></a>-<a href="#MAX_ZOOM_LEVEL"><code>MAX_ZOOM_LEVEL</code></a> range.
 Values outside the supported zoom range are ignored.
 </p><p>If the current camera zoom exceeds the limit range, it will immediately be set to minimum or maximum, depending on which is closest.
 </p><p>This new limit range becomes active during the next rendering loop.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The zoom range that can be applied to the camera.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetArea()">
<h3>getTargetArea</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">getTargetArea</span>()</div>
<div class="block"><p>Gets a GeoBox that limits the camera target to a specific geographical area. Absence of a value means that there is no limit.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Geographical area to which the camera target is limited.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTargetArea(com.here.sdk.core.GeoBox)">
<h3>setTargetArea</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTargetArea</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-explore-core-geobox" title="class in com.here.sdk.core">GeoBox</a> value)</span></div>
<div class="block"><p>Sets a GeoBox that limits the camera target to a specific geographical area. Set to <code>null</code> to remove the limit.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Geographical area to which the camera target is limited.</p></dd>
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

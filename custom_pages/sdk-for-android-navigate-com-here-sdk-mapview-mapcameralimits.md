---
title: "MapCameraLimits (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapCameraLimits.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapCameraLimits</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapCameraLimits</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Controls constraints on map camera parameters.
 When constraints are set, they are enforced for current camera state
 and for all future changes to the camera.
 When setting, limits are applied on next rendering loop.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static final double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MAX_TILT">MAX_TILT</a></code></div>
<div className="col-last even-row-color">
<div className="block">Absolute maximum possible value of tilt angle.</div>
</div>
<div className="col-first odd-row-color"><code>static final double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MAX_ZOOM_LEVEL">MAX_ZOOM_LEVEL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Absolute maximum possible value of zoom level.</div>
</div>
<div className="col-first even-row-color"><code>static final double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MIN_TILT">MIN_TILT</a></code></div>
<div className="col-last even-row-color">
<div className="block">Absolute minimum possible value of tilt angle.</div>
</div>
<div className="col-first odd-row-color"><code>static final double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MIN_ZOOM_LEVEL">MIN_ZOOM_LEVEL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Absolute minimum possible value of zoom level.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="MIN_TILT">
<h3>MIN_TILT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type">double</span> <span className="element-name">MIN_TILT</span></div>
<div className="block"><p>Absolute minimum possible value of tilt angle.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapCameraLimits.MIN_TILT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="MAX_TILT">
<h3>MAX_TILT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type">double</span> <span className="element-name">MAX_TILT</span></div>
<div className="block"><p>Absolute maximum possible value of tilt angle.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapCameraLimits.MAX_TILT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="MIN_ZOOM_LEVEL">
<h3>MIN_ZOOM_LEVEL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type">double</span> <span className="element-name">MIN_ZOOM_LEVEL</span></div>
<div className="block"><p>Absolute minimum possible value of zoom level.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapCameraLimits.MIN_ZOOM_LEVEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="MAX_ZOOM_LEVEL">
<h3>MAX_ZOOM_LEVEL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type">double</span> <span className="element-name">MAX_ZOOM_LEVEL</span></div>
<div className="block"><p>Absolute maximum possible value of zoom level.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapCameraLimits.MAX_ZOOM_LEVEL">Constant Field Values</a></li>
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="setBearingRangeAtZoom(com.here.sdk.mapview.MapMeasure,com.here.sdk.core.AngleRange)">
<h3>setBearingRangeAtZoom</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setBearingRangeAtZoom</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anglerange" title="class in com.here.sdk.core">AngleRange</a> bearingRange)</span></div>
<div className="block"><p>Sets the bearing range within which the camera can rotate at a given zoom.
 The resulting camera bearing at a zoom is an interpolated value of the ranges set for closest matching zoom values.
 When no bearing range is specified for <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MIN_ZOOM_LEVEL"><code>MIN_ZOOM_LEVEL</code></a>, the bearing range set through
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#setBearingRange(com.here.sdk.core.AngleRange)"><code>setBearingRange(com.here.sdk.core.AngleRange)</code></a> is used for interpolation.
 Zoom values outside the supported zoom range are ignored.
 By default, the maximum bearing range for all zoom values is set during initialization.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>zoom</code> - <p>Zoom at which the range is set.</p></dd>
<dd><code>bearingRange</code> - <p>Bearing range.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="clearBearingRanges()">
<h3>clearBearingRanges</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">clearBearingRanges</span>()</div>
<div className="block"><p>Clears bearing ranges for all zoom values and resets
 bearing range to default.</p></div>
</section>
</li>
<li>
<section className="detail" id="setTiltRangeAtZoom(com.here.sdk.mapview.MapMeasure,com.here.sdk.core.AngleRange)">
<h3>setTiltRangeAtZoom</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTiltRangeAtZoom</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anglerange" title="class in com.here.sdk.core">AngleRange</a> tiltRange)</span></div>
<div className="block"><p>Sets tilt ranges that can be set on the camera at given zoom.
 The resulting camera tilt at a zoom is an interpolated value of the ranges set for closest matching zoom values.
 When no tilt range is specified for <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MIN_ZOOM_LEVEL"><code>MIN_ZOOM_LEVEL</code></a>, the tilt range set through <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#setTiltRange(com.here.sdk.core.AngleRange)"><code>setTiltRange(com.here.sdk.core.AngleRange)</code></a> is used for interpolation.
 Zoom or tilt values outside the supported zoom and tilt range are ignored.
 By default, the maximum tilt range for all zoom values is set during initialization.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>zoom</code> - <p>Zoom at which the range is set.</p></dd>
<dd><code>tiltRange</code> - <p>Tilt range.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="clearTiltRanges()">
<h3>clearTiltRanges</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">clearTiltRanges</span>()</div>
<div className="block"><p>Clears tilt ranges for all zoom values and resets  tilt range to default.</p></div>
</section>
</li>
<li>
<section className="detail" id="getTiltRange()">
<h3>getTiltRange</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-anglerange" title="class in com.here.sdk.core">AngleRange</a></span> <span className="element-name">getTiltRange</span>()</div>
<div className="block"><p>Gets the current tilt range.
 By default, a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MIN_TILT"><code>MIN_TILT</code></a>-<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MAX_TILT"><code>MAX_TILT</code></a> tilt range is set during initialization.
 This range might not be yet active if no rendering loop has been executed since the last call to set the range.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The tilt range that can be applied to the camera.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTiltRange(com.here.sdk.core.AngleRange)">
<h3>setTiltRange</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTiltRange</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anglerange" title="class in com.here.sdk.core">AngleRange</a> value)</span></div>
<div className="block"><p>Sets a new tilt limit range.
 The supported values fall inside <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MIN_TILT"><code>MIN_TILT</code></a>-<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MAX_TILT"><code>MAX_TILT</code></a> range.
 Values outside the supported range are ignored.
 If the current camera tilt exceeds the new limit range, it will immediately be set to minimum or maximum,
 depending on which is closest.
 This new limit range becomes active during the next rendering loop.
 All previously set tilt ranges are cleared and the new tilt range is applied for all zoom values.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The tilt range that can be applied to the camera.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBearingRange()">
<h3>getBearingRange</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-anglerange" title="class in com.here.sdk.core">AngleRange</a></span> <span className="element-name">getBearingRange</span>()</div>
<div className="block"><p>Gets the currently set bearing range.
 This may not be active now if no rendering loop has been executed since
 the last call to set the range.
 By default, range for a full circle is set during initialization.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The bearing range within which the camera can be rotated.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setBearingRange(com.here.sdk.core.AngleRange)">
<h3>setBearingRange</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setBearingRange</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anglerange" title="class in com.here.sdk.core">AngleRange</a> value)</span></div>
<div className="block"><p>Sets a new bearing range.
 It will be updated during the next rendering loop.
 All previously set bearing ranges are cleared and the new bearing range is applied for all zoom values.
 If the current camera bearing exceeds the limit range, it will immediately be set to minimum or
 maximum, depending on which is closest.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The bearing range within which the camera can be rotated.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getZoomRange()">
<h3>getZoomRange</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a></span> <span className="element-name">getZoomRange</span>()</div>
<div className="block"><p>Gets the currently set camera zoom range.
 By default, a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MIN_ZOOM_LEVEL"><code>MIN_ZOOM_LEVEL</code></a>-<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MAX_ZOOM_LEVEL"><code>MAX_ZOOM_LEVEL</code></a> zoom range is set during initialization.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The zoom range that can be applied to the camera.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setZoomRange(com.here.sdk.mapview.MapMeasureRange)">
<h3>setZoomRange</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setZoomRange</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a> value)</span></div>
<div className="block"><p>Sets a new camera zoom range.
 The supported values fall inside <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MIN_ZOOM_LEVEL"><code>MIN_ZOOM_LEVEL</code></a>-<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameralimits#MAX_ZOOM_LEVEL"><code>MAX_ZOOM_LEVEL</code></a> range.
 Values outside the supported zoom range are ignored.
 If the current camera zoom exceeds the limit range, it will immediately be set to minimum or maximum, depending on which is closest.
 This new limit range becomes active during the next rendering loop.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The zoom range that can be applied to the camera.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTargetArea()">
<h3>getTargetArea</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">getTargetArea</span>()</div>
<div className="block"><p>Gets a GeoBox that limits the camera target to a specific geographical area. Absence of a value means that there is no limit.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Geographical area to which the camera target is limited.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTargetArea(com.here.sdk.core.GeoBox)">
<h3>setTargetArea</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTargetArea</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> value)</span></div>
<div className="block"><p>Sets a GeoBox that limits the camera target to a specific geographical area. Set to <code>null</code> to remove the limit.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>

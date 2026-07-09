---
title: "AreaCameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-areacamerabehavior"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- AreaCameraBehavior.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.navigation.AreaCameraBehavior</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">AreaCameraBehavior</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></span></div>
<div className="block"><p>Use this class to show an overview of geo points. By default, the orientation of the camera will be
 perpendicular to the Earth's surface (ie. looking towards the center of the Earth),
 while bearing will be towards north.
 Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are
 subject to change without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-areacamerabehavior#%3Cinit%3E()">AreaCameraBehavior</a>()</code></div>
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
<h3>AreaCameraBehavior</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">AreaCameraBehavior</span>()</div>
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
<section className="detail" id="setVisiblePoints(java.util.List)">
<h3>setVisiblePoints</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setVisiblePoints</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; visiblePoints)</span></div>
<div className="block"><p>Sets the list of geo points to show in the camera view.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>visiblePoints</code> - <p>The list of geo points to visualize. The list can be empty.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVisiblePoints()">
<h3>getVisiblePoints</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;</span> <span className="element-name">getVisiblePoints</span>()</div>
<div className="block"><p>Gets configured visible geo points.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of geo points to show in the camera view. The list can be empty.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getViewRectangle()">
<h3>getViewRectangle</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a></span> <span className="element-name">getViewRectangle</span>()</div>
<div className="block"><p>Gets the current view rectangle, if it's set.
 Defines a sub-space of the screen that the behavior should consider
 for camera updates.
 Defaults to <code>null</code>. If not set, it uses the viewport bounds of the underlying map view.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The view rectangle for camera updates.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setViewRectangle(com.here.sdk.core.Rectangle2D)">
<h3>setViewRectangle</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setViewRectangle</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> value)</span></div>
<div className="block"><p>Sets view rectangle.
 Defines a sub-space of the screen that the behavior should consider
 for camera updates.
 Defaults to <code>null</code>. If not set, it uses the viewport bounds of the underlying map view.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The view rectangle for camera updates.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCameraAnimationDuration()">
<h3>getCameraAnimationDuration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">getCameraAnimationDuration</span>()</div>
<div className="block"><p>Gets the current animation duration in milliseconds.
 If there is an animation, it will last for specified period of time.
 Defaults to 500 milliseconds, or half a second.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The duration of camera animation in milliseconds.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCameraAnimationDuration(com.here.time.Duration)">
<h3>setCameraAnimationDuration</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCameraAnimationDuration</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> value)</span></div>
<div className="block"><p>Sets the current animation duration in milliseconds.
 If there is an animation, it will last for specified period of time.
 Defaults to 500 milliseconds, or half a second.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The duration of camera animation in milliseconds.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPrincipalPointAnimationDuration()">
<h3>getPrincipalPointAnimationDuration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">getPrincipalPointAnimationDuration</span>()</div>
<div className="block"><p>Gets the current principal point animation duration in milliseconds.
 If the principal point is changed, the change will be animated
 over this duration.
 Defaults to 500 milliseconds, or half a second.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The duration of principal point animation in milliseconds.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setPrincipalPointAnimationDuration(com.here.time.Duration)">
<h3>setPrincipalPointAnimationDuration</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setPrincipalPointAnimationDuration</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> value)</span></div>
<div className="block"><p>Sets the current principal point animation in milliseconds.
 If the principal point is changed, the change will be animated
 over this duration.
 Defaults to 500 milliseconds, or half a second.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The duration of principal point animation in milliseconds.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getMaxZoom()">
<h3>getMaxZoom</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a></span> <span className="element-name">getMaxZoom</span>()</div>
<div className="block"><p>Gets maximal allowed zoom.
 Defines maximal zoom level to be applied to enclose geodetic bounding box.
 Defaults to a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> with kind <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> and value 20.0.
 Note: <a href="sdk-for-android-navigate-mapmeasure-kind#SCALE"><code>MapMeasure.Kind.SCALE</code></a> is not supported.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Maximal allowed zoom.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setMaxZoom(com.here.sdk.mapview.MapMeasure)">
<h3>setMaxZoom</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setMaxZoom</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> value)</span></div>
<div className="block"><p>Sets maximal allowed zoom.
 Defines maximal zoom level to be applied to enclose geodetic bounding box.
 Defaults to a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> with kind <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> and value 20.0.
 Note: <a href="sdk-for-android-navigate-mapmeasure-kind#SCALE"><code>MapMeasure.Kind.SCALE</code></a> is not supported.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Maximal allowed zoom.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCameraBearingInDegrees()">
<h3>getCameraBearingInDegrees</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getCameraBearingInDegrees</span>()</div>
<div className="block"><p>Gets the current camera bearing.
 The direction in which the camera will point in degrees clockwise, relative to
 true North. The input should range between [0, 360]. Defaults to true North (0 degrees).</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Camera bearing in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCameraBearingInDegrees(double)">
<h3>setCameraBearingInDegrees</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCameraBearingInDegrees</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets camera bearing.
 The direction in which the camera will point in degrees clockwise, relative to
 true North. The input should range between [0, 360]. Defaults to true North (0 degrees).</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Camera bearing in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCameraTiltInDegrees()">
<h3>getCameraTiltInDegrees</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getCameraTiltInDegrees</span>()</div>
<div className="block"><p>Gets the current camera tilt.
 The tilt of the camera relative to the axis perpendicular to the ground. Defaults to
 0 degrees, meaning that it will look straight down into the ground.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Camera tilt in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCameraTiltInDegrees(double)">
<h3>setCameraTiltInDegrees</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCameraTiltInDegrees</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets camera tilt.
 The tilt of the camera relative to the axis perpendicular to the ground. Defaults to
 0 degrees, meaning that it will look straight down into the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Camera tilt in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isCurrentPositionIncluded()">
<h3>isCurrentPositionIncluded</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isCurrentPositionIncluded</span>()</div>
<div className="block"><p>Gets whether to include the current position.
 Decides if the current position should be added to the set of visible points.
 Note that if the current position is in the vicinity of any of the visible points, setting this to
 <code>false</code> will not explicitly exclude the current position from the camera view. However if displaying
 an area potentially away from the current position, this does need to be explicitly set to <code>false</code>
 or it will try to include the current position. Defaults to false.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Include current position in camera view.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCurrentPositionIncluded(boolean)">
<h3>setCurrentPositionIncluded</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCurrentPositionIncluded</span><wbr/><span className="parameters">(boolean value)</span></div>
<div className="block"><p>Sets whether to include the current position.
 Decides if the current position should be added to the set of visible points.
 Note that if the current position is in the vicinity of any of the visible points, setting this to
 <code>false</code> will not explicitly exclude the current position from the camera view. However if displaying
 an area potentially away from the current position, this does need to be explicitly set to <code>false</code>
 or it will try to include the current position. Defaults to false.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Include current position in camera view.</p></dd>
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

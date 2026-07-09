---
title: "TrackingCameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrackingCameraBehavior.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.navigation.TrackingCameraBehavior</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TrackingCameraBehavior</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-navigation-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></span></div>
<div className="block"><p>Use this class to follow a moving target. The camera smoothly tracks the target’s
 position while adjusting heading, tilt, and zoom as needed. When tracking starts
 or resumes, the camera first animates a re-centering transition to align with the target.
 Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are
 subject to change without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</a></code></div>
<div className="col-last even-row-color">
<div className="block">Configuration for mapping functional road classes to zoom levels.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Configuration that defines how <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior</code></a> reacts to nearby maneuvers.</div>
</div>
<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverrule" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverRule</a></code></div>
<div className="col-last even-row-color">
<div className="block">Defines a single rule that determines how <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior</code></a> reacts to nearby
 maneuvers when the current position matches this rule.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverRuleOptions</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Defines a set of configurations specific to a <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverrule" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverRule</code></a>.</div>
</div>
<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverzoomrange" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverZoomRange</a></code></div>
<div className="col-last even-row-color">
<div className="block">Defines the bounds within which the zoom level is constrained when approaching a maneuver.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Configuration for computing zoom levels from speed thresholds defined per road classification.</div>
</div>
<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedthreshold" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedThreshold</a></code></div>
<div className="col-last even-row-color">
<div className="block">Defines a zoom level triggered when the vehicle reaches a specific speed.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Defines zoom behavior in different policy settings.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior#%3Cinit%3E()">TrackingCameraBehavior</a>()</code></div>
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
<h3>TrackingCameraBehavior</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TrackingCameraBehavior</span>()</div>
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
<section className="detail" id="flagFixedDurationForNextAnimation()">
<h3>flagFixedDurationForNextAnimation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">flagFixedDurationForNextAnimation</span>()</div>
<div className="block"><p>Enables fixed-duration animation mode for the next property change.
 When called, the next setter call (e.g., tilt_in_degrees or bearing_in_degrees)
 will animate using a fast fixed-duration animation instead of the default
 speed-based animation. The flag is automatically reset after the next setter is called.</p></div>
</section>
</li>
<li>
<section className="detail" id="setManeuverModeConfiguration(com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration)">
<h3>setManeuverModeConfiguration</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setManeuverModeConfiguration</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a> maneuverModeConfiguration)</span></div>
<div className="block"><p>Sets the configuration for camera behavior near maneuvers.
 Defines how the camera reacts to nearby maneuvers when
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior#isManeuverDetectionEnabled()"><code>isManeuverDetectionEnabled()</code></a> is <code>true</code>. When set to <code>null</code>, the camera does
 not react to maneuvers. The configuration must contain at least one rule to be valid.
 Defaults to <code>null</code>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>maneuverModeConfiguration</code> - <p>The maneuver mode configuration. Invalid configurations are rejected.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getManeuverModeConfiguration()">
<h3>getManeuverModeConfiguration</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a></span> <span className="element-name">getManeuverModeConfiguration</span>()</div>
<div className="block"><p>Gets the current maneuver mode configuration, or <code>null</code> if not set.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The current maneuver mode configuration.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="defaultFunctionalRoadClassZoomPolicyOptions()">
<h3>defaultFunctionalRoadClassZoomPolicyOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</a></span> <span className="element-name">defaultFunctionalRoadClassZoomPolicyOptions</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The default <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="defaultSpeedBasedZoomPolicyOptions()">
<h3>defaultSpeedBasedZoomPolicyOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</a></span> <span className="element-name">defaultSpeedBasedZoomPolicyOptions</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The default <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="defaultManeuverModeConfiguration()">
<h3>defaultManeuverModeConfiguration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a></span> <span className="element-name">defaultManeuverModeConfiguration</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The default <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverModeConfiguration</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRecenterAnimationDuration()">
<h3>getRecenterAnimationDuration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">getRecenterAnimationDuration</span>()</div>
<div className="block"><p>Gets the recenter animation duration in milliseconds.
 Time to recenter the camera reaching current car position.
 Defaults to 500 milliseconds, or half a second.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The duration of recenter animation in milliseconds.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRecenterAnimationDuration(com.here.time.Duration)">
<h3>setRecenterAnimationDuration</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRecenterAnimationDuration</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> value)</span></div>
<div className="block"><p>Sets the recenter animation duration in milliseconds.
 Time to recenter the camera reaching current car position.
 Defaults to 500 milliseconds, or half a second.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The duration of recenter animation in milliseconds.</p></dd>
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
<div className="block"><p>Sets a view rectangle.
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
<section className="detail" id="getTiltInDegrees()">
<h3>getTiltInDegrees</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getTiltInDegrees</span>()</div>
<div className="block"><p>Gets the camera tilt in degrees.
 Camera tilt angle relative to the ground plane, in degrees.
 Defaults to 50.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The value of camera tilt in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTiltInDegrees(double)">
<h3>setTiltInDegrees</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTiltInDegrees</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets the camera tilt in degrees.
 Camera tilt angle relative to the ground plane, in degrees.
 Defaults to 50.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The value of camera tilt in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBearingInDegrees()">
<h3>getBearingInDegrees</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getBearingInDegrees</span>()</div>
<div className="block"><p>Gets the bearing in degrees.
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
<dd><p>The camera bearing in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setBearingInDegrees(java.lang.Double)">
<h3>setBearingInDegrees</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setBearingInDegrees</span><wbr/><span className="parameters">(@Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value)</span></div>
<div className="block"><p>Sets the bearing in degrees.
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
<dd><code>value</code> - <p>The camera bearing in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getMaxRotationSpeedInDegreesPerSecond()">
<h3>getMaxRotationSpeedInDegreesPerSecond</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getMaxRotationSpeedInDegreesPerSecond</span>()</div>
<div className="block"><p>Gets the maximum rotation speed.
 Maximum bearing rotation speed in degrees per second,
 limiting how fast the camera turns.
 Defaults to 20 degrees per second.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The maximum rotation speed.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setMaxRotationSpeedInDegreesPerSecond(double)">
<h3>setMaxRotationSpeedInDegreesPerSecond</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setMaxRotationSpeedInDegreesPerSecond</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets the maximum rotation speed.
 Maximum bearing rotation speed in degrees per second,
 limiting how fast the camera turns.
 Defaults to 20 degrees per second.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The maximum rotation speed.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getZoomSpeedInLevelsPerSecond()">
<h3>getZoomSpeedInLevelsPerSecond</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getZoomSpeedInLevelsPerSecond</span>()</div>
<div className="block"><p>Gets the zoom level transition speed.
 Speed factor controlling how quickly the camera
 transitions between zoom levels
 Defaults to 0.5 zoom levels per second.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The zoom level transition speed.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setZoomSpeedInLevelsPerSecond(double)">
<h3>setZoomSpeedInLevelsPerSecond</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setZoomSpeedInLevelsPerSecond</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets the zoom level transition speed.
 Speed factor controlling how quickly the camera
 transitions between zoom levels
 Defaults to 0.5 zoom levels per second.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The zoom level transition speed.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getZoomPolicy()">
<h3>getZoomPolicy</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></span> <span className="element-name">getZoomPolicy</span>()</div>
<div className="block"><p>Gets the current zoom computation strategy.
 Defines the strategy used to compute the zoom level based on scene heuristics.
 Defaults to a fixed zoom policy at zoom level 16.5.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The strategy of computing the zoom level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setZoomPolicy(com.here.sdk.navigation.TrackingCameraBehavior.ZoomPolicy)">
<h3>setZoomPolicy</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setZoomPolicy</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a> value)</span></div>
<div className="block"><p>Sets the current zoom computation strategy.
 Defines the strategy used to compute the zoom level based on scene heuristics.
 Defaults to a fixed zoom policy at zoom level 16.5.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The strategy of computing the zoom level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isManeuverDetectionEnabled()">
<h3>isManeuverDetectionEnabled</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isManeuverDetectionEnabled</span>()</div>
<div className="block"><p>Gets whether maneuver detection is enabled.
 When <code>true</code>, the camera detects adjacent maneuvers and reacts according to
 the <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverModeConfiguration</code></a> set via <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior#setManeuverModeConfiguration(com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration)"><code>setManeuverModeConfiguration(com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration)</code></a>.
 A valid <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverModeConfiguration</code></a> must be set for the camera to react. Defaults to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Whether maneuver detection is enabled.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setManeuverDetectionEnabled(boolean)">
<h3>setManeuverDetectionEnabled</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setManeuverDetectionEnabled</span><wbr/><span className="parameters">(boolean value)</span></div>
<div className="block"><p>Sets whether maneuver detection is enabled.
 When <code>true</code>, the camera detects adjacent maneuvers and reacts according to
 the <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverModeConfiguration</code></a> set via <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior#setManeuverModeConfiguration(com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration)"><code>setManeuverModeConfiguration(com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration)</code></a>.
 A valid <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverModeConfiguration</code></a> must be set for the camera to react. Defaults to <code>false</code>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Whether maneuver detection is enabled.</p></dd>
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

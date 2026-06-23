---
title: "TrackingCameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrackingCameraBehavior.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.navigation.TrackingCameraBehavior</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">TrackingCameraBehavior</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></span></div>
<div class="block"><p>Use this class to follow a moving target. The camera smoothly tracks the target’s
 position while adjusting heading, tilt, and zoom as needed. When tracking starts
 or resumes, the camera first animates a re-centering transition to align with the target.
 </p><p>Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are
 subject to change without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-trackingcamerabehavior.functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">Configuration for mapping functional road classes to zoom levels.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-trackingcamerabehavior.maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Configuration that defines how <a href="sdk-for-android-navigate-trackingcamerabehavior" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior</code></a> reacts to nearby maneuvers.</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-trackingcamerabehavior.maneuverrule" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverRule</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines a single rule that determines how <a href="sdk-for-android-navigate-trackingcamerabehavior" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior</code></a> reacts to nearby
 maneuvers when the current position matches this rule.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-trackingcamerabehavior.maneuverruleoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverRuleOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Defines a set of configurations specific to a <a href="sdk-for-android-navigate-trackingcamerabehavior.maneuverrule" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverRule</code></a>.</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-trackingcamerabehavior.maneuverzoomrange" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverZoomRange</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines the bounds within which the zoom level is constrained when approaching a maneuver.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-trackingcamerabehavior.speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Configuration for computing zoom levels from speed thresholds defined per road classification.</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-trackingcamerabehavior.speedthreshold" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedThreshold</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines a zoom level triggered when the vehicle reaches a specific speed.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-trackingcamerabehavior.zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Defines zoom behavior in different policy settings.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E()">TrackingCameraBehavior</a>()</code></div>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-trackingcamerabehavior.functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#defaultFunctionalRoadClassZoomPolicyOptions()">defaultFunctionalRoadClassZoomPolicyOptions</a>()</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-trackingcamerabehavior.maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#defaultManeuverModeConfiguration()">defaultManeuverModeConfiguration</a>()</code></div>

<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-trackingcamerabehavior.speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#defaultSpeedBasedZoomPolicyOptions()">defaultSpeedBasedZoomPolicyOptions</a>()</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#flagFixedDurationForNextAnimation()">flagFixedDurationForNextAnimation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Enables fixed-duration animation mode for the next property change.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getBearingInDegrees()">getBearingInDegrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the bearing in degrees.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-trackingcamerabehavior.maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getManeuverModeConfiguration()">getManeuverModeConfiguration</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current maneuver mode configuration, or <code>null</code> if not set.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getMaxRotationSpeedInDegreesPerSecond()">getMaxRotationSpeedInDegreesPerSecond</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the maximum rotation speed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getNormalizedPrincipalPoint()">getNormalizedPrincipalPoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently set normalized principal point to be used during navigation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getPrincipalPointAnimationDuration()">getPrincipalPointAnimationDuration</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current principal point animation duration in milliseconds.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRecenterAnimationDuration()">getRecenterAnimationDuration</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the recenter animation duration in milliseconds.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTiltInDegrees()">getTiltInDegrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the camera tilt in degrees.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getViewRectangle()">getViewRectangle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current view rectangle, if it's set.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-trackingcamerabehavior.zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getZoomPolicy()">getZoomPolicy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current zoom computation strategy.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getZoomSpeedInLevelsPerSecond()">getZoomSpeedInLevelsPerSecond</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the zoom level transition speed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isManeuverDetectionEnabled()">isManeuverDetectionEnabled</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets whether maneuver detection is enabled.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setBearingInDegrees(java.lang.Double)">setBearingInDegrees</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the bearing in degrees.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setManeuverDetectionEnabled(boolean)">setManeuverDetectionEnabled</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether maneuver detection is enabled.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setManeuverModeConfiguration(com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration)">setManeuverModeConfiguration</a><wbr/>(<a href="sdk-for-android-navigate-trackingcamerabehavior.maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a> maneuverModeConfiguration)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the configuration for camera behavior near maneuvers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setMaxRotationSpeedInDegreesPerSecond(double)">setMaxRotationSpeedInDegreesPerSecond</a><wbr/>(double value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the maximum rotation speed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">setNormalizedPrincipalPoint</a><wbr/>(<a href="sdk-for-android-navigate-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a normalized principal point to be used during navigation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setPrincipalPointAnimationDuration(com.here.time.Duration)">setPrincipalPointAnimationDuration</a><wbr/>(<a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the current principal point animation in milliseconds.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRecenterAnimationDuration(com.here.time.Duration)">setRecenterAnimationDuration</a><wbr/>(<a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the recenter animation duration in milliseconds.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setTiltInDegrees(double)">setTiltInDegrees</a><wbr/>(double value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the camera tilt in degrees.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setViewRectangle(com.here.sdk.core.Rectangle2D)">setViewRectangle</a><wbr/>(<a href="sdk-for-android-navigate-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a view rectangle.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setZoomPolicy(com.here.sdk.navigation.TrackingCameraBehavior.ZoomPolicy)">setZoomPolicy</a><wbr/>(<a href="sdk-for-android-navigate-trackingcamerabehavior.zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the current zoom computation strategy.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setZoomSpeedInLevelsPerSecond(double)">setZoomSpeedInLevelsPerSecond</a><wbr/>(double value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the zoom level transition speed.</div>
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
<h3>TrackingCameraBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TrackingCameraBehavior</span>()</div>
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
<section class="detail" id="flagFixedDurationForNextAnimation()">
<h3>flagFixedDurationForNextAnimation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">flagFixedDurationForNextAnimation</span>()</div>
<div class="block"><p>Enables fixed-duration animation mode for the next property change.
 When called, the next setter call (e.g., tilt_in_degrees or bearing_in_degrees)
 will animate using a fast fixed-duration animation instead of the default
 speed-based animation. The flag is automatically reset after the next setter is called.</p></div>
</section>
</li>
<li>
<section class="detail" id="setManeuverModeConfiguration(com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration)">
<h3>setManeuverModeConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverModeConfiguration</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-trackingcamerabehavior.maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a> maneuverModeConfiguration)</span></div>
<div class="block"><p>Sets the configuration for camera behavior near maneuvers.
 Defines how the camera reacts to nearby maneuvers when
 <a href="sdk-for-android-navigate-index#isManeuverDetectionEnabled()"><code>isManeuverDetectionEnabled()</code></a> is <code>true</code>. When set to <code>null</code>, the camera does
 not react to maneuvers. The configuration must contain at least one rule to be valid.
 Defaults to <code>null</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>maneuverModeConfiguration</code> - <p>The maneuver mode configuration. Invalid configurations are rejected.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManeuverModeConfiguration()">
<h3>getManeuverModeConfiguration</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trackingcamerabehavior.maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a></span> <span class="element-name">getManeuverModeConfiguration</span>()</div>
<div class="block"><p>Gets the current maneuver mode configuration, or <code>null</code> if not set.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The current maneuver mode configuration.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="defaultFunctionalRoadClassZoomPolicyOptions()">
<h3>defaultFunctionalRoadClassZoomPolicyOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-trackingcamerabehavior.functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</a></span> <span class="element-name">defaultFunctionalRoadClassZoomPolicyOptions</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The default <a href="sdk-for-android-navigate-trackingcamerabehavior.functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="defaultSpeedBasedZoomPolicyOptions()">
<h3>defaultSpeedBasedZoomPolicyOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-trackingcamerabehavior.speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</a></span> <span class="element-name">defaultSpeedBasedZoomPolicyOptions</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The default <a href="sdk-for-android-navigate-trackingcamerabehavior.speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="defaultManeuverModeConfiguration()">
<h3>defaultManeuverModeConfiguration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-trackingcamerabehavior.maneuvermodeconfiguration" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverModeConfiguration</a></span> <span class="element-name">defaultManeuverModeConfiguration</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The default <a href="sdk-for-android-navigate-trackingcamerabehavior.maneuvermodeconfiguration" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverModeConfiguration</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRecenterAnimationDuration()">
<h3>getRecenterAnimationDuration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getRecenterAnimationDuration</span>()</div>
<div class="block"><p>Gets the recenter animation duration in milliseconds.
 </p><p>Time to recenter the camera reaching current car position.
 Defaults to 500 milliseconds, or half a second.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The duration of recenter animation in milliseconds.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRecenterAnimationDuration(com.here.time.Duration)">
<h3>setRecenterAnimationDuration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRecenterAnimationDuration</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> value)</span></div>
<div class="block"><p>Sets the recenter animation duration in milliseconds.
 </p><p>Time to recenter the camera reaching current car position.
 Defaults to 500 milliseconds, or half a second.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The duration of recenter animation in milliseconds.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getViewRectangle()">
<h3>getViewRectangle</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a></span> <span class="element-name">getViewRectangle</span>()</div>
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
 <a href="sdk-for-android-navigate-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> value)</span></div>
<div class="block"><p>Sets a view rectangle.
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
<section class="detail" id="getPrincipalPointAnimationDuration()">
<h3>getPrincipalPointAnimationDuration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getPrincipalPointAnimationDuration</span>()</div>
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
 <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> value)</span></div>
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
<section class="detail" id="getTiltInDegrees()">
<h3>getTiltInDegrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getTiltInDegrees</span>()</div>
<div class="block"><p>Gets the camera tilt in degrees.
 </p><p>Camera tilt angle relative to the ground plane, in degrees.
 Defaults to 50.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The value of camera tilt in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTiltInDegrees(double)">
<h3>setTiltInDegrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTiltInDegrees</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets the camera tilt in degrees.
 </p><p>Camera tilt angle relative to the ground plane, in degrees.
 Defaults to 50.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The value of camera tilt in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBearingInDegrees()">
<h3>getBearingInDegrees</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getBearingInDegrees</span>()</div>
<div class="block"><p>Gets the bearing in degrees.
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
<dd><p>The camera bearing in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBearingInDegrees(java.lang.Double)">
<h3>setBearingInDegrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBearingInDegrees</span><wbr/><span class="parameters">(@Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> value)</span></div>
<div class="block"><p>Sets the bearing in degrees.
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
<dd><code>value</code> - <p>The camera bearing in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMaxRotationSpeedInDegreesPerSecond()">
<h3>getMaxRotationSpeedInDegreesPerSecond</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getMaxRotationSpeedInDegreesPerSecond</span>()</div>
<div class="block"><p>Gets the maximum rotation speed.
 </p><p>Maximum bearing rotation speed in degrees per second,
 limiting how fast the camera turns.
 Defaults to 20 degrees per second.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The maximum rotation speed.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMaxRotationSpeedInDegreesPerSecond(double)">
<h3>setMaxRotationSpeedInDegreesPerSecond</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMaxRotationSpeedInDegreesPerSecond</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets the maximum rotation speed.
 </p><p>Maximum bearing rotation speed in degrees per second,
 limiting how fast the camera turns.
 Defaults to 20 degrees per second.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The maximum rotation speed.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getZoomSpeedInLevelsPerSecond()">
<h3>getZoomSpeedInLevelsPerSecond</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getZoomSpeedInLevelsPerSecond</span>()</div>
<div class="block"><p>Gets the zoom level transition speed.
 </p><p>Speed factor controlling how quickly the camera
 transitions between zoom levels
 Defaults to 0.5 zoom levels per second.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The zoom level transition speed.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setZoomSpeedInLevelsPerSecond(double)">
<h3>setZoomSpeedInLevelsPerSecond</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setZoomSpeedInLevelsPerSecond</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets the zoom level transition speed.
 </p><p>Speed factor controlling how quickly the camera
 transitions between zoom levels
 Defaults to 0.5 zoom levels per second.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The zoom level transition speed.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getZoomPolicy()">
<h3>getZoomPolicy</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trackingcamerabehavior.zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></span> <span class="element-name">getZoomPolicy</span>()</div>
<div class="block"><p>Gets the current zoom computation strategy.
 </p><p>Defines the strategy used to compute the zoom level based on scene heuristics.
 Defaults to a fixed zoom policy at zoom level 16.5.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The strategy of computing the zoom level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setZoomPolicy(com.here.sdk.navigation.TrackingCameraBehavior.ZoomPolicy)">
<h3>setZoomPolicy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setZoomPolicy</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-trackingcamerabehavior.zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a> value)</span></div>
<div class="block"><p>Sets the current zoom computation strategy.
 </p><p>Defines the strategy used to compute the zoom level based on scene heuristics.
 Defaults to a fixed zoom policy at zoom level 16.5.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The strategy of computing the zoom level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isManeuverDetectionEnabled()">
<h3>isManeuverDetectionEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isManeuverDetectionEnabled</span>()</div>
<div class="block"><p>Gets whether maneuver detection is enabled.
 </p><p>When <code>true</code>, the camera detects adjacent maneuvers and reacts according to
 the <a href="sdk-for-android-navigate-trackingcamerabehavior.maneuvermodeconfiguration" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverModeConfiguration</code></a> set via <a href="sdk-for-android-navigate-index#setManeuverModeConfiguration(com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration)"><code>setManeuverModeConfiguration(com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration)</code></a>.
 A valid <a href="sdk-for-android-navigate-trackingcamerabehavior.maneuvermodeconfiguration" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverModeConfiguration</code></a> must be set for the camera to react. Defaults to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Whether maneuver detection is enabled.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setManeuverDetectionEnabled(boolean)">
<h3>setManeuverDetectionEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverDetectionEnabled</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether maneuver detection is enabled.
 </p><p>When <code>true</code>, the camera detects adjacent maneuvers and reacts according to
 the <a href="sdk-for-android-navigate-trackingcamerabehavior.maneuvermodeconfiguration" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverModeConfiguration</code></a> set via <a href="sdk-for-android-navigate-index#setManeuverModeConfiguration(com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration)"><code>setManeuverModeConfiguration(com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration)</code></a>.
 A valid <a href="sdk-for-android-navigate-trackingcamerabehavior.maneuvermodeconfiguration" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverModeConfiguration</code></a> must be set for the camera to react. Defaults to <code>false</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Whether maneuver detection is enabled.</p></dd>
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

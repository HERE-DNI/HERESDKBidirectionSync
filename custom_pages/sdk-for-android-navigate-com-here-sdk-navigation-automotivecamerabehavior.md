---
title: "AutomotiveCameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-automotivecamerabehavior"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- AutomotiveCameraBehavior.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.navigation.AutomotiveCameraBehavior</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">AutomotiveCameraBehavior</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-camerabehavior" title="interface in com.here.sdk.navigation">CameraBehavior</a></span></div>
<div class="block"><p>Provides a high-level camera controller for automotive navigation that manages both tracking
 and area camera behaviors. This class acts as a facade, delegating camera operations to either
 a <a href="sdk-for-android-navigate-trackingcamerabehavior" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior</code></a> for following the vehicle during navigation or an <a href="sdk-for-android-navigate-areacamerabehavior" title="class in com.here.sdk.navigation"><code>AreaCameraBehavior</code></a>
 for showing overview areas such as points of interest or route previews.
 </p><p>The controller supports three states: tracking mode (following the vehicle), area mode (showing
 geographic regions), or inactive (no automatic camera control). The inactive state allows
 external control of the camera, such as when responding to user touch events or when UI logic
 temporarily disables automatic camera behavior.
 </p><p>Camera configuration, including animation durations, zoom policies, and maneuver handling
 settings, can be provided through a JSON configuration string or file. The configuration is
 validated and parsed during construction.
 </p><p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.ActiveCameraType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines the type of camera currently handling camera updates.</div>
</div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-automotivecamerabehavior.orientationmode" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.OrientationMode</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Defines the visual presentation modes for the camera orientation.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E()">AutomotiveCameraBehavior</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class with default camera behaviors and configuration.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(java.lang.String)">AutomotiveCameraBehavior</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> configJson)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of this class configured from a JSON string.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.ActiveCameraType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getActiveCameraType()">getActiveCameraType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the type of camera currently handling camera updates.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getNormalizedPrincipalPoint()">getNormalizedPrincipalPoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the currently set normalized principal point to be used during navigation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-automotivecamerabehavior.orientationmode" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.OrientationMode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getOrientationMode()">getOrientationMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current orientation mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getViewRectangle()">getViewRectangle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current view rectangle, if it's set.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isManeuverDetectionEnabled()">isManeuverDetectionEnabled</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets whether maneuver-based camera adjustments are enabled.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setActiveCameraType(com.here.sdk.navigation.AutomotiveCameraBehavior.ActiveCameraType)">setActiveCameraType</a><wbr/>(<a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.ActiveCameraType</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the type of camera currently handling camera updates.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setAreaCameraBehaviorGeobox(com.here.sdk.core.GeoBox)">setAreaCameraBehaviorGeobox</a><wbr/>(<a href="sdk-for-android-navigate-geobox" title="class in com.here.sdk.core">GeoBox</a> geobox)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures the Area camera to frame the specified geographic bounding box.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setAreaCameraBehaviorVisiblePoints(java.util.List,boolean)">setAreaCameraBehaviorVisiblePoints</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; points,
 boolean includeCurrentPosition)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures the Area camera to frame the specified points.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setManeuverDetectionEnabled(boolean)">setManeuverDetectionEnabled</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether maneuver-based camera adjustments are enabled.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">setNormalizedPrincipalPoint</a><wbr/>(<a href="sdk-for-android-navigate-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a normalized principal point to be used during navigation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setOrientationMode(com.here.sdk.navigation.AutomotiveCameraBehavior.OrientationMode)">setOrientationMode</a><wbr/>(<a href="sdk-for-android-navigate-automotivecamerabehavior.orientationmode" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.OrientationMode</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the orientation mode for the tracking camera.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setViewRectangle(com.here.sdk.core.Rectangle2D)">setViewRectangle</a><wbr/>(<a href="sdk-for-android-navigate-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a view rectangle for both child cameras.</div>
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
<h3>AutomotiveCameraBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AutomotiveCameraBehavior</span>()</div>
<div class="block"><p>Creates a new instance of this class with default camera behaviors and configuration.
 This constructor automatically creates and configures the underlying
 <a href="sdk-for-android-navigate-trackingcamerabehavior" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior</code></a> and <a href="sdk-for-android-navigate-areacamerabehavior" title="class in com.here.sdk.navigation"><code>AreaCameraBehavior</code></a> instances with default settings.</p></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>AutomotiveCameraBehavior</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AutomotiveCameraBehavior</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> configJson)</span>
                         throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class configured from a JSON string.
 The JSON configuration is validated during construction and applied to the
 underlying <a href="sdk-for-android-navigate-trackingcamerabehavior" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior</code></a> and <a href="sdk-for-android-navigate-areacamerabehavior" title="class in com.here.sdk.navigation"><code>AreaCameraBehavior</code></a> instances.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configJson</code> - <p>A JSON string containing automotive camera configuration settings.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors"><code>InstantiationErrorException</code></a> when the JSON is malformed or contains
     invalid values.</p></dd>
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
<section class="detail" id="setAreaCameraBehaviorVisiblePoints(java.util.List,boolean)">
<h3>setAreaCameraBehaviorVisiblePoints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAreaCameraBehaviorVisiblePoints</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; points,
 boolean includeCurrentPosition)</span></div>
<div class="block"><p>Configures the Area camera to frame the specified points.
 The camera calculates the optimal zoom level and center position to display
 all provided coordinates within the viewport. Use this for showing a single
 point of interest or multiple points such as safety cameras.
 </p><p>This function does not change <a href="sdk-for-android-navigate-index#getActiveCameraType()"><code>getActiveCameraType()</code></a>. To display the configured
 area view, set <a href="sdk-for-android-navigate-index#getActiveCameraType()"><code>getActiveCameraType()</code></a> to <a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype#AREA"><code>AutomotiveCameraBehavior.ActiveCameraType.AREA</code></a>.
 </p><p>Calling this function overrides any previously set geographic bounding box
 configured via <a href="sdk-for-android-navigate-index#setAreaCameraBehaviorGeobox(com.here.sdk.core.GeoBox)"><code>setAreaCameraBehaviorGeobox(com.here.sdk.core.GeoBox)</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>points</code> - <p>The list of geographic coordinates to display.</p></dd>
<dd><code>includeCurrentPosition</code> - <p>When true, the current vehicle position is
     included in the visible area calculation, ensuring the vehicle remains
     visible alongside the provided points.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAreaCameraBehaviorGeobox(com.here.sdk.core.GeoBox)">
<h3>setAreaCameraBehaviorGeobox</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAreaCameraBehaviorGeobox</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geobox" title="class in com.here.sdk.core">GeoBox</a> geobox)</span></div>
<div class="block"><p>Configures the Area camera to frame the specified geographic bounding box.
 The camera automatically calculates the appropriate zoom level and center
 position to ensure the entire area is visible within the viewport.
 </p><p>This function does not change <a href="sdk-for-android-navigate-index#getActiveCameraType()"><code>getActiveCameraType()</code></a>. To display the configured
 area view, set <a href="sdk-for-android-navigate-index#getActiveCameraType()"><code>getActiveCameraType()</code></a> to <a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype#AREA"><code>AutomotiveCameraBehavior.ActiveCameraType.AREA</code></a>.
 </p><p>Calling this function overrides any previously set visible points configured
 via <a href="sdk-for-android-navigate-index#setAreaCameraBehaviorVisiblePoints(java.util.List,boolean)"><code>setAreaCameraBehaviorVisiblePoints(java.util.List&lt;com.here.sdk.core.GeoCoordinates&gt;, boolean)</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geobox</code> - <p>The geographic bounding box to display.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isManeuverDetectionEnabled()">
<h3>isManeuverDetectionEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isManeuverDetectionEnabled</span>()</div>
<div class="block"><p>Gets whether maneuver-based camera adjustments are enabled.
 </p><p>When enabled, the tracking camera automatically adjusts zoom and framing to provide
 better visibility of upcoming turns and maneuvers during navigation. The specific
 adjustments and their timing are defined in the camera configuration.
 </p><p>If tracking is currently active when this property is changed, the setting takes effect
 immediately. Otherwise, it will apply the next time tracking is activated. The initial
 state is determined by the camera configuration provided during construction.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Enables or disables automatic camera adjustments during upcoming maneuvers.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setManeuverDetectionEnabled(boolean)">
<h3>setManeuverDetectionEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverDetectionEnabled</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether maneuver-based camera adjustments are enabled.
 </p><p>When enabled, the tracking camera automatically adjusts zoom and framing to provide
 better visibility of upcoming turns and maneuvers during navigation. The specific
 adjustments and their timing are defined in the camera configuration.
 </p><p>If tracking is currently active when this property is changed, the setting takes effect
 immediately. Otherwise, it will apply the next time tracking is activated. The initial
 state is determined by the camera configuration provided during construction.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Enables or disables automatic camera adjustments during upcoming maneuvers.</p></dd>
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
 for camera updates. This property is forwarded to both the tracking and area cameras,
 ensuring consistent viewport constraints across all camera modes.
 If not set, it uses the viewport bounds of the underlying map view.</p></div>
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
<div class="block"><p>Sets a view rectangle for both child cameras.
 </p><p>Defines a sub-space of the screen that the behavior should consider
 for camera updates. This property is forwarded to both the tracking and area cameras,
 ensuring consistent viewport constraints across all camera modes.
 If not set, it uses the viewport bounds of the underlying map view.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The view rectangle for camera updates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActiveCameraType()">
<h3>getActiveCameraType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.ActiveCameraType</a></span> <span class="element-name">getActiveCameraType</span>()</div>
<div class="block"><p>Gets the type of camera currently handling camera updates.
 </p><p>Defines which camera behavior is currently active:
 <a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype#NONE"><code>AutomotiveCameraBehavior.ActiveCameraType.NONE</code></a> (free navigation), <a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype#TRACKING"><code>AutomotiveCameraBehavior.ActiveCameraType.TRACKING</code></a>,
 or <a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype#AREA"><code>AutomotiveCameraBehavior.ActiveCameraType.AREA</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The active camera type.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActiveCameraType(com.here.sdk.navigation.AutomotiveCameraBehavior.ActiveCameraType)">
<h3>setActiveCameraType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActiveCameraType</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.ActiveCameraType</a> value)</span></div>
<div class="block"><p>Sets the type of camera currently handling camera updates. If <a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype#AREA"><code>AutomotiveCameraBehavior.ActiveCameraType.AREA</code></a> is selected,
 the most recently configured area framing is used. If <a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype#TRACKING"><code>AutomotiveCameraBehavior.ActiveCameraType.TRACKING</code></a> is selected,
 the tracking camera behavior is used. To deactivate set to <a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype#NONE"><code>AutomotiveCameraBehavior.ActiveCameraType.NONE</code></a>.
 </p><p>Defines which camera behavior is currently active:
 <a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype#NONE"><code>AutomotiveCameraBehavior.ActiveCameraType.NONE</code></a> (free navigation), <a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype#TRACKING"><code>AutomotiveCameraBehavior.ActiveCameraType.TRACKING</code></a>,
 or <a href="sdk-for-android-navigate-automotivecamerabehavior.activecameratype#AREA"><code>AutomotiveCameraBehavior.ActiveCameraType.AREA</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The active camera type.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrientationMode()">
<h3>getOrientationMode</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-automotivecamerabehavior.orientationmode" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.OrientationMode</a></span> <span class="element-name">getOrientationMode</span>()</div>
<div class="block"><p>Gets the current orientation mode.
 </p><p>Defines the camera's viewing angle and orientation for tracking mode.
 In <a href="sdk-for-android-navigate-automotivecamerabehavior.orientationmode#MODE_2D"><code>AutomotiveCameraBehavior.OrientationMode.MODE_2D</code></a>, the camera looks straight down and rotates with the vehicle heading.
 In <a href="sdk-for-android-navigate-automotivecamerabehavior.orientationmode#MODE_3D"><code>AutomotiveCameraBehavior.OrientationMode.MODE_3D</code></a>, the camera is tilted for a perspective view.
 In <a href="sdk-for-android-navigate-automotivecamerabehavior.orientationmode#MODE_NORTH_UP"><code>AutomotiveCameraBehavior.OrientationMode.MODE_NORTH_UP</code></a>, the camera maintains north-up orientation regardless of vehicle heading.
 </p><p>Changes to this property take effect immediately on the tracking camera and are
 preserved when switching between tracking and area modes.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The current orientation mode of the camera.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOrientationMode(com.here.sdk.navigation.AutomotiveCameraBehavior.OrientationMode)">
<h3>setOrientationMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOrientationMode</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-automotivecamerabehavior.orientationmode" title="enum class in com.here.sdk.navigation">AutomotiveCameraBehavior.OrientationMode</a> value)</span></div>
<div class="block"><p>Sets the orientation mode for the tracking camera.
 </p><p>Defines the camera's viewing angle and orientation for tracking mode.
 In <a href="sdk-for-android-navigate-automotivecamerabehavior.orientationmode#MODE_2D"><code>AutomotiveCameraBehavior.OrientationMode.MODE_2D</code></a>, the camera looks straight down and rotates with the vehicle heading.
 In <a href="sdk-for-android-navigate-automotivecamerabehavior.orientationmode#MODE_3D"><code>AutomotiveCameraBehavior.OrientationMode.MODE_3D</code></a>, the camera is tilted for a perspective view.
 In <a href="sdk-for-android-navigate-automotivecamerabehavior.orientationmode#MODE_NORTH_UP"><code>AutomotiveCameraBehavior.OrientationMode.MODE_NORTH_UP</code></a>, the camera maintains north-up orientation regardless of vehicle heading.
 </p><p>Changes to this property take effect immediately on the tracking camera and are
 preserved when switching between tracking and area modes.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The current orientation mode of the camera.</p></dd>
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
</main>





</div>
`
}</HTMLBlock>

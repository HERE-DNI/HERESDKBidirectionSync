---
title: "TrackingCameraBehavior.ManeuverModeConfiguration (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrackingCameraBehavior.ManeuverModeConfiguration.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a></dd>
</dl>

<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">TrackingCameraBehavior.ManeuverModeConfiguration</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Configuration that defines how <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior</code></a> reacts to nearby maneuvers.
 On each frame, and based on the current position, the availability of its functional road
 class, and the availability of maneuver data for at least one adjacent maneuver, the camera
 checks for a match against the <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration#maneuverRules"><code>maneuverRules</code></a> in the order they are listed. If a match is
 found, subsequent rules are not checked. If no match is found, if inputs are unavailable,
 or if the matched rule has <code>null</code> options, the camera does not react.
 For correct default initialization, use <a href="sdk-for-android-navigate-trackingcamerabehavior#defaultManeuverModeConfiguration()"><code>TrackingCameraBehavior.defaultManeuverModeConfiguration()</code></a>.</p></div>
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
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration#bearingThresholdInDegrees">bearingThresholdInDegrees</a></code></div>
<div class="col-last even-row-color">
<div class="block">Maximum angle difference in degrees between the current bearing and the bearing to the
 maneuver point.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior.maneuverrule" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverRule</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration#maneuverRules">maneuverRules</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Ordered list of maneuver rules.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration#%3Cinit%3E()">ManeuverModeConfiguration</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

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
<section class="detail" id="maneuverRules">
<h3>maneuverRules</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior.maneuverrule" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverRule</a>&gt;</span> <span class="element-name">maneuverRules</span></div>
<div class="block"><p>Ordered list of maneuver rules. Rules are evaluated in order; the first matching rule
 determines the camera behavior. If empty, this configuration is not valid and the
 camera does not react to maneuvers. If <a href="sdk-for-android-navigate-trackingcamerabehavior#defaultManeuverModeConfiguration()"><code>TrackingCameraBehavior.defaultManeuverModeConfiguration()</code></a> is not used
 for <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior.maneuvermodeconfiguration" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverModeConfiguration</code></a>, it will be an empty list.</p></div>
</section>
</li>
<li>
<section class="detail" id="bearingThresholdInDegrees">
<h3>bearingThresholdInDegrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">bearingThresholdInDegrees</span></div>
<div class="block"><p>Maximum angle difference in degrees between the current bearing and the bearing to the
 maneuver point. If the difference exceeds this threshold, the camera does not turn
 towards the maneuver. Valid range is 0.0 to 180.0. Defaults to 25.0.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ManeuverModeConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ManeuverModeConfiguration</span>()</div>
<div class="block"><p>Creates a new instance.
 Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and
 unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
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

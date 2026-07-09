---
title: "TrackingCameraBehavior.ManeuverModeConfiguration (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrackingCameraBehavior.ManeuverModeConfiguration.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.TrackingCameraBehavior.ManeuverModeConfiguration</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">TrackingCameraBehavior.ManeuverModeConfiguration</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Configuration that defines how <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior</code></a> reacts to nearby maneuvers.
 On each frame, and based on the current position, the availability of its functional road
 class, and the availability of maneuver data for at least one adjacent maneuver, the camera
 checks for a match against the <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration#maneuverRules"><code>maneuverRules</code></a> in the order they are listed. If a match is
 found, subsequent rules are not checked. If no match is found, if inputs are unavailable,
 or if the matched rule has <code>null</code> options, the camera does not react.
 For correct default initialization, use <a href="sdk-for-android-navigate-trackingcamerabehavior#defaultManeuverModeConfiguration()"><code>TrackingCameraBehavior.defaultManeuverModeConfiguration()</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration#bearingThresholdInDegrees">bearingThresholdInDegrees</a></code></div>
<div className="col-last even-row-color">
<div className="block">Maximum angle difference in degrees between the current bearing and the bearing to the
 maneuver point.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverrule" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverRule</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration#maneuverRules">maneuverRules</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Ordered list of maneuver rules.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration#%3Cinit%3E()">ManeuverModeConfiguration</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

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
<section className="detail" id="maneuverRules">
<h3>maneuverRules</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverrule" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverRule</a>&gt;</span> <span className="element-name">maneuverRules</span></div>
<div className="block"><p>Ordered list of maneuver rules. Rules are evaluated in order; the first matching rule
 determines the camera behavior. If empty, this configuration is not valid and the
 camera does not react to maneuvers. If <a href="sdk-for-android-navigate-trackingcamerabehavior#defaultManeuverModeConfiguration()"><code>TrackingCameraBehavior.defaultManeuverModeConfiguration()</code></a> is not used
 for <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuvermodeconfiguration" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverModeConfiguration</code></a>, it will be an empty list.</p></div>
</section>
</li>
<li>
<section className="detail" id="bearingThresholdInDegrees">
<h3>bearingThresholdInDegrees</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">bearingThresholdInDegrees</span></div>
<div className="block"><p>Maximum angle difference in degrees between the current bearing and the bearing to the
 maneuver point. If the difference exceeds this threshold, the camera does not turn
 towards the maneuver. Valid range is 0.0 to 180.0. Defaults to 25.0.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>ManeuverModeConfiguration</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ManeuverModeConfiguration</span>()</div>
<div className="block"><p>Creates a new instance.
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
</div>



</div>
`
}</HTMLBlock>

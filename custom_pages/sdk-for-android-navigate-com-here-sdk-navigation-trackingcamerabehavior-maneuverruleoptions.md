---
title: "TrackingCameraBehavior.ManeuverRuleOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrackingCameraBehavior.ManeuverRuleOptions.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.TrackingCameraBehavior.ManeuverRuleOptions</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">TrackingCameraBehavior.ManeuverRuleOptions</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Defines a set of configurations specific to a <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverrule" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverRule</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions#earlyPreManeuverActivationThresholdInMeters">earlyPreManeuverActivationThresholdInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">Distance in meters for early activation.</div>
</div>
<div className="col-first odd-row-color"><code>double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions#postManeuverActivationThresholdInMeters">postManeuverActivationThresholdInMeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Distance in meters after the previous maneuver point within which this rule remains
 active.</div>
</div>
<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions#preManeuverActivationThresholdInMeters">preManeuverActivationThresholdInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">Distance in meters before the next maneuver point within which this rule becomes active.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverzoomrange" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverZoomRange</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions#zoomRange">zoomRange</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The zoom range for this rule.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions#%3Cinit%3E()">ManeuverRuleOptions</a>()</code></div>
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
<section className="detail" id="zoomRange">
<h3>zoomRange</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverzoomrange" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverZoomRange</a></span> <span className="element-name">zoomRange</span></div>
<div className="block"><p>The zoom range for this rule. Defines the minimum and maximum zoom levels.
 Defaults to a default-constructed <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverzoomrange" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverZoomRange</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="earlyPreManeuverActivationThresholdInMeters">
<h3>earlyPreManeuverActivationThresholdInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">earlyPreManeuverActivationThresholdInMeters</span></div>
<div className="block"><p>Distance in meters for early activation. If the current position enters this threshold
 of the upcoming maneuver while still within <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions#postManeuverActivationThresholdInMeters"><code>postManeuverActivationThresholdInMeters</code></a>
 of the previous maneuver, the camera behaves as though it were already in the upcoming
 maneuver's pre-activation zone. Must be non-negative. Defaults to 0.0.</p></div>
</section>
</li>
<li>
<section className="detail" id="preManeuverActivationThresholdInMeters">
<h3>preManeuverActivationThresholdInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">preManeuverActivationThresholdInMeters</span></div>
<div className="block"><p>Distance in meters before the next maneuver point within which this rule becomes active.
 Must be non-negative. Defaults to 0.0.</p></div>
</section>
</li>
<li>
<section className="detail" id="postManeuverActivationThresholdInMeters">
<h3>postManeuverActivationThresholdInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">postManeuverActivationThresholdInMeters</span></div>
<div className="block"><p>Distance in meters after the previous maneuver point within which this rule remains
 active. Must be non-negative. Defaults to 0.0.</p></div>
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
<h3>ManeuverRuleOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ManeuverRuleOptions</span>()</div>
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

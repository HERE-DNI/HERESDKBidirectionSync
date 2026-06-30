---
title: "TrackingCameraBehavior.ManeuverRuleOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrackingCameraBehavior.ManeuverRuleOptions.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.TrackingCameraBehavior.ManeuverRuleOptions</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a></dd>
</dl>

<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">TrackingCameraBehavior.ManeuverRuleOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Defines a set of configurations specific to a <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior.maneuverrule" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverRule</code></a>.</p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions#earlyPreManeuverActivationThresholdInMeters">earlyPreManeuverActivationThresholdInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Distance in meters for early activation.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions#postManeuverActivationThresholdInMeters">postManeuverActivationThresholdInMeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Distance in meters after the previous maneuver point within which this rule remains
 active.</div>
</div>
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions#preManeuverActivationThresholdInMeters">preManeuverActivationThresholdInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Distance in meters before the next maneuver point within which this rule becomes active.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior.maneuverzoomrange" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverZoomRange</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions#zoomRange">zoomRange</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The zoom range for this rule.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions#%3Cinit%3E()">ManeuverRuleOptions</a>()</code></div>
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
<section class="detail" id="zoomRange">
<h3>zoomRange</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior.maneuverzoomrange" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ManeuverZoomRange</a></span> <span class="element-name">zoomRange</span></div>
<div class="block"><p>The zoom range for this rule. Defines the minimum and maximum zoom levels.
 Defaults to a default-constructed <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior.maneuverzoomrange" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.ManeuverZoomRange</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="earlyPreManeuverActivationThresholdInMeters">
<h3>earlyPreManeuverActivationThresholdInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">earlyPreManeuverActivationThresholdInMeters</span></div>
<div class="block"><p>Distance in meters for early activation. If the current position enters this threshold
 of the upcoming maneuver while still within <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-maneuverruleoptions#postManeuverActivationThresholdInMeters"><code>postManeuverActivationThresholdInMeters</code></a>
 of the previous maneuver, the camera behaves as though it were already in the upcoming
 maneuver's pre-activation zone. Must be non-negative. Defaults to 0.0.</p></div>
</section>
</li>
<li>
<section class="detail" id="preManeuverActivationThresholdInMeters">
<h3>preManeuverActivationThresholdInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">preManeuverActivationThresholdInMeters</span></div>
<div class="block"><p>Distance in meters before the next maneuver point within which this rule becomes active.
 Must be non-negative. Defaults to 0.0.</p></div>
</section>
</li>
<li>
<section class="detail" id="postManeuverActivationThresholdInMeters">
<h3>postManeuverActivationThresholdInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">postManeuverActivationThresholdInMeters</span></div>
<div class="block"><p>Distance in meters after the previous maneuver point within which this rule remains
 active. Must be non-negative. Defaults to 0.0.</p></div>
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
<h3>ManeuverRuleOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ManeuverRuleOptions</span>()</div>
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

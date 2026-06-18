---
title: "TrackingCameraBehavior.SpeedBasedZoomPolicyOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrackingCameraBehavior.SpeedBasedZoomPolicyOptions.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Configuration for computing zoom levels from speed thresholds defined per road classification.
 For correct default initialization, use <a href="sdk-for-android-navigate-trackingcamerabehavior#defaultSpeedBasedZoomPolicyOptions()"><code>TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions()</code></a>.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#delayBetweenThresholdChanges">delayBetweenThresholdChanges</a></code></div>
<div class="col-last even-row-color">
<div class="block">Minimum time interval that must pass before the zoom level is
 allowed to switch to a new speed threshold.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-roadclassification" title="enum class in com.here.sdk.navigation">RoadClassification</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-trackingcamerabehavior.speedthreshold" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedThreshold</a>&gt;&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#roadClassificationToSpeedThreshold">roadClassificationToSpeedThreshold</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Defines, per road classification, how the zoom level should change in
 response to different vehicle speeds.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E()">SpeedBasedZoomPolicyOptions</a>()</code></div>
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
<section class="detail" id="delayBetweenThresholdChanges">
<h3>delayBetweenThresholdChanges</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">delayBetweenThresholdChanges</span></div>
<div class="block"><p>Minimum time interval that must pass before the zoom level is
 allowed to switch to a new speed threshold. If <a href="sdk-for-android-navigate-trackingcamerabehavior#defaultSpeedBasedZoomPolicyOptions()"><code>TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions()</code></a> is not used
 for <a href="sdk-for-android-navigate-trackingcamerabehavior.speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</code></a>, it will be <code>null</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="roadClassificationToSpeedThreshold">
<h3>roadClassificationToSpeedThreshold</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-roadclassification" title="enum class in com.here.sdk.navigation">RoadClassification</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-trackingcamerabehavior.speedthreshold" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedThreshold</a>&gt;&gt;</span> <span class="element-name">roadClassificationToSpeedThreshold</span></div>
<div class="block"><p>Defines, per road classification, how the zoom level should change in
 response to different vehicle speeds. If <a href="sdk-for-android-navigate-trackingcamerabehavior#defaultSpeedBasedZoomPolicyOptions()"><code>TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions()</code></a> is not used
 for <a href="sdk-for-android-navigate-trackingcamerabehavior.speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</code></a>, it will be an empty map.</p></div>
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
<h3>SpeedBasedZoomPolicyOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SpeedBasedZoomPolicyOptions</span>()</div>
<div class="block"><p>Creates a new instance.
 </p><p>Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are
 subject to change without a deprecation process.</p></div>
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

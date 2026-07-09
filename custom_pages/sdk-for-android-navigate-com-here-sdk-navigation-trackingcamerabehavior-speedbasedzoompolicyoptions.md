---
title: "TrackingCameraBehavior.SpeedBasedZoomPolicyOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrackingCameraBehavior.SpeedBasedZoomPolicyOptions.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Configuration for computing zoom levels from speed thresholds defined per road classification.
 For correct default initialization, use <a href="sdk-for-android-navigate-trackingcamerabehavior#defaultSpeedBasedZoomPolicyOptions()"><code>TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions()</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions#delayBetweenThresholdChanges">delayBetweenThresholdChanges</a></code></div>
<div className="col-last even-row-color">
<div className="block">Minimum time interval that must pass before the zoom level is
 allowed to switch to a new speed threshold.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadclassification" title="enum class in com.here.sdk.navigation">RoadClassification</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedthreshold" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedThreshold</a>&gt;&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions#roadClassificationToSpeedThreshold">roadClassificationToSpeedThreshold</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Defines, per road classification, how the zoom level should change in
 response to different vehicle speeds.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions#%3Cinit%3E()">SpeedBasedZoomPolicyOptions</a>()</code></div>
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
<section className="detail" id="delayBetweenThresholdChanges">
<h3>delayBetweenThresholdChanges</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">delayBetweenThresholdChanges</span></div>
<div className="block"><p>Minimum time interval that must pass before the zoom level is
 allowed to switch to a new speed threshold. If <a href="sdk-for-android-navigate-trackingcamerabehavior#defaultSpeedBasedZoomPolicyOptions()"><code>TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions()</code></a> is not used
 for <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</code></a>, it will be <code>null</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="roadClassificationToSpeedThreshold">
<h3>roadClassificationToSpeedThreshold</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadclassification" title="enum class in com.here.sdk.navigation">RoadClassification</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedthreshold" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedThreshold</a>&gt;&gt;</span> <span className="element-name">roadClassificationToSpeedThreshold</span></div>
<div className="block"><p>Defines, per road classification, how the zoom level should change in
 response to different vehicle speeds. If <a href="sdk-for-android-navigate-trackingcamerabehavior#defaultSpeedBasedZoomPolicyOptions()"><code>TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions()</code></a> is not used
 for <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</code></a>, it will be an empty map.</p></div>
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
<h3>SpeedBasedZoomPolicyOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SpeedBasedZoomPolicyOptions</span>()</div>
<div className="block"><p>Creates a new instance.
 Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are
 subject to change without a deprecation process.</p></div>
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

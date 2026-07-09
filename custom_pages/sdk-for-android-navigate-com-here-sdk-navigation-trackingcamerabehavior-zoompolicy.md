---
title: "TrackingCameraBehavior.ZoomPolicy (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrackingCameraBehavior.ZoomPolicy.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.navigation.TrackingCameraBehavior.ZoomPolicy</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">TrackingCameraBehavior.ZoomPolicy</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Defines zoom behavior in different policy settings.
 Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are
 subject to change without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="makeFixedZoomPolicy(double)">
<h3>makeFixedZoomPolicy</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></span> <span className="element-name">makeFixedZoomPolicy</span><wbr/><span className="parameters">(double zoomLevel)</span></div>
<div className="block"><p>Creates a zoom policy that always returns a fixed zoom level.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>zoomLevel</code> - <p>The constant zoom level that the policy will return.</p></dd>
<dt>Returns:</dt>
<dd><p>The ZoomPolicy instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="makeFunctionalRoadClassZoomPolicy(com.here.sdk.navigation.TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions)">
<h3>makeFunctionalRoadClassZoomPolicy</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></span> <span className="element-name">makeFunctionalRoadClassZoomPolicy</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</a> options)</span></div>
<div className="block"><p>Instantiates a zoom policy that selects zoom levels based on functional road class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - <p>Configuration mapping road classes to zoom levels, including a default fallback.</p></dd>
<dt>Returns:</dt>
<dd><p>The ZoomPolicy instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="makeSpeedBasedZoomPolicy(com.here.sdk.navigation.TrackingCameraBehavior.SpeedBasedZoomPolicyOptions)">
<h3>makeSpeedBasedZoomPolicy</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></span> <span className="element-name">makeSpeedBasedZoomPolicy</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</a> options)</span></div>
<div className="block"><p>Instantiates a zoom policy driven by speed thresholds defined per road classification.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - <p>Configuration describing the speed thresholds mapping
     to road classifications.</p></dd>
<dt>Returns:</dt>
<dd><p>The ZoomPolicy instance.</p></dd>
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

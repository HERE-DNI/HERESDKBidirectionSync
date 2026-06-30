---
title: "TrackingCameraBehavior.ZoomPolicy (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrackingCameraBehavior.ZoomPolicy.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.navigation.TrackingCameraBehavior.ZoomPolicy</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a></dd>
</dl>

<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">TrackingCameraBehavior.ZoomPolicy</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Defines zoom behavior in different policy settings.
 Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are
 subject to change without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-trackingcamerabehavior.zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy#makeFixedZoomPolicy(double)">makeFixedZoomPolicy</a><wbr/>(double zoomLevel)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a zoom policy that always returns a fixed zoom level.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-trackingcamerabehavior.zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy#makeFunctionalRoadClassZoomPolicy(com.here.sdk.navigation.TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions)">makeFunctionalRoadClassZoomPolicy</a><wbr/>(<a href="sdk-for-android-navigate-trackingcamerabehavior.functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Instantiates a zoom policy that selects zoom levels based on functional road class.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-trackingcamerabehavior.zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-zoompolicy#makeSpeedBasedZoomPolicy(com.here.sdk.navigation.TrackingCameraBehavior.SpeedBasedZoomPolicyOptions)">makeSpeedBasedZoomPolicy</a><wbr/>(<a href="sdk-for-android-navigate-trackingcamerabehavior.speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Instantiates a zoom policy driven by speed thresholds defined per road classification.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="makeFixedZoomPolicy(double)">
<h3>makeFixedZoomPolicy</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-trackingcamerabehavior.zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></span> <span class="element-name">makeFixedZoomPolicy</span><wbr/><span class="parameters">(double zoomLevel)</span></div>
<div class="block"><p>Creates a zoom policy that always returns a fixed zoom level.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>zoomLevel</code> - <p>The constant zoom level that the policy will return.</p></dd>
<dt>Returns:</dt>
<dd><p>The ZoomPolicy instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeFunctionalRoadClassZoomPolicy(com.here.sdk.navigation.TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions)">
<h3>makeFunctionalRoadClassZoomPolicy</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-trackingcamerabehavior.zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></span> <span class="element-name">makeFunctionalRoadClassZoomPolicy</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-trackingcamerabehavior.functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</a> options)</span></div>
<div class="block"><p>Instantiates a zoom policy that selects zoom levels based on functional road class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - <p>Configuration mapping road classes to zoom levels, including a default fallback.</p></dd>
<dt>Returns:</dt>
<dd><p>The ZoomPolicy instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeSpeedBasedZoomPolicy(com.here.sdk.navigation.TrackingCameraBehavior.SpeedBasedZoomPolicyOptions)">
<h3>makeSpeedBasedZoomPolicy</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-trackingcamerabehavior.zoompolicy" title="class in com.here.sdk.navigation">TrackingCameraBehavior.ZoomPolicy</a></span> <span class="element-name">makeSpeedBasedZoomPolicy</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-trackingcamerabehavior.speedbasedzoompolicyoptions" title="class in com.here.sdk.navigation">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</a> options)</span></div>
<div class="block"><p>Instantiates a zoom policy driven by speed thresholds defined per road classification.</p></div>
<dl class="notes">
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
`
}</HTMLBlock>

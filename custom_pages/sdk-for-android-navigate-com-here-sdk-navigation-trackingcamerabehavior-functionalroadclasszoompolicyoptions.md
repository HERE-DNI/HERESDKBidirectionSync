---
title: "TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-functionalroadclasszoompolicyoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a></dd>
</dl>

<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Configuration for mapping functional road classes to zoom levels.
 For correct default initialization, use <a href="sdk-for-android-navigate-trackingcamerabehavior#defaultFunctionalRoadClassZoomPolicyOptions()"><code>TrackingCameraBehavior.defaultFunctionalRoadClassZoomPolicyOptions()</code></a>.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-functionalroadclasszoompolicyoptions#defaultZoom">defaultZoom</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default zoom returned when the functional road class is missing or unmapped.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a>,<wbr/><a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-functionalroadclasszoompolicyoptions#functionalRoadClassToZoom">functionalRoadClassToZoom</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Maps each functional road class to the zoom that should be used for it.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-trackingcamerabehavior-functionalroadclasszoompolicyoptions#%3Cinit%3E()">FunctionalRoadClassZoomPolicyOptions</a>()</code></div>
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
<section class="detail" id="defaultZoom">
<h3>defaultZoom</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a></span> <span class="element-name">defaultZoom</span></div>
<div class="block"><p>Default zoom returned when the functional road class is missing or unmapped.
 Defaults to a <a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> with kind <a href="sdk-for-android-navigate-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> and value 16.5.</p></div>
</section>
</li>
<li>
<section class="detail" id="functionalRoadClassToZoom">
<h3>functionalRoadClassToZoom</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a>,<wbr/><a href="sdk-for-android-navigate-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>&gt;</span> <span class="element-name">functionalRoadClassToZoom</span></div>
<div class="block"><p>Maps each functional road class to the zoom that should be used for it.
 If <a href="sdk-for-android-navigate-trackingcamerabehavior#defaultFunctionalRoadClassZoomPolicyOptions()"><code>TrackingCameraBehavior.defaultFunctionalRoadClassZoomPolicyOptions()</code></a> is not used
 for <a href="sdk-for-android-navigate-trackingcamerabehavior.functionalroadclasszoompolicyoptions" title="class in com.here.sdk.navigation"><code>TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</code></a>, it will be an empty map.</p></div>
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
<h3>FunctionalRoadClassZoomPolicyOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">FunctionalRoadClassZoomPolicyOptions</span>()</div>
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






</div>
`
}</HTMLBlock>

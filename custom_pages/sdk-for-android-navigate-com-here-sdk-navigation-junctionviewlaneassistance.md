---
title: "JunctionViewLaneAssistance (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- JunctionViewLaneAssistance.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.JunctionViewLaneAssistance</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">JunctionViewLaneAssistance</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A class that provides lane assistance information for the next complex junction
 in order to keep following the route. It is recommended to indicate <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance" title="class in com.here.sdk.navigation"><code>JunctionViewLaneAssistance</code></a>
 and <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance" title="class in com.here.sdk.navigation"><code>ManeuverViewLaneAssistance</code></a> separately or to indicate only <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance" title="class in com.here.sdk.navigation"><code>ManeuverViewLaneAssistance</code></a> information -
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance" title="class in com.here.sdk.navigation"><code>JunctionViewLaneAssistance</code></a> will recommend all lanes that allow to pass the upcoming complex junction, regardless
 if they will lead to the next maneuver or not.
 If the location of a maneuver lies on an upcoming complex junction, the recommended lanes will be
 the same as the ones from <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance" title="class in com.here.sdk.navigation"><code>ManeuverViewLaneAssistance</code></a>.
 A junction is recognized as complex only if:
 <ul>
<li>it is at least a bifurcation;</li>
<li>it has at least two lanes whose directions do not follow the current route.
 In opposition to <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance" title="class in com.here.sdk.navigation"><code>ManeuverViewLaneAssistance</code></a>, notifications are also forwarded when there is
 no maneuver action occurring at the next complex junction.
 Therefore, <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance" title="class in com.here.sdk.navigation"><code>JunctionViewLaneAssistance</code></a> can be disjointed from maneuvers. If lane assistance should be used to
 associate it with upcoming maneuvers, consider to use <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance" title="class in com.here.sdk.navigation"><code>ManeuverViewLaneAssistance</code></a> instead.
 Note that <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance" title="class in com.here.sdk.navigation"><code>ManeuverViewLaneAssistance</code></a> notifications are synchronized with maneuver events,
 whereas <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance" title="class in com.here.sdk.navigation"><code>JunctionViewLaneAssistance</code></a> events are not strictly synchronized with maneuver events.</li>
</ul></p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance#distanceToJunctionInMeters">distanceToJunctionInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Distance to the next complex junction in meters.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance#lanesForNextJunction">lanesForNextJunction</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A list of lanes on the next complex junction.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance#%3Cinit%3E(java.util.List,double)">JunctionViewLaneAssistance</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt; lanesForNextJunction,
 double distanceToJunctionInMeters)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="lanesForNextJunction">
<h3>lanesForNextJunction</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt;</span> <span class="element-name">lanesForNextJunction</span></div>
<div class="block"><p>A list of lanes on the next complex junction.
 The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
 the last index represents the rightmost lane. This is valid for right-hand and left-hand driving
 countries. An empty list means that the complex junction has been passed and that the lane information is not
 valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and
 one event with an empty list afterwards.
 <strong>Note:</strong> Lanes going in opposite direction are not included in the list.</p></div>
</section>
</li>
<li>
<section class="detail" id="distanceToJunctionInMeters">
<h3>distanceToJunctionInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceToJunctionInMeters</span></div>
<div class="block"><p>Distance to the next complex junction in meters.</p></div>
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
<section class="detail" id="&lt;init&gt;(java.util.List,double)">
<h3>JunctionViewLaneAssistance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">JunctionViewLaneAssistance</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt; lanesForNextJunction,
 double distanceToJunctionInMeters)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lanesForNextJunction</code> - <p>A list of lanes on the next complex junction.
 The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
 the last index represents the rightmost lane. This is valid for right-hand and left-hand driving
 countries. An empty list means that the complex junction has been passed and that the lane information is not
 valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and
 one event with an empty list afterwards.
 <strong>Note:</strong> Lanes going in opposite direction are not included in the list.</p></dd>
<dd><code>distanceToJunctionInMeters</code> - <p>Distance to the next complex junction in meters.</p></dd>
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
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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

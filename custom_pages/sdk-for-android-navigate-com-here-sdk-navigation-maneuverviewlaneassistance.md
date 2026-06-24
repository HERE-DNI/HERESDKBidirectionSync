---
title: "ManeuverViewLaneAssistance (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- ManeuverViewLaneAssistance.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.ManeuverViewLaneAssistance</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">ManeuverViewLaneAssistance</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A class that provides lane assistance information for the next maneuver(s).
 During turn-by-turn navigation lane assistance can help a driver to choose the recommended lanes
 in order to complete the upcoming maneuvers.
 The notifications are synchronized with the <a href="sdk-for-android-navigate-eventtextlistener" title="interface in com.here.sdk.navigation"><code>EventTextListener</code></a>.
 <a href="sdk-for-android-navigate-eventtextlistener" title="interface in com.here.sdk.navigation"><code>EventTextListener</code></a> has 4 notification types for each maneuver:
 Range, Reminder, Distance and Action.
 Only the maneuver notification of type Distance will also notify a ManeuverViewLaneAssistance object
 (e.g. "After 400 meters, turn right onto Invalidenstraße").
 The notification will not be sent when other types of maneuver notification are given.
 The notification will not be sent when no lane data is available.
 During tracking mode, no notifications are delivered.
 This ManeuverViewLaneAssistance information is valid until the next maneuver is reached.</p></div>
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
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lane" title="class in com.here.sdk.navigation">Lane</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance#lanesForNextManeuver">lanesForNextManeuver</a></code></div>
<div class="col-last even-row-color">
<div class="block">A list of lanes on the current road that leads to the upcoming maneuver.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lane" title="class in com.here.sdk.navigation">Lane</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance#lanesForNextNextManeuver">lanesForNextNextManeuver</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A list of lanes on the road that leads to the maneuver after the upcoming maneuver.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance#%3Cinit%3E(java.util.List,java.util.List)">ManeuverViewLaneAssistance</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lane" title="class in com.here.sdk.navigation">Lane</a>&gt; lanesForNextManeuver,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lane" title="class in com.here.sdk.navigation">Lane</a>&gt; lanesForNextNextManeuver)</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance#hashCode()">hashCode</a>()</code></div>

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
<section class="detail" id="lanesForNextManeuver">
<h3>lanesForNextManeuver</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lane" title="class in com.here.sdk.navigation">Lane</a>&gt;</span> <span class="element-name">lanesForNextManeuver</span></div>
<div class="block"><p>A list of lanes on the current road that leads to the upcoming maneuver.
 The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
 the last index represents the rightmost lane.
 This is valid for both right-hand and left-hand driving countries.
 Contraflow lanes are not included in the list.
 The list is guaranteed to be non-empty.
 <a href="sdk-for-android-navigate-roadattributes#isRightDrivingSide"><code>RoadAttributes.isRightDrivingSide</code></a> indicates if this is a left-hand driving country or not.</p></div>
</section>
</li>
<li>
<section class="detail" id="lanesForNextNextManeuver">
<h3>lanesForNextNextManeuver</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lane" title="class in com.here.sdk.navigation">Lane</a>&gt;</span> <span class="element-name">lanesForNextNextManeuver</span></div>
<div class="block"><p>A list of lanes on the road that leads to the maneuver after the upcoming maneuver.
 The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
 the last index represents the rightmost lane.
 This is valid for both right-hand and left-hand driving countries.
 Contraflow lanes are not included in the list.
 <a href="sdk-for-android-navigate-roadattributes#isRightDrivingSide"><code>RoadAttributes.isRightDrivingSide</code></a> indicates if this is a left-hand driving country or not.
 By default, this list is empty. It will be filled when the next two maneuvers are too
 close to each other, or when the next two maneuvers are roundabout maneuvers.
 Note: This notification is delivered at the same time as the <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance#lanesForNextManeuver"><code>lanesForNextManeuver</code></a>.
 There is no separate maneuver notification on the second maneuver when two maneuvers are
 are too close to each other.</p></div>
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
<section class="detail" id="&lt;init&gt;(java.util.List,java.util.List)">
<h3>ManeuverViewLaneAssistance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ManeuverViewLaneAssistance</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lane" title="class in com.here.sdk.navigation">Lane</a>&gt; lanesForNextManeuver,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lane" title="class in com.here.sdk.navigation">Lane</a>&gt; lanesForNextNextManeuver)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lanesForNextManeuver</code> - <p>A list of lanes on the current road that leads to the upcoming maneuver.
 The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
 the last index represents the rightmost lane.
 This is valid for both right-hand and left-hand driving countries.
 Contraflow lanes are not included in the list.
 The list is guaranteed to be non-empty.
 <a href="sdk-for-android-navigate-roadattributes#isRightDrivingSide"><code>RoadAttributes.isRightDrivingSide</code></a> indicates if this is a left-hand driving country or not.</p></dd>
<dd><code>lanesForNextNextManeuver</code> - <p>A list of lanes on the road that leads to the maneuver after the upcoming maneuver.
 The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
 the last index represents the rightmost lane.
 This is valid for both right-hand and left-hand driving countries.
 Contraflow lanes are not included in the list.
 <a href="sdk-for-android-navigate-roadattributes#isRightDrivingSide"><code>RoadAttributes.isRightDrivingSide</code></a> indicates if this is a left-hand driving country or not.
 By default, this list is empty. It will be filled when the next two maneuvers are too
 close to each other, or when the next two maneuvers are roundabout maneuvers.
 Note: This notification is delivered at the same time as the <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance#lanesForNextManeuver"><code>lanesForNextManeuver</code></a>.
 There is no separate maneuver notification on the second maneuver when two maneuvers are
 are too close to each other.</p></dd>
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
`
}</HTMLBlock>

---
title: "ManeuverViewLaneAssistance (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ManeuverViewLaneAssistance.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.ManeuverViewLaneAssistance</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">ManeuverViewLaneAssistance</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A class that provides lane assistance information for the next maneuver(s).
 During turn-by-turn navigation lane assistance can help a driver to choose the recommended lanes
 in order to complete the upcoming maneuvers.
 The notifications are synchronized with the <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener" title="interface in com.here.sdk.navigation"><code>EventTextListener</code></a>.
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener" title="interface in com.here.sdk.navigation"><code>EventTextListener</code></a> has 4 notification types for each maneuver:
 Range, Reminder, Distance and Action.
 Only the maneuver notification of type Distance will also notify a ManeuverViewLaneAssistance object
 (e.g. "After 400 meters, turn right onto Invalidenstraße").
 The notification will not be sent when other types of maneuver notification are given.
 The notification will not be sent when no lane data is available.
 During tracking mode, no notifications are delivered.
 This ManeuverViewLaneAssistance information is valid until the next maneuver is reached.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance#lanesForNextManeuver">lanesForNextManeuver</a></code></div>
<div className="col-last even-row-color">
<div className="block">A list of lanes on the current road that leads to the upcoming maneuver.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance#lanesForNextNextManeuver">lanesForNextNextManeuver</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A list of lanes on the road that leads to the maneuver after the upcoming maneuver.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance#%3Cinit%3E(java.util.List,java.util.List)">ManeuverViewLaneAssistance</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt; lanesForNextManeuver,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt; lanesForNextNextManeuver)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section className="detail" id="lanesForNextManeuver">
<h3>lanesForNextManeuver</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt;</span> <span className="element-name">lanesForNextManeuver</span></div>
<div className="block"><p>A list of lanes on the current road that leads to the upcoming maneuver.
 The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
 the last index represents the rightmost lane.
 This is valid for both right-hand and left-hand driving countries.
 Contraflow lanes are not included in the list.
 The list is guaranteed to be non-empty.
 <a href="sdk-for-android-navigate-roadattributes#isRightDrivingSide"><code>RoadAttributes.isRightDrivingSide</code></a> indicates if this is a left-hand driving country or not.</p></div>
</section>
</li>
<li>
<section className="detail" id="lanesForNextNextManeuver">
<h3>lanesForNextNextManeuver</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt;</span> <span className="element-name">lanesForNextNextManeuver</span></div>
<div className="block"><p>A list of lanes on the road that leads to the maneuver after the upcoming maneuver.
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
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(java.util.List,java.util.List)">
<h3>ManeuverViewLaneAssistance</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ManeuverViewLaneAssistance</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt; lanesForNextManeuver,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt; lanesForNextNextManeuver)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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

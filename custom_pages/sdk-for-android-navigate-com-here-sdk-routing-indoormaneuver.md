---
title: "IndoorManeuver (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-indoormaneuver"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- IndoorManeuver.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.routing.IndoorManeuver</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">IndoorManeuver</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents a maneuver within an indoor section.</p></div>
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
<section className="detail" id="getAction()">
<h3>getAction</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-indoormaneuveractions" title="enum class in com.here.sdk.routing">IndoorManeuverActions</a></span> <span className="element-name">getAction</span>()</div>
<div className="block"><p>Gets the action type of this maneuver.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The action type of this maneuver.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCoordinate()">
<h3>getCoordinate</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">getCoordinate</span>()</div>
<div className="block"><p>Gets the geographic coordinates of this maneuver.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The geographic coordinates of this maneuver.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOffset()">
<h3>getOffset</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getOffset</span>()</div>
<div className="block"><p>Gets the offset of this maneuver from the start of the section.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The offset of this maneuver from the start of the section.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSectionIndex()">
<h3>getSectionIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getSectionIndex</span>()</div>
<div className="block"><p>Gets the section index this maneuver belongs to.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The section index this maneuver belongs to.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLengthInMeters()">
<h3>getLengthInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">float</span> <span className="element-name">getLengthInMeters</span>()</div>
<div className="block"><p>Gets the length of this maneuver in meters.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The length of this maneuver in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDuration()">
<h3>getDuration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">getDuration</span>()</div>
<div className="block"><p>Gets the duration to complete this maneuver.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The duration to complete this maneuver.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLevelZIndex()">
<h3>getLevelZIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getLevelZIndex</span>()</div>
<div className="block"><p>Gets the vertical level index of this maneuver.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The vertical level index of this maneuver.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getIndoorSpaceData()">
<h3>getIndoorSpaceData</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-indoorspacedata" title="class in com.here.sdk.routing">IndoorSpaceData</a></span> <span className="element-name">getIndoorSpaceData</span>()</div>
<div className="block"><p>Gets the indoor space data for this maneuver. This will be not null if the IndoorManeuverAction is ENTER_ACTION or LEAVE_ACTION.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The indoor space data for this maneuver. This will be not null if the IndoorManeuverAction is ENTER_ACTION or LEAVE_ACTION.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getIndoorLevelChangeData()">
<h3>getIndoorLevelChangeData</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-indoorlevelchangedata" title="class in com.here.sdk.routing">IndoorLevelChangeData</a></span> <span className="element-name">getIndoorLevelChangeData</span>()</div>
<div className="block"><p>Gets the level change data for this maneuver. This will be not null if the IndoorManeuverAction is LEVEL_CHANGE_ACTION.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The level change data for this maneuver. This will be not null if the IndoorManeuverAction is LEVEL_CHANGE_ACTION.</p></dd>
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

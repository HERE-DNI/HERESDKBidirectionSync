---
title: "Milestone (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-milestone"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Milestone.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.Milestone</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Milestone</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents information about the waypoints along the route.
 Note that this can include additional waypoints added during route
 calculation that may not have been part of the original user-defined
 waypoint list. For example, additional waypoints are added automatically
 between sections that require a different transport mode like when taking a
 ferry.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-milestone#mapMatchedCoordinates">mapMatchedCoordinates</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map-matched geographic coordinates.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-milestone#originalCoordinates">originalCoordinates</a></code></div>
<div className="col-last odd-row-color">
<div className="block">User-defined geographic coordinates.</div>
</div>
<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-milestone#sectionIndex">sectionIndex</a></code></div>
<div className="col-last even-row-color">
<div className="block">Index of the section on the route.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-milestonetype" title="enum class in com.here.sdk.navigation">MilestoneType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-milestone#type">type</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Type of this Milestone</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-milestone#waypointIndex">waypointIndex</a></code></div>
<div className="col-last even-row-color">
<div className="block">If present, this index corresponds to the waypoint in the original
 user-defined waypoint list.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-milestone#%3Cinit%3E(int,java.lang.Integer,com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCoordinates,com.here.sdk.navigation.MilestoneType)">Milestone</a><wbr/>(int sectionIndex,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> waypointIndex,
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> originalCoordinates,
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> mapMatchedCoordinates,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestonetype" title="enum class in com.here.sdk.navigation">MilestoneType</a> type)</code></div>
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
<section className="detail" id="sectionIndex">
<h3>sectionIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">sectionIndex</span></div>
<div className="block"><p>Index of the section on the route.</p></div>
</section>
</li>
<li>
<section className="detail" id="waypointIndex">
<h3>waypointIndex</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">waypointIndex</span></div>
<div className="block"><p>If present, this index corresponds to the waypoint in the original
 user-defined waypoint list. Otherwise this waypoint was added during
 route calculation by the system.</p></div>
</section>
</li>
<li>
<section className="detail" id="originalCoordinates">
<h3>originalCoordinates</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">originalCoordinates</span></div>
<div className="block"><p>User-defined geographic coordinates. If not available, this waypoint was
 added during route calculation.</p></div>
</section>
</li>
<li>
<section className="detail" id="mapMatchedCoordinates">
<h3>mapMatchedCoordinates</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">mapMatchedCoordinates</span></div>
<div className="block"><p>Map-matched geographic coordinates.</p></div>
</section>
</li>
<li>
<section className="detail" id="type">
<h3>type</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-milestonetype" title="enum class in com.here.sdk.navigation">MilestoneType</a></span> <span className="element-name">type</span></div>
<div className="block"><p>Type of this Milestone</p></div>
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
<section className="detail" id="&lt;init&gt;(int,java.lang.Integer,com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCoordinates,com.here.sdk.navigation.MilestoneType)">
<h3>Milestone</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Milestone</span><wbr/><span className="parameters">(int sectionIndex,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> waypointIndex,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> originalCoordinates,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> mapMatchedCoordinates,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestonetype" title="enum class in com.here.sdk.navigation">MilestoneType</a> type)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sectionIndex</code> - <p>Index of the section on the route.</p></dd>
<dd><code>waypointIndex</code> - <p>If present, this index corresponds to the waypoint in the original
 user-defined waypoint list. Otherwise this waypoint was added during
 route calculation by the system.</p></dd>
<dd><code>originalCoordinates</code> - <p>User-defined geographic coordinates. If not available, this waypoint was
 added during route calculation.</p></dd>
<dd><code>mapMatchedCoordinates</code> - <p>Map-matched geographic coordinates.</p></dd>
<dd><code>type</code> - <p>Type of this Milestone</p></dd>
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

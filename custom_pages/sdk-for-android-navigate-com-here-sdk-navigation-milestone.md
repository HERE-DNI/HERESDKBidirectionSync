---
title: "Milestone (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-milestone"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Milestone.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.Milestone</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Milestone</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents information about the waypoints along the route.
 </p><p>Note that this can include additional waypoints added during route
 calculation that may not have been part of the original user-defined
 waypoint list. For example, additional waypoints are added automatically
 between sections that require a different transport mode like when taking a
 ferry.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#mapMatchedCoordinates">mapMatchedCoordinates</a></code></div>
<div class="col-last even-row-color">
<div class="block">Map-matched geographic coordinates.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#originalCoordinates">originalCoordinates</a></code></div>
<div class="col-last odd-row-color">
<div class="block">User-defined geographic coordinates.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#sectionIndex">sectionIndex</a></code></div>
<div class="col-last even-row-color">
<div class="block">Index of the section on the route.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-milestonetype" title="enum class in com.here.sdk.navigation">MilestoneType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#type">type</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type of this Milestone</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#waypointIndex">waypointIndex</a></code></div>
<div class="col-last even-row-color">
<div class="block">If present, this index corresponds to the waypoint in the original
 user-defined waypoint list.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(int,java.lang.Integer,com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCoordinates,com.here.sdk.navigation.MilestoneType)">Milestone</a><wbr/>(int sectionIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> waypointIndex,
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> originalCoordinates,
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> mapMatchedCoordinates,
 <a href="sdk-for-android-navigate-milestonetype" title="enum class in com.here.sdk.navigation">MilestoneType</a> type)</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>

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
<section class="detail" id="sectionIndex">
<h3>sectionIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">sectionIndex</span></div>
<div class="block"><p>Index of the section on the route.</p></div>
</section>
</li>
<li>
<section class="detail" id="waypointIndex">
<h3>waypointIndex</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">waypointIndex</span></div>
<div class="block"><p>If present, this index corresponds to the waypoint in the original
 user-defined waypoint list. Otherwise this waypoint was added during
 route calculation by the system.</p></div>
</section>
</li>
<li>
<section class="detail" id="originalCoordinates">
<h3>originalCoordinates</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">originalCoordinates</span></div>
<div class="block"><p>User-defined geographic coordinates. If not available, this waypoint was
 added during route calculation.</p></div>
</section>
</li>
<li>
<section class="detail" id="mapMatchedCoordinates">
<h3>mapMatchedCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">mapMatchedCoordinates</span></div>
<div class="block"><p>Map-matched geographic coordinates.</p></div>
</section>
</li>
<li>
<section class="detail" id="type">
<h3>type</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-milestonetype" title="enum class in com.here.sdk.navigation">MilestoneType</a></span> <span class="element-name">type</span></div>
<div class="block"><p>Type of this Milestone</p></div>
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
<section class="detail" id="&lt;init&gt;(int,java.lang.Integer,com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCoordinates,com.here.sdk.navigation.MilestoneType)">
<h3>Milestone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Milestone</span><wbr/><span class="parameters">(int sectionIndex,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> waypointIndex,
 @Nullable
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> originalCoordinates,
 @NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> mapMatchedCoordinates,
 @NonNull
 <a href="sdk-for-android-navigate-milestonetype" title="enum class in com.here.sdk.navigation">MilestoneType</a> type)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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

---
title: "MapMarkerCluster.Grouping (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapmarkercluster-grouping"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapMarkerCluster.Grouping.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapview.MapMarkerCluster.Grouping</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a></dd>
</dl>

<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">MapMarkerCluster.Grouping</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents a group of map markers belonging to a cluster.
 </p><p>It contains a list of map markers grouped on map view under single icon of marker cluster or
 single map marker entry for markers being part of cluster but spread enough not to be grouped.</p></div>
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
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#markers">markers</a></code></div>
<div class="col-last even-row-color">
<div class="block">List of map markers grouped on map view under map marker cluster icon.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#parent">parent</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Map marker cluster that entries in <a href="sdk-for-android-navigate-index#markers"><code>markers</code></a> belong to.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(java.util.List,com.here.sdk.mapview.MapMarkerCluster)">Grouping</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers,
 <a href="sdk-for-android-navigate-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a> parent)</code></div>
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
<section class="detail" id="markers">
<h3>markers</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>&gt;</span> <span class="element-name">markers</span></div>
<div class="block"><p>List of map markers grouped on map view under map marker cluster icon.</p></div>
</section>
</li>
<li>
<section class="detail" id="parent">
<h3>parent</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a></span> <span class="element-name">parent</span></div>
<div class="block"><p>Map marker cluster that entries in <a href="sdk-for-android-navigate-index#markers"><code>markers</code></a> belong to.</p></div>
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
<section class="detail" id="&lt;init&gt;(java.util.List,com.here.sdk.mapview.MapMarkerCluster)">
<h3>Grouping</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Grouping</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a>&gt; markers,
 @NonNull
 <a href="sdk-for-android-navigate-mapmarkercluster" title="class in com.here.sdk.mapview">MapMarkerCluster</a> parent)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>markers</code> - <p>List of map markers grouped on map view under map marker cluster icon.</p></dd>
<dd><code>parent</code> - <p>Map marker cluster that entries in <a href="sdk-for-android-navigate-index#markers"><code>markers</code></a> belong to.</p></dd>
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

---
title: "SegmentReference (API Reference)"
slug: "sdk-for-android-explore-segmentreference"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SegmentReference.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="../../../../index.html">Overview</a></li>
<li><a href="package-summary.html">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="package-tree.html">Tree</a></li>
<li><a href="../../../../deprecated-list.html">Deprecated</a></li>
<li><a href="../../../../index-all.html">Index</a></li>
<li><a href="../../../../help-doc.html#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li><a href="#field-summary">Field</a> | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#field-detail">Field</a> | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.SegmentReference</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SegmentReference</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Reference to a segment id with a travel direction.
 <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></p></div>
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
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#localId">localId</a></code></div>
<div class="col-last even-row-color">
<div class="block">Local ID of the segment inside the OCM tile.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#offsetEnd">offsetEnd</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment.</div>
</div>
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#offsetStart">offsetStart</a></code></div>
<div class="col-last even-row-color">
<div class="block">The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#segmentId">segmentId</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Topology segment id representing a unique identifier within the HERE platform catalogs.</div>
</div>
<div class="col-first even-row-color"><code>long</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#tilePartitionId">tilePartitionId</a></code></div>
<div class="col-last even-row-color">
<div class="block">HERE tile partition id (Morton-encoding + level indicator) of the segment.</div>
</div>
<div class="col-first odd-row-color"><code><a href="TravelDirection.html" title="enum class in com.here.sdk.routing">TravelDirection</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#travelDirection">travelDirection</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Travel direction of the segment.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SegmentReference</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">SegmentReference</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection)">SegmentReference</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 <a href="TravelDirection.html" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection,double)">SegmentReference</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 <a href="TravelDirection.html" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection,double,double)">SegmentReference</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 <a href="TravelDirection.html" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart,
 double offsetEnd)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long)">SegmentReference</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 <a href="TravelDirection.html" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart,
 double offsetEnd,
 long tilePartitionId)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long,java.lang.Long)">SegmentReference</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 <a href="TravelDirection.html" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart,
 double offsetEnd,
 long tilePartitionId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a> localId)</code></div>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SegmentReference.html" title="class in com.here.sdk.routing">SegmentReference</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#fromString(java.lang.String)">fromString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentRef)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an instance of this struct from a string if it's well-formatted, <code>null</code> otherwise.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="segmentId">
<h3>segmentId</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">segmentId</span></div>
<div class="block"><p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></div>
</section>
</li>
<li>
<section class="detail" id="travelDirection">
<h3>travelDirection</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="TravelDirection.html" title="enum class in com.here.sdk.routing">TravelDirection</a></span> <span class="element-name">travelDirection</span></div>
<div class="block"><p>Travel direction of the segment.</p></div>
</section>
</li>
<li>
<section class="detail" id="offsetStart">
<h3>offsetStart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">offsetStart</span></div>
<div class="block"><p>The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></div>
</section>
</li>
<li>
<section class="detail" id="offsetEnd">
<h3>offsetEnd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">offsetEnd</span></div>
<div class="block"><p>The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></div>
</section>
</li>
<li>
<section class="detail" id="tilePartitionId">
<h3>tilePartitionId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">tilePartitionId</span></div>
<div class="block"><p>HERE tile partition id (Morton-encoding + level indicator) of the segment.
 As in HERE Map Content.</p></div>
</section>
</li>
<li>
<section class="detail" id="localId">
<h3>localId</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a></span> <span class="element-name">localId</span></div>
<div class="block"><p>Local ID of the segment inside the OCM tile.</p></div>
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
<h3>SegmentReference</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SegmentReference</span>()</div>
<div class="block"><p>Creates a new instance.</p></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>SegmentReference</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SegmentReference</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.routing.TravelDirection)">
<h3>SegmentReference</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SegmentReference</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 @NonNull
 <a href="TravelDirection.html" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></dd>
<dd><code>travelDirection</code> - <p>Travel direction of the segment.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.routing.TravelDirection,double)">
<h3>SegmentReference</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SegmentReference</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 @NonNull
 <a href="TravelDirection.html" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></dd>
<dd><code>travelDirection</code> - <p>Travel direction of the segment.</p></dd>
<dd><code>offsetStart</code> - <p>The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.routing.TravelDirection,double,double)">
<h3>SegmentReference</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SegmentReference</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 @NonNull
 <a href="TravelDirection.html" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart,
 double offsetEnd)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></dd>
<dd><code>travelDirection</code> - <p>Travel direction of the segment.</p></dd>
<dd><code>offsetStart</code> - <p>The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
<dd><code>offsetEnd</code> - <p>The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long)">
<h3>SegmentReference</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SegmentReference</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 @NonNull
 <a href="TravelDirection.html" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart,
 double offsetEnd,
 long tilePartitionId)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></dd>
<dd><code>travelDirection</code> - <p>Travel direction of the segment.</p></dd>
<dd><code>offsetStart</code> - <p>The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
<dd><code>offsetEnd</code> - <p>The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
<dd><code>tilePartitionId</code> - <p>HERE tile partition id (Morton-encoding + level indicator) of the segment.
 As in HERE Map Content.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long,java.lang.Long)">
<h3>SegmentReference</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SegmentReference</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 @NonNull
 <a href="TravelDirection.html" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart,
 double offsetEnd,
 long tilePartitionId,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a> localId)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></dd>
<dd><code>travelDirection</code> - <p>Travel direction of the segment.</p></dd>
<dd><code>offsetStart</code> - <p>The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
<dd><code>offsetEnd</code> - <p>The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
<dd><code>tilePartitionId</code> - <p>HERE tile partition id (Morton-encoding + level indicator) of the segment.
 As in HERE Map Content.</p></dd>
<dd><code>localId</code> - <p>Local ID of the segment inside the OCM tile.</p></dd>
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
<li>
<section class="detail" id="fromString(java.lang.String)">
<h3>fromString</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public static</span> <span class="return-type"><a href="SegmentReference.html" title="class in com.here.sdk.routing">SegmentReference</a></span> <span class="element-name">fromString</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentRef)</span></div>
<div class="block"><p>Returns an instance of this struct from a string if it's well-formatted, <code>null</code> otherwise.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>segmentRef</code> - <p>The string to parse</p></dd>
<dt>Returns:</dt>
<dd><p>An instance of <a href="SegmentReference.html" title="class in com.here.sdk.routing"><code>SegmentReference</code></a> from a string if it's well-formatted, <code>null</code> otherwise.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
</div>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>

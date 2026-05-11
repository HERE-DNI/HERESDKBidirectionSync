---
title: "Isoline (API Reference)"
slug: "sdk-for-android-explore-isoline"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Isoline.html -->
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
<li>Field | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
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
<div class="inheritance"><a href="../../NativeBase.html" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.routing.Isoline</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Isoline</span>
<span class="extends-implements">extends <a href="../../NativeBase.html" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Represents an isoline polygon around a center point. Any possible route between
 the center and any point on the edges of the polygon can be travelled within the
 given range restriction. The edges of the polygon are not guaranteed to be on the road as
 all reachable road endpoints are smoothened to fit into one polygon shape. This
 process can be influenced by setting <a href="IsolineOptions.Calculation.html#maxPoints"><code>IsolineOptions.Calculation.maxPoints</code></a>.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.routing.IsolineRangeType,double,com.here.sdk.routing.MapMatchedCoordinates,java.util.List)">Isoline</a><wbr/>(<a href="IsolineRangeType.html" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 double rangeValue,
 <a href="MapMatchedCoordinates.html" title="class in com.here.sdk.routing">MapMatchedCoordinates</a> center,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../core/GeoPolygon.html" title="class in com.here.sdk.core">GeoPolygon</a>&gt; polygons)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs an isoline instance.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MapMatchedCoordinates.html" title="class in com.here.sdk.routing">MapMatchedCoordinates</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCenter()">getCenter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the center point that was used to calculate this isoline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../core/GeoPolygon.html" title="class in com.here.sdk.core">GeoPolygon</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPolygons()">getPolygons</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a list of polygons that belong to this isoline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="IsolineRangeType.html" title="enum class in com.here.sdk.routing">IsolineRangeType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRangeType()">getRangeType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the type of the restriction that was used to calculate this isoline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRangeValue()">getRangeValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the numerical value of the restriction that was used to calculate this isoline.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.IsolineRangeType,double,com.here.sdk.routing.MapMatchedCoordinates,java.util.List)">
<h3>Isoline</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Isoline</span><wbr/><span class="parameters">(@NonNull
 <a href="IsolineRangeType.html" title="enum class in com.here.sdk.routing">IsolineRangeType</a> rangeType,
 double rangeValue,
 @NonNull
 <a href="MapMatchedCoordinates.html" title="class in com.here.sdk.routing">MapMatchedCoordinates</a> center,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../core/GeoPolygon.html" title="class in com.here.sdk.core">GeoPolygon</a>&gt; polygons)</span></div>
<div class="block"><p>Constructs an isoline instance. This instance is provided by the
 <a href="CalculateIsolineCallback.html" title="interface in com.here.sdk.routing"><code>CalculateIsolineCallback</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rangeType</code> - <p>Specifies the range type of the provided <code>rangeValue</code> list.</p></dd>
<dd><code>rangeValue</code> - <p>A list of range values. At least one value must be set.</p></dd>
<dd><code>center</code> - <p>The center of the isoline.</p></dd>
<dd><code>polygons</code> - <p>A list of polygons that belong to this isoline. At least one value must be set.</p></dd>
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
<section class="detail" id="getRangeType()">
<h3>getRangeType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="IsolineRangeType.html" title="enum class in com.here.sdk.routing">IsolineRangeType</a></span> <span class="element-name">getRangeType</span>()</div>
<div class="block"><p>Gets the type of the restriction that was used to calculate this isoline.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Specifies the type of the restriction that was used to calculate this isoline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRangeValue()">
<h3>getRangeValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getRangeValue</span>()</div>
<div class="block"><p>Gets the numerical value of the restriction that was used to calculate this isoline.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Specifies the numerical value of the restriction that was used to calculate this isoline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCenter()">
<h3>getCenter</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="MapMatchedCoordinates.html" title="class in com.here.sdk.routing">MapMatchedCoordinates</a></span> <span class="element-name">getCenter</span>()</div>
<div class="block"><p>Gets the center point that was used to calculate this isoline.
 <p>Specifies the center point that was used to calculate this isoline.
 This includes the original center that was passed to the RoutingEngine.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The center point that was used to calculate this isoline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPolygons()">
<h3>getPolygons</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../core/GeoPolygon.html" title="class in com.here.sdk.core">GeoPolygon</a>&gt;</span> <span class="element-name">getPolygons</span>()</div>
<div class="block"><p>Gets a list of polygons that belong to this isoline. An isoline can consist of multiple
 polygons. For example, islands that can be reached by a ferry are included.
 Each island is then represented as a separate polygon. However, in most cases
 only a single polygon is included.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A list of polygons that belong to this isoline. An isoline can consist of multiple
     polygons. For example, islands that can be reached by a ferry are included.
     Each island is then represented as a separate polygon. However, in most cases
     only a single polygon is included.</p></dd>
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

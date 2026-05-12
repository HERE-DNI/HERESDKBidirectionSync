---
title: "TransitRouteOptions (API Reference)"
slug: "sdk-for-android-explore-transitrouteoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TransitRouteOptions.html -->
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
<div class="inheritance">com.here.sdk.routing.TransitRouteOptions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">TransitRouteOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>All the options to specify how a public transit route should be calculated.</p></div>
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
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#alternatives">alternatives</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of alternative routes to return aside from the optimal route.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#arrivalTime">arrivalTime</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional time when travel is expected to end.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#changes">changes</a></code></div>
<div class="col-last even-row-color">
<div class="block">Maximum number of changes or transfers allowed in a route.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#departureTime">departureTime</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional time when travel is expected to start.</div>
</div>
<div class="col-first even-row-color"><code><a href="TransitModeFilter.html" title="enum class in com.here.sdk.routing">TransitModeFilter</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#modeFilter">modeFilter</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines inclusion or exclusion of transit modes for route calculation.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="TransitMode.html" title="enum class in com.here.sdk.routing">TransitMode</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#modes">modes</a></code></div>
<div class="col-last odd-row-color">
<div class="block">This list is used to determine which transit modes should be used for route calculation,
 <a href="#modeFilter"><code>modeFilter</code></a> specifies whether this list is an inclusion or an exclusion.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#pedestrianMaxDistanceInMeters">pedestrianMaxDistanceInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Maximum allowed walking distance in meters (e.g.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#pedestrianSpeedInMetersPerSecond">pedestrianSpeedInMetersPerSecond</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Walking speed in meters per second.</div>
</div>
<div class="col-first even-row-color"><code><a href="RouteTextOptions.html" title="class in com.here.sdk.routing">RouteTextOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#textOptions">textOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">Customize textual content returned from the route calculation, such
 as localization, format, and unit system.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TransitRouteOptions</a>()</code></div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TransitRouteOptions.html" title="class in com.here.sdk.routing">TransitRouteOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#fromDefaultParameterConfiguration()">fromDefaultParameterConfiguration</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns TransitRouteOptions instance with default values used in SDK.</div>
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
<section class="detail" id="departureTime">
<h3>departureTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">departureTime</span></div>
<div class="block"><p>Optional time when travel is expected to start.
 If it is not specified, it is set to the current time.</p></div>
</section>
</li>
<li>
<section class="detail" id="arrivalTime">
<h3>arrivalTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">arrivalTime</span></div>
<div class="block"><p>Optional time when travel is expected to end.</p></div>
</section>
</li>
<li>
<section class="detail" id="alternatives">
<h3>alternatives</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">alternatives</span></div>
<div class="block"><p>Number of alternative routes to return aside from the optimal route.
 The provided value must be in the range [0, 6].
 By default, it is 0 and only one route is calculated.</p></div>
</section>
</li>
<li>
<section class="detail" id="changes">
<h3>changes</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">changes</span></div>
<div class="block"><p>Maximum number of changes or transfers allowed in a route.
 When it is not set, unlimited number of changes is permitted.
 The provided value must be in the range [0, 6].</p></div>
</section>
</li>
<li>
<section class="detail" id="modeFilter">
<h3>modeFilter</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="TransitModeFilter.html" title="enum class in com.here.sdk.routing">TransitModeFilter</a></span> <span class="element-name">modeFilter</span></div>
<div class="block"><p>Defines inclusion or exclusion of transit modes for route calculation.
 By default, the inclusion mode is used.</p></div>
</section>
</li>
<li>
<section class="detail" id="modes">
<h3>modes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="TransitMode.html" title="enum class in com.here.sdk.routing">TransitMode</a>&gt;</span> <span class="element-name">modes</span></div>
<div class="block"><p>This list is used to determine which transit modes should be used for route calculation,
 <a href="#modeFilter"><code>modeFilter</code></a> specifies whether this list is an inclusion or an exclusion.
 For example, specifying subway and bus transit modes with the include filter, returns only subway
 and bus transit modes, and with the exclude filter, returns all the transit modes except subway
 and bus. When not set, all the supported transit modes are permitted.
 By default, this list is empty.</p></div>
</section>
</li>
<li>
<section class="detail" id="pedestrianSpeedInMetersPerSecond">
<h3>pedestrianSpeedInMetersPerSecond</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">pedestrianSpeedInMetersPerSecond</span></div>
<div class="block"><p>Walking speed in meters per second. Influences the duration of walking segments from origin to a station,
 from a station to destination and in-between the stations (e.g. if transfer is needed).
 The provided value must be in the range [0.5, 2.0].
 The default value is 1.0 mps.</p></div>
</section>
</li>
<li>
<section class="detail" id="pedestrianMaxDistanceInMeters">
<h3>pedestrianMaxDistanceInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">pedestrianMaxDistanceInMeters</span></div>
<div class="block"><p>Maximum allowed walking distance in meters (e.g. when looking for nearest stations).
 The provided value must be in the range [0, 6000].
 The default value is 2000 meters.</p></div>
</section>
</li>
<li>
<section class="detail" id="textOptions">
<h3>textOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="RouteTextOptions.html" title="class in com.here.sdk.routing">RouteTextOptions</a></span> <span class="element-name">textOptions</span></div>
<div class="block"><p>Customize textual content returned from the route calculation, such
 as localization, format, and unit system.</p></div>
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
<h3>TransitRouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TransitRouteOptions</span>()</div>
<div class="block"><p>Creates a new instance.</p></div>
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
<section class="detail" id="fromDefaultParameterConfiguration()">
<h3>fromDefaultParameterConfiguration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="TransitRouteOptions.html" title="class in com.here.sdk.routing">TransitRouteOptions</a></span> <span class="element-name">fromDefaultParameterConfiguration</span>()</div>
<div class="block"><p>Returns TransitRouteOptions instance with default values used in SDK.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>An <a href="TransitRouteOptions.html" title="class in com.here.sdk.routing"><code>TransitRouteOptions</code></a> instance with default values used in SDK.</p></dd>
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

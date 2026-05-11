---
title: "Untitled"
slug: "sdk-for-android-explore-calculatetrafficonroutecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- CalculateTrafficOnRouteCallback.html -->
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
<li><a href="sdk-for-android-explore-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.routing</a></div>
<h1 class="title" title="Interface CalculateTrafficOnRouteCallback">Interface CalculateTrafficOnRouteCallback</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">CalculateTrafficOnRouteCallback</span></div>
<div class="block"><p>A function which is called by the RoutingEngine after route traffic calculation has completed.
 It is always called on the main thread.
 The first argument is the error in case of a failure. It is <code>null</code> for an operation that succeeds.
 The second argument is the calculated route traffic. It is <code>null</code> in case of an error.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onTrafficOnRouteCalculated(com.here.sdk.routing.RoutingError,com.here.sdk.routing.TrafficOnRoute)">onTrafficOnRouteCalculated</a><wbr/>(<a href="sdk-for-android-explore-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a> routingError,
 <a href="sdk-for-android-explore-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a> trafficOnRoute)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">A function which is called by the RoutingEngine after route traffic calculation has completed.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="onTrafficOnRouteCalculated(com.here.sdk.routing.RoutingError,com.here.sdk.routing.TrafficOnRoute)">
<h3>onTrafficOnRouteCalculated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onTrafficOnRouteCalculated</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-explore-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a> routingError,
 @Nullable
 <a href="sdk-for-android-explore-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a> trafficOnRoute)</span></div>
<div class="block"><p>A function which is called by the RoutingEngine after route traffic calculation has completed.
 It is always called on the main thread.
 The first argument is the error in case of a failure. It is <code>null</code> for an operation that succeeds.
 The second argument is the calculated route traffic. It is <code>null</code> in case of an error.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routingError</code> - <p>The error in case of a failure. It is <code>null</code> for an operation that succeeds.</p></dd>
<dd><code>trafficOnRoute</code> - <p>The calculated route traffic. It is <code>null</code> in case of an error.</p></dd>
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

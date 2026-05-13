---
title: "TrafficIncidentLookupCallback (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-traffic-trafficincidentlookupcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrafficIncidentLookupCallback.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-help-doc#class">Help</a></li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.traffic</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">TrafficIncidentLookupCallback</span></div>
<div class="block"><p>Callback passed to <a href="sdk-for-android-navigate-trafficengine#lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)"><code>TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback)</code></a>.
 The method will be called on the main thread when a search call has been completed.
 The first argument is the error in the case of the failure. It is <code>null</code> for an operation that succeeds.
 The second argument is the incident in the case of the success. It is <code>null</code> in case of an error.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onTrafficIncidentFetched(com.here.sdk.traffic.TrafficQueryError,com.here.sdk.traffic.TrafficIncident)">onTrafficIncidentFetched</a><wbr/>(<a href="sdk-for-android-navigate-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a> queryError,
 <a href="sdk-for-android-navigate-trafficincident" title="class in com.here.sdk.traffic">TrafficIncident</a> result)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Callback passed to <a href="sdk-for-android-navigate-trafficengine#lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)"><code>TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback)</code></a>.</div>
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

<ul class="member-list">
<li>
<section class="detail" id="onTrafficIncidentFetched(com.here.sdk.traffic.TrafficQueryError,com.here.sdk.traffic.TrafficIncident)">
<h3>onTrafficIncidentFetched</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onTrafficIncidentFetched</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a> queryError,
 @Nullable
 <a href="sdk-for-android-navigate-trafficincident" title="class in com.here.sdk.traffic">TrafficIncident</a> result)</span></div>
<div class="block"><p>Callback passed to <a href="sdk-for-android-navigate-trafficengine#lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)"><code>TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback)</code></a>.
 The method will be called on the main thread when a search call has been completed.
 The first argument is the error in the case of the failure. It is <code>null</code> for an operation that succeeds.
 The second argument is the incident in the case of the success. It is <code>null</code> in case of an error.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>queryError</code> - <p>The error in the case of the failure. It is <code>null</code> for an operation that succeeds.</p></dd>
<dd><code>result</code> - <p>The incident in the case of the success. It is <code>null</code> in case of an error.</p></dd>
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



</div>
`
}</HTMLBlock>

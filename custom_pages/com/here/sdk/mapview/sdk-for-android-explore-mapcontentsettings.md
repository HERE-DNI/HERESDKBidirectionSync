---
title: "MapContentSettings (API Reference)"
slug: "sdk-for-android-explore-mapcontentsettings"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapContentSettings.html -->
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
<li><a href="#nested-class-summary">Nested</a> | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../NativeBase.html" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapContentSettings</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapContentSettings</span>
<span class="extends-implements">extends <a href="../../NativeBase.html" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Provides settings regarding map data which are applied globally to all map views. The settings
 can already be changed before a map view instance is created.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="MapContentSettings.TrafficRefreshPeriodErrorCode.html" title="enum class in com.here.sdk.mapview">MapContentSettings.TrafficRefreshPeriodErrorCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Traffic refresh period error code</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="MapContentSettings.TrafficRefreshPeriodException.html" title="class in com.here.sdk.mapview">MapContentSettings.TrafficRefreshPeriodException</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Traffic refresh period error exception</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#filterTrafficIncidents(java.util.List)">filterTrafficIncidents</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../traffic/TrafficIncidentType.html" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a>&gt; trafficIncidents)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Filters the displayed traffic incidents so that only the ones applicable to the specified
 criteria are shown when general display of traffic incidents is enabled.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#resetTrafficIncidentFilter()">resetTrafficIncidentFilter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all filters regarding Traffic Incidents so that all incidents will be displayed,
 when the display of Traffic Incidents is enabled using <a href="MapScene.html#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a> with
 <a href="MapFeatures.html#TRAFFIC_INCIDENTS"><code>MapFeatures.TRAFFIC_INCIDENTS</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#resetTrafficRefreshPeriod()">resetTrafficRefreshPeriod</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Resets the traffic data (both flow and incidents) refresh period so the default traffic information
 validity time and the refresh period derived from the refresh period of the traffic server is used.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setTrafficRefreshPeriod(com.here.time.Duration)">setTrafficRefreshPeriod</a><wbr/>(<a href="../../time/Duration.html" title="class in com.here.time">Duration</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the traffic data refresh period for both <a href="MapFeatures.html#TRAFFIC_FLOW"><code>MapFeatures.TRAFFIC_FLOW</code></a> and
 <a href="MapFeatures.html#TRAFFIC_INCIDENTS"><code>MapFeatures.TRAFFIC_INCIDENTS</code></a>.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="filterTrafficIncidents(java.util.List)">
<h3>filterTrafficIncidents</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">filterTrafficIncidents</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../traffic/TrafficIncidentType.html" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a>&gt; trafficIncidents)</span></div>
<div class="block"><p>Filters the displayed traffic incidents so that only the ones applicable to the specified
 criteria are shown when general display of traffic incidents is enabled.
 The display of traffic incidents can be enabled using <a href="MapScene.html#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a> with
 <a href="MapFeatures.html#TRAFFIC_INCIDENTS"><code>MapFeatures.TRAFFIC_INCIDENTS</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>trafficIncidents</code> - <p>The traffic incidents to filter for, so that only applicable incidents are displayed.
     When the list is empty, then all traffic incidents will be displayed.
     If the <code>trafficIncidents</code> contains <a href="../traffic/TrafficIncidentType.html#UNKNOWN"><code>TrafficIncidentType.UNKNOWN</code></a>, then the
     traffic filter will be applied ignoring this element.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetTrafficIncidentFilter()">
<h3>resetTrafficIncidentFilter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetTrafficIncidentFilter</span>()</div>
<div class="block"><p>Removes all filters regarding Traffic Incidents so that all incidents will be displayed,
 when the display of Traffic Incidents is enabled using <a href="MapScene.html#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a> with
 <a href="MapFeatures.html#TRAFFIC_INCIDENTS"><code>MapFeatures.TRAFFIC_INCIDENTS</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="setTrafficRefreshPeriod(com.here.time.Duration)">
<h3>setTrafficRefreshPeriod</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setTrafficRefreshPeriod</span><wbr/><span class="parameters">(@NonNull
 <a href="../../time/Duration.html" title="class in com.here.time">Duration</a> value)</span>
                                    throws <span class="exceptions"><a href="MapContentSettings.TrafficRefreshPeriodException.html" title="class in com.here.sdk.mapview">MapContentSettings.TrafficRefreshPeriodException</a></span></div>
<div class="block"><p>Sets the traffic data refresh period for both <a href="MapFeatures.html#TRAFFIC_FLOW"><code>MapFeatures.TRAFFIC_FLOW</code></a> and
 <a href="MapFeatures.html#TRAFFIC_INCIDENTS"><code>MapFeatures.TRAFFIC_INCIDENTS</code></a>. By default, the traffic information
 validity time and the refresh period is derived from the refresh period of HERE's traffic server.
 The period set by this function will override the server's default setting for
 upcoming traffic data requests.
 Defaults to 60 seconds.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Traffic data refresh period in seconds. Valid range is [60, 300] seconds.
     The shortest refresh period that can be set is 60 seconds. This means that the traffic
     data shown on a map view will be refreshed every minute.
     The longest refresh period that can be set is 300 seconds. This means that the traffic
     data shown on the current map view will be refreshed every 5 minutes
     if the viewport does not change.
     Note that when a viewport change occurs, new traffic data may be requested
     regardless of the set refresh period. For example, during turn-by-turn navigation,
     frequent viewport changes can result in missing traffic data, causing new requests
     to be made more often.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="MapContentSettings.TrafficRefreshPeriodException.html" title="class in com.here.sdk.mapview">MapContentSettings.TrafficRefreshPeriodException</a></code> - <p><a href="MapContentSettings.TrafficRefreshPeriodException.html" title="class in com.here.sdk.mapview"><code>MapContentSettings.TrafficRefreshPeriodException</code></a> indicates what went wrong.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetTrafficRefreshPeriod()">
<h3>resetTrafficRefreshPeriod</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetTrafficRefreshPeriod</span>()</div>
<div class="block"><p>Resets the traffic data (both flow and incidents) refresh period so the default traffic information
 validity time and the refresh period derived from the refresh period of the traffic server is used.</p></div>
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

---
title: "Untitled"
slug: "sdk-for-android-explore-package-summary"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- package-summary.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="package-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-index">Overview</a></li>
<li class="nav-bar-cell1-rev">Package</li>
<li>Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-help-doc#package">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Package: </li>
<li>Description | </li>
<li>Related Packages | </li>
<li><a href="#class-summary">Classes and Interfaces</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<div class="header">
<h1 class="title" title="Package com.here.sdk.traffic">Package com.here.sdk.traffic</h1>
</div>
<hr/>
<div class="package-signature">package <span class="element-name">com.here.sdk.traffic</span></div>
<section class="summary">
<ul class="summary-list">
<li>
<div id="class-summary">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="class-summary.tabpanel" aria-selected="true" class="active-table-tab" id="class-summary-tab0" onclick="show('class-summary', 'class-summary', 2)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Classes and Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab1" onclick="show('class-summary', 'class-summary-tab1', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab2" onclick="show('class-summary', 'class-summary-tab2', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Classes</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab3" onclick="show('class-summary', 'class-summary-tab3', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Enum Classes</button></div>
<div aria-labelledby="class-summary-tab0" id="class-summary.tabpanel" role="tabpanel">
<div class="summary-table two-column-summary">
<div class="table-header col-first">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-junctionstraversability" title="enum class in com.here.sdk.traffic">JunctionsTraversability</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Junctions traversability of some traffic incident or flow section.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-trafficdataprovider" title="class in com.here.sdk.traffic">TrafficDataProvider</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">This interface provides traffic information from
 radio signals to other HERE SDK modules.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-trafficengine" title="class in com.here.sdk.traffic">TrafficEngine</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Use the TrafficEngine to get information about current traffic flow and incidents in an area
 specified by <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>, <a href="sdk-for-android-explore-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a>, or <a href="sdk-for-android-explore-geocorridor" title="class in com.here.sdk.core"><code>GeoCorridor</code></a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-trafficflow" title="class in com.here.sdk.traffic">TrafficFlow</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">This class provides details about traffic flow along a <a href="sdk-for-android-explore-geocorridor" title="class in com.here.sdk.core"><code>GeoCorridor</code></a>, inside a <a href="sdk-for-android-explore-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a> or a <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>, that represents particular path of the road network.<br/>
 Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.<br/>
 For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-explore-trafficflowbase" title="interface in com.here.sdk.traffic">TrafficFlowBase</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">This interface provides details about a traffic flow.<br/>
 For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="sdk-for-android-explore-trafficflowquerycallback" title="interface in com.here.sdk.traffic">TrafficFlowQueryCallback</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">Callback passed to following functions:
 <a href="sdk-for-android-explore-trafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)"><code>TrafficEngine.queryForFlow(GeoBox, TrafficFlowQueryOptions, TrafficFlowQueryCallback)</code></a>
<a href="sdk-for-android-explore-trafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)"><code>TrafficEngine.queryForFlow(GeoCircle, TrafficFlowQueryOptions, TrafficFlowQueryCallback)</code></a>
<a href="sdk-for-android-explore-trafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)"><code>TrafficEngine.queryForFlow(GeoCorridor, TrafficFlowQueryOptions, TrafficFlowQueryCallback)</code></a>
 The method will be called on the main thread when a search call has been completed.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-trafficflowqueryoptions" title="class in com.here.sdk.traffic">TrafficFlowQueryOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The options to specify how traffic flow data should be queried.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-trafficincident" title="class in com.here.sdk.traffic">TrafficIncident</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">TrafficIncident provides details about a traffic incident.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">The vehicle categories that can be restricted.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-trafficincident-vehiclerestriction" title="class in com.here.sdk.traffic">TrafficIncident.VehicleRestriction</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">The vehicle restriction representing a vehicle category and relevant restriction rules.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-explore-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">TrafficIncident provides details about a traffic incident.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-trafficincidentimpact" title="enum class in com.here.sdk.traffic">TrafficIncidentImpact</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Impact of a traffic incident.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-explore-trafficincidentlookupcallback" title="interface in com.here.sdk.traffic">TrafficIncidentLookupCallback</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">Callback passed to <a href="sdk-for-android-explore-trafficengine#lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)"><code>TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback)</code></a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-trafficincidentlookupoptions" title="class in com.here.sdk.traffic">TrafficIncidentLookupOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">All the options to specify how a single incident should be queried.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-explore-trafficincidentsquerycallback" title="interface in com.here.sdk.traffic">TrafficIncidentsQueryCallback</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">Callback passed to <a href="sdk-for-android-explore-trafficengine#queryForIncidents(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)"><code>TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback)</code></a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-trafficincidentsqueryoptions" title="class in com.here.sdk.traffic">TrafficIncidentsQueryOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">The options to specify how incidents should be queried.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Category of a traffic incident.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-trafficlocation" title="class in com.here.sdk.traffic">TrafficLocation</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">The location reference to the traffic incident.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Represents various errors that could occur from a traffic queries.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-traversability" title="enum class in com.here.sdk.traffic">Traversability</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Junctions traversability of some traffic incident or flow section.</div>
</div>
</div>
</div>
</div>
</li>
</ul>
</section>
</main>
</div>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>

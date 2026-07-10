---
title: "com.here.sdk.traffic (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-package-summary"
---

<div class="header">

</div>

<div class="package-signature">

package <span class="element-name">com.here.sdk.traffic</span>

</div>

- <div id="sdk-for-android-explore-class-summary">

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-junctionstraversability" title="enum class in com.here.sdk.traffic">JunctionsTraversability</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Junctions traversability of some traffic incident or flow section.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficdataprovider" title="class in com.here.sdk.traffic">TrafficDataProvider</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  This interface provides traffic information from radio signals to other HERE SDK modules.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficengine" title="class in com.here.sdk.traffic">TrafficEngine</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  Use the TrafficEngine to get information about current traffic flow and incidents in an area specified by GeoBox , GeoCircle , or GeoCorridor .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficflow" title="class in com.here.sdk.traffic">TrafficFlow</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  This class provides details about traffic flow along a GeoCorridor , inside a GeoCircle or a GeoBox , that represents particular path of the road network. Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data. For additional information about fields, refer to Traffic API v7 API Reference: Traffic API v7 .

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficflowbase" title="interface in com.here.sdk.traffic">TrafficFlowBase</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  This interface provides details about a traffic flow. For additional information about fields, refer to Traffic API v7 API Reference: Traffic API v7 .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficflowquerycallback" title="interface in com.here.sdk.traffic">TrafficFlowQueryCallback</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab1">

  <div class="block">

  Callback passed to following functions: TrafficEngine.queryForFlow(GeoBox, TrafficFlowQueryOptions, TrafficFlowQueryCallback) TrafficEngine.queryForFlow(GeoCircle, TrafficFlowQueryOptions, TrafficFlowQueryCallback) TrafficEngine.queryForFlow(GeoCorridor, TrafficFlowQueryOptions, TrafficFlowQueryCallback) The method will be called on the main thread when a search call has been completed.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficflowqueryoptions" title="class in com.here.sdk.traffic">TrafficFlowQueryOptions</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  The options to specify how traffic flow data should be queried.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident" title="class in com.here.sdk.traffic">TrafficIncident</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  TrafficIncident provides details about a traffic incident.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory" title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  The vehicle categories that can be restricted.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction" title="class in com.here.sdk.traffic">TrafficIncident.VehicleRestriction</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  The vehicle restriction representing a vehicle category and relevant restriction rules.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase" title="interface in com.here.sdk.traffic">TrafficIncidentBase</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  TrafficIncident provides details about a traffic incident.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentimpact" title="enum class in com.here.sdk.traffic">TrafficIncidentImpact</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Impact of a traffic incident.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentlookupcallback" title="interface in com.here.sdk.traffic">TrafficIncidentLookupCallback</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  Callback passed to TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback) .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentlookupoptions" title="class in com.here.sdk.traffic">TrafficIncidentLookupOptions</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  All the options to specify how a single incident should be queried.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentsquerycallback" title="interface in com.here.sdk.traffic">TrafficIncidentsQueryCallback</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  Callback passed to TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback) .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentsqueryoptions" title="class in com.here.sdk.traffic">TrafficIncidentsQueryOptions</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  The options to specify how incidents should be queried.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Category of a traffic incident.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficlocation" title="class in com.here.sdk.traffic">TrafficLocation</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  The location reference to the traffic incident.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Represents various errors that could occur from a traffic queries.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-traversability" title="enum class in com.here.sdk.traffic">Traversability</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Junctions traversability of some traffic incident or flow section.

  </div>

  </div>

  </div>

  </div>


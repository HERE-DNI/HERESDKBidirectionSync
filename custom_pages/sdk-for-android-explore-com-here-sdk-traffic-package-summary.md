---
title: "com.here.sdk.traffic (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-package-summary"
---

<div class="package-signature">

package <span class="element-name">com.here.sdk.traffic</span>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-class-summary">

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  [JunctionsTraversability](sdk-for-android-explore-com-here-sdk-traffic-junctionstraversability "enum class in com.here.sdk.traffic")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Junctions traversability of some traffic incident or flow section.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [TrafficDataProvider](sdk-for-android-explore-com-here-sdk-traffic-trafficdataprovider "class in com.here.sdk.traffic")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  This interface provides traffic information from radio signals to
  other HERE SDK modules.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [TrafficEngine](sdk-for-android-explore-com-here-sdk-traffic-trafficengine "class in com.here.sdk.traffic")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  Use the TrafficEngine to get information about current traffic flow
  and incidents in an area specified by GeoBox , GeoCircle , or
  GeoCorridor .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [TrafficFlow](sdk-for-android-explore-com-here-sdk-traffic-trafficflow "class in com.here.sdk.traffic")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  This class provides details about traffic flow along a GeoCorridor ,
  inside a GeoCircle or a GeoBox , that represents particular path of
  the road network. Backends for TrafficEngine and traffic vector tiles
  are different however backends may share the same data. For additional
  information about fields, refer to Traffic API v7 API Reference:
  Traffic API v7 .

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  [TrafficFlowBase](sdk-for-android-explore-com-here-sdk-traffic-trafficflowbase "interface in com.here.sdk.traffic")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  This interface provides details about a traffic flow. For additional
  information about fields, refer to Traffic API v7 API Reference:
  Traffic API v7 .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab1">

  [TrafficFlowQueryCallback](sdk-for-android-explore-com-here-sdk-traffic-trafficflowquerycallback "interface in com.here.sdk.traffic")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab1">

  <div class="block">

  Callback passed to following functions:
  TrafficEngine.queryForFlow(GeoBox, TrafficFlowQueryOptions,
  TrafficFlowQueryCallback) TrafficEngine.queryForFlow(GeoCircle,
  TrafficFlowQueryOptions, TrafficFlowQueryCallback)
  TrafficEngine.queryForFlow(GeoCorridor, TrafficFlowQueryOptions,
  TrafficFlowQueryCallback) The method will be called on the main thread
  when a search call has been completed.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [TrafficFlowQueryOptions](sdk-for-android-explore-com-here-sdk-traffic-trafficflowqueryoptions "class in com.here.sdk.traffic")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  The options to specify how traffic flow data should be queried.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [TrafficIncident](sdk-for-android-explore-com-here-sdk-traffic-trafficincident "class in com.here.sdk.traffic")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  TrafficIncident provides details about a traffic incident.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  The vehicle categories that can be restricted.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [TrafficIncident.VehicleRestriction](sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction "class in com.here.sdk.traffic")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  The vehicle restriction representing a vehicle category and relevant
  restriction rules.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  [TrafficIncidentBase](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase "interface in com.here.sdk.traffic")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  TrafficIncident provides details about a traffic incident.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  [TrafficIncidentImpact](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentimpact "enum class in com.here.sdk.traffic")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Impact of a traffic incident.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  [TrafficIncidentLookupCallback](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentlookupcallback "interface in com.here.sdk.traffic")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  Callback passed to TrafficEngine.lookupIncident(java.lang.String,
  com.here.sdk.traffic.TrafficIncidentLookupOptions,
  com.here.sdk.traffic.TrafficIncidentLookupCallback) .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [TrafficIncidentLookupOptions](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentlookupoptions "class in com.here.sdk.traffic")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  All the options to specify how a single incident should be queried.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  [TrafficIncidentsQueryCallback](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentsquerycallback "interface in com.here.sdk.traffic")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  Callback passed to TrafficEngine.queryForIncidents(GeoCorridor,
  TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback) .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [TrafficIncidentsQueryOptions](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentsqueryoptions "class in com.here.sdk.traffic")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  The options to specify how incidents should be queried.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  [TrafficIncidentType](sdk-for-android-explore-com-here-sdk-traffic-trafficincidenttype "enum class in com.here.sdk.traffic")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Category of a traffic incident.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [TrafficLocation](sdk-for-android-explore-com-here-sdk-traffic-trafficlocation "class in com.here.sdk.traffic")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  The location reference to the traffic incident.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  [TrafficQueryError](sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror "enum class in com.here.sdk.traffic")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Represents various errors that could occur from a traffic queries.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  [Traversability](sdk-for-android-explore-com-here-sdk-traffic-traversability "enum class in com.here.sdk.traffic")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Junctions traversability of some traffic incident or flow section.

  </div>

  </div>

  </div>

  </div>

</div>


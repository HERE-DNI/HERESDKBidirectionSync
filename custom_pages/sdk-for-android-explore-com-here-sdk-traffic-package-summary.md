---
title: "com.here.sdk.traffic (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-package-summary"
---

<div class="package-signature">

package <span class="element-name">com.here.sdk.traffic</span>

</div>

<div class="section summary">

- <div id="class-summary">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Classes and Interfaces
  Interfaces
  Classes
  Enum Classes

  </div>

  <div id="class-summary.tabpanel" aria-labelledby="class-summary-tab0"
  role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-junctionstraversability"
  title="enum class in com.here.sdk.traffic">JunctionsTraversability</a></td>
  <td><div class="block">
  Junctions traversability of some traffic incident or flow section.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficdataprovider"
  title="class in com.here.sdk.traffic">TrafficDataProvider</a></td>
  <td><div class="block">
  This interface provides traffic information from radio signals to other
  HERE SDK modules.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficengine"
  title="class in com.here.sdk.traffic">TrafficEngine</a></td>
  <td><div class="block">
  Use the TrafficEngine to get information about current traffic flow and
  incidents in an area specified by GeoBox , GeoCircle , or GeoCorridor .
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficflow"
  title="class in com.here.sdk.traffic">TrafficFlow</a></td>
  <td><div class="block">
  This class provides details about traffic flow along a GeoCorridor ,
  inside a GeoCircle or a GeoBox , that represents particular path of the
  road network. Backends for TrafficEngine and traffic vector tiles are
  different however backends may share the same data. For additional
  information about fields, refer to Traffic API v7 API Reference: Traffic
  API v7 .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficflowbase"
  title="interface in com.here.sdk.traffic">TrafficFlowBase</a></td>
  <td><div class="block">
  This interface provides details about a traffic flow. For additional
  information about fields, refer to Traffic API v7 API Reference: Traffic
  API v7 .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficflowquerycallback"
  title="interface in com.here.sdk.traffic">TrafficFlowQueryCallback</a></td>
  <td><div class="block">
  Callback passed to following functions:
  TrafficEngine.queryForFlow(GeoBox, TrafficFlowQueryOptions,
  TrafficFlowQueryCallback) TrafficEngine.queryForFlow(GeoCircle,
  TrafficFlowQueryOptions, TrafficFlowQueryCallback)
  TrafficEngine.queryForFlow(GeoCorridor, TrafficFlowQueryOptions,
  TrafficFlowQueryCallback) The method will be called on the main thread
  when a search call has been completed.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficflowqueryoptions"
  title="class in com.here.sdk.traffic">TrafficFlowQueryOptions</a></td>
  <td><div class="block">
  The options to specify how traffic flow data should be queried.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident"
  title="class in com.here.sdk.traffic">TrafficIncident</a></td>
  <td><div class="block">
  TrafficIncident provides details about a traffic incident.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-restrictedvehiclecategory"
  title="enum class in com.here.sdk.traffic">TrafficIncident.RestrictedVehicleCategory</a></td>
  <td><div class="block">
  The vehicle categories that can be restricted.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincident-vehiclerestriction"
  title="class in com.here.sdk.traffic">TrafficIncident.VehicleRestriction</a></td>
  <td><div class="block">
  The vehicle restriction representing a vehicle category and relevant
  restriction rules.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentbase"
  title="interface in com.here.sdk.traffic">TrafficIncidentBase</a></td>
  <td><div class="block">
  TrafficIncident provides details about a traffic incident.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentimpact"
  title="enum class in com.here.sdk.traffic">TrafficIncidentImpact</a></td>
  <td><div class="block">
  Impact of a traffic incident.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentlookupcallback"
  title="interface in com.here.sdk.traffic">TrafficIncidentLookupCallback</a></td>
  <td><div class="block">
  Callback passed to TrafficEngine.lookupIncident(java.lang.String,
  com.here.sdk.traffic.TrafficIncidentLookupOptions,
  com.here.sdk.traffic.TrafficIncidentLookupCallback) .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentlookupoptions"
  title="class in com.here.sdk.traffic">TrafficIncidentLookupOptions</a></td>
  <td><div class="block">
  All the options to specify how a single incident should be queried.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentsquerycallback"
  title="interface in com.here.sdk.traffic">TrafficIncidentsQueryCallback</a></td>
  <td><div class="block">
  Callback passed to TrafficEngine.queryForIncidents(GeoCorridor,
  TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback) .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidentsqueryoptions"
  title="class in com.here.sdk.traffic">TrafficIncidentsQueryOptions</a></td>
  <td><div class="block">
  The options to specify how incidents should be queried.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidenttype"
  title="enum class in com.here.sdk.traffic">TrafficIncidentType</a></td>
  <td><div class="block">
  Category of a traffic incident.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficlocation"
  title="class in com.here.sdk.traffic">TrafficLocation</a></td>
  <td><div class="block">
  The location reference to the traffic incident.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror"
  title="enum class in com.here.sdk.traffic">TrafficQueryError</a></td>
  <td><div class="block">
  Represents various errors that could occur from a traffic queries.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-traffic-traversability"
  title="enum class in com.here.sdk.traffic">Traversability</a></td>
  <td><div class="block">
  Junctions traversability of some traffic incident or flow section.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

</div>


---
title: "com.here.sdk.traffic (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpackage-summary"
hidden: false
---

# Package com.here.sdk.traffic

------------------------------------------------------------------------
package com.here.sdk.traffic

All Classes and Interfaces
  Interfaces
  Classes
  Enum Classes

  Class

  Description

  [JunctionsTraversability](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic")

Junctions traversability of some traffic incident or flow section.

[TrafficDataProvider](sdk-for-android-explore-api-reference-latesttrafficdataprovider "class in com.here.sdk.traffic")

This interface provides traffic information from radio signals to other HERE SDK modules.

[TrafficEngine](sdk-for-android-explore-api-reference-latesttrafficengine "class in com.here.sdk.traffic")

Use the TrafficEngine to get information about current traffic flow and incidents in an area specified by [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core"), [`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core"), or [`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core").

[TrafficFlow](sdk-for-android-explore-api-reference-latesttrafficflow "class in com.here.sdk.traffic")

This class provides details about traffic flow along a [`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core"), inside a [`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core") or a [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core"), that represents particular path of the road network.
  Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.
  For additional information about fields, refer to [Traffic API v7 API Reference: Traffic API v7](https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic).

[TrafficFlowBase](sdk-for-android-explore-api-reference-latesttrafficflowbase "interface in com.here.sdk.traffic")

This interface provides details about a traffic flow.
  For additional information about fields, refer to [Traffic API v7 API Reference: Traffic API v7](https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic).

[TrafficFlowQueryCallback](sdk-for-android-explore-api-reference-latesttrafficflowquerycallback "interface in com.here.sdk.traffic")

Callback passed to following functions: [`TrafficEngine.queryForFlow(GeoBox, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) [`TrafficEngine.queryForFlow(GeoCircle, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) [`TrafficEngine.queryForFlow(GeoCorridor, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) The method will be called on the main thread when a search call has been completed.

[TrafficFlowQueryOptions](sdk-for-android-explore-api-reference-latesttrafficflowqueryoptions "class in com.here.sdk.traffic")

The options to specify how traffic flow data should be queried.

[TrafficIncident](sdk-for-android-explore-api-reference-latesttrafficincident "class in com.here.sdk.traffic")

TrafficIncident provides details about a traffic incident.

[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")

The vehicle categories that can be restricted.

[TrafficIncident.VehicleRestriction](sdk-for-android-explore-api-reference-latesttrafficincident-vehiclerestriction "class in com.here.sdk.traffic")

The vehicle restriction representing a vehicle category and relevant restriction rules.

[TrafficIncidentBase](sdk-for-android-explore-api-reference-latesttrafficincidentbase "interface in com.here.sdk.traffic")

TrafficIncident provides details about a traffic incident.

[TrafficIncidentImpact](sdk-for-android-explore-api-reference-latesttrafficincidentimpact "enum class in com.here.sdk.traffic")

Impact of a traffic incident.

[TrafficIncidentLookupCallback](sdk-for-android-explore-api-reference-latesttrafficincidentlookupcallback "interface in com.here.sdk.traffic")

Callback passed to [`TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)).

[TrafficIncidentLookupOptions](sdk-for-android-explore-api-reference-latesttrafficincidentlookupoptions "class in com.here.sdk.traffic")

All the options to specify how a single incident should be queried.

[TrafficIncidentsQueryCallback](sdk-for-android-explore-api-reference-latesttrafficincidentsquerycallback "interface in com.here.sdk.traffic")

Callback passed to [`TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForIncidents(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)).

[TrafficIncidentsQueryOptions](sdk-for-android-explore-api-reference-latesttrafficincidentsqueryoptions "class in com.here.sdk.traffic")

The options to specify how incidents should be queried.

[TrafficIncidentType](sdk-for-android-explore-api-reference-latesttrafficincidenttype "enum class in com.here.sdk.traffic")

Category of a traffic incident.

[TrafficLocation](sdk-for-android-explore-api-reference-latesttrafficlocation "class in com.here.sdk.traffic")

The location reference to the traffic incident.

[TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic")

Represents various errors that could occur from a traffic queries.

[Traversability](sdk-for-android-explore-api-reference-latesttraversability "enum class in com.here.sdk.traffic")

Junctions traversability of some traffic incident or flow section.

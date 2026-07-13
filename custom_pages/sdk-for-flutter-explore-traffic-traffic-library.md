---
title: "traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-traffic-library"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="" data-below-sidebar="traffic/traffic-library-sidebar.html">

<div>

# <span class="kind-library">traffic</span> library

</div>

## Classes

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficdataprovider-class">TrafficDataProvider</a></span>  
This abstract class provides traffic information from radio signals to other HERE SDK modules.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficengine-class">TrafficEngine</a></span>  
Use the TrafficEngine to get information about current traffic flow and incidents in an area specified by <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>, <a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a>, or <a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a>.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflow-class">TrafficFlow</a></span>  
This class provides details about traffic flow along a <a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a>, inside a <a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a> or a <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>, that represents particular path of the road network.\
Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.\
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowbase-class">TrafficFlowBase</a></span>  
This interface provides details about a traffic flow.\
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowqueryoptions-class">TrafficFlowQueryOptions</a></span>  
The options to specify how traffic flow data should be queried.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincident-class">TrafficIncident</a></span>  
TrafficIncident provides details about a traffic incident.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentbase-class">TrafficIncidentBase</a></span>  
TrafficIncident provides details about a traffic incident.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentlookupoptions-class">TrafficIncidentLookupOptions</a></span>  
All the options to specify how a single incident should be queried.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class">TrafficIncidentsQueryOptions</a></span>  
The options to specify how incidents should be queried.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-class">TrafficIncidentVehicleRestriction</a></span>  
The vehicle restriction representing a vehicle category and relevant restriction rules.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficlocation-class">TrafficLocation</a></span>  
The location reference to the traffic incident.

## Enums

<span class="name"><a href="sdk-for-flutter-explore-traffic-junctionstraversability">JunctionsTraversability</a></span>  
Junctions traversability of some traffic incident or flow section.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentimpact">TrafficIncidentImpact</a></span>  
Impact of a traffic incident.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>  
The vehicle categories that can be restricted.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidenttype">TrafficIncidentType</a></span>  
Category of a traffic incident.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Represents various errors that could occur from a traffic queries.

<span class="name"><a href="sdk-for-flutter-explore-traffic-traversability">Traversability</a></span>  
Junctions traversability of some traffic incident or flow section.

## Typedefs

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowquerycallback">TrafficFlowQueryCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-explore-param-queryError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficqueryerror">TrafficQueryError</a>?</span> <span class="parameter-name">queryError</span>, </span><span id="sdk-for-flutter-explore-param-result" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-traffic-trafficflow-class">TrafficFlow</a></span>\></span>?</span> <span class="parameter-name">result</span></span>)</span></span> </span>  
Callback passed to following functions: <a href="sdk-for-flutter-explore-traffic-trafficengine-queryforflowinbox">TrafficEngine.queryForFlowInBox</a> <a href="sdk-for-flutter-explore-traffic-trafficengine-queryforflowincircle">TrafficEngine.queryForFlowInCircle</a> <a href="sdk-for-flutter-explore-traffic-trafficengine-queryforflowincorridor">TrafficEngine.queryForFlowInCorridor</a> The method will be called on the main thread when a search call has been completed.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentlookupcallback">TrafficIncidentLookupCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-explore-param-queryError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficqueryerror">TrafficQueryError</a>?</span> <span class="parameter-name">queryError</span>, </span><span id="sdk-for-flutter-explore-param-result" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficincident-class">TrafficIncident</a>?</span> <span class="parameter-name">result</span></span>)</span></span> </span>  
Callback passed to <a href="sdk-for-flutter-explore-traffic-trafficengine-lookupincident">TrafficEngine.lookupIncident</a>.

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentsquerycallback">TrafficIncidentsQueryCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-explore-param-queryError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficqueryerror">TrafficQueryError</a>?</span> <span class="parameter-name">queryError</span>, </span><span id="sdk-for-flutter-explore-param-result" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-traffic-trafficincident-class">TrafficIncident</a></span>\></span>?</span> <span class="parameter-name">result</span></span>)</span></span> </span>  
Callback passed to <a href="sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsincorridor">TrafficEngine.queryForIncidentsInCorridor</a>.

</div>

<!-- /.main-content --> <!--/sidebar-offcanvas-right--> <span class="no-break"> here_sdk 4.26.0 </span>


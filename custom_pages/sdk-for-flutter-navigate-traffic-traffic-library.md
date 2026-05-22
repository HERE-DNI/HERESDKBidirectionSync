---
title: "Untitled"
slug: "sdk-for-flutter-navigate-traffic-traffic-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- traffic-library.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">traffic.dart</li>
</ol>
<div class="self-name">traffic</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="" data-below-sidebar="traffic/traffic-library-sidebar.html" id="dartdoc-main-content">
<div>
<h1>traffic library</h1>
</div>
<section class="summary offset-anchor" id="classes">
<h2>Classes</h2>
<dl>
<dt id="TrafficDataProvider">
/sdk-for-flutter-navigate-traffic-trafficdataprovider-class
</dt>
<dd>
  This abstract class provides traffic information from
radio signals to other HERE SDK modules.
</dd>
<dt id="TrafficEngine">
/sdk-for-flutter-navigate-traffic-trafficengine-class
</dt>
<dd>
  Use the TrafficEngine to get information about current traffic flow and incidents in an area
specified by /sdk-for-flutter-navigate-core-geobox-class, /sdk-for-flutter-navigate-core-geocircle-class, or /sdk-for-flutter-navigate-core-geocorridor-class.
</dd>
<dt id="TrafficFlow">
/sdk-for-flutter-navigate-traffic-trafficflow-class
</dt>
<dd>
  This class provides details about traffic flow along a /sdk-for-flutter-navigate-core-geocorridor-class, inside a /sdk-for-flutter-navigate-core-geocircle-class or a /sdk-for-flutter-navigate-core-geobox-class, that represents particular path of the road network.<br/>
Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.<br/>
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.
</dd>
<dt id="TrafficFlowBase">
/sdk-for-flutter-navigate-traffic-trafficflowbase-class
</dt>
<dd>
  This interface provides details about a traffic flow.<br/>
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.
</dd>
<dt id="TrafficFlowQueryOptions">
/sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-class
</dt>
<dd>
  The options to specify how traffic flow data should be queried.
</dd>
<dt id="TrafficIncident">
/sdk-for-flutter-navigate-traffic-trafficincident-class
</dt>
<dd>
  TrafficIncident provides details about a traffic incident.
</dd>
<dt id="TrafficIncidentBase">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-class
</dt>
<dd>
  TrafficIncident provides details about a traffic incident.
</dd>
<dt id="TrafficIncidentLookupOptions">
/sdk-for-flutter-navigate-traffic-trafficincidentlookupoptions-class
</dt>
<dd>
  All the options to specify how a single incident should be queried.
</dd>
<dt id="TrafficIncidentsQueryOptions">
/sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-class
</dt>
<dd>
  The options to specify how incidents should be queried.
</dd>
<dt id="TrafficIncidentVehicleRestriction">
/sdk-for-flutter-navigate-traffic-trafficincidentvehiclerestriction-class
</dt>
<dd>
  The vehicle restriction representing a vehicle category and relevant restriction rules.
</dd>
<dt id="TrafficLocation">
/sdk-for-flutter-navigate-traffic-trafficlocation-class
</dt>
<dd>
  The location reference to the traffic incident.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="enums">
<h2>Enums</h2>
<dl>
<dt id="JunctionsTraversability">
/sdk-for-flutter-navigate-traffic-junctionstraversability
</dt>
<dd>
  Junctions traversability of some traffic incident or flow section.
</dd>
<dt id="TrafficIncidentImpact">
/sdk-for-flutter-navigate-traffic-trafficincidentimpact
</dt>
<dd>
  Impact of a traffic incident.
</dd>
<dt id="TrafficIncidentRestrictedVehicleCategory">
/sdk-for-flutter-navigate-traffic-trafficincidentrestrictedvehiclecategory
</dt>
<dd>
  The vehicle categories that can be restricted.
</dd>
<dt id="TrafficIncidentType">
/sdk-for-flutter-navigate-traffic-trafficincidenttype
</dt>
<dd>
  Category of a traffic incident.
</dd>
<dt id="TrafficQueryError">
/sdk-for-flutter-navigate-traffic-trafficqueryerror
</dt>
<dd>
  Represents various errors that could occur from a traffic queries.
</dd>
<dt id="Traversability">
/sdk-for-flutter-navigate-traffic-traversability
</dt>
<dd>
  Junctions traversability of some traffic incident or flow section.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="typedefs">
<h2>Typedefs</h2>
<dl>
<dt class="callable" id="TrafficFlowQueryCallback">
/sdk-for-flutter-navigate-traffic-trafficflowquerycallback
= void Function(/sdk-for-flutter-navigate-traffic-trafficqueryerror? queryError, List&lt;<wbr/>/sdk-for-flutter-navigate-traffic-trafficflow-class&gt;? result)

</dt>
<dd>
    Callback passed to following functions:
/sdk-for-flutter-navigate-traffic-trafficengine-queryforflowinbox
/sdk-for-flutter-navigate-traffic-trafficengine-queryforflowincircle
/sdk-for-flutter-navigate-traffic-trafficengine-queryforflowincorridor
The method will be called on the main thread when a search call has been completed.
    

  </dd>
<dt class="callable" id="TrafficIncidentLookupCallback">
/sdk-for-flutter-navigate-traffic-trafficincidentlookupcallback
= void Function(/sdk-for-flutter-navigate-traffic-trafficqueryerror? queryError, /sdk-for-flutter-navigate-traffic-trafficincident-class? result)

</dt>
<dd>
    Callback passed to /sdk-for-flutter-navigate-traffic-trafficengine-lookupincident.
    

  </dd>
<dt class="callable" id="TrafficIncidentsQueryCallback">
/sdk-for-flutter-navigate-traffic-trafficincidentsquerycallback
= void Function(/sdk-for-flutter-navigate-traffic-trafficqueryerror? queryError, List&lt;<wbr/>/sdk-for-flutter-navigate-traffic-trafficincident-class&gt;? result)

</dt>
<dd>
    Callback passed to /sdk-for-flutter-navigate-traffic-trafficengine-queryforincidentsincorridor.
    

  </dd>
</dl>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">traffic.dart</li>
</ol>
<h5>here_sdk package</h5>
<ol>
<li class="section-title">Libraries</li>
<li>/sdk-for-flutter-navigate-animation-animation-library</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-errors-core-errors-library</li>
<li>/sdk-for-flutter-navigate-core-threading-core-threading-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-ev-ev-library</li>
<li>/sdk-for-flutter-navigate-gestures-gestures-library</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library</li>
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-library</li>
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li>/sdk-for-flutter-navigate-venue-venue-library</li>
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li>/sdk-for-flutter-navigate-venue-data-venue-data-library</li>
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li>/sdk-for-flutter-navigate-venue-service-venue-service-library</li>
<li>/sdk-for-flutter-navigate-venue-style-venue-style-library</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
</ol>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
<h5>traffic library</h5>
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>

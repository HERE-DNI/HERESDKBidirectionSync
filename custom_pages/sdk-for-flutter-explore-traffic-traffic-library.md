---
title: "traffic library"
slug: "sdk-for-flutter-explore-traffic-traffic-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- traffic-library.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="traffic/traffic-library.html#classes">Classes</a></li>
<li><a href="traffic/TrafficDataProvider-class.html">TrafficDataProvider</a></li>
<li><a href="traffic/TrafficEngine-class.html">TrafficEngine</a></li>
<li><a href="traffic/TrafficFlow-class.html">TrafficFlow</a></li>
<li><a href="traffic/TrafficFlowBase-class.html">TrafficFlowBase</a></li>
<li><a href="traffic/TrafficFlowQueryOptions-class.html">TrafficFlowQueryOptions</a></li>
<li><a href="traffic/TrafficIncident-class.html">TrafficIncident</a></li>
<li><a href="traffic/TrafficIncidentBase-class.html">TrafficIncidentBase</a></li>
<li><a href="traffic/TrafficIncidentLookupOptions-class.html">TrafficIncidentLookupOptions</a></li>
<li><a href="traffic/TrafficIncidentsQueryOptions-class.html">TrafficIncidentsQueryOptions</a></li>
<li><a href="traffic/TrafficIncidentVehicleRestriction-class.html">TrafficIncidentVehicleRestriction</a></li>
<li><a href="traffic/TrafficLocation-class.html">TrafficLocation</a></li>
<li class="section-title"><a href="traffic/traffic-library.html#enums">Enums</a></li>
<li><a href="traffic/JunctionsTraversability.html">JunctionsTraversability</a></li>
<li><a href="traffic/TrafficIncidentImpact.html">TrafficIncidentImpact</a></li>
<li><a href="traffic/TrafficIncidentRestrictedVehicleCategory.html">TrafficIncidentRestrictedVehicleCategory</a></li>
<li><a href="traffic/TrafficIncidentType.html">TrafficIncidentType</a></li>
<li><a href="traffic/TrafficQueryError.html">TrafficQueryError</a></li>
<li><a href="traffic/Traversability.html">Traversability</a></li>
<li class="section-title"><a href="traffic/traffic-library.html#typedefs">Typedefs</a></li>
<li><a href="traffic/TrafficFlowQueryCallback.html">TrafficFlowQueryCallback</a></li>
<li><a href="traffic/TrafficIncidentLookupCallback.html">TrafficIncidentLookupCallback</a></li>
<li><a href="traffic/TrafficIncidentsQueryCallback.html">TrafficIncidentsQueryCallback</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
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
/sdk-for-flutter-explore-traffic-trafficdataprovider-class
</dt>
<dd>
  This abstract class provides traffic information from
radio signals to other HERE SDK modules.
</dd>
<dt id="TrafficEngine">
/sdk-for-flutter-explore-traffic-trafficengine-class
</dt>
<dd>
  Use the TrafficEngine to get information about current traffic flow and incidents in an area
specified by /sdk-for-flutter-explore-core-geobox-class, /sdk-for-flutter-explore-core-geocircle-class, or /sdk-for-flutter-explore-core-geocorridor-class.
</dd>
<dt id="TrafficFlow">
/sdk-for-flutter-explore-traffic-trafficflow-class
</dt>
<dd>
  This class provides details about traffic flow along a /sdk-for-flutter-explore-core-geocorridor-class, inside a /sdk-for-flutter-explore-core-geocircle-class or a /sdk-for-flutter-explore-core-geobox-class, that represents particular path of the road network.<br/>
Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.<br/>
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.
</dd>
<dt id="TrafficFlowBase">
/sdk-for-flutter-explore-traffic-trafficflowbase-class
</dt>
<dd>
  This interface provides details about a traffic flow.<br/>
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.
</dd>
<dt id="TrafficFlowQueryOptions">
/sdk-for-flutter-explore-traffic-trafficflowqueryoptions-class
</dt>
<dd>
  The options to specify how traffic flow data should be queried.
</dd>
<dt id="TrafficIncident">
/sdk-for-flutter-explore-traffic-trafficincident-class
</dt>
<dd>
  TrafficIncident provides details about a traffic incident.
</dd>
<dt id="TrafficIncidentBase">
/sdk-for-flutter-explore-traffic-trafficincidentbase-class
</dt>
<dd>
  TrafficIncident provides details about a traffic incident.
</dd>
<dt id="TrafficIncidentLookupOptions">
/sdk-for-flutter-explore-traffic-trafficincidentlookupoptions-class
</dt>
<dd>
  All the options to specify how a single incident should be queried.
</dd>
<dt id="TrafficIncidentsQueryOptions">
/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class
</dt>
<dd>
  The options to specify how incidents should be queried.
</dd>
<dt id="TrafficIncidentVehicleRestriction">
/sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-class
</dt>
<dd>
  The vehicle restriction representing a vehicle category and relevant restriction rules.
</dd>
<dt id="TrafficLocation">
/sdk-for-flutter-explore-traffic-trafficlocation-class
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
/sdk-for-flutter-explore-traffic-junctionstraversability
</dt>
<dd>
  Junctions traversability of some traffic incident or flow section.
</dd>
<dt id="TrafficIncidentImpact">
/sdk-for-flutter-explore-traffic-trafficincidentimpact
</dt>
<dd>
  Impact of a traffic incident.
</dd>
<dt id="TrafficIncidentRestrictedVehicleCategory">
/sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory
</dt>
<dd>
  The vehicle categories that can be restricted.
</dd>
<dt id="TrafficIncidentType">
/sdk-for-flutter-explore-traffic-trafficincidenttype
</dt>
<dd>
  Category of a traffic incident.
</dd>
<dt id="TrafficQueryError">
/sdk-for-flutter-explore-traffic-trafficqueryerror
</dt>
<dd>
  Represents various errors that could occur from a traffic queries.
</dd>
<dt id="Traversability">
/sdk-for-flutter-explore-traffic-traversability
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
/sdk-for-flutter-explore-traffic-trafficflowquerycallback
= void Function(/sdk-for-flutter-explore-traffic-trafficqueryerror? queryError, List&lt;<wbr/>/sdk-for-flutter-explore-traffic-trafficflow-class&gt;? result)

</dt>
<dd>
    Callback passed to following functions:
/sdk-for-flutter-explore-traffic-trafficengine-queryforflowinbox
/sdk-for-flutter-explore-traffic-trafficengine-queryforflowincircle
/sdk-for-flutter-explore-traffic-trafficengine-queryforflowincorridor
The method will be called on the main thread when a search call has been completed.
    

  </dd>
<dt class="callable" id="TrafficIncidentLookupCallback">
/sdk-for-flutter-explore-traffic-trafficincidentlookupcallback
= void Function(/sdk-for-flutter-explore-traffic-trafficqueryerror? queryError, /sdk-for-flutter-explore-traffic-trafficincident-class? result)

</dt>
<dd>
    Callback passed to /sdk-for-flutter-explore-traffic-trafficengine-lookupincident.
    

  </dd>
<dt class="callable" id="TrafficIncidentsQueryCallback">
/sdk-for-flutter-explore-traffic-trafficincidentsquerycallback
= void Function(/sdk-for-flutter-explore-traffic-trafficqueryerror? queryError, List&lt;<wbr/>/sdk-for-flutter-explore-traffic-trafficincident-class&gt;? result)

</dt>
<dd>
    Callback passed to /sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsincorridor.
    

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
<li>/sdk-for-flutter-explore</li>
<li class="self-crumb">traffic.dart</li>
</ol>
<h5>here_sdk package</h5>
<ol>
<li class="section-title">Libraries</li>
<li>/sdk-for-flutter-explore-animation-animation-library</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-errors-core-errors-library</li>
<li>/sdk-for-flutter-explore-core-threading-core-threading-library</li>
<li>/sdk-for-flutter-explore-ev-ev-library</li>
<li>/sdk-for-flutter-explore-gestures-gestures-library</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
<li>/sdk-for-flutter-explore-transport-transport-library</li>
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
</div></div>
</div>
`
}</HTMLBlock>

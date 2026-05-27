---
title: "Classes"
slug: "sdk-for-flutter-explore-traffic-traffic-library"
---

<HTMLBlock>
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
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
<a href="../traffic/TrafficDataProvider-class.html">/sdk-for-flutter-explore-traffic-trafficdataprovider-class</a>
</dt>
<dd>
  This abstract class provides traffic information from
radio signals to other HERE SDK modules.
</dd>
<dt id="TrafficEngine">
<a href="../traffic/TrafficEngine-class.html">/sdk-for-flutter-explore-traffic-trafficengine-class</a>
</dt>
<dd>
  Use the TrafficEngine to get information about current traffic flow and incidents in an area
specified by <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>, <a href="../core/GeoCircle-class.html">/sdk-for-flutter-explore-core-geocircle-class</a>, or <a href="../core/GeoCorridor-class.html">/sdk-for-flutter-explore-core-geocorridor-class</a>.
</dd>
<dt id="TrafficFlow">
<a href="../traffic/TrafficFlow-class.html">/sdk-for-flutter-explore-traffic-trafficflow-class</a>
</dt>
<dd>
  This class provides details about traffic flow along a <a href="../core/GeoCorridor-class.html">/sdk-for-flutter-explore-core-geocorridor-class</a>, inside a <a href="../core/GeoCircle-class.html">/sdk-for-flutter-explore-core-geocircle-class</a> or a <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>, that represents particular path of the road network.<br/>
Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.<br/>
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.
</dd>
<dt id="TrafficFlowBase">
<a href="../traffic/TrafficFlowBase-class.html">/sdk-for-flutter-explore-traffic-trafficflowbase-class</a>
</dt>
<dd>
  This interface provides details about a traffic flow.<br/>
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.
</dd>
<dt id="TrafficFlowQueryOptions">
<a href="../traffic/TrafficFlowQueryOptions-class.html">/sdk-for-flutter-explore-traffic-trafficflowqueryoptions-class</a>
</dt>
<dd>
  The options to specify how traffic flow data should be queried.
</dd>
<dt id="TrafficIncident">
<a href="../traffic/TrafficIncident-class.html">/sdk-for-flutter-explore-traffic-trafficincident-class</a>
</dt>
<dd>
  TrafficIncident provides details about a traffic incident.
</dd>
<dt id="TrafficIncidentBase">
<a href="../traffic/TrafficIncidentBase-class.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-class</a>
</dt>
<dd>
  TrafficIncident provides details about a traffic incident.
</dd>
<dt id="TrafficIncidentLookupOptions">
<a href="../traffic/TrafficIncidentLookupOptions-class.html">/sdk-for-flutter-explore-traffic-trafficincidentlookupoptions-class</a>
</dt>
<dd>
  All the options to specify how a single incident should be queried.
</dd>
<dt id="TrafficIncidentsQueryOptions">
<a href="../traffic/TrafficIncidentsQueryOptions-class.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class</a>
</dt>
<dd>
  The options to specify how incidents should be queried.
</dd>
<dt id="TrafficIncidentVehicleRestriction">
<a href="../traffic/TrafficIncidentVehicleRestriction-class.html">/sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-class</a>
</dt>
<dd>
  The vehicle restriction representing a vehicle category and relevant restriction rules.
</dd>
<dt id="TrafficLocation">
<a href="../traffic/TrafficLocation-class.html">/sdk-for-flutter-explore-traffic-trafficlocation-class</a>
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
<a href="../traffic/JunctionsTraversability.html">/sdk-for-flutter-explore-traffic-junctionstraversability</a>
</dt>
<dd>
  Junctions traversability of some traffic incident or flow section.
</dd>
<dt id="TrafficIncidentImpact">
<a href="../traffic/TrafficIncidentImpact.html">/sdk-for-flutter-explore-traffic-trafficincidentimpact</a>
</dt>
<dd>
  Impact of a traffic incident.
</dd>
<dt id="TrafficIncidentRestrictedVehicleCategory">
<a href="../traffic/TrafficIncidentRestrictedVehicleCategory.html">/sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory</a>
</dt>
<dd>
  The vehicle categories that can be restricted.
</dd>
<dt id="TrafficIncidentType">
<a href="../traffic/TrafficIncidentType.html">/sdk-for-flutter-explore-traffic-trafficincidenttype</a>
</dt>
<dd>
  Category of a traffic incident.
</dd>
<dt id="TrafficQueryError">
<a href="../traffic/TrafficQueryError.html">/sdk-for-flutter-explore-traffic-trafficqueryerror</a>
</dt>
<dd>
  Represents various errors that could occur from a traffic queries.
</dd>
<dt id="Traversability">
<a href="../traffic/Traversability.html">/sdk-for-flutter-explore-traffic-traversability</a>
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
<a href="../traffic/TrafficFlowQueryCallback.html">/sdk-for-flutter-explore-traffic-trafficflowquerycallback</a>
= void Function(<a href="../traffic/TrafficQueryError.html">/sdk-for-flutter-explore-traffic-trafficqueryerror</a>? queryError, List&lt;<wbr/><a href="../traffic/TrafficFlow-class.html">/sdk-for-flutter-explore-traffic-trafficflow-class</a>&gt;? result)

</dt>
<dd>
    Callback passed to following functions:
<a href="../traffic/TrafficEngine/queryForFlowInBox.html">/sdk-for-flutter-explore-traffic-trafficengine-queryforflowinbox</a>
<a href="../traffic/TrafficEngine/queryForFlowInCircle.html">/sdk-for-flutter-explore-traffic-trafficengine-queryforflowincircle</a>
<a href="../traffic/TrafficEngine/queryForFlowInCorridor.html">/sdk-for-flutter-explore-traffic-trafficengine-queryforflowincorridor</a>
The method will be called on the main thread when a search call has been completed.
    

  </dd>
<dt class="callable" id="TrafficIncidentLookupCallback">
<a href="../traffic/TrafficIncidentLookupCallback.html">/sdk-for-flutter-explore-traffic-trafficincidentlookupcallback</a>
= void Function(<a href="../traffic/TrafficQueryError.html">/sdk-for-flutter-explore-traffic-trafficqueryerror</a>? queryError, <a href="../traffic/TrafficIncident-class.html">/sdk-for-flutter-explore-traffic-trafficincident-class</a>? result)

</dt>
<dd>
    Callback passed to <a href="../traffic/TrafficEngine/lookupIncident.html">/sdk-for-flutter-explore-traffic-trafficengine-lookupincident</a>.
    

  </dd>
<dt class="callable" id="TrafficIncidentsQueryCallback">
<a href="../traffic/TrafficIncidentsQueryCallback.html">/sdk-for-flutter-explore-traffic-trafficincidentsquerycallback</a>
= void Function(<a href="../traffic/TrafficQueryError.html">/sdk-for-flutter-explore-traffic-trafficqueryerror</a>? queryError, List&lt;<wbr/><a href="../traffic/TrafficIncident-class.html">/sdk-for-flutter-explore-traffic-trafficincident-class</a>&gt;? result)

</dt>
<dd>
    Callback passed to <a href="../traffic/TrafficEngine/queryForIncidentsInCorridor.html">/sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsincorridor</a>.
    

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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li class="self-crumb">traffic.dart</li>
</ol>
<h5>here_sdk package</h5>
<ol>
<li class="section-title">Libraries</li>
<li><a href="../animation/animation-library.html">/sdk-for-flutter-explore-animation-animation-library</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li><a href="../core.errors/core.errors-library.html">/sdk-for-flutter-explore-core-errors-core-errors-library</a></li>
<li><a href="../core.threading/core.threading-library.html">/sdk-for-flutter-explore-core-threading-core-threading-library</a></li>
<li><a href="../ev/ev-library.html">/sdk-for-flutter-explore-ev-ev-library</a></li>
<li><a href="../gestures/gestures-library.html">/sdk-for-flutter-explore-gestures-gestures-library</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../traffic/traffic-library.html">/sdk-for-flutter-explore-traffic-traffic-library</a></li>
<li><a href="../transport/transport-library.html">/sdk-for-flutter-explore-transport-transport-library</a></li>
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
</HTMLBlock>

---
title: "Constructors"
slug: "sdk-for-flutter-explore-traffic-trafficengine-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- TrafficEngine-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="traffic/TrafficEngine-class.html#constructors">Constructors</a></li>
<li><a href="traffic/TrafficEngine/TrafficEngine.html">TrafficEngine</a></li>
<li><a href="traffic/TrafficEngine/TrafficEngine.withSdkEngine.html">withSdkEngine</a></li>
<li class="section-title inherited">
<a href="traffic/TrafficEngine-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="traffic/TrafficEngine/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="traffic/TrafficEngine/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="traffic/TrafficEngine-class.html#instance-methods">Methods</a></li>
<li><a href="traffic/TrafficEngine/lookupIncident.html">lookupIncident</a></li>
<li class="inherited"><a href="traffic/TrafficEngine/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="traffic/TrafficEngine/queryForFlowInBox.html">queryForFlowInBox</a></li>
<li><a href="traffic/TrafficEngine/queryForFlowInCircle.html">queryForFlowInCircle</a></li>
<li><a href="traffic/TrafficEngine/queryForFlowInCorridor.html">queryForFlowInCorridor</a></li>
<li><a href="traffic/TrafficEngine/queryForIncidentsInBox.html">queryForIncidentsInBox</a></li>
<li><a href="traffic/TrafficEngine/queryForIncidentsInCircle.html">queryForIncidentsInCircle</a></li>
<li><a href="traffic/TrafficEngine/queryForIncidentsInCorridor.html">queryForIncidentsInCorridor</a></li>
<li class="inherited"><a href="traffic/TrafficEngine/toString.html">toString</a></li>
<li class="section-title inherited"><a href="traffic/TrafficEngine-class.html#operators">Operators</a></li>
<li class="inherited"><a href="traffic/TrafficEngine/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../traffic/traffic-library.html">/sdk-for-flutter-explore-traffic-traffic-library</a></li>
<li class="self-crumb">TrafficEngine class</li>
</ol>
<div class="self-name">TrafficEngine</div>
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
<div class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrafficEngine class abstract</h1></div>
<section class="desc markdown">
<p>Use the TrafficEngine to get information about current traffic flow and incidents in an area
specified by <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>, <a href="../core/GeoCircle-class.html">/sdk-for-flutter-explore-core-geocircle-class</a>, or <a href="../core/GeoCorridor-class.html">/sdk-for-flutter-explore-core-geocorridor-class</a>.</p>
<p>Provides optional parameters given in <a href="../traffic/TrafficIncidentsQueryOptions-class.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class</a> and <a href="../traffic/TrafficFlowQueryOptions-class.html">/sdk-for-flutter-explore-traffic-trafficflowqueryoptions-class</a> to filter the result.</p>
<p>By default, incidents are localized based on their geographical
location. You can override that behavior by specifying the
desired language that should be used for the incidents description and summary.</p>
<p>The resulting traffic data contains information on incident
types such as congestion, construction for road works, road hazard,
road closure, weather updates for road condition, lane restriction
and others.</p>
<p>Traffic data is fetched online to get the most precise and freshest data available.
In offline mode, live traffic data can be fetched using the traffic pass-through features.
See <a href="../core.engine/SDKNativeEngine/passThroughFeatures.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-passthroughfeatures</a></p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficEngine">
<a href="../traffic/TrafficEngine/TrafficEngine.html">/sdk-for-flutter-explore-traffic-trafficengine-trafficengine</a>()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="TrafficEngine.withSdkEngine">
<a href="../traffic/TrafficEngine/TrafficEngine.withSdkEngine.html">/sdk-for-flutter-explore-traffic-trafficengine-trafficengine-withsdkengine</a>(<a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a> sdkEngine)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../traffic/TrafficEngine/hashCode.html">/sdk-for-flutter-explore-traffic-trafficengine-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../traffic/TrafficEngine/runtimeType.html">/sdk-for-flutter-explore-traffic-trafficengine-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="lookupIncident">
<a href="../traffic/TrafficEngine/lookupIncident.html">/sdk-for-flutter-explore-traffic-trafficengine-lookupincident</a>(<wbr/>String originalId, <a href="../traffic/TrafficIncidentLookupOptions-class.html">/sdk-for-flutter-explore-traffic-trafficincidentlookupoptions-class</a> lookupOptions, <a href="../traffic/TrafficIncidentLookupCallback.html">/sdk-for-flutter-explore-traffic-trafficincidentlookupcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously queries for traffic incident by the original id.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../traffic/TrafficEngine/noSuchMethod.html">/sdk-for-flutter-explore-traffic-trafficengine-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="queryForFlowInBox">
<a href="../traffic/TrafficEngine/queryForFlowInBox.html">/sdk-for-flutter-explore-traffic-trafficengine-queryforflowinbox</a>(<wbr/><a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> boxArea, <a href="../traffic/TrafficFlowQueryOptions-class.html">/sdk-for-flutter-explore-traffic-trafficflowqueryoptions-class</a> queryOptions, <a href="../traffic/TrafficFlowQueryCallback.html">/sdk-for-flutter-explore-traffic-trafficflowquerycallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously queries for traffic flow using a bounding box as a filter.
  

</dd>
<dt class="callable" id="queryForFlowInCircle">
<a href="../traffic/TrafficEngine/queryForFlowInCircle.html">/sdk-for-flutter-explore-traffic-trafficengine-queryforflowincircle</a>(<wbr/><a href="../core/GeoCircle-class.html">/sdk-for-flutter-explore-core-geocircle-class</a> circleArea, <a href="../traffic/TrafficFlowQueryOptions-class.html">/sdk-for-flutter-explore-traffic-trafficflowqueryoptions-class</a> queryOptions, <a href="../traffic/TrafficFlowQueryCallback.html">/sdk-for-flutter-explore-traffic-trafficflowquerycallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously queries for traffic flow using a circle as a filter.
  

</dd>
<dt class="callable" id="queryForFlowInCorridor">
<a href="../traffic/TrafficEngine/queryForFlowInCorridor.html">/sdk-for-flutter-explore-traffic-trafficengine-queryforflowincorridor</a>(<wbr/><a href="../core/GeoCorridor-class.html">/sdk-for-flutter-explore-core-geocorridor-class</a> corridorArea, <a href="../traffic/TrafficFlowQueryOptions-class.html">/sdk-for-flutter-explore-traffic-trafficflowqueryoptions-class</a> queryOptions, <a href="../traffic/TrafficFlowQueryCallback.html">/sdk-for-flutter-explore-traffic-trafficflowquerycallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously queries for traffic flow by a corridor as a filter.
  

</dd>
<dt class="callable" id="queryForIncidentsInBox">
<a href="../traffic/TrafficEngine/queryForIncidentsInBox.html">/sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsinbox</a>(<wbr/><a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> boxArea, <a href="../traffic/TrafficIncidentsQueryOptions-class.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class</a> queryOptions, <a href="../traffic/TrafficIncidentsQueryCallback.html">/sdk-for-flutter-explore-traffic-trafficincidentsquerycallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously queries for traffic incidents using a bounding box as a filter.
  

</dd>
<dt class="callable" id="queryForIncidentsInCircle">
<a href="../traffic/TrafficEngine/queryForIncidentsInCircle.html">/sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsincircle</a>(<wbr/><a href="../core/GeoCircle-class.html">/sdk-for-flutter-explore-core-geocircle-class</a> circleArea, <a href="../traffic/TrafficIncidentsQueryOptions-class.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class</a> queryOptions, <a href="../traffic/TrafficIncidentsQueryCallback.html">/sdk-for-flutter-explore-traffic-trafficincidentsquerycallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously queries for traffic incidents using a circle as a filter.
  

</dd>
<dt class="callable" id="queryForIncidentsInCorridor">
<a href="../traffic/TrafficEngine/queryForIncidentsInCorridor.html">/sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsincorridor</a>(<wbr/><a href="../core/GeoCorridor-class.html">/sdk-for-flutter-explore-core-geocorridor-class</a> corridorArea, <a href="../traffic/TrafficIncidentsQueryOptions-class.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class</a> queryOptions, <a href="../traffic/TrafficIncidentsQueryCallback.html">/sdk-for-flutter-explore-traffic-trafficincidentsquerycallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously queries for traffic incidents by a corridor as a filter.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../traffic/TrafficEngine/toString.html">/sdk-for-flutter-explore-traffic-trafficengine-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../traffic/TrafficEngine/operator_equals.html">/sdk-for-flutter-explore-traffic-trafficengine-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
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
<li><a href="../traffic/traffic-library.html">/sdk-for-flutter-explore-traffic-traffic-library</a></li>
<li class="self-crumb">TrafficEngine class</li>
</ol>
<h5>traffic library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>

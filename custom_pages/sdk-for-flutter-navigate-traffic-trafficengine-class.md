---
title: "Untitled"
slug: "sdk-for-flutter-navigate-traffic-trafficengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficEngine-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
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
specified by /sdk-for-flutter-navigate-core-geobox-class, /sdk-for-flutter-navigate-core-geocircle-class, or /sdk-for-flutter-navigate-core-geocorridor-class.</p>
<p>Provides optional parameters given in /sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-class and /sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-class to filter the result.</p>
<p>By default, incidents are localized based on their geographical
location. You can override that behavior by specifying the
desired language that should be used for the incidents description and summary.</p>
<p>The resulting traffic data contains information on incident
types such as congestion, construction for road works, road hazard,
road closure, weather updates for road condition, lane restriction
and others.</p>
<p>Traffic data is fetched online to get the most precise and freshest data available.
In offline mode, live traffic data can be fetched using the traffic pass-through features.
See /sdk-for-flutter-navigate-core-engine-sdknativeengine-passthroughfeatures</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficEngine">
/sdk-for-flutter-navigate-traffic-trafficengine-trafficengine()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="TrafficEngine.withSdkEngine">
/sdk-for-flutter-navigate-traffic-trafficengine-trafficengine-withsdkengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
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
/sdk-for-flutter-navigate-traffic-trafficengine-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-traffic-trafficengine-runtimetype
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
/sdk-for-flutter-navigate-traffic-trafficengine-lookupincident(<wbr/>String originalId, /sdk-for-flutter-navigate-traffic-trafficincidentlookupoptions-class lookupOptions, /sdk-for-flutter-navigate-traffic-trafficincidentlookupcallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously queries for traffic incident by the original id.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-traffic-trafficengine-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="queryForFlowInBox">
/sdk-for-flutter-navigate-traffic-trafficengine-queryforflowinbox(<wbr/>/sdk-for-flutter-navigate-core-geobox-class boxArea, /sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-class queryOptions, /sdk-for-flutter-navigate-traffic-trafficflowquerycallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously queries for traffic flow using a bounding box as a filter.
  

</dd>
<dt class="callable" id="queryForFlowInCircle">
/sdk-for-flutter-navigate-traffic-trafficengine-queryforflowincircle(<wbr/>/sdk-for-flutter-navigate-core-geocircle-class circleArea, /sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-class queryOptions, /sdk-for-flutter-navigate-traffic-trafficflowquerycallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously queries for traffic flow using a circle as a filter.
  

</dd>
<dt class="callable" id="queryForFlowInCorridor">
/sdk-for-flutter-navigate-traffic-trafficengine-queryforflowincorridor(<wbr/>/sdk-for-flutter-navigate-core-geocorridor-class corridorArea, /sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-class queryOptions, /sdk-for-flutter-navigate-traffic-trafficflowquerycallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously queries for traffic flow by a corridor as a filter.
  

</dd>
<dt class="callable" id="queryForIncidentsInBox">
/sdk-for-flutter-navigate-traffic-trafficengine-queryforincidentsinbox(<wbr/>/sdk-for-flutter-navigate-core-geobox-class boxArea, /sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-class queryOptions, /sdk-for-flutter-navigate-traffic-trafficincidentsquerycallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously queries for traffic incidents using a bounding box as a filter.
  

</dd>
<dt class="callable" id="queryForIncidentsInCircle">
/sdk-for-flutter-navigate-traffic-trafficengine-queryforincidentsincircle(<wbr/>/sdk-for-flutter-navigate-core-geocircle-class circleArea, /sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-class queryOptions, /sdk-for-flutter-navigate-traffic-trafficincidentsquerycallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously queries for traffic incidents using a circle as a filter.
  

</dd>
<dt class="callable" id="queryForIncidentsInCorridor">
/sdk-for-flutter-navigate-traffic-trafficengine-queryforincidentsincorridor(<wbr/>/sdk-for-flutter-navigate-core-geocorridor-class corridorArea, /sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-class queryOptions, /sdk-for-flutter-navigate-traffic-trafficincidentsquerycallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously queries for traffic incidents by a corridor as a filter.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-traffic-trafficengine-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-traffic-trafficengine-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
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



</div>
`
}</HTMLBlock>

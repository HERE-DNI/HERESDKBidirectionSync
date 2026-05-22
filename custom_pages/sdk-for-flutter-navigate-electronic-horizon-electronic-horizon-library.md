---
title: "Untitled"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- electronic_horizon-library.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">electronic_horizon.dart</li>
</ol>
<div class="self-name">electronic_horizon</div>
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
<div class="main-content" data-above-sidebar="" data-below-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html" id="dartdoc-main-content">
<div>
<h1>electronic_horizon library</h1>
</div>
<section class="summary offset-anchor" id="classes">
<h2>Classes</h2>
<dl>
<dt id="ElectronicHorizon">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizon-class
</dt>
<dd>
  A class containing the full set of available paths
predicted for the current vehicle state.
</dd>
<dt id="ElectronicHorizonDataLoader">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-class
</dt>
<dd>
  Loads map data for segments that belong to the /sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-class paths.
</dd>
<dt id="ElectronicHorizonDataLoaderResult">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderresult-class
</dt>
<dd>
  Represents the result of a data loading operation performed by /sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-class.
</dd>
<dt id="ElectronicHorizonDataLoaderStatusListener">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderstatuslistener-class
</dt>
<dd>
  Provides a listener for status updates from the /sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-loaddata method.
</dd>
<dt id="ElectronicHorizonEngine">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-class
</dt>
<dd>
  Provides an electronic horizon engine that continuously predicts
the road network ahead of the vehicle by using detailed map data, including road topography that is
currently out of sight.
</dd>
<dt id="ElectronicHorizonListener">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class
</dt>
<dd>
  Provides a listener for receiving updates during execution of the /sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-update method.
</dd>
<dt id="ElectronicHorizonOptions">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-class
</dt>
<dd>
  Provides options to configure /sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-class.
</dd>
<dt id="ElectronicHorizonPath">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-class
</dt>
<dd>
  Represents a single electronic horizon path.
</dd>
<dt id="ElectronicHorizonPosition">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonposition-class
</dt>
<dd>
  Provides a position on an electronic horizon path with a reference to the current item in the /sdk-for-flutter-navigate-electronic-horizon-electronichorizon-class.
</dd>
<dt id="ElectronicHorizonSegment">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegment-class
</dt>
<dd>
  Represents a segment in an /sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-class.
</dd>
<dt id="ElectronicHorizonSegmentChanges">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegmentchanges-class
</dt>
<dd>
  A class describing the set of changes in horizon segments
between two consecutive updates.
</dd>
<dt id="ElectronicHorizonSegmentId">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegmentid-class
</dt>
<dd>
  Identifies a segment in an /sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-class.
</dd>
<dt id="ElectronicHorizonUpdate">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-class
</dt>
<dd>
  A class representing a full update delivered via /sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class notifications.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="enums">
<h2>Enums</h2>
<dl>
<dt id="ElectronicHorizonDataLoadedStatus">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloadedstatus
</dt>
<dd>
  Represents the status of data that was loaded by /sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-class.
</dd>
<dt id="ElectronicHorizonDataLoaderErrorCode">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloadererrorcode
</dt>
<dd>
  Represents error codes that describe the result of the /sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-getsegment method.
</dd>
<dt id="ElectronicHorizonErrorCode">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonerrorcode
</dt>
<dd>
  Represents error codes that describe the result of the /sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-update method.
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
<li class="self-crumb">electronic_horizon.dart</li>
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
<h5>electronic_horizon library</h5>
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>

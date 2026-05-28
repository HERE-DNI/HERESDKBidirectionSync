---
title: "location library"
slug: "sdk-for-flutter-navigate-location-location-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- location-library.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="location/location-library.html#classes">Classes</a></li>
<li><a href="location/CellularPositioningOptions-class.html">CellularPositioningOptions</a></li>
<li><a href="location/LocationEngine-class.html">LocationEngine</a></li>
<li><a href="location/LocationEngineBase-class.html">LocationEngineBase</a></li>
<li><a href="location/LocationIssueListener-class.html">LocationIssueListener</a></li>
<li><a href="location/LocationOptions-class.html">LocationOptions</a></li>
<li><a href="location/LocationStatusListener-class.html">LocationStatusListener</a></li>
<li><a href="location/NotificationOptions-class.html">NotificationOptions</a></li>
<li><a href="location/SatellitePositioningOptions-class.html">SatellitePositioningOptions</a></li>
<li><a href="location/SensorOptions-class.html">SensorOptions</a></li>
<li><a href="location/WifiPositioningOptions-class.html">WifiPositioningOptions</a></li>
<li class="section-title"><a href="location/location-library.html#enums">Enums</a></li>
<li><a href="location/ConfirmationStatus.html">ConfirmationStatus</a></li>
<li><a href="location/LocationAccuracy.html">LocationAccuracy</a></li>
<li><a href="location/LocationEngineStatus.html">LocationEngineStatus</a></li>
<li><a href="location/LocationFeature.html">LocationFeature</a></li>
<li><a href="location/LocationIssueType.html">LocationIssueType</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">location.dart</li>
</ol>
<div class="self-name">location</div>
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
<div class="main-content" data-above-sidebar="" data-below-sidebar="location/location-library-sidebar.html" id="dartdoc-main-content">
<div>
<h1>location library</h1>
</div>
<section class="summary offset-anchor" id="classes">
<h2>Classes</h2>
<dl>
<dt id="CellularPositioningOptions">
/sdk-for-flutter-navigate-location-cellularpositioningoptions-class
</dt>
<dd>
  Cellular positioning options.
</dd>
<dt id="LocationEngine">
/sdk-for-flutter-navigate-location-locationengine-class
</dt>
<dd>
  Handles location updates received according to the desired /sdk-for-flutter-navigate-location-locationaccuracy or /sdk-for-flutter-navigate-location-locationoptions-class.
</dd>
<dt id="LocationEngineBase">
/sdk-for-flutter-navigate-location-locationenginebase-class
</dt>
<dd>
  Public abstract class that describes the behaviour of <code>LocationEngine</code>.
</dd>
<dt id="LocationIssueListener">
/sdk-for-flutter-navigate-location-locationissuelistener-class
</dt>
<dd>
  abstract class receiving notifications when the set of
currently active location issues changes.
</dd>
<dt id="LocationOptions">
/sdk-for-flutter-navigate-location-locationoptions-class
</dt>
<dd>
  Location options that combine notification, sensor, cellular positioning, GNSS positioning and WiFi positioning options.
</dd>
<dt id="LocationStatusListener">
/sdk-for-flutter-navigate-location-locationstatuslistener-class
</dt>
<dd>
  Abstract class for listening the
LocationEngine status updates.
</dd>
<dt id="NotificationOptions">
/sdk-for-flutter-navigate-location-notificationoptions-class
</dt>
<dd>
  Positioning notification options.
</dd>
<dt id="SatellitePositioningOptions">
/sdk-for-flutter-navigate-location-satellitepositioningoptions-class
</dt>
<dd>
  GNSS positioning options.
</dd>
<dt id="SensorOptions">
/sdk-for-flutter-navigate-location-sensoroptions-class
</dt>
<dd>
  Options for controlling sensor usage in positioning.
</dd>
<dt id="WifiPositioningOptions">
/sdk-for-flutter-navigate-location-wifipositioningoptions-class
</dt>
<dd>
  Wi-Fi positioning options.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="enums">
<h2>Enums</h2>
<dl>
<dt id="ConfirmationStatus">
/sdk-for-flutter-navigate-location-confirmationstatus
</dt>
<dd>
  Confirmation action specific status codes.
</dd>
<dt id="LocationAccuracy">
/sdk-for-flutter-navigate-location-locationaccuracy
</dt>
<dd>
  Indicates the desired location accuracy, however the actual accuracy is not
guaranteed.
</dd>
<dt id="LocationEngineStatus">
/sdk-for-flutter-navigate-location-locationenginestatus
</dt>
<dd>
  Indicates the status of the LocationEngine.
</dd>
<dt id="LocationFeature">
/sdk-for-flutter-navigate-location-locationfeature
</dt>
<dd>
  Location features supported by HERE positioning.
</dd>
<dt id="LocationIssueType">
/sdk-for-flutter-navigate-location-locationissuetype
</dt>
<dd>
  Represents specific issues affecting location retrieval quality, availability, or functionality.
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
<li class="self-crumb">location.dart</li>
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
<h5>location library</h5>
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

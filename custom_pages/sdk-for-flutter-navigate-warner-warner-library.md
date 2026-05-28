---
title: "warner library"
slug: "sdk-for-flutter-navigate-warner-warner-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- warner-library.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="warner/warner-library.html#classes">Classes</a></li>
<li><a href="warner/CustomWarning-class.html">CustomWarning</a></li>
<li><a href="warner/CustomWarningProvider-class.html">CustomWarningProvider</a></li>
<li><a href="warner/LaneDecreaseWarning-class.html">LaneDecreaseWarning</a></li>
<li><a href="warner/LaneDecreaseWarningOptions-class.html">LaneDecreaseWarningOptions</a></li>
<li><a href="warner/WarnerEngine-class.html">WarnerEngine</a></li>
<li><a href="warner/Warning-class.html">Warning</a></li>
<li><a href="warner/WarningListener-class.html">WarningListener</a></li>
<li><a href="warner/WarningOptions-class.html">WarningOptions</a></li>
<li><a href="warner/WarningsRegistry-class.html">WarningsRegistry</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">warner.dart</li>
</ol>
<div class="self-name">warner</div>
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
<div class="main-content" data-above-sidebar="" data-below-sidebar="warner/warner-library-sidebar.html" id="dartdoc-main-content">
<div>
<h1>warner library</h1>
</div>
<section class="summary offset-anchor" id="classes">
<h2>Classes</h2>
<dl>
<dt id="CustomWarning">
/sdk-for-flutter-navigate-warner-customwarning-class
</dt>
<dd>
  class container for custom warning data.
</dd>
<dt id="CustomWarningProvider">
/sdk-for-flutter-navigate-warner-customwarningprovider-class
</dt>
<dd>
  A abstract class representing a provider of custom warnings based on vehicle position.
</dd>
<dt id="LaneDecreaseWarning">
/sdk-for-flutter-navigate-warner-lanedecreasewarning-class
</dt>
<dd>
  Represents a lane decrease warning that notifies about upcoming reductions in the number of available lanes.
</dd>
<dt id="LaneDecreaseWarningOptions">
/sdk-for-flutter-navigate-warner-lanedecreasewarningoptions-class
</dt>
<dd>
  A class that provides lane decrease warning options.
</dd>
<dt id="WarnerEngine">
/sdk-for-flutter-navigate-warner-warnerengine-class
</dt>
<dd>
  Provides the core functionality for generating and managing navigation warnings.
</dd>
<dt id="Warning">
/sdk-for-flutter-navigate-warner-warning-class
</dt>
<dd>
  A class which represents a warning.
</dd>
<dt id="WarningListener">
/sdk-for-flutter-navigate-warner-warninglistener-class
</dt>
<dd>
  A generic listener interface abstract class for receiving warning notifications.
</dd>
<dt id="WarningOptions">
/sdk-for-flutter-navigate-warner-warningoptions-class
</dt>
<dd>
  A class with options to configure /sdk-for-flutter-navigate-warner-warnerengine-warningoptions
</dd>
<dt id="WarningsRegistry">
/sdk-for-flutter-navigate-warner-warningsregistry-class
</dt>
<dd>
  A class that store warning metadata for different warning types.
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
<li class="self-crumb">warner.dart</li>
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
<h5>warner library</h5>
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

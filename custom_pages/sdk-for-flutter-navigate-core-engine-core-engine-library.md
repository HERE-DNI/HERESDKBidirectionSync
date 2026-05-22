---
title: "Untitled"
slug: "sdk-for-flutter-navigate-core-engine-core-engine-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- core.engine-library.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">core.engine.dart</li>
</ol>
<div class="self-name">core.engine</div>
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
<div class="main-content" data-above-sidebar="" data-below-sidebar="core.engine/core.engine-library-sidebar.html" id="dartdoc-main-content">
<div>
<h1>core.engine library</h1>
</div>
<section class="summary offset-anchor" id="classes">
<h2>Classes</h2>
<dl>
<dt id="AuthenticationMode">
/sdk-for-flutter-navigate-core-engine-authenticationmode-class
</dt>
<dd>
  This is a bearer authentication mode which adds or does not add a
header ("Authorization", "Bearer $Token") to each online request of the
module the object is added to.
</dd>
<dt id="CatalogConfiguration">
/sdk-for-flutter-navigate-core-engine-catalogconfiguration-class
</dt>
<dd>
  Using this class you can configure in the /sdk-for-flutter-navigate-core-engine-sdkoptions-class,
how the /sdk-for-flutter-navigate-core-engine-sdknativeengine-class should access, use and store the data for the desired catalog.
</dd>
<dt id="CatalogIdentifier">
/sdk-for-flutter-navigate-core-engine-catalogidentifier-class
</dt>
<dd>
  This class is used to identify any catalog in the HERE platform.
</dd>
<dt id="CatalogVersionHint">
/sdk-for-flutter-navigate-core-engine-catalogversionhint-class
</dt>
<dd>
  This is a class for capturing user's intent for the
desired catalog version to use in /sdk-for-flutter-navigate-core-engine-desiredcatalog-class class.
</dd>
<dt id="CertificateSettings">
/sdk-for-flutter-navigate-core-engine-certificatesettings-class
</dt>
<dd>
  Certificate settings to be used by Curl+OpenSSL for authority only on Android
</dd>
<dt id="DesiredCatalog">
/sdk-for-flutter-navigate-core-engine-desiredcatalog-class
</dt>
<dd>
  This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access.
</dd>
<dt id="EngineOptions">
/sdk-for-flutter-navigate-core-engine-engineoptions-class
</dt>
<dd>
  Specifies several options specific to different engines.
</dd>
<dt id="LayerConfiguration">
/sdk-for-flutter-navigate-core-engine-layerconfiguration-class
</dt>
<dd>
  A class to configure which layers should be enabled or disabled in the OCM map data.
</dd>
<dt id="LockingProcess">
/sdk-for-flutter-navigate-core-engine-lockingprocess-class
</dt>
<dd>
  LockingProcess helps to detect situations when cache is locked with another process and
attempt to create instance of /sdk-for-flutter-navigate-core-engine-sdknativeengine-class fails with error
/sdk-for-flutter-navigate-core-errors-instantiationerrorcode.
</dd>
<dt id="LogAppender">
/sdk-for-flutter-navigate-core-engine-logappender-class
</dt>
<dd>
  An interface to implement a listener to receive log messages.
</dd>
<dt id="LogControl">
/sdk-for-flutter-navigate-core-engine-logcontrol-class
</dt>
<dd>
  This class provides functionality to enable/disable console logs as well as
setting a custom log appender to receive log messages from the SDK.
</dd>
<dt id="NetworkSettings">
/sdk-for-flutter-navigate-core-engine-networksettings-class
</dt>
<dd>
  Network configuration to be used by /sdk-for-flutter-navigate-core-engine-sdknativeengine-class during the initialization.
</dd>
<dt id="ProxySettings">
/sdk-for-flutter-navigate-core-engine-proxysettings-class
</dt>
<dd>
  Proxy configuration for the HERE SDK network that is applied per request.
</dd>
<dt id="ProxySettingsCredentials">
/sdk-for-flutter-navigate-core-engine-proxysettingscredentials-class
</dt>
<dd>
  Authentication data
</dd>
<dt id="SDKBuildInformation">
/sdk-for-flutter-navigate-core-engine-sdkbuildinformation-class
</dt>
<dd>
  The SDKBuildInformation class is designed to provide information about the SDK build.
</dd>
<dt id="SDKDartInfo">
/sdk-for-flutter-navigate-core-engine-sdkdartinfo-class
</dt>
<dd>
  Accessor for SDK Dart version.
</dd>
<dt id="SDKLogger">
/sdk-for-flutter-navigate-core-engine-sdklogger-class
</dt>
<dd>
  Logging interface for Android/iOS platforms.
</dd>
<dt id="SDKNativeEngine">
/sdk-for-flutter-navigate-core-engine-sdknativeengine-class
</dt>
<dd>
  Holds internal services and configurations needed by various HERE SDK modules.
</dd>
<dt id="SDKOptions">
/sdk-for-flutter-navigate-core-engine-sdkoptions-class
</dt>
<dd>
  SDKOptions provide an alternative way to set or update the HERE SDK credentials and other
parameters at runtime to initialize the /sdk-for-flutter-navigate-core-engine-sdknativeengine-class.
</dd>
<dt id="SDKVersion">
/sdk-for-flutter-navigate-core-engine-sdkversion-class
</dt>
<dd>
  The <code>SDKVersion</code> represents version information for an SDK product.
</dd>
<dt id="UsageStats">
/sdk-for-flutter-navigate-core-engine-usagestats-class
</dt>
<dd>
  A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.
</dd>
<dt id="UsageStatsNetworkStats">
/sdk-for-flutter-navigate-core-engine-usagestatsnetworkstats-class
</dt>
<dd>
  Provides network statistics in bytes per method.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="enums">
<h2>Enums</h2>
<dl>
<dt id="CatalogType">
/sdk-for-flutter-navigate-core-engine-catalogtype
</dt>
<dd>
  Represents default HERE catalog types.
</dd>
<dt id="EngineBaseURL">
/sdk-for-flutter-navigate-core-engine-enginebaseurl
</dt>
<dd>
  Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.
</dd>
<dt id="LayerConfigurationFeature">
/sdk-for-flutter-navigate-core-engine-layerconfigurationfeature
</dt>
<dd>
  Defines a list of possible map data features that can be enabled / disabled.
</dd>
<dt id="LogLevel">
/sdk-for-flutter-navigate-core-engine-loglevel
</dt>
<dd>
  Severity levels for log messages.
</dd>
<dt id="PassThroughFeature">
/sdk-for-flutter-navigate-core-engine-passthroughfeature
</dt>
<dd>
  Represents features that are allowed to consume online data when the HERE SDK's offline mode
is activated via /sdk-for-flutter-navigate-core-engine-sdknativeengine-isofflinemode and/or
/sdk-for-flutter-navigate-core-engine-sdkoptions-offlinemode.
</dd>
<dt id="ProxySettingsProxyType">
/sdk-for-flutter-navigate-core-engine-proxysettingsproxytype
</dt>
<dd>
  Supported types of proxy connection.
</dd>
<dt id="SDKNativeEnginePurgeMemoryStrategy">
/sdk-for-flutter-navigate-core-engine-sdknativeenginepurgememorystrategy
</dt>
<dd>
  Enum representing a strategy to flush memory caches.
</dd>
<dt id="SDKOptionsActionOnCacheLock">
/sdk-for-flutter-navigate-core-engine-sdkoptionsactiononcachelock
</dt>
<dd>
  Action on cache lock
</dd>
<dt id="UsageStatsFeature">
/sdk-for-flutter-navigate-core-engine-usagestatsfeature
</dt>
<dd>
  Represents the feature enum associated with the gathered usage stats.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="typedefs">
<h2>Typedefs</h2>
<dl>
<dt class="callable" id="AuthenticationModeAccessTokenProvider">
/sdk-for-flutter-navigate-core-engine-authenticationmodeaccesstokenprovider
= String? Function()

</dt>
<dd>
    This lambda is used to retrieve access token in synchronous manner.
    

  </dd>
<dt class="callable" id="DeviceIdCallback">
/sdk-for-flutter-navigate-core-engine-deviceidcallback
= void Function(String deviceId)

</dt>
<dd>
    This method will be called on the main thread when /sdk-for-flutter-navigate-core-engine-sdknativeengine-getdeviceid has been completed.
    

  </dd>
</dl>
</section>
<section class="summary offset-anchor" id="exceptions">
<h2>Exceptions / Errors</h2>
<dl>
<dt id="LogControlInvalidPathExceptionException">
/sdk-for-flutter-navigate-core-engine-logcontrolinvalidpathexceptionexception-class
</dt>
<dd>
  Invalid file path exception.
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
<li class="self-crumb">core.engine.dart</li>
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
<h5>core.engine library</h5>
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>

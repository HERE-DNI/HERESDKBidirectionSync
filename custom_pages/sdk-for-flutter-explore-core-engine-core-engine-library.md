---
title: "Classes"
slug: "sdk-for-flutter-explore-core-engine-core-engine-library"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- core.engine-library.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/core.engine-library.html#classes">Classes</a></li>
<li><a href="core.engine/AuthenticationMode-class.html">AuthenticationMode</a></li>
<li><a href="core.engine/CatalogConfiguration-class.html">CatalogConfiguration</a></li>
<li><a href="core.engine/CatalogIdentifier-class.html">CatalogIdentifier</a></li>
<li><a href="core.engine/CatalogVersionHint-class.html">CatalogVersionHint</a></li>
<li><a href="core.engine/CertificateSettings-class.html">CertificateSettings</a></li>
<li><a href="core.engine/DesiredCatalog-class.html">DesiredCatalog</a></li>
<li><a href="core.engine/EngineOptions-class.html">EngineOptions</a></li>
<li><a href="core.engine/LayerConfiguration-class.html">LayerConfiguration</a></li>
<li><a href="core.engine/LockingProcess-class.html">LockingProcess</a></li>
<li><a href="core.engine/LogAppender-class.html">LogAppender</a></li>
<li><a href="core.engine/LogControl-class.html">LogControl</a></li>
<li><a href="core.engine/NetworkSettings-class.html">NetworkSettings</a></li>
<li><a href="core.engine/ProxySettings-class.html">ProxySettings</a></li>
<li><a href="core.engine/ProxySettingsCredentials-class.html">ProxySettingsCredentials</a></li>
<li><a href="core.engine/SDKBuildInformation-class.html">SDKBuildInformation</a></li>
<li><a href="core.engine/SDKDartInfo-class.html">SDKDartInfo</a></li>
<li><a href="core.engine/SDKLogger-class.html">SDKLogger</a></li>
<li><a href="core.engine/SDKNativeEngine-class.html">SDKNativeEngine</a></li>
<li><a href="core.engine/SDKOptions-class.html">SDKOptions</a></li>
<li><a href="core.engine/SDKVersion-class.html">SDKVersion</a></li>
<li><a href="core.engine/UsageStats-class.html">UsageStats</a></li>
<li><a href="core.engine/UsageStatsNetworkStats-class.html">UsageStatsNetworkStats</a></li>
<li class="section-title"><a href="core.engine/core.engine-library.html#enums">Enums</a></li>
<li><a href="core.engine/CatalogType.html">CatalogType</a></li>
<li><a href="core.engine/EngineBaseURL.html">EngineBaseURL</a></li>
<li><a href="core.engine/LayerConfigurationFeature.html">LayerConfigurationFeature</a></li>
<li><a href="core.engine/LogLevel.html">LogLevel</a></li>
<li><a href="core.engine/PassThroughFeature.html">PassThroughFeature</a></li>
<li><a href="core.engine/ProxySettingsProxyType.html">ProxySettingsProxyType</a></li>
<li><a href="core.engine/SDKNativeEnginePurgeMemoryStrategy.html">SDKNativeEnginePurgeMemoryStrategy</a></li>
<li><a href="core.engine/SDKOptionsActionOnCacheLock.html">SDKOptionsActionOnCacheLock</a></li>
<li><a href="core.engine/UsageStatsFeature.html">UsageStatsFeature</a></li>
<li class="section-title"><a href="core.engine/core.engine-library.html#typedefs">Typedefs</a></li>
<li><a href="core.engine/AuthenticationModeAccessTokenProvider.html">AuthenticationModeAccessTokenProvider</a></li>
<li><a href="core.engine/DeviceIdCallback.html">DeviceIdCallback</a></li>
<li class="section-title"><a href="core.engine/core.engine-library.html#exceptions">Exceptions</a></li>
<li><a href="core.engine/LogControlInvalidPathExceptionException-class.html">LogControlInvalidPathExceptionException</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
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
<a href="../core.engine/AuthenticationMode-class.html">/sdk-for-flutter-explore-core-engine-authenticationmode-class</a>
</dt>
<dd>
  This is a bearer authentication mode which adds or does not add a
header ("Authorization", "Bearer $Token") to each online request of the
module the object is added to.
</dd>
<dt id="CatalogConfiguration">
<a href="../core.engine/CatalogConfiguration-class.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-class</a>
</dt>
<dd>
  Using this class you can configure in the <a href="../core.engine/SDKOptions-class.html">/sdk-for-flutter-explore-core-engine-sdkoptions-class</a>,
how the <a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a> should access, use and store the data for the desired catalog.
</dd>
<dt id="CatalogIdentifier">
<a href="../core.engine/CatalogIdentifier-class.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-class</a>
</dt>
<dd>
  This class is used to identify any catalog in the HERE platform.
</dd>
<dt id="CatalogVersionHint">
<a href="../core.engine/CatalogVersionHint-class.html">/sdk-for-flutter-explore-core-engine-catalogversionhint-class</a>
</dt>
<dd>
  This is a class for capturing user's intent for the
desired catalog version to use in <a href="../core.engine/DesiredCatalog-class.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-class</a> class.
</dd>
<dt id="CertificateSettings">
<a href="../core.engine/CertificateSettings-class.html">/sdk-for-flutter-explore-core-engine-certificatesettings-class</a>
</dt>
<dd>
  Certificate settings to be used by Curl+OpenSSL for authority only on Android
</dd>
<dt id="DesiredCatalog">
<a href="../core.engine/DesiredCatalog-class.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-class</a>
</dt>
<dd>
  This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access.
</dd>
<dt id="EngineOptions">
<a href="../core.engine/EngineOptions-class.html">/sdk-for-flutter-explore-core-engine-engineoptions-class</a>
</dt>
<dd>
  Specifies several options specific to different engines.
</dd>
<dt id="LayerConfiguration">
<a href="../core.engine/LayerConfiguration-class.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-class</a>
</dt>
<dd>
  A class to configure which layers should be enabled or disabled in the OCM map data.
</dd>
<dt id="LockingProcess">
<a href="../core.engine/LockingProcess-class.html">/sdk-for-flutter-explore-core-engine-lockingprocess-class</a>
</dt>
<dd>
  LockingProcess helps to detect situations when cache is locked with another process and
attempt to create instance of <a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a> fails with error
<a href="../core.errors/InstantiationErrorCode.html">/sdk-for-flutter-explore-core-errors-instantiationerrorcode</a>.
</dd>
<dt id="LogAppender">
<a href="../core.engine/LogAppender-class.html">/sdk-for-flutter-explore-core-engine-logappender-class</a>
</dt>
<dd>
  An interface to implement a listener to receive log messages.
</dd>
<dt id="LogControl">
<a href="../core.engine/LogControl-class.html">/sdk-for-flutter-explore-core-engine-logcontrol-class</a>
</dt>
<dd>
  This class provides functionality to enable/disable console logs as well as
setting a custom log appender to receive log messages from the SDK.
</dd>
<dt id="NetworkSettings">
<a href="../core.engine/NetworkSettings-class.html">/sdk-for-flutter-explore-core-engine-networksettings-class</a>
</dt>
<dd>
  Network configuration to be used by <a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a> during the initialization.
</dd>
<dt id="ProxySettings">
<a href="../core.engine/ProxySettings-class.html">/sdk-for-flutter-explore-core-engine-proxysettings-class</a>
</dt>
<dd>
  Proxy configuration for the HERE SDK network that is applied per request.
</dd>
<dt id="ProxySettingsCredentials">
<a href="../core.engine/ProxySettingsCredentials-class.html">/sdk-for-flutter-explore-core-engine-proxysettingscredentials-class</a>
</dt>
<dd>
  Authentication data
</dd>
<dt id="SDKBuildInformation">
<a href="../core.engine/SDKBuildInformation-class.html">/sdk-for-flutter-explore-core-engine-sdkbuildinformation-class</a>
</dt>
<dd>
  The SDKBuildInformation class is designed to provide information about the SDK build.
</dd>
<dt id="SDKDartInfo">
<a href="../core.engine/SDKDartInfo-class.html">/sdk-for-flutter-explore-core-engine-sdkdartinfo-class</a>
</dt>
<dd>
  Accessor for SDK Dart version.
</dd>
<dt id="SDKLogger">
<a href="../core.engine/SDKLogger-class.html">/sdk-for-flutter-explore-core-engine-sdklogger-class</a>
</dt>
<dd>
  Logging interface for Android/iOS platforms.
</dd>
<dt id="SDKNativeEngine">
<a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a>
</dt>
<dd>
  Holds internal services and configurations needed by various HERE SDK modules.
</dd>
<dt id="SDKOptions">
<a href="../core.engine/SDKOptions-class.html">/sdk-for-flutter-explore-core-engine-sdkoptions-class</a>
</dt>
<dd>
  SDKOptions provide an alternative way to set or update the HERE SDK credentials and other
parameters at runtime to initialize the <a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a>.
</dd>
<dt id="SDKVersion">
<a href="../core.engine/SDKVersion-class.html">/sdk-for-flutter-explore-core-engine-sdkversion-class</a>
</dt>
<dd>
  The <code>SDKVersion</code> represents version information for an SDK product.
</dd>
<dt id="UsageStats">
<a href="../core.engine/UsageStats-class.html">/sdk-for-flutter-explore-core-engine-usagestats-class</a>
</dt>
<dd>
  A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.
</dd>
<dt id="UsageStatsNetworkStats">
<a href="../core.engine/UsageStatsNetworkStats-class.html">/sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-class</a>
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
<a href="../core.engine/CatalogType.html">/sdk-for-flutter-explore-core-engine-catalogtype</a>
</dt>
<dd>
  Represents default HERE catalog types.
</dd>
<dt id="EngineBaseURL">
<a href="../core.engine/EngineBaseURL.html">/sdk-for-flutter-explore-core-engine-enginebaseurl</a>
</dt>
<dd>
  Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.
</dd>
<dt id="LayerConfigurationFeature">
<a href="../core.engine/LayerConfigurationFeature.html">/sdk-for-flutter-explore-core-engine-layerconfigurationfeature</a>
</dt>
<dd>
  Defines a list of possible map data features that can be enabled / disabled.
</dd>
<dt id="LogLevel">
<a href="../core.engine/LogLevel.html">/sdk-for-flutter-explore-core-engine-loglevel</a>
</dt>
<dd>
  Severity levels for log messages.
</dd>
<dt id="PassThroughFeature">
<a href="../core.engine/PassThroughFeature.html">/sdk-for-flutter-explore-core-engine-passthroughfeature</a>
</dt>
<dd>
  Represents features that are allowed to consume online data when the HERE SDK's offline mode
is activated via <a href="../core.engine/SDKNativeEngine/isOfflineMode.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-isofflinemode</a> and/or
<a href="../core.engine/SDKOptions/offlineMode.html">/sdk-for-flutter-explore-core-engine-sdkoptions-offlinemode</a>.
</dd>
<dt id="ProxySettingsProxyType">
<a href="../core.engine/ProxySettingsProxyType.html">/sdk-for-flutter-explore-core-engine-proxysettingsproxytype</a>
</dt>
<dd>
  Supported types of proxy connection.
</dd>
<dt id="SDKNativeEnginePurgeMemoryStrategy">
<a href="../core.engine/SDKNativeEnginePurgeMemoryStrategy.html">/sdk-for-flutter-explore-core-engine-sdknativeenginepurgememorystrategy</a>
</dt>
<dd>
  Enum representing a strategy to flush memory caches.
</dd>
<dt id="SDKOptionsActionOnCacheLock">
<a href="../core.engine/SDKOptionsActionOnCacheLock.html">/sdk-for-flutter-explore-core-engine-sdkoptionsactiononcachelock</a>
</dt>
<dd>
  Action on cache lock
</dd>
<dt id="UsageStatsFeature">
<a href="../core.engine/UsageStatsFeature.html">/sdk-for-flutter-explore-core-engine-usagestatsfeature</a>
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
<a href="../core.engine/AuthenticationModeAccessTokenProvider.html">/sdk-for-flutter-explore-core-engine-authenticationmodeaccesstokenprovider</a>
= String? Function()

</dt>
<dd>
    This lambda is used to retrieve access token in synchronous manner.
    

  </dd>
<dt class="callable" id="DeviceIdCallback">
<a href="../core.engine/DeviceIdCallback.html">/sdk-for-flutter-explore-core-engine-deviceidcallback</a>
= void Function(String deviceId)

</dt>
<dd>
    This method will be called on the main thread when <a href="../core.engine/SDKNativeEngine/getDeviceId.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-getdeviceid</a> has been completed.
    

  </dd>
</dl>
</section>
<section class="summary offset-anchor" id="exceptions">
<h2>Exceptions / Errors</h2>
<dl>
<dt id="LogControlInvalidPathExceptionException">
<a href="../core.engine/LogControlInvalidPathExceptionException-class.html">/sdk-for-flutter-explore-core-engine-logcontrolinvalidpathexceptionexception-class</a>
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li class="self-crumb">core.engine.dart</li>
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
<h5>core.engine library</h5>
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>

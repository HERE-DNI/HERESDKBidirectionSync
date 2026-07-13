---
title: "core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-core-engine-library"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="" data-below-sidebar="core.engine/core.engine-library-sidebar.html">

<div>

# <span class="kind-library">core.engine</span> library

</div>

## Classes

<span class="name"><a href="sdk-for-flutter-explore-core-engine-authenticationmode-class">AuthenticationMode</a></span>  
This is a bearer authentication mode which adds or does not add a header ("Authorization", "Bearer \$Token") to each online request of the module the object is added to.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-class">CatalogConfiguration</a></span>  
Using this class you can configure in the <a href="sdk-for-flutter-explore-core-engine-sdkoptions-class">SDKOptions</a>, how the <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-class">SDKNativeEngine</a> should access, use and store the data for the desired catalog.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogidentifier-class">CatalogIdentifier</a></span>  
This class is used to identify any catalog in the HERE platform.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogversionhint-class">CatalogVersionHint</a></span>  
This is a class for capturing user's intent for the desired catalog version to use in <a href="sdk-for-flutter-explore-core-engine-desiredcatalog-class">DesiredCatalog</a> class.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-certificatesettings-class">CertificateSettings</a></span>  
Certificate settings to be used by Curl+OpenSSL for authority only on Android

<span class="name"><a href="sdk-for-flutter-explore-core-engine-desiredcatalog-class">DesiredCatalog</a></span>  
This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-engineoptions-class">EngineOptions</a></span>  
Specifies several options specific to different engines.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-layerconfiguration-class">LayerConfiguration</a></span>  
A class to configure which layers should be enabled or disabled in the OCM map data.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-lockingprocess-class">LockingProcess</a></span>  
LockingProcess helps to detect situations when cache is locked with another process and attempt to create instance of <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-class">SDKNativeEngine</a> fails with error <a href="sdk-for-flutter-explore-core-errors-instantiationerrorcode">InstantiationErrorCode.failedToLockCacheFolder</a>.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-logappender-class">LogAppender</a></span>  
An interface to implement a listener to receive log messages.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-logcontrol-class">LogControl</a></span>  
This class provides functionality to enable/disable console logs as well as setting a custom log appender to receive log messages from the SDK.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-networksettings-class">NetworkSettings</a></span>  
Network configuration to be used by <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-class">SDKNativeEngine</a> during the initialization.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettings-class">ProxySettings</a></span>  
Proxy configuration for the HERE SDK network that is applied per request.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettingscredentials-class">ProxySettingsCredentials</a></span>  
Authentication data

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdkbuildinformation-class">SDKBuildInformation</a></span>  
The SDKBuildInformation class is designed to provide information about the SDK build.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdkdartinfo-class">SDKDartInfo</a></span>  
Accessor for SDK Dart version.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdklogger-class">SDKLogger</a></span>  
Logging interface for Android/iOS platforms.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdknativeengine-class">SDKNativeEngine</a></span>  
Holds internal services and configurations needed by various HERE SDK modules.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdkoptions-class">SDKOptions</a></span>  
SDKOptions provide an alternative way to set or update the HERE SDK credentials and other parameters at runtime to initialize the <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-class">SDKNativeEngine</a>.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdkversion-class">SDKVersion</a></span>  
The `SDKVersion` represents version information for an SDK product.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-usagestats-class">UsageStats</a></span>  
A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-class">UsageStatsNetworkStats</a></span>  
Provides network statistics in bytes per method.

## Enums

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogtype">CatalogType</a></span>  
Represents default HERE catalog types.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL</a></span>  
Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>  
Defines a list of possible map data features that can be enabled / disabled.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-loglevel">LogLevel</a></span>  
Severity levels for log messages.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-passthroughfeature">PassThroughFeature</a></span>  
Represents features that are allowed to consume online data when the HERE SDK's offline mode is activated via <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-isofflinemode">SDKNativeEngine.isOfflineMode</a> and/or <a href="sdk-for-flutter-explore-core-engine-sdkoptions-offlinemode">SDKOptions.offlineMode</a>.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-proxysettingsproxytype">ProxySettingsProxyType</a></span>  
Supported types of proxy connection.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdknativeenginepurgememorystrategy">SDKNativeEnginePurgeMemoryStrategy</a></span>  
Enum representing a strategy to flush memory caches.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdkoptionsactiononcachelock">SDKOptionsActionOnCacheLock</a></span>  
Action on cache lock

<span class="name"><a href="sdk-for-flutter-explore-core-engine-usagestatsfeature">UsageStatsFeature</a></span>  
Represents the feature enum associated with the gathered usage stats.

## Typedefs

<span class="name"><a href="sdk-for-flutter-explore-core-engine-authenticationmodeaccesstokenprovider">AuthenticationModeAccessTokenProvider</a></span><span class="signature"> <span class="returntype parameter">= String? Function<span class="signature">()</span></span> </span>  
This lambda is used to retrieve access token in synchronous manner.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-deviceidcallback">DeviceIdCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-explore-param-deviceId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">deviceId</span></span>)</span></span> </span>  
This method will be called on the main thread when <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-getdeviceid">SDKNativeEngine.getDeviceId</a> has been completed.

## Exceptions / Errors

<span class="name"><a href="sdk-for-flutter-explore-core-engine-logcontrolinvalidpathexceptionexception-class">LogControlInvalidPathExceptionException</a></span>  
Invalid file path exception.

</div>

<!-- /.main-content --> <!--/sidebar-offcanvas-right--> <span class="no-break"> here_sdk 4.26.0 </span>


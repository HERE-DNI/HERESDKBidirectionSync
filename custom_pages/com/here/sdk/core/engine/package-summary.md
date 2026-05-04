---
title: "com.here.sdk.core.engine (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpackage-summary"
hidden: false
---

# Package com.here.sdk.core.engine

------------------------------------------------------------------------
package com.here.sdk.core.engine

Related Packages

Package

  Description

  [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

  [com.here.sdk.core.errors](sdk-for-android-explore-api-reference-latestpackage-summary)

  [com.here.sdk.core.threading](sdk-for-android-explore-api-reference-latestpackage-summary)

  [com.here.sdk.core.utilities](sdk-for-android-explore-api-reference-latestpackage-summary)

All Classes and Interfaces
  Interfaces
  Classes
  Enum Classes
  Exceptions

  Class

  Description

  [ApplicationUtilsInitializer](sdk-for-android-explore-api-reference-latestapplicationutilsinitializer "class in com.here.sdk.core.engine")

This class is for internal use only.

[AuthenticationMode](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine")

This is a bearer authentication mode which adds or does not add a header ("Authorization", "Bearer \$Token") to each online request of the module the object is added to.

[AuthenticationMode.AccessTokenProvider](sdk-for-android-explore-api-reference-latestauthenticationmode-accesstokenprovider "interface in com.here.sdk.core.engine")

This lambda is used to retrieve access token in synchronous manner.

[CatalogConfiguration](sdk-for-android-explore-api-reference-latestcatalogconfiguration "class in com.here.sdk.core.engine")

Using this class you can configure in the [`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine"), how the [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") should access, use and store the data for the desired catalog.

[CatalogIdentifier](sdk-for-android-explore-api-reference-latestcatalogidentifier "class in com.here.sdk.core.engine")

This class is used to identify any catalog in the HERE platform.

[CatalogType](sdk-for-android-explore-api-reference-latestcatalogtype "enum class in com.here.sdk.core.engine")

Represents default HERE catalog types.

[CatalogVersionHint](sdk-for-android-explore-api-reference-latestcatalogversionhint "class in com.here.sdk.core.engine")

This is a class for capturing user's intent for the desired catalog version to use in [`DesiredCatalog`](sdk-for-android-explore-api-reference-latestdesiredcatalog "class in com.here.sdk.core.engine") class.

[CertificateSettings](sdk-for-android-explore-api-reference-latestcertificatesettings "class in com.here.sdk.core.engine")

Certificate settings to be used by Curl+OpenSSL for authority

[DesiredCatalog](sdk-for-android-explore-api-reference-latestdesiredcatalog "class in com.here.sdk.core.engine")

This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access.

[DeviceIdCallback](sdk-for-android-explore-api-reference-latestdeviceidcallback "interface in com.here.sdk.core.engine")

This method will be called on the main thread when [`SDKNativeEngine.getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)`](sdk-for-android-explore-api-reference-latestsdknativeengine#getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)) has been completed.

[EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine")

Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.

[EngineOptions](sdk-for-android-explore-api-reference-latestengineoptions "class in com.here.sdk.core.engine")

Specifies several options specific to different engines.

[LayerConfiguration](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine")

A class to configure which layers should be enabled or disabled in the OCM map data.

[LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")

Defines a list of possible map data features that can be enabled / disabled.

[LockingProcess](sdk-for-android-explore-api-reference-latestlockingprocess "class in com.here.sdk.core.engine")

LockingProcess helps to detect situations when cache is locked with another process and attempt to create instance of [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") fails with error [`InstantiationErrorCode.FAILED_TO_LOCK_CACHE_FOLDER`](sdk-for-android-explore-api-reference-latestinstantiationerrorcode#FAILED_TO_LOCK_CACHE_FOLDER).

[LogAppender](sdk-for-android-explore-api-reference-latestlogappender "interface in com.here.sdk.core.engine")

An interface to implement a listener to receive log messages.

[LogControl](sdk-for-android-explore-api-reference-latestlogcontrol "class in com.here.sdk.core.engine")

This class provides functionality to enable/disable console logs as well as setting a custom log appender to receive log messages from the SDK.

[LogControl.InvalidPathException](sdk-for-android-explore-api-reference-latestlogcontrol-invalidpathexception "class in com.here.sdk.core.engine")

Invalid file path exception.

[LogLevel](sdk-for-android-explore-api-reference-latestloglevel "enum class in com.here.sdk.core.engine")

Severity levels for log messages.

[NetworkSettings](sdk-for-android-explore-api-reference-latestnetworksettings "class in com.here.sdk.core.engine")

Network configuration to be used by [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") during the initialization.

[PassThroughFeature](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine")

Represents features that are allowed to consume online data when the HERE SDK's offline mode is activated via [`SDKNativeEngine.isOfflineMode()`](sdk-for-android-explore-api-reference-latestsdknativeengine#isOfflineMode()) and/or [`SDKOptions.offlineMode`](sdk-for-android-explore-api-reference-latestsdkoptions#offlineMode).

[ProxySettings](sdk-for-android-explore-api-reference-latestproxysettings "class in com.here.sdk.core.engine")

Proxy configuration for the HERE SDK network that is applied per request.

[ProxySettings.Credentials](sdk-for-android-explore-api-reference-latestproxysettings-credentials "class in com.here.sdk.core.engine")

Authentication data

[ProxySettings.ProxyType](sdk-for-android-explore-api-reference-latestproxysettings-proxytype "enum class in com.here.sdk.core.engine")

Supported types of proxy connection.

[SDKBuildInformation](sdk-for-android-explore-api-reference-latestsdkbuildinformation "class in com.here.sdk.core.engine")

The SDKBuildInformation class is designed to provide information about the SDK build.

[SDKLogger](sdk-for-android-explore-api-reference-latestsdklogger "class in com.here.sdk.core.engine")

Logging interface for Android/iOS platforms.

[SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")

Holds internal services and configurations needed by various HERE SDK modules.

[SDKNativeEngine.PurgeMemoryStrategy](sdk-for-android-explore-api-reference-latestsdknativeengine-purgememorystrategy "enum class in com.here.sdk.core.engine")

Enum representing a strategy to flush memory caches.

[SDKOptions](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine")

SDKOptions provide an alternative way to set or update the HERE SDK credentials and other parameters at runtime to initialize the [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine").

[SDKOptions.ActionOnCacheLock](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine")

Action on cache lock

[SDKVersion](sdk-for-android-explore-api-reference-latestsdkversion "class in com.here.sdk.core.engine")

The `SDKVersion` represents version information for an SDK product.

[UsageStats](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine")

A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.

[UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine")

Represents the feature enum associated with the gathered usage stats.

[UsageStats.NetworkStats](sdk-for-android-explore-api-reference-latestusagestats-networkstats "class in com.here.sdk.core.engine")

Provides network statistics in bytes per method.

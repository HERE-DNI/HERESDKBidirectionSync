---
title: "com.here.sdk.core.engine (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-package-summary"
---

<div class="header">

</div>

<div class="package-signature">

package <span class="element-name">com.here.sdk.core.engine</span>

</div>

- <div id="sdk-for-android-explore-related-package-summary">

  <div class="caption">

  Related Packages

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Package

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

  </div>

  <div class="col-last even-row-color">

   

  </div>

  <div class="col-first odd-row-color">

  [com.here.sdk.core.errors](sdk-for-android-explore-com-here-sdk-core-errors-package-summary)

  </div>

  <div class="col-last odd-row-color">

   

  </div>

  <div class="col-first even-row-color">

  [com.here.sdk.core.threading](sdk-for-android-explore-com-here-sdk-core-threading-package-summary)

  </div>

  <div class="col-last even-row-color">

   

  </div>

  <div class="col-first odd-row-color">

  [com.here.sdk.core.utilities](sdk-for-android-explore-com-here-sdk-core-utilities-package-summary)

  </div>

  <div class="col-last odd-row-color">

   

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-class-summary">

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [ApplicationUtilsInitializer](sdk-for-android-explore-com-here-sdk-core-engine-applicationutilsinitializer "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  This class is for internal use only.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [AuthenticationMode](sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  This is a bearer authentication mode which adds or does not add a header ("Authorization", "Bearer \$Token") to each online request of the module the object is added to.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  [AuthenticationMode.AccessTokenProvider](sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode-accesstokenprovider "interface in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  This lambda is used to retrieve access token in synchronous manner.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [CatalogConfiguration](sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Using this class you can configure in the SDKOptions , how the SDKNativeEngine should access, use and store the data for the desired catalog.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [CatalogIdentifier](sdk-for-android-explore-com-here-sdk-core-engine-catalogidentifier "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  This class is used to identify any catalog in the HERE platform.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  [CatalogType](sdk-for-android-explore-com-here-sdk-core-engine-catalogtype "enum class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Represents default HERE catalog types.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [CatalogVersionHint](sdk-for-android-explore-com-here-sdk-core-engine-catalogversionhint "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  This is a class for capturing user's intent for the desired catalog version to use in DesiredCatalog class.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [CertificateSettings](sdk-for-android-explore-com-here-sdk-core-engine-certificatesettings "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Certificate settings to be used by Curl+OpenSSL for authority

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [DesiredCatalog](sdk-for-android-explore-com-here-sdk-core-engine-desiredcatalog "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab1">

  [DeviceIdCallback](sdk-for-android-explore-com-here-sdk-core-engine-deviceidcallback "interface in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab1">

  <div class="block">

  This method will be called on the main thread when SDKNativeEngine.getDeviceId(com.here.sdk.core.engine.DeviceIdCallback) has been completed.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  [EngineBaseURL](sdk-for-android-explore-com-here-sdk-core-engine-enginebaseurl "enum class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [EngineOptions](sdk-for-android-explore-com-here-sdk-core-engine-engineoptions "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Specifies several options specific to different engines.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [LayerConfiguration](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  A class to configure which layers should be enabled or disabled in the OCM map data.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  [LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Defines a list of possible map data features that can be enabled / disabled.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [LockingProcess](sdk-for-android-explore-com-here-sdk-core-engine-lockingprocess "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  LockingProcess helps to detect situations when cache is locked with another process and attempt to create instance of SDKNativeEngine fails with error InstantiationErrorCode.FAILED_TO_LOCK_CACHE_FOLDER .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab1">

  [LogAppender](sdk-for-android-explore-com-here-sdk-core-engine-logappender "interface in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab1">

  <div class="block">

  An interface to implement a listener to receive log messages.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [LogControl](sdk-for-android-explore-com-here-sdk-core-engine-logcontrol "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  This class provides functionality to enable/disable console logs as well as setting a custom log appender to receive log messages from the SDK.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab5">

  [LogControl.InvalidPathException](sdk-for-android-explore-com-here-sdk-core-engine-logcontrol-invalidpathexception "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab5">

  <div class="block">

  Invalid file path exception.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  [LogLevel](sdk-for-android-explore-com-here-sdk-core-engine-loglevel "enum class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Severity levels for log messages.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [NetworkSettings](sdk-for-android-explore-com-here-sdk-core-engine-networksettings "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Network configuration to be used by SDKNativeEngine during the initialization.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  [PassThroughFeature](sdk-for-android-explore-com-here-sdk-core-engine-passthroughfeature "enum class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Represents features that are allowed to consume online data when the HERE SDK's offline mode is activated via SDKNativeEngine.isOfflineMode() and/or SDKOptions.offlineMode .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [ProxySettings](sdk-for-android-explore-com-here-sdk-core-engine-proxysettings "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Proxy configuration for the HERE SDK network that is applied per request.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [ProxySettings.Credentials](sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-credentials "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  Authentication data

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  [ProxySettings.ProxyType](sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-proxytype "enum class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Supported types of proxy connection.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [SDKBuildInformation](sdk-for-android-explore-com-here-sdk-core-engine-sdkbuildinformation "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  The SDKBuildInformation class is designed to provide information about the SDK build.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [SDKLogger](sdk-for-android-explore-com-here-sdk-core-engine-sdklogger "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Logging interface for Android/iOS platforms.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  Holds internal services and configurations needed by various HERE SDK modules.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  [SDKNativeEngine.PurgeMemoryStrategy](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine-purgememorystrategy "enum class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Enum representing a strategy to flush memory caches.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [SDKOptions](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  SDKOptions provide an alternative way to set or update the HERE SDK credentials and other parameters at runtime to initialize the SDKNativeEngine .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  [SDKOptions.ActionOnCacheLock](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Action on cache lock

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  [SDKVersion](sdk-for-android-explore-com-here-sdk-core-engine-sdkversion "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  The SDKVersion represents version information for an SDK product.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [UsageStats](sdk-for-android-explore-com-here-sdk-core-engine-usagestats "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  [UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Represents the feature enum associated with the gathered usage stats.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  [UsageStats.NetworkStats](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-networkstats "class in com.here.sdk.core.engine")

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Provides network statistics in bytes per method.

  </div>

  </div>

  </div>

  </div>


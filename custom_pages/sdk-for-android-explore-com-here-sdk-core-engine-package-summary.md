---
title: "com.here.sdk.core.engine (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-package-summary"
---

<div class="package-signature">

package <span class="element-name">com.here.sdk.core.engine</span>

</div>

<div class="section summary">

- <div id="related-package-summary">

  <div class="caption">

  Related Packages

  </div>

  | Package | Description |
  |----|----|
  | [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary) |   |
  | [com.here.sdk.core.errors](sdk-for-android-explore-com-here-sdk-core-errors-package-summary) |   |
  | [com.here.sdk.core.threading](sdk-for-android-explore-com-here-sdk-core-threading-package-summary) |   |
  | [com.here.sdk.core.utilities](sdk-for-android-explore-com-here-sdk-core-utilities-package-summary) |   |

  </div>

- <div id="class-summary">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Classes and Interfaces
  Interfaces
  Classes
  Enum Classes
  Exceptions

  </div>

  <div id="class-summary.tabpanel" aria-labelledby="class-summary-tab0"
  role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-applicationutilsinitializer"
  title="class in com.here.sdk.core.engine">ApplicationUtilsInitializer</a></td>
  <td><div class="block">
  This class is for internal use only.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode"
  title="class in com.here.sdk.core.engine">AuthenticationMode</a></td>
  <td><div class="block">
  This is a bearer authentication mode which adds or does not add a header
  ("Authorization", "Bearer $Token") to each online request of the module
  the object is added to.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode-accesstokenprovider"
  title="interface in com.here.sdk.core.engine">AuthenticationMode.AccessTokenProvider</a></td>
  <td><div class="block">
  This lambda is used to retrieve access token in synchronous manner.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration"
  title="class in com.here.sdk.core.engine">CatalogConfiguration</a></td>
  <td><div class="block">
  Using this class you can configure in the SDKOptions , how the
  SDKNativeEngine should access, use and store the data for the desired
  catalog.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-catalogidentifier"
  title="class in com.here.sdk.core.engine">CatalogIdentifier</a></td>
  <td><div class="block">
  This class is used to identify any catalog in the HERE platform.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-catalogtype"
  title="enum class in com.here.sdk.core.engine">CatalogType</a></td>
  <td><div class="block">
  Represents default HERE catalog types.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-catalogversionhint"
  title="class in com.here.sdk.core.engine">CatalogVersionHint</a></td>
  <td><div class="block">
  This is a class for capturing user's intent for the desired catalog
  version to use in DesiredCatalog class.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-certificatesettings"
  title="class in com.here.sdk.core.engine">CertificateSettings</a></td>
  <td><div class="block">
  Certificate settings to be used by Curl+OpenSSL for authority
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-desiredcatalog"
  title="class in com.here.sdk.core.engine">DesiredCatalog</a></td>
  <td><div class="block">
  This class provides an interface to the user, to identify a catalog on
  the HERE platform, whose data he wants to access.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-deviceidcallback"
  title="interface in com.here.sdk.core.engine">DeviceIdCallback</a></td>
  <td><div class="block">
  This method will be called on the main thread when
  SDKNativeEngine.getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)
  has been completed.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-enginebaseurl"
  title="enum class in com.here.sdk.core.engine">EngineBaseURL</a></td>
  <td><div class="block">
  Lists the available HERE SDK endpoints that can be customized with a
  custom backend base URL.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-engineoptions"
  title="class in com.here.sdk.core.engine">EngineOptions</a></td>
  <td><div class="block">
  Specifies several options specific to different engines.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration"
  title="class in com.here.sdk.core.engine">LayerConfiguration</a></td>
  <td><div class="block">
  A class to configure which layers should be enabled or disabled in the
  OCM map data.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature"
  title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></td>
  <td><div class="block">
  Defines a list of possible map data features that can be enabled /
  disabled.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-lockingprocess"
  title="class in com.here.sdk.core.engine">LockingProcess</a></td>
  <td><div class="block">
  LockingProcess helps to detect situations when cache is locked with
  another process and attempt to create instance of SDKNativeEngine fails
  with error InstantiationErrorCode.FAILED_TO_LOCK_CACHE_FOLDER .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-logappender"
  title="interface in com.here.sdk.core.engine">LogAppender</a></td>
  <td><div class="block">
  An interface to implement a listener to receive log messages.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-logcontrol"
  title="class in com.here.sdk.core.engine">LogControl</a></td>
  <td><div class="block">
  This class provides functionality to enable/disable console logs as well
  as setting a custom log appender to receive log messages from the SDK.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-logcontrol-invalidpathexception"
  title="class in com.here.sdk.core.engine">LogControl.InvalidPathException</a></td>
  <td><div class="block">
  Invalid file path exception.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-engine-loglevel"
  title="enum class in com.here.sdk.core.engine">LogLevel</a></td>
  <td><div class="block">
  Severity levels for log messages.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-networksettings"
  title="class in com.here.sdk.core.engine">NetworkSettings</a></td>
  <td><div class="block">
  Network configuration to be used by SDKNativeEngine during the
  initialization.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-passthroughfeature"
  title="enum class in com.here.sdk.core.engine">PassThroughFeature</a></td>
  <td><div class="block">
  Represents features that are allowed to consume online data when the
  HERE SDK's offline mode is activated via SDKNativeEngine.isOfflineMode()
  and/or SDKOptions.offlineMode .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings"
  title="class in com.here.sdk.core.engine">ProxySettings</a></td>
  <td><div class="block">
  Proxy configuration for the HERE SDK network that is applied per
  request.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-credentials"
  title="class in com.here.sdk.core.engine">ProxySettings.Credentials</a></td>
  <td><div class="block">
  Authentication data
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-proxysettings-proxytype"
  title="enum class in com.here.sdk.core.engine">ProxySettings.ProxyType</a></td>
  <td><div class="block">
  Supported types of proxy connection.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkbuildinformation"
  title="class in com.here.sdk.core.engine">SDKBuildInformation</a></td>
  <td><div class="block">
  The SDKBuildInformation class is designed to provide information about
  the SDK build.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-engine-sdklogger"
  title="class in com.here.sdk.core.engine">SDKLogger</a></td>
  <td><div class="block">
  Logging interface for Android/iOS platforms.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine"
  title="class in com.here.sdk.core.engine">SDKNativeEngine</a></td>
  <td><div class="block">
  Holds internal services and configurations needed by various HERE SDK
  modules.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine-purgememorystrategy"
  title="enum class in com.here.sdk.core.engine">SDKNativeEngine.PurgeMemoryStrategy</a></td>
  <td><div class="block">
  Enum representing a strategy to flush memory caches.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions"
  title="class in com.here.sdk.core.engine">SDKOptions</a></td>
  <td><div class="block">
  SDKOptions provide an alternative way to set or update the HERE SDK
  credentials and other parameters at runtime to initialize the
  SDKNativeEngine .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions-actiononcachelock"
  title="enum class in com.here.sdk.core.engine">SDKOptions.ActionOnCacheLock</a></td>
  <td><div class="block">
  Action on cache lock
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkversion"
  title="class in com.here.sdk.core.engine">SDKVersion</a></td>
  <td><div class="block">
  The SDKVersion represents version information for an SDK product.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats"
  title="class in com.here.sdk.core.engine">UsageStats</a></td>
  <td><div class="block">
  A class that gathers statistics of the HERE SDK network usage for
  uploaded and downloaded data.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature"
  title="enum class in com.here.sdk.core.engine">UsageStats.Feature</a></td>
  <td><div class="block">
  Represents the feature enum associated with the gathered usage stats.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-networkstats"
  title="class in com.here.sdk.core.engine">UsageStats.NetworkStats</a></td>
  <td><div class="block">
  Provides network statistics in bytes per method.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

</div>


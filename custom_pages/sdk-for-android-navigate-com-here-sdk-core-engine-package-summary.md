---
title: "com.here.sdk.core.engine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-engine-package-summary"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- package-summary.html -->
<!DOCTYPE HTML>









<main role="main">
<div class="header">

</div>
<hr/>
<div class="package-signature">package <span class="element-name">com.here.sdk.core.engine</span></div>
<section class="summary">
<ul class="summary-list">
<li>
<div id="related-package-summary">
<div class="caption"><span>Related Packages</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Package</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.core.errors</a></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.core.threading</a></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.core.utilities</a></div>
<div class="col-last odd-row-color"> </div>
</div>
</div>
</li>
<li>
<div id="class-summary">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="class-summary.tabpanel" aria-selected="true" class="active-table-tab" id="class-summary-tab0" onclick="show('class-summary', 'class-summary', 2)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Classes and Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab1" onclick="show('class-summary', 'class-summary-tab1', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab2" onclick="show('class-summary', 'class-summary-tab2', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Classes</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab3" onclick="show('class-summary', 'class-summary-tab3', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Enum Classes</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab5" onclick="show('class-summary', 'class-summary-tab5', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Exceptions</button></div>
<div aria-labelledby="class-summary-tab0" id="class-summary.tabpanel" role="tabpanel">
<div class="summary-table two-column-summary">
<div class="table-header col-first">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-applicationutilsinitializer" title="class in com.here.sdk.core.engine">ApplicationUtilsInitializer</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">This class is for internal use only.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-authenticationmode" title="class in com.here.sdk.core.engine">AuthenticationMode</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">This is a bearer authentication mode which adds or does not add a
 header ("Authorization", "Bearer $Token") to each online request of the
 module the object is added to.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-authenticationmode.accesstokenprovider" title="interface in com.here.sdk.core.engine">AuthenticationMode.AccessTokenProvider</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">This lambda is used to retrieve access token in synchronous manner.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-catalogconfiguration" title="class in com.here.sdk.core.engine">CatalogConfiguration</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Using this class you can configure in the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a>,
 how the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> should access, use and store the data for the desired catalog.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-catalogidentifier" title="class in com.here.sdk.core.engine">CatalogIdentifier</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">This class is used to identify any catalog in the HERE platform.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-catalogtype" title="enum class in com.here.sdk.core.engine">CatalogType</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Represents default HERE catalog types.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-catalogversionhint" title="class in com.here.sdk.core.engine">CatalogVersionHint</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">This is a class for capturing user's intent for the
 desired catalog version to use in <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-desiredcatalog" title="class in com.here.sdk.core.engine"><code>DesiredCatalog</code></a> class.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-certificatesettings" title="class in com.here.sdk.core.engine">CertificateSettings</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Certificate settings to be used by Curl+OpenSSL for authority</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-desiredcatalog" title="class in com.here.sdk.core.engine">DesiredCatalog</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-deviceidcallback" title="interface in com.here.sdk.core.engine">DeviceIdCallback</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">This method will be called on the main thread when <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine#getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)"><code>SDKNativeEngine.getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)</code></a> has been completed.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-enginebaseurl" title="enum class in com.here.sdk.core.engine">EngineBaseURL</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-engineoptions" title="class in com.here.sdk.core.engine">EngineOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Specifies several options specific to different engines.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-layerconfiguration" title="class in com.here.sdk.core.engine">LayerConfiguration</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">A class to configure which layers should be enabled or disabled in the OCM map data.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Defines a list of possible map data features that can be enabled / disabled.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-lockingprocess" title="class in com.here.sdk.core.engine">LockingProcess</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">LockingProcess helps to detect situations when cache is locked with another process and
 attempt to create instance of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> fails with error
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorcode#FAILED_TO_LOCK_CACHE_FOLDER"><code>InstantiationErrorCode.FAILED_TO_LOCK_CACHE_FOLDER</code></a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-logappender" title="interface in com.here.sdk.core.engine">LogAppender</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">An interface to implement a listener to receive log messages.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-logcontrol" title="class in com.here.sdk.core.engine">LogControl</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">This class provides functionality to enable/disable console logs as well as
 setting a custom log appender to receive log messages from the SDK.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab5"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-logcontrol.invalidpathexception" title="class in com.here.sdk.core.engine">LogControl.InvalidPathException</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab5">
<div class="block">Invalid file path exception.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-loglevel" title="enum class in com.here.sdk.core.engine">LogLevel</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Severity levels for log messages.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-networksettings" title="class in com.here.sdk.core.engine">NetworkSettings</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Network configuration to be used by <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> during the initialization.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-passthroughfeature" title="enum class in com.here.sdk.core.engine">PassThroughFeature</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Represents features that are allowed to consume online data when the HERE SDK's offline mode
 is activated via <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine#isOfflineMode()"><code>SDKNativeEngine.isOfflineMode()</code></a> and/or
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdkoptions#offlineMode"><code>SDKOptions.offlineMode</code></a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-proxysettings" title="class in com.here.sdk.core.engine">ProxySettings</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Proxy configuration for the HERE SDK network that is applied per request.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-proxysettings.credentials" title="class in com.here.sdk.core.engine">ProxySettings.Credentials</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Authentication data</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-proxysettings.proxytype" title="enum class in com.here.sdk.core.engine">ProxySettings.ProxyType</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Supported types of proxy connection.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdkbuildinformation" title="class in com.here.sdk.core.engine">SDKBuildInformation</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The SDKBuildInformation class is designed to provide information about the SDK build.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdklogger" title="class in com.here.sdk.core.engine">SDKLogger</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Logging interface for Android/iOS platforms.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Holds internal services and configurations needed by various HERE SDK modules.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine.purgememorystrategy" title="enum class in com.here.sdk.core.engine">SDKNativeEngine.PurgeMemoryStrategy</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Enum representing a strategy to flush memory caches.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdkoptions" title="class in com.here.sdk.core.engine">SDKOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">SDKOptions provide an alternative way to set or update the HERE SDK credentials and other
 parameters at runtime to initialize the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdkoptions.actiononcachelock" title="enum class in com.here.sdk.core.engine">SDKOptions.ActionOnCacheLock</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Action on cache lock</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdkversion" title="class in com.here.sdk.core.engine">SDKVersion</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The <code>SDKVersion</code> represents version information for an SDK product.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-usagestats" title="class in com.here.sdk.core.engine">UsageStats</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-usagestats.feature" title="enum class in com.here.sdk.core.engine">UsageStats.Feature</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Represents the feature enum associated with the gathered usage stats.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-usagestats.networkstats" title="class in com.here.sdk.core.engine">UsageStats.NetworkStats</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Provides network statistics in bytes per method.</div>
</div>
</div>
</div>
</div>
</li>
</ul>
</section>
</main>





</div>
`
}</HTMLBlock>

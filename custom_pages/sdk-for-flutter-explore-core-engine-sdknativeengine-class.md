---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- SDKNativeEngine-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/SDKNativeEngine-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/SDKNativeEngine/SDKNativeEngine.html">SDKNativeEngine</a></li>
<li class="section-title">
<a href="core.engine/SDKNativeEngine-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="core.engine/SDKNativeEngine/hashCode.html">hashCode</a></li>
<li><a href="core.engine/SDKNativeEngine/isOfflineMode.html">isOfflineMode</a></li>
<li><a href="core.engine/SDKNativeEngine/options.html">options</a></li>
<li><a href="core.engine/SDKNativeEngine/passThroughFeatures.html">passThroughFeatures</a></li>
<li><a href="core.engine/SDKNativeEngine/proxySettings.html">proxySettings</a></li>
<li class="inherited"><a href="core.engine/SDKNativeEngine/runtimeType.html">runtimeType</a></li>
<li><a href="core.engine/SDKNativeEngine/sdkUsageStats.html">sdkUsageStats</a></li>
<li class="section-title"><a href="core.engine/SDKNativeEngine-class.html#instance-methods">Methods</a></li>
<li><a href="core.engine/SDKNativeEngine/clearPersistentUsageStats.html">clearPersistentUsageStats</a></li>
<li><a href="core.engine/SDKNativeEngine/clearUsageStatsCache.html">clearUsageStatsCache</a></li>
<li><a href="core.engine/SDKNativeEngine/dispose.html">dispose</a></li>
<li><a href="core.engine/SDKNativeEngine/enableUsageStats.html">enableUsageStats</a></li>
<li><a href="core.engine/SDKNativeEngine/getDeviceId.html">getDeviceId</a></li>
<li class="inherited"><a href="core.engine/SDKNativeEngine/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="core.engine/SDKNativeEngine/purgeMemoryCaches.html">purgeMemoryCaches</a></li>
<li><a href="core.engine/SDKNativeEngine/setAccessKeySecret.html">setAccessKeySecret</a></li>
<li><a href="core.engine/SDKNativeEngine/setAccessScope.html">setAccessScope</a></li>
<li class="inherited"><a href="core.engine/SDKNativeEngine/toString.html">toString</a></li>
<li class="section-title inherited"><a href="core.engine/SDKNativeEngine-class.html#operators">Operators</a></li>
<li class="inherited"><a href="core.engine/SDKNativeEngine/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="core.engine/SDKNativeEngine-class.html#static-properties">Static properties</a></li>
<li><a href="core.engine/SDKNativeEngine/parameterConfig.html">parameterConfig</a></li>
<li><a href="core.engine/SDKNativeEngine/sharedInstance.html">sharedInstance</a></li>
<li class="section-title"><a href="core.engine/SDKNativeEngine-class.html#static-methods">Static methods</a></li>
<li><a href="core.engine/SDKNativeEngine/makeSharedInstance.html">makeSharedInstance</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">SDKNativeEngine class</li>
</ol>
<div class="self-name">SDKNativeEngine</div>
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
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SDKNativeEngine class abstract</h1></div>
<section class="desc markdown">
<p>Holds internal services and configurations needed by various HERE SDK modules.</p>
<p>You can initialize the HERE SDK in two ways:</p>
<ul>
<li>Create a shared instance of the <code>SDKNativeEngine</code> with <code>SDKNativeEngine.makeSharedInstance()</code>.</li>
<li>Create individual instances of the <code>SDKNativeEngine</code> via <code>SDKNativeEngine()</code>. Note that this does not automatically set a shared instance.</li>
</ul>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SDKNativeEngine">
<a href="../core.engine/SDKNativeEngine/SDKNativeEngine.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-sdknativeengine</a>(<a href="../core.engine/SDKOptions-class.html">/sdk-for-flutter-explore-core-engine-sdkoptions-class</a> options)
</dt>
<dd>
          Makes a new instance of SDKNativeEngine using supplied options.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../core.engine/SDKNativeEngine/hashCode.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="isOfflineMode">
<a href="../core.engine/SDKNativeEngine/isOfflineMode.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-isofflinemode</a>
↔ bool
</dt>
<dd>
  The offline mode.
Sets offline mode for the HERE SDK to offline or online.
Defaults to false, which means the HERE SDK uses an online connection.
When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set.
See <a href="../core.engine/SDKNativeEngine/passThroughFeatures.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-passthroughfeatures</a>.
Note that the flag does not cancel pending requests.
The mode can be enabled or disabled at any time. In order to fully operate offline, the mode
needs to be enabled via <a href="../core.engine/SDKOptions/offlineMode.html">/sdk-for-flutter-explore-core-engine-sdkoptions-offlinemode</a>.
Initialization of the HERE SDK itself does not require an internet connection.
Returns <code>true</code> if the HERE SDK uses offline connection mode, otherwise returns <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="options">
<a href="../core.engine/SDKNativeEngine/options.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-options</a>
→ <a href="../core.engine/SDKOptions-class.html">/sdk-for-flutter-explore-core-engine-sdkoptions-class</a>
</dt>
<dd>
  Options used by this instance of <a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a>.
Gets the options used by this instance of <a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a>.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="passThroughFeatures">
<a href="../core.engine/SDKNativeEngine/passThroughFeatures.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-passthroughfeatures</a>
↔ Set&lt;<wbr/><a href="../core.engine/PassThroughFeature.html">/sdk-for-flutter-explore-core-engine-passthroughfeature</a>&gt;?
</dt>
<dd>
  The pass through features.
Sets pass through features which are allowed to use online data when HERE SDK is in offline mode.
Pass through features can be updated at any time.
When offline mode is disabled, existing pass through features will be removed.
These needs to be set again when you enable offline mode next time.
By default, reporting of HERE SDK <a href="../core.engine/UsageStats-class.html">/sdk-for-flutter-explore-core-engine-usagestats-class</a> will be enabled when at least one pass-through feature is set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="proxySettings">
<a href="../core.engine/SDKNativeEngine/proxySettings.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-proxysettings</a>
↔ <a href="../core.engine/ProxySettings-class.html">/sdk-for-flutter-explore-core-engine-proxysettings-class</a>?
</dt>
<dd>
  Proxy settings of this SDK engine that will be used by HERE SDK network for all requests.
Defaults to (<code>null</code>), which indicates proxy is not enabled.
When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings.
Pass (<code>null</code>) to indicate that proxy should be disabled.
If proxy is necessary from the start then it's recommended to use <a href="../core.engine/NetworkSettings/proxySettings.html">/sdk-for-flutter-explore-core-engine-networksettings-proxysettings</a> in <a href="../core.engine/SDKOptions/networkSettings.html">/sdk-for-flutter-explore-core-engine-sdkoptions-networksettings</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core.engine/SDKNativeEngine/runtimeType.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sdkUsageStats">
<a href="../core.engine/SDKNativeEngine/sdkUsageStats.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-sdkusagestats</a>
→ List&lt;<wbr/><a href="../core.engine/UsageStats-class.html">/sdk-for-flutter-explore-core-engine-usagestats-class</a>&gt;
</dt>
<dd>
  Gets a list of usage statistics for all available HERE SDK features.
<a href="../core.engine/UsageStats-class.html">/sdk-for-flutter-explore-core-engine-usagestats-class</a> has cache and persistent storage. Reads from the persistent storage happen on <code>SDKNativeEngine</code> creation step.
Writes to persistent storage happen by reaching internal limit (amount of upload bytes, by default is 50KB).
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="clearPersistentUsageStats">
<a href="../core.engine/SDKNativeEngine/clearPersistentUsageStats.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-clearpersistentusagestats</a>(<wbr/>)
    → void

</dt>
<dd>
  Clear persistent storage for the HERE SDK <a href="../core.engine/UsageStats-class.html">/sdk-for-flutter-explore-core-engine-usagestats-class</a>.
  

</dd>
<dt class="callable" id="clearUsageStatsCache">
<a href="../core.engine/SDKNativeEngine/clearUsageStatsCache.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-clearusagestatscache</a>(<wbr/>)
    → void

</dt>
<dd>
  Clear cache for the HERE SDK <a href="../core.engine/UsageStats-class.html">/sdk-for-flutter-explore-core-engine-usagestats-class</a>.
  

</dd>
<dt class="callable" id="dispose">
<a href="../core.engine/SDKNativeEngine/dispose.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-dispose</a>(<wbr/>)
    → Future&lt;<wbr/>void&gt;

</dt>
<dd>
  Stops pending requests and closes open files and databases in main thread.
  

</dd>
<dt class="callable" id="enableUsageStats">
<a href="../core.engine/SDKNativeEngine/enableUsageStats.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-enableusagestats</a>(<wbr/>bool enabled)
    → void

</dt>
<dd>
  Enable or disable <a href="../core.engine/UsageStats-class.html">/sdk-for-flutter-explore-core-engine-usagestats-class</a> for the HERE SDK.
  

</dd>
<dt class="callable" id="getDeviceId">
<a href="../core.engine/SDKNativeEngine/getDeviceId.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-getdeviceid</a>(<wbr/>)
    → Future&lt;<wbr/>String&gt;

</dt>
<dd>
  The unique identifier assigned to the device for this application.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../core.engine/SDKNativeEngine/noSuchMethod.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="purgeMemoryCaches">
<a href="../core.engine/SDKNativeEngine/purgeMemoryCaches.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-purgememorycaches</a>(<wbr/><a href="../core.engine/SDKNativeEnginePurgeMemoryStrategy.html">/sdk-for-flutter-explore-core-engine-sdknativeenginepurgememorystrategy</a> strategy)
    → void

</dt>
<dd>
  Releases memory occupied by internal caches.
  

</dd>
<dt class="callable" id="setAccessKeySecret">
<a href="../core.engine/SDKNativeEngine/setAccessKeySecret.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-setaccesskeysecret</a>(<wbr/>String accessKeySecret)
    → void

</dt>
<dd>
  Overrides HERE SDK access key secret with new value.
  

</dd>
<dt class="callable" id="setAccessScope">
<a href="../core.engine/SDKNativeEngine/setAccessScope.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-setaccessscope</a>(<wbr/>String scope)
    → void

</dt>
<dd>
  Overrides the token scope of the HERE SDK with new value.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../core.engine/SDKNativeEngine/toString.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../core.engine/SDKNativeEngine/operator_equals.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-properties">
<h2>Static Properties</h2>
<dl class="properties">
<dt class="property" id="parameterConfig">
<a href="../core.engine/SDKNativeEngine/parameterConfig.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-parameterconfig</a>
↔ <a href="../core/ParameterConfiguration-class.html">/sdk-for-flutter-explore-core-parameterconfiguration-class</a>
</dt>
<dd>
  Configuration for default values of parameters used in the HERE SDK.
<strong>Note:</strong> This feature is in beta state and thus there can be bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.
Gets the configuration for default values of parameters used in the HERE SDK.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="sharedInstance">
<a href="../core.engine/SDKNativeEngine/sharedInstance.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-sharedinstance</a>
↔ <a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a>?
</dt>
<dd>
  Shared instance of this SDK engine that can be accessed by any HERE SDK module as the default
engine.
This is automatically set as a part of the SDK initialization process.
Gets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default
engine.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="makeSharedInstance">
<a href="../core.engine/SDKNativeEngine/makeSharedInstance.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-makesharedinstance</a>(<wbr/><a href="../core.engine/SDKOptions-class.html">/sdk-for-flutter-explore-core-engine-sdkoptions-class</a> options)
    → Future&lt;<wbr/>void&gt;

</dt>
<dd>
  Makes a new instance of SDKNativeEngine using supplied options and stores it as shared instance
see <a href="../core.engine/SDKNativeEngine/sharedInstance.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-sharedinstance</a>.
  

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
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">SDKNativeEngine class</li>
</ol>
<h5>core.engine library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>

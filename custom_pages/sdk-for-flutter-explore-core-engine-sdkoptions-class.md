---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-engine-sdkoptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- SDKOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/SDKOptions-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/SDKOptions/SDKOptions.withAuthenticationMode.html">withAuthenticationMode</a></li>
<li class="section-title">
<a href="core.engine/SDKOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="core.engine/SDKOptions/actionOnCacheLock.html">actionOnCacheLock</a></li>
<li><a href="core.engine/SDKOptions/authenticationMode.html">authenticationMode</a></li>
<li><a href="core.engine/SDKOptions/autoUpdateOfOnlineCache.html">autoUpdateOfOnlineCache</a></li>
<li><a href="core.engine/SDKOptions/billingTag.html">billingTag</a></li>
<li><a href="core.engine/SDKOptions/cachePath.html">cachePath</a></li>
<li><a href="core.engine/SDKOptions/cacheSizeInBytes.html">cacheSizeInBytes</a></li>
<li><a href="core.engine/SDKOptions/catalogConfigurations.html">catalogConfigurations</a></li>
<li><a href="core.engine/SDKOptions/customEngineOptions.html">customEngineOptions</a></li>
<li><a href="core.engine/SDKOptions/customOptions.html">customOptions</a></li>
<li><a href="core.engine/SDKOptions/dataPath.html">dataPath</a></li>
<li><a href="core.engine/SDKOptions/hashCode.html">hashCode</a></li>
<li><a href="core.engine/SDKOptions/layerConfiguration.html">layerConfiguration</a></li>
<li><a href="core.engine/SDKOptions/lowMemoryMode.html">lowMemoryMode</a></li>
<li><a href="core.engine/SDKOptions/networkSettings.html">networkSettings</a></li>
<li><a href="core.engine/SDKOptions/offlineMode.html">offlineMode</a></li>
<li><a href="core.engine/SDKOptions/persistentMapStoragePath.html">persistentMapStoragePath</a></li>
<li><a href="core.engine/SDKOptions/politicalView.html">politicalView</a></li>
<li class="inherited"><a href="core.engine/SDKOptions/runtimeType.html">runtimeType</a></li>
<li><a href="core.engine/SDKOptions/scope.html">scope</a></li>
<li class="section-title inherited"><a href="core.engine/SDKOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core.engine/SDKOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.engine/SDKOptions/toString.html">toString</a></li>
<li class="section-title"><a href="core.engine/SDKOptions-class.html#operators">Operators</a></li>
<li><a href="core.engine/SDKOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">SDKOptions class</li>
</ol>
<div class="self-name">SDKOptions</div>
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
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/SDKOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SDKOptions class</h1></div>
<section class="desc markdown">
<p>SDKOptions provide an alternative way to set or update the HERE SDK credentials and other
parameters at runtime to initialize the <a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a>.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SDKOptions.withAuthenticationMode">
<a href="../core.engine/SDKOptions/SDKOptions.withAuthenticationMode.html">/sdk-for-flutter-explore-core-engine-sdkoptions-sdkoptions-withauthenticationmode</a>(<a href="../core.engine/AuthenticationMode-class.html">/sdk-for-flutter-explore-core-engine-authenticationmode-class</a> authenticationMode)
</dt>
<dd>
          Constructs a SDKOptions from authentication mode.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="actionOnCacheLock">
<a href="../core.engine/SDKOptions/actionOnCacheLock.html">/sdk-for-flutter-explore-core-engine-sdkoptions-actiononcachelock</a>
↔ <a href="../core.engine/SDKOptionsActionOnCacheLock.html">/sdk-for-flutter-explore-core-engine-sdkoptionsactiononcachelock</a>
</dt>
<dd>
  Specifies action to perform when cache folder is locked by another process. Default value is <a href="../core.engine/SDKOptionsActionOnCacheLock.html">/sdk-for-flutter-explore-core-engine-sdkoptionsactiononcachelock</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="authenticationMode">
<a href="../core.engine/SDKOptions/authenticationMode.html">/sdk-for-flutter-explore-core-engine-sdkoptions-authenticationmode</a>
↔ <a href="../core.engine/AuthenticationMode-class.html">/sdk-for-flutter-explore-core-engine-authenticationmode-class</a>
</dt>
<dd>
  Encapsulates Authentication method and parameters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="autoUpdateOfOnlineCache">
<a href="../core.engine/SDKOptions/autoUpdateOfOnlineCache.html">/sdk-for-flutter-explore-core-engine-sdkoptions-autoupdateofonlinecache</a>
↔ bool
</dt>
<dd>
  Parameter to enable automatic cache updates.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="billingTag">
<a href="../core.engine/SDKOptions/billingTag.html">/sdk-for-flutter-explore-core-engine-sdkoptions-billingtag</a>
↔ String?
</dt>
<dd>
  Internal to HERE SDK. DO NOT USE THIS YET.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="cachePath">
<a href="../core.engine/SDKOptions/cachePath.html">/sdk-for-flutter-explore-core-engine-sdkoptions-cachepath</a>
↔ String
</dt>
<dd>
  Path to be used for caching purposes. It should be a path to the desired location where the application has read/write permissions.
The path can be on internal or external storage.
By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="cacheSizeInBytes">
<a href="../core.engine/SDKOptions/cacheSizeInBytes.html">/sdk-for-flutter-explore-core-engine-sdkoptions-cachesizeinbytes</a>
↔ int
</dt>
<dd>
  Desired upper bound of application size in bytes. When cached data exceeds cache_size, least recently used data will be removed.
Default value 256MB
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="catalogConfigurations">
<a href="../core.engine/SDKOptions/catalogConfigurations.html">/sdk-for-flutter-explore-core-engine-sdkoptions-catalogconfigurations</a>
↔ List&lt;<wbr/><a href="../core.engine/CatalogConfiguration-class.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-class</a>&gt;
</dt>
<dd>
  This field specifies how the <a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a> should access, use and store
data for different catalogs. You can access default catalogs on the HERE platform and
also custom catalogs such as for self-hosted or BYOD (bring your own data) use cases.
For further information about catalogs and related concepts see
<a href="../core.engine/CatalogConfiguration-class.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-class</a>
<div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="customEngineOptions">
<a href="../core.engine/SDKOptions/customEngineOptions.html">/sdk-for-flutter-explore-core-engine-sdkoptions-customengineoptions</a>
↔ Map&lt;<wbr/><a href="../core.engine/EngineBaseURL.html">/sdk-for-flutter-explore-core-engine-enginebaseurl</a>, <a href="../core.engine/EngineOptions-class.html">/sdk-for-flutter-explore-core-engine-engineoptions-class</a>&gt;
</dt>
<dd>
  Set custom options for SDK Engines. This includes:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="customOptions">
<a href="../core.engine/SDKOptions/customOptions.html">/sdk-for-flutter-explore-core-engine-sdkoptions-customoptions</a>
↔ <a href="../core/Metadata-class.html">/sdk-for-flutter-explore-core-metadata-class</a>?
</dt>
<dd>
  Options that define custom behavior for the HERE SDK. These settings allow fine-tuning
of internal thread pools and resource management for advanced use cases.
These options are intended for <em>internal</em> usage only and should not be modified unless
instructed by HERE support.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="dataPath">
<a href="../core.engine/SDKOptions/dataPath.html">/sdk-for-flutter-explore-core-engine-sdkoptions-datapath</a>
↔ String
</dt>
<dd>
  Path used for storing application internal data, such as the offline search index and other essential data required for proper functionality.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../core.engine/SDKOptions/hashCode.html">/sdk-for-flutter-explore-core-engine-sdkoptions-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="layerConfiguration">
<a href="../core.engine/SDKOptions/layerConfiguration.html">/sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration</a>
↔ <a href="../core.engine/LayerConfiguration-class.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-class</a>
</dt>
<dd>
  Defines a list of data features that can be enabled / disabled. Once set to <a href="../core.engine/SDKOptions-class.html">/sdk-for-flutter-explore-core-engine-sdkoptions-class</a> when
a new HERE SDK is constructed, it will affect the map cache and offline maps.
When disabling certain features, less data will be prefetched when the map is rendered. Map
data that was already cached will not be removed until the least recently used strategy (LRU)
applies. That means you cannot remove any content from the map cache by updating the
<a href="../core.engine/LayerConfiguration-class.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-class</a>. However, for new map data, it will be applied.
For offline maps, this <a href="../core.engine/LayerConfiguration-class.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-class</a> can reduce the download size of all regions.
Note that the <a href="../core.engine/LayerConfiguration-class.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-class</a> is applied globally to all regions that will be downloaded
in the future. It will not affect already downloaded regions. Updating a region will also
not update the <a href="../core.engine/LayerConfiguration-class.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-class</a>. Only the <a href="../core.engine/LayerConfiguration-class.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-class</a> will be used that was set
globally when a region was downloaded for the first time. If you want to update the
<a href="../core.engine/LayerConfiguration-class.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-class</a> for an already downloaded region, please delete the region and download it again.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lowMemoryMode">
<a href="../core.engine/SDKOptions/lowMemoryMode.html">/sdk-for-flutter-explore-core-engine-sdkoptions-lowmemorymode</a>
↔ bool
</dt>
<dd>
  If an application runs in a memory-constrained environment, enable this option to reduce the HERE SDK's memory footprint.
When set to <code>true</code> configures internal memory caches to consume less memory.
Reduction in cache sizes also reduces performance of the HERE SDK.
In order to release memory occupied by internal caches see <a href="../core.engine/SDKNativeEngine/purgeMemoryCaches.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-purgememorycaches</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="networkSettings">
<a href="../core.engine/SDKOptions/networkSettings.html">/sdk-for-flutter-explore-core-engine-sdkoptions-networksettings</a>
↔ <a href="../core.engine/NetworkSettings-class.html">/sdk-for-flutter-explore-core-engine-networksettings-class</a>
</dt>
<dd>
  Network settings to use at the start. Some of those settings can be changed later.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="offlineMode">
<a href="../core.engine/SDKOptions/offlineMode.html">/sdk-for-flutter-explore-core-engine-sdkoptions-offlinemode</a>
↔ bool
</dt>
<dd>
  Sets offline mode for the HERE SDK. Defaults to <code>false</code>. When enabled, this prevents the
HERE SDK from initiating any online connection from starting.
The mode can be disabled or enabled again at any time via <a href="../core.engine/SDKNativeEngine/isOfflineMode.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-isofflinemode</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="persistentMapStoragePath">
<a href="../core.engine/SDKOptions/persistentMapStoragePath.html">/sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath</a>
↔ String
</dt>
<dd>
  Path to store persistent map data. This should be the a path to the desired location for which the application has read/write permissions.
The path can be on internal or external storage.
By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="politicalView">
<a href="../core.engine/SDKOptions/politicalView.html">/sdk-for-flutter-explore-core-engine-sdkoptions-politicalview</a>
↔ String
</dt>
<dd>
  Geopolitical view of a country, defined as a three letter country code by ISO 3166-1 alpha-3. Each disputed territory has
an international and an alternative geopolitical view.
When set, the map view will show all country boundaries according to the geopolitical view of the country that has been set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core.engine/SDKOptions/runtimeType.html">/sdk-for-flutter-explore-core-engine-sdkoptions-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="scope">
<a href="../core.engine/SDKOptions/scope.html">/sdk-for-flutter-explore-core-engine-sdkoptions-scope</a>
↔ String
</dt>
<dd>
  Optional project ID to set the project scope of the login session. Not used if empty.
see also <a href="https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/manage-projects.html">Manage Projects</a>
and <a href="https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/concepts.html">IAM Concepts</a>
<div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../core.engine/SDKOptions/noSuchMethod.html">/sdk-for-flutter-explore-core-engine-sdkoptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core.engine/SDKOptions/toString.html">/sdk-for-flutter-explore-core-engine-sdkoptions-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
<a href="../core.engine/SDKOptions/operator_equals.html">/sdk-for-flutter-explore-core-engine-sdkoptions-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

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
<li class="self-crumb">SDKOptions class</li>
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

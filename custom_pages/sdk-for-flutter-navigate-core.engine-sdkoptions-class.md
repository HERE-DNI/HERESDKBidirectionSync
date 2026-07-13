---
title: "SDKOptions class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-sdkoptions-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/SDKOptions-class-sidebar.html">

<div>

# <span class="kind-class">SDKOptions</span> class

</div>

<div class="section desc markdown">

SDKOptions provide an alternative way to set or update the HERE SDK credentials and other parameters at runtime to initialize the <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-sdkoptions-withauthenticationmode">SDKOptions.withAuthenticationMode</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withAuthenticationMode-param-authenticationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-authenticationmode-class">AuthenticationMode</a></span> <span class="parameter-name">authenticationMode</span></span>)</span>  
Constructs a SDKOptions from authentication mode.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-actiononcachelock">actionOnCacheLock</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-engine-sdkoptionsactiononcachelock">SDKOptionsActionOnCacheLock</a></span>  
Specifies action to perform when cache folder is locked by another process. Default value is <a href="sdk-for-flutter-navigate-core-engine-sdkoptionsactiononcachelock">SDKOptionsActionOnCacheLock.waitLockingAppFinish</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-authenticationmode">authenticationMode</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-engine-authenticationmode-class">AuthenticationMode</a></span>  
Encapsulates Authentication method and parameters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-autoupdateofonlinecache">autoUpdateOfOnlineCache</a></span> <span class="signature">↔ bool</span>  
Parameter to enable automatic cache updates.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-billingtag">billingTag</a></span> <span class="signature">↔ String?</span>  
Internal to HERE SDK. DO NOT USE THIS YET.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-cachepath">cachePath</a></span> <span class="signature">↔ String</span>  
Path to be used for caching purposes. It should be a path to the desired location where the application has read/write permissions. The path can be on internal or external storage. By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-cachesizeinbytes">cacheSizeInBytes</a></span> <span class="signature">↔ int</span>  
Desired upper bound of application size in bytes. When cached data exceeds cache_size, least recently used data will be removed. Default value 256MB

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-catalogconfigurations">catalogConfigurations</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-catalogconfiguration-class">CatalogConfiguration</a></span>\></span></span>  
This field specifies how the <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> should access, use and store data for different catalogs. You can access default catalogs on the HERE platform and also custom catalogs such as for self-hosted or BYOD (bring your own data) use cases. For further information about catalogs and related concepts see <a href="sdk-for-flutter-navigate-core-engine-catalogconfiguration-class">CatalogConfiguration</a>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-customengineoptions">customEngineOptions</a></span> <span class="signature">↔ Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-enginebaseurl">EngineBaseURL</a></span>, <span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-engineoptions-class">EngineOptions</a></span>\></span></span>  
Set custom options for SDK Engines. This includes:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-customoptions">customOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-metadata-class">Metadata</a>?</span>  
Options that define custom behavior for the HERE SDK. These settings allow fine-tuning of internal thread pools and resource management for advanced use cases. These options are intended for *internal* usage only and should not be modified unless instructed by HERE support.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-datapath">dataPath</a></span> <span class="signature">↔ String</span>  
Path used for storing application internal data, such as the offline search index and other essential data required for proper functionality.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration">layerConfiguration</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a></span>  
Defines a list of data features that can be enabled / disabled. Once set to <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-class">SDKOptions</a> when a new HERE SDK is constructed, it will affect the map cache and offline maps. When disabling certain features, less data will be prefetched when the map is rendered. Map data that was already cached will not be removed until the least recently used strategy (LRU) applies. That means you cannot remove any content from the map cache by updating the <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a>. However, for new map data, it will be applied. For offline maps, this <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a> can reduce the download size of all regions. Note that the <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a> is applied globally to all regions that will be downloaded in the future. It will not affect already downloaded regions. Updating a region will also not update the <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a>. Only the <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a> will be used that was set globally when a region was downloaded for the first time. If you want to update the <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a> for an already downloaded region, please delete the region and download it again.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-lowmemorymode">lowMemoryMode</a></span> <span class="signature">↔ bool</span>  
If an application runs in a memory-constrained environment, enable this option to reduce the HERE SDK's memory footprint. When set to `true` configures internal memory caches to consume less memory. Reduction in cache sizes also reduces performance of the HERE SDK. In order to release memory occupied by internal caches see <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-purgememorycaches">SDKNativeEngine.purgeMemoryCaches</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-networksettings">networkSettings</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-engine-networksettings-class">NetworkSettings</a></span>  
Network settings to use at the start. Some of those settings can be changed later.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-offlinemode">offlineMode</a></span> <span class="signature">↔ bool</span>  
Sets offline mode for the HERE SDK. Defaults to `false`. When enabled, this prevents the HERE SDK from initiating any online connection from starting. The mode can be disabled or enabled again at any time via <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-isofflinemode">SDKNativeEngine.isOfflineMode</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath">persistentMapStoragePath</a></span> <span class="signature">↔ String</span>  
Path to store persistent map data. This should be the a path to the desired location for which the application has read/write permissions. The path can be on internal or external storage. By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-politicalview">politicalView</a></span> <span class="signature">↔ String</span>  
Geopolitical view of a country, defined as a three letter country code by ISO 3166-1 alpha-3. Each disputed territory has an international and an alternative geopolitical view. When set, the map view will show all country boundaries according to the geopolitical view of the country that has been set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-scope">scope</a></span> <span class="signature">↔ String</span>  
Optional project ID to set the project scope of the login session. Not used if empty. see also <a href="https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/manage-projects.html">Manage Projects</a> and <a href="https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/concepts.html">IAM Concepts</a>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


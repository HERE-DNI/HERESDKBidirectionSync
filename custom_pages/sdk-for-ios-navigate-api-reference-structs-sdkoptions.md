---
title: "SDKOptions"
slug: "sdk-for-ios-navigate-api-reference-structs-sdkoptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SDKOptions"></a>
<a title="SDKOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-core">Core</a>

        SDKOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SDKOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SDKOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>SDKOptions provide an alternative way to set or update the HERE SDK credentials and other
parameters at runtime to initialize the <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV5scopeSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/scope"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV5scopeSSvp">scope</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional project ID to set the project scope of the login session. Not used if empty.
see also <a href="https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/manage-projects.html">Manage Projects</a>
and <a href="https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/concepts.html">IAM Concepts</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">scope</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV9cachePathSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cachePath"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV9cachePathSSvp">cachePath</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Path to be used for caching purposes. It should be a path to the desired location where the application has read/write permissions.
The path can be on internal or external storage.
By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths:
<code>&lt;Application_Home&gt;/Library/Caches</code>
.
If an absolute path is set, it will be used instead.
If a relative path is set then directory <code>&lt;Application_Home&gt;/Library/Caches</code>
is used as parent path.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">cachePath</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV16cacheSizeInBytess5Int64Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cacheSizeInBytes"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV16cacheSizeInBytess5Int64Vvp">cacheSizeInBytes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Desired upper bound of application size in bytes. When cached data exceeds cache_size, least recently used data will be removed.
Default value 256MB</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">cacheSizeInBytes</span><span class="p">:</span> <span class="kt">Int64</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV8dataPathSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dataPath"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV8dataPathSSvp">dataPath</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Path used for storing application internal data, such as the offline search index and other essential data required for proper functionality.</p>
<p><strong>Note:</strong> For common use cases, prefer <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code>, or keep the default paths. Use <code>dataPath</code> only as a fallback if <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code> is not writable, for example, when you have an agreement with HERE to flash data at factory time.</p>
<p>By default, this returns an empty string. In this case, the same path as <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code> will be used.
If an absolute path is set, it will be used instead.
If a relative path is set then directory <code>Application Library directory</code>
is used as parent path.
Application must have read/write permissions to the given desired path.
It is recommended that the application has exclusive access to this path.
Avoid using shared or public directories such as <code>Download</code> or <code>Documents</code>.
Using such directories may cause certain HERE SDK features to behave with limitations.
For example, index creation for offline search may fail or not function as expected.
It is recommended not to use the application cache paths like <code>&lt;Application_Home&gt;/Library/Caches</code>
, since operating system manages data in this location
and data can be deleted if the device is low on storage space, which will result in application malfunction.
The path can be on internal or external storage. The internal storage is recommended due to the file I/O speed.
Note:
If the <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code> is writable, <code>dataPath</code> can be left empty.
If the <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code> is not writable, <code>dataPath</code> must be set and also be writable. Note that <code>dataPath</code> is used to store essential HERE SDK data.</p>
<p><strong>Important:</strong>
There is no automatic migration of stored data between the <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code> and the <code>dataPath</code>. For ease of management,
it’s recommended to set the persistence path as writable and ignore <code>dataPath</code>.
If <code>dataPath</code> is set differently from the <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code>, some data that would typically be saved in the <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code> will now be saved to <code>dataPath</code>.
If <code>dataPath</code> is set and later unset, any data stored there will remain inaccessible and will not be migrated back.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">dataPath</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/persistentMapStoragePath"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">persistentMapStoragePath</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Path to store persistent map data. This should be the a path to the desired location for which the application has read/write permissions.
The path can be on internal or external storage.
By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths:
<code>Application Library directory</code>
.
If an absolute path is set, it will be used instead.
If a relative path is set then directory <code>Application Library directory</code>
is used as parent path.
<strong>Note</strong>: Offline maps stored at <code>&lt;persistent_map_storage_path&gt;/v1/&lt;access_key_id&gt;/ocm-map/</code>, where <code>&lt;access_key_id&gt;</code> is
taken from <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV18authenticationModeAA014AuthenticationD0Cvp">SDKOptions.authenticationMode</a></code>.
When <code>SDKOptions</code> initialized with <code>AuthenticationMode.withToken</code> or <code>AuthenticationMode.withExternal</code>, then <code>&lt;access_key_id&gt;</code> left empty.</p>
<p>Note: If the persistent map storage location has the read only permission, then the <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV8dataPathSSvp">SDKOptions.dataPath</a></code> must be configured.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">persistentMapStoragePath</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV13politicalViewSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/politicalView"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV13politicalViewSSvp">politicalView</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geopolitical view of a country, defined as a three letter country code by ISO 3166-1 alpha-3. Each disputed territory has
an international and an alternative geopolitical view.
When set, the map view will show all country boundaries according to the geopolitical view of the country that has been set.</p>
<p>Note: Defaults to an empty string which enables the international view.</p>
<p>This is a beta feature and thus there can be bugs and unexpected behavior.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">politicalView</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV11offlineModeSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offlineMode"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV11offlineModeSbvp">offlineMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets offline mode for the HERE SDK. Defaults to <code>false</code>. When enabled, this prevents the
HERE SDK from initiating any online connection from starting.
The mode can be disabled or enabled again at any time via <code><a href="../Classes/SDKNativeEngine.html#/s:7heresdk15SDKNativeEngineC13isOfflineModeSbvp">SDKNativeEngine.isOfflineMode</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">offlineMode</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/layerConfiguration"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">layerConfiguration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines a list of data features that can be enabled / disabled. Once set to <code>SDKOptions</code> when
a new HERE SDK is constructed, it will affect the map cache and offline maps.
When disabling certain features, less data will be prefetched when the map is rendered. Map
data that was already cached will not be removed until the least recently used strategy (LRU)
applies. That means you cannot remove any content from the map cache by updating the
<code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code>. However, for new map data, it will be applied.
For offline maps, this <code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code> can reduce the download size of all regions.
Note that the <code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code> is applied globally to all regions that will be downloaded
in the future. It will not affect already downloaded regions. Updating a region will also
not update the <code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code>. Only the <code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code> will be used that was set
globally when a region was downloaded for the first time. If you want to update the
<code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code> for an already downloaded region, please delete the region and download it again.</p>
<p>Please also note</p>
<ul>
<li>The <code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code> is only applicable for the HERE SDK (Navigate) that contains the offline maps
feature. It has no effect on other licenses.</li>
<li>The <code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code> cannot be set separately for a region, it will be applied globally
for all regions that will be downloaded in the future.</li>
<li>It is not possible to specify a separate <code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code> for the map cache and offline maps.
The <code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code> will be always applied to both.</li>
<li>The <code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code> does affect the map cache when a device has connectivity. Even
when a device has connectivity it will only download the specified layers.</li>
<li>This is a beta feature and thus there can be bugs and unexpected behavior.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">layerConfiguration</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV21catalogConfigurationsSayAA20CatalogConfigurationVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/catalogConfigurations"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV21catalogConfigurationsSayAA20CatalogConfigurationVGvp">catalogConfigurations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This field specifies how the <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code> should access, use and store
data for different catalogs. You can access default catalogs on the HERE platform and
also custom catalogs such as for self-hosted or BYOD (bring your own data) use cases.
For further information about catalogs and related concepts see
<code><a href="sdk-for-ios-navigate-api-reference-structs-catalogconfiguration">CatalogConfiguration</a></code></p>
<p><strong>Note:</strong>
This API is only available for the Navigate license. It has no affect on other license.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">catalogConfigurations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-catalogconfiguration">CatalogConfiguration</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV23autoUpdateOfOnlineCacheSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/autoUpdateOfOnlineCache"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV23autoUpdateOfOnlineCacheSbvp">autoUpdateOfOnlineCache</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Parameter to enable automatic cache updates.</p>
<p>When it is false, the cache will always use the same map version as
offline maps. If offline maps are updated, the cache will be also updated.
The cache version will never be older than the offline maps version.</p>
<p>When it is true, the cache will be automatically updated to use the latest map data
that is available. In that case, the cache may contain map data that is newer than
the offline maps data. Note that auto updates may also lead to increased network traffic, as
the cached data will be evicted tile-by-tile before it is filled with newer map data. This
process continues everytime the user views a new map view area until the data is replaced.
Once also the offline map data is updated by the user, both map versions will
be the same again.</p>
<p>If the value is also specified via the manifest (Android) or plist (iOS), than the
value set via <code>SDKOptions</code> will overrule the value that was set in manifest/plist - until
the current session ends and the value is read/set again.</p>
<p>Note that offline maps are only available for the Navigate license.</p>
<p>Defaults to <code>false</code>.</p>
<p><strong>Note:</strong> Do not use this yet, the behavior of this feature may be inconsistent.
Once it will be usable, it will be announced in the regular HERE SDK release notes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">autoUpdateOfOnlineCache</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV19customEngineOptionsSDyAA0D7BaseURLOAA0dE0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/customEngineOptions"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV19customEngineOptionsSDyAA0D7BaseURLOAA0dE0VGvp">customEngineOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Set custom options for SDK Engines. This includes:</p>
<ul>
<li><code>custom_base_url</code>: Allows engines to use custom base URLs for alternative services.
By default, the available endpoints use HERE backend endpoints.
If unsupported base URLs are specified, the related features will become non-functional.
Please contact your HERE representative to learn about possible custom base URL usage options.</li>
<li><code>custom_authentication_mode</code>: Enables bearer authentication mode for engines,
which adds or omits the header (“Authorization”, “Bearer $Token”) to each
online request made by the module the object is added to.
The token (if used) can be provided directly or retrieved via key/secret
from a dedicated backend.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">customEngineOptions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-enginebaseurl">EngineBaseURL</a></span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-engineoptions">EngineOptions</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV18authenticationModeAA014AuthenticationD0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/authenticationMode"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV18authenticationModeAA014AuthenticationD0Cvp">authenticationMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Encapsulates Authentication method and parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">authenticationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-authenticationmode">AuthenticationMode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV15networkSettingsAA07NetworkD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/networkSettings"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV15networkSettingsAA07NetworkD0Vvp">networkSettings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Network settings to use at the start. Some of those settings can be changed later.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">networkSettings</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-networksettings">NetworkSettings</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV13lowMemoryModeSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lowMemoryMode"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV13lowMemoryModeSbvp">lowMemoryMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If an application runs in a memory-constrained environment, enable this option to reduce the HERE SDK’s memory footprint.
When set to <code>true</code> configures internal memory caches to consume less memory.
Reduction in cache sizes also reduces performance of the HERE SDK.
In order to release memory occupied by internal caches see <code><a href="../Classes/SDKNativeEngine.html#/s:7heresdk15SDKNativeEngineC17purgeMemoryCaches8strategyyAC05PurgeE8StrategyO_tF">SDKNativeEngine.purgeMemoryCaches(...)</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lowMemoryMode</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV10billingTagSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/billingTag"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV10billingTagSSSgvp">billingTag</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Internal to HERE SDK. DO NOT USE THIS YET.</p>
<p><strong>Warning:</strong> This is a placeholder and under developement. We will announce its availability in our changelog once it is ready for use.</p>
<p>A parameter to set a billing tag to track your HERE platform usage across the various HERE services your application may contact.
For more information on the billing tag, see our
<a href="https://www.here.com/docs/bundle/cost-management-developer-guide/page/topics/tutorial-billing-tags.html">cost management guide</a>.
The tag needs to follow the format as described in the guide or it will be ignored.
The parameter defaults to <code>nil</code>, which also means that the tag is ignored for all requests.</p>
<p><strong>Note:</strong> The billing tag is optional, but when set, it can help you to understand
how often your app uses certain services, for example, the number of hits to our
HERE backend routing services. For more details on tracking such details,
please consult the <em>cost management guide</em> or get in touch with the HERE billing team.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">billingTag</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV13customOptionsAA8MetadataCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/customOptions"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV13customOptionsAA8MetadataCSgvp">customOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options that define custom behavior for the HERE SDK. These settings allow fine-tuning
of internal thread pools and resource management for advanced use cases.
These options are intended for <em>internal</em> usage only and should not be modified unless
instructed by HERE support.</p>
<p>Note: This is a <em>beta</em> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">customOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-metadata">Metadata</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV18authenticationModeAcA014AuthenticationD0C_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(authenticationMode:)"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV18authenticationModeAcA014AuthenticationD0C_tcfc">init(authenticationMode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a SDKOptions from authentication mode. Other fields are filled with default values.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">authenticationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-authenticationmode">AuthenticationMode</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>authenticationMode</em>
</code>
</td>
<td>
<div>
<p>Authentication Mode used for obtaining an access token.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
} </HTMLBlock>

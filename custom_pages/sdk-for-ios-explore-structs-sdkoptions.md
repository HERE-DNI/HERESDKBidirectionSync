---
title: "SDKOptions Structure Reference"
slug: "sdk-for-ios-explore-structs-sdkoptions"
---

# SDKOptions

<div class="declaration">

<div class="language">

``` highlight
public struct SDKOptions : Hashable
```

</div>

</div>

SDKOptions provide an alternative way to set or update the HERE SDK credentials and other parameters at runtime to initialize the <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV5scopeSSvp"></span>` `<span id="//apple_ref/swift/Property/scope" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV5scopeSSvp" class="token"><code>scope</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional project ID to set the project scope of the login session. Not used if empty. see also <a href="https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/manage-projects.html">Manage Projects</a> and <a href="https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/concepts.html">IAM Concepts</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var scope: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV9cachePathSSvp"></span>` `<span id="//apple_ref/swift/Property/cachePath" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV9cachePathSSvp" class="token"><code>cachePath</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Path to be used for caching purposes. It should be a path to the desired location where the application has read/write permissions. The path can be on internal or external storage. By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths: `<Application_Home>/Library/Caches` . If an absolute path is set, it will be used instead. If a relative path is set then directory `<Application_Home>/Library/Caches` is used as parent path.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cachePath: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV16cacheSizeInBytess5Int64Vvp"></span>` `<span id="//apple_ref/swift/Property/cacheSizeInBytes" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV16cacheSizeInBytess5Int64Vvp" class="token"><code>cacheSizeInBytes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Desired upper bound of application size in bytes. When cached data exceeds cache_size, least recently used data will be removed. Default value 256MB

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cacheSizeInBytes: Int64
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV8dataPathSSvp"></span>` `<span id="//apple_ref/swift/Property/dataPath" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV8dataPathSSvp" class="token"><code>dataPath</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Path used for storing application internal data, such as the offline search index and other essential data required for proper functionality.

  **Note:** For common use cases, prefer <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a>, or keep the default paths. Use `dataPath` only as a fallback if <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a> is not writable, for example, when you have an agreement with HERE to flash data at factory time.

  By default, this returns an empty string. In this case, the same path as <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a> will be used. If an absolute path is set, it will be used instead. If a relative path is set then directory `Application Library directory` is used as parent path. Application must have read/write permissions to the given desired path. It is recommended that the application has exclusive access to this path. Avoid using shared or public directories such as `Download` or `Documents`. Using such directories may cause certain HERE SDK features to behave with limitations. For example, index creation for offline search may fail or not function as expected. It is recommended not to use the application cache paths like `<Application_Home>/Library/Caches` , since operating system manages data in this location and data can be deleted if the device is low on storage space, which will result in application malfunction. The path can be on internal or external storage. The internal storage is recommended due to the file I/O speed. Note: If the <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a> is writable, `dataPath` can be left empty. If the <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a> is not writable, `dataPath` must be set and also be writable. Note that `dataPath` is used to store essential HERE SDK data.

  **Important:** There is no automatic migration of stored data between the <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a> and the `dataPath`. For ease of management, it’s recommended to set the persistence path as writable and ignore `dataPath`. If `dataPath` is set differently from the <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a>, some data that would typically be saved in the <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a> will now be saved to `dataPath`. If `dataPath` is set and later unset, any data stored there will remain inaccessible and will not be migrated back.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var dataPath: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp"></span>` `<span id="//apple_ref/swift/Property/persistentMapStoragePath" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp" class="token"><code>persistentMapStoragePath</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Path to store persistent map data. This should be the a path to the desired location for which the application has read/write permissions. The path can be on internal or external storage. By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths: `Application Library directory` . If an absolute path is set, it will be used instead. If a relative path is set then directory `Application Library directory` is used as parent path. **Note**: Offline maps stored at `<persistent_map_storage_path>/v1/<access_key_id>/ocm-map/`, where `<access_key_id>` is taken from <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV18authenticationModeAA014AuthenticationD0Cvp">`SDKOptions.authenticationMode`</a>. When `SDKOptions` initialized with `AuthenticationMode.withToken` or `AuthenticationMode.withExternal`, then `<access_key_id>` left empty.

  Note: If the persistent map storage location has the read only permission, then the <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV8dataPathSSvp">`SDKOptions.dataPath`</a> must be configured.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var persistentMapStoragePath: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV13politicalViewSSvp"></span>` `<span id="//apple_ref/swift/Property/politicalView" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV13politicalViewSSvp" class="token"><code>politicalView</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geopolitical view of a country, defined as a three letter country code by ISO 3166-1 alpha-3. Each disputed territory has an international and an alternative geopolitical view. When set, the map view will show all country boundaries according to the geopolitical view of the country that has been set.

  Note: Defaults to an empty string which enables the international view.

  This is a beta feature and thus there can be bugs and unexpected behavior.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var politicalView: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV11offlineModeSbvp"></span>` `<span id="//apple_ref/swift/Property/offlineMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV11offlineModeSbvp" class="token"><code>offlineMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets offline mode for the HERE SDK. Defaults to `false`. When enabled, this prevents the HERE SDK from initiating any online connection from starting. The mode can be disabled or enabled again at any time via <a href="sdk-for-ios-explore-classes-sdknativeengine#/s:7heresdk15SDKNativeEngineC13isOfflineModeSbvp">`SDKNativeEngine.isOfflineMode`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var offlineMode: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp"></span>` `<span id="//apple_ref/swift/Property/layerConfiguration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp" class="token"><code>layerConfiguration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines a list of data features that can be enabled / disabled. Once set to `SDKOptions` when a new HERE SDK is constructed, it will affect the map cache and offline maps. When disabling certain features, less data will be prefetched when the map is rendered. Map data that was already cached will not be removed until the least recently used strategy (LRU) applies. That means you cannot remove any content from the map cache by updating the <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a>. However, for new map data, it will be applied. For offline maps, this <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a> can reduce the download size of all regions. Note that the <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a> is applied globally to all regions that will be downloaded in the future. It will not affect already downloaded regions. Updating a region will also not update the <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a>. Only the <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a> will be used that was set globally when a region was downloaded for the first time. If you want to update the <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a> for an already downloaded region, please delete the region and download it again.

  Please also note

  - The <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a> is only applicable for the HERE SDK (Navigate) that contains the offline maps feature. It has no effect on other licenses.
  - The <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a> cannot be set separately for a region, it will be applied globally for all regions that will be downloaded in the future.
  - It is not possible to specify a separate <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a> for the map cache and offline maps. The <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a> will be always applied to both.
  - The <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a> does affect the map cache when a device has connectivity. Even when a device has connectivity it will only download the specified layers.
  - This is a beta feature and thus there can be bugs and unexpected behavior.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var layerConfiguration: LayerConfiguration
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV21catalogConfigurationsSayAA20CatalogConfigurationVGvp"></span>` `<span id="//apple_ref/swift/Property/catalogConfigurations" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV21catalogConfigurationsSayAA20CatalogConfigurationVGvp" class="token"><code>catalogConfigurations</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This field specifies how the <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a> should access, use and store data for different catalogs. You can access default catalogs on the HERE platform and also custom catalogs such as for self-hosted or BYOD (bring your own data) use cases. For further information about catalogs and related concepts see <a href="sdk-for-ios-explore-structs-catalogconfiguration">`CatalogConfiguration`</a>

  **Note:** This API is only available for the Navigate license. It has no affect on other license.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var catalogConfigurations: [CatalogConfiguration]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV23autoUpdateOfOnlineCacheSbvp"></span>` `<span id="//apple_ref/swift/Property/autoUpdateOfOnlineCache" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV23autoUpdateOfOnlineCacheSbvp" class="token"><code>autoUpdateOfOnlineCache</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Parameter to enable automatic cache updates.

  When it is false, the cache will always use the same map version as offline maps. If offline maps are updated, the cache will be also updated. The cache version will never be older than the offline maps version.

  When it is true, the cache will be automatically updated to use the latest map data that is available. In that case, the cache may contain map data that is newer than the offline maps data. Note that auto updates may also lead to increased network traffic, as the cached data will be evicted tile-by-tile before it is filled with newer map data. This process continues everytime the user views a new map view area until the data is replaced. Once also the offline map data is updated by the user, both map versions will be the same again.

  If the value is also specified via the manifest (Android) or plist (iOS), than the value set via `SDKOptions` will overrule the value that was set in manifest/plist - until the current session ends and the value is read/set again.

  Note that offline maps are only available for the Navigate license.

  Defaults to `false`.

  **Note:** Do not use this yet, the behavior of this feature may be inconsistent. Once it will be usable, it will be announced in the regular HERE SDK release notes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var autoUpdateOfOnlineCache: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV19customEngineOptionsSDyAA0D7BaseURLOAA0dE0VGvp"></span>` `<span id="//apple_ref/swift/Property/customEngineOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV19customEngineOptionsSDyAA0D7BaseURLOAA0dE0VGvp" class="token"><code>customEngineOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Set custom options for SDK Engines. This includes:

  - `custom_base_url`: Allows engines to use custom base URLs for alternative services. By default, the available endpoints use HERE backend endpoints. If unsupported base URLs are specified, the related features will become non-functional. Please contact your HERE representative to learn about possible custom base URL usage options.
  - `custom_authentication_mode`: Enables bearer authentication mode for engines, which adds or omits the header (“Authorization”, “Bearer \$Token”) to each online request made by the module the object is added to. The token (if used) can be provided directly or retrieved via key/secret from a dedicated backend. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var customEngineOptions: [EngineBaseURL : EngineOptions]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV18authenticationModeAA014AuthenticationD0Cvp"></span>` `<span id="//apple_ref/swift/Property/authenticationMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV18authenticationModeAA014AuthenticationD0Cvp" class="token"><code>authenticationMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Encapsulates Authentication method and parameters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var authenticationMode: AuthenticationMode
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV15networkSettingsAA07NetworkD0Vvp"></span>` `<span id="//apple_ref/swift/Property/networkSettings" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV15networkSettingsAA07NetworkD0Vvp" class="token"><code>networkSettings</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Network settings to use at the start. Some of those settings can be changed later.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var networkSettings: NetworkSettings
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV13lowMemoryModeSbvp"></span>` `<span id="//apple_ref/swift/Property/lowMemoryMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV13lowMemoryModeSbvp" class="token"><code>lowMemoryMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If an application runs in a memory-constrained environment, enable this option to reduce the HERE SDK’s memory footprint. When set to `true` configures internal memory caches to consume less memory. Reduction in cache sizes also reduces performance of the HERE SDK. In order to release memory occupied by internal caches see

      SDKNativeEngine.purgeMemoryCaches(...)

  .
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lowMemoryMode: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV10billingTagSSSgvp"></span>` `<span id="//apple_ref/swift/Property/billingTag" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV10billingTagSSSgvp" class="token"><code>billingTag</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Internal to HERE SDK. DO NOT USE THIS YET.

  **Warning:** This is a placeholder and under developement. We will announce its availability in our changelog once it is ready for use.

  A parameter to set a billing tag to track your HERE platform usage across the various HERE services your application may contact. For more information on the billing tag, see our <a href="https://www.here.com/docs/bundle/cost-management-developer-guide/page/topics/tutorial-billing-tags.html">cost management guide</a>. The tag needs to follow the format as described in the guide or it will be ignored. The parameter defaults to `nil`, which also means that the tag is ignored for all requests.

  **Note:** The billing tag is optional, but when set, it can help you to understand how often your app uses certain services, for example, the number of hits to our HERE backend routing services. For more details on tracking such details, please consult the *cost management guide* or get in touch with the HERE billing team.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var billingTag: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV13customOptionsAA8MetadataCSgvp"></span>` `<span id="//apple_ref/swift/Property/customOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV13customOptionsAA8MetadataCSgvp" class="token"><code>customOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options that define custom behavior for the HERE SDK. These settings allow fine-tuning of internal thread pools and resource management for advanced use cases. These options are intended for *internal* usage only and should not be modified unless instructed by HERE support.

  Note: This is a *beta* release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var customOptions: Metadata?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(authenticationMode: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a SDKOptions from authentication mode. Other fields are filled with default values.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( authenticationMode : AuthenticationMode )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>authenticationMode</code></em><code> </code></td>
  <td><div>
  <p>Authentication Mode used for obtaining an access token.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>


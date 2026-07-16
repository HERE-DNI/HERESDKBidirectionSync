---
title: "CatalogConfiguration Structure Reference"
slug: "sdk-for-ios-navigate-structs-catalogconfiguration"
---

# CatalogConfiguration

<div class="declaration">

<div class="language">

``` highlight
public struct CatalogConfiguration : Hashable
```

</div>

</div>

Using this class you can configure in the <a href="sdk-for-ios-navigate-structs-sdkoptions">`SDKOptions`</a>, how the <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a> should access, use and store the data for the desired catalog.

Using this class, you can access default catalogs on the HERE platform and also custom catalogs such as for self-hosted or BYOD (bring your own data) use cases.

For information on how the user can identify a catalog on the HERE platform, see <a href="sdk-for-ios-navigate-structs-desiredcatalog">`DesiredCatalog`</a> For further information about catalogs and related concepts see <a href="sdk-for-ios-navigate-structs-catalogidentifier">`CatalogIdentifier`</a>.

**Note:** This API is only applicable for the Navigate license.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV7catalogAA07DesiredB0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-catalog" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-catalogconfiguration#sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV7catalogAA07DesiredB0Vvp" class="token"><code>catalog</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The identifier for the desired catalog to be accessed on the HERE platform. See <a href="sdk-for-ios-navigate-structs-desiredcatalog">`DesiredCatalog`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var catalog: DesiredCatalog
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-desiredcatalog">DesiredCatalog</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV8patchHrnSSSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-patchHrn" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-catalogconfiguration#sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV8patchHrnSSSgvp" class="token"><code>patchHrn</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Some catalogs may have additional modifications to their data contained in an entirely separate catalog, called the patch catalog. This field indicates the HERE Resource Name (HRN) for the patch catalog. When this field is present, the catalog’s data as referenced by <a href="sdk-for-ios-navigate-structs-catalogconfiguration#sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV7catalogAA07DesiredB0Vvp">`CatalogConfiguration.catalog`</a> is merged with data from the patch catalog. If this field is `nil`, then incremental updates are disabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var patchHrn: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV21cacheExpirationPeriodSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-cacheExpirationPeriod" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-catalogconfiguration#sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV21cacheExpirationPeriodSdSgvp" class="token"><code>cacheExpirationPeriod</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Expiration time in seconds for how long the catalog data is retained in the map cache before it is removed. Cache path is specified by <a href="sdk-for-ios-navigate-structs-sdkoptions#sdk-for-ios-navigate-s-7heresdk10SDKOptionsV9cachePathSSvp">`SDKOptions.cachePath`</a>. If not set, the cache will be deleted on a Least Recently Used (LRU) basis.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cacheExpirationPeriod: TimeInterval?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV13allowDownloadSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-allowDownload" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-catalogconfiguration#sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV13allowDownloadSbvp" class="token"><code>allowDownload</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag to indicate if the data for this catalog is allowed to be stored in persistent storage for use with offline maps. The storage path is specified in <a href="sdk-for-ios-navigate-structs-sdkoptions#sdk-for-ios-navigate-s-7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a>. If set to false, the data is not stored in persistent storage and is only retained in the cache for a limited time (see <a href="sdk-for-ios-navigate-structs-catalogconfiguration#sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV21cacheExpirationPeriodSdSgvp">`CatalogConfiguration.cacheExpirationPeriod`</a>). Defaults to `true`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var allowDownload: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV7catalog8patchHrn21cacheExpirationPeriod13allowDownloadAcA07DesiredB0V_SSSgSdSgSbtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-catalog-patchHrn-cacheExpirationPeriod-allowDownload" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-catalogconfiguration#sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV7catalog8patchHrn21cacheExpirationPeriod13allowDownloadAcA07DesiredB0V_SSSgSdSgSbtcfc" class="token"><code>init(catalog:</code><wbr></wbr><code>patchHrn:</code><wbr></wbr><code>cacheExpirationPeriod:</code><wbr></wbr><code>allowDownload:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(catalog: DesiredCatalog, patchHrn: String? = nil, cacheExpirationPeriod: TimeInterval? = nil, allowDownload: Bool = true)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-desiredcatalog">DesiredCatalog</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV10getDefault11catalogTypeAcA0bG0O_tFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getDefault-catalogType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-catalogconfiguration#sdk-for-ios-navigate-s-7heresdk20CatalogConfigurationV10getDefault11catalogTypeAcA0bG0O_tFZ" class="token"><code>getDefault(catalogType:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the default catalog configuration for the specified catalog type. It uses the catalog version that was the latest at the time when the HERE SDK was built.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func getDefault(catalogType: CatalogType) -> CatalogConfiguration
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-catalogtype">CatalogType</a>

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
  <td><code> </code><em><code>catalogType</code></em><code> </code></td>
  <td><div>
  <p>Catalog type</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Instance of `CatalogConfiguration`.

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>


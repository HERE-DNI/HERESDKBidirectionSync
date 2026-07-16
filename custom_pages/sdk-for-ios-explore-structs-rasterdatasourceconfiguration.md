---
title: "RasterDataSourceConfiguration Structure Reference"
slug: "sdk-for-ios-explore-structs-rasterdatasourceconfiguration"
---

# RasterDataSourceConfiguration

<div class="declaration">

<div class="language">

``` highlight
public struct RasterDataSourceConfiguration
```

</div>

</div>

Called on the main thread after

    fromJsonFile()

method finishes loading the configuration.
</p>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV4nameSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-name" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration#sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV4nameSSvp" class="token"><code>name</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The unique name of the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var name: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV8providerAC8ProviderVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-provider" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration#sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV8providerAC8ProviderVvp" class="token"><code>provider</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Data provider configuration.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var provider: RasterDataSourceConfiguration.Provider
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration-provider">Provider</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV5cacheAC5CacheVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-cache" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration#sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV5cacheAC5CacheVvp" class="token"><code>cache</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Local cache configuration.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cache: RasterDataSourceConfiguration.Cache
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration-cache">Cache</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV013ignoreExpiredC0Sbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-ignoreExpiredData" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration#sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV013ignoreExpiredC0Sbvp" class="token"><code>ignoreExpiredData</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag indicating whether expired data should be ignored until refreshed. Default value is `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var ignoreExpiredData: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV4name8provider5cache013ignoreExpiredC0ACSS_AC8ProviderVAC5CacheVSbtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-name-provider-cache-ignoreExpiredData" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration#sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV4name8provider5cache013ignoreExpiredC0ACSS_AC8ProviderVAC5CacheVSbtcfc" class="token"><code>init(name:</code><wbr></wbr><code>provider:</code><wbr></wbr><code>cache:</code><wbr></wbr><code>ignoreExpiredData:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(name: String, provider: RasterDataSourceConfiguration.Provider, cache: RasterDataSourceConfiguration.Cache, ignoreExpiredData: Bool = false)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration-provider">Provider</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration-cache">Cache</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV8ProviderV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-Provider" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration#sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV8ProviderV" class="token"><code>Provider</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configuration of a data provider.

  <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration-provider" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Provider
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV5CacheV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-Cache" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration#sdk-for-ios-explore-s-7heresdk29RasterDataSourceConfigurationV5CacheV" class="token"><code>Cache</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configuration of a local data cache.

  <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration-cache" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Cache
  ```

  </div>

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


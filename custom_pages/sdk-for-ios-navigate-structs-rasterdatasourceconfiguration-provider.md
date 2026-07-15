---
title: "Provider Structure Reference"
slug: "sdk-for-ios-navigate-structs-rasterdatasourceconfiguration-provider"
---

# Provider

<div class="declaration">

<div class="language">

``` highlight
public struct Provider
```

</div>

</div>

Configuration of a data provider.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk29RasterDataSourceConfigurationV8ProviderV03urlF0ySSs5Int32V_A2Htcvp"></span>` `<span id="//apple_ref/swift/Property/urlProvider" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-rasterdatasourceconfiguration-provider#/s:7heresdk29RasterDataSourceConfigurationV8ProviderV03urlF0ySSs5Int32V_A2Htcvp" class="token"><code>urlProvider</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides a function that generates URLs based on tile coordinates and storage level.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var urlProvider: TileUrlRequestHandler
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29RasterDataSourceConfigurationV8ProviderV12tilingSchemeAA06TilingH0Ovp"></span>` `<span id="//apple_ref/swift/Property/tilingScheme" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-rasterdatasourceconfiguration-provider#/s:7heresdk29RasterDataSourceConfigurationV8ProviderV12tilingSchemeAA06TilingH0Ovp" class="token"><code>tilingScheme</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The tiling scheme used by this source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tilingScheme: TilingScheme
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29RasterDataSourceConfigurationV8ProviderV13storageLevelsSays5Int32VGvp"></span>` `<span id="//apple_ref/swift/Property/storageLevels" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-rasterdatasourceconfiguration-provider#/s:7heresdk29RasterDataSourceConfigurationV8ProviderV13storageLevelsSays5Int32VGvp" class="token"><code>storageLevels</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this provider to be used as a source of data. At storage level zero, the whole world is represented by one tile. At storage level 1 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The tiling process continues in this fashion until sufficient granularity has been achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds to the storage level. Depending on the available storage levels and the given camera zoom level, the appropriate z value of the tile key will be determined.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var storageLevels: [Int32]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29RasterDataSourceConfigurationV8ProviderV15hasAlphaChannelSbvp"></span>` `<span id="//apple_ref/swift/Property/hasAlphaChannel" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-rasterdatasourceconfiguration-provider#/s:7heresdk29RasterDataSourceConfigurationV8ProviderV15hasAlphaChannelSbvp" class="token"><code>hasAlphaChannel</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag indicating whether the image content contains an alpha channel for transparency. Default value is `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var hasAlphaChannel: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29RasterDataSourceConfigurationV8ProviderV7headersSDyS2SGSgvp"></span>` `<span id="//apple_ref/swift/Property/headers" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-rasterdatasourceconfiguration-provider#/s:7heresdk29RasterDataSourceConfigurationV8ProviderV7headersSDyS2SGSgvp" class="token"><code>headers</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The optional name-value pairs specifying HTTP headers that are passed with each tile request.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var headers: [String : String]?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(urlProvider: tilingScheme: storageLevels: hasAlphaChannel: headers: )

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
  public init ( urlProvider : @escaping TileUrlRequestHandler , tilingScheme : TilingScheme , storageLevels : [ Int32 ], hasAlphaChannel : Bool = false , headers : [ String : String ]? = nil )
  ```

  </pre>

  </div>

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


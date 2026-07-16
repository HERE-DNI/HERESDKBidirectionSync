---
title: "RasterDataSource Class Reference"
slug: "sdk-for-ios-explore-classes-rasterdatasource"
---

# RasterDataSource

<div class="declaration">

<div class="language">

``` highlight
public class RasterDataSource
```

``` highlight
extension RasterDataSource: NativeBase
```

``` highlight
extension RasterDataSource: Hashable
```

</div>

</div>

Data source to load map layers using a raster image format (jpg, png). The example below illustrates how to create a raster data source and how to link it to a newly created map layer.

``` highlight
  let rasterDataSource = RasterDataSource(mapContext, rasterDataSourceConfig)

  let layer = MapLayerBuilder()
     // The name and the type of the data source have to be provided.
     // In our case, the name of the raster data source is in rasterDataSourceConfig.
     .withDataSource(named: rasterDataSourceConfig.name, contentType: MapContentType.rasterImage)
     .forMap(map)
     .withName("rasterLayer")
     .build();
```

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16RasterDataSourceC7context13configurationAcA10MapContextC_AA0bcD13ConfigurationVtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-context-configuration" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-rasterdatasource#sdk-for-ios-explore-s-7heresdk16RasterDataSourceC7context13configurationAcA10MapContextC_AA0bcD13ConfigurationVtcfc" class="token"><code>init(context:</code><wbr></wbr><code>configuration:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a RasterDataSource instance with the provided data source configuration.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(context: MapContext, configuration: RasterDataSourceConfiguration)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcontext">MapContext</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration">RasterDataSourceConfiguration</a>

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
  <td><code> </code><em><code>context</code></em><code> </code></td>
  <td><div>
  <p>The map context to associate the data source with.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>configuration</code></em><code> </code></td>
  <td><div>
  <p>The data source configuration object to use.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16RasterDataSourceC7context13configuration8delegateAcA10MapContextC_AA0bcD13ConfigurationVAA0bcD8Delegate_ptcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-context-configuration-delegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-rasterdatasource#sdk-for-ios-explore-s-7heresdk16RasterDataSourceC7context13configuration8delegateAcA10MapContextC_AA0bcD13ConfigurationVAA0bcD8Delegate_ptcfc" class="token"><code>init(context:</code><wbr></wbr><code>configuration:</code><wbr></wbr><code>delegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a RasterDataSource instance with the provided data source configuration and registers a delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(context: MapContext, configuration: RasterDataSourceConfiguration, delegate: RasterDataSourceDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcontext">MapContext</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration">RasterDataSourceConfiguration</a>
  - <a href="sdk-for-ios-explore-protocols-rasterdatasourcedelegate">RasterDataSourceDelegate</a>

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
  <td><code> </code><em><code>context</code></em><code> </code></td>
  <td><div>
  <p>The map context to associate the data source with.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>configuration</code></em><code> </code></td>
  <td><div>
  <p>The data source configuration object to use.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The initial delegate to be registered for receiving state notifications. Due to the asynchronous nature of the data source initialization, the delegates registered later might miss some notifications. This delegate is guaranteed to receive all notifications.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16RasterDataSourceC7context4name04tileD0AcA10MapContextC_SSAA0b4TileD0_ptcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-context-name-tileSource" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-rasterdatasource#sdk-for-ios-explore-s-7heresdk16RasterDataSourceC7context4name04tileD0AcA10MapContextC_SSAA0b4TileD0_ptcfc" class="token"><code>init(context:</code><wbr></wbr><code>name:</code><wbr></wbr><code>tileSource:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a RasterDataSource instance with the provided raster tile source. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(context: MapContext, name: String, tileSource: RasterTileSource)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcontext">MapContext</a>
  - <a href="sdk-for-ios-explore-protocols-rastertilesource">RasterTileSource</a>

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
  <td><code> </code><em><code>context</code></em><code> </code></td>
  <td><div>
  <p>The map context to associate the data source with.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>name</code></em><code> </code></td>
  <td><div>
  <p>The unique name of the data source.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>tileSource</code></em><code> </code></td>
  <td><div>
  <p>The raster tile source.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16RasterDataSourceC7context4name04tileD08delegateAcA10MapContextC_SSAA0b4TileD0_pAA0bcD8Delegate_ptcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-context-name-tileSource-delegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-rasterdatasource#sdk-for-ios-explore-s-7heresdk16RasterDataSourceC7context4name04tileD08delegateAcA10MapContextC_SSAA0b4TileD0_pAA0bcD8Delegate_ptcfc" class="token"><code>init(context:</code><wbr></wbr><code>name:</code><wbr></wbr><code>tileSource:</code><wbr></wbr><code>delegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a RasterDataSource instance with the provided raster tile source and registers a delegate. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(context: MapContext, name: String, tileSource: RasterTileSource, delegate: RasterDataSourceDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcontext">MapContext</a>
  - <a href="sdk-for-ios-explore-protocols-rastertilesource">RasterTileSource</a>
  - <a href="sdk-for-ios-explore-protocols-rasterdatasourcedelegate">RasterDataSourceDelegate</a>

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
  <td><code> </code><em><code>context</code></em><code> </code></td>
  <td><div>
  <p>The map context to associate the data source with.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>name</code></em><code> </code></td>
  <td><div>
  <p>The unique name of the data source.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>tileSource</code></em><code> </code></td>
  <td><div>
  <p>The raster tile source.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The initial delegate to be registered for receiving state notifications. Due to the asynchronous nature of the data source initialization, the delegates registered later might miss some notifications. This delegate is guaranteed to receive all notifications.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16RasterDataSourceC19changeConfigurationyyAA0bcdF6UpdateVF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-changeConfiguration-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-rasterdatasource#sdk-for-ios-explore-s-7heresdk16RasterDataSourceC19changeConfigurationyyAA0bcdF6UpdateVF" class="token"><code>changeConfiguration(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Applies the configuration update to the data source. An example for a configuration update is the update to a new bearer token for authentication.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func changeConfiguration(_ configuration: RasterDataSourceConfigurationUpdate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfigurationupdate">RasterDataSourceConfigurationUpdate</a>

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
  <td><code> </code><em><code>configuration</code></em><code> </code></td>
  <td><div>
  <p>The data source configuration update to apply.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16RasterDataSourceC11addDelegateyyAA0bcdF0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-rasterdatasource#sdk-for-ios-explore-s-7heresdk16RasterDataSourceC11addDelegateyyAA0bcdF0_pF" class="token"><code>addDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Add delegate for receiving state notifications. The new delegate is appended to the set of data source delegates as a strong reference and will receive only the notifications occurring after the registration. Caller is responsible for releasing the strong reference by calling <a href="sdk-for-ios-explore-classes-rasterdatasource#sdk-for-ios-explore-s-7heresdk16RasterDataSourceC14removeDelegateyyAA0bcdF0_pF">`RasterDataSource.removeDelegate(...)`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addDelegate(_ listener: RasterDataSourceDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-rasterdatasourcedelegate">RasterDataSourceDelegate</a>

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
  <td><code> </code><em><code>listener</code></em><code> </code></td>
  <td><div>
  <p>Delegate to be added for receiving state notifications.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16RasterDataSourceC14removeDelegateyyAA0bcdF0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-rasterdatasource#sdk-for-ios-explore-s-7heresdk16RasterDataSourceC14removeDelegateyyAA0bcdF0_pF" class="token"><code>removeDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Remove a delegate from receiving state notifications.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeDelegate(_ listener: RasterDataSourceDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-rasterdatasourcedelegate">RasterDataSourceDelegate</a>

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
  <td><code> </code><em><code>listener</code></em><code> </code></td>
  <td><div>
  <p>Delegate to be removed from receiving state notifications.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16RasterDataSourceC15removeDelegatesyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeDelegates" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-rasterdatasource#sdk-for-ios-explore-s-7heresdk16RasterDataSourceC15removeDelegatesyyF" class="token"><code>removeDelegates()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Remove all delegates from receiving state notifications.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeDelegates()
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


---
title: "RasterTileSource Protocol Reference"
slug: "sdk-for-ios-explore-protocols-rastertilesource"
---

# RasterTileSource

<div class="declaration">

<div class="language">

``` highlight
public protocol RasterTileSource : TileSource
```

</div>

</div>

A source of raster tiles. The implementations must be thread-safe. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk16RasterTileSourceP12tilingSchemeAA06TilingF0Ovp"></span>` `<span id="//apple_ref/swift/Property/tilingScheme" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-protocols-rastertilesource#/s:7heresdk16RasterTileSourceP12tilingSchemeAA06TilingF0Ovp" class="token"><code>tilingScheme</code></a>` `

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
  var tilingScheme: TilingScheme { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16RasterTileSourceP13storageLevelsSays5Int32VGvp"></span>` `<span id="//apple_ref/swift/Property/storageLevels" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-protocols-rastertilesource#/s:7heresdk16RasterTileSourceP13storageLevelsSays5Int32VGvp" class="token"><code>storageLevels</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The storage levels available for this data source. Supported range \[0, 31\].

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var storageLevels: [Int32] { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      getDataVersion(tileKey: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the current data version of a tile.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func getDataVersion ( tileKey : TileKey ) -> TileSourceDataVersion
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
  <td><code> </code><em><code>tileKey</code></em><code> </code></td>
  <td><div>
  <p>Key of the tile for which to retrieve the version.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Data version for a tile.

  </div>

  </div>

  </div>

- <div>

      addDelegate(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a delegate for receiving state notifications.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func addDelegate ( _ delegate : TileSourceDelegate )
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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeDelegate(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a delegate from receiving state notifications.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func removeDelegate ( _ delegate : TileSourceDelegate )
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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
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

      loadTile(tileKey: completionHandler: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Load data of a tile. Upon completion, the handler gets informed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func loadTile ( tileKey : TileKey , completionHandler : RasterTileSourceLoadResultHandler ) -> TileSourceLoadTileRequestHandle ?
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
  <td><code> </code><em><code>tileKey</code></em><code> </code></td>
  <td><div>
  <p>Key of the tile to load data for.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completionHandler</code></em><code> </code></td>
  <td><div>
  <p>Load result handler.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  A handle to the created load request.

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


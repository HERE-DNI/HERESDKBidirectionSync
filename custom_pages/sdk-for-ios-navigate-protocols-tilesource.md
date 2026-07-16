---
title: "TileSource Protocol Reference"
slug: "sdk-for-ios-navigate-protocols-tilesource"
---

# TileSource

<div class="declaration">

<div class="language">

``` highlight
public protocol TileSource : AnyObject
```

</div>

</div>

A source of tiles. The implementations must be thread-safe.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10TileSourceP12tilingSchemeAA06TilingE0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-tilingScheme" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-tilesource#sdk-for-ios-navigate-s-7heresdk10TileSourceP12tilingSchemeAA06TilingE0Ovp" class="token"><code>tilingScheme</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-navigate-enums-tilingscheme">TilingScheme</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10TileSourceP13storageLevelsSays5Int32VGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-storageLevels" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-tilesource#sdk-for-ios-navigate-s-7heresdk10TileSourceP13storageLevelsSays5Int32VGvp" class="token"><code>storageLevels</code></a> 

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

   <span id="sdk-for-ios-navigate-s-7heresdk10TileSourceP14getDataVersion7tileKeyAA0bceF0VAA0bH0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getDataVersion-tileKey" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-tilesource#sdk-for-ios-navigate-s-7heresdk10TileSourceP14getDataVersion7tileKeyAA0bceF0VAA0bH0V_tF" class="token"><code>getDataVersion(tileKey:</code><wbr></wbr><code>)</code></a> 

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
  func getDataVersion(tileKey: TileKey) -> TileSourceDataVersion
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-tilekey">TileKey</a>
  - <a href="sdk-for-ios-navigate-structs-tilesourcedataversion">TileSourceDataVersion</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk10TileSourceP11addDelegateyyAA0bcE0_pF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-addDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-tilesource#sdk-for-ios-navigate-s-7heresdk10TileSourceP11addDelegateyyAA0bcE0_pF" class="token"><code>addDelegate(_:</code><wbr></wbr><code>)</code></a> 

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
  func addDelegate(_ delegate: TileSourceDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-tilesourcedelegate">TileSourceDelegate</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk10TileSourceP14removeDelegateyyAA0bcE0_pF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-removeDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-tilesource#sdk-for-ios-navigate-s-7heresdk10TileSourceP14removeDelegateyyAA0bcE0_pF" class="token"><code>removeDelegate(_:</code><wbr></wbr><code>)</code></a> 

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
  func removeDelegate(_ delegate: TileSourceDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-tilesourcedelegate">TileSourceDelegate</a>

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

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>


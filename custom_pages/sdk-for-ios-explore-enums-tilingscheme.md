---
title: "TilingScheme Enumeration Reference"
slug: "sdk-for-ios-explore-enums-tilingscheme"
---

# TilingScheme

<div class="declaration">

<div class="language">

``` highlight
public enum TilingScheme : UInt32, CaseIterable, Codable
```

</div>

</div>

List of available data tiling schemes. X axis has the origin at -180 longitude and is increasing in east direction. Y axis has the origin at max latitude and is increasing in south direction. For half quad tree schemes, only the uppper half of the tree is used.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12TilingSchemeO20halfQuadTreeIdentityyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-halfQuadTreeIdentity" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-tilingscheme#sdk-for-ios-explore-s-7heresdk12TilingSchemeO20halfQuadTreeIdentityyA2CmF" class="token"><code>halfQuadTreeIdentity</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case halfQuadTreeIdentity
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12TilingSchemeO20halfQuadTreeMercatoryA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-halfQuadTreeMercator" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-tilingscheme#sdk-for-ios-explore-s-7heresdk12TilingSchemeO20halfQuadTreeMercatoryA2CmF" class="token"><code>halfQuadTreeMercator</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles. The coordinates of the tile’s corners are transformed through the web-mercator projection.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case halfQuadTreeMercator
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12TilingSchemeO27halfQuadTreeEquirectangularyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-halfQuadTreeEquirectangular" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-tilingscheme#sdk-for-ios-explore-s-7heresdk12TilingSchemeO27halfQuadTreeEquirectangularyA2CmF" class="token"><code>halfQuadTreeEquirectangular</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles. The coordinates of the tile’s corners are transformed through the equirectangular (plate carree) projection.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case halfQuadTreeEquirectangular
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12TilingSchemeO16quadTreeIdentityyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-quadTreeIdentity" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-tilingscheme#sdk-for-ios-explore-s-7heresdk12TilingSchemeO16quadTreeIdentityyA2CmF" class="token"><code>quadTreeIdentity</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A tiling scheme that splits each level tile into 4 equal-sized subtiles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case quadTreeIdentity
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12TilingSchemeO16quadTreeMercatoryA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-quadTreeMercator" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-tilingscheme#sdk-for-ios-explore-s-7heresdk12TilingSchemeO16quadTreeMercatoryA2CmF" class="token"><code>quadTreeMercator</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A tiling scheme that splits each level tile into 4 equal-sized subtiles. The coordinates of the tile’s corners are transformed through the web-mercator projection.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case quadTreeMercator
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12TilingSchemeO23quadTreeEquirectangularyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-quadTreeEquirectangular" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-tilingscheme#sdk-for-ios-explore-s-7heresdk12TilingSchemeO23quadTreeEquirectangularyA2CmF" class="token"><code>quadTreeEquirectangular</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A tiling scheme that splits each level tile into 4 equal-sized subtiles. The coordinates of the tile’s corners are transformed through the equirectangular (plate carree) projection.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case quadTreeEquirectangular
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


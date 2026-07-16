---
title: "MemoryManagementOptions Structure Reference"
slug: "sdk-for-ios-explore-classes-mapcontext-memorymanagementoptions"
---

# MemoryManagementOptions

<div class="declaration">

<div class="language">

``` highlight
public struct MemoryManagementOptions
```

</div>

</div>

Memory management options.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapContextC23MemoryManagementOptionsV06memoryE8StrategyAC0deH0Ovp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-memoryManagementStrategy" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementoptions#sdk-for-ios-explore-s-7heresdk10MapContextC23MemoryManagementOptionsV06memoryE8StrategyAC0deH0Ovp" class="token"><code>memoryManagementStrategy</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The default setting MemoryManagementStrategy.DYNAMIC is suitable for common cases. The map data cache can adjust dynamically to fit visible data. When the visible data needs extra memory, it would increase. When it’s not needed, it will reduce to a limit which is calculated internally or by using <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementoptions#sdk-for-ios-explore-s-7heresdk10MapContextC23MemoryManagementOptionsV09tileCacheD10LimitInKiBs5Int32VSgvp">`MapContext.MemoryManagementOptions.tileCacheMemoryLimitInKiB`</a> option. The MemoryManagementStrategy.FIXED would be only useful when there is very strict memory consumption requirement for the application. It potentially can have flickering visual artifacts when the map data to be visualized is very large and exceeds the cache limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var memoryManagementStrategy: MapContext.MemoryManagementStrategy
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcontext">MapContext</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementstrategy">MemoryManagementStrategy</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapContextC23MemoryManagementOptionsV09tileCacheD10LimitInKiBs5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-tileCacheMemoryLimitInKiB" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementoptions#sdk-for-ios-explore-s-7heresdk10MapContextC23MemoryManagementOptionsV09tileCacheD10LimitInKiBs5Int32VSgvp" class="token"><code>tileCacheMemoryLimitInKiB</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tile cache memory limit in kibibytes. Non positive or `nil` values are ignored. Default value is `nil`. Low tile cache limit will lead to eviction of tiles only if MemoryManagementStrategy is set to FIXED.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tileCacheMemoryLimitInKiB: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapContextC23MemoryManagementOptionsV05videoD10LimitInKiBs5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-videoMemoryLimitInKiB" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementoptions#sdk-for-ios-explore-s-7heresdk10MapContextC23MemoryManagementOptionsV05videoD10LimitInKiBs5Int32VSgvp" class="token"><code>videoMemoryLimitInKiB</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Target video memory limit in kibibytes. Non positive or `nil` values are ignored. Default value is `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var videoMemoryLimitInKiB: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapContextC23MemoryManagementOptionsV06memoryE8Strategy09tileCacheD10LimitInKiB05videodklM1BAeC0deH0O_s5Int32VSgAMtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-memoryManagementStrategy-tileCacheMemoryLimitInKiB-videoMemoryLimitInKiB" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementoptions#sdk-for-ios-explore-s-7heresdk10MapContextC23MemoryManagementOptionsV06memoryE8Strategy09tileCacheD10LimitInKiB05videodklM1BAeC0deH0O_s5Int32VSgAMtcfc" class="token"><code>init(memoryManagementStrategy:</code><wbr></wbr><code>tileCacheMemoryLimitInKiB:</code><wbr></wbr><code>videoMemoryLimitInKiB:</code><wbr></wbr><code>)</code></a> 

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
  public init(memoryManagementStrategy: MapContext.MemoryManagementStrategy = MapContext.MemoryManagementStrategy.dynamic, tileCacheMemoryLimitInKiB: Int32? = nil, videoMemoryLimitInKiB: Int32? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcontext">MapContext</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementstrategy">MemoryManagementStrategy</a>

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


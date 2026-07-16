---
title: "UsageStats Structure Reference"
slug: "sdk-for-ios-navigate-structs-usagestats"
---

# UsageStats

<div class="declaration">

<div class="language">

``` highlight
public struct UsageStats
```

</div>

</div>

A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10UsageStatsV07networkC0SayAC07NetworkC0VGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-networkStats" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-usagestats#sdk-for-ios-navigate-s-7heresdk10UsageStatsV07networkC0SayAC07NetworkC0VGvp" class="token"><code>networkStats</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides network statistics.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var networkStats: [UsageStats.NetworkStats]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-usagestats-networkstats">NetworkStats</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10UsageStatsV7featureAC7FeatureOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-feature" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-usagestats#sdk-for-ios-navigate-s-7heresdk10UsageStatsV7featureAC7FeatureOvp" class="token"><code>feature</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the HERE SDK feature associated with the gathered usage statistics.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var feature: UsageStats.Feature
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-usagestats-feature">Feature</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10UsageStatsV07networkC07featureACSayAC07NetworkC0VG_AC7FeatureOtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-networkStats-feature" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-usagestats#sdk-for-ios-navigate-s-7heresdk10UsageStatsV07networkC07featureACSayAC07NetworkC0VG_AC7FeatureOtcfc" class="token"><code>init(networkStats:</code><wbr></wbr><code>feature:</code><wbr></wbr><code>)</code></a> 

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
  public init(networkStats: [UsageStats.NetworkStats], feature: UsageStats.Feature)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-usagestats-networkstats">NetworkStats</a>
  - <a href="sdk-for-ios-navigate-structs-usagestats-feature">Feature</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10UsageStatsV7FeatureO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-Feature" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-usagestats#sdk-for-ios-navigate-s-7heresdk10UsageStatsV7FeatureO" class="token"><code>Feature</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the feature enum associated with the gathered usage stats.

  <a href="sdk-for-ios-navigate-structs-usagestats-feature" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum Feature : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10UsageStatsV07NetworkC0V"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-NetworkStats" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-usagestats#sdk-for-ios-navigate-s-7heresdk10UsageStatsV07NetworkC0V" class="token"><code>NetworkStats</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides network statistics in bytes per method.

  <a href="sdk-for-ios-navigate-structs-usagestats-networkstats" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct NetworkStats
  ```

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


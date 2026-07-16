---
title: "MemoryManagementResultCode Enumeration Reference"
slug: "sdk-for-ios-explore-classes-mapcontext-memorymanagementresultcode"
---

# MemoryManagementResultCode

<div class="declaration">

<div class="language">

``` highlight
public enum MemoryManagementResultCode : UInt32, CaseIterable, Codable
```

</div>

</div>

The memory management result code.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapContextC26MemoryManagementResultCodeO7appliedyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-applied" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementresultcode#sdk-for-ios-explore-s-7heresdk10MapContextC26MemoryManagementResultCodeO7appliedyA2EmF" class="token"><code>applied</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The memory management options were successfully applied.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case applied
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapContextC26MemoryManagementResultCodeO012tileCacheCpuD13LimitExceededyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-tileCacheCpuMemoryLimitExceeded" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementresultcode#sdk-for-ios-explore-s-7heresdk10MapContextC26MemoryManagementResultCodeO012tileCacheCpuD13LimitExceededyA2EmF" class="token"><code>tileCacheCpuMemoryLimitExceeded</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The requested memory limit exceeds the maximum allowed limit for CPU tile cache. Previous value of CPU tile cache limit is preserved. Video memory limit applied correctly.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case tileCacheCpuMemoryLimitExceeded
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapContextC26MemoryManagementResultCodeO05videoD13LimitExceededyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-videoMemoryLimitExceeded" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementresultcode#sdk-for-ios-explore-s-7heresdk10MapContextC26MemoryManagementResultCodeO05videoD13LimitExceededyA2EmF" class="token"><code>videoMemoryLimitExceeded</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The requested memory limit exceeds the maximum allowed limit for video memory. Previous value of video memory limit is preserved. CPU tile cache limit applied correctly.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case videoMemoryLimitExceeded
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapContextC26MemoryManagementResultCodeO010failedBothD14LimitsExceededyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-failedBothMemoryLimitsExceeded" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementresultcode#sdk-for-ios-explore-s-7heresdk10MapContextC26MemoryManagementResultCodeO010failedBothD14LimitsExceededyA2EmF" class="token"><code>failedBothMemoryLimitsExceeded</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Both video memory and CPU tile cache limits were exceeded and limits were not applied. Previous values of video memory and CPU tile cache limits are preserved.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case failedBothMemoryLimitsExceeded
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapContextC26MemoryManagementResultCodeO6failedyA2EmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-failed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementresultcode#sdk-for-ios-explore-s-7heresdk10MapContextC26MemoryManagementResultCodeO6failedyA2EmF" class="token"><code>failed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The memory management options could not be applied due to other errors.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case failed
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


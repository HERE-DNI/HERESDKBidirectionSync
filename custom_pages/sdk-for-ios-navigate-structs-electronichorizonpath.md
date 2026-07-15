---
title: "ElectronicHorizonPath Structure Reference"
slug: "sdk-for-ios-navigate-structs-electronichorizonpath"
---

# ElectronicHorizonPath

<div class="declaration">

<div class="language">

``` highlight
public struct ElectronicHorizonPath : Hashable
```

</div>

</div>

Represents a single electronic horizon path.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk21ElectronicHorizonPathV06parentD5Indexs5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/parentPathIndex" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-electronichorizonpath#/s:7heresdk21ElectronicHorizonPathV06parentD5Indexs5Int32VSgvp" class="token"><code>parentPathIndex</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The index of the parent path. Index 0 marks the most-preferred path.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var parentPathIndex: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21ElectronicHorizonPathV18parentSegmentIndexs5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/parentSegmentIndex" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-electronichorizonpath#/s:7heresdk21ElectronicHorizonPathV18parentSegmentIndexs5Int32VSgvp" class="token"><code>parentSegmentIndex</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The index of the parent segment in the parent path. This value is `nil` if the path is the most-preferred path.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var parentSegmentIndex: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21ElectronicHorizonPathV8segmentsSayAA0bC7SegmentVGvp"></span>` `<span id="//apple_ref/swift/Property/segments" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-electronichorizonpath#/s:7heresdk21ElectronicHorizonPathV8segmentsSayAA0bC7SegmentVGvp" class="token"><code>segments</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The ordered list of segments in this path. The list can be empty when no segments are available for the current path.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var segments: [ElectronicHorizonSegment]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21ElectronicHorizonPathV11probabilitySdvp"></span>` `<span id="//apple_ref/swift/Property/probability" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-electronichorizonpath#/s:7heresdk21ElectronicHorizonPathV11probabilitySdvp" class="token"><code>probability</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The probability of this electronic horizon path, where a value of 1 represents the most-preferred path and a value of 0 represents an unlikely path.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var probability: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21ElectronicHorizonPathV5levels5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/level" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-electronichorizonpath#/s:7heresdk21ElectronicHorizonPathV5levels5Int32Vvp" class="token"><code>level</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The level of this path. A value of 0 represents the most-preferred path.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var level: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(parentPathIndex: parentSegmentIndex: segments: probability: level: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  Offline availability: This property is available online and offline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( parentPathIndex : Int32 ? = nil , parentSegmentIndex : Int32 ? = nil , segments : [ ElectronicHorizonSegment ], probability : Double , level : Int32 )
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


---
title: "SegmentReference Structure Reference"
slug: "sdk-for-ios-explore-structs-segmentreference"
---

# SegmentReference

<div class="declaration">

<div class="language">

``` highlight
public struct SegmentReference : Hashable
```

</div>

</div>

Reference to a segment id with a travel direction.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk16SegmentReferenceV9segmentIdSSvp"></span>` `<span id="//apple_ref/swift/Property/segmentId" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-segmentreference#/s:7heresdk16SegmentReferenceV9segmentIdSSvp" class="token"><code>segmentId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Topology segment id representing a unique identifier within the HERE platform catalogs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var segmentId: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SegmentReferenceV15travelDirectionAA06TravelE0Ovp"></span>` `<span id="//apple_ref/swift/Property/travelDirection" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-segmentreference#/s:7heresdk16SegmentReferenceV15travelDirectionAA06TravelE0Ovp" class="token"><code>travelDirection</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Travel direction of the segment.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var travelDirection: TravelDirection
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SegmentReferenceV11offsetStartSdvp"></span>` `<span id="//apple_ref/swift/Property/offsetStart" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-segmentreference#/s:7heresdk16SegmentReferenceV11offsetStartSdvp" class="token"><code>offsetStart</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var offsetStart: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SegmentReferenceV9offsetEndSdvp"></span>` `<span id="//apple_ref/swift/Property/offsetEnd" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-segmentreference#/s:7heresdk16SegmentReferenceV9offsetEndSdvp" class="token"><code>offsetEnd</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var offsetEnd: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SegmentReferenceV15tilePartitionIds6UInt32Vvp"></span>` `<span id="//apple_ref/swift/Property/tilePartitionId" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-segmentreference#/s:7heresdk16SegmentReferenceV15tilePartitionIds6UInt32Vvp" class="token"><code>tilePartitionId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  HERE tile partition id (Morton-encoding + level indicator) of the segment. As in HERE Map Content.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tilePartitionId: UInt32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SegmentReferenceV7localIds6UInt32VSgvp"></span>` `<span id="//apple_ref/swift/Property/localId" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-segmentreference#/s:7heresdk16SegmentReferenceV7localIds6UInt32VSgvp" class="token"><code>localId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Local ID of the segment inside the OCM tile.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var localId: UInt32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(segmentId: travelDirection: offsetStart: offsetEnd: tilePartitionId: localId: )

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
  public init ( segmentId : String = "" , travelDirection : TravelDirection = TravelDirection . bidirectional , offsetStart : Double = 0.0 , offsetEnd : Double = 1.0 , tilePartitionId : UInt32 = 0 , localId : UInt32 ? = 0 )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      fromString(segmentRef: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns an instance of this struct from a string if it’s well-formatted, `nil` otherwise.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fromString ( segmentRef : String ) -> SegmentReference ?
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
  <td><code> </code><em><code>segmentRef</code></em><code> </code></td>
  <td><div>
  <p>The string to parse</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  An instance of `SegmentReference` from a string if it’s well-formatted, `nil` otherwise.

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


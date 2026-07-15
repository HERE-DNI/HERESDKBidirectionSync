---
title: "CustomWarning Structure Reference"
slug: "sdk-for-ios-navigate-structs-customwarning"
---

# CustomWarning

<div class="declaration">

<div class="language">

``` highlight
public struct CustomWarning : Hashable
```

</div>

</div>

struct container for custom warning data.

This structure represents the type-specific payload associated with a custom warning.

Instances of this structure are typically produced by custom warning evaluation logic and may also be retrieved from the `WarningRegistry`.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk13CustomWarningV2ids5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-customwarning#/s:7heresdk13CustomWarningV2ids5Int32Vvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifier of the warning. The ID is unique only within its specific <a href="sdk-for-ios-navigate-structs-customwarning#/s:7heresdk13CustomWarningV06customC4Types5Int32Vvp">`CustomWarning.customWarningType`</a> and can be used to retrieve additional information from a corresponding registry.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CustomWarningV06customC4Types5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/customWarningType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-customwarning#/s:7heresdk13CustomWarningV06customC4Types5Int32Vvp" class="token"><code>customWarningType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifier of the custom warning type.

  Defines the category of the custom warning and determines which warning registry should be used to retrieve additional warning details.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var customWarningType: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CustomWarningV19startOffsetInMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/startOffsetInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-customwarning#/s:7heresdk13CustomWarningV19startOffsetInMetersSdvp" class="token"><code>startOffsetInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Start offset of the warning range along the segment.

  Specifies the distance, in meters, from the beginning of the corresponding <a href="sdk-for-ios-navigate-structs-electronichorizonsegment">`ElectronicHorizonSegment`</a> at which the warning becomes applicable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var startOffsetInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CustomWarningV17endOffsetInMetersSdSgvp"></span>` `<span id="//apple_ref/swift/Property/endOffsetInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-customwarning#/s:7heresdk13CustomWarningV17endOffsetInMetersSdSgvp" class="token"><code>endOffsetInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  End offset of the warning range along the segment.

  Specifies the distance, in meters, from the beginning of the corresponding <a href="sdk-for-ios-navigate-structs-electronichorizonsegment">`ElectronicHorizonSegment`</a> at which the warning is no longer applicable.

  May be `nil`. In this case, the value is automatically considered to be equal to <a href="sdk-for-ios-navigate-structs-customwarning#/s:7heresdk13CustomWarningV19startOffsetInMetersSdvp">`startOffsetInMeters`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var endOffsetInMeters: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CustomWarningV7payloadAA8MetadataCSgvp"></span>` `<span id="//apple_ref/swift/Property/payload" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-customwarning#/s:7heresdk13CustomWarningV7payloadAA8MetadataCSgvp" class="token"><code>payload</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Custom warning payload.

  Contains warning-specific payload data. A value of `nil` indicates that no additional data is associated with the warning.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var payload: Metadata?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(id: customWarningType: startOffsetInMeters: endOffsetInMeters: payload: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  - Parameters

    - id: Identifier of the warning. The ID is unique only within its specific <a href="sdk-for-ios-navigate-structs-customwarning#/s:7heresdk13CustomWarningV06customC4Types5Int32Vvp">`CustomWarning.customWarningType`</a> and can be used to retrieve additional information from a corresponding registry.
    - customWarningType: Identifier of the custom warning type.

    Defines the category of the custom warning and determines which warning registry should be used to retrieve additional warning details.

    - startOffsetInMeters: Start offset of the warning range along the segment.

    Specifies the distance, in meters, from the beginning of the corresponding <a href="sdk-for-ios-navigate-structs-electronichorizonsegment">`ElectronicHorizonSegment`</a> at which the warning becomes applicable.

    - endOffsetInMeters: End offset of the warning range along the segment.

    Specifies the distance, in meters, from the beginning of the corresponding <a href="sdk-for-ios-navigate-structs-electronichorizonsegment">`ElectronicHorizonSegment`</a> at which the warning is no longer applicable.

    May be `nil`. In this case, the value is automatically considered to be equal to <a href="sdk-for-ios-navigate-structs-customwarning#/s:7heresdk13CustomWarningV19startOffsetInMetersSdvp">`startOffsetInMeters`</a>.

    - payload: Custom warning payload.

    Contains warning-specific payload data. A value of `nil` indicates that no additional data is associated with the warning.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( id : Int32 = 0 , customWarningType : Int32 = 0 , startOffsetInMeters : Double = 0.0 , endOffsetInMeters : Double ? = nil , payload : Metadata ? = nil )
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


---
title: "Warning Structure Reference"
slug: "sdk-for-ios-explore-structs-warning"
---

# Warning

<div class="declaration">

<div class="language">

``` highlight
public struct Warning : Hashable
```

</div>

</div>

A struct which represents a warning.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk7WarningV2ids5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-id" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-warning#sdk-for-ios-explore-s-7heresdk7WarningV2ids5Int32Vvp" class="token"><code>id</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifier of the warning. The ID is unique only within its specific <a href="sdk-for-ios-explore-structs-warning#sdk-for-ios-explore-s-7heresdk7WarningV11warningTypeAA0bD0Ovp">`warningType`</a> and can be used to retrieve additional information from a corresponding registry.

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

   <span id="sdk-for-ios-explore-s-7heresdk7WarningV12distanceTypeAA08DistanceD0Ovp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-distanceType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-warning#sdk-for-ios-explore-s-7heresdk7WarningV12distanceTypeAA08DistanceD0Ovp" class="token"><code>distanceType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The type of distance measurement used for this warning.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceType: DistanceType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-distancetype">DistanceType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk7WarningV11warningTypeAA0bD0Ovp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-warningType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-warning#sdk-for-ios-explore-s-7heresdk7WarningV11warningTypeAA0bD0Ovp" class="token"><code>warningType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The specific type of the warning.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var warningType: WarningType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk7WarningV06customB4Types5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-customWarningType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-warning#sdk-for-ios-explore-s-7heresdk7WarningV06customB4Types5Int32VSgvp" class="token"><code>customWarningType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifier of the custom warning type.

  Defines the category of the custom warning and determines which warning registry should be used to retrieve additional warning details. This field is set only when `warningType == WarningType.CUSTOM` and is `nil` for all other warning types.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var customWarningType: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk7WarningV2id12distanceType07warningE006custombE0ACs5Int32V_AA08DistanceE0OAA0bE0OAISgtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-id-distanceType-warningType-customWarningType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-warning#sdk-for-ios-explore-s-7heresdk7WarningV2id12distanceType07warningE006custombE0ACs5Int32V_AA08DistanceE0OAA0bE0OAISgtcfc" class="token"><code>init(id:</code><wbr></wbr><code>distanceType:</code><wbr></wbr><code>warningType:</code><wbr></wbr><code>customWarningType:</code><wbr></wbr><code>)</code></a> 

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

    - id: Identifier of the warning. The ID is unique only within its specific <a href="sdk-for-ios-explore-structs-warning#sdk-for-ios-explore-s-7heresdk7WarningV11warningTypeAA0bD0Ovp">`warningType`</a> and can be used to retrieve additional information from a corresponding registry.
    - distanceType: The type of distance measurement used for this warning.
    - warningType: The specific type of the warning.
    - customWarningType: Identifier of the custom warning type.

    Defines the category of the custom warning and determines which warning registry should be used to retrieve additional warning details. This field is set only when `warningType == WarningType.CUSTOM` and is `nil` for all other warning types.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(id: Int32, distanceType: DistanceType, warningType: WarningType, customWarningType: Int32? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-distancetype">DistanceType</a>
  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>

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


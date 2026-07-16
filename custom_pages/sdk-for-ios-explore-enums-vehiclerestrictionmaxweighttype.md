---
title: "VehicleRestrictionMaxWeightType Enumeration Reference"
slug: "sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype"
---

# VehicleRestrictionMaxWeightType

<div class="declaration">

<div class="language">

``` highlight
public enum VehicleRestrictionMaxWeightType : UInt32, CaseIterable, Codable
```

</div>

</div>

This enum represents the specific type of the maximum permitted weight restriction. **NOTES:** A restriction of type <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype#sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO7unknownyA2CmF">`VehicleRestrictionMaxWeightType.unknown`</a> may change to <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype#sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO5grossyA2CmF">`VehicleRestrictionMaxWeightType.gross`</a>, <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype#sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO7currentyA2CmF">`VehicleRestrictionMaxWeightType.current`</a> or <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype#sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO5emptyyA2CmF">`VehicleRestrictionMaxWeightType.empty`</a> when data becomes available in future. A restriction of type <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype#sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO5grossyA2CmF">`VehicleRestrictionMaxWeightType.gross`</a>, <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype#sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO7currentyA2CmF">`VehicleRestrictionMaxWeightType.current`</a> or <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype#sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO5emptyyA2CmF">`VehicleRestrictionMaxWeightType.empty`</a> may also change to a different type if actual regulation changes.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO7unknownyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-unknown" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype#sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO7unknownyA2CmF" class="token"><code>unknown</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Restriction may apply to gross or current weight.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case unknown
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO5grossyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-gross" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype#sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO5grossyA2CmF" class="token"><code>gross</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Restriction is for gross weight.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case gross
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO7currentyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-current" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype#sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO7currentyA2CmF" class="token"><code>current</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Restriction is for current weight.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case current
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO5emptyyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-empty" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype#sdk-for-ios-explore-s-7heresdk31VehicleRestrictionMaxWeightTypeO5emptyyA2CmF" class="token"><code>empty</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Restriction is for empty weight.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case empty
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


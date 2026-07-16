---
title: "AdministrativeCommercialVehicleRules Structure Reference"
slug: "sdk-for-ios-explore-structs-administrativecommercialvehiclerules"
---

# AdministrativeCommercialVehicleRules

<div class="declaration">

<div class="language">

``` highlight
public struct AdministrativeCommercialVehicleRules : Hashable
```

</div>

</div>

Commercial vehicle regulations for an administrative region (country or state). Contains access restrictions, speed limits, and drive/rest rules applicable to commercial vehicles on road segments within the region.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk36AdministrativeCommercialVehicleRulesV2idAA14AdminContextIdVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-id" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-administrativecommercialvehiclerules#sdk-for-ios-explore-s-7heresdk36AdministrativeCommercialVehicleRulesV2idAA14AdminContextIdVvp" class="token"><code>id</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Administrative context identifier for this set of rules.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: AdminContextId
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-admincontextid">AdminContextId</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk36AdministrativeCommercialVehicleRulesV17accessRegulationsSayAA0D14SpecificAccessVGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-accessRegulations" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-administrativecommercialvehiclerules#sdk-for-ios-explore-s-7heresdk36AdministrativeCommercialVehicleRulesV17accessRegulationsSayAA0D14SpecificAccessVGvp" class="token"><code>accessRegulations</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Access restrictions for commercial vehicles (e.g. bridge/tunnel restrictions).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var accessRegulations: [VehicleSpecificAccess]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-vehiclespecificaccess">VehicleSpecificAccess</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk36AdministrativeCommercialVehicleRulesV21speedLimitRegulationsSayAA0d13SpecificSpeedG0VGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-speedLimitRegulations" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-administrativecommercialvehiclerules#sdk-for-ios-explore-s-7heresdk36AdministrativeCommercialVehicleRulesV21speedLimitRegulationsSayAA0d13SpecificSpeedG0VGvp" class="token"><code>speedLimitRegulations</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle-specific speed limits for commercial vehicles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedLimitRegulations: [VehicleSpecificSpeedLimit]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-vehiclespecificspeedlimit">VehicleSpecificSpeedLimit</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk36AdministrativeCommercialVehicleRulesV19driveRestRegulationAA05DrivegH0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-driveRestRegulation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-administrativecommercialvehiclerules#sdk-for-ios-explore-s-7heresdk36AdministrativeCommercialVehicleRulesV19driveRestRegulationAA05DrivegH0Vvp" class="token"><code>driveRestRegulation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Drive and rest regulations for commercial drivers.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var driveRestRegulation: DriveRestRegulation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-driverestregulation">DriveRestRegulation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk36AdministrativeCommercialVehicleRulesV2id17accessRegulations010speedLimitH019driveRestRegulationAcA14AdminContextIdV_SayAA0D14SpecificAccessVGSayAA0dq5SpeedJ0VGAA05DrivelM0Vtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-id-accessRegulations-speedLimitRegulations-driveRestRegulation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-administrativecommercialvehiclerules#sdk-for-ios-explore-s-7heresdk36AdministrativeCommercialVehicleRulesV2id17accessRegulations010speedLimitH019driveRestRegulationAcA14AdminContextIdV_SayAA0D14SpecificAccessVGSayAA0dq5SpeedJ0VGAA05DrivelM0Vtcfc" class="token"><code>init(id:</code><wbr></wbr><code>accessRegulations:</code><wbr></wbr><code>speedLimitRegulations:</code><wbr></wbr><code>driveRestRegulation:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance with default values.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(id: AdminContextId, accessRegulations: [VehicleSpecificAccess] = [], speedLimitRegulations: [VehicleSpecificSpeedLimit] = [], driveRestRegulation: DriveRestRegulation = DriveRestRegulation())
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-admincontextid">AdminContextId</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecificaccess">VehicleSpecificAccess</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecificspeedlimit">VehicleSpecificSpeedLimit</a>
  - <a href="sdk-for-ios-explore-structs-driverestregulation">DriveRestRegulation</a>

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


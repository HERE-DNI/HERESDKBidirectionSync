---
title: "BorderCrossingWarning Structure Reference"
slug: "sdk-for-ios-explore-structs-bordercrossingwarning"
---

# BorderCrossingWarning

<div class="declaration">

<div class="language">

``` highlight
public struct BorderCrossingWarning : Hashable
```

</div>

</div>

A border crossing. The main field describing the border crossing is <a href="sdk-for-ios-explore-structs-bordercrossingwarning#/s:7heresdk21BorderCrossingWarningV4typeAA0bC4TypeOvp">`BorderCrossingWarning.type`</a> specifying whether the border crossing is given for a country border or a state border. The <a href="sdk-for-ios-explore-structs-bordercrossingwarning#/s:7heresdk21BorderCrossingWarningV4typeAA0bC4TypeOvp">`BorderCrossingWarning.type`</a> must be known. The country and state codes are contained in <a href="sdk-for-ios-explore-structs-bordercrossingwarning#/s:7heresdk21BorderCrossingWarningV19administrativeRulesAA014AdministrativeF0Vvp">`BorderCrossingWarning.administrativeRules`</a> along with other information such as speed limits, u-turn regulations or pre-trip planning information contained by the <a href="sdk-for-ios-explore-structs-administrativerules">`AdministrativeRules`</a>.

Use `BorderCrossingWarningListener` to get notifications about upcoming country or state border crossings.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk21BorderCrossingWarningV2ids5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-bordercrossingwarning#/s:7heresdk21BorderCrossingWarningV2ids5Int32Vvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier for this specific border crossing warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

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

  ` `<span id="/s:7heresdk21BorderCrossingWarningV010distanceTobC8InMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/distanceToBorderCrossingInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-bordercrossingwarning#/s:7heresdk21BorderCrossingWarningV010distanceTobC8InMetersSdvp" class="token"><code>distanceToBorderCrossingInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance to the border crossing in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceToBorderCrossingInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BorderCrossingWarningV4typeAA0bC4TypeOvp"></span>` `<span id="//apple_ref/swift/Property/type" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-bordercrossingwarning#/s:7heresdk21BorderCrossingWarningV4typeAA0bC4TypeOvp" class="token"><code>type</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of border crossing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: BorderCrossingType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BorderCrossingWarningV19administrativeRulesAA014AdministrativeF0Vvp"></span>` `<span id="//apple_ref/swift/Property/administrativeRules" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-bordercrossingwarning#/s:7heresdk21BorderCrossingWarningV19administrativeRulesAA014AdministrativeF0Vvp" class="token"><code>administrativeRules</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The administrative rules for the country or state after the border crossing. It contains information regarding rules such as driving side, speed limits, various sticker requirements, toll costs and others.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var administrativeRules: AdministrativeRules
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BorderCrossingWarningV12distanceTypeAA08DistanceF0Ovp"></span>` `<span id="//apple_ref/swift/Property/distanceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-bordercrossingwarning#/s:7heresdk21BorderCrossingWarningV12distanceTypeAA08DistanceF0Ovp" class="token"><code>distanceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance type for the warning, e.g. a warning for a new border crossing ahead or a warning for passing a border crossing. Since the border crossing warning is given relative to a single position on the route, <a href="sdk-for-ios-explore-enums-distancetype#/s:7heresdk12DistanceTypeO7reachedyA2CmF">`DistanceType.reached`</a> will never be given for this warning.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceType: DistanceType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BorderCrossingWarningV28commercialVehicleRegulationsAA024AdministrativeCommercialF5RulesVSgvp"></span>` `<span id="//apple_ref/swift/Property/commercialVehicleRegulations" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-bordercrossingwarning#/s:7heresdk21BorderCrossingWarningV28commercialVehicleRegulationsAA024AdministrativeCommercialF5RulesVSgvp" class="token"><code>commercialVehicleRegulations</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Commercial vehicle regulations for the administrative region after the border crossing. Contains access restrictions, speed limits, and drive/rest rules applicable to commercial vehicles. This field is only populated when crossing into a region with specific commercial vehicle regulations.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var commercialVehicleRegulations: AdministrativeCommercialVehicleRules?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(id: distanceToBorderCrossingInMeters: type: administrativeRules: distanceType: commercialVehicleRegulations: )

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
  public init ( id : Int32 = 0 , distanceToBorderCrossingInMeters : Double , type : BorderCrossingType , administrativeRules : AdministrativeRules , distanceType : DistanceType , commercialVehicleRegulations : AdministrativeCommercialVehicleRules ? = nil )
  ```

  </pre>

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


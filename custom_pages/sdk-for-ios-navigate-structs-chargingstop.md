---
title: "ChargingStop Structure Reference"
slug: "sdk-for-ios-navigate-structs-chargingstop"
---

# ChargingStop

<div class="declaration">

<div class="language">

``` highlight
public struct ChargingStop : Hashable
```

</div>

</div>

The options to specify a user-planned charging stop. **Note:** In order to specify this `ChargingStop`, it is also required to set \[sdk.routing.BatterySpecifications.total_capacity_in_kilowatt_hours\], \[sdk.routing.BatterySpecifications.initial_charge_in_kilowatt_hours\], and \[sdk.routing.BatterySpecifications.charging_curve\]. Without all of them, the route calculation will fail as an invalid parameter error.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12ChargingStopV16powerInKilowattsSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-powerInKilowatts" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-chargingstop#sdk-for-ios-navigate-s-7heresdk12ChargingStopV16powerInKilowattsSdvp" class="token"><code>powerInKilowatts</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The value of rated power of the connector (in kW).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var powerInKilowatts: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12ChargingStopV16currentInAmperesSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-currentInAmperes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-chargingstop#sdk-for-ios-navigate-s-7heresdk12ChargingStopV16currentInAmperesSdvp" class="token"><code>currentInAmperes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The value of rated current of the connector (in A).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var currentInAmperes: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12ChargingStopV14voltageInVoltsSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-voltageInVolts" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-chargingstop#sdk-for-ios-navigate-s-7heresdk12ChargingStopV14voltageInVoltsSdvp" class="token"><code>voltageInVolts</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The value of rated voltage of the connector (in V).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var voltageInVolts: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12ChargingStopV10supplyTypeAA0b6SupplyE0OSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-supplyType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-chargingstop#sdk-for-ios-navigate-s-7heresdk12ChargingStopV10supplyTypeAA0b6SupplyE0OSgvp" class="token"><code>supplyType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Supply type of the suggested connector.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var supplyType: ChargingSupplyType?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-chargingsupplytype">ChargingSupplyType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12ChargingStopV11minDurationSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-minDuration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-chargingstop#sdk-for-ios-navigate-s-7heresdk12ChargingStopV11minDurationSdSgvp" class="token"><code>minDuration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The minimum duration the user expects to charge at the station, including <a href="sdk-for-ios-navigate-structs-batteryspecifications#sdk-for-ios-navigate-s-7heresdk21BatterySpecificationsV21chargingSetupDurationSdvp">`BatterySpecifications.chargingSetupDuration`</a>. **Note:** At least one of `min_duration` and `max_duration` is required for a user-planned charging stop. For most use cases, providing at least `min_duration` is recommended.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var minDuration: TimeInterval?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12ChargingStopV11maxDurationSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-maxDuration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-chargingstop#sdk-for-ios-navigate-s-7heresdk12ChargingStopV11maxDurationSdSgvp" class="token"><code>maxDuration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The maximum duration the user plans to charge at the station, including <a href="sdk-for-ios-navigate-structs-batteryspecifications#sdk-for-ios-navigate-s-7heresdk21BatterySpecificationsV21chargingSetupDurationSdvp">`BatterySpecifications.chargingSetupDuration`</a>. **Note:** At least one of `min_duration` and `max_duration` is required for a user-planned charging stop. For most use cases, providing at least `min_duration` is recommended.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxDuration: TimeInterval?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12ChargingStopV16powerInKilowatts07currentE7Amperes07voltageE5Volts10supplyType11minDuration03maxN0ACSd_S2dAA0b6SupplyL0OSgSdSgAMtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-powerInKilowatts-currentInAmperes-voltageInVolts-supplyType-minDuration-maxDuration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-chargingstop#sdk-for-ios-navigate-s-7heresdk12ChargingStopV16powerInKilowatts07currentE7Amperes07voltageE5Volts10supplyType11minDuration03maxN0ACSd_S2dAA0b6SupplyL0OSgSdSgAMtcfc" class="token"><code>init(powerInKilowatts:</code><wbr></wbr><code>currentInAmperes:</code><wbr></wbr><code>voltageInVolts:</code><wbr></wbr><code>supplyType:</code><wbr></wbr><code>minDuration:</code><wbr></wbr><code>maxDuration:</code><wbr></wbr><code>)</code></a> 

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
  public init(powerInKilowatts: Double = 0.0, currentInAmperes: Double = 0.0, voltageInVolts: Double = 0.0, supplyType: ChargingSupplyType? = nil, minDuration: TimeInterval? = nil, maxDuration: TimeInterval? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-chargingsupplytype">ChargingSupplyType</a>

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


---
title: "EVConsumptionModel Structure Reference"
slug: "sdk-for-ios-explore-structs-evconsumptionmodel"
---

# EVConsumptionModel

<div class="declaration">

<div class="language">

``` highlight
public struct EVConsumptionModel : Hashable
```

</div>

</div>

Parameters specific for the electric vehicle, which are then used to calculate energy consumption on a given route. At minimum, you must provide <a href="sdk-for-ios-explore-structs-evconsumptionmodel#sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV36ascentConsumptionInWattHoursPerMeterSdvp">`EVConsumptionModel.ascentConsumptionInWattHoursPerMeter`</a>, <a href="sdk-for-ios-explore-structs-evconsumptionmodel#sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV34descentRecoveryInWattHoursPerMeterSdvp">`EVConsumptionModel.descentRecoveryInWattHoursPerMeter`</a> and a <a href="sdk-for-ios-explore-structs-evconsumptionmodel#sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV18freeFlowSpeedTableSDys5Int32VSdGvp">`EVConsumptionModel.freeFlowSpeedTable`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV36ascentConsumptionInWattHoursPerMeterSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-ascentConsumptionInWattHoursPerMeter" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evconsumptionmodel#sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV36ascentConsumptionInWattHoursPerMeterSdvp" class="token"><code>ascentConsumptionInWattHoursPerMeter</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Rate of energy consumed per meter rise in elevation (in Wh/m, i.e., Watt-hours per meter).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var ascentConsumptionInWattHoursPerMeter: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV34descentRecoveryInWattHoursPerMeterSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-descentRecoveryInWattHoursPerMeter" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evconsumptionmodel#sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV34descentRecoveryInWattHoursPerMeterSdvp" class="token"><code>descentRecoveryInWattHoursPerMeter</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Rate of energy recovered per meter fall in elevation (in Wh/m, i.e., Watt-hours per meter).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var descentRecoveryInWattHoursPerMeter: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV18freeFlowSpeedTableSDys5Int32VSdGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-freeFlowSpeedTable" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evconsumptionmodel#sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV18freeFlowSpeedTableSDys5Int32VSdGvp" class="token"><code>freeFlowSpeedTable</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Free flow speed table describes energy consumption when traveling at constant speed. It defines a function curve specifying consumption rate at a given free flow speed on a flat stretch of road. Map keys represent speed values that are non-negative integers in units of (km/h). Map values represent consumption values that are non-negative floating point values in units of (Wh/m). The function is linearly interpolated between each successive pair of data points: For values below the first list value, the first value is used. For values after the last list value, the last list value is used. At minimum, one key/value pair must be set. In this case the consumption value is used for all possible speed keys.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var freeFlowSpeedTable: [Int32 : Double]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV17trafficSpeedTableSDys5Int32VSdGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trafficSpeedTable" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evconsumptionmodel#sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV17trafficSpeedTableSDys5Int32VSdGvp" class="token"><code>trafficSpeedTable</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Traffic speed table describes energy consumption when traveling under heavy traffic conditions, i.e. when the vehicle is expected to often change the travel speed. It defines a function curve specifying consumption rate at a given speed under traffic conditions on a flat stretch of road. Map keys represent traffic speed values that are non-negative integers in units of (km/h). Map values represent consumption values that are non-negative floating point values in units of (Wh/m). The function is linearly interpolated between each successive pair of data points: For values below the first list value, the first value is used. For values after the last list value, the last list value is used. If only one key/value pair is set, the consumption value is used for all possible traffic speed keys. If `EVConsumptionModel.trafficSpeedTable` is empty then only <a href="sdk-for-ios-explore-structs-evconsumptionmodel#sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV18freeFlowSpeedTableSDys5Int32VSdGvp">`EVConsumptionModel.freeFlowSpeedTable`</a> is used for calculating speed-related energy consumption.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficSpeedTable: [Int32 : Double]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV40auxiliaryConsumptionInWattHoursPerSecondSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-auxiliaryConsumptionInWattHoursPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evconsumptionmodel#sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV40auxiliaryConsumptionInWattHoursPerSecondSdvp" class="token"><code>auxiliaryConsumptionInWattHoursPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Rate of energy (in Wh/s) consumed by the vehicle’s auxiliary systems (e.g., air conditioning, lights) per second of travel.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var auxiliaryConsumptionInWattHoursPerSecond: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV36ascentConsumptionInWattHoursPerMeter015descentRecoveryfghiJ018freeFlowSpeedTable07trafficoP009auxiliaryefghI6SecondACSd_SdSDys5Int32VSdGAKSdtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-ascentConsumptionInWattHoursPerMeter-descentRecoveryInWattHoursPerMeter-freeFlowSpeedTable-trafficSpeedTable-auxiliaryConsumptionInWattHoursPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evconsumptionmodel#sdk-for-ios-explore-s-7heresdk18EVConsumptionModelV36ascentConsumptionInWattHoursPerMeter015descentRecoveryfghiJ018freeFlowSpeedTable07trafficoP009auxiliaryefghI6SecondACSd_SdSDys5Int32VSdGAKSdtcfc" class="token"><code>init(ascentConsumptionInWattHoursPerMeter:</code><wbr></wbr><code>descentRecoveryInWattHoursPerMeter:</code><wbr></wbr><code>freeFlowSpeedTable:</code><wbr></wbr><code>trafficSpeedTable:</code><wbr></wbr><code>auxiliaryConsumptionInWattHoursPerSecond:</code><wbr></wbr><code>)</code></a> 

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
  public init(ascentConsumptionInWattHoursPerMeter: Double = 0.0, descentRecoveryInWattHoursPerMeter: Double = 0.0, freeFlowSpeedTable: [Int32 : Double] = [:], trafficSpeedTable: [Int32 : Double] = [:], auxiliaryConsumptionInWattHoursPerSecond: Double = 0.0)
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


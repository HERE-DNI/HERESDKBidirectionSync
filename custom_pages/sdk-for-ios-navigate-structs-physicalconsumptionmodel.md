---
title: "PhysicalConsumptionModel Structure Reference"
slug: "sdk-for-ios-navigate-structs-physicalconsumptionmodel"
---

# PhysicalConsumptionModel

<div class="declaration">

<div class="language">

``` highlight
public struct PhysicalConsumptionModel : Hashable
```

</div>

</div>

Defines the physical consumption model for electric vehicles, using vehicle-specific parameters to calculate energy consumption along a route. **Note:** \[sdk.transport.VehicleSpecification.current_weight_in_kilograms\] must be set. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV20driveTrainEfficiencySdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-driveTrainEfficiency" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-physicalconsumptionmodel#sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV20driveTrainEfficiencySdvp" class="token"><code>driveTrainEfficiency</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The proportion of the energy drawn from the battery that is used to move the vehicle. (This is to factor in energy losses through heat in the motors, for example.) Supported range from 0 to 1

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var driveTrainEfficiency: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV22recuperationEfficiencySdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-recuperationEfficiency" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-physicalconsumptionmodel#sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV22recuperationEfficiencySdvp" class="token"><code>recuperationEfficiency</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The proportion of the energy gained when braking or going downhill that can be recuperated and restored as battery charge.

  Supported range from 0 to 1

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var recuperationEfficiency: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV014auxiliaryPowerC7InWattsSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-auxiliaryPowerConsumptionInWatts" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-physicalconsumptionmodel#sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV014auxiliaryPowerC7InWattsSdvp" class="token"><code>auxiliaryPowerConsumptionInWatts</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Power (in W) consumed by the vehicle’s auxiliary systems (for example, air conditioning, lights).

  The provided value must be greater than or equal to 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var auxiliaryPowerConsumptionInWatts: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV25frontalAreaInSquareMetersSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-frontalAreaInSquareMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-physicalconsumptionmodel#sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV25frontalAreaInSquareMetersSdvp" class="token"><code>frontalAreaInSquareMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters. Physical consumption model is using this value in combination with <a href="sdk-for-ios-navigate-structs-physicalconsumptionmodel#sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV18airDragCoefficientSdvp">`airDragCoefficient`</a> to calculate the consumption caused by air resistance. As fallback <a href="sdk-for-ios-navigate-structs-vehiclespecification#sdk-for-ios-navigate-s-7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">`VehicleSpecification.widthInCentimeters`</a> and <a href="sdk-for-ios-navigate-structs-vehiclespecification#sdk-for-ios-navigate-s-7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">`VehicleSpecification.heightInCentimeters`</a> are used.

  This parameter is used to provide a more accurate consumption prediction for electric vehicles.

  In the range from 0.5 to 50

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var frontalAreaInSquareMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV28rollingResistanceCoefficientSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-rollingResistanceCoefficient" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-physicalconsumptionmodel#sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV28rollingResistanceCoefficientSdvp" class="token"><code>rollingResistanceCoefficient</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Rolling resistance refers to the resistance experienced by your vehicle tire as it rolls over a surface. The main causes of this resistance are tire deformation, wing drag, and friction with the ground. The coefficient of rolling resistance is a numerical value indicating the severity of this factor.

  This parameter is used to provide a more accurate consumption prediction for electric vehicles.

  Supported range from 0 to 1

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var rollingResistanceCoefficient: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV18airDragCoefficientSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-airDragCoefficient" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-physicalconsumptionmodel#sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV18airDragCoefficientSdvp" class="token"><code>airDragCoefficient</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The drag coefficient of an vehicle defines the way the vehicle is expected to pass through the surrounding air. More streamlined vehicles are more aerodynamic and therefore have smaller drag coefficient.

  This parameter is used to provide a more accurate consumption prediction for electric vehicles.

  Supported range from 0 to 1

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var airDragCoefficient: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV20driveTrainEfficiency012recuperationG0014auxiliaryPowerC7InWatts011frontalAreaK12SquareMeters28rollingResistanceCoefficient07airDragS0ACSd_S5dtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-driveTrainEfficiency-recuperationEfficiency-auxiliaryPowerConsumptionInWatts-frontalAreaInSquareMeters-rollingResistanceCoefficient-airDragCoefficient" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-physicalconsumptionmodel#sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV20driveTrainEfficiency012recuperationG0014auxiliaryPowerC7InWatts011frontalAreaK12SquareMeters28rollingResistanceCoefficient07airDragS0ACSd_S5dtcfc" class="token"><code>init(driveTrainEfficiency:</code><wbr></wbr><code>recuperationEfficiency:</code><wbr></wbr><code>auxiliaryPowerConsumptionInWatts:</code><wbr></wbr><code>frontalAreaInSquareMeters:</code><wbr></wbr><code>rollingResistanceCoefficient:</code><wbr></wbr><code>airDragCoefficient:</code><wbr></wbr><code>)</code></a> 

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

    - driveTrainEfficiency: The proportion of the energy drawn from the battery that is used to move the vehicle. (This is to factor in energy losses through heat in the motors, for example.) Supported range from 0 to 1
    - recuperationEfficiency: The proportion of the energy gained when braking or going downhill that can be recuperated and restored as battery charge.

    Supported range from 0 to 1

    - auxiliaryPowerConsumptionInWatts: Power (in W) consumed by the vehicle’s auxiliary systems (for example, air conditioning, lights).

    The provided value must be greater than or equal to 0.

    - frontalAreaInSquareMeters: Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters. Physical consumption model is using this value in combination with <a href="sdk-for-ios-navigate-structs-physicalconsumptionmodel#sdk-for-ios-navigate-s-7heresdk24PhysicalConsumptionModelV18airDragCoefficientSdvp">`airDragCoefficient`</a> to calculate the consumption caused by air resistance. As fallback <a href="sdk-for-ios-navigate-structs-vehiclespecification#sdk-for-ios-navigate-s-7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">`VehicleSpecification.widthInCentimeters`</a> and <a href="sdk-for-ios-navigate-structs-vehiclespecification#sdk-for-ios-navigate-s-7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">`VehicleSpecification.heightInCentimeters`</a> are used.

    This parameter is used to provide a more accurate consumption prediction for electric vehicles.

    In the range from 0.5 to 50

    - rollingResistanceCoefficient: Rolling resistance refers to the resistance experienced by your vehicle tire as it rolls over a surface. The main causes of this resistance are tire deformation, wing drag, and friction with the ground. The coefficient of rolling resistance is a numerical value indicating the severity of this factor.

    This parameter is used to provide a more accurate consumption prediction for electric vehicles.

    Supported range from 0 to 1

    - airDragCoefficient: The drag coefficient of an vehicle defines the way the vehicle is expected to pass through the surrounding air. More streamlined vehicles are more aerodynamic and therefore have smaller drag coefficient.

    This parameter is used to provide a more accurate consumption prediction for electric vehicles.

    Supported range from 0 to 1

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(driveTrainEfficiency: Double = 0.1, recuperationEfficiency: Double = 0.1, auxiliaryPowerConsumptionInWatts: Double = 0.1, frontalAreaInSquareMeters: Double = 0.5, rollingResistanceCoefficient: Double = 0.1, airDragCoefficient: Double = 0.1)
  ```

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


---
title: "ScooterBuilder Class Reference"
slug: "sdk-for-ios-explore-structs-vehiclespecification-scooterbuilder"
---

# ScooterBuilder

<div class="declaration">

<div class="language">

``` highlight
public class ScooterBuilder
```

``` highlight
extension VehicleSpecification.ScooterBuilder: NativeBase
```

``` highlight
extension VehicleSpecification.ScooterBuilder: Hashable
```

</div>

Related types:

- <a href="sdk-for-ios-explore-structs-vehiclespecification">VehicleSpecification</a>

</div>

This class constructs a <a href="sdk-for-ios-explore-structs-vehiclespecification">`VehicleSpecification`</a> for a scooter.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV14ScooterBuilderCAEycfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-vehiclespecification-scooterbuilder#sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV14ScooterBuilderCAEycfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV14ScooterBuilderC32withEngineSizeInCubicCentimetersyAEs5Int32VF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-withEngineSizeInCubicCentimeters-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-vehiclespecification-scooterbuilder#sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV14ScooterBuilderC32withEngineSizeInCubicCentimetersyAEs5Int32VF" class="token"><code>withEngineSizeInCubicCentimeters(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle engine size in cubic centimeters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withEngineSizeInCubicCentimeters(_ engineSizeInCubicCentimeters: Int32) -> VehicleSpecification.ScooterBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-vehiclespecification">VehicleSpecification</a>

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
  <td><code> </code><em><code>engineSizeInCubicCentimeters</code></em><code> </code></td>
  <td><div>
  <p>The vehicle engine size in cubic centimeters.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.ScooterBuilder` object with the engine size set to the new value.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV14ScooterBuilderC13withOccupancyyAEs5Int32VF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-withOccupancy-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-vehiclespecification-scooterbuilder#sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV14ScooterBuilderC13withOccupancyyAEs5Int32VF" class="token"><code>withOccupancy(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle occupants number.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withOccupancy(_ occupancy: Int32) -> VehicleSpecification.ScooterBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-vehiclespecification">VehicleSpecification</a>

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
  <td><code> </code><em><code>occupancy</code></em><code> </code></td>
  <td><div>
  <p>The vehicle occupants number.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.ScooterBuilder` object with the vehicle occupants number set to the new value.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV14ScooterBuilderC5buildACyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-build" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-vehiclespecification-scooterbuilder#sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV14ScooterBuilderC5buildACyF" class="token"><code>build()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builds the <a href="sdk-for-ios-explore-structs-vehiclespecification">`VehicleSpecification`</a> object for <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO7scooteryA2CmF">`TransportMode.scooter`</a> with the specifications taken from the `VehicleSpecification.ScooterBuilder` object.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build() -> VehicleSpecification
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-vehiclespecification">VehicleSpecification</a>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-explore-structs-vehiclespecification">`VehicleSpecification`</a> object created from the `VehicleSpecification.ScooterBuilder` object.

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


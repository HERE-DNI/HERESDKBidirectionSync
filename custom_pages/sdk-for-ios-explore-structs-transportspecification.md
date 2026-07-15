---
title: "TransportSpecification Structure Reference"
slug: "sdk-for-ios-explore-structs-transportspecification"
---

# TransportSpecification

<div class="declaration">

<div class="language">

``` highlight
public struct TransportSpecification : Hashable
```

</div>

</div>

Contains transport attributes details related to the transport mode. **Notes**

- By default all vehicle specifications from `RoutingOptions.transport_specification` are set to `nil` and the `RoutingOptions.transport_specification.transport_mode` is set to <a href="sdk-for-ios-explore-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>.
- A route can be calculated with only the `RoutingOptions.transport_specification.transport_mode` set.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp"></span>` `<span id="//apple_ref/swift/Property/transportMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transportspecification#/s:7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp" class="token"><code>transportMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Transport mode. Defaults to `CAR`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var transportMode: TransportMode
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp"></span>` `<span id="//apple_ref/swift/Property/vehicleSpecification" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transportspecification#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp" class="token"><code>vehicleSpecification</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The vehicle specification for the transport mode. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var vehicleSpecification: VehicleSpecification?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV010pedestrianC0AA010PedestrianC0VSgvp"></span>` `<span id="//apple_ref/swift/Property/pedestrianSpecification" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transportspecification#/s:7heresdk22TransportSpecificationV010pedestrianC0AA010PedestrianC0VSgvp" class="token"><code>pedestrianSpecification</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The pedestrian specification for the transport mode. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var pedestrianSpecification: PedestrianSpecification?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV04taxiC0AA04TaxiC0VSgvp"></span>` `<span id="//apple_ref/swift/Property/taxiSpecification" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transportspecification#/s:7heresdk22TransportSpecificationV04taxiC0AA04TaxiC0VSgvp" class="token"><code>taxiSpecification</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The taxi specification for the transport mode. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var taxiSpecification: TaxiSpecification?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV07scooterC0AA07ScooterC0VSgvp"></span>` `<span id="//apple_ref/swift/Property/scooterSpecification" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transportspecification#/s:7heresdk22TransportSpecificationV07scooterC0AA07ScooterC0VSgvp" class="token"><code>scooterSpecification</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The scooter specification for the transport mode. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var scooterSpecification: ScooterSpecification?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(transportMode: vehicleSpecification: pedestrianSpecification: taxiSpecification: scooterSpecification: )

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
  public init ( transportMode : TransportMode = TransportMode . car , vehicleSpecification : VehicleSpecification ? = nil , pedestrianSpecification : PedestrianSpecification ? = nil , taxiSpecification : TaxiSpecification ? = nil , scooterSpecification : ScooterSpecification ? = nil )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV10CarBuilderC"></span>` `<span id="//apple_ref/swift/Class/CarBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transportspecification#/s:7heresdk22TransportSpecificationV10CarBuilderC" class="token"><code>CarBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> for a car.

  <a href="sdk-for-ios-explore-structs-transportspecification-carbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class CarBuilder
  ```

  ``` highlight
  extension TransportSpecification.CarBuilder: NativeBase
  ```

  ``` highlight
  extension TransportSpecification.CarBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV12TruckBuilderC"></span>` `<span id="//apple_ref/swift/Class/TruckBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transportspecification#/s:7heresdk22TransportSpecificationV12TruckBuilderC" class="token"><code>TruckBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> for a truck.

  <a href="sdk-for-ios-explore-structs-transportspecification-truckbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TruckBuilder
  ```

  ``` highlight
  extension TransportSpecification.TruckBuilder: NativeBase
  ```

  ``` highlight
  extension TransportSpecification.TruckBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV17PedestrianBuilderC"></span>` `<span id="//apple_ref/swift/Class/PedestrianBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transportspecification#/s:7heresdk22TransportSpecificationV17PedestrianBuilderC" class="token"><code>PedestrianBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> for pedestrian.

  <a href="sdk-for-ios-explore-structs-transportspecification-pedestrianbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PedestrianBuilder
  ```

  ``` highlight
  extension TransportSpecification.PedestrianBuilder: NativeBase
  ```

  ``` highlight
  extension TransportSpecification.PedestrianBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV14ScooterBuilderC"></span>` `<span id="//apple_ref/swift/Class/ScooterBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transportspecification#/s:7heresdk22TransportSpecificationV14ScooterBuilderC" class="token"><code>ScooterBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> for a scooter.

  <a href="sdk-for-ios-explore-structs-transportspecification-scooterbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class ScooterBuilder
  ```

  ``` highlight
  extension TransportSpecification.ScooterBuilder: NativeBase
  ```

  ``` highlight
  extension TransportSpecification.ScooterBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV14BicycleBuilderC"></span>` `<span id="//apple_ref/swift/Class/BicycleBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transportspecification#/s:7heresdk22TransportSpecificationV14BicycleBuilderC" class="token"><code>BicycleBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> for a bicycle.

  <a href="sdk-for-ios-explore-structs-transportspecification-bicyclebuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class BicycleBuilder
  ```

  ``` highlight
  extension TransportSpecification.BicycleBuilder: NativeBase
  ```

  ``` highlight
  extension TransportSpecification.BicycleBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV11TaxiBuilderC"></span>` `<span id="//apple_ref/swift/Class/TaxiBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transportspecification#/s:7heresdk22TransportSpecificationV11TaxiBuilderC" class="token"><code>TaxiBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> for a taxi.

  <a href="sdk-for-ios-explore-structs-transportspecification-taxibuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TaxiBuilder
  ```

  ``` highlight
  extension TransportSpecification.TaxiBuilder: NativeBase
  ```

  ``` highlight
  extension TransportSpecification.TaxiBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV10BusBuilderC"></span>` `<span id="//apple_ref/swift/Class/BusBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transportspecification#/s:7heresdk22TransportSpecificationV10BusBuilderC" class="token"><code>BusBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> for a bus.

  <a href="sdk-for-ios-explore-structs-transportspecification-busbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class BusBuilder
  ```

  ``` highlight
  extension TransportSpecification.BusBuilder: NativeBase
  ```

  ``` highlight
  extension TransportSpecification.BusBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV17PrivateBusBuilderC"></span>` `<span id="//apple_ref/swift/Class/PrivateBusBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transportspecification#/s:7heresdk22TransportSpecificationV17PrivateBusBuilderC" class="token"><code>PrivateBusBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> for a private bus.

  <a href="sdk-for-ios-explore-structs-transportspecification-privatebusbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PrivateBusBuilder
  ```

  ``` highlight
  extension TransportSpecification.PrivateBusBuilder: NativeBase
  ```

  ``` highlight
  extension TransportSpecification.PrivateBusBuilder: Hashable
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


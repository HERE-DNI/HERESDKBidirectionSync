---
title: "VehicleProfile Structure Reference"
slug: "sdk-for-ios-navigate-structs-vehicleprofile"
---

# VehicleProfile

<div class="declaration">

<div class="language">

``` highlight
@available(*, deprecated, message: "Will be removed in v4.28.0. Use `sdk.transport.TransportSpecification` instead.") public struct VehicleProfile : Hashable
```

</pre>

</div>

</div>

A vehicle profile describes the vehicle being used with the HSDK.

The profile is planned to be used as single source of information describing the vehicle.

Current modules that use this profile:

- Navigation: Tracking mode for truck related vehicle restrictions.

**Note:** This is a beta release of this vehicle profile, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases or even become unsupported, without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk14VehicleProfileV11vehicleTypeAA0bE0Ovp"></span>` `<span id="//apple_ref/swift/Property/vehicleType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehicleprofile#/s:7heresdk14VehicleProfileV11vehicleTypeAA0bE0Ovp" class="token"><code>vehicleType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the vehicle type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var vehicleType: VehicleType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14VehicleProfileV13truckCategoryAA05TruckE0OSgvp"></span>` `<span id="//apple_ref/swift/Property/truckCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehicleprofile#/s:7heresdk14VehicleProfileV13truckCategoryAA05TruckE0OSgvp" class="token"><code>truckCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the truck category. Only used when the <a href="sdk-for-ios-navigate-structs-vehicleprofile#/s:7heresdk14VehicleProfileV11vehicleTypeAA0bE0Ovp">`VehicleProfile.vehicleType`</a> is <a href="sdk-for-ios-navigate-enums-vehicletype#/s:7heresdk11VehicleTypeO5truckyA2CmF">`VehicleType.truck`</a> By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var truckCategory: TruckCategory?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14VehicleProfileV12trailerCounts5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/trailerCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehicleprofile#/s:7heresdk14VehicleProfileV12trailerCounts5Int32Vvp" class="token"><code>trailerCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. When not set, possible trailer count restrictions will not be taken into consideration for route calculation. By default, it is 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trailerCount: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14VehicleProfileV18hazardousMaterialsSayAA17HazardousMaterialOGvp"></span>` `<span id="//apple_ref/swift/Property/hazardousMaterials" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehicleprofile#/s:7heresdk14VehicleProfileV18hazardousMaterialsSayAA17HazardousMaterialOGvp" class="token"><code>hazardousMaterials</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies a list of hazardous materials shipped in the vehicle. Refer to <a href="sdk-for-ios-navigate-enums-hazardousmaterial">`HazardousMaterial`</a> for the available options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var hazardousMaterials: [HazardousMaterial]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14VehicleProfileV14tunnelCategoryAA06TunnelE0OSgvp"></span>` `<span id="//apple_ref/swift/Property/tunnelCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehicleprofile#/s:7heresdk14VehicleProfileV14tunnelCategoryAA06TunnelE0OSgvp" class="token"><code>tunnelCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the tunnel categories to restrict certain route links. The route will pass only through tunnels of a less strict category. Refer to <a href="sdk-for-ios-navigate-enums-tunnelcategory">`TunnelCategory`</a> for the available options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tunnelCategory: TunnelCategory?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14VehicleProfileV9axleCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/axleCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehicleprofile#/s:7heresdk14VehicleProfileV9axleCounts5Int32VSgvp" class="token"><code>axleCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. When not set, possible axle count restrictions will not be taken into consideration for route calculation. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var axleCount: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14VehicleProfileV22grossWeightInKilogramss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/grossWeightInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehicleprofile#/s:7heresdk14VehicleProfileV22grossWeightInKilogramss5Int32VSgvp" class="token"><code>grossWeightInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle weight including trailers and shipped goods in kilograms. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var grossWeightInKilograms: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14VehicleProfileV19heightInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/heightInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehicleprofile#/s:7heresdk14VehicleProfileV19heightInCentimeterss5Int32VSgvp" class="token"><code>heightInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var heightInCentimeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14VehicleProfileV19lengthInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/lengthInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehicleprofile#/s:7heresdk14VehicleProfileV19lengthInCentimeterss5Int32VSgvp" class="token"><code>lengthInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lengthInCentimeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14VehicleProfileV18widthInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/widthInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehicleprofile#/s:7heresdk14VehicleProfileV18widthInCentimeterss5Int32VSgvp" class="token"><code>widthInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var widthInCentimeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14VehicleProfileV24weightPerAxleInKilogramss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/weightPerAxleInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehicleprofile#/s:7heresdk14VehicleProfileV24weightPerAxleInKilogramss5Int32VSgvp" class="token"><code>weightPerAxleInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle weight per axle in kilograms. The provided value must be greater or equal to 0. When not set, possible weight per axle restrictions will not be taken into consideration for route calculation. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var weightPerAxleInKilograms: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(vehicleType: truckCategory: trailerCount: hazardousMaterials: tunnelCategory: axleCount: grossWeightInKilograms: heightInCentimeters: lengthInCentimeters: widthInCentimeters: weightPerAxleInKilograms: )

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
  public init ( vehicleType : VehicleType = VehicleType . car , truckCategory : TruckCategory ? = nil , trailerCount : Int32 = 0 , hazardousMaterials : [ HazardousMaterial ] = [], tunnelCategory : TunnelCategory ? = nil , axleCount : Int32 ? = nil , grossWeightInKilograms : Int32 ? = nil , heightInCentimeters : Int32 ? = nil , lengthInCentimeters : Int32 ? = nil , widthInCentimeters : Int32 ? = nil , weightPerAxleInKilograms : Int32 ? = nil )
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


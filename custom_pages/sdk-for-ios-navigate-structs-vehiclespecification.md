---
title: "VehicleSpecification Structure Reference"
slug: "sdk-for-ios-navigate-structs-vehiclespecification"
---

# VehicleSpecification

<div class="declaration">

<div class="language">

``` highlight
public struct VehicleSpecification : Hashable
```

</div>

</div>

Contains vehicle related attributes. Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/heightInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp" class="token"><code>heightInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

  **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

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

  ` `<span id="/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/widthInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp" class="token"><code>widthInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

  **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

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

  ` `<span id="/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/lengthInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp" class="token"><code>lengthInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

  **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

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

  ` `<span id="/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/axleCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp" class="token"><code>axleCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. Rendering: When set, truck restriction icons for an axle count greater than `VehicleSpecification.axleCount` will not be displayed. When specifying <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">`VehicleSpecification.trailerAxleCount`</a>, then `VehicleSpecification.axleCount` is required and must be greater than <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">`VehicleSpecification.trailerAxleCount`</a>.

  **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

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

  ` `<span id="/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/trailerCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp" class="token"><code>trailerCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. By default, it is not set. When specifying <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">`VehicleSpecification.trailerAxleCount`</a>, then `VehicleSpecification.trailerCount` is required and must be greater than 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trailerCount: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV9truckTypeAA05TruckE0Ovp"></span>` `<span id="//apple_ref/swift/Property/truckType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9truckTypeAA05TruckE0Ovp" class="token"><code>truckType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Will be replaced with <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp">`truckCategory`</a> when the `TruckSpecification` will be replaced by `VehicleSpecification`. Defines the type of truck. Defaults to <a href="sdk-for-ios-navigate-enums-trucktype#/s:7heresdk9TruckTypeO8straightyA2CmF">`TruckType.straight`</a>. Rendering `sdk.mapview.TruckProfile`: `VehicleSpecification.truckType` is ignored and has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.27.0. Use `VehicleSpecification.truckCategory` instead.") public var truckType : TruckType
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp"></span>` `<span id="//apple_ref/swift/Property/truckCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp" class="token"><code>truckCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the truck category. By default, it is not set. Rendering: `VehicleSpecification.truckCategory` is ignored and has no effect.

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

  ` `<span id="/s:7heresdk20VehicleSpecificationV12isTruckLightSbvp"></span>` `<span id="//apple_ref/swift/Property/isTruckLight" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV12isTruckLightSbvp" class="token"><code>isTruckLight</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan. The flag should not be set to `true` in other countries than Japan. Defaults to `false`.

  A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets the vehicle can access, which access restrictions apply, and which speed limits are applicable. Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will not always overwrite these settings. Make sure to not exceed the specifications that classify a truck as light.

  In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to `true`, you will get, for example, the same speed limits as for cars. Make sure to set the flag only to `true`, when a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.

  When on <a href="sdk-for-ios-navigate-classes-mapcontentsettings">`MapContentSettings`</a>, then this flag will be ignored and has no effect.

  **Notes:**

  - This flag and the concept of light trucks are supported only in Japan as beta and are considered to be experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.

  <div class="aside aside-note">

  Note

  Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  - Supported only in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a> transport mode.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isTruckLight: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV26payloadCapacityInKilogramss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/payloadCapacityInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV26payloadCapacityInKilogramss5Int32VSgvp" class="token"><code>payloadCapacityInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Allowed payload capacity, including trailers, specified in kilograms. The provided value must be greater then or equal to 0. By default, it is not set.

  **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var payloadCapacityInKilograms: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/trailerAxleCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp" class="token"><code>trailerAxleCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines total number of axles across all the trailers attached to the vehicle. This number is included in <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a>, hence `VehicleSpecification.trailerAxleCount` must be less than <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a> and greater than or equal to 1. <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a> and <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">`VehicleSpecification.trailerCount`</a> are required to specify `VehicleSpecification.trailerAxleCount`. By default, it is not set.

  **Note:**: This parameter is currently used only for the calculation of tolls in regions where it is applicable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trailerAxleCount: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV38kingpinToRearAxleDistanceInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/kingpinToRearAxleDistanceInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV38kingpinToRearAxleDistanceInCentimeterss5Int32VSgvp" class="token"><code>kingpinToRearAxleDistanceInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the kingpin to rear axle distance, in centimeters.

  **NOTE:** Currently, the KPRA restrictions are only present in California and Idaho. **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var kingpinToRearAxleDistanceInCentimeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV22emptyWeightInKilogramss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/emptyWeightInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV22emptyWeightInKilogramss5Int32VSgvp" class="token"><code>emptyWeightInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Empty weight of the vehicle without any load, excluding trailers, specified in kilograms. The provided value must be greater than or equal to 0. By default, it is not set.

  **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var emptyWeightInKilograms: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/grossWeightInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp" class="token"><code>grossWeightInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">`VehicleSpecification.currentWeightInKilograms`</a>. By default, it is not set.

  **Notes:**

  - Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.
  - Maximum weight for a car or taxi *without* a trailer is 4250 kg.
  - Maximum weight for a car or taxi *with* a trailer is 7550 kg.

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

  ` `<span id="/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/currentWeightInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp" class="token"><code>currentWeightInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Current truck weight, including trailers and shipped goods currently loaded, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">`VehicleSpecification.grossWeightInKilograms`</a>. By default, it is not set.

  **Notes:**

  - Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.
  - Maximum weight for a car or taxi *without* a trailer is 5000 kg.
  - Maximum weight for a car or taxi *with* a trailer is 8500 kg.
  - A route request with `VehicleSpecification.currentWeightInKilograms` above <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">`VehicleSpecification.grossWeightInKilograms`</a> may result in non-compliant or invalid routes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var currentWeightInKilograms: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/weightPerAxleInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp" class="token"><code>weightPerAxleInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Heaviest weight per axle, regardless of axle type or axle group. It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions. The provided value must be greater or equal to 0. By default, it is not set.

  **Notes:**

  - `VehicleSpecification.weightPerAxleInKilograms` and <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">`VehicleSpecification.weightPerAxleGroup`</a> are incompatible. When available for your edition, if both attributes are set, during online <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> an `RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> is in place, both parameters are evaluated and the maximum value between them will be used.
  - Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

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

  ` `<span id="/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp"></span>` `<span id="//apple_ref/swift/Property/weightPerAxleGroup" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp" class="token"><code>weightPerAxleGroup</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Allows specification of axle weights in a more fine-grained way than <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">`VehicleSpecification.weightPerAxleInKilograms`</a>. This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden. By default is not set.

  **Notes:**

  - <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">`VehicleSpecification.weightPerAxleInKilograms`</a> and `VehicleSpecification.weightPerAxleGroup` are incompatible. When available for your edition, if both attributes are set, during online <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> an `RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> is in place, both parameters are evaluated and the maximum value between them will be used.
  - Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var weightPerAxleGroup: WeightPerAxleGroup?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV12isCommercialSbvp"></span>` `<span id="//apple_ref/swift/Property/isCommercial" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV12isCommercialSbvp" class="token"><code>isCommercial</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies whether the vehicle is a commercial or a non-commercial vehicle. Defaults to `false`.

  **Notes**

  - Only supported for online routing.
  - This parameter is currently used only for the calculation of tolls in regions where it is applicable.
  - Not used for offline calculations.
  - Supported for <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a> and <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isCommercial: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV27lastCharacterOfLicensePlateSSSgvp"></span>` `<span id="//apple_ref/swift/Property/lastCharacterOfLicensePlate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV27lastCharacterOfLicensePlateSSSgvp" class="token"><code>lastCharacterOfLicensePlate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Last character of license plate in String format. This value can be used to evaluate restrictions in environmental zones. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lastCharacterOfLicensePlate: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV28engineSizeInCubicCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/engineSizeInCubicCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV28engineSizeInCubicCentimeterss5Int32VSgvp" class="token"><code>engineSizeInCubicCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Engine size of the scooter in cubic centimeters. Shouldn’t be less than 1 or greater than 65535. Default value is `nil`, which means the scooter route calculation ignores all engine size limits on the road.

  **Notes**

  - For now, this option is only relevant in Japan and will be ignored for other countries. Currently, map data for this option is only available for Japan.
  - Supported only in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO7scooteryA2CmF">`TransportMode.scooter`</a> (Alpha) transport mode.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var engineSizeInCubicCentimeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV10tiresCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/tiresCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV10tiresCounts5Int32VSgvp" class="token"><code>tiresCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The total number of tires the vehicle has, i.e., the tires on the base vehicle and any attached trailers. By default, it is not set. Otherwise it is guaranteed to be in the range \[1, 255\].

  **Note**: This parameter is not supported in isoline routing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tiresCount: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV14tunnelCategoryAA06TunnelE0OSgvp"></span>` `<span id="//apple_ref/swift/Property/tunnelCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV14tunnelCategoryAA06TunnelE0OSgvp" class="token"><code>tunnelCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the tunnel categories to restrict certain route links. The route will pass only through tunnels of a less strict category. Refer to <a href="sdk-for-ios-navigate-enums-tunnelcategory">`TunnelCategory`</a> for the available options. By default, it is not set.

  **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

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

  ` `<span id="/s:7heresdk20VehicleSpecificationV18hazardousMaterialsSayAA17HazardousMaterialOGvp"></span>` `<span id="//apple_ref/swift/Property/hazardousMaterials" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18hazardousMaterialsSayAA17HazardousMaterialOGvp" class="token"><code>hazardousMaterials</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies a list of hazardous materials shipped in the vehicle. Refer to <a href="sdk-for-ios-navigate-enums-hazardousmaterial">`HazardousMaterial`</a> for the available options. By default, it is an empty list.

  **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

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

  ` `<span id="/s:7heresdk20VehicleSpecificationV9occupancys5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/occupancy" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9occupancys5Int32VSgvp" class="token"><code>occupancy</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the number of occupants in the vehicle, including driver, can affect the vehicle’s ability to use HOV/carpool restricted lanes. Should not be less than 1 or greater than 255. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var occupancy: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(heightInCentimeters: widthInCentimeters: lengthInCentimeters: axleCount: trailerCount: truckCategory: isTruckLight: payloadCapacityInKilograms: trailerAxleCount: kingpinToRearAxleDistanceInCentimeters: emptyWeightInKilograms: grossWeightInKilograms: currentWeightInKilograms: weightPerAxleInKilograms: weightPerAxleGroup: isCommercial: lastCharacterOfLicensePlate: engineSizeInCubicCentimeters: tiresCount: tunnelCategory: hazardousMaterials: occupancy: )

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

    - heightInCentimeters: Vehicle height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - widthInCentimeters: Vehicle width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - lengthInCentimeters: Vehicle length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - axleCount: Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. Rendering: When set, truck restriction icons for an axle count greater than <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a> will not be displayed. When specifying <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">`VehicleSpecification.trailerAxleCount`</a>, then <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a> is required and must be greater than <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">`VehicleSpecification.trailerAxleCount`</a>.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - trailerCount: Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. By default, it is not set. When specifying <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">`VehicleSpecification.trailerAxleCount`</a>, then <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">`VehicleSpecification.trailerCount`</a> is required and must be greater than 0.
    - truckCategory: Defines the truck category. By default, it is not set. Rendering: <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp">`VehicleSpecification.truckCategory`</a> is ignored and has no effect.
    - isTruckLight: A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan. The flag should not be set to `true` in other countries than Japan. Defaults to `false`.

    A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets the vehicle can access, which access restrictions apply, and which speed limits are applicable. Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will not always overwrite these settings. Make sure to not exceed the specifications that classify a truck as light.

    In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to `true`, you will get, for example, the same speed limits as for cars. Make sure to set the flag only to `true`, when a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.

    When on <a href="sdk-for-ios-navigate-classes-mapcontentsettings">`MapContentSettings`</a>, then this flag will be ignored and has no effect.

    **Notes:**

    - This flag and the concept of light trucks are supported only in Japan as beta and are considered to be experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.

    <div class="aside aside-note">

    Note

    Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    - Supported only in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a> transport mode.
      - payloadCapacityInKilograms: Allowed payload capacity, including trailers, specified in kilograms. The provided value must be greater then or equal to 0. By default, it is not set.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - trailerAxleCount: Defines total number of axles across all the trailers attached to the vehicle. This number is included in <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a>, hence <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">`VehicleSpecification.trailerAxleCount`</a> must be less than <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a> and greater than or equal to 1. <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a> and <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">`VehicleSpecification.trailerCount`</a> are required to specify <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">`VehicleSpecification.trailerAxleCount`</a>. By default, it is not set.

    **Note:**: This parameter is currently used only for the calculation of tolls in regions where it is applicable.

    - kingpinToRearAxleDistanceInCentimeters: Defines the kingpin to rear axle distance, in centimeters.

    **NOTE:** Currently, the KPRA restrictions are only present in California and Idaho. **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - emptyWeightInKilograms: Empty weight of the vehicle without any load, excluding trailers, specified in kilograms. The provided value must be greater than or equal to 0. By default, it is not set.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - grossWeightInKilograms: Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">`VehicleSpecification.currentWeightInKilograms`</a>. By default, it is not set.

    **Notes:**

    - Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.
    - Maximum weight for a car or taxi *without* a trailer is 4250 kg.
    - Maximum weight for a car or taxi *with* a trailer is 7550 kg.
      - currentWeightInKilograms: Current truck weight, including trailers and shipped goods currently loaded, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">`VehicleSpecification.grossWeightInKilograms`</a>. By default, it is not set.

    **Notes:**

    - Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.
    - Maximum weight for a car or taxi *without* a trailer is 5000 kg.
    - Maximum weight for a car or taxi *with* a trailer is 8500 kg.
    - A route request with <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">`VehicleSpecification.currentWeightInKilograms`</a> above <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">`VehicleSpecification.grossWeightInKilograms`</a> may result in non-compliant or invalid routes.
      - weightPerAxleInKilograms: Heaviest weight per axle, regardless of axle type or axle group. It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions. The provided value must be greater or equal to 0. By default, it is not set.

    **Notes:**

    - <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">`VehicleSpecification.weightPerAxleInKilograms`</a> and <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">`VehicleSpecification.weightPerAxleGroup`</a> are incompatible. When available for your edition, if both attributes are set, during online <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> an `RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> is in place, both parameters are evaluated and the maximum value between them will be used.
    - Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.
      - weightPerAxleGroup: Allows specification of axle weights in a more fine-grained way than <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">`VehicleSpecification.weightPerAxleInKilograms`</a>. This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden. By default is not set.

    **Notes:**

    - <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">`VehicleSpecification.weightPerAxleInKilograms`</a> and <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">`VehicleSpecification.weightPerAxleGroup`</a> are incompatible. When available for your edition, if both attributes are set, during online <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> an `RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> is in place, both parameters are evaluated and the maximum value between them will be used.
    - Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.
      - isCommercial: Specifies whether the vehicle is a commercial or a non-commercial vehicle. Defaults to `false`.

    **Notes**

    - Only supported for online routing.
    - This parameter is currently used only for the calculation of tolls in regions where it is applicable.
    - Not used for offline calculations.
    - Supported for <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a> and <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a>.
      - lastCharacterOfLicensePlate: Last character of license plate in String format. This value can be used to evaluate restrictions in environmental zones. By default, it is not set.
      - engineSizeInCubicCentimeters: Engine size of the scooter in cubic centimeters. Shouldn’t be less than 1 or greater than 65535. Default value is `nil`, which means the scooter route calculation ignores all engine size limits on the road.

    **Notes**

    - For now, this option is only relevant in Japan and will be ignored for other countries. Currently, map data for this option is only available for Japan.
    - Supported only in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO7scooteryA2CmF">`TransportMode.scooter`</a> (Alpha) transport mode.
      - tiresCount: The total number of tires the vehicle has, i.e., the tires on the base vehicle and any attached trailers. By default, it is not set. Otherwise it is guaranteed to be in the range \[1, 255\].

    **Note**: This parameter is not supported in isoline routing.

    - tunnelCategory: Specifies the tunnel categories to restrict certain route links. The route will pass only through tunnels of a less strict category. Refer to <a href="sdk-for-ios-navigate-enums-tunnelcategory">`TunnelCategory`</a> for the available options. By default, it is not set.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - hazardousMaterials: Specifies a list of hazardous materials shipped in the vehicle. Refer to <a href="sdk-for-ios-navigate-enums-hazardousmaterial">`HazardousMaterial`</a> for the available options. By default, it is an empty list.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - occupancy: Specifies the number of occupants in the vehicle, including driver, can affect the vehicle’s ability to use HOV/carpool restricted lanes. Should not be less than 1 or greater than 255. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( heightInCentimeters : Int32 ? = nil , widthInCentimeters : Int32 ? = nil , lengthInCentimeters : Int32 ? = nil , axleCount : Int32 ? = nil , trailerCount : Int32 ? = nil , truckCategory : TruckCategory ? = nil , isTruckLight : Bool = false , payloadCapacityInKilograms : Int32 ? = nil , trailerAxleCount : Int32 ? = nil , kingpinToRearAxleDistanceInCentimeters : Int32 ? = nil , emptyWeightInKilograms : Int32 ? = nil , grossWeightInKilograms : Int32 ? = nil , currentWeightInKilograms : Int32 ? = nil , weightPerAxleInKilograms : Int32 ? = nil , weightPerAxleGroup : WeightPerAxleGroup ? = nil , isCommercial : Bool = false , lastCharacterOfLicensePlate : String ? = nil , engineSizeInCubicCentimeters : Int32 ? = nil , tiresCount : Int32 ? = nil , tunnelCategory : TunnelCategory ? = nil , hazardousMaterials : [ HazardousMaterial ] = [], occupancy : Int32 ? = nil )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      init(heightInCentimeters: widthInCentimeters: lengthInCentimeters: axleCount: trailerCount: truckType: truckCategory: isTruckLight: payloadCapacityInKilograms: trailerAxleCount: kingpinToRearAxleDistanceInCentimeters: emptyWeightInKilograms: grossWeightInKilograms: currentWeightInKilograms: weightPerAxleInKilograms: weightPerAxleGroup: isCommercial: lastCharacterOfLicensePlate: engineSizeInCubicCentimeters: tiresCount: tunnelCategory: hazardousMaterials: occupancy: )

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

    - heightInCentimeters: Vehicle height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - widthInCentimeters: Vehicle width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - lengthInCentimeters: Vehicle length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - axleCount: Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. Rendering: When set, truck restriction icons for an axle count greater than <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a> will not be displayed. When specifying <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">`VehicleSpecification.trailerAxleCount`</a>, then <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a> is required and must be greater than <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">`VehicleSpecification.trailerAxleCount`</a>.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - trailerCount: Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. By default, it is not set. When specifying <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">`VehicleSpecification.trailerAxleCount`</a>, then <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">`VehicleSpecification.trailerCount`</a> is required and must be greater than 0.
    - truckType: Will be replaced with <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp">`truckCategory`</a> when the `TruckSpecification` will be replaced by `VehicleSpecification`. Defines the type of truck. Defaults to <a href="sdk-for-ios-navigate-enums-trucktype#/s:7heresdk9TruckTypeO8straightyA2CmF">`TruckType.straight`</a>. Rendering `sdk.mapview.TruckProfile`: <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9truckTypeAA05TruckE0Ovp">`VehicleSpecification.truckType`</a> is ignored and has no effect.
    - truckCategory: Defines the truck category. By default, it is not set. Rendering: <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp">`VehicleSpecification.truckCategory`</a> is ignored and has no effect.
    - isTruckLight: A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan. The flag should not be set to `true` in other countries than Japan. Defaults to `false`.

    A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets the vehicle can access, which access restrictions apply, and which speed limits are applicable. Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will not always overwrite these settings. Make sure to not exceed the specifications that classify a truck as light.

    In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to `true`, you will get, for example, the same speed limits as for cars. Make sure to set the flag only to `true`, when a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.

    When on <a href="sdk-for-ios-navigate-classes-mapcontentsettings">`MapContentSettings`</a>, then this flag will be ignored and has no effect.

    **Notes:**

    - This flag and the concept of light trucks are supported only in Japan as beta and are considered to be experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.

    <div class="aside aside-note">

    Note

    Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    - Supported only in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a> transport mode.
      - payloadCapacityInKilograms: Allowed payload capacity, including trailers, specified in kilograms. The provided value must be greater then or equal to 0. By default, it is not set.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - trailerAxleCount: Defines total number of axles across all the trailers attached to the vehicle. This number is included in <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a>, hence <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">`VehicleSpecification.trailerAxleCount`</a> must be less than <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a> and greater than or equal to 1. <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a> and <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">`VehicleSpecification.trailerCount`</a> are required to specify <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">`VehicleSpecification.trailerAxleCount`</a>. By default, it is not set.

    **Note:**: This parameter is currently used only for the calculation of tolls in regions where it is applicable.

    - kingpinToRearAxleDistanceInCentimeters: Defines the kingpin to rear axle distance, in centimeters.

    **NOTE:** Currently, the KPRA restrictions are only present in California and Idaho. **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - emptyWeightInKilograms: Empty weight of the vehicle without any load, excluding trailers, specified in kilograms. The provided value must be greater than or equal to 0. By default, it is not set.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - grossWeightInKilograms: Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">`VehicleSpecification.currentWeightInKilograms`</a>. By default, it is not set.

    **Notes:**

    - Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.
    - Maximum weight for a car or taxi *without* a trailer is 4250 kg.
    - Maximum weight for a car or taxi *with* a trailer is 7550 kg.
      - currentWeightInKilograms: Current truck weight, including trailers and shipped goods currently loaded, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">`VehicleSpecification.grossWeightInKilograms`</a>. By default, it is not set.

    **Notes:**

    - Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.
    - Maximum weight for a car or taxi *without* a trailer is 5000 kg.
    - Maximum weight for a car or taxi *with* a trailer is 8500 kg.
    - A route request with <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">`VehicleSpecification.currentWeightInKilograms`</a> above <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">`VehicleSpecification.grossWeightInKilograms`</a> may result in non-compliant or invalid routes.
      - weightPerAxleInKilograms: Heaviest weight per axle, regardless of axle type or axle group. It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions. The provided value must be greater or equal to 0. By default, it is not set.

    **Notes:**

    - <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">`VehicleSpecification.weightPerAxleInKilograms`</a> and <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">`VehicleSpecification.weightPerAxleGroup`</a> are incompatible. When available for your edition, if both attributes are set, during online <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> an `RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> is in place, both parameters are evaluated and the maximum value between them will be used.
    - Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.
      - weightPerAxleGroup: Allows specification of axle weights in a more fine-grained way than <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">`VehicleSpecification.weightPerAxleInKilograms`</a>. This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden. By default is not set.

    **Notes:**

    - <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">`VehicleSpecification.weightPerAxleInKilograms`</a> and <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">`VehicleSpecification.weightPerAxleGroup`</a> are incompatible. When available for your edition, if both attributes are set, during online <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> an `RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> is in place, both parameters are evaluated and the maximum value between them will be used.
    - Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.
      - isCommercial: Specifies whether the vehicle is a commercial or a non-commercial vehicle. Defaults to `false`.

    **Notes**

    - Only supported for online routing.
    - This parameter is currently used only for the calculation of tolls in regions where it is applicable.
    - Not used for offline calculations.
    - Supported for <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a> and <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a>.
      - lastCharacterOfLicensePlate: Last character of license plate in String format. This value can be used to evaluate restrictions in environmental zones. By default, it is not set.
      - engineSizeInCubicCentimeters: Engine size of the scooter in cubic centimeters. Shouldn’t be less than 1 or greater than 65535. Default value is `nil`, which means the scooter route calculation ignores all engine size limits on the road.

    **Notes**

    - For now, this option is only relevant in Japan and will be ignored for other countries. Currently, map data for this option is only available for Japan.
    - Supported only in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO7scooteryA2CmF">`TransportMode.scooter`</a> (Alpha) transport mode.
      - tiresCount: The total number of tires the vehicle has, i.e., the tires on the base vehicle and any attached trailers. By default, it is not set. Otherwise it is guaranteed to be in the range \[1, 255\].

    **Note**: This parameter is not supported in isoline routing.

    - tunnelCategory: Specifies the tunnel categories to restrict certain route links. The route will pass only through tunnels of a less strict category. Refer to <a href="sdk-for-ios-navigate-enums-tunnelcategory">`TunnelCategory`</a> for the available options. By default, it is not set.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - hazardousMaterials: Specifies a list of hazardous materials shipped in the vehicle. Refer to <a href="sdk-for-ios-navigate-enums-hazardousmaterial">`HazardousMaterial`</a> for the available options. By default, it is an empty list.

    **Note:** Supported in <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3busyA2CmF">`TransportMode.bus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10privateBusyA2CmF">`TransportMode.privateBus`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a> (Beta), <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> (Beta) transport modes.

    - occupancy: Specifies the number of occupants in the vehicle, including driver, can affect the vehicle’s ability to use HOV/carpool restricted lanes. Should not be less than 1 or greater than 255. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated) public init ( heightInCentimeters : Int32 ? = nil , widthInCentimeters : Int32 ? = nil , lengthInCentimeters : Int32 ? = nil , axleCount : Int32 ? = nil , trailerCount : Int32 ? = nil , truckType : TruckType = TruckType . straight , truckCategory : TruckCategory ? = nil , isTruckLight : Bool = false , payloadCapacityInKilograms : Int32 ? = nil , trailerAxleCount : Int32 ? = nil , kingpinToRearAxleDistanceInCentimeters : Int32 ? = nil , emptyWeightInKilograms : Int32 ? = nil , grossWeightInKilograms : Int32 ? = nil , currentWeightInKilograms : Int32 ? = nil , weightPerAxleInKilograms : Int32 ? = nil , weightPerAxleGroup : WeightPerAxleGroup ? = nil , isCommercial : Bool = false , lastCharacterOfLicensePlate : String ? = nil , engineSizeInCubicCentimeters : Int32 ? = nil , tiresCount : Int32 ? = nil , tunnelCategory : TunnelCategory ? = nil , hazardousMaterials : [ HazardousMaterial ] = [], occupancy : Int32 ? = nil )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV10CarBuilderC"></span>` `<span id="//apple_ref/swift/Class/CarBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV10CarBuilderC" class="token"><code>CarBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-navigate-structs-vehiclespecification">`VehicleSpecification`</a> for a car.

  <a href="sdk-for-ios-navigate-structs-vehiclespecification-carbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class CarBuilder
  ```

  ``` highlight
  extension VehicleSpecification.CarBuilder: NativeBase
  ```

  ``` highlight
  extension VehicleSpecification.CarBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV12TruckBuilderC"></span>` `<span id="//apple_ref/swift/Class/TruckBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV12TruckBuilderC" class="token"><code>TruckBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-navigate-structs-vehiclespecification">`VehicleSpecification`</a> for a truck.

  <a href="sdk-for-ios-navigate-structs-vehiclespecification-truckbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TruckBuilder
  ```

  ``` highlight
  extension VehicleSpecification.TruckBuilder: NativeBase
  ```

  ``` highlight
  extension VehicleSpecification.TruckBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV14ScooterBuilderC"></span>` `<span id="//apple_ref/swift/Class/ScooterBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV14ScooterBuilderC" class="token"><code>ScooterBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-navigate-structs-vehiclespecification">`VehicleSpecification`</a> for a scooter.

  <a href="sdk-for-ios-navigate-structs-vehiclespecification-scooterbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC"></span>` `<span id="//apple_ref/swift/Class/TaxiBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC" class="token"><code>TaxiBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-navigate-structs-vehiclespecification">`VehicleSpecification`</a> for a taxi.

  <a href="sdk-for-ios-navigate-structs-vehiclespecification-taxibuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TaxiBuilder
  ```

  ``` highlight
  extension VehicleSpecification.TaxiBuilder: NativeBase
  ```

  ``` highlight
  extension VehicleSpecification.TaxiBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV10BusBuilderC"></span>` `<span id="//apple_ref/swift/Class/BusBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV10BusBuilderC" class="token"><code>BusBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-navigate-structs-vehiclespecification">`VehicleSpecification`</a> for a bus.

  <a href="sdk-for-ios-navigate-structs-vehiclespecification-busbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class BusBuilder
  ```

  ``` highlight
  extension VehicleSpecification.BusBuilder: NativeBase
  ```

  ``` highlight
  extension VehicleSpecification.BusBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20VehicleSpecificationV17PrivateBusBuilderC"></span>` `<span id="//apple_ref/swift/Class/PrivateBusBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV17PrivateBusBuilderC" class="token"><code>PrivateBusBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class constructs a <a href="sdk-for-ios-navigate-structs-vehiclespecification">`VehicleSpecification`</a> for a private bus.

  <a href="sdk-for-ios-navigate-structs-vehiclespecification-privatebusbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PrivateBusBuilder
  ```

  ``` highlight
  extension VehicleSpecification.PrivateBusBuilder: NativeBase
  ```

  ``` highlight
  extension VehicleSpecification.PrivateBusBuilder: Hashable
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


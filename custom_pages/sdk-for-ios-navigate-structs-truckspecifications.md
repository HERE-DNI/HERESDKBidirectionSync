---
title: "TruckSpecifications Structure Reference"
slug: "sdk-for-ios-navigate-structs-truckspecifications"
---

# TruckSpecifications

<div class="declaration">

<div class="language">

``` highlight
@available(*, deprecated, message: "Will be removed in v4.28.0. Use `TransportSpecification` instead.") public struct TruckSpecifications : Hashable
```

</pre>

</div>

</div>

Truck specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk19TruckSpecificationsV22grossWeightInKilogramss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/grossWeightInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV22grossWeightInKilogramss5Int32VSgvp" class="token"><code>grossWeightInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV24currentWeightInKilogramss5Int32VSgvp">`TruckSpecifications.currentWeightInKilograms`</a>. By default, it is not set.

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

  ` `<span id="/s:7heresdk19TruckSpecificationsV24currentWeightInKilogramss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/currentWeightInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV24currentWeightInKilogramss5Int32VSgvp" class="token"><code>currentWeightInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Current truck weight, including trailers and shipped goods currently loaded, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV22grossWeightInKilogramss5Int32VSgvp">`TruckSpecifications.grossWeightInKilograms`</a>. By default, it is not set.

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

  ` `<span id="/s:7heresdk19TruckSpecificationsV24weightPerAxleInKilogramss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/weightPerAxleInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV24weightPerAxleInKilogramss5Int32VSgvp" class="token"><code>weightPerAxleInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Heaviest weight per axle, regardless of axle type or axle group. It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions. The provided value must be greater or equal to 0. By default, it is not set. **Note:** `weight_per_axle_in_kilograms` and `weight_per_axle_group` are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.

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

  ` `<span id="/s:7heresdk19TruckSpecificationsV18weightPerAxleGroupAA06WeightefG0VSgvp"></span>` `<span id="//apple_ref/swift/Property/weightPerAxleGroup" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV18weightPerAxleGroupAA06WeightefG0VSgvp" class="token"><code>weightPerAxleGroup</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Allows specification of axle weights in a more fine-grained way than `weight_per_axle_in_kilograms`. This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden. By default is not set. **Note:** `weight_per_axle_in_kilograms` and `weight_per_axle_group` are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.

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

  ` `<span id="/s:7heresdk19TruckSpecificationsV19heightInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/heightInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV19heightInCentimeterss5Int32VSgvp" class="token"><code>heightInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Truck height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

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

  ` `<span id="/s:7heresdk19TruckSpecificationsV18widthInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/widthInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV18widthInCentimeterss5Int32VSgvp" class="token"><code>widthInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Truck width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

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

  ` `<span id="/s:7heresdk19TruckSpecificationsV19lengthInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/lengthInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV19lengthInCentimeterss5Int32VSgvp" class="token"><code>lengthInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Truck length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

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

  ` `<span id="/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/axleCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp" class="token"><code>axleCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. Rendering `sdk.mapview.TruckProfile`: When set, truck restriction icons for an axle count greater than `TruckSpecifications.axleCount` will not be displayed. When specifying <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">`TruckSpecifications.trailerAxleCount`</a>, then `TruckSpecifications.axleCount` is required and must be greater than <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">`TruckSpecifications.trailerAxleCount`</a>.

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

  ` `<span id="/s:7heresdk19TruckSpecificationsV12trailerCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/trailerCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV12trailerCounts5Int32VSgvp" class="token"><code>trailerCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. By default, it is not set. When specifying <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">`TruckSpecifications.trailerAxleCount`</a>, then `TruckSpecifications.trailerCount` is required and must be greater than 0.

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

  ` `<span id="/s:7heresdk19TruckSpecificationsV9truckTypeAA0bE0Ovp"></span>` `<span id="//apple_ref/swift/Property/truckType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV9truckTypeAA0bE0Ovp" class="token"><code>truckType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the type of truck. By default, it is <a href="sdk-for-ios-navigate-enums-trucktype#/s:7heresdk9TruckTypeO8straightyA2CmF">`TruckType.straight`</a>. Rendering `sdk.mapview.TruckProfile`: `TruckSpecifications.truckType` is ignored and has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var truckType: TruckType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19TruckSpecificationsV02isB5LightSbvp"></span>` `<span id="//apple_ref/swift/Property/isTruckLight" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV02isB5LightSbvp" class="token"><code>isTruckLight</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan. The flag should not be set to `true` in other countries than Japan. The flag defaults to `false`.

  A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets the vehicle can access, which access restrictions apply, and which speed limits are applicable. Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will not always overwrite these settings: Make sure to not exceed the specifications that classify a truck as light.

  In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to true, you will get, for example, the same speed limits as for cars. Make sure to set the flag only to true, when a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.

  When `TruckSpecifications` are set as part of <a href="sdk-for-ios-navigate-classes-mapcontentsettings">`MapContentSettings`</a>, then this flag will be ignored and has no effect.

  **Note:** This flag and the concept of light trucks are supported only in Japan as beta and are considered to be experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan. Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases with a deprecation process.

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

  ` `<span id="/s:7heresdk19TruckSpecificationsV26payloadCapacityInKilogramss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/payloadCapacityInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV26payloadCapacityInKilogramss5Int32VSgvp" class="token"><code>payloadCapacityInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Allowed payload capacity, including trailers, specified in kilograms. The provided value must be greater then or equal to 0. By default, it is not set.

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

  ` `<span id="/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/trailerAxleCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp" class="token"><code>trailerAxleCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines total number of axles across all the trailers attached to the vehicle. This number is included in <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">`TruckSpecifications.axleCount`</a>, hence `TruckSpecifications.trailerAxleCount` must be less than <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">`TruckSpecifications.axleCount`</a> and greater than or equal to 1. <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">`TruckSpecifications.axleCount`</a> and <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV12trailerCounts5Int32VSgvp">`TruckSpecifications.trailerCount`</a> are required to specify `TruckSpecifications.trailerAxleCount`. By default, it is not set. Note: This parameter is currently used only for the calculation of tolls in regions where it is applicable.

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

      init(grossWeightInKilograms: currentWeightInKilograms: weightPerAxleInKilograms: weightPerAxleGroup: heightInCentimeters: widthInCentimeters: lengthInCentimeters: axleCount: trailerCount: truckType: isTruckLight: payloadCapacityInKilograms: trailerAxleCount: )

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

    - grossWeightInKilograms: Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV24currentWeightInKilogramss5Int32VSgvp">`TruckSpecifications.currentWeightInKilograms`</a>. By default, it is not set.
    - currentWeightInKilograms: Current truck weight, including trailers and shipped goods currently loaded, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV22grossWeightInKilogramss5Int32VSgvp">`TruckSpecifications.grossWeightInKilograms`</a>. By default, it is not set.
    - weightPerAxleInKilograms: Heaviest weight per axle, regardless of axle type or axle group. It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions. The provided value must be greater or equal to 0. By default, it is not set. **Note:** `weight_per_axle_in_kilograms` and `weight_per_axle_group` are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.
    - weightPerAxleGroup: Allows specification of axle weights in a more fine-grained way than `weight_per_axle_in_kilograms`. This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden. By default is not set. **Note:** `weight_per_axle_in_kilograms` and `weight_per_axle_group` are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.
    - heightInCentimeters: Truck height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.
    - widthInCentimeters: Truck width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.
    - lengthInCentimeters: Truck length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.
    - axleCount: Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. Rendering `sdk.mapview.TruckProfile`: When set, truck restriction icons for an axle count greater than <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">`TruckSpecifications.axleCount`</a> will not be displayed. When specifying <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">`TruckSpecifications.trailerAxleCount`</a>, then <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">`TruckSpecifications.axleCount`</a> is required and must be greater than <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">`TruckSpecifications.trailerAxleCount`</a>.
    - trailerCount: Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. By default, it is not set. When specifying <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">`TruckSpecifications.trailerAxleCount`</a>, then <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV12trailerCounts5Int32VSgvp">`TruckSpecifications.trailerCount`</a> is required and must be greater than 0.
    - truckType: Defines the type of truck. By default, it is <a href="sdk-for-ios-navigate-enums-trucktype#/s:7heresdk9TruckTypeO8straightyA2CmF">`TruckType.straight`</a>. Rendering `sdk.mapview.TruckProfile`: <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV9truckTypeAA0bE0Ovp">`TruckSpecifications.truckType`</a> is ignored and has no effect.
    - isTruckLight: A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan. The flag should not be set to `true` in other countries than Japan. The flag defaults to `false`.

    A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets the vehicle can access, which access restrictions apply, and which speed limits are applicable. Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will not always overwrite these settings: Make sure to not exceed the specifications that classify a truck as light.

    In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to true, you will get, for example, the same speed limits as for cars. Make sure to set the flag only to true, when a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.

    When `TruckSpecifications` are set as part of <a href="sdk-for-ios-navigate-classes-mapcontentsettings">`MapContentSettings`</a>, then this flag will be ignored and has no effect.

    **Note:** This flag and the concept of light trucks are supported only in Japan as beta and are considered to be experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan. Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases with a deprecation process.

    - payloadCapacityInKilograms: Allowed payload capacity, including trailers, specified in kilograms. The provided value must be greater then or equal to 0. By default, it is not set.
    - trailerAxleCount: Defines total number of axles across all the trailers attached to the vehicle. This number is included in <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">`TruckSpecifications.axleCount`</a>, hence <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">`TruckSpecifications.trailerAxleCount`</a> must be less than <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">`TruckSpecifications.axleCount`</a> and greater than or equal to 1. <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">`TruckSpecifications.axleCount`</a> and <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV12trailerCounts5Int32VSgvp">`TruckSpecifications.trailerCount`</a> are required to specify <a href="sdk-for-ios-navigate-structs-truckspecifications#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">`TruckSpecifications.trailerAxleCount`</a>. By default, it is not set. Note: This parameter is currently used only for the calculation of tolls in regions where it is applicable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( grossWeightInKilograms : Int32 ? = nil , currentWeightInKilograms : Int32 ? = nil , weightPerAxleInKilograms : Int32 ? = nil , weightPerAxleGroup : WeightPerAxleGroup ? = nil , heightInCentimeters : Int32 ? = nil , widthInCentimeters : Int32 ? = nil , lengthInCentimeters : Int32 ? = nil , axleCount : Int32 ? = nil , trailerCount : Int32 ? = nil , truckType : TruckType = TruckType . straight , isTruckLight : Bool = false , payloadCapacityInKilograms : Int32 ? = nil , trailerAxleCount : Int32 ? = nil )
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


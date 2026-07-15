---
title: "Details Structure Reference"
slug: "sdk-for-ios-navigate-structs-violatedrestriction-details"
---

# Details

<div class="declaration">

<div class="language">

``` highlight
public struct Details : Hashable
```

</div>

</div>

Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set. For example, if the vehicle violates the maximum allowed height during the trip, then the member `max_height_in_centimeters` will be set with the maximum allowed height value.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV27maxWeightPerAxleInKilogramss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/maxWeightPerAxleInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV27maxWeightPerAxleInKilogramss5Int32VSgvp" class="token"><code>maxWeightPerAxleInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Max permitted weight per axle during the trip, in kilograms. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">`VehicleSpecification.weightPerAxleInKilograms`</a> exceeds this value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxWeightPerAxleInKilograms: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV32maxWeightPerAxleGroupInKilogramsAA03MaxhiF0VSgvp"></span>` `<span id="//apple_ref/swift/Property/maxWeightPerAxleGroupInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV32maxWeightPerAxleGroupInKilogramsAA03MaxhiF0VSgvp" class="token"><code>maxWeightPerAxleGroupInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Max permitted weight per axle group during the trip, in kilograms. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">`VehicleSpecification.weightPerAxleGroup`</a> exceeds this value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxWeightPerAxleGroupInKilograms: MaxAxleGroupWeight?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV22maxHeightInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/maxHeightInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV22maxHeightInCentimeterss5Int32VSgvp" class="token"><code>maxHeightInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Max permitted height during the trip, in centimeters. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">`VehicleSpecification.heightInCentimeters`</a> exceeds this value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxHeightInCentimeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV21maxWidthInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/maxWidthInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV21maxWidthInCentimeterss5Int32VSgvp" class="token"><code>maxWidthInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Max permitted width during the trip, in centimeters. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">`VehicleSpecification.widthInCentimeters`</a> exceeds this value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxWidthInCentimeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV22maxLengthInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/maxLengthInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV22maxLengthInCentimeterss5Int32VSgvp" class="token"><code>maxLengthInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Max permitted length during the trip, in centimeters. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp">`VehicleSpecification.lengthInCentimeters`</a> exceeds this value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxLengthInCentimeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV18forbiddenAxleCountAA12IntegerRangeVSgvp"></span>` `<span id="//apple_ref/swift/Property/forbiddenAxleCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV18forbiddenAxleCountAA12IntegerRangeVSgvp" class="token"><code>forbiddenAxleCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The restriction to trucks with axles number within specified range during the trip. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a> is within this range.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var forbiddenAxleCount: IntegerRange?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV21forbiddenTrailerCountAA12IntegerRangeVSgvp"></span>` `<span id="//apple_ref/swift/Property/forbiddenTrailerCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV21forbiddenTrailerCountAA12IntegerRangeVSgvp" class="token"><code>forbiddenTrailerCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constrains the restriction to trucks with number of trailer within specified range during the trip. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">`VehicleSpecification.trailerCount`</a> is within this range.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var forbiddenTrailerCount: IntegerRange?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV23forbiddenHazardousGoodsSayAA0F8MaterialOGvp"></span>` `<span id="//apple_ref/swift/Property/forbiddenHazardousGoods" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV23forbiddenHazardousGoodsSayAA0F8MaterialOGvp" class="token"><code>forbiddenHazardousGoods</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used for the route calculation provided using <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18hazardousMaterialsSayAA17HazardousMaterialOGvp">`VehicleSpecification.hazardousMaterials`</a> from <a href="sdk-for-ios-navigate-structs-transportspecification#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">`TransportSpecification.vehicleSpecification`</a> from <a href="sdk-for-ios-navigate-structs-routingoptions#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">`RoutingOptions.transportSpecification`</a>. This property is the intersection of the two lists.

  **Note** <a href="sdk-for-ios-navigate-structs-roadsignwarning">`RoadSignWarning`</a> events and `RouteViolations` are only given for violations that are indicated on a road sign. Additional legal restrictions might apply when transporting hazardous materials.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var forbiddenHazardousGoods: [HazardousMaterial]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV17maxTunnelCategoryAA0fG0OSgvp"></span>` `<span id="//apple_ref/swift/Property/maxTunnelCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV17maxTunnelCategoryAA0fG0OSgvp" class="token"><code>maxTunnelCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tunnel category to restrict transport of specific goods during the trip. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV14tunnelCategoryAA06TunnelE0OSgvp">`VehicleSpecification.tunnelCategory`</a> from <a href="sdk-for-ios-navigate-structs-transportspecification#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">`TransportSpecification.vehicleSpecification`</a> from <a href="sdk-for-ios-navigate-structs-routingoptions#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">`RoutingOptions.transportSpecification`</a> exceeds this value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxTunnelCategory: TunnelCategory?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV18forbiddenTruckTypeAA0fG0OSgvp"></span>` `<span id="//apple_ref/swift/Property/forbiddenTruckType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV18forbiddenTruckTypeAA0fG0OSgvp" class="token"><code>forbiddenTruckType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This property will be set if a restriction applies to the value of <a href="sdk-for-ios-navigate-enums-trucktype">`TruckType`</a> parameter used for route calculation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.27.0. Use `forbidden_truck_category` instead.") public var forbiddenTruckType : TruckType ?
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV22forbiddenTruckCategoryAA0fG0OSgvp"></span>` `<span id="//apple_ref/swift/Property/forbiddenTruckCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV22forbiddenTruckCategoryAA0fG0OSgvp" class="token"><code>forbiddenTruckCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This property will be set if a restriction applies to the value of <a href="sdk-for-ios-navigate-enums-truckcategory">`TruckCategory`</a> parameter used for route calculation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var forbiddenTruckCategory: TruckCategory?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV23forbiddenTruckRoadTypesSayAA0fG4TypeOGvp"></span>` `<span id="//apple_ref/swift/Property/forbiddenTruckRoadTypes" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV23forbiddenTruckRoadTypesSayAA0fG4TypeOGvp" class="token"><code>forbiddenTruckRoadTypes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains violated restrictions for truck road types.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var forbiddenTruckRoadTypes: [TruckRoadType]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV20routingZoneReferenceSSSgvp"></span>` `<span id="//apple_ref/swift/Property/routingZoneReference" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV20routingZoneReferenceSSSgvp" class="token"><code>routingZoneReference</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains the restricted routing zone reference This property will be set if the <a href="sdk-for-ios-navigate-structs-avoidanceoptions#/s:7heresdk16AvoidanceOptionsV14zoneCategoriesSayAA12ZoneCategoryOGvp">`AvoidanceOptions.zoneCategories`</a> is not empty

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routingZoneReference: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV29maxPayloadCapacityInKilogramss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/maxPayloadCapacityInKilograms" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV29maxPayloadCapacityInKilogramss5Int32VSgvp" class="token"><code>maxPayloadCapacityInKilograms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Max permitted payload capacity during the trip, in kilograms. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV26payloadCapacityInKilogramss5Int32VSgvp">`VehicleSpecification.payloadCapacityInKilograms`</a> exceeds this value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxPayloadCapacityInKilograms: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV8timeRuleAA04TimeF0CSgvp"></span>` `<span id="//apple_ref/swift/Property/timeRule" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV8timeRuleAA04TimeF0CSgvp" class="token"><code>timeRule</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Time intervals during which restrictions are enforced.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timeRule: TimeRule?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV9maxWeightAA07Vehiclec3MaxF0VSgvp"></span>` `<span id="//apple_ref/swift/Property/maxWeight" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV9maxWeightAA07Vehiclec3MaxF0VSgvp" class="token"><code>maxWeight</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">`VehicleSpecification.grossWeightInKilograms`</a> parameter used for route calculation exceeds this value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxWeight: VehicleRestrictionMaxWeight?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV16maxNumberOfTiress5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/maxNumberOfTires" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV16maxNumberOfTiress5Int32VSgvp" class="token"><code>maxNumberOfTires</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains the maximum permitted number of tires. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV10tiresCounts5Int32VSgvp">`VehicleSpecification.tiresCount`</a> exceeds the specified value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxNumberOfTires: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ViolatedRestrictionV7DetailsV41maxKingpinToRearAxleDistanceInCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/maxKingpinToRearAxleDistanceInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-violatedrestriction-details#/s:7heresdk19ViolatedRestrictionV7DetailsV41maxKingpinToRearAxleDistanceInCentimeterss5Int32VSgvp" class="token"><code>maxKingpinToRearAxleDistanceInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains the maximum permitted distance from kingpin to the rear axle in centimeters. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV38kingpinToRearAxleDistanceInCentimeterss5Int32VSgvp">`VehicleSpecification.kingpinToRearAxleDistanceInCentimeters`</a> exceeds the specified value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxKingpinToRearAxleDistanceInCentimeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(maxWeightPerAxleInKilograms: maxWeightPerAxleGroupInKilograms: maxHeightInCentimeters: maxWidthInCentimeters: maxLengthInCentimeters: forbiddenAxleCount: forbiddenTrailerCount: forbiddenHazardousGoods: maxTunnelCategory: forbiddenTruckCategory: forbiddenTruckRoadTypes: routingZoneReference: maxPayloadCapacityInKilograms: timeRule: maxWeight: maxNumberOfTires: maxKingpinToRearAxleDistanceInCentimeters: )

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

    - maxWeightPerAxleInKilograms: Max permitted weight per axle during the trip, in kilograms. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">`VehicleSpecification.weightPerAxleInKilograms`</a> exceeds this value.
    - maxWeightPerAxleGroupInKilograms: Max permitted weight per axle group during the trip, in kilograms. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">`VehicleSpecification.weightPerAxleGroup`</a> exceeds this value.
    - maxHeightInCentimeters: Max permitted height during the trip, in centimeters. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">`VehicleSpecification.heightInCentimeters`</a> exceeds this value.
    - maxWidthInCentimeters: Max permitted width during the trip, in centimeters. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">`VehicleSpecification.widthInCentimeters`</a> exceeds this value.
    - maxLengthInCentimeters: Max permitted length during the trip, in centimeters. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp">`VehicleSpecification.lengthInCentimeters`</a> exceeds this value.
    - forbiddenAxleCount: The restriction to trucks with axles number within specified range during the trip. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a> is within this range.
    - forbiddenTrailerCount: Constrains the restriction to trucks with number of trailer within specified range during the trip. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">`VehicleSpecification.trailerCount`</a> is within this range.
    - forbiddenHazardousGoods: There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used for the route calculation provided using <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18hazardousMaterialsSayAA17HazardousMaterialOGvp">`VehicleSpecification.hazardousMaterials`</a> from <a href="sdk-for-ios-navigate-structs-transportspecification#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">`TransportSpecification.vehicleSpecification`</a> from <a href="sdk-for-ios-navigate-structs-routingoptions#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">`RoutingOptions.transportSpecification`</a>. This property is the intersection of the two lists.

    **Note** <a href="sdk-for-ios-navigate-structs-roadsignwarning">`RoadSignWarning`</a> events and `RouteViolations` are only given for violations that are indicated on a road sign. Additional legal restrictions might apply when transporting hazardous materials.

    - maxTunnelCategory: Tunnel category to restrict transport of specific goods during the trip. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV14tunnelCategoryAA06TunnelE0OSgvp">`VehicleSpecification.tunnelCategory`</a> from <a href="sdk-for-ios-navigate-structs-transportspecification#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">`TransportSpecification.vehicleSpecification`</a> from <a href="sdk-for-ios-navigate-structs-routingoptions#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">`RoutingOptions.transportSpecification`</a> exceeds this value.
    - forbiddenTruckCategory: This property will be set if a restriction applies to the value of <a href="sdk-for-ios-navigate-enums-truckcategory">`TruckCategory`</a> parameter used for route calculation.
    - forbiddenTruckRoadTypes: Contains violated restrictions for truck road types.
    - routingZoneReference: Contains the restricted routing zone reference This property will be set if the <a href="sdk-for-ios-navigate-structs-avoidanceoptions#/s:7heresdk16AvoidanceOptionsV14zoneCategoriesSayAA12ZoneCategoryOGvp">`AvoidanceOptions.zoneCategories`</a> is not empty
    - maxPayloadCapacityInKilograms: Max permitted payload capacity during the trip, in kilograms. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV26payloadCapacityInKilogramss5Int32VSgvp">`VehicleSpecification.payloadCapacityInKilograms`</a> exceeds this value.
    - timeRule: Time intervals during which restrictions are enforced.
    - maxWeight: Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">`VehicleSpecification.grossWeightInKilograms`</a> parameter used for route calculation exceeds this value.
    - maxNumberOfTires: Contains the maximum permitted number of tires. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV10tiresCounts5Int32VSgvp">`VehicleSpecification.tiresCount`</a> exceeds the specified value.
    - maxKingpinToRearAxleDistanceInCentimeters: Contains the maximum permitted distance from kingpin to the rear axle in centimeters. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV38kingpinToRearAxleDistanceInCentimeterss5Int32VSgvp">`VehicleSpecification.kingpinToRearAxleDistanceInCentimeters`</a> exceeds the specified value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( maxWeightPerAxleInKilograms : Int32 ? = nil , maxWeightPerAxleGroupInKilograms : MaxAxleGroupWeight ? = nil , maxHeightInCentimeters : Int32 ? = nil , maxWidthInCentimeters : Int32 ? = nil , maxLengthInCentimeters : Int32 ? = nil , forbiddenAxleCount : IntegerRange ? = nil , forbiddenTrailerCount : IntegerRange ? = nil , forbiddenHazardousGoods : [ HazardousMaterial ] = [], maxTunnelCategory : TunnelCategory ? = nil , forbiddenTruckCategory : TruckCategory ? = nil , forbiddenTruckRoadTypes : [ TruckRoadType ] = [], routingZoneReference : String ? = nil , maxPayloadCapacityInKilograms : Int32 ? = nil , timeRule : TimeRule ? = nil , maxWeight : VehicleRestrictionMaxWeight ? = nil , maxNumberOfTires : Int32 ? = nil , maxKingpinToRearAxleDistanceInCentimeters : Int32 ? = nil )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      init(maxWeightPerAxleInKilograms: maxWeightPerAxleGroupInKilograms: maxHeightInCentimeters: maxWidthInCentimeters: maxLengthInCentimeters: forbiddenAxleCount: forbiddenTrailerCount: forbiddenHazardousGoods: maxTunnelCategory: forbiddenTruckType: forbiddenTruckCategory: forbiddenTruckRoadTypes: routingZoneReference: maxPayloadCapacityInKilograms: timeRule: maxWeight: maxNumberOfTires: maxKingpinToRearAxleDistanceInCentimeters: )

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

    - maxWeightPerAxleInKilograms: Max permitted weight per axle during the trip, in kilograms. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">`VehicleSpecification.weightPerAxleInKilograms`</a> exceeds this value.
    - maxWeightPerAxleGroupInKilograms: Max permitted weight per axle group during the trip, in kilograms. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">`VehicleSpecification.weightPerAxleGroup`</a> exceeds this value.
    - maxHeightInCentimeters: Max permitted height during the trip, in centimeters. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">`VehicleSpecification.heightInCentimeters`</a> exceeds this value.
    - maxWidthInCentimeters: Max permitted width during the trip, in centimeters. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">`VehicleSpecification.widthInCentimeters`</a> exceeds this value.
    - maxLengthInCentimeters: Max permitted length during the trip, in centimeters. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp">`VehicleSpecification.lengthInCentimeters`</a> exceeds this value.
    - forbiddenAxleCount: The restriction to trucks with axles number within specified range during the trip. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">`VehicleSpecification.axleCount`</a> is within this range.
    - forbiddenTrailerCount: Constrains the restriction to trucks with number of trailer within specified range during the trip. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">`VehicleSpecification.trailerCount`</a> is within this range.
    - forbiddenHazardousGoods: There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used for the route calculation provided using <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18hazardousMaterialsSayAA17HazardousMaterialOGvp">`VehicleSpecification.hazardousMaterials`</a> from <a href="sdk-for-ios-navigate-structs-transportspecification#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">`TransportSpecification.vehicleSpecification`</a> from <a href="sdk-for-ios-navigate-structs-routingoptions#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">`RoutingOptions.transportSpecification`</a>. This property is the intersection of the two lists.

    **Note** <a href="sdk-for-ios-navigate-structs-roadsignwarning">`RoadSignWarning`</a> events and `RouteViolations` are only given for violations that are indicated on a road sign. Additional legal restrictions might apply when transporting hazardous materials.

    - maxTunnelCategory: Tunnel category to restrict transport of specific goods during the trip. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV14tunnelCategoryAA06TunnelE0OSgvp">`VehicleSpecification.tunnelCategory`</a> from <a href="sdk-for-ios-navigate-structs-transportspecification#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">`TransportSpecification.vehicleSpecification`</a> from <a href="sdk-for-ios-navigate-structs-routingoptions#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">`RoutingOptions.transportSpecification`</a> exceeds this value.
    - forbiddenTruckType: This property will be set if a restriction applies to the value of <a href="sdk-for-ios-navigate-enums-trucktype">`TruckType`</a> parameter used for route calculation.
    - forbiddenTruckCategory: This property will be set if a restriction applies to the value of <a href="sdk-for-ios-navigate-enums-truckcategory">`TruckCategory`</a> parameter used for route calculation.
    - forbiddenTruckRoadTypes: Contains violated restrictions for truck road types.
    - routingZoneReference: Contains the restricted routing zone reference This property will be set if the <a href="sdk-for-ios-navigate-structs-avoidanceoptions#/s:7heresdk16AvoidanceOptionsV14zoneCategoriesSayAA12ZoneCategoryOGvp">`AvoidanceOptions.zoneCategories`</a> is not empty
    - maxPayloadCapacityInKilograms: Max permitted payload capacity during the trip, in kilograms. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV26payloadCapacityInKilogramss5Int32VSgvp">`VehicleSpecification.payloadCapacityInKilograms`</a> exceeds this value.
    - timeRule: Time intervals during which restrictions are enforced.
    - maxWeight: Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">`VehicleSpecification.grossWeightInKilograms`</a> parameter used for route calculation exceeds this value.
    - maxNumberOfTires: Contains the maximum permitted number of tires. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV10tiresCounts5Int32VSgvp">`VehicleSpecification.tiresCount`</a> exceeds the specified value.
    - maxKingpinToRearAxleDistanceInCentimeters: Contains the maximum permitted distance from kingpin to the rear axle in centimeters. This property will be set if the <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV38kingpinToRearAxleDistanceInCentimeterss5Int32VSgvp">`VehicleSpecification.kingpinToRearAxleDistanceInCentimeters`</a> exceeds the specified value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated) public init ( maxWeightPerAxleInKilograms : Int32 ? = nil , maxWeightPerAxleGroupInKilograms : MaxAxleGroupWeight ? = nil , maxHeightInCentimeters : Int32 ? = nil , maxWidthInCentimeters : Int32 ? = nil , maxLengthInCentimeters : Int32 ? = nil , forbiddenAxleCount : IntegerRange ? = nil , forbiddenTrailerCount : IntegerRange ? = nil , forbiddenHazardousGoods : [ HazardousMaterial ] = [], maxTunnelCategory : TunnelCategory ? = nil , forbiddenTruckType : TruckType ? = nil , forbiddenTruckCategory : TruckCategory ? = nil , forbiddenTruckRoadTypes : [ TruckRoadType ] = [], routingZoneReference : String ? = nil , maxPayloadCapacityInKilograms : Int32 ? = nil , timeRule : TimeRule ? = nil , maxWeight : VehicleRestrictionMaxWeight ? = nil , maxNumberOfTires : Int32 ? = nil , maxKingpinToRearAxleDistanceInCentimeters : Int32 ? = nil )
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


---
title: "Transport  Reference"
slug: "sdk-for-ios-explore-transport"
---

# Transport

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk17BusSpecificationsV"></span>` `<span id="//apple_ref/swift/Struct/BusSpecifications" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk17BusSpecificationsV" class="token"><code>BusSpecifications</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Bus specifications contain vehicle related attributes. Examples: height, weight, width. Only the fields that are set are considered for restriction handling.

  <a href="sdk-for-ios-explore-structs-busspecifications" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use `TransportSpecification` instead.") public struct BusSpecifications : Hashable
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17CarSpecificationsV"></span>` `<span id="//apple_ref/swift/Struct/CarSpecifications" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk17CarSpecificationsV" class="token"><code>CarSpecifications</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Car specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.

  <a href="sdk-for-ios-explore-structs-carspecifications" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use `TransportSpecification` instead.") public struct CarSpecifications : Hashable
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25GeneralVehicleSpeedLimitsV"></span>` `<span id="//apple_ref/swift/Struct/GeneralVehicleSpeedLimits" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk25GeneralVehicleSpeedLimitsV" class="token"><code>GeneralVehicleSpeedLimits</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains the speed limits for vehicles in a country / state.

  <a href="sdk-for-ios-explore-structs-generalvehiclespeedlimits" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeneralVehicleSpeedLimits : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk28HazardousMaterialRestrictionV"></span>` `<span id="//apple_ref/swift/Struct/HazardousMaterialRestriction" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk28HazardousMaterialRestrictionV" class="token"><code>HazardousMaterialRestriction</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents restriction on transport of hazardous materials. A generic restriction, applying to any hazardous material, is encoded with empty member variables.

  **Note:** This is a beta release of this feature. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-hazardousmaterialrestriction" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct HazardousMaterialRestriction : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23PedestrianSpecificationV"></span>` `<span id="//apple_ref/swift/Struct/PedestrianSpecification" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk23PedestrianSpecificationV" class="token"><code>PedestrianSpecification</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Pedestrian specific settings.

  <a href="sdk-for-ios-explore-structs-pedestrianspecification" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct PedestrianSpecification : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RestrictionTypeO"></span>` `<span id="//apple_ref/swift/Enum/RestrictionType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk15RestrictionTypeO" class="token"><code>RestrictionType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of vehicle restriction.

  **Note:** This is a beta release of this feature. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-restrictiontype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum RestrictionType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20ScooterSpecificationV"></span>` `<span id="//apple_ref/swift/Struct/ScooterSpecification" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk20ScooterSpecificationV" class="token"><code>ScooterSpecification</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Scooter specific settings.

  <a href="sdk-for-ios-explore-structs-scooterspecification" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ScooterSpecification : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19SpecificRestrictionV"></span>` `<span id="//apple_ref/swift/Struct/SpecificRestriction" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk19SpecificRestrictionV" class="token"><code>SpecificRestriction</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a specific vehicle restriction. A `SpecificRestriction` defines what type of restriction applies (weight, height, etc.) and the range of allowed values. It is always used as part of a <a href="sdk-for-ios-explore-structs-vehiclerestriction">`VehicleRestriction`</a>.

  **Note:** This is a beta release of this feature. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-specificrestriction" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SpecificRestriction : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17TaxiSpecificationV"></span>` `<span id="//apple_ref/swift/Struct/TaxiSpecification" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk17TaxiSpecificationV" class="token"><code>TaxiSpecification</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Taxi specific settings.

  <a href="sdk-for-ios-explore-structs-taxispecification" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TaxiSpecification : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TimeRestrictionV"></span>` `<span id="//apple_ref/swift/Struct/TimeRestriction" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk15TimeRestrictionV" class="token"><code>TimeRestriction</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents restriction based on time.

  **Note:** This is a beta release of this feature. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-timerestriction" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TimeRestriction : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13TransportModeO"></span>` `<span id="//apple_ref/swift/Enum/TransportMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk13TransportModeO" class="token"><code>TransportMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the mode of transport used for route calculalation.

  <a href="sdk-for-ios-explore-enums-transportmode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TransportMode : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TransportSpecificationV"></span>` `<span id="//apple_ref/swift/Struct/TransportSpecification" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk22TransportSpecificationV" class="token"><code>TransportSpecification</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains transport attributes details related to the transport mode. **Notes**

  - By default all vehicle specifications from `RoutingOptions.transport_specification` are set to `nil` and the `RoutingOptions.transport_specification.transport_mode` is set to <a href="sdk-for-ios-explore-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>.
  - A route can be calculated with only the `RoutingOptions.transport_specification.transport_mode` set.

  <a href="sdk-for-ios-explore-structs-transportspecification" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TransportSpecification : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13TransportTypeO"></span>` `<span id="//apple_ref/swift/Enum/TransportType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk13TransportTypeO" class="token"><code>TransportType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies types of transportation for which access/restriction rules apply.

  **Note:** This is a beta release of this feature. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-transporttype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TransportType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13TruckCategoryO"></span>` `<span id="//apple_ref/swift/Enum/TruckCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk13TruckCategoryO" class="token"><code>TruckCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the truck category. **Note:** This is a **beta release** of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-truckcategory" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TruckCategory : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10TruckClassO"></span>` `<span id="//apple_ref/swift/Enum/TruckClass" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk10TruckClassO" class="token"><code>TruckClass</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines truck class based on weight. Note: This is a BETA feature and thus subject to change.

  <a href="sdk-for-ios-explore-enums-truckclass" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TruckClass : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13TruckRoadTypeO"></span>` `<span id="//apple_ref/swift/Enum/TruckRoadType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk13TruckRoadTypeO" class="token"><code>TruckRoadType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies Truck road type

  <a href="sdk-for-ios-explore-enums-truckroadtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TruckRoadType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13TruckFuelTypeO"></span>` `<span id="//apple_ref/swift/Enum/TruckFuelType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk13TruckFuelTypeO" class="token"><code>TruckFuelType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Define possible fuel types for trucks provided by a fuel station. Note: This is a BETA feature and thus subject to change.

  <a href="sdk-for-ios-explore-enums-truckfueltype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TruckFuelType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18VehicleRestrictionV"></span>` `<span id="//apple_ref/swift/Struct/VehicleRestriction" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk18VehicleRestrictionV" class="token"><code>VehicleRestriction</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a vehicle restriction.

  Any non `nil` property adds more details to the restriction. A general truck restriction is represented with `nil` values for properties `restriction` and `hazmatRestriction`.

  **Note:** This is a beta release of this feature. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-vehiclerestriction" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct VehicleRestriction : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11VehicleTypeO"></span>` `<span id="//apple_ref/swift/Enum/VehicleType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk11VehicleTypeO" class="token"><code>VehicleType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the type of the vehicle.

  **Note:** This is a beta release of this vehicle type, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases or even become unsupported, without a deprecation process.

  <a href="sdk-for-ios-explore-enums-vehicletype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use `sdk.transport.TransportMode` instead.") public enum VehicleType : UInt32 , CaseIterable , Codable
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14VehicleProfileV"></span>` `<span id="//apple_ref/swift/Struct/VehicleProfile" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk14VehicleProfileV" class="token"><code>VehicleProfile</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A vehicle profile describes the vehicle being used with the HSDK.

  The profile is planned to be used as single source of information describing the vehicle.

  Current modules that use this profile:

  - Navigation: Tracking mode for truck related vehicle restrictions.

  **Note:** This is a beta release of this vehicle profile, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases or even become unsupported, without a deprecation process.

  <a href="sdk-for-ios-explore-structs-vehicleprofile" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use `sdk.transport.TransportSpecification` instead.") public struct VehicleProfile : Hashable
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18WeightPerAxleGroupV"></span>` `<span id="//apple_ref/swift/Struct/WeightPerAxleGroup" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-transport#/s:7heresdk18WeightPerAxleGroupV" class="token"><code>WeightPerAxleGroup</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Struct which defines the weight of the different axle groups of a vehicle. The provided value must be greater or equal to 0.

  <a href="sdk-for-ios-explore-structs-weightperaxlegroup" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct WeightPerAxleGroup : Hashable
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


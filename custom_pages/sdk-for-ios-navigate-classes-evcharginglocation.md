---
title: "EVChargingLocation Class Reference"
slug: "sdk-for-ios-navigate-classes-evcharginglocation"
---

# EVChargingLocation

<div class="declaration">

<div class="language">

``` highlight
public class EVChargingLocation
```

``` highlight
extension EVChargingLocation: NativeBase
```

``` highlight
extension EVChargingLocation: Hashable
```

</div>

</div>

An electric vehicle (EV) charging location.

The semantics generally follow the OCPI 2.2.1 standard.

Known EV-specific acronyms:

- EV: Electric Vehicle
- OCPI: Open Charge Point Interface (a standard with a rather wide adoption worldwide, <https://evroaming.org/>)
- CPO: Charge Point Operator (company that runs the EV charging location)
- eMSP: e-Mobility Service Provider (customer-facing company)
- EVSE: Electric Vehicle Supply Equipment (the actual charger that can charge one car at a time)

A charging location includes a collection of one or more EV supply equipment (EVSE) instances. Typically, the charging location is the exact location of the group of EVSEs, simplified to a single point, but it can also be the entrance of a parking structure which contains these EVSEs. Each EVSE supports more precise position, where applicable.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC2idSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-id" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC2idSSvp" class="token"><code>id</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A unique identifier of the charging location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC4nameSSSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-name" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC4nameSSSgvp" class="token"><code>name</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Display name of the charging location, if available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var name: String? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC5cpoIDSSSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-cpoID" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC5cpoIDSSSgvp" class="token"><code>cpoID</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  CPO’s own ID for the location. This ID may be relevant for some clients to map the charging location data to their own or 3rd party systems. Available only if `EVChargingLocationFeature.LOCATION_INFO` is included in `EVSearchOptions.additional_features`, otherwise `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cpoID: String? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC18evChargingOperatorAA0bF0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-evChargingOperator" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC18evChargingOperatorAA0bF0VSgvp" class="token"><code>evChargingOperator</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Operator of the charging point, if available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var evChargingOperator: EVChargingOperator? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-evchargingoperator">EVChargingOperator</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC21evChargingSubOperatorAA0bG0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-evChargingSubOperator" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC21evChargingSubOperatorAA0bG0VSgvp" class="token"><code>evChargingSubOperator</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Suboperator of the charging point, if available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var evChargingSubOperator: EVChargingOperator? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-evchargingoperator">EVChargingOperator</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC25eMobilityServiceProvidersSayAA0B8OperatorVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-eMobilityServiceProviders" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC25eMobilityServiceProvidersSayAA0B8OperatorVGvp" class="token"><code>eMobilityServiceProviders</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  eMSPs with a roaming agreement enabling access to the EV charging location. Available only if `EVChargingLocationFeature.EMSPS` is included in `EVSearchOptions.additional_features`, otherwise empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var eMobilityServiceProviders: [EVChargingOperator] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-evchargingoperator">EVChargingOperator</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC13facilityTypesSayAA12FacilityTypeOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-facilityTypes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC13facilityTypesSayAA12FacilityTypeOGvp" class="token"><code>facilityTypes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Facilities available at the charging location, for example hotel, wifi, parking lot etc. Available only if `EVChargingLocationFeature.NEARBY` is included in `EVSearchOptions.additional_features`, otherwise empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var facilityTypes: [FacilityType] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-facilitytype">FacilityType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC11parkingTypeAA07ParkingE0OSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-parkingType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC11parkingTypeAA07ParkingE0OSgvp" class="token"><code>parkingType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The type of parking at the charging location. Available only if `EVChargingLocationFeature.LOCATION_INFO` is included in `EVSearchOptions.additional_features`, otherwise `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var parkingType: ParkingType? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-parkingtype">ParkingType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC9energyMixAA06EnergyE0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-energyMix" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC9energyMixAA06EnergyE0VSgvp" class="token"><code>energyMix</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Details on the energy supplied at the charging location. Available only if `EVChargingLocationFeature.LOCATION_INFO` is included in `EVSearchOptions.additional_features`, otherwise `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var energyMix: EnergyMix? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-energymix">EnergyMix</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC5evsesSayAA8EVSEInfoVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-evses" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC5evsesSayAA8EVSEInfoVGvp" class="token"><code>evses</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of EVSEs at the charging station. Available only if `EVChargingLocationFeature.EVSES` is included in `EVSearchOptions.additional_features`, otherwise empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var evses: [EVSEInfo] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-evseinfo">EVSEInfo</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC7tariffsSayAA0B6TariffVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-tariffs" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC7tariffsSayAA0B6TariffVGvp" class="token"><code>tariffs</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of tariffs or price plans for the connectors of the charging station. Tariffs are typically connector-type specific. Hence, they are always linked with connectors and/or connector groups, by indexes to this list.

  This property is set only when data is available and when `EVSearchOptions.additional_features` include either `EVChargingLocationFeature.EVSES` or `EVChargingLocationFeature.CONNECTOR_GROUPS`.

  By default, the list includes tariffs for ad-hoc charging, per connector type, for EVSEs that accept payment without registering.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tariffs: [EVChargingTariff] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-evchargingtariff">EVChargingTariff</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC15connectorGroupsSayAA0B14ConnectorGroupVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-connectorGroups" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC15connectorGroupsSayAA0B14ConnectorGroupVGvp" class="token"><code>connectorGroups</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Connector groups for the location. Provides an overview of the charging connectors in the location by type and power. Available only if `EVChargingLocationFeature.CONNECTOR_GROUPS` is included in `EVSearchOptions.additional_features`, otherwise empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectorGroups: [EVChargingConnectorGroup] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-evchargingconnectorgroup">EVChargingConnectorGroup</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC17supportedVehiclesSayAA0B15VehicleCategoryOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-supportedVehicles" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC17supportedVehiclesSayAA0B15VehicleCategoryOGvp" class="token"><code>supportedVehicles</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of vehicle categories this charging location can support. For example, the same location can be suitable for charging passenger cars and motorcycles. There may be some further restrictions specified in other attributes, for example the available connector types may not be suitable for all vehicles in the supported category.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var supportedVehicles: [EVChargingVehicleCategory] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-evchargingvehiclecategory">EVChargingVehicleCategory</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC17truckRestrictionsAA0B16TruckRestrictionVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-truckRestrictions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC17truckRestrictionsAA0B16TruckRestrictionVSgvp" class="token"><code>truckRestrictions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Access restrictions for trucks and light commercial vehicles. Restricted, only available to customers having a specific contract with HERE and if requested by including `EVChargingLocationFeature.TRUCK_RESTRICTIONS` in `EVSearchOptions.additional_features`, otherwise `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var truckRestrictions: EVChargingTruckRestriction? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-evchargingtruckrestriction">EVChargingTruckRestriction</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC12openingHoursAA0b7OpeningE0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-openingHours" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC12openingHoursAA0b7OpeningE0VSgvp" class="token"><code>openingHours</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The times when the EVSEs at the charging location can be accessed for charging. Available only if `EVChargingLocationFeature.LOCATION_INFO` is included in `EVSearchOptions.additional_features`, otherwise `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var openingHours: EVChargingOpeningHours? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-evchargingopeninghours">EVChargingOpeningHours</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC12restrictionsSayAA25EVAccessRestrictionReasonOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-restrictions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC12restrictionsSayAA25EVAccessRestrictionReasonOGvp" class="token"><code>restrictions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Reason(s) for restricted access.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var restrictions: [EVAccessRestrictionReason] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-evaccessrestrictionreason">EVAccessRestrictionReason</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC18supportPhoneNumberSSSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-supportPhoneNumber" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC18supportPhoneNumberSSSgvp" class="token"><code>supportPhoneNumber</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The phone number that EV drivers should call when need assistance at the charge location, in E.164 format. Available only if `EVChargingLocationFeature.LOCATION_INFO` is included in `EVSearchOptions.additional_features`, otherwise `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var supportPhoneNumber: String? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC8timeZoneSSSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-timeZone" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC8timeZoneSSSgvp" class="token"><code>timeZone</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time zone of the charging location. Based on IANA tzdata’s TZ-values. Available only if `EVChargingLocationFeature.LOCATION_INFO` is included in `EVSearchOptions.additional_features`, otherwise `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timeZone: String? { get }
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


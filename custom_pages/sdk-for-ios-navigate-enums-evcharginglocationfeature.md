---
title: "EVChargingLocationFeature Enumeration Reference"
slug: "sdk-for-ios-navigate-enums-evcharginglocationfeature"
---

# EVChargingLocationFeature

<div class="declaration">

<div class="language">

``` highlight
public enum EVChargingLocationFeature : UInt32, CaseIterable, Codable
```

</div>

</div>

Optional features that can be requested for EV charging locations. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO5evsesyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-evses" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evcharginglocationfeature#sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO5evsesyA2CmF" class="token"><code>evses</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC5evsesSayAA8EVSEInfoVGvp">`EVChargingLocation.evses`</a> will be returned. If <a href="sdk-for-ios-navigate-enums-evcharginglocationfeature#sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO15connectorGroupsyA2CmF">`EVChargingLocationFeature.connectorGroups`</a> is also included, then <a href="sdk-for-ios-navigate-structs-evchargingconnectorgroup#sdk-for-ios-navigate-s-7heresdk24EVChargingConnectorGroupV10connectorsSayAA0bC9ReferenceVGvp">`EVChargingConnectorGroup.connectors`</a> will also be returned.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case evses
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO17truckRestrictionsyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-truckRestrictions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evcharginglocationfeature#sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO17truckRestrictionsyA2CmF" class="token"><code>truckRestrictions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC17truckRestrictionsAA0B16TruckRestrictionVSgvp">`EVChargingLocation.truckRestrictions`</a> will be returned.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case truckRestrictions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO12locationInfoyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-locationInfo" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evcharginglocationfeature#sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO12locationInfoyA2CmF" class="token"><code>locationInfo</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC5cpoIDSSSgvp">`EVChargingLocation.cpoID`</a>, <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC13facilityTypesSayAA12FacilityTypeOGvp">`EVChargingLocation.facilityTypes`</a>, <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC11parkingTypeAA07ParkingE0OSgvp">`EVChargingLocation.parkingType`</a>, <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC9energyMixAA06EnergyE0VSgvp">`EVChargingLocation.energyMix`</a>, and <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC12openingHoursAA0b7OpeningE0VSgvp">`EVChargingLocation.openingHours`</a> will be returned.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case locationInfo
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO5emspsyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-emsps" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evcharginglocationfeature#sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO5emspsyA2CmF" class="token"><code>emsps</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC25eMobilityServiceProvidersSayAA0B8OperatorVGvp">`EVChargingLocation.eMobilityServiceProviders`</a> will be returned.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case emsps
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO15connectorGroupsyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-connectorGroups" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evcharginglocationfeature#sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO15connectorGroupsyA2CmF" class="token"><code>connectorGroups</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC15connectorGroupsSayAA0B14ConnectorGroupVGvp">`EVChargingLocation.connectorGroups`</a> will be returned. To ensure <a href="sdk-for-ios-navigate-structs-evchargingconnectorgroup#sdk-for-ios-navigate-s-7heresdk24EVChargingConnectorGroupV10connectorsSayAA0bC9ReferenceVGvp">`EVChargingConnectorGroup.connectors`</a> is available, also include <a href="sdk-for-ios-navigate-enums-evcharginglocationfeature#sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO5evsesyA2CmF">`EVChargingLocationFeature.evses`</a>. To ensure <a href="sdk-for-ios-navigate-structs-evchargingconnectorgroup#sdk-for-ios-navigate-s-7heresdk24EVChargingConnectorGroupV13tariffIndexesSays5Int32VGvp">`EVChargingConnectorGroup.tariffIndexes`</a> is available, also include <a href="sdk-for-ios-navigate-enums-evcharginglocationfeature#sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO7tariffsyA2CmF">`EVChargingLocationFeature.tariffs`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case connectorGroups
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO7tariffsyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-tariffs" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evcharginglocationfeature#sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO7tariffsyA2CmF" class="token"><code>tariffs</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-structs-evchargingconnectorgroup#sdk-for-ios-navigate-s-7heresdk24EVChargingConnectorGroupV13tariffIndexesSays5Int32VGvp">`EVChargingConnectorGroup.tariffIndexes`</a> will be returned. Ignored if neither <a href="sdk-for-ios-navigate-enums-evcharginglocationfeature#sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO5evsesyA2CmF">`EVChargingLocationFeature.evses`</a> nor <a href="sdk-for-ios-navigate-enums-evcharginglocationfeature#sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO15connectorGroupsyA2CmF">`EVChargingLocationFeature.connectorGroups`</a> are included.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case tariffs
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO6nearbyyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-nearby" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evcharginglocationfeature#sdk-for-ios-navigate-s-7heresdk25EVChargingLocationFeatureO6nearbyyA2CmF" class="token"><code>nearby</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-classes-evcharginglocation#sdk-for-ios-navigate-s-7heresdk18EVChargingLocationC13facilityTypesSayAA12FacilityTypeOGvp">`EVChargingLocation.facilityTypes`</a> will be returned.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case nearby
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


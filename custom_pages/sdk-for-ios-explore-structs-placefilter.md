---
title: "PlaceFilter Structure Reference"
slug: "sdk-for-ios-explore-structs-placefilter"
---

# PlaceFilter

<div class="declaration">

<div class="language">

``` highlight
public struct PlaceFilter : Hashable
```

</div>

</div>

The filter options to specify a place. Consists of fuel, truck and EV options.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11PlaceFilterV9fuelTypesSayAA8FuelTypeOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-fuelTypes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-placefilter#sdk-for-ios-explore-s-7heresdk11PlaceFilterV9fuelTypesSayAA8FuelTypeOGvp" class="token"><code>fuelTypes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of <a href="sdk-for-ios-explore-enums-fueltype">`FuelType`</a> elements that should be used to find only the <a href="sdk-for-ios-explore-structs-fuelstation">`FuelStation`</a> search results that support all of them. This filter is available to use with the <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a> and <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license), however <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> supports it only for `searchByText` and `searchByCategory` with allowed fuel types `DIESEL, LPG, BIO_DIESEL, CNG, DIESEL_WITH_ADDITIVES, E10, E85, ETHANOL, ETHANOL_WITH_ADDITIVES, GASOLINE, HYDROGEN, LNG, MIDGRADE, PREMIUM` and `REGULAR`.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var fuelTypes: [FuelType]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-fueltype">FuelType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11PlaceFilterV14truckFuelTypesSayAA05TruckE4TypeOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-truckFuelTypes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-placefilter#sdk-for-ios-explore-s-7heresdk11PlaceFilterV14truckFuelTypesSayAA05TruckE4TypeOGvp" class="token"><code>truckFuelTypes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of <a href="sdk-for-ios-explore-enums-truckfueltype">`TruckFuelType`</a> elements that should be used to find only the <a href="sdk-for-ios-explore-structs-fuelstation">`FuelStation`</a> search results that support all of them. Not supported for `suggestByText` in <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var truckFuelTypes: [TruckFuelType]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-truckfueltype">TruckFuelType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11PlaceFilterV10truckClassAA05TruckE0OSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-truckClass" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-placefilter#sdk-for-ios-explore-s-7heresdk11PlaceFilterV10truckClassAA05TruckE0OSgvp" class="token"><code>truckClass</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Should be used to find only the <a href="sdk-for-ios-explore-structs-fuelstation">`FuelStation`</a> search results with minimum supported <a href="sdk-for-ios-explore-enums-truckclass">`TruckClass`</a>. This filter is only available to use with the <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>. The <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license) does not apply this filter. <a href="sdk-for-ios-explore-enums-truckclass#sdk-for-ios-explore-s-7heresdk10TruckClassO05lightC0yA2CmF">`TruckClass.lightClass`</a> is not accepted in the filter. Otherwise will result in <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO17invalidTruckClassyA2CmF">`SearchError.invalidTruckClass`</a>.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var truckClass: TruckClass?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-truckclass">TruckClass</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11PlaceFilterV2evAC2EvVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-ev" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-placefilter#sdk-for-ios-explore-s-7heresdk11PlaceFilterV2evAC2EvVvp" class="token"><code>ev</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constraints that are applicable on the places of category EV station.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var ev: PlaceFilter.Ev
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-placefilter-ev">Ev</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11PlaceFilterV9fuelTypes09truckFuelE00F5Class2evACSayAA0G4TypeOG_SayAA05TruckgJ0OGAA0kH0OSgAC2EvVtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-fuelTypes-truckFuelTypes-truckClass-ev" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-placefilter#sdk-for-ios-explore-s-7heresdk11PlaceFilterV9fuelTypes09truckFuelE00F5Class2evACSayAA0G4TypeOG_SayAA05TruckgJ0OGAA0kH0OSgAC2EvVtcfc" class="token"><code>init(fuelTypes:</code><wbr></wbr><code>truckFuelTypes:</code><wbr></wbr><code>truckClass:</code><wbr></wbr><code>ev:</code><wbr></wbr><code>)</code></a> 

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

    - fuelTypes: The list of <a href="sdk-for-ios-explore-enums-fueltype">`FuelType`</a> elements that should be used to find only the <a href="sdk-for-ios-explore-structs-fuelstation">`FuelStation`</a> search results that support all of them. This filter is available to use with the <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a> and <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license), however <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> supports it only for `searchByText` and `searchByCategory` with allowed fuel types `DIESEL, LPG, BIO_DIESEL, CNG, DIESEL_WITH_ADDITIVES, E10, E85, ETHANOL, ETHANOL_WITH_ADDITIVES, GASOLINE, HYDROGEN, LNG, MIDGRADE, PREMIUM` and `REGULAR`.

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    - truckFuelTypes: The list of <a href="sdk-for-ios-explore-enums-truckfueltype">`TruckFuelType`</a> elements that should be used to find only the <a href="sdk-for-ios-explore-structs-fuelstation">`FuelStation`</a> search results that support all of them. Not supported for `suggestByText` in <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    - truckClass: Should be used to find only the <a href="sdk-for-ios-explore-structs-fuelstation">`FuelStation`</a> search results with minimum supported <a href="sdk-for-ios-explore-enums-truckclass">`TruckClass`</a>. This filter is only available to use with the <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>. The <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license) does not apply this filter. <a href="sdk-for-ios-explore-enums-truckclass#sdk-for-ios-explore-s-7heresdk10TruckClassO05lightC0yA2CmF">`TruckClass.lightClass`</a> is not accepted in the filter. Otherwise will result in <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO17invalidTruckClassyA2CmF">`SearchError.invalidTruckClass`</a>.

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    - ev: Constraints that are applicable on the places of category EV station.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(fuelTypes: [FuelType] = [], truckFuelTypes: [TruckFuelType] = [], truckClass: TruckClass? = nil, ev: PlaceFilter.Ev = PlaceFilter.Ev())
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-fueltype">FuelType</a>
  - <a href="sdk-for-ios-explore-enums-truckfueltype">TruckFuelType</a>
  - <a href="sdk-for-ios-explore-enums-truckclass">TruckClass</a>
  - <a href="sdk-for-ios-explore-structs-placefilter-ev">Ev</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11PlaceFilterV2EvV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-Ev" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-placefilter#sdk-for-ios-explore-s-7heresdk11PlaceFilterV2EvV" class="token"><code>Ev</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constraints that are applicable on the places of category EV station.

  <a href="sdk-for-ios-explore-structs-placefilter-ev" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Ev : Hashable
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


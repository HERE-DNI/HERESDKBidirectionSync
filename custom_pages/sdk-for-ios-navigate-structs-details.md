---
title: "Details Structure Reference"
slug: "sdk-for-ios-navigate-structs-details"
---

# Details

<div class="declaration">

<div class="language">

``` highlight
public struct Details : Hashable
```

</div>

</div>

Contains details of a specific place, such as contact information, opening hours and assigned categories.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk7DetailsV8contactsSayAA7ContactVGvp"></span>` `<span id="//apple_ref/swift/Property/contacts" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-details#/s:7heresdk7DetailsV8contactsSayAA7ContactVGvp" class="token"><code>contacts</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of contact information of the place.

  **Note:** Not available as part of <a href="sdk-for-ios-navigate-classes-suggestion">`Suggestion`</a> results.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var contacts: [Contact]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7DetailsV12openingHoursSayAA07OpeningD0VGvp"></span>` `<span id="//apple_ref/swift/Property/openingHours" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-details#/s:7heresdk7DetailsV12openingHoursSayAA07OpeningD0VGvp" class="token"><code>openingHours</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of opening hours information of the place.

  **Note:** Not available as part of <a href="sdk-for-ios-navigate-classes-suggestion">`Suggestion`</a> results.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var openingHours: [OpeningHours]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7DetailsV10categoriesSayAA13PlaceCategoryCGvp"></span>` `<span id="//apple_ref/swift/Property/categories" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-details#/s:7heresdk7DetailsV10categoriesSayAA13PlaceCategoryCGvp" class="token"><code>categories</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of categories assigned to this place.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var categories: [PlaceCategory]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7DetailsV6imagesSayAA8WebImageVGvp"></span>` `<span id="//apple_ref/swift/Property/images" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-details#/s:7heresdk7DetailsV6imagesSayAA8WebImageVGvp" class="token"><code>images</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of images associated with the place. The images are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

  **Note:** Not available as part of <a href="sdk-for-ios-navigate-classes-suggestion">`Suggestion`</a> results.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var images: [WebImage]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7DetailsV10editorialsSayAA12WebEditorialVGvp"></span>` `<span id="//apple_ref/swift/Property/editorials" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-details#/s:7heresdk7DetailsV10editorialsSayAA12WebEditorialVGvp" class="token"><code>editorials</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of editorials associated with the place. The editorials are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

  **Note:** Not available as part of <a href="sdk-for-ios-navigate-classes-suggestion">`Suggestion`</a> results.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var editorials: [WebEditorial]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7DetailsV7ratingsSayAA9WebRatingVGvp"></span>` `<span id="//apple_ref/swift/Property/ratings" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-details#/s:7heresdk7DetailsV7ratingsSayAA9WebRatingVGvp" class="token"><code>ratings</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of ratings associated with the place. The ratings are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

  **Note:** Not available as part of <a href="sdk-for-ios-navigate-classes-suggestion">`Suggestion`</a> results.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var ratings: [WebRating]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7DetailsV10referencesSayAA17SupplierReferenceVGvp"></span>` `<span id="//apple_ref/swift/Property/references" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-details#/s:7heresdk7DetailsV10referencesSayAA17SupplierReferenceVGvp" class="token"><code>references</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var references: [SupplierReference]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7DetailsV14evChargingPoolAA010EVChargingE0VSgvp"></span>` `<span id="//apple_ref/swift/Property/evChargingPool" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-details#/s:7heresdk7DetailsV14evChargingPoolAA010EVChargingE0VSgvp" class="token"><code>evChargingPool</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  EV charging pool details. It is available only for a place that is a charging pool for electric vehicles. It is fully supported for offline search, provided that <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">`LayerConfiguration.Feature.ev`</a> is enabled in <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">`SDKOptions.layerConfiguration`</a>.

  For online search, this feature is only available if it is explicitly enabled. To do that, call

      SearchEngine.set_custom_option()

  with arguments: name: “lookup.show” or “discover.show” or “browse.show” value: “ev” To enable this feature for all queries, call
      SearchEngine.set_custom_option()

  for all: “lookup.show”, “discover.show” and “browse.show”. To enable fuel station details or truck amenities, the custom option value can be combined as “ev,truck”, “ev,truck,fuel” etc.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var evChargingPool: EVChargingPool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7DetailsV14truckAmenitiesAA05TruckD0VSgvp"></span>` `<span id="//apple_ref/swift/Property/truckAmenities" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-details#/s:7heresdk7DetailsV14truckAmenitiesAA05TruckD0VSgvp" class="token"><code>truckAmenities</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Additional information that is available only for places that contain truck amenities. It is fully supported for offline search, provided that <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO22truckServiceAttributesyA2EmF">`LayerConfiguration.Feature.truckServiceAttributes`</a> is enabled in <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">`SDKOptions.layerConfiguration`</a>.

  **Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a <a href="sdk-for-ios-navigate-enums-searcherror#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">`SearchError.forbidden`</a> will be propagated.

  For online search, this feature is only available if it is explicitly enabled. To do that, call

      SearchEngine.set_custom_option()

  with arguments: name: “lookup.show” or “discover.show” or “autosuggest.show” or “browse.show” value: “truck” To enable this feature for all queries, call
      SearchEngine.set_custom_option()

  for all: “lookup.show”, “discover.show”, “autosuggest.show” and “browse.show”. To enable both `truck_amenities` and `fuel_station` features, set the value to “fuel,truck”.
  </p>

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var truckAmenities: TruckAmenities?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7DetailsV11fuelStationAA04FuelD0VSgvp"></span>` `<span id="//apple_ref/swift/Property/fuelStation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-details#/s:7heresdk7DetailsV11fuelStationAA04FuelD0VSgvp" class="token"><code>fuelStation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Fuel station details. It is available only if a place is a fuel station and contain fuel data. It is fully supported for offline search, provided that <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO21fuelStationAttributesyA2EmF">`LayerConfiguration.Feature.fuelStationAttributes`</a> is enabled in <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">`SDKOptions.layerConfiguration`</a>.

  **Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a <a href="sdk-for-ios-navigate-enums-searcherror#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">`SearchError.forbidden`</a> will be propagated.

  For online search, this feature is only available if it is explicitly enabled. To do that, call

      SearchEngine.set_custom_option()

  with arguments: name: “lookup.show” or “discover.show” or “autosuggest.show” or “browse.show” value: “fuel” To enable this feature for all queries, call
      SearchEngine.set_custom_option()

  for all: “lookup.show”, “discover.show”, “autosuggest.show” and “browse.show”. To enable both `truck_amenities` and `fuel_station` features, set the value to “fuel,truck”.
  </p>

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var fuelStation: FuelStation?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7DetailsV9foodTypesSayAA13PlaceFoodTypeVGvp"></span>` `<span id="//apple_ref/swift/Property/foodTypes" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-details#/s:7heresdk7DetailsV9foodTypesSayAA13PlaceFoodTypeVGvp" class="token"><code>foodTypes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of food types assigned to this place. Not supported in <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var foodTypes: [PlaceFoodType]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7DetailsV7paymentAA010POIPaymentB0VSgvp"></span>` `<span id="//apple_ref/swift/Property/payment" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-details#/s:7heresdk7DetailsV7paymentAA010POIPaymentB0VSgvp" class="token"><code>payment</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Details about the payment options at the POI. Set to `nil` if the place is not a POI or if payment details are not available. Not supported in <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var payment: POIPaymentDetails?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7DetailsV18evChargingLocationAA010EVChargingE0CSgvp"></span>` `<span id="//apple_ref/swift/Property/evChargingLocation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-details#/s:7heresdk7DetailsV18evChargingLocationAA010EVChargingE0CSgvp" class="token"><code>evChargingLocation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Details about the EV charging station, if this place belongs to the EV charging station category. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var evChargingLocation: EVChargingLocation?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(contacts: openingHours: categories: images: editorials: ratings: references: evChargingPool: truckAmenities: fuelStation: foodTypes: payment: evChargingLocation: )

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

    - contacts: The list of contact information of the place.

    **Note:** Not available as part of <a href="sdk-for-ios-navigate-classes-suggestion">`Suggestion`</a> results.

    - openingHours: The list of opening hours information of the place.

    **Note:** Not available as part of <a href="sdk-for-ios-navigate-classes-suggestion">`Suggestion`</a> results.

    - categories: The list of categories assigned to this place.
    - images: The list of images associated with the place. The images are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of <a href="sdk-for-ios-navigate-classes-suggestion">`Suggestion`</a> results.

    - editorials: The list of editorials associated with the place. The editorials are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of <a href="sdk-for-ios-navigate-classes-suggestion">`Suggestion`</a> results.

    - ratings: The list of ratings associated with the place. The ratings are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of <a href="sdk-for-ios-navigate-classes-suggestion">`Suggestion`</a> results.

    - references: The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.
    - evChargingPool: EV charging pool details. It is available only for a place that is a charging pool for electric vehicles. It is fully supported for offline search, provided that <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">`LayerConfiguration.Feature.ev`</a> is enabled in <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">`SDKOptions.layerConfiguration`</a>.

    For online search, this feature is only available if it is explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: “lookup.show” or “discover.show” or “browse.show” value: “ev” To enable this feature for all queries, call

        SearchEngine.set_custom_option()

    for all: “lookup.show”, “discover.show” and “browse.show”. To enable fuel station details or truck amenities, the custom option value can be combined as “ev,truck”, “ev,truck,fuel” etc.

    </p>

    - truckAmenities: Additional information that is available only for places that contain truck amenities. It is fully supported for offline search, provided that <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO22truckServiceAttributesyA2EmF">`LayerConfiguration.Feature.truckServiceAttributes`</a> is enabled in <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">`SDKOptions.layerConfiguration`</a>.

    **Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a <a href="sdk-for-ios-navigate-enums-searcherror#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">`SearchError.forbidden`</a> will be propagated.

    For online search, this feature is only available if it is explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: “lookup.show” or “discover.show” or “autosuggest.show” or “browse.show” value: “truck” To enable this feature for all queries, call

        SearchEngine.set_custom_option()

    for all: “lookup.show”, “discover.show”, “autosuggest.show” and “browse.show”. To enable both `truck_amenities` and `fuel_station` features, set the value to “fuel,truck”.

    </p>

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    - fuelStation: Fuel station details. It is available only if a place is a fuel station and contain fuel data. It is fully supported for offline search, provided that <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO21fuelStationAttributesyA2EmF">`LayerConfiguration.Feature.fuelStationAttributes`</a> is enabled in <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">`SDKOptions.layerConfiguration`</a>.

    **Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a <a href="sdk-for-ios-navigate-enums-searcherror#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">`SearchError.forbidden`</a> will be propagated.

    For online search, this feature is only available if it is explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: “lookup.show” or “discover.show” or “autosuggest.show” or “browse.show” value: “fuel” To enable this feature for all queries, call

        SearchEngine.set_custom_option()

    for all: “lookup.show”, “discover.show”, “autosuggest.show” and “browse.show”. To enable both `truck_amenities` and `fuel_station` features, set the value to “fuel,truck”.

    </p>

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    - foodTypes: The list of food types assigned to this place. Not supported in <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).
    - payment: Details about the payment options at the POI. Set to `nil` if the place is not a POI or if payment details are not available. Not supported in <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    - evChargingLocation: Details about the EV charging station, if this place belongs to the EV charging station category. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( contacts : [ Contact ], openingHours : [ OpeningHours ], categories : [ PlaceCategory ], images : [ WebImage ], editorials : [ WebEditorial ], ratings : [ WebRating ], references : [ SupplierReference ], evChargingPool : EVChargingPool ? = nil , truckAmenities : TruckAmenities ? = nil , fuelStation : FuelStation ? = nil , foodTypes : [ PlaceFoodType ] = [], payment : POIPaymentDetails ? = nil , evChargingLocation : EVChargingLocation ? = nil )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      getPrimaryCategories()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the list of primary categories assigned to this place.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getPrimaryCategories () -> [ PlaceCategory ]
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  List of categories.

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


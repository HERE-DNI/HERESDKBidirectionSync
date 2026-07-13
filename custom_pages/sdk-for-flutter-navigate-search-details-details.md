---
title: "Details constructor - Details - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-details-details"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/Details-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">Details</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">Details</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-contacts" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-contact-class">Contact</a></span>\></span></span> <span class="parameter-name">contacts</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-openingHours" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-openinghours-class">OpeningHours</a></span>\></span></span> <span class="parameter-name">openingHours</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-categories" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a></span>\></span></span> <span class="parameter-name">categories</span>, </span>
4.  <span id="sdk-for-flutter-navigate-param-images" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-webimage-class">WebImage</a></span>\></span></span> <span class="parameter-name">images</span>, </span>
5.  <span id="sdk-for-flutter-navigate-param-editorials" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-webeditorial-class">WebEditorial</a></span>\></span></span> <span class="parameter-name">editorials</span>, </span>
6.  <span id="sdk-for-flutter-navigate-param-ratings" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-webrating-class">WebRating</a></span>\></span></span> <span class="parameter-name">ratings</span>, </span>
7.  <span id="sdk-for-flutter-navigate-param-references" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-supplierreference-class">SupplierReference</a></span>\></span></span> <span class="parameter-name">references</span>, \<a href="sdk-for-flutter-navigate-search-evchargingpool-class"></span>
8.  <span id="sdk-for-flutter-navigate-param-evChargingPool" class="parameter"><span class="type-annotation">[EVChargingPool</a>?</span> <span class="parameter-name">evChargingPool</span> = <span class="default-value">null</span>, </span>
9.  <span id="sdk-for-flutter-navigate-param-truckAmenities" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-truckamenities-class">TruckAmenities</a>?</span> <span class="parameter-name">truckAmenities</span> = <span class="default-value">null</span>, </span>
10. <span id="sdk-for-flutter-navigate-param-fuelStation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-fuelstation-class">FuelStation</a>?</span> <span class="parameter-name">fuelStation</span> = <span class="default-value">null</span>, </span>
11. <span id="sdk-for-flutter-navigate-param-foodTypes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placefoodtype-class">PlaceFoodType</a></span>\></span></span> <span class="parameter-name">foodTypes</span> = <span class="default-value">const \[\]</span>, </span>
12. <span id="sdk-for-flutter-navigate-param-payment" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-poipaymentdetails-class">POIPaymentDetails</a>?</span> <span class="parameter-name">payment</span> = <span class="default-value">null</span>, </span>
13. <span id="sdk-for-flutter-navigate-param-evChargingLocation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-evcharginglocation-class">EVChargingLocation</a>?</span> <span class="parameter-name">evChargingLocation</span> = <span class="default-value">null</span>, </span>

\])

</div>

<div class="section desc markdown">

Creates a new instance.

- `contacts` The list of contact information of the place.

**Note:** Not available as part of <a href="sdk-for-flutter-navigate-search-suggestion-class">Suggestion</a> results.

- `openingHours` The list of opening hours information of the place.

**Note:** Not available as part of <a href="sdk-for-flutter-navigate-search-suggestion-class">Suggestion</a> results.

- `categories` The list of categories assigned to this place.
- `images` The list of images associated with the place. The images are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

**Note:** Not available as part of <a href="sdk-for-flutter-navigate-search-suggestion-class">Suggestion</a> results.

- `editorials` The list of editorials associated with the place. The editorials are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

**Note:** Not available as part of <a href="sdk-for-flutter-navigate-search-suggestion-class">Suggestion</a> results.

- `ratings` The list of ratings associated with the place. The ratings are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

**Note:** Not available as part of <a href="sdk-for-flutter-navigate-search-suggestion-class">Suggestion</a> results.

- `references` The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.
- `evChargingPool` EV charging pool details. It is available only for a place that is a charging pool for electric vehicles. It is fully supported for offline search, provided that <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.ev</a> is enabled in <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.

For online search, this feature is only available if it is explicitly enabled. To do that, call

    SearchEngine.set_custom_option()

with arguments: name: "lookup.show" or "discover.show" or "browse.show" value: "ev" To enable this feature for all queries, call

    SearchEngine.set_custom_option()

for all: "lookup.show", "discover.show" and "browse.show". To enable fuel station details or truck amenities, the custom option value can be combined as "ev,truck", "ev,truck,fuel" etc.
</p>

- `truckAmenities` Additional information that is available only for places that contain truck amenities. It is fully supported for offline search, provided that <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.truckServiceAttributes</a> is enabled in <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.

**Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a <a href="sdk-for-flutter-navigate-search-searcherror">SearchError.forbidden</a> will be propagated.

For online search, this feature is only available if it is explicitly enabled. To do that, call

    SearchEngine.set_custom_option()

with arguments: name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show" value: "truck" To enable this feature for all queries, call

    SearchEngine.set_custom_option()

for all: "lookup.show", "discover.show", "autosuggest.show" and "browse.show". To enable both `truck_amenities` and `fuel_station` features, set the value to "fuel,truck".
</p>

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `fuelStation` Fuel station details. It is available only if a place is a fuel station and contain fuel data. It is fully supported for offline search, provided that <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.fuelStationAttributes</a> is enabled in <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.

**Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a <a href="sdk-for-flutter-navigate-search-searcherror">SearchError.forbidden</a> will be propagated.

For online search, this feature is only available if it is explicitly enabled. To do that, call

    SearchEngine.set_custom_option()

with arguments: name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show" value: "fuel" To enable this feature for all queries, call

    SearchEngine.set_custom_option()

for all: "lookup.show", "discover.show", "autosuggest.show" and "browse.show". To enable both `truck_amenities` and `fuel_station` features, set the value to "fuel,truck".
</p>

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `foodTypes` The list of food types assigned to this place. Not supported in `OfflineSearchEngine` (only available for the Navigate license).
- `payment` Details about the payment options at the POI. Set to `null` if the place is not a POI or if payment details are not available. Not supported in `OfflineSearchEngine` (only available for the Navigate license).

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `evChargingLocation` Details about the EV charging station, if this place belongs to the EV charging station category. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
Details(List<Contact> contacts, List<OpeningHours> openingHours, List<PlaceCategory> categories, List<WebImage> images, List<WebEditorial> editorials, List<WebRating> ratings, List<SupplierReference> references, [EVChargingPool? evChargingPool = null, TruckAmenities? truckAmenities = null, FuelStation? fuelStation = null, List<PlaceFoodType> foodTypes = const [], POIPaymentDetails? payment = null, EVChargingLocation? evChargingLocation = null])
  : contacts = contacts, openingHours = openingHours, categories = categories, images = images, editorials = editorials, ratings = ratings, references = references, evChargingPool = evChargingPool ?? null, truckAmenities = truckAmenities ?? null, fuelStation = fuelStation ?? null, foodTypes = foodTypes, payment = payment ?? null, evChargingLocation = evChargingLocation;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "Details class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-details-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/Details-class-sidebar.html">

<div>

# <span class="kind-class">Details</span> class

</div>

<div class="section desc markdown">

Contains details of a specific place, such as contact information, opening hours and assigned categories.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-details-details">Details</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-contacts" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-contact-class">Contact</a></span>\></span></span> <span class="parameter-name">contacts</span>, </span><span id="sdk-for-flutter-explore-param-openingHours" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-openinghours-class">OpeningHours</a></span>\></span></span> <span class="parameter-name">openingHours</span>, </span><span id="sdk-for-flutter-explore-param-categories" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-placecategory-class">PlaceCategory</a></span>\></span></span> <span class="parameter-name">categories</span>, </span><span id="sdk-for-flutter-explore-param-images" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-webimage-class">WebImage</a></span>\></span></span> <span class="parameter-name">images</span>, </span><span id="sdk-for-flutter-explore-param-editorials" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-webeditorial-class">WebEditorial</a></span>\></span></span> <span class="parameter-name">editorials</span>, </span><span id="sdk-for-flutter-explore-param-ratings" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-webrating-class">WebRating</a></span>\></span></span> <span class="parameter-name">ratings</span>, </span><span id="sdk-for-flutter-explore-param-references" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-supplierreference-class">SupplierReference</a></span>\></span></span> <span class="parameter-name">references</span>, \<a href="sdk-for-flutter-explore-search-evchargingpool-class"></span><span id="sdk-for-flutter-explore-param-evChargingPool" class="parameter"><span class="type-annotation">[EVChargingPool</a>?</span> <span class="parameter-name">evChargingPool</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-truckAmenities" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-truckamenities-class">TruckAmenities</a>?</span> <span class="parameter-name">truckAmenities</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-fuelStation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-fuelstation-class">FuelStation</a>?</span> <span class="parameter-name">fuelStation</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-foodTypes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-placefoodtype-class">PlaceFoodType</a></span>\></span></span> <span class="parameter-name">foodTypes</span> = <span class="default-value">const \[\]</span>, </span><span id="sdk-for-flutter-explore-param-payment" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-poipaymentdetails-class">POIPaymentDetails</a>?</span> <span class="parameter-name">payment</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-evChargingLocation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-evcharginglocation-class">EVChargingLocation</a>?</span> <span class="parameter-name">evChargingLocation</span> = <span class="default-value">null</span></span>\])</span>  
Creates a new instance.

<span class="name"><a href="sdk-for-flutter-explore-search-details-details-withdefaults">Details.withDefaults</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withDefaults-param-contacts" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-contact-class">Contact</a></span>\></span></span> <span class="parameter-name">contacts</span>, </span><span id="sdk-for-flutter-explore-withDefaults-param-openingHours" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-openinghours-class">OpeningHours</a></span>\></span></span> <span class="parameter-name">openingHours</span>, </span><span id="sdk-for-flutter-explore-withDefaults-param-categories" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-placecategory-class">PlaceCategory</a></span>\></span></span> <span class="parameter-name">categories</span>, </span><span id="sdk-for-flutter-explore-withDefaults-param-images" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-webimage-class">WebImage</a></span>\></span></span> <span class="parameter-name">images</span>, </span><span id="sdk-for-flutter-explore-withDefaults-param-editorials" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-webeditorial-class">WebEditorial</a></span>\></span></span> <span class="parameter-name">editorials</span>, </span><span id="sdk-for-flutter-explore-withDefaults-param-ratings" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-webrating-class">WebRating</a></span>\></span></span> <span class="parameter-name">ratings</span>, </span><span id="sdk-for-flutter-explore-withDefaults-param-references" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-supplierreference-class">SupplierReference</a></span>\></span></span> <span class="parameter-name">references</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-details-categories">categories</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-placecategory-class">PlaceCategory</a></span>\></span></span>  
The list of categories assigned to this place.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-contacts">contacts</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-contact-class">Contact</a></span>\></span></span>  
The list of contact information of the place.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-editorials">editorials</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-webeditorial-class">WebEditorial</a></span>\></span></span>  
The list of editorials associated with the place. The editorials are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-evcharginglocation">evChargingLocation</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-search-evcharginglocation-class">EVChargingLocation</a>?</span>  
Details about the EV charging station, if this place belongs to the EV charging station category. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-evchargingpool">evChargingPool</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-search-evchargingpool-class">EVChargingPool</a>?</span>  
EV charging pool details. It is available only for a place that is a charging pool for electric vehicles. It is fully supported for offline search, provided that <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.ev</a> is enabled in <a href="sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-foodtypes">foodTypes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-placefoodtype-class">PlaceFoodType</a></span>\></span></span>  
The list of food types assigned to this place. Not supported in `OfflineSearchEngine` (only available for the Navigate license).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-fuelstation">fuelStation</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-search-fuelstation-class">FuelStation</a>?</span>  
Fuel station details. It is available only if a place is a fuel station and contain fuel data. It is fully supported for offline search, provided that <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.fuelStationAttributes</a> is enabled in <a href="sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-images">images</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-webimage-class">WebImage</a></span>\></span></span>  
The list of images associated with the place. The images are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-openinghours">openingHours</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-openinghours-class">OpeningHours</a></span>\></span></span>  
The list of opening hours information of the place.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-payment">payment</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-search-poipaymentdetails-class">POIPaymentDetails</a>?</span>  
Details about the payment options at the POI. Set to `null` if the place is not a POI or if payment details are not available. Not supported in `OfflineSearchEngine` (only available for the Navigate license).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-ratings">ratings</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-webrating-class">WebRating</a></span>\></span></span>  
The list of ratings associated with the place. The ratings are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-references">references</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-supplierreference-class">SupplierReference</a></span>\></span></span>  
The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-truckamenities">truckAmenities</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-search-truckamenities-class">TruckAmenities</a>?</span>  
Additional information that is available only for places that contain truck amenities. It is fully supported for offline search, provided that <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.truckServiceAttributes</a> is enabled in <a href="sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-details-getprimarycategories">getPrimaryCategories</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-placecategory-class">PlaceCategory</a></span>\></span></span> </span>  
Gets the list of primary categories assigned to this place.

<span class="name"><a href="sdk-for-flutter-explore-search-details-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-details-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-details-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


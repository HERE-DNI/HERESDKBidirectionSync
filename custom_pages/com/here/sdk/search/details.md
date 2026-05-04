---
title: "Details (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestdetails"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Details

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.Details
------------------------------------------------------------------------
public final class Details extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains details of a specific place, such as contact information, opening hours and assigned categories.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`>`

  [categories](#categories)

The list of categories assigned to this place.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Contact`](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")`>`

  [contacts](#contacts)

The list of contact information of the place.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebEditorial`](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")`>`

  [editorials](#editorials)

The list of editorials associated with the place.

[`EVChargingPool`](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search")

  [evChargingPool](#evChargingPool)

EV charging pool details.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceFoodType`](sdk-for-android-explore-api-reference-latestplacefoodtype "class in com.here.sdk.search")`>`

  [foodTypes](#foodTypes)

The list of food types assigned to this place.

[`FuelStation`](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search")

  [fuelStation](#fuelStation)

Fuel station details.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebImage`](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")`>`

  [images](#images)

The list of images associated with the place.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`OpeningHours`](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")`>`

  [openingHours](#openingHours)

The list of opening hours information of the place.

[`POIPaymentDetails`](sdk-for-android-explore-api-reference-latestpoipaymentdetails "class in com.here.sdk.search")

  [payment](#payment)

Details about the payment options at the POI.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebRating`](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")`>`

  [ratings](#ratings)

The list of ratings associated with the place.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`SupplierReference`](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")`>`

  [references](#references)

The list of supplier references to this place.

[`TruckAmenities`](sdk-for-android-explore-api-reference-latesttruckamenities "class in com.here.sdk.search")

  [truckAmenities](#truckAmenities)

Additional information that is available only for places that contain truck amenities.

## Constructor Summary

Constructors

Constructor

  Description

  [Details](#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Contact`](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")`> contacts, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`OpeningHours`](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")`> openingHours, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`> categories, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebImage`](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")`> images, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebEditorial`](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")`> editorials, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebRating`](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")`> ratings, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`SupplierReference`](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")`> references)`

Creates a new instance.

[Details](#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Contact`](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")`> contacts, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`OpeningHours`](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")`> openingHours, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`> categories, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebImage`](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")`> images, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebEditorial`](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")`> editorials, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebRating`](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")`> ratings, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`SupplierReference`](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")`> references, `[`EVChargingPool`](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search")` evChargingPool)`

Creates a new instance.

[Details](#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Contact`](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")`> contacts, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`OpeningHours`](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")`> openingHours, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`> categories, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebImage`](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")`> images, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebEditorial`](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")`> editorials, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebRating`](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")`> ratings, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`SupplierReference`](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")`> references, `[`EVChargingPool`](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search")` evChargingPool, `[`TruckAmenities`](sdk-for-android-explore-api-reference-latesttruckamenities "class in com.here.sdk.search")` truckAmenities)`

Creates a new instance.

[Details](#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Contact`](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")`> contacts, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`OpeningHours`](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")`> openingHours, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`> categories, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebImage`](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")`> images, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebEditorial`](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")`> editorials, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebRating`](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")`> ratings, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`SupplierReference`](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")`> references, `[`EVChargingPool`](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search")` evChargingPool, `[`TruckAmenities`](sdk-for-android-explore-api-reference-latesttruckamenities "class in com.here.sdk.search")` truckAmenities, `[`FuelStation`](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search")` fuelStation)`

Creates a new instance.

[Details](#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Contact`](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")`> contacts, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`OpeningHours`](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")`> openingHours, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`> categories, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebImage`](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")`> images, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebEditorial`](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")`> editorials, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebRating`](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")`> ratings, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`SupplierReference`](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")`> references, `[`EVChargingPool`](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search")` evChargingPool, `[`TruckAmenities`](sdk-for-android-explore-api-reference-latesttruckamenities "class in com.here.sdk.search")` truckAmenities, `[`FuelStation`](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search")` fuelStation, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceFoodType`](sdk-for-android-explore-api-reference-latestplacefoodtype "class in com.here.sdk.search")`> foodTypes)`

Creates a new instance.

[Details](#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List,com.here.sdk.search.POIPaymentDetails))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Contact`](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")`> contacts, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`OpeningHours`](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")`> openingHours, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`> categories, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebImage`](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")`> images, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebEditorial`](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")`> editorials, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebRating`](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")`> ratings, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`SupplierReference`](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")`> references, `[`EVChargingPool`](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search")` evChargingPool, `[`TruckAmenities`](sdk-for-android-explore-api-reference-latesttruckamenities "class in com.here.sdk.search")` truckAmenities, `[`FuelStation`](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search")` fuelStation, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceFoodType`](sdk-for-android-explore-api-reference-latestplacefoodtype "class in com.here.sdk.search")`> foodTypes, `[`POIPaymentDetails`](sdk-for-android-explore-api-reference-latestpoipaymentdetails "class in com.here.sdk.search")` payment)`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`>`

  [getPrimaryCategories](#getPrimaryCategories())`()`

Gets the list of primary categories assigned to this place.

`int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### contacts

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Contact](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")\> contacts

    The list of contact information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

### openingHours

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[OpeningHours](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")\> openingHours

    The list of opening hours information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

### categories

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories

    The list of categories assigned to this place.

### images

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebImage](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")\> images

    The list of images associated with the place. The images are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

### editorials

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebEditorial](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")\> editorials

    The list of editorials associated with the place. The editorials are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

### ratings

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebRating](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")\> ratings

    The list of ratings associated with the place. The ratings are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

### references

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[SupplierReference](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")\> references

    The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

### evChargingPool

@Nullable public [EVChargingPool](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search") evChargingPool

    EV charging pool details. It is available only for a place that is a charging pool for electric vehicles. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "browse.show" value: "ev" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show" and "browse.show". To enable fuel station details or truck amenities, the custom option value can be combined as "ev,truck", "ev,truck,fuel" etc.

### truckAmenities

@Nullable public [TruckAmenities](sdk-for-android-explore-api-reference-latesttruckamenities "class in com.here.sdk.search") truckAmenities

    Additional information that is available only for places that contain truck amenities. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    **Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a [`SearchError.FORBIDDEN`](sdk-for-android-explore-api-reference-latestsearcherror#FORBIDDEN) will be propagated.

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show" value: "truck" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show", "autosuggest.show" and "browse.show". To enable both `truck_amenities` and `fuel_station` features, set the value to "fuel,truck".

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### fuelStation

@Nullable public [FuelStation](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search") fuelStation

    Fuel station details. It is available only if a place is a fuel station and contain fuel data. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#FUEL_STATION_ATTRIBUTES) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    **Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a [`SearchError.FORBIDDEN`](sdk-for-android-explore-api-reference-latestsearcherror#FORBIDDEN) will be propagated.

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show" value: "fuel" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show", "autosuggest.show" and "browse.show". To enable both `truck_amenities` and `fuel_station` features, set the value to "fuel,truck".

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### foodTypes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceFoodType](sdk-for-android-explore-api-reference-latestplacefoodtype "class in com.here.sdk.search")\> foodTypes

    The list of food types assigned to this place. Not supported in `OfflineSearchEngine` (only available for the Navigate license).

### payment

@Nullable public [POIPaymentDetails](sdk-for-android-explore-api-reference-latestpoipaymentdetails "class in com.here.sdk.search") payment

    Details about the payment options at the POI. Set to `null` if the place is not a POI or if payment details are not available. Not supported in `OfflineSearchEngine` (only available for the Navigate license).

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Constructor Details

  - (java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List)" class="section detail">

### Details

public Details(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Contact](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")\> contacts, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[OpeningHours](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")\> openingHours, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebImage](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")\> images, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebEditorial](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")\> editorials, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebRating](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")\> ratings, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[SupplierReference](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")\> references)

    Creates a new instance.
Parameters:
    `contacts` -

    The list of contact information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `openingHours` -

    The list of opening hours information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `categories` -

    The list of categories assigned to this place.

    `images` -

    The list of images associated with the place. The images are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `editorials` -

    The list of editorials associated with the place. The editorials are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `ratings` -

    The list of ratings associated with the place. The ratings are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `references` -

    The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.
- (java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool)" class="section detail">

### Details

public Details(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Contact](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")\> contacts, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[OpeningHours](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")\> openingHours, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebImage](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")\> images, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebEditorial](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")\> editorials, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebRating](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")\> ratings, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[SupplierReference](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")\> references, @Nullable [EVChargingPool](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search") evChargingPool)

    Creates a new instance.
Parameters:
    `contacts` -

    The list of contact information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `openingHours` -

    The list of opening hours information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `categories` -

    The list of categories assigned to this place.

    `images` -

    The list of images associated with the place. The images are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `editorials` -

    The list of editorials associated with the place. The editorials are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `ratings` -

    The list of ratings associated with the place. The ratings are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `references` -

    The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    `evChargingPool` -

    EV charging pool details. It is available only for a place that is a charging pool for electric vehicles. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "browse.show" value: "ev" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show" and "browse.show". To enable fuel station details or truck amenities, the custom option value can be combined as "ev,truck", "ev,truck,fuel" etc.
- (java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities)" class="section detail">

### Details

public Details(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Contact](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")\> contacts, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[OpeningHours](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")\> openingHours, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebImage](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")\> images, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebEditorial](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")\> editorials, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebRating](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")\> ratings, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[SupplierReference](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")\> references, @Nullable [EVChargingPool](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search") evChargingPool, @Nullable [TruckAmenities](sdk-for-android-explore-api-reference-latesttruckamenities "class in com.here.sdk.search") truckAmenities)

    Creates a new instance.
Parameters:
    `contacts` -

    The list of contact information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `openingHours` -

    The list of opening hours information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `categories` -

    The list of categories assigned to this place.

    `images` -

    The list of images associated with the place. The images are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `editorials` -

    The list of editorials associated with the place. The editorials are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `ratings` -

    The list of ratings associated with the place. The ratings are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `references` -

    The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    `evChargingPool` -

    EV charging pool details. It is available only for a place that is a charging pool for electric vehicles. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "browse.show" value: "ev" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show" and "browse.show". To enable fuel station details or truck amenities, the custom option value can be combined as "ev,truck", "ev,truck,fuel" etc.

    `truckAmenities` -

    Additional information that is available only for places that contain truck amenities. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    **Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a [`SearchError.FORBIDDEN`](sdk-for-android-explore-api-reference-latestsearcherror#FORBIDDEN) will be propagated.

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show" value: "truck" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show", "autosuggest.show" and "browse.show". To enable both `truck_amenities` and `fuel_station` features, set the value to "fuel,truck".

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
- (java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation)" class="section detail">

### Details

public Details(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Contact](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")\> contacts, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[OpeningHours](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")\> openingHours, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebImage](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")\> images, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebEditorial](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")\> editorials, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebRating](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")\> ratings, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[SupplierReference](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")\> references, @Nullable [EVChargingPool](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search") evChargingPool, @Nullable [TruckAmenities](sdk-for-android-explore-api-reference-latesttruckamenities "class in com.here.sdk.search") truckAmenities, @Nullable [FuelStation](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search") fuelStation)

    Creates a new instance.
Parameters:
    `contacts` -

    The list of contact information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `openingHours` -

    The list of opening hours information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `categories` -

    The list of categories assigned to this place.

    `images` -

    The list of images associated with the place. The images are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `editorials` -

    The list of editorials associated with the place. The editorials are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `ratings` -

    The list of ratings associated with the place. The ratings are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `references` -

    The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    `evChargingPool` -

    EV charging pool details. It is available only for a place that is a charging pool for electric vehicles. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "browse.show" value: "ev" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show" and "browse.show". To enable fuel station details or truck amenities, the custom option value can be combined as "ev,truck", "ev,truck,fuel" etc.

    `truckAmenities` -

    Additional information that is available only for places that contain truck amenities. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    **Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a [`SearchError.FORBIDDEN`](sdk-for-android-explore-api-reference-latestsearcherror#FORBIDDEN) will be propagated.

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show" value: "truck" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show", "autosuggest.show" and "browse.show". To enable both `truck_amenities` and `fuel_station` features, set the value to "fuel,truck".

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    `fuelStation` -

    Fuel station details. It is available only if a place is a fuel station and contain fuel data. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#FUEL_STATION_ATTRIBUTES) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    **Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a [`SearchError.FORBIDDEN`](sdk-for-android-explore-api-reference-latestsearcherror#FORBIDDEN) will be propagated.

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show" value: "fuel" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show", "autosuggest.show" and "browse.show". To enable both `truck_amenities` and `fuel_station` features, set the value to "fuel,truck".

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
- (java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List)" class="section detail">

### Details

public Details(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Contact](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")\> contacts, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[OpeningHours](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")\> openingHours, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebImage](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")\> images, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebEditorial](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")\> editorials, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebRating](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")\> ratings, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[SupplierReference](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")\> references, @Nullable [EVChargingPool](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search") evChargingPool, @Nullable [TruckAmenities](sdk-for-android-explore-api-reference-latesttruckamenities "class in com.here.sdk.search") truckAmenities, @Nullable [FuelStation](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search") fuelStation, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceFoodType](sdk-for-android-explore-api-reference-latestplacefoodtype "class in com.here.sdk.search")\> foodTypes)

    Creates a new instance.
Parameters:
    `contacts` -

    The list of contact information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `openingHours` -

    The list of opening hours information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `categories` -

    The list of categories assigned to this place.

    `images` -

    The list of images associated with the place. The images are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `editorials` -

    The list of editorials associated with the place. The editorials are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `ratings` -

    The list of ratings associated with the place. The ratings are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `references` -

    The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    `evChargingPool` -

    EV charging pool details. It is available only for a place that is a charging pool for electric vehicles. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "browse.show" value: "ev" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show" and "browse.show". To enable fuel station details or truck amenities, the custom option value can be combined as "ev,truck", "ev,truck,fuel" etc.

    `truckAmenities` -

    Additional information that is available only for places that contain truck amenities. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    **Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a [`SearchError.FORBIDDEN`](sdk-for-android-explore-api-reference-latestsearcherror#FORBIDDEN) will be propagated.

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show" value: "truck" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show", "autosuggest.show" and "browse.show". To enable both `truck_amenities` and `fuel_station` features, set the value to "fuel,truck".

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    `fuelStation` -

    Fuel station details. It is available only if a place is a fuel station and contain fuel data. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#FUEL_STATION_ATTRIBUTES) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    **Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a [`SearchError.FORBIDDEN`](sdk-for-android-explore-api-reference-latestsearcherror#FORBIDDEN) will be propagated.

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show" value: "fuel" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show", "autosuggest.show" and "browse.show". To enable both `truck_amenities` and `fuel_station` features, set the value to "fuel,truck".

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    `foodTypes` -

    The list of food types assigned to this place. Not supported in `OfflineSearchEngine` (only available for the Navigate license).
- (java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List,com.here.sdk.search.POIPaymentDetails)" class="section detail">

### Details

public Details(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Contact](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")\> contacts, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[OpeningHours](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")\> openingHours, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebImage](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")\> images, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebEditorial](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")\> editorials, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebRating](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")\> ratings, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[SupplierReference](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")\> references, @Nullable [EVChargingPool](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search") evChargingPool, @Nullable [TruckAmenities](sdk-for-android-explore-api-reference-latesttruckamenities "class in com.here.sdk.search") truckAmenities, @Nullable [FuelStation](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search") fuelStation, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceFoodType](sdk-for-android-explore-api-reference-latestplacefoodtype "class in com.here.sdk.search")\> foodTypes, @Nullable [POIPaymentDetails](sdk-for-android-explore-api-reference-latestpoipaymentdetails "class in com.here.sdk.search") payment)

    Creates a new instance.
Parameters:
    `contacts` -

    The list of contact information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `openingHours` -

    The list of opening hours information of the place.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `categories` -

    The list of categories assigned to this place.

    `images` -

    The list of images associated with the place. The images are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `editorials` -

    The list of editorials associated with the place. The editorials are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `ratings` -

    The list of ratings associated with the place. The ratings are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    **Note:** Not available as part of [`Suggestion`](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search") results.

    `references` -

    The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    `evChargingPool` -

    EV charging pool details. It is available only for a place that is a charging pool for electric vehicles. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "browse.show" value: "ev" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show" and "browse.show". To enable fuel station details or truck amenities, the custom option value can be combined as "ev,truck", "ev,truck,fuel" etc.

    `truckAmenities` -

    Additional information that is available only for places that contain truck amenities. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    **Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a [`SearchError.FORBIDDEN`](sdk-for-android-explore-api-reference-latestsearcherror#FORBIDDEN) will be propagated.

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show" value: "truck" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show", "autosuggest.show" and "browse.show". To enable both `truck_amenities` and `fuel_station` features, set the value to "fuel,truck".

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    `fuelStation` -

    Fuel station details. It is available only if a place is a fuel station and contain fuel data. It is fully supported for offline search, provided that [`LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#FUEL_STATION_ATTRIBUTES) is enabled in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

    **Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a [`SearchError.FORBIDDEN`](sdk-for-android-explore-api-reference-latestsearcherror#FORBIDDEN) will be propagated.

    For online search, this feature is only available if it is explicitly enabled. To do that, call `SearchEngine.set_custom_option()` with arguments: name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show" value: "fuel" To enable this feature for all queries, call `SearchEngine.set_custom_option()` for all: "lookup.show", "discover.show", "autosuggest.show" and "browse.show". To enable both `truck_amenities` and `fuel_station` features, set the value to "fuel,truck".

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    `foodTypes` -

    The list of food types assigned to this place. Not supported in `OfflineSearchEngine` (only available for the Navigate license).

    `payment` -

    Details about the payment options at the POI. Set to `null` if the place is not a POI or if payment details are not available. Not supported in `OfflineSearchEngine` (only available for the Navigate license).

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### getPrimaryCategories

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> getPrimaryCategories()

    Gets the list of primary categories assigned to this place.
Returns:
    List of categories.

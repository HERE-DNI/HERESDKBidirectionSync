---
title: "Details (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-details"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.search.Details

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Details</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Contains details of a specific place, such as contact information,
opening hours and assigned categories.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`PlaceCategory`](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-details#categories"
  class="member-name-link"><code>categories</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The list of categories assigned to this place.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`Contact`](sdk-for-android-explore-com-here-sdk-search-contact "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-details#contacts"
  class="member-name-link"><code>contacts</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The list of contact information of the place.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`WebEditorial`](sdk-for-android-explore-com-here-sdk-search-webeditorial "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-details#editorials"
  class="member-name-link"><code>editorials</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The list of editorials associated with the place.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`EVChargingLocation`](sdk-for-android-explore-com-here-sdk-search-evcharginglocation "class in com.here.sdk.search")

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-details#evChargingLocation"
  class="member-name-link"><code>evChargingLocation</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Details about the EV charging station, if this place belongs to the EV
  charging station category.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`EVChargingPool`](sdk-for-android-explore-com-here-sdk-search-evchargingpool "class in com.here.sdk.search")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-details#evChargingPool"
  class="member-name-link"><code>evChargingPool</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  EV charging pool details.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`PlaceFoodType`](sdk-for-android-explore-com-here-sdk-search-placefoodtype "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-details#foodTypes"
  class="member-name-link"><code>foodTypes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The list of food types assigned to this place.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`FuelStation`](sdk-for-android-explore-com-here-sdk-search-fuelstation "class in com.here.sdk.search")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-details#fuelStation"
  class="member-name-link"><code>fuelStation</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Fuel station details.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`WebImage`](sdk-for-android-explore-com-here-sdk-search-webimage "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-details#images"
  class="member-name-link"><code>images</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The list of images associated with the place.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`OpeningHours`](sdk-for-android-explore-com-here-sdk-search-openinghours "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-details#openingHours"
  class="member-name-link"><code>openingHours</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The list of opening hours information of the place.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`POIPaymentDetails`](sdk-for-android-explore-com-here-sdk-search-poipaymentdetails "class in com.here.sdk.search")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-details#payment"
  class="member-name-link"><code>payment</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Details about the payment options at the POI.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`WebRating`](sdk-for-android-explore-com-here-sdk-search-webrating "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-details#ratings"
  class="member-name-link"><code>ratings</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The list of ratings associated with the place.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`SupplierReference`](sdk-for-android-explore-com-here-sdk-search-supplierreference "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-details#references"
  class="member-name-link"><code>references</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The list of supplier references to this place.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`TruckAmenities`](sdk-for-android-explore-com-here-sdk-search-truckamenities "class in com.here.sdk.search")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-details#truckAmenities"
  class="member-name-link"><code>truckAmenities</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Additional information that is available only for places that contain
  truck amenities.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      Details(List<Contact> contacts,
       List<OpeningHours> openingHours,
       List<PlaceCategory> categories,
       List<WebImage> images,
       List<WebEditorial> editorials,
       List<WebRating> ratings,
       List<SupplierReference> references)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      Details(List<Contact> contacts,
       List<OpeningHours> openingHours,
       List<PlaceCategory> categories,
       List<WebImage> images,
       List<WebEditorial> editorials,
       List<WebRating> ratings,
       List<SupplierReference> references,
       EVChargingPool evChargingPool)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      Details(List<Contact> contacts,
       List<OpeningHours> openingHours,
       List<PlaceCategory> categories,
       List<WebImage> images,
       List<WebEditorial> editorials,
       List<WebRating> ratings,
       List<SupplierReference> references,
       EVChargingPool evChargingPool,
       TruckAmenities truckAmenities)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      Details(List<Contact> contacts,
       List<OpeningHours> openingHours,
       List<PlaceCategory> categories,
       List<WebImage> images,
       List<WebEditorial> editorials,
       List<WebRating> ratings,
       List<SupplierReference> references,
       EVChargingPool evChargingPool,
       TruckAmenities truckAmenities,
       FuelStation fuelStation)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      Details(List<Contact> contacts,
       List<OpeningHours> openingHours,
       List<PlaceCategory> categories,
       List<WebImage> images,
       List<WebEditorial> editorials,
       List<WebRating> ratings,
       List<SupplierReference> references,
       EVChargingPool evChargingPool,
       TruckAmenities truckAmenities,
       FuelStation fuelStation,
       List<PlaceFoodType> foodTypes)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      Details(List<Contact> contacts,
       List<OpeningHours> openingHours,
       List<PlaceCategory> categories,
       List<WebImage> images,
       List<WebEditorial> editorials,
       List<WebRating> ratings,
       List<SupplierReference> references,
       EVChargingPool evChargingPool,
       TruckAmenities truckAmenities,
       FuelStation fuelStation,
       List<PlaceFoodType> foodTypes,
       POIPaymentDetails payment)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      Details(List<Contact> contacts,
       List<OpeningHours> openingHours,
       List<PlaceCategory> categories,
       List<WebImage> images,
       List<WebEditorial> editorials,
       List<WebRating> ratings,
       List<SupplierReference> references,
       EVChargingPool evChargingPool,
       TruckAmenities truckAmenities,
       FuelStation fuelStation,
       List<PlaceFoodType> foodTypes,
       POIPaymentDetails payment,
       EVChargingLocation evChargingLocation)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals(Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`PlaceCategory`](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPrimaryCategories()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of primary categories assigned to this place.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-contacts" class="section detail">

    ### contacts

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[Contact](sdk-for-android-explore-com-here-sdk-search-contact "class in com.here.sdk.search")></span> <span class="element-name">contacts</span>

    </div>

    <div class="block">

    The list of contact information of the place. Note: Not available as
    part of Suggestion results.

    </div>

    </div>

  - <div id="sdk-for-android-explore-openingHours"
    class="section detail">

    ### openingHours

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[OpeningHours](sdk-for-android-explore-com-here-sdk-search-openinghours "class in com.here.sdk.search")></span> <span class="element-name">openingHours</span>

    </div>

    <div class="block">

    The list of opening hours information of the place. Note: Not
    available as part of Suggestion results.

    </div>

    </div>

  - <div id="sdk-for-android-explore-categories" class="section detail">

    ### categories

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")></span> <span class="element-name">categories</span>

    </div>

    <div class="block">

    The list of categories assigned to this place.

    </div>

    </div>

  - <div id="sdk-for-android-explore-images" class="section detail">

    ### images

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebImage](sdk-for-android-explore-com-here-sdk-search-webimage "class in com.here.sdk.search")></span> <span class="element-name">images</span>

    </div>

    <div class="block">

    The list of images associated with the place. The images are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. Note: Not available as part of
    Suggestion results.

    </div>

    </div>

  - <div id="sdk-for-android-explore-editorials" class="section detail">

    ### editorials

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebEditorial](sdk-for-android-explore-com-here-sdk-search-webeditorial "class in com.here.sdk.search")></span> <span class="element-name">editorials</span>

    </div>

    <div class="block">

    The list of editorials associated with the place. The editorials are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. Note: Not available as part of
    Suggestion results.

    </div>

    </div>

  - <div id="sdk-for-android-explore-ratings" class="section detail">

    ### ratings

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebRating](sdk-for-android-explore-com-here-sdk-search-webrating "class in com.here.sdk.search")></span> <span class="element-name">ratings</span>

    </div>

    <div class="block">

    The list of ratings associated with the place. The ratings are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. Note: Not available as part of
    Suggestion results.

    </div>

    </div>

  - <div id="sdk-for-android-explore-references" class="section detail">

    ### references

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[SupplierReference](sdk-for-android-explore-com-here-sdk-search-supplierreference "class in com.here.sdk.search")></span> <span class="element-name">references</span>

    </div>

    <div class="block">

    The list of supplier references to this place. The references are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty.

    </div>

    </div>

  - <div id="sdk-for-android-explore-evChargingPool"
    class="section detail">

    ### evChargingPool

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[EVChargingPool](sdk-for-android-explore-com-here-sdk-search-evchargingpool "class in com.here.sdk.search")</span> <span class="element-name">evChargingPool</span>

    </div>

    <div class="block">

    EV charging pool details. It is available only for a place that is a
    charging pool for electric vehicles. It is fully supported for
    offline search, provided that LayerConfiguration.Feature.EV is
    enabled in SDKOptions.layerConfiguration . For online search, this
    feature is only available if it is explicitly enabled. To do that,
    call SearchEngine.set_custom_option() with arguments: name:
    "lookup.show" or "discover.show" or "browse.show" value: "ev" To
    enable this feature for all queries, call
    SearchEngine.set_custom_option() for all: "lookup.show",
    "discover.show" and "browse.show". To enable fuel station details or
    truck amenities, the custom option value can be combined as
    "ev,truck", "ev,truck,fuel" etc.

    </div>

    </div>

  - <div id="sdk-for-android-explore-truckAmenities"
    class="section detail">

    ### truckAmenities

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TruckAmenities](sdk-for-android-explore-com-here-sdk-search-truckamenities "class in com.here.sdk.search")</span> <span class="element-name">truckAmenities</span>

    </div>

    <div class="block">

    Additional information that is available only for places that
    contain truck amenities. It is fully supported for offline search,
    provided that LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES is
    enabled in SDKOptions.layerConfiguration . Note: Currently, for
    online search, this is a closed-alpha feature, so it is available
    only for selected customers. The field is always null for everyone
    that is not part of the closed-alpha group. Participants of the
    closed-alpha group can get access from HERE to use this feature. If
    the credentials are not enabled, a SearchError.FORBIDDEN will be
    propagated. For online search, this feature is only available if it
    is explicitly enabled. To do that, call
    SearchEngine.set_custom_option() with arguments: name: "lookup.show"
    or "discover.show" or "autosuggest.show" or "browse.show" value:
    "truck" To enable this feature for all queries, call
    SearchEngine.set_custom_option() for all: "lookup.show",
    "discover.show", "autosuggest.show" and "browse.show". To enable
    both truck_amenities and fuel_station features, set the value to
    "fuel,truck". Note: This is a beta release of this feature, so there
    could be a few bugs and unexpected behaviors. Related APIs may
    change for new releases without a deprecation process.

    </div>

    </div>

  - <div id="sdk-for-android-explore-fuelStation"
    class="section detail">

    ### fuelStation

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[FuelStation](sdk-for-android-explore-com-here-sdk-search-fuelstation "class in com.here.sdk.search")</span> <span class="element-name">fuelStation</span>

    </div>

    <div class="block">

    Fuel station details. It is available only if a place is a fuel
    station and contain fuel data. It is fully supported for offline
    search, provided that
    LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES is enabled in
    SDKOptions.layerConfiguration . Note: Currently, for online search,
    this is a closed-alpha feature, so it is available only for selected
    customers. The field is always null for everyone that is not part of
    the closed-alpha group. Participants of the closed-alpha group can
    get access from HERE to use this feature. If the credentials are not
    enabled, a SearchError.FORBIDDEN will be propagated. For online
    search, this feature is only available if it is explicitly enabled.
    To do that, call SearchEngine.set_custom_option() with arguments:
    name: "lookup.show" or "discover.show" or "autosuggest.show" or
    "browse.show" value: "fuel" To enable this feature for all queries,
    call SearchEngine.set_custom_option() for all: "lookup.show",
    "discover.show", "autosuggest.show" and "browse.show". To enable
    both truck_amenities and fuel_station features, set the value to
    "fuel,truck". Note: This is a beta release of this feature, so there
    could be a few bugs and unexpected behaviors. Related APIs may
    change for new releases without a deprecation process.

    </div>

    </div>

  - <div id="sdk-for-android-explore-foodTypes" class="section detail">

    ### foodTypes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PlaceFoodType](sdk-for-android-explore-com-here-sdk-search-placefoodtype "class in com.here.sdk.search")></span> <span class="element-name">foodTypes</span>

    </div>

    <div class="block">

    The list of food types assigned to this place. Not supported in
    OfflineSearchEngine (only available for the Navigate license).

    </div>

    </div>

  - <div id="sdk-for-android-explore-payment" class="section detail">

    ### payment

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[POIPaymentDetails](sdk-for-android-explore-com-here-sdk-search-poipaymentdetails "class in com.here.sdk.search")</span> <span class="element-name">payment</span>

    </div>

    <div class="block">

    Details about the payment options at the POI. Set to null if the
    place is not a POI or if payment details are not available. Not
    supported in OfflineSearchEngine (only available for the Navigate
    license). Note: This is a beta release of this feature, so there
    could be a few bugs and unexpected behaviors. Related APIs may
    change for new releases without a deprecation process.

    </div>

    </div>

  - <div id="sdk-for-android-explore-evChargingLocation"
    class="section detail">

    ### evChargingLocation

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[EVChargingLocation](sdk-for-android-explore-com-here-sdk-search-evcharginglocation "class in com.here.sdk.search")</span> <span class="element-name">evChargingLocation</span>

    </div>

    <div class="block">

    Details about the EV charging station, if this place belongs to the
    EV charging station category. Note: This is a beta release of this
    feature, so there could be a few bugs and unexpected behaviors.
    Related APIs may change for new releases without a deprecation
    process.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List)"
    class="section detail">

    ### Details

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Details</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[Contact](sdk-for-android-explore-com-here-sdk-search-contact "class in com.here.sdk.search")> contacts,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[OpeningHours](sdk-for-android-explore-com-here-sdk-search-openinghours "class in com.here.sdk.search")> openingHours,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")> categories,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebImage](sdk-for-android-explore-com-here-sdk-search-webimage "class in com.here.sdk.search")> images,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebEditorial](sdk-for-android-explore-com-here-sdk-search-webeditorial "class in com.here.sdk.search")> editorials,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebRating](sdk-for-android-explore-com-here-sdk-search-webrating "class in com.here.sdk.search")> ratings,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[SupplierReference](sdk-for-android-explore-com-here-sdk-search-supplierreference "class in com.here.sdk.search")> references)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `contacts` -

    The list of contact information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `openingHours` -

    The list of opening hours information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `categories` -

    The list of categories assigned to this place.

    `images` -

    The list of images associated with the place. The images are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `editorials` -

    The list of editorials associated with the place. The editorials are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `ratings` -

    The list of ratings associated with the place. The ratings are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `references` -

    The list of supplier references to this place. The references are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty.

    </div>

  - <div id="sdk-for-android-explore-<init>(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool)"
    class="section detail">

    ### Details

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Details</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[Contact](sdk-for-android-explore-com-here-sdk-search-contact "class in com.here.sdk.search")> contacts,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[OpeningHours](sdk-for-android-explore-com-here-sdk-search-openinghours "class in com.here.sdk.search")> openingHours,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")> categories,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebImage](sdk-for-android-explore-com-here-sdk-search-webimage "class in com.here.sdk.search")> images,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebEditorial](sdk-for-android-explore-com-here-sdk-search-webeditorial "class in com.here.sdk.search")> editorials,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebRating](sdk-for-android-explore-com-here-sdk-search-webrating "class in com.here.sdk.search")> ratings,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[SupplierReference](sdk-for-android-explore-com-here-sdk-search-supplierreference "class in com.here.sdk.search")> references,
    @Nullable
    [EVChargingPool](sdk-for-android-explore-com-here-sdk-search-evchargingpool "class in com.here.sdk.search") evChargingPool)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `contacts` -

    The list of contact information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `openingHours` -

    The list of opening hours information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `categories` -

    The list of categories assigned to this place.

    `images` -

    The list of images associated with the place. The images are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `editorials` -

    The list of editorials associated with the place. The editorials are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `ratings` -

    The list of ratings associated with the place. The ratings are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `references` -

    The list of supplier references to this place. The references are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty.

    `evChargingPool` -

    EV charging pool details. It is available only for a place that is a
    charging pool for electric vehicles. It is fully supported for
    offline search, provided that
    [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#EV)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    For online search, this feature is only available if it is
    explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "browse.show" value: "ev" To enable this feature for all queries,
    call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show" and "browse.show". To enable
    fuel station details or truck amenities, the custom option value can
    be combined as "ev,truck", "ev,truck,fuel" etc.

    </div>

  - <div id="sdk-for-android-explore-<init>(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities)"
    class="section detail">

    ### Details

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Details</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[Contact](sdk-for-android-explore-com-here-sdk-search-contact "class in com.here.sdk.search")> contacts,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[OpeningHours](sdk-for-android-explore-com-here-sdk-search-openinghours "class in com.here.sdk.search")> openingHours,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")> categories,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebImage](sdk-for-android-explore-com-here-sdk-search-webimage "class in com.here.sdk.search")> images,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebEditorial](sdk-for-android-explore-com-here-sdk-search-webeditorial "class in com.here.sdk.search")> editorials,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebRating](sdk-for-android-explore-com-here-sdk-search-webrating "class in com.here.sdk.search")> ratings,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[SupplierReference](sdk-for-android-explore-com-here-sdk-search-supplierreference "class in com.here.sdk.search")> references,
    @Nullable
    [EVChargingPool](sdk-for-android-explore-com-here-sdk-search-evchargingpool "class in com.here.sdk.search") evChargingPool,
    @Nullable
    [TruckAmenities](sdk-for-android-explore-com-here-sdk-search-truckamenities "class in com.here.sdk.search") truckAmenities)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `contacts` -

    The list of contact information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `openingHours` -

    The list of opening hours information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `categories` -

    The list of categories assigned to this place.

    `images` -

    The list of images associated with the place. The images are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `editorials` -

    The list of editorials associated with the place. The editorials are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `ratings` -

    The list of ratings associated with the place. The ratings are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `references` -

    The list of supplier references to this place. The references are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty.

    `evChargingPool` -

    EV charging pool details. It is available only for a place that is a
    charging pool for electric vehicles. It is fully supported for
    offline search, provided that
    [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#EV)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    For online search, this feature is only available if it is
    explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "browse.show" value: "ev" To enable this feature for all queries,
    call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show" and "browse.show". To enable
    fuel station details or truck amenities, the custom option value can
    be combined as "ev,truck", "ev,truck,fuel" etc.

    `truckAmenities` -

    Additional information that is available only for places that
    contain truck amenities. It is fully supported for offline search,
    provided that
    [`LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    **Note:** Currently, for online search, this is a closed-alpha
    feature, so it is available only for selected customers. The field
    is always null for everyone that is not part of the closed-alpha
    group. Participants of the closed-alpha group can get access from
    HERE to use this feature. If the credentials are not enabled, a
    [`SearchError.FORBIDDEN`](sdk-for-android-explore-com-here-sdk-search-searcherror#FORBIDDEN)
    will be propagated. For online search, this feature is only
    available if it is explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "autosuggest.show" or "browse.show" value: "truck" To enable this
    feature for all queries, call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show", "autosuggest.show" and
    "browse.show". To enable both `truck_amenities` and `fuel_station`
    features, set the value to "fuel,truck". **Note:** This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    </div>

  - <div id="sdk-for-android-explore-<init>(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation)"
    class="section detail">

    ### Details

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Details</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[Contact](sdk-for-android-explore-com-here-sdk-search-contact "class in com.here.sdk.search")> contacts,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[OpeningHours](sdk-for-android-explore-com-here-sdk-search-openinghours "class in com.here.sdk.search")> openingHours,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")> categories,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebImage](sdk-for-android-explore-com-here-sdk-search-webimage "class in com.here.sdk.search")> images,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebEditorial](sdk-for-android-explore-com-here-sdk-search-webeditorial "class in com.here.sdk.search")> editorials,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebRating](sdk-for-android-explore-com-here-sdk-search-webrating "class in com.here.sdk.search")> ratings,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[SupplierReference](sdk-for-android-explore-com-here-sdk-search-supplierreference "class in com.here.sdk.search")> references,
    @Nullable
    [EVChargingPool](sdk-for-android-explore-com-here-sdk-search-evchargingpool "class in com.here.sdk.search") evChargingPool,
    @Nullable
    [TruckAmenities](sdk-for-android-explore-com-here-sdk-search-truckamenities "class in com.here.sdk.search") truckAmenities,
    @Nullable
    [FuelStation](sdk-for-android-explore-com-here-sdk-search-fuelstation "class in com.here.sdk.search") fuelStation)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `contacts` -

    The list of contact information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `openingHours` -

    The list of opening hours information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `categories` -

    The list of categories assigned to this place.

    `images` -

    The list of images associated with the place. The images are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `editorials` -

    The list of editorials associated with the place. The editorials are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `ratings` -

    The list of ratings associated with the place. The ratings are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `references` -

    The list of supplier references to this place. The references are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty.

    `evChargingPool` -

    EV charging pool details. It is available only for a place that is a
    charging pool for electric vehicles. It is fully supported for
    offline search, provided that
    [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#EV)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    For online search, this feature is only available if it is
    explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "browse.show" value: "ev" To enable this feature for all queries,
    call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show" and "browse.show". To enable
    fuel station details or truck amenities, the custom option value can
    be combined as "ev,truck", "ev,truck,fuel" etc.

    `truckAmenities` -

    Additional information that is available only for places that
    contain truck amenities. It is fully supported for offline search,
    provided that
    [`LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    **Note:** Currently, for online search, this is a closed-alpha
    feature, so it is available only for selected customers. The field
    is always null for everyone that is not part of the closed-alpha
    group. Participants of the closed-alpha group can get access from
    HERE to use this feature. If the credentials are not enabled, a
    [`SearchError.FORBIDDEN`](sdk-for-android-explore-com-here-sdk-search-searcherror#FORBIDDEN)
    will be propagated. For online search, this feature is only
    available if it is explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "autosuggest.show" or "browse.show" value: "truck" To enable this
    feature for all queries, call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show", "autosuggest.show" and
    "browse.show". To enable both `truck_amenities` and `fuel_station`
    features, set the value to "fuel,truck". **Note:** This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    `fuelStation` -

    Fuel station details. It is available only if a place is a fuel
    station and contain fuel data. It is fully supported for offline
    search, provided that
    [`LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#FUEL_STATION_ATTRIBUTES)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    **Note:** Currently, for online search, this is a closed-alpha
    feature, so it is available only for selected customers. The field
    is always null for everyone that is not part of the closed-alpha
    group. Participants of the closed-alpha group can get access from
    HERE to use this feature. If the credentials are not enabled, a
    [`SearchError.FORBIDDEN`](sdk-for-android-explore-com-here-sdk-search-searcherror#FORBIDDEN)
    will be propagated. For online search, this feature is only
    available if it is explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "autosuggest.show" or "browse.show" value: "fuel" To enable this
    feature for all queries, call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show", "autosuggest.show" and
    "browse.show". To enable both `truck_amenities` and `fuel_station`
    features, set the value to "fuel,truck". **Note:** This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    </div>

  - <div id="sdk-for-android-explore-<init>(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List)"
    class="section detail">

    ### Details

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Details</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[Contact](sdk-for-android-explore-com-here-sdk-search-contact "class in com.here.sdk.search")> contacts,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[OpeningHours](sdk-for-android-explore-com-here-sdk-search-openinghours "class in com.here.sdk.search")> openingHours,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")> categories,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebImage](sdk-for-android-explore-com-here-sdk-search-webimage "class in com.here.sdk.search")> images,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebEditorial](sdk-for-android-explore-com-here-sdk-search-webeditorial "class in com.here.sdk.search")> editorials,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebRating](sdk-for-android-explore-com-here-sdk-search-webrating "class in com.here.sdk.search")> ratings,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[SupplierReference](sdk-for-android-explore-com-here-sdk-search-supplierreference "class in com.here.sdk.search")> references,
    @Nullable
    [EVChargingPool](sdk-for-android-explore-com-here-sdk-search-evchargingpool "class in com.here.sdk.search") evChargingPool,
    @Nullable
    [TruckAmenities](sdk-for-android-explore-com-here-sdk-search-truckamenities "class in com.here.sdk.search") truckAmenities,
    @Nullable
    [FuelStation](sdk-for-android-explore-com-here-sdk-search-fuelstation "class in com.here.sdk.search") fuelStation,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PlaceFoodType](sdk-for-android-explore-com-here-sdk-search-placefoodtype "class in com.here.sdk.search")> foodTypes)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `contacts` -

    The list of contact information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `openingHours` -

    The list of opening hours information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `categories` -

    The list of categories assigned to this place.

    `images` -

    The list of images associated with the place. The images are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `editorials` -

    The list of editorials associated with the place. The editorials are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `ratings` -

    The list of ratings associated with the place. The ratings are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `references` -

    The list of supplier references to this place. The references are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty.

    `evChargingPool` -

    EV charging pool details. It is available only for a place that is a
    charging pool for electric vehicles. It is fully supported for
    offline search, provided that
    [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#EV)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    For online search, this feature is only available if it is
    explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "browse.show" value: "ev" To enable this feature for all queries,
    call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show" and "browse.show". To enable
    fuel station details or truck amenities, the custom option value can
    be combined as "ev,truck", "ev,truck,fuel" etc.

    `truckAmenities` -

    Additional information that is available only for places that
    contain truck amenities. It is fully supported for offline search,
    provided that
    [`LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    **Note:** Currently, for online search, this is a closed-alpha
    feature, so it is available only for selected customers. The field
    is always null for everyone that is not part of the closed-alpha
    group. Participants of the closed-alpha group can get access from
    HERE to use this feature. If the credentials are not enabled, a
    [`SearchError.FORBIDDEN`](sdk-for-android-explore-com-here-sdk-search-searcherror#FORBIDDEN)
    will be propagated. For online search, this feature is only
    available if it is explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "autosuggest.show" or "browse.show" value: "truck" To enable this
    feature for all queries, call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show", "autosuggest.show" and
    "browse.show". To enable both `truck_amenities` and `fuel_station`
    features, set the value to "fuel,truck". **Note:** This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    `fuelStation` -

    Fuel station details. It is available only if a place is a fuel
    station and contain fuel data. It is fully supported for offline
    search, provided that
    [`LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#FUEL_STATION_ATTRIBUTES)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    **Note:** Currently, for online search, this is a closed-alpha
    feature, so it is available only for selected customers. The field
    is always null for everyone that is not part of the closed-alpha
    group. Participants of the closed-alpha group can get access from
    HERE to use this feature. If the credentials are not enabled, a
    [`SearchError.FORBIDDEN`](sdk-for-android-explore-com-here-sdk-search-searcherror#FORBIDDEN)
    will be propagated. For online search, this feature is only
    available if it is explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "autosuggest.show" or "browse.show" value: "fuel" To enable this
    feature for all queries, call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show", "autosuggest.show" and
    "browse.show". To enable both `truck_amenities` and `fuel_station`
    features, set the value to "fuel,truck". **Note:** This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    `foodTypes` -

    The list of food types assigned to this place. Not supported in
    `OfflineSearchEngine` (only available for the Navigate license).

    </div>

  - <div id="sdk-for-android-explore-<init>(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List,com.here.sdk.search.POIPaymentDetails)"
    class="section detail">

    ### Details

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Details</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[Contact](sdk-for-android-explore-com-here-sdk-search-contact "class in com.here.sdk.search")> contacts,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[OpeningHours](sdk-for-android-explore-com-here-sdk-search-openinghours "class in com.here.sdk.search")> openingHours,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")> categories,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebImage](sdk-for-android-explore-com-here-sdk-search-webimage "class in com.here.sdk.search")> images,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebEditorial](sdk-for-android-explore-com-here-sdk-search-webeditorial "class in com.here.sdk.search")> editorials,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebRating](sdk-for-android-explore-com-here-sdk-search-webrating "class in com.here.sdk.search")> ratings,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[SupplierReference](sdk-for-android-explore-com-here-sdk-search-supplierreference "class in com.here.sdk.search")> references,
    @Nullable
    [EVChargingPool](sdk-for-android-explore-com-here-sdk-search-evchargingpool "class in com.here.sdk.search") evChargingPool,
    @Nullable
    [TruckAmenities](sdk-for-android-explore-com-here-sdk-search-truckamenities "class in com.here.sdk.search") truckAmenities,
    @Nullable
    [FuelStation](sdk-for-android-explore-com-here-sdk-search-fuelstation "class in com.here.sdk.search") fuelStation,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PlaceFoodType](sdk-for-android-explore-com-here-sdk-search-placefoodtype "class in com.here.sdk.search")> foodTypes,
    @Nullable
    [POIPaymentDetails](sdk-for-android-explore-com-here-sdk-search-poipaymentdetails "class in com.here.sdk.search") payment)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `contacts` -

    The list of contact information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `openingHours` -

    The list of opening hours information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `categories` -

    The list of categories assigned to this place.

    `images` -

    The list of images associated with the place. The images are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `editorials` -

    The list of editorials associated with the place. The editorials are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `ratings` -

    The list of ratings associated with the place. The ratings are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `references` -

    The list of supplier references to this place. The references are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty.

    `evChargingPool` -

    EV charging pool details. It is available only for a place that is a
    charging pool for electric vehicles. It is fully supported for
    offline search, provided that
    [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#EV)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    For online search, this feature is only available if it is
    explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "browse.show" value: "ev" To enable this feature for all queries,
    call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show" and "browse.show". To enable
    fuel station details or truck amenities, the custom option value can
    be combined as "ev,truck", "ev,truck,fuel" etc.

    `truckAmenities` -

    Additional information that is available only for places that
    contain truck amenities. It is fully supported for offline search,
    provided that
    [`LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    **Note:** Currently, for online search, this is a closed-alpha
    feature, so it is available only for selected customers. The field
    is always null for everyone that is not part of the closed-alpha
    group. Participants of the closed-alpha group can get access from
    HERE to use this feature. If the credentials are not enabled, a
    [`SearchError.FORBIDDEN`](sdk-for-android-explore-com-here-sdk-search-searcherror#FORBIDDEN)
    will be propagated. For online search, this feature is only
    available if it is explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "autosuggest.show" or "browse.show" value: "truck" To enable this
    feature for all queries, call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show", "autosuggest.show" and
    "browse.show". To enable both `truck_amenities` and `fuel_station`
    features, set the value to "fuel,truck". **Note:** This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    `fuelStation` -

    Fuel station details. It is available only if a place is a fuel
    station and contain fuel data. It is fully supported for offline
    search, provided that
    [`LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#FUEL_STATION_ATTRIBUTES)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    **Note:** Currently, for online search, this is a closed-alpha
    feature, so it is available only for selected customers. The field
    is always null for everyone that is not part of the closed-alpha
    group. Participants of the closed-alpha group can get access from
    HERE to use this feature. If the credentials are not enabled, a
    [`SearchError.FORBIDDEN`](sdk-for-android-explore-com-here-sdk-search-searcherror#FORBIDDEN)
    will be propagated. For online search, this feature is only
    available if it is explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "autosuggest.show" or "browse.show" value: "fuel" To enable this
    feature for all queries, call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show", "autosuggest.show" and
    "browse.show". To enable both `truck_amenities` and `fuel_station`
    features, set the value to "fuel,truck". **Note:** This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    `foodTypes` -

    The list of food types assigned to this place. Not supported in
    `OfflineSearchEngine` (only available for the Navigate license).

    `payment` -

    Details about the payment options at the POI. Set to `null` if the
    place is not a POI or if payment details are not available. Not
    supported in `OfflineSearchEngine` (only available for the Navigate
    license). **Note:** This is a beta release of this feature, so there
    could be a few bugs and unexpected behaviors. Related APIs may
    change for new releases without a deprecation process.

    </div>

  - <div id="sdk-for-android-explore-<init>(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List,com.here.sdk.search.POIPaymentDetails,com.here.sdk.search.EVChargingLocation)"
    class="section detail">

    ### Details

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Details</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[Contact](sdk-for-android-explore-com-here-sdk-search-contact "class in com.here.sdk.search")> contacts,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[OpeningHours](sdk-for-android-explore-com-here-sdk-search-openinghours "class in com.here.sdk.search")> openingHours,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")> categories,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebImage](sdk-for-android-explore-com-here-sdk-search-webimage "class in com.here.sdk.search")> images,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebEditorial](sdk-for-android-explore-com-here-sdk-search-webeditorial "class in com.here.sdk.search")> editorials,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[WebRating](sdk-for-android-explore-com-here-sdk-search-webrating "class in com.here.sdk.search")> ratings,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[SupplierReference](sdk-for-android-explore-com-here-sdk-search-supplierreference "class in com.here.sdk.search")> references,
    @Nullable
    [EVChargingPool](sdk-for-android-explore-com-here-sdk-search-evchargingpool "class in com.here.sdk.search") evChargingPool,
    @Nullable
    [TruckAmenities](sdk-for-android-explore-com-here-sdk-search-truckamenities "class in com.here.sdk.search") truckAmenities,
    @Nullable
    [FuelStation](sdk-for-android-explore-com-here-sdk-search-fuelstation "class in com.here.sdk.search") fuelStation,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PlaceFoodType](sdk-for-android-explore-com-here-sdk-search-placefoodtype "class in com.here.sdk.search")> foodTypes,
    @Nullable
    [POIPaymentDetails](sdk-for-android-explore-com-here-sdk-search-poipaymentdetails "class in com.here.sdk.search") payment,
    @Nullable
    [EVChargingLocation](sdk-for-android-explore-com-here-sdk-search-evcharginglocation "class in com.here.sdk.search") evChargingLocation)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `contacts` -

    The list of contact information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `openingHours` -

    The list of opening hours information of the place. **Note:** Not
    available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `categories` -

    The list of categories assigned to this place.

    `images` -

    The list of images associated with the place. The images are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `editorials` -

    The list of editorials associated with the place. The editorials are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `ratings` -

    The list of ratings associated with the place. The ratings are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty. **Note:** Not available as part of
    [`Suggestion`](sdk-for-android-explore-com-here-sdk-search-suggestion "class in com.here.sdk.search")
    results.

    `references` -

    The list of supplier references to this place. The references are
    provided by external suppliers and are only available to users with
    valid contracts with said suppliers. If the user has no such
    contracts, the list is empty.

    `evChargingPool` -

    EV charging pool details. It is available only for a place that is a
    charging pool for electric vehicles. It is fully supported for
    offline search, provided that
    [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#EV)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    For online search, this feature is only available if it is
    explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "browse.show" value: "ev" To enable this feature for all queries,
    call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show" and "browse.show". To enable
    fuel station details or truck amenities, the custom option value can
    be combined as "ev,truck", "ev,truck,fuel" etc.

    `truckAmenities` -

    Additional information that is available only for places that
    contain truck amenities. It is fully supported for offline search,
    provided that
    [`LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    **Note:** Currently, for online search, this is a closed-alpha
    feature, so it is available only for selected customers. The field
    is always null for everyone that is not part of the closed-alpha
    group. Participants of the closed-alpha group can get access from
    HERE to use this feature. If the credentials are not enabled, a
    [`SearchError.FORBIDDEN`](sdk-for-android-explore-com-here-sdk-search-searcherror#FORBIDDEN)
    will be propagated. For online search, this feature is only
    available if it is explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "autosuggest.show" or "browse.show" value: "truck" To enable this
    feature for all queries, call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show", "autosuggest.show" and
    "browse.show". To enable both `truck_amenities` and `fuel_station`
    features, set the value to "fuel,truck". **Note:** This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    `fuelStation` -

    Fuel station details. It is available only if a place is a fuel
    station and contain fuel data. It is fully supported for offline
    search, provided that
    [`LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#FUEL_STATION_ATTRIBUTES)
    is enabled in
    [`SDKOptions.layerConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration).
    **Note:** Currently, for online search, this is a closed-alpha
    feature, so it is available only for selected customers. The field
    is always null for everyone that is not part of the closed-alpha
    group. Participants of the closed-alpha group can get access from
    HERE to use this feature. If the credentials are not enabled, a
    [`SearchError.FORBIDDEN`](sdk-for-android-explore-com-here-sdk-search-searcherror#FORBIDDEN)
    will be propagated. For online search, this feature is only
    available if it is explicitly enabled. To do that, call

        SearchEngine.set_custom_option()

    with arguments: name: "lookup.show" or "discover.show" or
    "autosuggest.show" or "browse.show" value: "fuel" To enable this
    feature for all queries, call

        SearchEngine.set_custom_option()

    for all: "lookup.show", "discover.show", "autosuggest.show" and
    "browse.show". To enable both `truck_amenities` and `fuel_station`
    features, set the value to "fuel,truck". **Note:** This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    `foodTypes` -

    The list of food types assigned to this place. Not supported in
    `OfflineSearchEngine` (only available for the Navigate license).

    `payment` -

    Details about the payment options at the POI. Set to `null` if the
    place is not a POI or if payment details are not available. Not
    supported in `OfflineSearchEngine` (only available for the Navigate
    license). **Note:** This is a beta release of this feature, so there
    could be a few bugs and unexpected behaviors. Related APIs may
    change for new releases without a deprecation process.

    `evChargingLocation` -

    Details about the EV charging station, if this place belongs to the
    EV charging station category. **Note:** This is a beta release of
    this feature, so there could be a few bugs and unexpected behaviors.
    Related APIs may change for new releases without a deprecation
    process.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals(java.lang.Object)"
    class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
    class="external-link"
    title="class or interface in java.lang"><code>equals</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
    class="external-link"
    title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-getPrimaryCategories()"
    class="section detail">

    ### getPrimaryCategories

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")></span> <span class="element-name">getPrimaryCategories</span>()

    </div>

    <div class="block">

    Gets the list of primary categories assigned to this place.

    </div>

    Returns:  
    List of categories.

    </div>

  </div>

</div>


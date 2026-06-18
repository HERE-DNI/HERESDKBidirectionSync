---
title: "Details (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-details"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Details.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-search-package-summary">com.here.sdk.search</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.search.Details</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Details</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Contains details of a specific place, such as contact information,
 opening hours and assigned categories.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#categories">categories</a></code></div>
<div class="col-last even-row-color">
<div class="block">The list of categories assigned to this place.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#contacts">contacts</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The list of contact information of the place.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#editorials">editorials</a></code></div>
<div class="col-last even-row-color">
<div class="block">The list of editorials associated with the place.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-evcharginglocation" title="class in com.here.sdk.search">EVChargingLocation</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#evChargingLocation">evChargingLocation</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Details about the EV charging station, if this place belongs to the EV charging station category.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#evChargingPool">evChargingPool</a></code></div>
<div class="col-last even-row-color">
<div class="block">EV charging pool details.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#foodTypes">foodTypes</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The list of food types assigned to this place.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-fuelstation" title="class in com.here.sdk.search">FuelStation</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#fuelStation">fuelStation</a></code></div>
<div class="col-last even-row-color">
<div class="block">Fuel station details.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#images">images</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The list of images associated with the place.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#openingHours">openingHours</a></code></div>
<div class="col-last even-row-color">
<div class="block">The list of opening hours information of the place.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-poipaymentdetails" title="class in com.here.sdk.search">POIPaymentDetails</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#payment">payment</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Details about the payment options at the POI.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#ratings">ratings</a></code></div>
<div class="col-last even-row-color">
<div class="block">The list of ratings associated with the place.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#references">references</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The list of supplier references to this place.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#truckAmenities">truckAmenities</a></code></div>
<div class="col-last even-row-color">
<div class="block">Additional information that is available only for places that contain truck amenities.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List)">Details</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool)">Details</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 <a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities)">Details</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 <a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 <a href="sdk-for-android-navigate-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation)">Details</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 <a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 <a href="sdk-for-android-navigate-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 <a href="sdk-for-android-navigate-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List)">Details</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 <a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 <a href="sdk-for-android-navigate-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 <a href="sdk-for-android-navigate-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt; foodTypes)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List,com.here.sdk.search.POIPaymentDetails)">Details</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 <a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 <a href="sdk-for-android-navigate-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 <a href="sdk-for-android-navigate-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt; foodTypes,
 <a href="sdk-for-android-navigate-poipaymentdetails" title="class in com.here.sdk.search">POIPaymentDetails</a> payment)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List,com.here.sdk.search.POIPaymentDetails,com.here.sdk.search.EVChargingLocation)">Details</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 <a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 <a href="sdk-for-android-navigate-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 <a href="sdk-for-android-navigate-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt; foodTypes,
 <a href="sdk-for-android-navigate-poipaymentdetails" title="class in com.here.sdk.search">POIPaymentDetails</a> payment,
 <a href="sdk-for-android-navigate-evcharginglocation" title="class in com.here.sdk.search">EVChargingLocation</a> evChargingLocation)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getPrimaryCategories()">getPrimaryCategories</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of primary categories assigned to this place.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="contacts">
<h3>contacts</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt;</span> <span class="element-name">contacts</span></div>
<div class="block"><p>The list of contact information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></div>
</section>
</li>
<li>
<section class="detail" id="openingHours">
<h3>openingHours</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt;</span> <span class="element-name">openingHours</span></div>
<div class="block"><p>The list of opening hours information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></div>
</section>
</li>
<li>
<section class="detail" id="categories">
<h3>categories</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</span> <span class="element-name">categories</span></div>
<div class="block"><p>The list of categories assigned to this place.</p></div>
</section>
</li>
<li>
<section class="detail" id="images">
<h3>images</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt;</span> <span class="element-name">images</span></div>
<div class="block"><p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></div>
</section>
</li>
<li>
<section class="detail" id="editorials">
<h3>editorials</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt;</span> <span class="element-name">editorials</span></div>
<div class="block"><p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></div>
</section>
</li>
<li>
<section class="detail" id="ratings">
<h3>ratings</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt;</span> <span class="element-name">ratings</span></div>
<div class="block"><p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></div>
</section>
</li>
<li>
<section class="detail" id="references">
<h3>references</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt;</span> <span class="element-name">references</span></div>
<div class="block"><p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></div>
</section>
</li>
<li>
<section class="detail" id="evChargingPool">
<h3>evChargingPool</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a></span> <span class="element-name">evChargingPool</span></div>
<div class="block"><p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "browse.show"
 value: "ev"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show" and "browse.show".
 To enable fuel station details or truck amenities, the custom option value can be combined
 as "ev,truck", "ev,truck,fuel" etc.</p></div>
</section>
</li>
<li>
<section class="detail" id="truckAmenities">
<h3>truckAmenities</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a></span> <span class="element-name">truckAmenities</span></div>
<div class="block"><p>Additional information that is available only for places that contain truck amenities.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#TRUCK_SERVICE_ATTRIBUTES"><code>LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "truck"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section class="detail" id="fuelStation">
<h3>fuelStation</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-fuelstation" title="class in com.here.sdk.search">FuelStation</a></span> <span class="element-name">fuelStation</span></div>
<div class="block"><p>Fuel station details. It is available only if a place is a fuel station and contain fuel data.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#FUEL_STATION_ATTRIBUTES"><code>LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "fuel"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section class="detail" id="foodTypes">
<h3>foodTypes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt;</span> <span class="element-name">foodTypes</span></div>
<div class="block"><p>The list of food types assigned to this place.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p></div>
</section>
</li>
<li>
<section class="detail" id="payment">
<h3>payment</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-poipaymentdetails" title="class in com.here.sdk.search">POIPaymentDetails</a></span> <span class="element-name">payment</span></div>
<div class="block"><p>Details about the payment options at the POI.
 Set to <code>null</code> if the place is not a POI or if payment details are not available.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section class="detail" id="evChargingLocation">
<h3>evChargingLocation</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-evcharginglocation" title="class in com.here.sdk.search">EVChargingLocation</a></span> <span class="element-name">evChargingLocation</span></div>
<div class="block"><p>Details about the EV charging station, if this place belongs to the EV charging station category.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List)">
<h3>Details</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Details</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool)">
<h3>Details</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Details</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 @Nullable
 <a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
<dd><code>evChargingPool</code> - <p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "browse.show"
 value: "ev"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show" and "browse.show".
 To enable fuel station details or truck amenities, the custom option value can be combined
 as "ev,truck", "ev,truck,fuel" etc.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities)">
<h3>Details</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Details</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 @Nullable
 <a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 @Nullable
 <a href="sdk-for-android-navigate-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
<dd><code>evChargingPool</code> - <p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "browse.show"
 value: "ev"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show" and "browse.show".
 To enable fuel station details or truck amenities, the custom option value can be combined
 as "ev,truck", "ev,truck,fuel" etc.</p></dd>
<dd><code>truckAmenities</code> - <p>Additional information that is available only for places that contain truck amenities.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#TRUCK_SERVICE_ATTRIBUTES"><code>LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "truck"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation)">
<h3>Details</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Details</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 @Nullable
 <a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 @Nullable
 <a href="sdk-for-android-navigate-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 @Nullable
 <a href="sdk-for-android-navigate-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
<dd><code>evChargingPool</code> - <p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "browse.show"
 value: "ev"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show" and "browse.show".
 To enable fuel station details or truck amenities, the custom option value can be combined
 as "ev,truck", "ev,truck,fuel" etc.</p></dd>
<dd><code>truckAmenities</code> - <p>Additional information that is available only for places that contain truck amenities.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#TRUCK_SERVICE_ATTRIBUTES"><code>LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "truck"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>fuelStation</code> - <p>Fuel station details. It is available only if a place is a fuel station and contain fuel data.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#FUEL_STATION_ATTRIBUTES"><code>LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "fuel"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List)">
<h3>Details</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Details</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 @Nullable
 <a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 @Nullable
 <a href="sdk-for-android-navigate-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 @Nullable
 <a href="sdk-for-android-navigate-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt; foodTypes)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
<dd><code>evChargingPool</code> - <p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "browse.show"
 value: "ev"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show" and "browse.show".
 To enable fuel station details or truck amenities, the custom option value can be combined
 as "ev,truck", "ev,truck,fuel" etc.</p></dd>
<dd><code>truckAmenities</code> - <p>Additional information that is available only for places that contain truck amenities.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#TRUCK_SERVICE_ATTRIBUTES"><code>LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "truck"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>fuelStation</code> - <p>Fuel station details. It is available only if a place is a fuel station and contain fuel data.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#FUEL_STATION_ATTRIBUTES"><code>LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "fuel"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>foodTypes</code> - <p>The list of food types assigned to this place.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List,com.here.sdk.search.POIPaymentDetails)">
<h3>Details</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Details</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 @Nullable
 <a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 @Nullable
 <a href="sdk-for-android-navigate-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 @Nullable
 <a href="sdk-for-android-navigate-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt; foodTypes,
 @Nullable
 <a href="sdk-for-android-navigate-poipaymentdetails" title="class in com.here.sdk.search">POIPaymentDetails</a> payment)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
<dd><code>evChargingPool</code> - <p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "browse.show"
 value: "ev"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show" and "browse.show".
 To enable fuel station details or truck amenities, the custom option value can be combined
 as "ev,truck", "ev,truck,fuel" etc.</p></dd>
<dd><code>truckAmenities</code> - <p>Additional information that is available only for places that contain truck amenities.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#TRUCK_SERVICE_ATTRIBUTES"><code>LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "truck"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>fuelStation</code> - <p>Fuel station details. It is available only if a place is a fuel station and contain fuel data.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#FUEL_STATION_ATTRIBUTES"><code>LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "fuel"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>foodTypes</code> - <p>The list of food types assigned to this place.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p></dd>
<dd><code>payment</code> - <p>Details about the payment options at the POI.
 Set to <code>null</code> if the place is not a POI or if payment details are not available.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List,com.here.sdk.search.POIPaymentDetails,com.here.sdk.search.EVChargingLocation)">
<h3>Details</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Details</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 @Nullable
 <a href="sdk-for-android-navigate-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 @Nullable
 <a href="sdk-for-android-navigate-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 @Nullable
 <a href="sdk-for-android-navigate-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt; foodTypes,
 @Nullable
 <a href="sdk-for-android-navigate-poipaymentdetails" title="class in com.here.sdk.search">POIPaymentDetails</a> payment,
 @Nullable
 <a href="sdk-for-android-navigate-evcharginglocation" title="class in com.here.sdk.search">EVChargingLocation</a> evChargingLocation)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 </p><p><strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
<dd><code>evChargingPool</code> - <p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "browse.show"
 value: "ev"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show" and "browse.show".
 To enable fuel station details or truck amenities, the custom option value can be combined
 as "ev,truck", "ev,truck,fuel" etc.</p></dd>
<dd><code>truckAmenities</code> - <p>Additional information that is available only for places that contain truck amenities.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#TRUCK_SERVICE_ATTRIBUTES"><code>LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "truck"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>fuelStation</code> - <p>Fuel station details. It is available only if a place is a fuel station and contain fuel data.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration.feature#FUEL_STATION_ATTRIBUTES"><code>LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 </p><p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 </p><p>For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "fuel"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>foodTypes</code> - <p>The list of food types assigned to this place.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p></dd>
<dd><code>payment</code> - <p>Details about the payment options at the POI.
 Set to <code>null</code> if the place is not a POI or if payment details are not available.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>evChargingLocation</code> - <p>Details about the EV charging station, if this place belongs to the EV charging station category.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrimaryCategories()">
<h3>getPrimaryCategories</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</span> <span class="element-name">getPrimaryCategories</span>()</div>
<div class="block"><p>Gets the list of primary categories assigned to this place.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>List of categories.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>

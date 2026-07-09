---
title: "Details (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-details"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Details.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.search.Details</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Details</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Contains details of a specific place, such as contact information,
 opening hours and assigned categories.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#categories">categories</a></code></div>
<div className="col-last even-row-color">
<div className="block">The list of categories assigned to this place.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#contacts">contacts</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The list of contact information of the place.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#editorials">editorials</a></code></div>
<div className="col-last even-row-color">
<div className="block">The list of editorials associated with the place.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocation" title="class in com.here.sdk.search">EVChargingLocation</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#evChargingLocation">evChargingLocation</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Details about the EV charging station, if this place belongs to the EV charging station category.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#evChargingPool">evChargingPool</a></code></div>
<div className="col-last even-row-color">
<div className="block">EV charging pool details.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#foodTypes">foodTypes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The list of food types assigned to this place.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search">FuelStation</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#fuelStation">fuelStation</a></code></div>
<div className="col-last even-row-color">
<div className="block">Fuel station details.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#images">images</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The list of images associated with the place.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#openingHours">openingHours</a></code></div>
<div className="col-last even-row-color">
<div className="block">The list of opening hours information of the place.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-poipaymentdetails" title="class in com.here.sdk.search">POIPaymentDetails</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#payment">payment</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Details about the payment options at the POI.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#ratings">ratings</a></code></div>
<div className="col-last even-row-color">
<div className="block">The list of ratings associated with the place.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#references">references</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The list of supplier references to this place.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-search-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#truckAmenities">truckAmenities</a></code></div>
<div className="col-last even-row-color">
<div className="block">Additional information that is available only for places that contain truck amenities.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List)">Details</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool)">Details</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 <a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities)">Details</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 <a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 <a href="sdk-for-android-navigate-com-here-sdk-search-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation)">Details</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 <a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 <a href="sdk-for-android-navigate-com-here-sdk-search-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List)">Details</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 <a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 <a href="sdk-for-android-navigate-com-here-sdk-search-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt; foodTypes)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List,com.here.sdk.search.POIPaymentDetails)">Details</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 <a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 <a href="sdk-for-android-navigate-com-here-sdk-search-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt; foodTypes,
 <a href="sdk-for-android-navigate-com-here-sdk-search-poipaymentdetails" title="class in com.here.sdk.search">POIPaymentDetails</a> payment)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-details#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List,com.here.sdk.search.POIPaymentDetails,com.here.sdk.search.EVChargingLocation)">Details</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 <a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 <a href="sdk-for-android-navigate-com-here-sdk-search-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt; foodTypes,
 <a href="sdk-for-android-navigate-com-here-sdk-search-poipaymentdetails" title="class in com.here.sdk.search">POIPaymentDetails</a> payment,
 <a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocation" title="class in com.here.sdk.search">EVChargingLocation</a> evChargingLocation)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="contacts">
<h3>contacts</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt;</span> <span className="element-name">contacts</span></div>
<div className="block"><p>The list of contact information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></div>
</section>
</li>
<li>
<section className="detail" id="openingHours">
<h3>openingHours</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt;</span> <span className="element-name">openingHours</span></div>
<div className="block"><p>The list of opening hours information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></div>
</section>
</li>
<li>
<section className="detail" id="categories">
<h3>categories</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</span> <span className="element-name">categories</span></div>
<div className="block"><p>The list of categories assigned to this place.</p></div>
</section>
</li>
<li>
<section className="detail" id="images">
<h3>images</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt;</span> <span className="element-name">images</span></div>
<div className="block"><p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></div>
</section>
</li>
<li>
<section className="detail" id="editorials">
<h3>editorials</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt;</span> <span className="element-name">editorials</span></div>
<div className="block"><p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></div>
</section>
</li>
<li>
<section className="detail" id="ratings">
<h3>ratings</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt;</span> <span className="element-name">ratings</span></div>
<div className="block"><p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></div>
</section>
</li>
<li>
<section className="detail" id="references">
<h3>references</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt;</span> <span className="element-name">references</span></div>
<div className="block"><p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></div>
</section>
</li>
<li>
<section className="detail" id="evChargingPool">
<h3>evChargingPool</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a></span> <span className="element-name">evChargingPool</span></div>
<div className="block"><p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 For online search, this feature is only available if it is explicitly enabled.
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
<section className="detail" id="truckAmenities">
<h3>truckAmenities</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a></span> <span className="element-name">truckAmenities</span></div>
<div className="block"><p>Additional information that is available only for places that contain truck amenities.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES"><code>LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 <strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "truck"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section className="detail" id="fuelStation">
<h3>fuelStation</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search">FuelStation</a></span> <span className="element-name">fuelStation</span></div>
<div className="block"><p>Fuel station details. It is available only if a place is a fuel station and contain fuel data.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#FUEL_STATION_ATTRIBUTES"><code>LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 <strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "fuel"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section className="detail" id="foodTypes">
<h3>foodTypes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt;</span> <span className="element-name">foodTypes</span></div>
<div className="block"><p>The list of food types assigned to this place.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p></div>
</section>
</li>
<li>
<section className="detail" id="payment">
<h3>payment</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-poipaymentdetails" title="class in com.here.sdk.search">POIPaymentDetails</a></span> <span className="element-name">payment</span></div>
<div className="block"><p>Details about the payment options at the POI.
 Set to <code>null</code> if the place is not a POI or if payment details are not available.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section className="detail" id="evChargingLocation">
<h3>evChargingLocation</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocation" title="class in com.here.sdk.search">EVChargingLocation</a></span> <span className="element-name">evChargingLocation</span></div>
<div className="block"><p>Details about the EV charging station, if this place belongs to the EV charging station category.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List)">
<h3>Details</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Details</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool)">
<h3>Details</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Details</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
<dd><code>evChargingPool</code> - <p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 For online search, this feature is only available if it is explicitly enabled.
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
<section className="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities)">
<h3>Details</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Details</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
<dd><code>evChargingPool</code> - <p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "browse.show"
 value: "ev"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show" and "browse.show".
 To enable fuel station details or truck amenities, the custom option value can be combined
 as "ev,truck", "ev,truck,fuel" etc.</p></dd>
<dd><code>truckAmenities</code> - <p>Additional information that is available only for places that contain truck amenities.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES"><code>LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 <strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "truck"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation)">
<h3>Details</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Details</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
<dd><code>evChargingPool</code> - <p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "browse.show"
 value: "ev"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show" and "browse.show".
 To enable fuel station details or truck amenities, the custom option value can be combined
 as "ev,truck", "ev,truck,fuel" etc.</p></dd>
<dd><code>truckAmenities</code> - <p>Additional information that is available only for places that contain truck amenities.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES"><code>LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 <strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "truck"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>fuelStation</code> - <p>Fuel station details. It is available only if a place is a fuel station and contain fuel data.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#FUEL_STATION_ATTRIBUTES"><code>LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 <strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "fuel"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List)">
<h3>Details</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Details</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt; foodTypes)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
<dd><code>evChargingPool</code> - <p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "browse.show"
 value: "ev"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show" and "browse.show".
 To enable fuel station details or truck amenities, the custom option value can be combined
 as "ev,truck", "ev,truck,fuel" etc.</p></dd>
<dd><code>truckAmenities</code> - <p>Additional information that is available only for places that contain truck amenities.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES"><code>LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 <strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "truck"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>fuelStation</code> - <p>Fuel station details. It is available only if a place is a fuel station and contain fuel data.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#FUEL_STATION_ATTRIBUTES"><code>LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 <strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "fuel"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>foodTypes</code> - <p>The list of food types assigned to this place.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List,com.here.sdk.search.POIPaymentDetails)">
<h3>Details</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Details</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt; foodTypes,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-poipaymentdetails" title="class in com.here.sdk.search">POIPaymentDetails</a> payment)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
<dd><code>evChargingPool</code> - <p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "browse.show"
 value: "ev"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show" and "browse.show".
 To enable fuel station details or truck amenities, the custom option value can be combined
 as "ev,truck", "ev,truck,fuel" etc.</p></dd>
<dd><code>truckAmenities</code> - <p>Additional information that is available only for places that contain truck amenities.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES"><code>LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 <strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "truck"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>fuelStation</code> - <p>Fuel station details. It is available only if a place is a fuel station and contain fuel data.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#FUEL_STATION_ATTRIBUTES"><code>LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 <strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "fuel"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>foodTypes</code> - <p>The list of food types assigned to this place.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p></dd>
<dd><code>payment</code> - <p>Details about the payment options at the POI.
 Set to <code>null</code> if the place is not a POI or if payment details are not available.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,java.util.List,com.here.sdk.search.EVChargingPool,com.here.sdk.search.TruckAmenities,com.here.sdk.search.FuelStation,java.util.List,com.here.sdk.search.POIPaymentDetails,com.here.sdk.search.EVChargingLocation)">
<h3>Details</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Details</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-contact" title="class in com.here.sdk.search">Contact</a>&gt; contacts,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-openinghours" title="class in com.here.sdk.search">OpeningHours</a>&gt; openingHours,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt; categories,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webimage" title="class in com.here.sdk.search">WebImage</a>&gt; images,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webeditorial" title="class in com.here.sdk.search">WebEditorial</a>&gt; editorials,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-webrating" title="class in com.here.sdk.search">WebRating</a>&gt; ratings,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-supplierreference" title="class in com.here.sdk.search">SupplierReference</a>&gt; references,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-evchargingpool" title="class in com.here.sdk.search">EVChargingPool</a> evChargingPool,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-truckamenities" title="class in com.here.sdk.search">TruckAmenities</a> truckAmenities,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-fuelstation" title="class in com.here.sdk.search">FuelStation</a> fuelStation,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>&gt; foodTypes,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-poipaymentdetails" title="class in com.here.sdk.search">POIPaymentDetails</a> payment,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-search-evcharginglocation" title="class in com.here.sdk.search">EVChargingLocation</a> evChargingLocation)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>contacts</code> - <p>The list of contact information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>openingHours</code> - <p>The list of opening hours information of the place.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>categories</code> - <p>The list of categories assigned to this place.</p></dd>
<dd><code>images</code> - <p>The list of images associated with the place.
 The images are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>editorials</code> - <p>The list of editorials associated with the place.
 The editorials are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>ratings</code> - <p>The list of ratings associated with the place.
 The ratings are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.
 <strong>Note:</strong> Not available as part of <a href="sdk-for-android-navigate-com-here-sdk-search-suggestion" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></dd>
<dd><code>references</code> - <p>The list of supplier references to this place.
 The references are provided by external suppliers and are only available to users with
 valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p></dd>
<dd><code>evChargingPool</code> - <p>EV charging pool details. It is available only for a place that is a charging pool
 for electric vehicles.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#EV"><code>LayerConfiguration.Feature.EV</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "browse.show"
 value: "ev"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show" and "browse.show".
 To enable fuel station details or truck amenities, the custom option value can be combined
 as "ev,truck", "ev,truck,fuel" etc.</p></dd>
<dd><code>truckAmenities</code> - <p>Additional information that is available only for places that contain truck amenities.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES"><code>LayerConfiguration.Feature.TRUCK_SERVICE_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 <strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "truck"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>fuelStation</code> - <p>Fuel station details. It is available only if a place is a fuel station and contain fuel data.
 It is fully supported for offline search, provided that <a href="sdk-for-android-navigate-layerconfiguration-feature#FUEL_STATION_ATTRIBUTES"><code>LayerConfiguration.Feature.FUEL_STATION_ATTRIBUTES</code></a>
 is enabled in <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.
 <strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
 only for selected customers. The field is always null for everyone that is not part of
 the closed-alpha group.
 Participants of the closed-alpha group can get access from HERE to use this feature.
 If the credentials are not enabled, a <a href="sdk-for-android-navigate-searcherror#FORBIDDEN"><code>SearchError.FORBIDDEN</code></a> will be propagated.
 For online search, this feature is only available if it is explicitly enabled.
 To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
 name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
 value: "fuel"
 To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
 "lookup.show", "discover.show", "autosuggest.show" and "browse.show".
 To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
 unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
<dd><code>foodTypes</code> - <p>The list of food types assigned to this place.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p></dd>
<dd><code>payment</code> - <p>Details about the payment options at the POI.
 Set to <code>null</code> if the place is not a POI or if payment details are not available.
 Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPrimaryCategories()">
<h3>getPrimaryCategories</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>&gt;</span> <span className="element-name">getPrimaryCategories</span>()</div>
<div className="block"><p>Gets the list of primary categories assigned to this place.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>

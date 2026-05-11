---
title: "PlaceCategory (API Reference)"
slug: "sdk-for-android-explore-placecategory"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PlaceCategory.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li><a href="#field-summary">Field</a> | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#field-detail">Field</a> | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.search</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.search.PlaceCategory</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">PlaceCategory</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Represents a category of place with different levels of granularity.
 This class also defines a set of most commonly used categories.</p></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACCOMMODATION">ACCOMMODATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Top level category for places offering lodging accommodations, dwellings or similar living quarters to travellers,
 such as hotels, motels, resorts, cruise ships and campgrounds.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ACCOMMODATION_HOTEL_MOTEL">ACCOMMODATION_HOTEL_MOTEL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A business that provides lodging or temporary living quarters.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACCOMMODATION_LODGING">ACCOMMODATION_LODGING</a></code></div>
<div class="col-last even-row-color">
<div class="block">A business that provides lodging to the public generally without room service.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#AREAS_AND_BUILDINGS">AREAS_AND_BUILDINGS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Top level category for places that are owned, operated or managed by municipalities,
 such as cities, towns, villages, boroughs and shires.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX">AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX</a></code></div>
<div class="col-last even-row-color">
<div class="block">Outdoor areas or complexes with designations for specific businesses or interests.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE">AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Areas and buildings designated for residential or office use.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_COMMERCIAL_SERVICES">BUSINESS_AND_COMMERCIAL_SERVICES</a></code></div>
<div class="col-last even-row-color">
<div class="block">Businesses that provide a service or product for use by other businesses.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_CONSUMER_SERVICES">BUSINESS_AND_CONSUMER_SERVICES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An organization that provides consumer services for a variety of products for used by the public.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES">BUSINESS_AND_SERVICES</a></code></div>
<div class="col-last even-row-color">
<div class="block">Top level category for places that provide professional services to other businesses,
 such as printing, photocopying, graphic design, marketing, advertising and other general business services.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_ATM">BUSINESS_AND_SERVICES_ATM</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A computer terminal that allows bank customers to deposit, withdraw, or transfer funds without the assistance of a bank teller.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_BANKING">BUSINESS_AND_SERVICES_BANKING</a></code></div>
<div class="col-last even-row-color">
<div class="block">Businesses that specialize in the maintenance, lending, exchange, or issuance of money.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_CAR_DEALER_SALES">BUSINESS_AND_SERVICES_CAR_DEALER_SALES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Businesses that sell new automobiles and motorcycles.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_CAR_RENTAL">BUSINESS_AND_SERVICES_CAR_RENTAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Businesses that rent or lease automobiles.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES">BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Businesses that provide automotive repair services.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA">BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA</a></code></div>
<div class="col-last even-row-color">
<div class="block">Businesses that provide communication services.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_EV_CHARGING_STATION">BUSINESS_AND_SERVICES_EV_CHARGING_STATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Businesses that provide recharging services for electric vehicles.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_FUELING_STATION">BUSINESS_AND_SERVICES_FUELING_STATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Businesses that sell fuel for vehicles, such as petrol, electricity etc.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_INDUSTRY">BUSINESS_AND_SERVICES_INDUSTRY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Businesses that employ people in and around the city in which it is located.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_MONEY_CASH">BUSINESS_AND_SERVICES_MONEY_CASH</a></code></div>
<div class="col-last even-row-color">
<div class="block">Businesses that provide money related services.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION">BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Businesses that sell fuel, oil, and other motoring supplies.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY">BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Municipal emergency services.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_POST_OFFICE">BUSINESS_AND_SERVICES_POST_OFFICE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An office or station that receives, sorts, dispatches and delivers mail to a specific area or region.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_TOURIST_INFORMATION">BUSINESS_AND_SERVICES_TOURIST_INFORMATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Businesses that provide a variety of information for visiting tourists,
 such as event schedules, lodging/accommodations, restaurants, attractions and more.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER">BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Business that sell or service trucks and tractor trailers.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EAT_AND_DRINK">EAT_AND_DRINK</a></code></div>
<div class="col-last even-row-color">
<div class="block">Top level category for places where food or beverages are prepared or served.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EAT_AND_DRINK_COFFEE_TEA">EAT_AND_DRINK_COFFEE_TEA</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An establishment that sells drinks, such as coffee and tea, as well as refreshments.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EAT_AND_DRINK_RESTAURANT">EAT_AND_DRINK_RESTAURANT</a></code></div>
<div class="col-last even-row-color">
<div class="block">An establishment that prepares and serves refreshments and prepared meals.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FACILITIES">FACILITIES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Top level category for places associated with specialized facilities,
 such as sports venues, government buildings, health care centers and other types of facilities.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FACILITIES_EDUCATION">FACILITIES_EDUCATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Facilities that are used for educational purposes including training, coaching, universities and more.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FACILITIES_EVENT_SPACES">FACILITIES_EVENT_SPACES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An area or facility used for the hosting of fairs and conventions.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FACILITIES_GOVERNMENT_COMMUNITTY">FACILITIES_GOVERNMENT_COMMUNITTY</a></code></div>
<div class="col-last even-row-color">
<div class="block">A Place where government services are provided.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FACILITIES_HOSPITAL_HEALTHCARE">FACILITIES_HOSPITAL_HEALTHCARE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Facilities that include dental offices, hospitals, nursing homes and other health care-related services.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FACILITIES_LIBRARY">FACILITIES_LIBRARY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Facilities that offer books, periodicals, audio, video and other material for public use.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FACILITIES_OTHER">FACILITIES_OTHER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Facilities with miscellaneous uses such as Clubhouses, Offices, and Registration Offices.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FACILITIES_PARKING">FACILITIES_PARKING</a></code></div>
<div class="col-last even-row-color">
<div class="block">Area or building used for parking cars.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FACILITIES_SCHOOL">FACILITIES_SCHOOL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Educational facilities that include primary schools, secondary schools and more.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FACILITIES_VENUE_SPORTS">FACILITIES_VENUE_SPORTS</a></code></div>
<div class="col-last even-row-color">
<div class="block">A facility used for individual and team sports including recreational sports.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GOING_OUT_CINEMA">GOING_OUT_CINEMA</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An establishment that shows movies through screen projection.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#GOING_OUT_ENTERTAINMENT">GOING_OUT_ENTERTAINMENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Top level category for places commonly associated with entertainment,
 such as bars, cinemas, theatres, casinos and night clubs.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GOING_OUT_GAMBLING_LOTTERY_BETTING">GOING_OUT_GAMBLING_LOTTERY_BETTING</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An establishment that provides gambling entertainment.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#GOING_OUT_NIGHTLIFE">GOING_OUT_NIGHTLIFE</a></code></div>
<div class="col-last even-row-color">
<div class="block">An establishment that provides evening entertainment and usually serves alcoholic beverages.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GOING_OUT_THEATRE_MUSIC_CULTURE">GOING_OUT_THEATRE_MUSIC_CULTURE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An establishment where various types of performing arts are presented.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LEISURE_AND_OUTDOOR">LEISURE_AND_OUTDOOR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Top level category for places that are designated for sports, recreation, parking, beaches
 and other leisure and outdoor activities.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LEISURE_OTHER">LEISURE_OTHER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A park that contains rides and/or other entertainment which may be based on a central theme.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LEISURE_OUTDOOR_RECREATION">LEISURE_OUTDOOR_RECREATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Public land preserved and maintained for recreational use.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NATURAL_AND_GEOGRAPHICAL">NATURAL_AND_GEOGRAPHICAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Top level category for natural or man-made areas of regional importance,
 such as bodies of water, mountains, forested areas and other geographic areas.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER">NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER</a></code></div>
<div class="col-last even-row-color">
<div class="block">A natural and geographical feature of the earth's surface that is covered with water, such as a lake, river, stream or ocean.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION">NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A dense growth of trees, open uncultivated land or other large masses of vegetation.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL">NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL</a></code></div>
<div class="col-last even-row-color">
<div class="block">A natural and geographical feature that is higher than the surrounding land.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NATURAL_AND_GEOGRAPHICAL_OTHER">NATURAL_AND_GEOGRAPHICAL_OTHER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A feature not classified as a Body of Water, Mountain or Hill, Undersea Feature, or Forest, Heath or Other Vegetation.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE">NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE</a></code></div>
<div class="col-last even-row-color">
<div class="block">A natural or artificial feature that is below sea level.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOPPING">SHOPPING</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Top level category for places where consumer goods are commonly sold,
 such as clothing stores, grocery stores, hardware stores and other types of shopping centers.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOPPING_BOOKSTORE">SHOPPING_BOOKSTORE</a></code></div>
<div class="col-last even-row-color">
<div class="block">A business that sells books, magazines and other reading material.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOPPING_CLOTHING_AND_ACCESORIES">SHOPPING_CLOTHING_AND_ACCESORIES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A business that sells apparel items, garments or fashion accessories for men, women, and children.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOPPING_CONSUMER_GOODS">SHOPPING_CONSUMER_GOODS</a></code></div>
<div class="col-last even-row-color">
<div class="block">A business that sells a variety of products targeted to consumers.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOPPING_CONVENIENCE_STORE">SHOPPING_CONVENIENCE_STORE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An establishment that sells groceries, candy, toiletries, soft drinks, tobacco products, newspapers and other products.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOPPING_DEPARTMENT_STORE">SHOPPING_DEPARTMENT_STORE</a></code></div>
<div class="col-last even-row-color">
<div class="block">A business that sells a wide variety of merchandise that is organized by product or service departments.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOPPING_DRUGSTORE_PHARMACY">SHOPPING_DRUGSTORE_PHARMACY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A business that sells medications, toiletry items and other retail cosmetics.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOPPING_ELECTRONICS">SHOPPING_ELECTRONICS</a></code></div>
<div class="col-last even-row-color">
<div class="block">A business that sells consumer electronics and electronic entertainment equipment.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOPPING_FOOD_AND_DRINK">SHOPPING_FOOD_AND_DRINK</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A business that sells specialty products of a particular type of food or beverage.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOPPING_HAIR_AND_BEAUTY">SHOPPING_HAIR_AND_BEAUTY</a></code></div>
<div class="col-last even-row-color">
<div class="block">A business that provides hair styling and personal appearance services.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHOPPING_HARDWARE_HOUSE_GARDEN">SHOPPING_HARDWARE_HOUSE_GARDEN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A business that sells crafts, gardening, remodeling, or decorating items for the home.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHOPPING_MALL_COMPLEX">SHOPPING_MALL_COMPLEX</a></code></div>
<div class="col-last even-row-color">
<div class="block">A complex of businesses that are co-located and share common services.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SIGHTS_AND_MUSEUMS">SIGHTS_AND_MUSEUMS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Top level category for places of special interest,
 such as common tourist attractions, museums and places of worship.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SIGHTS_LANDMARK_ATTRACTION">SIGHTS_LANDMARK_ATTRACTION</a></code></div>
<div class="col-last even-row-color">
<div class="block">A designated area of special interest to tourists.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SIGHTS_MUSEUM">SIGHTS_MUSEUM</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An establishment dedicated to the preservation and exhibition of artistic, historical, or scientific artifacts.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SIGHTS_RELIGIOUS_PLACE">SIGHTS_RELIGIOUS_PLACE</a></code></div>
<div class="col-last even-row-color">
<div class="block">An establishment special religious significance or where religious services are held.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TRANSPORT">TRANSPORT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Top level category for places commonly associated with pedestrian and cargo transport facilities,
 including airports, rail yards and seaports.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TRANSPORT_AIRPORT">TRANSPORT_AIRPORT</a></code></div>
<div class="col-last even-row-color">
<div class="block">A designated area that serves various aspects of aviation related sports, including gliders, recreational aircraft and model airplanes.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TRANSPORT_CARGO">TRANSPORT_CARGO</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A facility that handles some aspect of the transportation of cargo freight.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TRANSPORT_PUBLIC">TRANSPORT_PUBLIC</a></code></div>
<div class="col-last even-row-color">
<div class="block">A facility for travelers who are travelling between stops on public transport.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TRANSPORT_REST_AREA">TRANSPORT_REST_AREA</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An establishment along a motorway (controlled access road) that provides restrooms and parking.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">PlaceCategory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getId()">getId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the place category ID.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the localised place category name.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="EAT_AND_DRINK">
<h3>EAT_AND_DRINK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EAT_AND_DRINK</span></div>
<div class="block"><p>Top level category for places where food or beverages are prepared or served.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.EAT_AND_DRINK">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EAT_AND_DRINK_RESTAURANT">
<h3>EAT_AND_DRINK_RESTAURANT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EAT_AND_DRINK_RESTAURANT</span></div>
<div class="block"><p>An establishment that prepares and serves refreshments and prepared meals.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.EAT_AND_DRINK_RESTAURANT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EAT_AND_DRINK_COFFEE_TEA">
<h3>EAT_AND_DRINK_COFFEE_TEA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EAT_AND_DRINK_COFFEE_TEA</span></div>
<div class="block"><p>An establishment that sells drinks, such as coffee and tea, as well as refreshments.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.EAT_AND_DRINK_COFFEE_TEA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GOING_OUT_ENTERTAINMENT">
<h3>GOING_OUT_ENTERTAINMENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">GOING_OUT_ENTERTAINMENT</span></div>
<div class="block"><p>Top level category for places commonly associated with entertainment,
 such as bars, cinemas, theatres, casinos and night clubs.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_ENTERTAINMENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GOING_OUT_NIGHTLIFE">
<h3>GOING_OUT_NIGHTLIFE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">GOING_OUT_NIGHTLIFE</span></div>
<div class="block"><p>An establishment that provides evening entertainment and usually serves alcoholic beverages.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_NIGHTLIFE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GOING_OUT_CINEMA">
<h3>GOING_OUT_CINEMA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">GOING_OUT_CINEMA</span></div>
<div class="block"><p>An establishment that shows movies through screen projection.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_CINEMA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GOING_OUT_THEATRE_MUSIC_CULTURE">
<h3>GOING_OUT_THEATRE_MUSIC_CULTURE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">GOING_OUT_THEATRE_MUSIC_CULTURE</span></div>
<div class="block"><p>An establishment where various types of performing arts are presented.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_THEATRE_MUSIC_CULTURE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GOING_OUT_GAMBLING_LOTTERY_BETTING">
<h3>GOING_OUT_GAMBLING_LOTTERY_BETTING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">GOING_OUT_GAMBLING_LOTTERY_BETTING</span></div>
<div class="block"><p>An establishment that provides gambling entertainment.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_GAMBLING_LOTTERY_BETTING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SIGHTS_AND_MUSEUMS">
<h3>SIGHTS_AND_MUSEUMS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SIGHTS_AND_MUSEUMS</span></div>
<div class="block"><p>Top level category for places of special interest,
 such as common tourist attractions, museums and places of worship.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SIGHTS_AND_MUSEUMS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SIGHTS_LANDMARK_ATTRACTION">
<h3>SIGHTS_LANDMARK_ATTRACTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SIGHTS_LANDMARK_ATTRACTION</span></div>
<div class="block"><p>A designated area of special interest to tourists.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SIGHTS_LANDMARK_ATTRACTION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SIGHTS_MUSEUM">
<h3>SIGHTS_MUSEUM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SIGHTS_MUSEUM</span></div>
<div class="block"><p>An establishment dedicated to the preservation and exhibition of artistic, historical, or scientific artifacts.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SIGHTS_MUSEUM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SIGHTS_RELIGIOUS_PLACE">
<h3>SIGHTS_RELIGIOUS_PLACE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SIGHTS_RELIGIOUS_PLACE</span></div>
<div class="block"><p>An establishment special religious significance or where religious services are held.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SIGHTS_RELIGIOUS_PLACE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NATURAL_AND_GEOGRAPHICAL">
<h3>NATURAL_AND_GEOGRAPHICAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NATURAL_AND_GEOGRAPHICAL</span></div>
<div class="block"><p>Top level category for natural or man-made areas of regional importance,
 such as bodies of water, mountains, forested areas and other geographic areas.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER">
<h3>NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER</span></div>
<div class="block"><p>A natural and geographical feature of the earth's surface that is covered with water, such as a lake, river, stream or ocean.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL">
<h3>NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL</span></div>
<div class="block"><p>A natural and geographical feature that is higher than the surrounding land.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE">
<h3>NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE</span></div>
<div class="block"><p>A natural or artificial feature that is below sea level.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION">
<h3>NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION</span></div>
<div class="block"><p>A dense growth of trees, open uncultivated land or other large masses of vegetation.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NATURAL_AND_GEOGRAPHICAL_OTHER">
<h3>NATURAL_AND_GEOGRAPHICAL_OTHER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NATURAL_AND_GEOGRAPHICAL_OTHER</span></div>
<div class="block"><p>A feature not classified as a Body of Water, Mountain or Hill, Undersea Feature, or Forest, Heath or Other Vegetation.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_OTHER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRANSPORT">
<h3>TRANSPORT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRANSPORT</span></div>
<div class="block"><p>Top level category for places commonly associated with pedestrian and cargo transport facilities,
 including airports, rail yards and seaports.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.TRANSPORT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRANSPORT_AIRPORT">
<h3>TRANSPORT_AIRPORT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRANSPORT_AIRPORT</span></div>
<div class="block"><p>A designated area that serves various aspects of aviation related sports, including gliders, recreational aircraft and model airplanes.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.TRANSPORT_AIRPORT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRANSPORT_PUBLIC">
<h3>TRANSPORT_PUBLIC</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRANSPORT_PUBLIC</span></div>
<div class="block"><p>A facility for travelers who are travelling between stops on public transport.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.TRANSPORT_PUBLIC">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRANSPORT_CARGO">
<h3>TRANSPORT_CARGO</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRANSPORT_CARGO</span></div>
<div class="block"><p>A facility that handles some aspect of the transportation of cargo freight.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.TRANSPORT_CARGO">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRANSPORT_REST_AREA">
<h3>TRANSPORT_REST_AREA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRANSPORT_REST_AREA</span></div>
<div class="block"><p>An establishment along a motorway (controlled access road) that provides restrooms and parking.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.TRANSPORT_REST_AREA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACCOMMODATION">
<h3>ACCOMMODATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACCOMMODATION</span></div>
<div class="block"><p>Top level category for places offering lodging accommodations, dwellings or similar living quarters to travellers,
 such as hotels, motels, resorts, cruise ships and campgrounds.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.ACCOMMODATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACCOMMODATION_HOTEL_MOTEL">
<h3>ACCOMMODATION_HOTEL_MOTEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACCOMMODATION_HOTEL_MOTEL</span></div>
<div class="block"><p>A business that provides lodging or temporary living quarters.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.ACCOMMODATION_HOTEL_MOTEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACCOMMODATION_LODGING">
<h3>ACCOMMODATION_LODGING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACCOMMODATION_LODGING</span></div>
<div class="block"><p>A business that provides lodging to the public generally without room service.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.ACCOMMODATION_LODGING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LEISURE_AND_OUTDOOR">
<h3>LEISURE_AND_OUTDOOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LEISURE_AND_OUTDOOR</span></div>
<div class="block"><p>Top level category for places that are designated for sports, recreation, parking, beaches
 and other leisure and outdoor activities.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.LEISURE_AND_OUTDOOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LEISURE_OUTDOOR_RECREATION">
<h3>LEISURE_OUTDOOR_RECREATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LEISURE_OUTDOOR_RECREATION</span></div>
<div class="block"><p>Public land preserved and maintained for recreational use.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.LEISURE_OUTDOOR_RECREATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LEISURE_OTHER">
<h3>LEISURE_OTHER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LEISURE_OTHER</span></div>
<div class="block"><p>A park that contains rides and/or other entertainment which may be based on a central theme.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.LEISURE_OTHER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOPPING">
<h3>SHOPPING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOPPING</span></div>
<div class="block"><p>Top level category for places where consumer goods are commonly sold,
 such as clothing stores, grocery stores, hardware stores and other types of shopping centers.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOPPING_CONVENIENCE_STORE">
<h3>SHOPPING_CONVENIENCE_STORE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOPPING_CONVENIENCE_STORE</span></div>
<div class="block"><p>An establishment that sells groceries, candy, toiletries, soft drinks, tobacco products, newspapers and other products.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_CONVENIENCE_STORE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOPPING_MALL_COMPLEX">
<h3>SHOPPING_MALL_COMPLEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOPPING_MALL_COMPLEX</span></div>
<div class="block"><p>A complex of businesses that are co-located and share common services.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_MALL_COMPLEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOPPING_DEPARTMENT_STORE">
<h3>SHOPPING_DEPARTMENT_STORE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOPPING_DEPARTMENT_STORE</span></div>
<div class="block"><p>A business that sells a wide variety of merchandise that is organized by product or service departments.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_DEPARTMENT_STORE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOPPING_FOOD_AND_DRINK">
<h3>SHOPPING_FOOD_AND_DRINK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOPPING_FOOD_AND_DRINK</span></div>
<div class="block"><p>A business that sells specialty products of a particular type of food or beverage.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_FOOD_AND_DRINK">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOPPING_DRUGSTORE_PHARMACY">
<h3>SHOPPING_DRUGSTORE_PHARMACY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOPPING_DRUGSTORE_PHARMACY</span></div>
<div class="block"><p>A business that sells medications, toiletry items and other retail cosmetics.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_DRUGSTORE_PHARMACY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOPPING_ELECTRONICS">
<h3>SHOPPING_ELECTRONICS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOPPING_ELECTRONICS</span></div>
<div class="block"><p>A business that sells consumer electronics and electronic entertainment equipment.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_ELECTRONICS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOPPING_HARDWARE_HOUSE_GARDEN">
<h3>SHOPPING_HARDWARE_HOUSE_GARDEN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOPPING_HARDWARE_HOUSE_GARDEN</span></div>
<div class="block"><p>A business that sells crafts, gardening, remodeling, or decorating items for the home.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_HARDWARE_HOUSE_GARDEN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOPPING_BOOKSTORE">
<h3>SHOPPING_BOOKSTORE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOPPING_BOOKSTORE</span></div>
<div class="block"><p>A business that sells books, magazines and other reading material.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_BOOKSTORE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOPPING_CLOTHING_AND_ACCESORIES">
<h3>SHOPPING_CLOTHING_AND_ACCESORIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOPPING_CLOTHING_AND_ACCESORIES</span></div>
<div class="block"><p>A business that sells apparel items, garments or fashion accessories for men, women, and children.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_CLOTHING_AND_ACCESORIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOPPING_CONSUMER_GOODS">
<h3>SHOPPING_CONSUMER_GOODS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOPPING_CONSUMER_GOODS</span></div>
<div class="block"><p>A business that sells a variety of products targeted to consumers.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_CONSUMER_GOODS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHOPPING_HAIR_AND_BEAUTY">
<h3>SHOPPING_HAIR_AND_BEAUTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHOPPING_HAIR_AND_BEAUTY</span></div>
<div class="block"><p>A business that provides hair styling and personal appearance services.
 Places in this category may also sell hair products and other related cosmetic items.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_HAIR_AND_BEAUTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES">
<h3>BUSINESS_AND_SERVICES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES</span></div>
<div class="block"><p>Top level category for places that provide professional services to other businesses,
 such as printing, photocopying, graphic design, marketing, advertising and other general business services.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_BANKING">
<h3>BUSINESS_AND_SERVICES_BANKING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_BANKING</span></div>
<div class="block"><p>Businesses that specialize in the maintenance, lending, exchange, or issuance of money.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_BANKING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_ATM">
<h3>BUSINESS_AND_SERVICES_ATM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_ATM</span></div>
<div class="block"><p>A computer terminal that allows bank customers to deposit, withdraw, or transfer funds without the assistance of a bank teller.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_ATM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_MONEY_CASH">
<h3>BUSINESS_AND_SERVICES_MONEY_CASH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_MONEY_CASH</span></div>
<div class="block"><p>Businesses that provide money related services.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_MONEY_CASH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA">
<h3>BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA</span></div>
<div class="block"><p>Businesses that provide communication services.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_COMMERCIAL_SERVICES">
<h3>BUSINESS_AND_COMMERCIAL_SERVICES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_COMMERCIAL_SERVICES</span></div>
<div class="block"><p>Businesses that provide a service or product for use by other businesses.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_COMMERCIAL_SERVICES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_INDUSTRY">
<h3>BUSINESS_AND_SERVICES_INDUSTRY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_INDUSTRY</span></div>
<div class="block"><p>Businesses that employ people in and around the city in which it is located.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_INDUSTRY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY">
<h3>BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY</span></div>
<div class="block"><p>Municipal emergency services.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_CONSUMER_SERVICES">
<h3>BUSINESS_AND_CONSUMER_SERVICES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_CONSUMER_SERVICES</span></div>
<div class="block"><p>An organization that provides consumer services for a variety of products for used by the public.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_CONSUMER_SERVICES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_POST_OFFICE">
<h3>BUSINESS_AND_SERVICES_POST_OFFICE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_POST_OFFICE</span></div>
<div class="block"><p>An office or station that receives, sorts, dispatches and delivers mail to a specific area or region.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_POST_OFFICE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_TOURIST_INFORMATION">
<h3>BUSINESS_AND_SERVICES_TOURIST_INFORMATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_TOURIST_INFORMATION</span></div>
<div class="block"><p>Businesses that provide a variety of information for visiting tourists,
 such as event schedules, lodging/accommodations, restaurants, attractions and more.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_TOURIST_INFORMATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_FUELING_STATION">
<h3>BUSINESS_AND_SERVICES_FUELING_STATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_FUELING_STATION</span></div>
<div class="block"><p>Businesses that sell fuel for vehicles, such as petrol, electricity etc.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_FUELING_STATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION">
<h3>BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION</span></div>
<div class="block"><p>Businesses that sell fuel, oil, and other motoring supplies.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_EV_CHARGING_STATION">
<h3>BUSINESS_AND_SERVICES_EV_CHARGING_STATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_EV_CHARGING_STATION</span></div>
<div class="block"><p>Businesses that provide recharging services for electric vehicles.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_EV_CHARGING_STATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_CAR_DEALER_SALES">
<h3>BUSINESS_AND_SERVICES_CAR_DEALER_SALES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_CAR_DEALER_SALES</span></div>
<div class="block"><p>Businesses that sell new automobiles and motorcycles.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_CAR_DEALER_SALES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES">
<h3>BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES</span></div>
<div class="block"><p>Businesses that provide automotive repair services.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_CAR_RENTAL">
<h3>BUSINESS_AND_SERVICES_CAR_RENTAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_CAR_RENTAL</span></div>
<div class="block"><p>Businesses that rent or lease automobiles.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_CAR_RENTAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER">
<h3>BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER</span></div>
<div class="block"><p>Business that sell or service trucks and tractor trailers.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FACILITIES">
<h3>FACILITIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FACILITIES</span></div>
<div class="block"><p>Top level category for places associated with specialized facilities,
 such as sports venues, government buildings, health care centers and other types of facilities.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FACILITIES_HOSPITAL_HEALTHCARE">
<h3>FACILITIES_HOSPITAL_HEALTHCARE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FACILITIES_HOSPITAL_HEALTHCARE</span></div>
<div class="block"><p>Facilities that include dental offices, hospitals, nursing homes and other health care-related services.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_HOSPITAL_HEALTHCARE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FACILITIES_GOVERNMENT_COMMUNITTY">
<h3>FACILITIES_GOVERNMENT_COMMUNITTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FACILITIES_GOVERNMENT_COMMUNITTY</span></div>
<div class="block"><p>A Place where government services are provided.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_GOVERNMENT_COMMUNITTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FACILITIES_EDUCATION">
<h3>FACILITIES_EDUCATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FACILITIES_EDUCATION</span></div>
<div class="block"><p>Facilities that are used for educational purposes including training, coaching, universities and more.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_EDUCATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FACILITIES_SCHOOL">
<h3>FACILITIES_SCHOOL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FACILITIES_SCHOOL</span></div>
<div class="block"><p>Educational facilities that include primary schools, secondary schools and more.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_SCHOOL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FACILITIES_LIBRARY">
<h3>FACILITIES_LIBRARY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FACILITIES_LIBRARY</span></div>
<div class="block"><p>Facilities that offer books, periodicals, audio, video and other material for public use.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_LIBRARY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FACILITIES_EVENT_SPACES">
<h3>FACILITIES_EVENT_SPACES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FACILITIES_EVENT_SPACES</span></div>
<div class="block"><p>An area or facility used for the hosting of fairs and conventions.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_EVENT_SPACES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FACILITIES_PARKING">
<h3>FACILITIES_PARKING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FACILITIES_PARKING</span></div>
<div class="block"><p>Area or building used for parking cars.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_PARKING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FACILITIES_VENUE_SPORTS">
<h3>FACILITIES_VENUE_SPORTS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FACILITIES_VENUE_SPORTS</span></div>
<div class="block"><p>A facility used for individual and team sports including recreational sports.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_VENUE_SPORTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FACILITIES_OTHER">
<h3>FACILITIES_OTHER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FACILITIES_OTHER</span></div>
<div class="block"><p>Facilities with miscellaneous uses such as Clubhouses, Offices, and Registration Offices.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_OTHER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AREAS_AND_BUILDINGS">
<h3>AREAS_AND_BUILDINGS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AREAS_AND_BUILDINGS</span></div>
<div class="block"><p>Top level category for places that are owned, operated or managed by municipalities,
 such as cities, towns, villages, boroughs and shires.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.AREAS_AND_BUILDINGS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX">
<h3>AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX</span></div>
<div class="block"><p>Outdoor areas or complexes with designations for specific businesses or interests.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE">
<h3>AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE</span></div>
<div class="block"><p>Areas and buildings designated for residential or office use.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.search.PlaceCategory.AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
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
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>PlaceCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PlaceCategory</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - <p>Place category ID.
     The HERE places category system provides three levels of granularity:
     <ol>
<li>Level 1 represents high level groupings, such as "Eat and drink".
     Their IDs take the form "xxx", for example "100".</li>
<li>Level 2 represents logical sub-groups or domains, such as "Eat and Drink / Restaurant".
     Their IDs take the form "xxx-xxxx", for example "100-1000".</li>
<li>Level 3 provides the greatest level of granularity about place categorization,
     such as "Eat and Drink / Restaurant / Casual Dining".
     Their IDs take the form "xxx-xxxx-xxxx", for example "100-1000-0001".
     The category ID can be provided as one of the predefined values, such as
     <a href="#EAT_AND_DRINK_RESTAURANT"><code>EAT_AND_DRINK_RESTAURANT</code></a> or as a literal string that matches
     one of the category IDs defined by the HERE Search service.
     Only level 1 and 2 category IDs are predefined.
     The complete list of supported category IDs, including level 3, can be found online:
     https://www.here.com/docs/bundle/geocoding-and-search-api-v7-api-reference/page/index.html.</li>
</ol></p></dd>
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
<section class="detail" id="getId()">
<h3>getId</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()</div>
<div class="block"><p>Gets the place category ID.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Place category ID.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block"><p>Gets the localised place category name.
 <p>It is available only when when <code>PlaceCategory</code> is obtained from <code>Place</code>.
 That means that when <code>PlaceCategory</code> is constructed directly by the client,
 <code>name</code> is always <code>null</code>.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Localised place category name.</p></dd>
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
</div>
</body>
</html>

</div>
`
}</HTMLBlock>

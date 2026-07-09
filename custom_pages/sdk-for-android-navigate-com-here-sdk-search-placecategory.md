---
title: "PlaceCategory (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-placecategory"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PlaceCategory.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.search.PlaceCategory</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">PlaceCategory</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents a category of place with different levels of granularity.
 This class also defines a set of most commonly used categories.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#ACCOMMODATION">ACCOMMODATION</a></code></div>
<div className="col-last even-row-color">
<div className="block">Top level category for places offering lodging accommodations, dwellings or similar living quarters to travellers,
 such as hotels, motels, resorts, cruise ships and campgrounds.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#ACCOMMODATION_HOTEL_MOTEL">ACCOMMODATION_HOTEL_MOTEL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A business that provides lodging or temporary living quarters.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#ACCOMMODATION_LODGING">ACCOMMODATION_LODGING</a></code></div>
<div className="col-last even-row-color">
<div className="block">A business that provides lodging to the public generally without room service.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#AREAS_AND_BUILDINGS">AREAS_AND_BUILDINGS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Top level category for places that are owned, operated or managed by municipalities,
 such as cities, towns, villages, boroughs and shires.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX">AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX</a></code></div>
<div className="col-last even-row-color">
<div className="block">Outdoor areas or complexes with designations for specific businesses or interests.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE">AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Areas and buildings designated for residential or office use.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_COMMERCIAL_SERVICES">BUSINESS_AND_COMMERCIAL_SERVICES</a></code></div>
<div className="col-last even-row-color">
<div className="block">Businesses that provide a service or product for use by other businesses.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_CONSUMER_SERVICES">BUSINESS_AND_CONSUMER_SERVICES</a></code></div>
<div className="col-last odd-row-color">
<div className="block">An organization that provides consumer services for a variety of products for used by the public.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES">BUSINESS_AND_SERVICES</a></code></div>
<div className="col-last even-row-color">
<div className="block">Top level category for places that provide professional services to other businesses,
 such as printing, photocopying, graphic design, marketing, advertising and other general business services.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_ATM">BUSINESS_AND_SERVICES_ATM</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A computer terminal that allows bank customers to deposit, withdraw, or transfer funds without the assistance of a bank teller.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_BANKING">BUSINESS_AND_SERVICES_BANKING</a></code></div>
<div className="col-last even-row-color">
<div className="block">Businesses that specialize in the maintenance, lending, exchange, or issuance of money.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_CAR_DEALER_SALES">BUSINESS_AND_SERVICES_CAR_DEALER_SALES</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Businesses that sell new automobiles and motorcycles.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_CAR_RENTAL">BUSINESS_AND_SERVICES_CAR_RENTAL</a></code></div>
<div className="col-last even-row-color">
<div className="block">Businesses that rent or lease automobiles.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES">BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Businesses that provide automotive repair services.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA">BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA</a></code></div>
<div className="col-last even-row-color">
<div className="block">Businesses that provide communication services.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_EV_CHARGING_STATION">BUSINESS_AND_SERVICES_EV_CHARGING_STATION</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Businesses that provide recharging services for electric vehicles.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_FUELING_STATION">BUSINESS_AND_SERVICES_FUELING_STATION</a></code></div>
<div className="col-last even-row-color">
<div className="block">Businesses that sell fuel for vehicles, such as petrol, electricity etc.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_INDUSTRY">BUSINESS_AND_SERVICES_INDUSTRY</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Businesses that employ people in and around the city in which it is located.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_MONEY_CASH">BUSINESS_AND_SERVICES_MONEY_CASH</a></code></div>
<div className="col-last even-row-color">
<div className="block">Businesses that provide money related services.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION">BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Businesses that sell fuel, oil, and other motoring supplies.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY">BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY</a></code></div>
<div className="col-last even-row-color">
<div className="block">Municipal emergency services.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_POST_OFFICE">BUSINESS_AND_SERVICES_POST_OFFICE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">An office or station that receives, sorts, dispatches and delivers mail to a specific area or region.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_TOURIST_INFORMATION">BUSINESS_AND_SERVICES_TOURIST_INFORMATION</a></code></div>
<div className="col-last even-row-color">
<div className="block">Businesses that provide a variety of information for visiting tourists,
 such as event schedules, lodging/accommodations, restaurants, attractions and more.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER">BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Business that sell or service trucks and tractor trailers.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#EAT_AND_DRINK">EAT_AND_DRINK</a></code></div>
<div className="col-last even-row-color">
<div className="block">Top level category for places where food or beverages are prepared or served.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#EAT_AND_DRINK_COFFEE_TEA">EAT_AND_DRINK_COFFEE_TEA</a></code></div>
<div className="col-last odd-row-color">
<div className="block">An establishment that sells drinks, such as coffee and tea, as well as refreshments.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#EAT_AND_DRINK_RESTAURANT">EAT_AND_DRINK_RESTAURANT</a></code></div>
<div className="col-last even-row-color">
<div className="block">An establishment that prepares and serves refreshments and prepared meals.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#FACILITIES">FACILITIES</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Top level category for places associated with specialized facilities,
 such as sports venues, government buildings, health care centers and other types of facilities.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#FACILITIES_EDUCATION">FACILITIES_EDUCATION</a></code></div>
<div className="col-last even-row-color">
<div className="block">Facilities that are used for educational purposes including training, coaching, universities and more.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#FACILITIES_EVENT_SPACES">FACILITIES_EVENT_SPACES</a></code></div>
<div className="col-last odd-row-color">
<div className="block">An area or facility used for the hosting of fairs and conventions.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#FACILITIES_GOVERNMENT_COMMUNITTY">FACILITIES_GOVERNMENT_COMMUNITTY</a></code></div>
<div className="col-last even-row-color">
<div className="block">A Place where government services are provided.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#FACILITIES_HOSPITAL_HEALTHCARE">FACILITIES_HOSPITAL_HEALTHCARE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Facilities that include dental offices, hospitals, nursing homes and other health care-related services.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#FACILITIES_LIBRARY">FACILITIES_LIBRARY</a></code></div>
<div className="col-last even-row-color">
<div className="block">Facilities that offer books, periodicals, audio, video and other material for public use.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#FACILITIES_OTHER">FACILITIES_OTHER</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Facilities with miscellaneous uses such as Clubhouses, Offices, and Registration Offices.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#FACILITIES_PARKING">FACILITIES_PARKING</a></code></div>
<div className="col-last even-row-color">
<div className="block">Area or building used for parking cars.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#FACILITIES_SCHOOL">FACILITIES_SCHOOL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Educational facilities that include primary schools, secondary schools and more.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#FACILITIES_VENUE_SPORTS">FACILITIES_VENUE_SPORTS</a></code></div>
<div className="col-last even-row-color">
<div className="block">A facility used for individual and team sports including recreational sports.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#GOING_OUT_CINEMA">GOING_OUT_CINEMA</a></code></div>
<div className="col-last odd-row-color">
<div className="block">An establishment that shows movies through screen projection.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#GOING_OUT_ENTERTAINMENT">GOING_OUT_ENTERTAINMENT</a></code></div>
<div className="col-last even-row-color">
<div className="block">Top level category for places commonly associated with entertainment,
 such as bars, cinemas, theatres, casinos and night clubs.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#GOING_OUT_GAMBLING_LOTTERY_BETTING">GOING_OUT_GAMBLING_LOTTERY_BETTING</a></code></div>
<div className="col-last odd-row-color">
<div className="block">An establishment that provides gambling entertainment.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#GOING_OUT_NIGHTLIFE">GOING_OUT_NIGHTLIFE</a></code></div>
<div className="col-last even-row-color">
<div className="block">An establishment that provides evening entertainment and usually serves alcoholic beverages.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#GOING_OUT_THEATRE_MUSIC_CULTURE">GOING_OUT_THEATRE_MUSIC_CULTURE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">An establishment where various types of performing arts are presented.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#LEISURE_AND_OUTDOOR">LEISURE_AND_OUTDOOR</a></code></div>
<div className="col-last even-row-color">
<div className="block">Top level category for places that are designated for sports, recreation, parking, beaches
 and other leisure and outdoor activities.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#LEISURE_OTHER">LEISURE_OTHER</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A park that contains rides and/or other entertainment which may be based on a central theme.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#LEISURE_OUTDOOR_RECREATION">LEISURE_OUTDOOR_RECREATION</a></code></div>
<div className="col-last even-row-color">
<div className="block">Public land preserved and maintained for recreational use.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#NATURAL_AND_GEOGRAPHICAL">NATURAL_AND_GEOGRAPHICAL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Top level category for natural or man-made areas of regional importance,
 such as bodies of water, mountains, forested areas and other geographic areas.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER">NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER</a></code></div>
<div className="col-last even-row-color">
<div className="block">A natural and geographical feature of the earth's surface that is covered with water, such as a lake, river, stream or ocean.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION">NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A dense growth of trees, open uncultivated land or other large masses of vegetation.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL">NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL</a></code></div>
<div className="col-last even-row-color">
<div className="block">A natural and geographical feature that is higher than the surrounding land.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#NATURAL_AND_GEOGRAPHICAL_OTHER">NATURAL_AND_GEOGRAPHICAL_OTHER</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A feature not classified as a Body of Water, Mountain or Hill, Undersea Feature, or Forest, Heath or Other Vegetation.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE">NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE</a></code></div>
<div className="col-last even-row-color">
<div className="block">A natural or artificial feature that is below sea level.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SHOPPING">SHOPPING</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Top level category for places where consumer goods are commonly sold,
 such as clothing stores, grocery stores, hardware stores and other types of shopping centers.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SHOPPING_BOOKSTORE">SHOPPING_BOOKSTORE</a></code></div>
<div className="col-last even-row-color">
<div className="block">A business that sells books, magazines and other reading material.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SHOPPING_CLOTHING_AND_ACCESORIES">SHOPPING_CLOTHING_AND_ACCESORIES</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A business that sells apparel items, garments or fashion accessories for men, women, and children.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SHOPPING_CONSUMER_GOODS">SHOPPING_CONSUMER_GOODS</a></code></div>
<div className="col-last even-row-color">
<div className="block">A business that sells a variety of products targeted to consumers.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SHOPPING_CONVENIENCE_STORE">SHOPPING_CONVENIENCE_STORE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">An establishment that sells groceries, candy, toiletries, soft drinks, tobacco products, newspapers and other products.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SHOPPING_DEPARTMENT_STORE">SHOPPING_DEPARTMENT_STORE</a></code></div>
<div className="col-last even-row-color">
<div className="block">A business that sells a wide variety of merchandise that is organized by product or service departments.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SHOPPING_DRUGSTORE_PHARMACY">SHOPPING_DRUGSTORE_PHARMACY</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A business that sells medications, toiletry items and other retail cosmetics.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SHOPPING_ELECTRONICS">SHOPPING_ELECTRONICS</a></code></div>
<div className="col-last even-row-color">
<div className="block">A business that sells consumer electronics and electronic entertainment equipment.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SHOPPING_FOOD_AND_DRINK">SHOPPING_FOOD_AND_DRINK</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A business that sells specialty products of a particular type of food or beverage.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SHOPPING_HAIR_AND_BEAUTY">SHOPPING_HAIR_AND_BEAUTY</a></code></div>
<div className="col-last even-row-color">
<div className="block">A business that provides hair styling and personal appearance services.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SHOPPING_HARDWARE_HOUSE_GARDEN">SHOPPING_HARDWARE_HOUSE_GARDEN</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A business that sells crafts, gardening, remodeling, or decorating items for the home.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SHOPPING_MALL_COMPLEX">SHOPPING_MALL_COMPLEX</a></code></div>
<div className="col-last even-row-color">
<div className="block">A complex of businesses that are co-located and share common services.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SIGHTS_AND_MUSEUMS">SIGHTS_AND_MUSEUMS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Top level category for places of special interest,
 such as common tourist attractions, museums and places of worship.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SIGHTS_LANDMARK_ATTRACTION">SIGHTS_LANDMARK_ATTRACTION</a></code></div>
<div className="col-last even-row-color">
<div className="block">A designated area of special interest to tourists.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SIGHTS_MUSEUM">SIGHTS_MUSEUM</a></code></div>
<div className="col-last odd-row-color">
<div className="block">An establishment dedicated to the preservation and exhibition of artistic, historical, or scientific artifacts.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#SIGHTS_RELIGIOUS_PLACE">SIGHTS_RELIGIOUS_PLACE</a></code></div>
<div className="col-last even-row-color">
<div className="block">An establishment special religious significance or where religious services are held.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#TRANSPORT">TRANSPORT</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Top level category for places commonly associated with pedestrian and cargo transport facilities,
 including airports, rail yards and seaports.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#TRANSPORT_AIRPORT">TRANSPORT_AIRPORT</a></code></div>
<div className="col-last even-row-color">
<div className="block">A designated area that serves various aspects of aviation related sports, including gliders, recreational aircraft and model airplanes.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#TRANSPORT_CARGO">TRANSPORT_CARGO</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A facility that handles some aspect of the transportation of cargo freight.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#TRANSPORT_PUBLIC">TRANSPORT_PUBLIC</a></code></div>
<div className="col-last even-row-color">
<div className="block">A facility for travelers who are travelling between stops on public transport.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#TRANSPORT_REST_AREA">TRANSPORT_REST_AREA</a></code></div>
<div className="col-last odd-row-color">
<div className="block">An establishment along a motorway (controlled access road) that provides restrooms and parking.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-placecategory#%3Cinit%3E(java.lang.String)">PlaceCategory</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section className="detail" id="EAT_AND_DRINK">
<h3>EAT_AND_DRINK</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">EAT_AND_DRINK</span></div>
<div className="block"><p>Top level category for places where food or beverages are prepared or served.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.EAT_AND_DRINK">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="EAT_AND_DRINK_RESTAURANT">
<h3>EAT_AND_DRINK_RESTAURANT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">EAT_AND_DRINK_RESTAURANT</span></div>
<div className="block"><p>An establishment that prepares and serves refreshments and prepared meals.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.EAT_AND_DRINK_RESTAURANT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="EAT_AND_DRINK_COFFEE_TEA">
<h3>EAT_AND_DRINK_COFFEE_TEA</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">EAT_AND_DRINK_COFFEE_TEA</span></div>
<div className="block"><p>An establishment that sells drinks, such as coffee and tea, as well as refreshments.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.EAT_AND_DRINK_COFFEE_TEA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="GOING_OUT_ENTERTAINMENT">
<h3>GOING_OUT_ENTERTAINMENT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">GOING_OUT_ENTERTAINMENT</span></div>
<div className="block"><p>Top level category for places commonly associated with entertainment,
 such as bars, cinemas, theatres, casinos and night clubs.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_ENTERTAINMENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="GOING_OUT_NIGHTLIFE">
<h3>GOING_OUT_NIGHTLIFE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">GOING_OUT_NIGHTLIFE</span></div>
<div className="block"><p>An establishment that provides evening entertainment and usually serves alcoholic beverages.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_NIGHTLIFE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="GOING_OUT_CINEMA">
<h3>GOING_OUT_CINEMA</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">GOING_OUT_CINEMA</span></div>
<div className="block"><p>An establishment that shows movies through screen projection.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_CINEMA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="GOING_OUT_THEATRE_MUSIC_CULTURE">
<h3>GOING_OUT_THEATRE_MUSIC_CULTURE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">GOING_OUT_THEATRE_MUSIC_CULTURE</span></div>
<div className="block"><p>An establishment where various types of performing arts are presented.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_THEATRE_MUSIC_CULTURE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="GOING_OUT_GAMBLING_LOTTERY_BETTING">
<h3>GOING_OUT_GAMBLING_LOTTERY_BETTING</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">GOING_OUT_GAMBLING_LOTTERY_BETTING</span></div>
<div className="block"><p>An establishment that provides gambling entertainment.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_GAMBLING_LOTTERY_BETTING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SIGHTS_AND_MUSEUMS">
<h3>SIGHTS_AND_MUSEUMS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SIGHTS_AND_MUSEUMS</span></div>
<div className="block"><p>Top level category for places of special interest,
 such as common tourist attractions, museums and places of worship.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SIGHTS_AND_MUSEUMS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SIGHTS_LANDMARK_ATTRACTION">
<h3>SIGHTS_LANDMARK_ATTRACTION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SIGHTS_LANDMARK_ATTRACTION</span></div>
<div className="block"><p>A designated area of special interest to tourists.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SIGHTS_LANDMARK_ATTRACTION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SIGHTS_MUSEUM">
<h3>SIGHTS_MUSEUM</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SIGHTS_MUSEUM</span></div>
<div className="block"><p>An establishment dedicated to the preservation and exhibition of artistic, historical, or scientific artifacts.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SIGHTS_MUSEUM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SIGHTS_RELIGIOUS_PLACE">
<h3>SIGHTS_RELIGIOUS_PLACE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SIGHTS_RELIGIOUS_PLACE</span></div>
<div className="block"><p>An establishment special religious significance or where religious services are held.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SIGHTS_RELIGIOUS_PLACE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="NATURAL_AND_GEOGRAPHICAL">
<h3>NATURAL_AND_GEOGRAPHICAL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">NATURAL_AND_GEOGRAPHICAL</span></div>
<div className="block"><p>Top level category for natural or man-made areas of regional importance,
 such as bodies of water, mountains, forested areas and other geographic areas.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER">
<h3>NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER</span></div>
<div className="block"><p>A natural and geographical feature of the earth's surface that is covered with water, such as a lake, river, stream or ocean.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL">
<h3>NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL</span></div>
<div className="block"><p>A natural and geographical feature that is higher than the surrounding land.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE">
<h3>NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE</span></div>
<div className="block"><p>A natural or artificial feature that is below sea level.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION">
<h3>NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION</span></div>
<div className="block"><p>A dense growth of trees, open uncultivated land or other large masses of vegetation.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="NATURAL_AND_GEOGRAPHICAL_OTHER">
<h3>NATURAL_AND_GEOGRAPHICAL_OTHER</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">NATURAL_AND_GEOGRAPHICAL_OTHER</span></div>
<div className="block"><p>A feature not classified as a Body of Water, Mountain or Hill, Undersea Feature, or Forest, Heath or Other Vegetation.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_OTHER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRANSPORT">
<h3>TRANSPORT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRANSPORT</span></div>
<div className="block"><p>Top level category for places commonly associated with pedestrian and cargo transport facilities,
 including airports, rail yards and seaports.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.TRANSPORT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRANSPORT_AIRPORT">
<h3>TRANSPORT_AIRPORT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRANSPORT_AIRPORT</span></div>
<div className="block"><p>A designated area that serves various aspects of aviation related sports, including gliders, recreational aircraft and model airplanes.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.TRANSPORT_AIRPORT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRANSPORT_PUBLIC">
<h3>TRANSPORT_PUBLIC</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRANSPORT_PUBLIC</span></div>
<div className="block"><p>A facility for travelers who are travelling between stops on public transport.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.TRANSPORT_PUBLIC">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRANSPORT_CARGO">
<h3>TRANSPORT_CARGO</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRANSPORT_CARGO</span></div>
<div className="block"><p>A facility that handles some aspect of the transportation of cargo freight.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.TRANSPORT_CARGO">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRANSPORT_REST_AREA">
<h3>TRANSPORT_REST_AREA</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRANSPORT_REST_AREA</span></div>
<div className="block"><p>An establishment along a motorway (controlled access road) that provides restrooms and parking.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.TRANSPORT_REST_AREA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ACCOMMODATION">
<h3>ACCOMMODATION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">ACCOMMODATION</span></div>
<div className="block"><p>Top level category for places offering lodging accommodations, dwellings or similar living quarters to travellers,
 such as hotels, motels, resorts, cruise ships and campgrounds.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.ACCOMMODATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ACCOMMODATION_HOTEL_MOTEL">
<h3>ACCOMMODATION_HOTEL_MOTEL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">ACCOMMODATION_HOTEL_MOTEL</span></div>
<div className="block"><p>A business that provides lodging or temporary living quarters.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.ACCOMMODATION_HOTEL_MOTEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ACCOMMODATION_LODGING">
<h3>ACCOMMODATION_LODGING</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">ACCOMMODATION_LODGING</span></div>
<div className="block"><p>A business that provides lodging to the public generally without room service.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.ACCOMMODATION_LODGING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="LEISURE_AND_OUTDOOR">
<h3>LEISURE_AND_OUTDOOR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">LEISURE_AND_OUTDOOR</span></div>
<div className="block"><p>Top level category for places that are designated for sports, recreation, parking, beaches
 and other leisure and outdoor activities.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.LEISURE_AND_OUTDOOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="LEISURE_OUTDOOR_RECREATION">
<h3>LEISURE_OUTDOOR_RECREATION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">LEISURE_OUTDOOR_RECREATION</span></div>
<div className="block"><p>Public land preserved and maintained for recreational use.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.LEISURE_OUTDOOR_RECREATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="LEISURE_OTHER">
<h3>LEISURE_OTHER</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">LEISURE_OTHER</span></div>
<div className="block"><p>A park that contains rides and/or other entertainment which may be based on a central theme.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.LEISURE_OTHER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHOPPING">
<h3>SHOPPING</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHOPPING</span></div>
<div className="block"><p>Top level category for places where consumer goods are commonly sold,
 such as clothing stores, grocery stores, hardware stores and other types of shopping centers.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHOPPING_CONVENIENCE_STORE">
<h3>SHOPPING_CONVENIENCE_STORE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHOPPING_CONVENIENCE_STORE</span></div>
<div className="block"><p>An establishment that sells groceries, candy, toiletries, soft drinks, tobacco products, newspapers and other products.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_CONVENIENCE_STORE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHOPPING_MALL_COMPLEX">
<h3>SHOPPING_MALL_COMPLEX</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHOPPING_MALL_COMPLEX</span></div>
<div className="block"><p>A complex of businesses that are co-located and share common services.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_MALL_COMPLEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHOPPING_DEPARTMENT_STORE">
<h3>SHOPPING_DEPARTMENT_STORE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHOPPING_DEPARTMENT_STORE</span></div>
<div className="block"><p>A business that sells a wide variety of merchandise that is organized by product or service departments.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_DEPARTMENT_STORE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHOPPING_FOOD_AND_DRINK">
<h3>SHOPPING_FOOD_AND_DRINK</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHOPPING_FOOD_AND_DRINK</span></div>
<div className="block"><p>A business that sells specialty products of a particular type of food or beverage.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_FOOD_AND_DRINK">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHOPPING_DRUGSTORE_PHARMACY">
<h3>SHOPPING_DRUGSTORE_PHARMACY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHOPPING_DRUGSTORE_PHARMACY</span></div>
<div className="block"><p>A business that sells medications, toiletry items and other retail cosmetics.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_DRUGSTORE_PHARMACY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHOPPING_ELECTRONICS">
<h3>SHOPPING_ELECTRONICS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHOPPING_ELECTRONICS</span></div>
<div className="block"><p>A business that sells consumer electronics and electronic entertainment equipment.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_ELECTRONICS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHOPPING_HARDWARE_HOUSE_GARDEN">
<h3>SHOPPING_HARDWARE_HOUSE_GARDEN</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHOPPING_HARDWARE_HOUSE_GARDEN</span></div>
<div className="block"><p>A business that sells crafts, gardening, remodeling, or decorating items for the home.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_HARDWARE_HOUSE_GARDEN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHOPPING_BOOKSTORE">
<h3>SHOPPING_BOOKSTORE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHOPPING_BOOKSTORE</span></div>
<div className="block"><p>A business that sells books, magazines and other reading material.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_BOOKSTORE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHOPPING_CLOTHING_AND_ACCESORIES">
<h3>SHOPPING_CLOTHING_AND_ACCESORIES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHOPPING_CLOTHING_AND_ACCESORIES</span></div>
<div className="block"><p>A business that sells apparel items, garments or fashion accessories for men, women, and children.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_CLOTHING_AND_ACCESORIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHOPPING_CONSUMER_GOODS">
<h3>SHOPPING_CONSUMER_GOODS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHOPPING_CONSUMER_GOODS</span></div>
<div className="block"><p>A business that sells a variety of products targeted to consumers.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_CONSUMER_GOODS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHOPPING_HAIR_AND_BEAUTY">
<h3>SHOPPING_HAIR_AND_BEAUTY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHOPPING_HAIR_AND_BEAUTY</span></div>
<div className="block"><p>A business that provides hair styling and personal appearance services.
 Places in this category may also sell hair products and other related cosmetic items.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.SHOPPING_HAIR_AND_BEAUTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES">
<h3>BUSINESS_AND_SERVICES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES</span></div>
<div className="block"><p>Top level category for places that provide professional services to other businesses,
 such as printing, photocopying, graphic design, marketing, advertising and other general business services.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_BANKING">
<h3>BUSINESS_AND_SERVICES_BANKING</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_BANKING</span></div>
<div className="block"><p>Businesses that specialize in the maintenance, lending, exchange, or issuance of money.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_BANKING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_ATM">
<h3>BUSINESS_AND_SERVICES_ATM</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_ATM</span></div>
<div className="block"><p>A computer terminal that allows bank customers to deposit, withdraw, or transfer funds without the assistance of a bank teller.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_ATM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_MONEY_CASH">
<h3>BUSINESS_AND_SERVICES_MONEY_CASH</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_MONEY_CASH</span></div>
<div className="block"><p>Businesses that provide money related services.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_MONEY_CASH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA">
<h3>BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA</span></div>
<div className="block"><p>Businesses that provide communication services.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_COMMERCIAL_SERVICES">
<h3>BUSINESS_AND_COMMERCIAL_SERVICES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_COMMERCIAL_SERVICES</span></div>
<div className="block"><p>Businesses that provide a service or product for use by other businesses.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_COMMERCIAL_SERVICES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_INDUSTRY">
<h3>BUSINESS_AND_SERVICES_INDUSTRY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_INDUSTRY</span></div>
<div className="block"><p>Businesses that employ people in and around the city in which it is located.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_INDUSTRY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY">
<h3>BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY</span></div>
<div className="block"><p>Municipal emergency services.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_CONSUMER_SERVICES">
<h3>BUSINESS_AND_CONSUMER_SERVICES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_CONSUMER_SERVICES</span></div>
<div className="block"><p>An organization that provides consumer services for a variety of products for used by the public.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_CONSUMER_SERVICES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_POST_OFFICE">
<h3>BUSINESS_AND_SERVICES_POST_OFFICE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_POST_OFFICE</span></div>
<div className="block"><p>An office or station that receives, sorts, dispatches and delivers mail to a specific area or region.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_POST_OFFICE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_TOURIST_INFORMATION">
<h3>BUSINESS_AND_SERVICES_TOURIST_INFORMATION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_TOURIST_INFORMATION</span></div>
<div className="block"><p>Businesses that provide a variety of information for visiting tourists,
 such as event schedules, lodging/accommodations, restaurants, attractions and more.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_TOURIST_INFORMATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_FUELING_STATION">
<h3>BUSINESS_AND_SERVICES_FUELING_STATION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_FUELING_STATION</span></div>
<div className="block"><p>Businesses that sell fuel for vehicles, such as petrol, electricity etc.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_FUELING_STATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION">
<h3>BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION</span></div>
<div className="block"><p>Businesses that sell fuel, oil, and other motoring supplies.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_EV_CHARGING_STATION">
<h3>BUSINESS_AND_SERVICES_EV_CHARGING_STATION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_EV_CHARGING_STATION</span></div>
<div className="block"><p>Businesses that provide recharging services for electric vehicles.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_EV_CHARGING_STATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_CAR_DEALER_SALES">
<h3>BUSINESS_AND_SERVICES_CAR_DEALER_SALES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_CAR_DEALER_SALES</span></div>
<div className="block"><p>Businesses that sell new automobiles and motorcycles.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_CAR_DEALER_SALES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES">
<h3>BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES</span></div>
<div className="block"><p>Businesses that provide automotive repair services.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_CAR_RENTAL">
<h3>BUSINESS_AND_SERVICES_CAR_RENTAL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_CAR_RENTAL</span></div>
<div className="block"><p>Businesses that rent or lease automobiles.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_CAR_RENTAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER">
<h3>BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER</span></div>
<div className="block"><p>Business that sell or service trucks and tractor trailers.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="FACILITIES">
<h3>FACILITIES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">FACILITIES</span></div>
<div className="block"><p>Top level category for places associated with specialized facilities,
 such as sports venues, government buildings, health care centers and other types of facilities.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="FACILITIES_HOSPITAL_HEALTHCARE">
<h3>FACILITIES_HOSPITAL_HEALTHCARE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">FACILITIES_HOSPITAL_HEALTHCARE</span></div>
<div className="block"><p>Facilities that include dental offices, hospitals, nursing homes and other health care-related services.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_HOSPITAL_HEALTHCARE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="FACILITIES_GOVERNMENT_COMMUNITTY">
<h3>FACILITIES_GOVERNMENT_COMMUNITTY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">FACILITIES_GOVERNMENT_COMMUNITTY</span></div>
<div className="block"><p>A Place where government services are provided.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_GOVERNMENT_COMMUNITTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="FACILITIES_EDUCATION">
<h3>FACILITIES_EDUCATION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">FACILITIES_EDUCATION</span></div>
<div className="block"><p>Facilities that are used for educational purposes including training, coaching, universities and more.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_EDUCATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="FACILITIES_SCHOOL">
<h3>FACILITIES_SCHOOL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">FACILITIES_SCHOOL</span></div>
<div className="block"><p>Educational facilities that include primary schools, secondary schools and more.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_SCHOOL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="FACILITIES_LIBRARY">
<h3>FACILITIES_LIBRARY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">FACILITIES_LIBRARY</span></div>
<div className="block"><p>Facilities that offer books, periodicals, audio, video and other material for public use.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_LIBRARY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="FACILITIES_EVENT_SPACES">
<h3>FACILITIES_EVENT_SPACES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">FACILITIES_EVENT_SPACES</span></div>
<div className="block"><p>An area or facility used for the hosting of fairs and conventions.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_EVENT_SPACES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="FACILITIES_PARKING">
<h3>FACILITIES_PARKING</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">FACILITIES_PARKING</span></div>
<div className="block"><p>Area or building used for parking cars.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_PARKING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="FACILITIES_VENUE_SPORTS">
<h3>FACILITIES_VENUE_SPORTS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">FACILITIES_VENUE_SPORTS</span></div>
<div className="block"><p>A facility used for individual and team sports including recreational sports.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_VENUE_SPORTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="FACILITIES_OTHER">
<h3>FACILITIES_OTHER</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">FACILITIES_OTHER</span></div>
<div className="block"><p>Facilities with miscellaneous uses such as Clubhouses, Offices, and Registration Offices.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.FACILITIES_OTHER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="AREAS_AND_BUILDINGS">
<h3>AREAS_AND_BUILDINGS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">AREAS_AND_BUILDINGS</span></div>
<div className="block"><p>Top level category for places that are owned, operated or managed by municipalities,
 such as cities, towns, villages, boroughs and shires.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.AREAS_AND_BUILDINGS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX">
<h3>AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX</span></div>
<div className="block"><p>Outdoor areas or complexes with designations for specific businesses or interests.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE">
<h3>AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE</span></div>
<div className="block"><p>Areas and buildings designated for residential or office use.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.search.PlaceCategory.AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE">Constant Field Values</a></li>
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
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String)">
<h3>PlaceCategory</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">PlaceCategory</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
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
     <a href="sdk-for-android-navigate-com-here-sdk-search-placecategory#EAT_AND_DRINK_RESTAURANT"><code>EAT_AND_DRINK_RESTAURANT</code></a> or as a literal string that matches
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getId()">
<h3>getId</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getId</span>()</div>
<div className="block"><p>Gets the place category ID.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Place category ID.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getName()">
<h3>getName</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getName</span>()</div>
<div className="block"><p>Gets the localised place category name.
 It is available only when when <code>PlaceCategory</code> is obtained from <code>Place</code>.
 That means that when <code>PlaceCategory</code> is constructed directly by the client,
 <code>name</code> is always <code>null</code>.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>

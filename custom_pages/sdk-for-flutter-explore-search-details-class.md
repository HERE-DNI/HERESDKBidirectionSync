---
title: "Untitled"
slug: "sdk-for-flutter-explore-search-details-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Details-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">Details class</li>
</ol>
<div class="self-name">Details</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/Details-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Details class</h1></div>
<section class="desc markdown">
<p>Contains details of a specific place, such as contact information,
opening hours and assigned categories.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Details">
/sdk-for-flutter-explore-search-details-details(List&lt;<wbr/>/sdk-for-flutter-explore-search-contact-class&gt; contacts, List&lt;<wbr/>/sdk-for-flutter-explore-search-openinghours-class&gt; openingHours, List&lt;<wbr/>/sdk-for-flutter-explore-search-placecategory-class&gt; categories, List&lt;<wbr/>/sdk-for-flutter-explore-search-webimage-class&gt; images, List&lt;<wbr/>/sdk-for-flutter-explore-search-webeditorial-class&gt; editorials, List&lt;<wbr/>/sdk-for-flutter-explore-search-webrating-class&gt; ratings, List&lt;<wbr/>/sdk-for-flutter-explore-search-supplierreference-class&gt; references, [/sdk-for-flutter-explore-search-evchargingpool-class? evChargingPool = null, /sdk-for-flutter-explore-search-truckamenities-class? truckAmenities = null, /sdk-for-flutter-explore-search-fuelstation-class? fuelStation = null, List&lt;<wbr/>/sdk-for-flutter-explore-search-placefoodtype-class&gt; foodTypes = const [], /sdk-for-flutter-explore-search-poipaymentdetails-class? payment = null, /sdk-for-flutter-explore-search-evcharginglocation-class? evChargingLocation = null])
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="Details.withDefaults">
/sdk-for-flutter-explore-search-details-details-withdefaults(List&lt;<wbr/>/sdk-for-flutter-explore-search-contact-class&gt; contacts, List&lt;<wbr/>/sdk-for-flutter-explore-search-openinghours-class&gt; openingHours, List&lt;<wbr/>/sdk-for-flutter-explore-search-placecategory-class&gt; categories, List&lt;<wbr/>/sdk-for-flutter-explore-search-webimage-class&gt; images, List&lt;<wbr/>/sdk-for-flutter-explore-search-webeditorial-class&gt; editorials, List&lt;<wbr/>/sdk-for-flutter-explore-search-webrating-class&gt; ratings, List&lt;<wbr/>/sdk-for-flutter-explore-search-supplierreference-class&gt; references)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="categories">
/sdk-for-flutter-explore-search-details-categories
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-placecategory-class&gt;
</dt>
<dd>
  The list of categories assigned to this place.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="contacts">
/sdk-for-flutter-explore-search-details-contacts
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-contact-class&gt;
</dt>
<dd>
  The list of contact information of the place.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="editorials">
/sdk-for-flutter-explore-search-details-editorials
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-webeditorial-class&gt;
</dt>
<dd>
  The list of editorials associated with the place.
The editorials are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="evChargingLocation">
/sdk-for-flutter-explore-search-details-evcharginglocation
↔ /sdk-for-flutter-explore-search-evcharginglocation-class?
</dt>
<dd>
  Details about the EV charging station, if this place belongs to the EV charging station category.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="evChargingPool">
/sdk-for-flutter-explore-search-details-evchargingpool
↔ /sdk-for-flutter-explore-search-evchargingpool-class?
</dt>
<dd>
  EV charging pool details. It is available only for a place that is a charging pool
for electric vehicles.
It is fully supported for offline search, provided that /sdk-for-flutter-explore-core-engine-layerconfigurationfeature
is enabled in /sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="foodTypes">
/sdk-for-flutter-explore-search-details-foodtypes
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-placefoodtype-class&gt;
</dt>
<dd>
  The list of food types assigned to this place.
Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="fuelStation">
/sdk-for-flutter-explore-search-details-fuelstation
↔ /sdk-for-flutter-explore-search-fuelstation-class?
</dt>
<dd>
  Fuel station details. It is available only if a place is a fuel station and contain fuel data.
It is fully supported for offline search, provided that /sdk-for-flutter-explore-core-engine-layerconfigurationfeature
is enabled in /sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-search-details-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="images">
/sdk-for-flutter-explore-search-details-images
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-webimage-class&gt;
</dt>
<dd>
  The list of images associated with the place.
The images are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="openingHours">
/sdk-for-flutter-explore-search-details-openinghours
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-openinghours-class&gt;
</dt>
<dd>
  The list of opening hours information of the place.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="payment">
/sdk-for-flutter-explore-search-details-payment
↔ /sdk-for-flutter-explore-search-poipaymentdetails-class?
</dt>
<dd>
  Details about the payment options at the POI.
Set to <code>null</code> if the place is not a POI or if payment details are not available.
Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="ratings">
/sdk-for-flutter-explore-search-details-ratings
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-webrating-class&gt;
</dt>
<dd>
  The list of ratings associated with the place.
The ratings are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="references">
/sdk-for-flutter-explore-search-details-references
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-supplierreference-class&gt;
</dt>
<dd>
  The list of supplier references to this place.
The references are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-search-details-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="truckAmenities">
/sdk-for-flutter-explore-search-details-truckamenities
↔ /sdk-for-flutter-explore-search-truckamenities-class?
</dt>
<dd>
  Additional information that is available only for places that contain truck amenities.
It is fully supported for offline search, provided that /sdk-for-flutter-explore-core-engine-layerconfigurationfeature
is enabled in /sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="getPrimaryCategories">
/sdk-for-flutter-explore-search-details-getprimarycategories(<wbr/>)
    → List&lt;<wbr/>/sdk-for-flutter-explore-search-placecategory-class&gt;

</dt>
<dd>
  Gets the list of primary categories assigned to this place.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-search-details-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-search-details-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-explore-search-details-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">Details class</li>
</ol>
<h5>search library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>

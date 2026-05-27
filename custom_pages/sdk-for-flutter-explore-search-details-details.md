---
title: "Implementation"
slug: "sdk-for-flutter-explore-search-details-details"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- Details.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/Details-class.html">/sdk-for-flutter-explore-search-details-class</a></li>
<li class="self-crumb">Details constructor</li>
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
<div class="main-content" data-above-sidebar="search/Details-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>Details constructor</h1></div>
<section class="multi-line-signature">
Details(<wbr/><ol class="parameter-list"> <li>List&lt;<wbr/><a href="../../search/Contact-class.html">/sdk-for-flutter-explore-search-contact-class</a>&gt; contacts, </li>
<li>List&lt;<wbr/><a href="../../search/OpeningHours-class.html">/sdk-for-flutter-explore-search-openinghours-class</a>&gt; openingHours, </li>
<li>List&lt;<wbr/><a href="../../search/PlaceCategory-class.html">/sdk-for-flutter-explore-search-placecategory-class</a>&gt; categories, </li>
<li>List&lt;<wbr/><a href="../../search/WebImage-class.html">/sdk-for-flutter-explore-search-webimage-class</a>&gt; images, </li>
<li>List&lt;<wbr/><a href="../../search/WebEditorial-class.html">/sdk-for-flutter-explore-search-webeditorial-class</a>&gt; editorials, </li>
<li>List&lt;<wbr/><a href="../../search/WebRating-class.html">/sdk-for-flutter-explore-search-webrating-class</a>&gt; ratings, </li>
<li>List&lt;<wbr/><a href="../../search/SupplierReference-class.html">/sdk-for-flutter-explore-search-supplierreference-class</a>&gt; references, [</li>
<li><a href="../../search/EVChargingPool-class.html">/sdk-for-flutter-explore-search-evchargingpool-class</a>? evChargingPool = null, </li>
<li><a href="../../search/TruckAmenities-class.html">/sdk-for-flutter-explore-search-truckamenities-class</a>? truckAmenities = null, </li>
<li><a href="../../search/FuelStation-class.html">/sdk-for-flutter-explore-search-fuelstation-class</a>? fuelStation = null, </li>
<li>List&lt;<wbr/><a href="../../search/PlaceFoodType-class.html">/sdk-for-flutter-explore-search-placefoodtype-class</a>&gt; foodTypes = const [], </li>
<li><a href="../../search/POIPaymentDetails-class.html">/sdk-for-flutter-explore-search-poipaymentdetails-class</a>? payment = null, </li>
<li><a href="../../search/EVChargingLocation-class.html">/sdk-for-flutter-explore-search-evcharginglocation-class</a>? evChargingLocation = null, </li>
</ol>])
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>contacts</code> The list of contact information of the place.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <a href="../../search/Suggestion-class.html">/sdk-for-flutter-explore-search-suggestion-class</a> results.</p>
<ul>
<li><code>openingHours</code> The list of opening hours information of the place.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <a href="../../search/Suggestion-class.html">/sdk-for-flutter-explore-search-suggestion-class</a> results.</p>
<ul>
<li><code>categories</code> The list of categories assigned to this place.</li>
<li><code>images</code> The list of images associated with the place.
The images are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <a href="../../search/Suggestion-class.html">/sdk-for-flutter-explore-search-suggestion-class</a> results.</p>
<ul>
<li><code>editorials</code> The list of editorials associated with the place.
The editorials are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <a href="../../search/Suggestion-class.html">/sdk-for-flutter-explore-search-suggestion-class</a> results.</p>
<ul>
<li><code>ratings</code> The list of ratings associated with the place.
The ratings are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <a href="../../search/Suggestion-class.html">/sdk-for-flutter-explore-search-suggestion-class</a> results.</p>
<ul>
<li><code>references</code> The list of supplier references to this place.
The references are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</li>
<li><code>evChargingPool</code> EV charging pool details. It is available only for a place that is a charging pool
for electric vehicles.
It is fully supported for offline search, provided that <a href="../../core.engine/LayerConfigurationFeature.html">/sdk-for-flutter-explore-core-engine-layerconfigurationfeature</a>
is enabled in <a href="../../core.engine/SDKOptions/layerConfiguration.html">/sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration</a>.</li>
</ul>
<p>For online search, this feature is only available if it is explicitly enabled.
To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
name: "lookup.show" or "discover.show" or "browse.show"
value: "ev"
To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
"lookup.show", "discover.show" and "browse.show".
To enable fuel station details or truck amenities, the custom option value can be combined
as "ev,truck", "ev,truck,fuel" etc.</p>
<ul>
<li><code>truckAmenities</code> Additional information that is available only for places that contain truck amenities.
It is fully supported for offline search, provided that <a href="../../core.engine/LayerConfigurationFeature.html">/sdk-for-flutter-explore-core-engine-layerconfigurationfeature</a>
is enabled in <a href="../../core.engine/SDKOptions/layerConfiguration.html">/sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration</a>.</li>
</ul>
<p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
only for selected customers. The field is always null for everyone that is not part of
the closed-alpha group.
Participants of the closed-alpha group can get access from HERE to use this feature.
If the credentials are not enabled, a <a href="../../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a> will be propagated.</p>
<p>For online search, this feature is only available if it is explicitly enabled.
To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
value: "truck"
To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
"lookup.show", "discover.show", "autosuggest.show" and "browse.show".
To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>fuelStation</code> Fuel station details. It is available only if a place is a fuel station and contain fuel data.
It is fully supported for offline search, provided that <a href="../../core.engine/LayerConfigurationFeature.html">/sdk-for-flutter-explore-core-engine-layerconfigurationfeature</a>
is enabled in <a href="../../core.engine/SDKOptions/layerConfiguration.html">/sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration</a>.</li>
</ul>
<p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
only for selected customers. The field is always null for everyone that is not part of
the closed-alpha group.
Participants of the closed-alpha group can get access from HERE to use this feature.
If the credentials are not enabled, a <a href="../../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a> will be propagated.</p>
<p>For online search, this feature is only available if it is explicitly enabled.
To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show"
value: "fuel"
To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
"lookup.show", "discover.show", "autosuggest.show" and "browse.show".
To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to "fuel,truck".</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>foodTypes</code> The list of food types assigned to this place.
Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</li>
<li><code>payment</code> Details about the payment options at the POI.
Set to <code>null</code> if the place is not a POI or if payment details are not available.
Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>evChargingLocation</code> Details about the EV charging station, if this place belongs to the EV charging station category.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Details(List&lt;Contact&gt; contacts, List&lt;OpeningHours&gt; openingHours, List&lt;PlaceCategory&gt; categories, List&lt;WebImage&gt; images, List&lt;WebEditorial&gt; editorials, List&lt;WebRating&gt; ratings, List&lt;SupplierReference&gt; references, [EVChargingPool? evChargingPool = null, TruckAmenities? truckAmenities = null, FuelStation? fuelStation = null, List&lt;PlaceFoodType&gt; foodTypes = const [], POIPaymentDetails? payment = null, EVChargingLocation? evChargingLocation = null])
  : contacts = contacts, openingHours = openingHours, categories = categories, images = images, editorials = editorials, ratings = ratings, references = references, evChargingPool = evChargingPool ?? null, truckAmenities = truckAmenities ?? null, fuelStation = fuelStation ?? null, foodTypes = foodTypes, payment = payment ?? null, evChargingLocation = evChargingLocation;</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/Details-class.html">/sdk-for-flutter-explore-search-details-class</a></li>
<li class="self-crumb">Details constructor</li>
</ol>
<h5>Details class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>

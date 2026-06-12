---
title: "Details"
slug: "sdk-for-ios-explore-api-reference-structs-details"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Details"></a>
<a title="Details Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-search">Search</a>

        Details Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Details</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Details</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains details of a specific place, such as contact information,
opening hours and assigned categories.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV8contactsSayAA7ContactVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/contacts"></a>
<a class="token" href="#/s:7heresdk7DetailsV8contactsSayAA7ContactVGvp">contacts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of contact information of the place.</p>
<p><strong>Note:</strong> Not available as part of <code><a href="sdk-for-ios-explore-api-reference-classes-suggestion">Suggestion</a></code> results.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">contacts</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-contact">Contact</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV12openingHoursSayAA07OpeningD0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/openingHours"></a>
<a class="token" href="#/s:7heresdk7DetailsV12openingHoursSayAA07OpeningD0VGvp">openingHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of opening hours information of the place.</p>
<p><strong>Note:</strong> Not available as part of <code><a href="sdk-for-ios-explore-api-reference-classes-suggestion">Suggestion</a></code> results.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">openingHours</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-openinghours">OpeningHours</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV10categoriesSayAA13PlaceCategoryCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/categories"></a>
<a class="token" href="#/s:7heresdk7DetailsV10categoriesSayAA13PlaceCategoryCGvp">categories</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of categories assigned to this place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">categories</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-placecategory">PlaceCategory</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV6imagesSayAA8WebImageVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/images"></a>
<a class="token" href="#/s:7heresdk7DetailsV6imagesSayAA8WebImageVGvp">images</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of images associated with the place.
The images are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p>
<p><strong>Note:</strong> Not available as part of <code><a href="sdk-for-ios-explore-api-reference-classes-suggestion">Suggestion</a></code> results.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">images</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-webimage">WebImage</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV10editorialsSayAA12WebEditorialVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/editorials"></a>
<a class="token" href="#/s:7heresdk7DetailsV10editorialsSayAA12WebEditorialVGvp">editorials</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of editorials associated with the place.
The editorials are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p>
<p><strong>Note:</strong> Not available as part of <code><a href="sdk-for-ios-explore-api-reference-classes-suggestion">Suggestion</a></code> results.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">editorials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-webeditorial">WebEditorial</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV7ratingsSayAA9WebRatingVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ratings"></a>
<a class="token" href="#/s:7heresdk7DetailsV7ratingsSayAA9WebRatingVGvp">ratings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of ratings associated with the place.
The ratings are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p>
<p><strong>Note:</strong> Not available as part of <code><a href="sdk-for-ios-explore-api-reference-classes-suggestion">Suggestion</a></code> results.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">ratings</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-webrating">WebRating</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV10referencesSayAA17SupplierReferenceVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/references"></a>
<a class="token" href="#/s:7heresdk7DetailsV10referencesSayAA17SupplierReferenceVGvp">references</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of supplier references to this place.
The references are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">references</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-supplierreference">SupplierReference</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV14evChargingPoolAA010EVChargingE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evChargingPool"></a>
<a class="token" href="#/s:7heresdk7DetailsV14evChargingPoolAA010EVChargingE0VSgvp">evChargingPool</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EV charging pool details. It is available only for a place that is a charging pool
for electric vehicles.
It is fully supported for offline search, provided that <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">LayerConfiguration.Feature.ev</a></code>
is enabled in <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code>.</p>
<p>For online search, this feature is only available if it is explicitly enabled.
To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
name: “lookup.show” or “discover.show” or “browse.show”
value: “ev”
To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
“lookup.show”, “discover.show” and “browse.show”.
To enable fuel station details or truck amenities, the custom option value can be combined
as “ev,truck”, “ev,truck,fuel” etc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">evChargingPool</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evchargingpool">EVChargingPool</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV14truckAmenitiesAA05TruckD0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckAmenities"></a>
<a class="token" href="#/s:7heresdk7DetailsV14truckAmenitiesAA05TruckD0VSgvp">truckAmenities</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Additional information that is available only for places that contain truck amenities.
It is fully supported for offline search, provided that <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO22truckServiceAttributesyA2EmF">LayerConfiguration.Feature.truckServiceAttributes</a></code>
is enabled in <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code>.</p>
<p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
only for selected customers. The field is always null for everyone that is not part of
the closed-alpha group.
Participants of the closed-alpha group can get access from HERE to use this feature.
If the credentials are not enabled, a <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">SearchError.forbidden</a></code> will be propagated.</p>
<p>For online search, this feature is only available if it is explicitly enabled.
To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
name: “lookup.show” or “discover.show” or “autosuggest.show” or “browse.show”
value: “truck”
To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
“lookup.show”, “discover.show”, “autosuggest.show” and “browse.show”.
To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to “fuel,truck”.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckAmenities</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-truckamenities">TruckAmenities</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV11fuelStationAA04FuelD0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/fuelStation"></a>
<a class="token" href="#/s:7heresdk7DetailsV11fuelStationAA04FuelD0VSgvp">fuelStation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Fuel station details. It is available only if a place is a fuel station and contain fuel data.
It is fully supported for offline search, provided that <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO21fuelStationAttributesyA2EmF">LayerConfiguration.Feature.fuelStationAttributes</a></code>
is enabled in <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code>.</p>
<p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
only for selected customers. The field is always null for everyone that is not part of
the closed-alpha group.
Participants of the closed-alpha group can get access from HERE to use this feature.
If the credentials are not enabled, a <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">SearchError.forbidden</a></code> will be propagated.</p>
<p>For online search, this feature is only available if it is explicitly enabled.
To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
name: “lookup.show” or “discover.show” or “autosuggest.show” or “browse.show”
value: “fuel”
To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
“lookup.show”, “discover.show”, “autosuggest.show” and “browse.show”.
To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to “fuel,truck”.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">fuelStation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-fuelstation">FuelStation</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV9foodTypesSayAA13PlaceFoodTypeVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/foodTypes"></a>
<a class="token" href="#/s:7heresdk7DetailsV9foodTypesSayAA13PlaceFoodTypeVGvp">foodTypes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of food types assigned to this place.
Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">foodTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-placefoodtype">PlaceFoodType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV7paymentAA010POIPaymentB0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/payment"></a>
<a class="token" href="#/s:7heresdk7DetailsV7paymentAA010POIPaymentB0VSgvp">payment</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Details about the payment options at the POI.
Set to <code>nil</code> if the place is not a POI or if payment details are not available.
Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">payment</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-poipaymentdetails">POIPaymentDetails</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV18evChargingLocationAA010EVChargingE0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evChargingLocation"></a>
<a class="token" href="#/s:7heresdk7DetailsV18evChargingLocationAA010EVChargingE0CSgvp">evChargingLocation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Details about the EV charging station, if this place belongs to the EV charging station category.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">evChargingLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-evcharginglocation">EVChargingLocation</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV8contacts12openingHours10categories6images10editorials7ratings10references14evChargingPool14truckAmenities11fuelStation9foodTypes7payment0kL8LocationACSayAA7ContactVG_SayAA07OpeningE0VGSayAA13PlaceCategoryCGSayAA8WebImageVGSayAA0Z9EditorialVGSayAA0Z6RatingVGSayAA17SupplierReferenceVGAA010EVChargingM0VSgAA05TruckO0VSgAA04FuelQ0VSgSayAA0X8FoodTypeVGAA010POIPaymentB0VSgAA010EVChargingU0CSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(contacts:openingHours:categories:images:editorials:ratings:references:evChargingPool:truckAmenities:fuelStation:foodTypes:payment:evChargingLocation:)"></a>
<a class="token" href="#/s:7heresdk7DetailsV8contacts12openingHours10categories6images10editorials7ratings10references14evChargingPool14truckAmenities11fuelStation9foodTypes7payment0kL8LocationACSayAA7ContactVG_SayAA07OpeningE0VGSayAA13PlaceCategoryCGSayAA8WebImageVGSayAA0Z9EditorialVGSayAA0Z6RatingVGSayAA17SupplierReferenceVGAA010EVChargingM0VSgAA05TruckO0VSgAA04FuelQ0VSgSayAA0X8FoodTypeVGAA010POIPaymentB0VSgAA010EVChargingU0CSgtcfc">init(contacts:<wbr/>openingHours:<wbr/>categories:<wbr/>images:<wbr/>editorials:<wbr/>ratings:<wbr/>references:<wbr/>evChargingPool:<wbr/>truckAmenities:<wbr/>fuelStation:<wbr/>foodTypes:<wbr/>payment:<wbr/>evChargingLocation:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>contacts: The list of contact information of the place.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <code><a href="sdk-for-ios-explore-api-reference-classes-suggestion">Suggestion</a></code> results.</p>
<ul>
<li>openingHours: The list of opening hours information of the place.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <code><a href="sdk-for-ios-explore-api-reference-classes-suggestion">Suggestion</a></code> results.</p>
<ul>
<li>categories: The list of categories assigned to this place.</li>
<li>images: The list of images associated with the place.
The images are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <code><a href="sdk-for-ios-explore-api-reference-classes-suggestion">Suggestion</a></code> results.</p>
<ul>
<li>editorials: The list of editorials associated with the place.
The editorials are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <code><a href="sdk-for-ios-explore-api-reference-classes-suggestion">Suggestion</a></code> results.</p>
<ul>
<li>ratings: The list of ratings associated with the place.
The ratings are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</li>
</ul>
<p><strong>Note:</strong> Not available as part of <code><a href="sdk-for-ios-explore-api-reference-classes-suggestion">Suggestion</a></code> results.</p>
<ul>
<li>references: The list of supplier references to this place.
The references are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</li>
<li>evChargingPool: EV charging pool details. It is available only for a place that is a charging pool
for electric vehicles.
It is fully supported for offline search, provided that <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">LayerConfiguration.Feature.ev</a></code>
is enabled in <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code>.</li>
</ul>
<p>For online search, this feature is only available if it is explicitly enabled.
  To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
  name: “lookup.show” or “discover.show” or “browse.show”
  value: “ev”
  To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
  “lookup.show”, “discover.show” and “browse.show”.
  To enable fuel station details or truck amenities, the custom option value can be combined
  as “ev,truck”, “ev,truck,fuel” etc.</p>
<ul>
<li>truckAmenities: Additional information that is available only for places that contain truck amenities.
It is fully supported for offline search, provided that <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO22truckServiceAttributesyA2EmF">LayerConfiguration.Feature.truckServiceAttributes</a></code>
is enabled in <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code>.</li>
</ul>
<p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
  only for selected customers. The field is always null for everyone that is not part of
  the closed-alpha group.
  Participants of the closed-alpha group can get access from HERE to use this feature.
  If the credentials are not enabled, a <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">SearchError.forbidden</a></code> will be propagated.</p>
<p>For online search, this feature is only available if it is explicitly enabled.
  To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
  name: “lookup.show” or “discover.show” or “autosuggest.show” or “browse.show”
  value: “truck”
  To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
  “lookup.show”, “discover.show”, “autosuggest.show” and “browse.show”.
  To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to “fuel,truck”.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
  unexpected behaviors.
  Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>fuelStation: Fuel station details. It is available only if a place is a fuel station and contain fuel data.
It is fully supported for offline search, provided that <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO21fuelStationAttributesyA2EmF">LayerConfiguration.Feature.fuelStationAttributes</a></code>
is enabled in <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code>.</li>
</ul>
<p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
  only for selected customers. The field is always null for everyone that is not part of
  the closed-alpha group.
  Participants of the closed-alpha group can get access from HERE to use this feature.
  If the credentials are not enabled, a <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">SearchError.forbidden</a></code> will be propagated.</p>
<p>For online search, this feature is only available if it is explicitly enabled.
  To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
  name: “lookup.show” or “discover.show” or “autosuggest.show” or “browse.show”
  value: “fuel”
  To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
  “lookup.show”, “discover.show”, “autosuggest.show” and “browse.show”.
  To enable both <code>truck_amenities</code> and <code>fuel_station</code> features, set the value to “fuel,truck”.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
  unexpected behaviors.
  Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>foodTypes: The list of food types assigned to this place.
Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</li>
<li>payment: Details about the payment options at the POI.
Set to <code>nil</code> if the place is not a POI or if payment details are not available.
Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
  unexpected behaviors.
  Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>evChargingLocation: Details about the EV charging station, if this place belongs to the EV charging station category.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">contacts</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-contact">Contact</a></span><span class="p">],</span> <span class="nv">openingHours</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-openinghours">OpeningHours</a></span><span class="p">],</span> <span class="nv">categories</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-placecategory">PlaceCategory</a></span><span class="p">],</span> <span class="nv">images</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-webimage">WebImage</a></span><span class="p">],</span> <span class="nv">editorials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-webeditorial">WebEditorial</a></span><span class="p">],</span> <span class="nv">ratings</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-webrating">WebRating</a></span><span class="p">],</span> <span class="nv">references</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-supplierreference">SupplierReference</a></span><span class="p">],</span> <span class="nv">evChargingPool</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evchargingpool">EVChargingPool</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">truckAmenities</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-truckamenities">TruckAmenities</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">fuelStation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-fuelstation">FuelStation</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">foodTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-placefoodtype">PlaceFoodType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">payment</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-poipaymentdetails">POIPaymentDetails</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">evChargingLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-evcharginglocation">EVChargingLocation</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7DetailsV20getPrimaryCategoriesSayAA13PlaceCategoryCGyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getPrimaryCategories()"></a>
<a class="token" href="#/s:7heresdk7DetailsV20getPrimaryCategoriesSayAA13PlaceCategoryCGyF">getPrimaryCategories()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the list of primary categories assigned to this place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getPrimaryCategories</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-placecategory">PlaceCategory</a></span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>List of categories.</p>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
} </HTMLBlock>

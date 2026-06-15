---
title: "truckAmenities property"
slug: "sdk-for-flutter-explore-search-details-truckamenities"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- truckAmenities.html -->


<div>
<h1>truckAmenities property</h1></div>

<a href="sdk-for-flutter-explore-search-truckamenities-class">TruckAmenities</a>?
        truckAmenities
<div class="features">getter/setter pair</div>


<p>Additional information that is available only for places that contain truck amenities.
It is fully supported for offline search, provided that <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.truckServiceAttributes</a>
is enabled in <a href="sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.</p>
<p><strong>Note:</strong> Currently, for online search, this is a closed-alpha feature, so it is available
only for selected customers. The field is always null for everyone that is not part of
the closed-alpha group.
Participants of the closed-alpha group can get access from HERE to use this feature.
If the credentials are not enabled, a <a href="sdk-for-flutter-explore-search-searcherror">SearchError.forbidden</a> will be propagated.</p>
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


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TruckAmenities? truckAmenities;</code></pre>

 



</div>
`
}</HTMLBlock>

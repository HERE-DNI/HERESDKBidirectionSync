---
title: "truckAmenities property - Details class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-details-truckamenities"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/Details-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">truckAmenities</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-explore-search-truckamenities-class">TruckAmenities</a>? <span class="name">truckAmenities</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Additional information that is available only for places that contain truck amenities. It is fully supported for offline search, provided that <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.truckServiceAttributes</a> is enabled in <a href="sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.

**Note:** Currently, for online search, this is a closed-alpha feature, so it is available only for selected customers. The field is always null for everyone that is not part of the closed-alpha group. Participants of the closed-alpha group can get access from HERE to use this feature. If the credentials are not enabled, a <a href="sdk-for-flutter-explore-search-searcherror">SearchError.forbidden</a> will be propagated.

For online search, this feature is only available if it is explicitly enabled. To do that, call

    SearchEngine.set_custom_option()

with arguments: name: "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show" value: "truck" To enable this feature for all queries, call

    SearchEngine.set_custom_option()

for all: "lookup.show", "discover.show", "autosuggest.show" and "browse.show". To enable both `truck_amenities` and `fuel_station` features, set the value to "fuel,truck".
</p>

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
TruckAmenities? truckAmenities;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


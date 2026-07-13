---
title: "fuelTypes property - PlaceFilter class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-placefilter-fueltypes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fuelTypes.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/PlaceFilter-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">fuelTypes</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-transport-fueltype">FuelType</a></span>\></span> <span class="name">fuelTypes</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The list of <a href="sdk-for-flutter-navigate-transport-fueltype">FuelType</a> elements that should be used to find only the <a href="sdk-for-flutter-navigate-search-fuelstation-class">FuelStation</a> search results that support all of them. This filter is available to use with the `SearchEngine` and `OfflineSearchEngine` (only available for the Navigate license), however `OfflineSearchEngine` supports it only for `searchByText` and `searchByCategory` with allowed fuel types `DIESEL`, `LPG`, `BIO_DIESEL`, `CNG`, `DIESEL_WITH_ADDITIVES`, `E10`, `E85`, `ETHANOL`, `ETHANOL_WITH_ADDITIVES`, `GASOLINE`, `HYDROGEN`, `LNG`, `MIDGRADE`, `PREMIUM` and `REGULAR`.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
List<FuelType> fuelTypes;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

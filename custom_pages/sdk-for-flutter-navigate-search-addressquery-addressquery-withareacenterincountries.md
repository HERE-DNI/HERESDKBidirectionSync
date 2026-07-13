---
title: "AddressQuery.withAreaCenterInCountries constructor - AddressQuery - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-addressquery-addressquery-withareacenterincountries"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AddressQuery.withAreaCenterInCountries.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/AddressQuery-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">AddressQuery.withAreaCenterInCountries</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">AddressQuery.withAreaCenterInCountries</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withAreaCenterInCountries-param-query" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">query</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withAreaCenterInCountries-param-areaCenter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">areaCenter</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withAreaCenterInCountries-param-countries" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-countrycode">CountryCode</a></span>\></span></span> <span class="parameter-name">countries</span></span>

)

</div>

<div class="section desc markdown">

Constructs an AddressQuery from the provided text query, geographical coordinates and the list of countries the query is applied in.

- `query` Desired query to search.

- `areaCenter` Geographical coordinates of the center around which to provide the most relevant places.

- `countries` A list of countries that the query is applied in.

</div>

## Implementation

``` dart
factory AddressQuery.withAreaCenterInCountries(String query, GeoCoordinates areaCenter, List<CountryCode> countries) => $prototype.withAreaCenterInCountries(query, areaCenter, countries);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

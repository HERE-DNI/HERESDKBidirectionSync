---
title: "SearchInterface constructor - SearchInterface - search library - Dart API"
slug: "sdk-for-flutter-explore-search-searchinterface-searchinterface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SearchInterface.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">SearchInterface</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">SearchInterface</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-searchByTextLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">searchByTextLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a></span>, </span>
    2.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
2.  <span id="sdk-for-flutter-explore-param-searchByAddressLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">searchByAddressLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-addressquery-class">AddressQuery</a></span>, </span>
    2.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
3.  <span id="sdk-for-flutter-explore-param-searchByCategoryLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">searchByCategoryLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-categoryquery-class">CategoryQuery</a></span>, </span>
    2.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
4.  <span id="sdk-for-flutter-explore-param-searchByCoordinatesLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">searchByCoordinatesLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>, </span>
    2.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
5.  <span id="sdk-for-flutter-explore-param-searchByPlaceIdLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">searchByPlaceIdLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidquery-class">PlaceIdQuery</a></span>, </span>
    2.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?</span>, </span>
    3.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidsearchcallback">PlaceIdSearchCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
6.  <span id="sdk-for-flutter-explore-param-searchByPickedPlaceLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">searchByPickedPlaceLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-pickedplace-class">PickedPlace</a></span>, </span>
    2.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?</span>, </span>
    3.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidsearchcallback">PlaceIdSearchCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>
7.  <span id="sdk-for-flutter-explore-param-suggestByTextLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="parameter-name">suggestByTextLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a></span>, </span>
    2.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span>, </span>
    3.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-suggestcallback">SuggestCallback</a></span> <span class="parameter-name"></span></span>

    ), </span>

)

</div>

<div class="section desc markdown">

Provides the abstract class for the online and offline search engines.

</div>

## Implementation

``` dart
factory SearchInterface(
  TaskHandle Function(TextQuery, SearchOptions, SearchCallback) searchByTextLambda,
  TaskHandle Function(AddressQuery, SearchOptions, SearchCallback) searchByAddressLambda,
  TaskHandle Function(CategoryQuery, SearchOptions, SearchCallback) searchByCategoryLambda,
  TaskHandle Function(GeoCoordinates, SearchOptions, SearchCallback) searchByCoordinatesLambda,
  TaskHandle Function(PlaceIdQuery, LanguageCode?, PlaceIdSearchCallback) searchByPlaceIdLambda,
  TaskHandle Function(PickedPlace, LanguageCode?, PlaceIdSearchCallback) searchByPickedPlaceLambda,
  TaskHandle Function(TextQuery, SearchOptions, SuggestCallback) suggestByTextLambda,

) => SearchInterface$Lambdas(
  searchByTextLambda,
  searchByAddressLambda,
  searchByCategoryLambda,
  searchByCoordinatesLambda,
  searchByPlaceIdLambda,
  searchByPickedPlaceLambda,
  suggestByTextLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

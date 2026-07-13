---
title: "searchByPlaceIdWithLanguageCodeExtended method - SearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-searchengine-searchbyplaceidwithlanguagecodeextended"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByPlaceIdWithLanguageCodeExtended</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByPlaceIdWithLanguageCodeExtended</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-searchByPlaceIdWithLanguageCodeExtended-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidquery-class">PlaceIdQuery</a></span> <span class="parameter-name">query</span>, </span>
2.  <span id="sdk-for-flutter-explore-searchByPlaceIdWithLanguageCodeExtended-param-languageCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?</span> <span class="parameter-name">languageCode</span>, </span>
3.  <span id="sdk-for-flutter-explore-searchByPlaceIdWithLanguageCodeExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-placeidsearchcallbackextended">PlaceIdSearchCallbackExtended</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request to search for a <a href="sdk-for-flutter-explore-search-place-class">Place</a> based on its ID and <a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>.

- `query` The id of place to search.

- `languageCode` The preferred language for the search results. When unset or unsupported language is chosen, results will be returned in their local language.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByPlaceIdWithLanguageCodeExtended(PlaceIdQuery query, LanguageCode? languageCode, PlaceIdSearchCallbackExtended callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


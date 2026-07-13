---
title: "searchByPlaceId method - SearchInterface class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-searchinterface-searchbyplaceid"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByPlaceId</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByPlaceId</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-searchByPlaceId-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-placeidquery-class">PlaceIdQuery</a></span> <span class="parameter-name">query</span>, </span>
2.  <span id="sdk-for-flutter-navigate-searchByPlaceId-param-languageCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>?</span> <span class="parameter-name">languageCode</span>, </span>
3.  <span id="sdk-for-flutter-navigate-searchByPlaceId-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-placeidsearchcallback">PlaceIdSearchCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous search for a <a href="sdk-for-flutter-navigate-search-place-class">Place</a> based on its ID and <a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>.

- `query` The id of place to search.

- `languageCode` The preferred language for the search results. When unset or unsupported language is chosen, results will be returned in their local language.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByPlaceId(PlaceIdQuery query, LanguageCode? languageCode, PlaceIdSearchCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


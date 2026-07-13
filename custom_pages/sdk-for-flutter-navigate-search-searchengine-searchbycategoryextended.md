---
title: "searchByCategoryExtended method - SearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-searchengine-searchbycategoryextended"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByCategoryExtended</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByCategoryExtended</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-searchByCategoryExtended-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-categoryquery-class">CategoryQuery</a></span> <span class="parameter-name">query</span>, </span>
2.  <span id="sdk-for-flutter-navigate-searchByCategoryExtended-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-navigate-searchByCategoryExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchcallbackextended">SearchCallbackExtended</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request to do a category search for <a href="sdk-for-flutter-navigate-search-place-class">Place</a> instances.

A list containing at least one <a href="sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a> must be provided as part of the `SearchEngine.searchByCategoryExtended.query`.

- `query` Query with list of desired categories.

- `options` Search options.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByCategoryExtended(CategoryQuery query, SearchOptions options, SearchCallbackExtended callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


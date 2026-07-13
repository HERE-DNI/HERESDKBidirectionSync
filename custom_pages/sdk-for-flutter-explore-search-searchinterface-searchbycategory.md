---
title: "searchByCategory method - SearchInterface class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-searchinterface-searchbycategory"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByCategory</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByCategory</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-searchByCategory-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-categoryquery-class">CategoryQuery</a></span> <span class="parameter-name">query</span>, </span>
2.  <span id="sdk-for-flutter-explore-searchByCategory-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-explore-searchByCategory-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous category search for <a href="sdk-for-flutter-explore-search-place-class">Place</a> instances.

A list containing at least one <a href="sdk-for-flutter-explore-search-placecategory-class">PlaceCategory</a> must be provided as part of the `SearchInterface.searchByCategory.query`.

- `query` Query with list of desired categories.

- `options` Search options.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByCategory(CategoryQuery query, SearchOptions options, SearchCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


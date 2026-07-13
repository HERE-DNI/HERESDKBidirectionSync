---
title: "searchByAddress method - SearchInterface class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-searchinterface-searchbyaddress"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByAddress</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByAddress</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-searchByAddress-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-addressquery-class">AddressQuery</a></span> <span class="parameter-name">query</span>, </span>
2.  <span id="sdk-for-flutter-explore-searchByAddress-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-explore-searchByAddress-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous address query search for <a href="sdk-for-flutter-explore-search-place-class">Place</a> instances.

This is the same type of search as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one <a href="sdk-for-flutter-explore-search-place-class">Place</a> result, although all found places will share the same geographic coordinates. The returned places are sorted by relevance.

- `query` Desired free-form address query text to search.

- `options` Search options.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByAddress(AddressQuery query, SearchOptions options, SearchCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


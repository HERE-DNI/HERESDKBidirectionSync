---
title: "searchByAddressExtended method - SearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-searchengine-searchbyaddressextended"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByAddressExtended</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByAddressExtended</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-searchByAddressExtended-param-query" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-addressquery-class">AddressQuery</a></span> <span class="parameter-name">query</span>, </span>
2.  <span id="sdk-for-flutter-navigate-searchByAddressExtended-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-navigate-searchByAddressExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchcallbackextended">SearchCallbackExtended</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request to search for places based on a given address.

This is the same process as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one <a href="sdk-for-flutter-navigate-search-place-class">Place</a> result, although all found places will share the same geographic coordinates. Provides candidate places sorted by relevance.

- `query` Desired free-form address query text to search.

- `options` Search options.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByAddressExtended(AddressQuery query, SearchOptions options, SearchCallbackExtended callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


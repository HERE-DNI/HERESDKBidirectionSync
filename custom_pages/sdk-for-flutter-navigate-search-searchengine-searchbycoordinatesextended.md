---
title: "searchByCoordinatesExtended method - SearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-searchengine-searchbycoordinatesextended"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByCoordinatesExtended.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByCoordinatesExtended</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByCoordinatesExtended</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-searchByCoordinatesExtended-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span>
2.  <span id="sdk-for-flutter-navigate-searchByCoordinatesExtended-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-navigate-searchByCoordinatesExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchcallbackextended">SearchCallbackExtended</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request to search for places based on given geographic coordinates.

This is the same process as reverse geocoding, except that more data is returned than just the <a href="sdk-for-flutter-navigate-search-address-class">Address</a> that belongs to given coordinates. Note that coordinates can belong to more than one <a href="sdk-for-flutter-navigate-search-place-class">Place</a> result. Provides candidate places sorted by relevance.

- `coordinates` The coordinates where to search.

- `options` Search options.

- `callback` Callback which receives result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByCoordinatesExtended(GeoCoordinates coordinates, SearchOptions options, SearchCallbackExtended callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

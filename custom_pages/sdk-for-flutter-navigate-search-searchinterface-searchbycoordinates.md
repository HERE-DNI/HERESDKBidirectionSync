---
title: "searchByCoordinates method - SearchInterface class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-searchinterface-searchbycoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByCoordinates.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByCoordinates</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByCoordinates</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-searchByCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span>
2.  <span id="sdk-for-flutter-navigate-searchByCoordinates-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-navigate-searchByCoordinates-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-searchcallback">SearchCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous search for <a href="sdk-for-flutter-navigate-search-place-class">Place</a> instances based on the given geographic coordinates.

This is the same search type as reverse geocoding, except that more data is returned than just the <a href="sdk-for-flutter-navigate-search-address-class">Address</a> related to the given coordinates. Note that more than one <a href="sdk-for-flutter-navigate-search-place-class">Place</a> can be related to the given coordinates. The returned places are sorted by relevance.

- `coordinates` The coordinates where to search.

- `options` Search options.

- `callback` Callback which receives result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByCoordinates(GeoCoordinates coordinates, SearchOptions options, SearchCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

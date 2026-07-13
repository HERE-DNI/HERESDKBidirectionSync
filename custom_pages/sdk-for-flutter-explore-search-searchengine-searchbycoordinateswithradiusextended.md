---
title: "searchByCoordinatesWithRadiusExtended method - SearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-searchengine-searchbycoordinateswithradiusextended"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/SearchEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByCoordinatesWithRadiusExtended</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByCoordinatesWithRadiusExtended</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-searchByCoordinatesWithRadiusExtended-param-circle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a></span> <span class="parameter-name">circle</span>, </span>
2.  <span id="sdk-for-flutter-explore-searchByCoordinatesWithRadiusExtended-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-explore-searchByCoordinatesWithRadiusExtended-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-searchcallbackextended">SearchCallbackExtended</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request to search for places based on given circular spatial filter.

This is the same process as reverse geocoding, except that more data is returned than just the <a href="sdk-for-flutter-explore-search-address-class">Address</a> that belongs to given coordinates. Note that coordinates can belong to more than one <a href="sdk-for-flutter-explore-search-place-class">Place</a> result. Provides candidate places sorted by relevance and located inside the radius of filter.

- `circle` The coordinates where to search and radius of the circular spatial filter. Passed in form of <a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a>.

- `options` Search options.

- `callback` Callback which receives result on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByCoordinatesWithRadiusExtended(GeoCircle circle, SearchOptions options, SearchCallbackExtended callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


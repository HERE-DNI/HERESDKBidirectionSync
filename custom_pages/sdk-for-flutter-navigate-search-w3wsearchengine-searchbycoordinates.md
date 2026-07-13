---
title: "searchByCoordinates method - W3WSearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-w3wsearchengine-searchbycoordinates"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/W3WSearchEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">searchByCoordinates</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">searchByCoordinates</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-searchByCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span>
2.  <span id="sdk-for-flutter-navigate-searchByCoordinates-param-language" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">language</span>, </span>
3.  <span id="sdk-for-flutter-navigate-searchByCoordinates-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-w3wsearchcallback">W3WSearchCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request to search for a <a href="sdk-for-flutter-navigate-search-w3wsquare-class">W3WSquare</a>, which includes the 3 word address, that corresponds to the given coordinates.

- `coordinates` The coordinates where to search.

- `language` A supported 3 word address language as an ISO 639-1 2 letter code. For Bosnian-Croatian-Montenegrin-Serbian use "oo". Defaults to "en" (English).

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that can be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle searchByCoordinates(GeoCoordinates coordinates, String? language, W3WSearchCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


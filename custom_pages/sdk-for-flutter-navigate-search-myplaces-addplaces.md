---
title: "addPlaces method - MyPlaces class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-myplaces-addplaces"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/MyPlaces-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">addPlaces</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">addPlaces</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-addPlaces-param-places" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-geoplace-class">GeoPlace</a></span>\></span></span> <span class="parameter-name">places</span>, </span>
2.  <span id="sdk-for-flutter-navigate-addPlaces-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-ontaskcompleted">OnTaskCompleted</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Adds a list of places to this data source.

- `places` Places

- `callback` The callback to be called when task is completed.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle addPlaces(List<GeoPlace> places, OnTaskCompleted callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


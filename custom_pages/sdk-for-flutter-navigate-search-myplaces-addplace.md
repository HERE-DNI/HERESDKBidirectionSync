---
title: "addPlace method - MyPlaces class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-myplaces-addplace"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addPlace.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/MyPlaces-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">addPlace</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">addPlace</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-addPlace-param-place" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-geoplace-class">GeoPlace</a></span> <span class="parameter-name">place</span>, </span>
2.  <span id="sdk-for-flutter-navigate-addPlace-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-ontaskcompleted">OnTaskCompleted</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Adds a place to this data source.

- `place` The place.

- `callback` The callback to be called when task is completed.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle addPlace(GeoPlace place, OnTaskCompleted callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

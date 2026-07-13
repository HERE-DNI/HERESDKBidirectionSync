---
title: "removePlace method - MyPlaces class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-myplaces-removeplace"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- removePlace.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/MyPlaces-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">removePlace</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">removePlace</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-removePlace-param-placeId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">placeId</span>, </span>
2.  <span id="sdk-for-flutter-navigate-removePlace-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-ontaskcompleted">OnTaskCompleted</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Removes a place from this data source.

- `placeId` The place id

- `callback` The callback to be called when task is completed.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle removePlace(String placeId, OnTaskCompleted callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

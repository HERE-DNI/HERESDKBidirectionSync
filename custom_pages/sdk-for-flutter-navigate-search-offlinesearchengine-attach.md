---
title: "attach method - OfflineSearchEngine class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-offlinesearchengine-attach"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- attach.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/OfflineSearchEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">attach</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">attach</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-attach-param-dataSource" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-myplaces-class">MyPlaces</a></span> <span class="parameter-name">dataSource</span>, </span>
2.  <span id="sdk-for-flutter-navigate-attach-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-ontaskcompleted">OnTaskCompleted</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Attach data source into SearchEngine instance.

Places from MyPlaces ranked the same way as places from default source. New data source replaces old one. Note: Only OfflineSearchEngine supports search over MyPlaces.

- `dataSource` The data source.

- `callback` The callback to be called when task is completed.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle attach(MyPlaces dataSource, OnTaskCompleted callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

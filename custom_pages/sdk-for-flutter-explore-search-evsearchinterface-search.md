---
title: "search method - EVSearchInterface class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evsearchinterface-search"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/EVSearchInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">search</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">search</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-search-param-ids" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">ids</span>, </span>
2.  <span id="sdk-for-flutter-explore-search-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-evsearchcallback">EVSearchCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request for <a href="sdk-for-flutter-explore-search-evcharginglocation-class">EVChargingLocation</a> instances with given Place IDs.

- `ids` List of charging location identifiers.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle search(List<String> ids, EVSearchCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "retrieveCatalogsUpdateInfo method - MapUpdater class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapUpdater-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">retrieveCatalogsUpdateInfo</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">retrieveCatalogsUpdateInfo</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-retrieveCatalogsUpdateInfo-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback">CatalogsUpdateInfoCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Retrieves information of all catalogs that have newer version available.

This method can also be used to query catalog information like HRN, current installed version and newer available version on server. An empty list in <a href="sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback">CatalogsUpdateInfoCallback</a> represent no map updates.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. A handle to cancel a pending operation.

</div>

## Implementation

``` dart
TaskHandle retrieveCatalogsUpdateInfo(CatalogsUpdateInfoCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


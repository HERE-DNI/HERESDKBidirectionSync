---
title: "CatalogsUpdateInfoCallback typedef - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">CatalogsUpdateInfoCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">CatalogsUpdateInfoCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">error</span>, </span><span id="sdk-for-flutter-navigate-param-catalogs" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-class">CatalogUpdateInfo</a></span>\></span>?</span> <span class="parameter-name">catalogs</span></span>)</span></span>

</div>

<div class="section desc markdown">

This method will be called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo">MapUpdater.retrieveCatalogsUpdateInfo</a> has been completed.

The first parameter indicates an error in case of a failure. The second parameter contains the results. Both parameters cannot be `null` at the same time - or not `null` at the same time. An empty `CatalogUpdateInfo` list represent no map updates.

- `error` Represents an error in case of a failure. It is `null` for an operation that succeeds.

- `catalogs` Represents a list of all catalogs that can be updated. It is `null` in case of an error.

</div>

## Implementation

``` dart
typedef CatalogsUpdateInfoCallback = void Function(MapLoaderError? error, List<CatalogUpdateInfo>? catalogs);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


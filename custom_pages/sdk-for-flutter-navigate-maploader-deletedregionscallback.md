---
title: "DeletedRegionsCallback typedef - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-deletedregionscallback"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">DeletedRegionsCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">DeletedRegionsCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-maploaderError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">maploaderError</span>, </span><span id="sdk-for-flutter-navigate-param-regions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>\></span>?</span> <span class="parameter-name">regions</span></span>)</span></span>

</div>

<div class="section desc markdown">

A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapdownloader-deleteregions">MapDownloader.deleteRegions</a> has been completed.

- `maploaderError` Represents an error in case of a failure. It is \[null\] for an operation that succeeds.

- `regions` Represents a list of successfully removed map regions. It is \[null\] in case of an error.

</div>

## Implementation

``` dart
typedef DeletedRegionsCallback = void Function(MapLoaderError? maploaderError, List<RegionId>? regions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


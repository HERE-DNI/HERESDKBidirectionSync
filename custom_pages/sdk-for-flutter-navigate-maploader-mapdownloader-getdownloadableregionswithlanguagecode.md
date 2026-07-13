---
title: "getDownloadableRegionsWithLanguageCode method - MapDownloader class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getDownloadableRegionsWithLanguageCode</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">getDownloadableRegionsWithLanguageCode</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getDownloadableRegionsWithLanguageCode-param-languageCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a></span> <span class="parameter-name">languageCode</span>, </span>
2.  <span id="sdk-for-flutter-navigate-getDownloadableRegionsWithLanguageCode-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-downloadableregionscallback">DownloadableRegionsCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request to fetch a list of <a href="sdk-for-flutter-navigate-maploader-region-class">Region</a> objects with <a href="sdk-for-flutter-navigate-maploader-region-name">Region.name</a> in given `MapDownloader.getDownloadableRegionsWithLanguageCode.languageCode`, that can be used to download the actual map data in a separate request.

- `languageCode` The language code determines the language of <a href="sdk-for-flutter-navigate-maploader-region-name">Region.name</a>.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

</div>

## Implementation

``` dart
TaskHandle getDownloadableRegionsWithLanguageCode(LanguageCode languageCode, DownloadableRegionsCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


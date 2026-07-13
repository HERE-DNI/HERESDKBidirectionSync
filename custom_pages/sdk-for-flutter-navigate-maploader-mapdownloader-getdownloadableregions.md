---
title: "getDownloadableRegions method - MapDownloader class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getDownloadableRegions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getDownloadableRegions</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">getDownloadableRegions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getDownloadableRegions-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-downloadableregionscallback">DownloadableRegionsCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request to fetch a list of <a href="sdk-for-flutter-navigate-maploader-region-class">Region</a> objects for downloading map data in a separate request.

The default language for <a href="sdk-for-flutter-navigate-maploader-region-name">Region.name</a> is <a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode.enUs</a>.

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

</div>

## Implementation

``` dart
TaskHandle getDownloadableRegions(DownloadableRegionsCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "onDownloadRegionsComplete method - DownloadRegionsStatusListener class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/DownloadRegionsStatusListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onDownloadRegionsComplete</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onDownloadRegionsComplete</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onDownloadRegionsComplete-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">error</span>, </span>
2.  <span id="sdk-for-flutter-navigate-onDownloadRegionsComplete-param-regions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>\></span>?</span> <span class="parameter-name">regions</span></span>

)

</div>

<div class="section desc markdown">

Called after the download for all requested regions has been completed with success or failure.

In this callback, failure represents non-retryable error (eg. authentication failure because of invalid credentials and similars). Temporary failures (eg. network errors) are notified through <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-onpause">DownloadRegionsStatusListener.onPause</a> and downloads will be in paused state so they can be resumed later. Invoked on the main thread.

- `error` Represents an error in case of a failure. It is `null` for an operation that succeeds.

- `regions` Represents a list of regions which has been downloaded. It is `null` in case of an error.

</div>

## Implementation

``` dart
void onDownloadRegionsComplete(MapLoaderError? error, List<RegionId>? regions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "onProgress method - DownloadRegionsStatusListener class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-onprogress"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/DownloadRegionsStatusListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onProgress</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onProgress</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onProgress-param-region" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span> <span class="parameter-name">region</span>, </span>
2.  <span id="sdk-for-flutter-navigate-onProgress-param-percentage" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">percentage</span></span>

)

</div>

<div class="section desc markdown">

Called multiple times to indicate the download progress for each requested region individually.

Invoked on the main thread.

- `region` Represents an id of region status update is related to.

- `percentage` Represents a percentage of data which has been downloaded for particular region.

</div>

## Implementation

``` dart
void onProgress(RegionId region, int percentage);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


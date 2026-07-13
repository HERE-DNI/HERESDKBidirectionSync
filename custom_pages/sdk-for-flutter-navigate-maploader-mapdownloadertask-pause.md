---
title: "pause method - MapDownloaderTask class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloadertask-pause"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloaderTask-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">pause</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">pause</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Pauses the ongoing map download operation.

Operation can be resumed afterwards. It will do nothing if operation is not in running state. Status of the call will be reported via <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-onpause">DownloadRegionsStatusListener.onPause</a>.

</div>

## Implementation

``` dart
void pause();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


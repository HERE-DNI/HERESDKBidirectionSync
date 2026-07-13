---
title: "cancel method - MapDownloaderTask class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloadertask-cancel"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloaderTask-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">cancel</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">cancel</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Cancels the ongoing map download operation.

Operation cannot be resumed afterwards. It will do nothing if the task was already cancelled or has been completed. Status of the call will be reported via <a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">DownloadRegionsStatusListener.onDownloadRegionsComplete</a>. <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.operationCancelled</a> will be reported for successful cancel.

</div>

## Implementation

``` dart
void cancel();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


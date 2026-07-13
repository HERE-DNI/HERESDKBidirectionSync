---
title: "getInitialPersistentMapStatus method - MapDownloader class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getinitialpersistentmapstatus"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getInitialPersistentMapStatus</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a></span> <span class="name">getInitialPersistentMapStatus</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Gets the initial status of the already downloaded regions at start-up time of the app.

It is not recommended to download or to upload map data while an app is running in background. However, it can happen, that an app gets shut down during an ongoing operation, for example, due to a crash. In such a case, some or all of the downloaded map data may be in a corrupted state. Refer to the <a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a> for exact healing procedure for specific status. Note: This value will not change during the lifetime of an app.

Returns <a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a>. Initial status of the persistent map.

</div>

## Implementation

``` dart
PersistentMapStatus getInitialPersistentMapStatus();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


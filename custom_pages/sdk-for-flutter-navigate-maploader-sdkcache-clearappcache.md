---
title: "clearAppCache method - SDKCache class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-sdkcache-clearappcache"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/SDKCache-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">clearAppCache</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">clearAppCache</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-clearAppCache-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-sdkcachecallback">SDKCacheCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Clears all data that is currently stored in the SDK cache.

Path for cache is specified by <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-cachepath">SDKOptions.cachePath</a>. The operation can have unexpected behaviour when it is called during a map interaction, during turn-by-turn navigation (only available for the Navigate license) or during ongoing requests initiated by the OfflineSearchEngine or the OfflineRouteEngine (only available for the Navigate license).

- `callback` Callback which receives the result on the main thread.

</div>

## Implementation

``` dart
void clearAppCache(SDKCacheCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "autoUpdateOfOnlineCache property - SDKOptions class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-sdkoptions-autoupdateofonlinecache"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">autoUpdateOfOnlineCache</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">autoUpdateOfOnlineCache</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Parameter to enable automatic cache updates.

When it is false, the cache will always use the same map version as offline maps. If offline maps are updated, the cache will be also updated. The cache version will never be older than the offline maps version.

When it is true, the cache will be automatically updated to use the latest map data that is available. In that case, the cache may contain map data that is newer than the offline maps data. Note that auto updates may also lead to increased network traffic, as the cached data will be evicted tile-by-tile before it is filled with newer map data. This process continues everytime the user views a new map view area until the data is replaced. Once also the offline map data is updated by the user, both map versions will be the same again.

If the value is also specified via the manifest (Android) or plist (iOS), than the value set via `SDKOptions` will overrule the value that was set in manifest/plist - until the current session ends and the value is read/set again.

Note that offline maps are only available for the Navigate license.

Defaults to `false`.

**Note:** Do not use this yet, the behavior of this feature may be inconsistent. Once it will be usable, it will be announced in the regular HERE SDK release notes.

</div>

## Implementation

``` dart
bool autoUpdateOfOnlineCache;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


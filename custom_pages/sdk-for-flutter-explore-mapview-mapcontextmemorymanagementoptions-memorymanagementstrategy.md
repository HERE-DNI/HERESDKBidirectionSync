---
title: "memoryManagementStrategy property - MapContextMemoryManagementOptions class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-memorymanagementstrategy"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapContextMemoryManagementOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">memoryManagementStrategy</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementstrategy">MapContextMemoryManagementStrategy</a> <span class="name">memoryManagementStrategy</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The default setting MemoryManagementStrategy.DYNAMIC is suitable for common cases. The map data cache can adjust dynamically to fit visible data. When the visible data needs extra memory, it would increase. When it's not needed, it will reduce to a limit which is calculated internally or by using <a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-tilecachememorylimitinkib">MapContextMemoryManagementOptions.tileCacheMemoryLimitInKiB</a> option. The MemoryManagementStrategy.FIXED would be only useful when there is very strict memory consumption requirement for the application. It potentially can have flickering visual artifacts when the map data to be visualized is very large and exceeds the cache limit.

</div>

## Implementation

``` dart
MapContextMemoryManagementStrategy memoryManagementStrategy;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


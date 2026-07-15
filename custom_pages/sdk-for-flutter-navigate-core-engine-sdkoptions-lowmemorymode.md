---
title: "lowMemoryMode property - SDKOptions class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core-engine-sdkoptions-lowmemorymode"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">lowMemoryMode</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">lowMemoryMode</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

If an application runs in a memory-constrained environment, enable this option to reduce the HERE SDK's memory footprint. When set to `true` configures internal memory caches to consume less memory. Reduction in cache sizes also reduces performance of the HERE SDK. In order to release memory occupied by internal caches see <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-purgememorycaches">SDKNativeEngine.purgeMemoryCaches</a>.

</div>

## Implementation

``` dart
bool lowMemoryMode;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


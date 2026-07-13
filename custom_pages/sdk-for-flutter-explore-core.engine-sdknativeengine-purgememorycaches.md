---
title: "purgeMemoryCaches method - SDKNativeEngine class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-sdknativeengine-purgememorycaches"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">purgeMemoryCaches</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">purgeMemoryCaches</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-purgeMemoryCaches-param-strategy" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-sdknativeenginepurgememorystrategy">SDKNativeEnginePurgeMemoryStrategy</a></span> <span class="parameter-name">strategy</span></span>

)

</div>

<div class="section desc markdown">

Releases memory occupied by internal caches.

Purging caches reduces memory footprint of application and may temporary reduce performance.

- `strategy` Option to control how much memory caches will be purged.

</div>

## Implementation

``` dart
void purgeMemoryCaches(SDKNativeEnginePurgeMemoryStrategy strategy);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "setMemoryManagementOptions method - MapContext class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcontext-setmemorymanagementoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setMemoryManagementOptions.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapContext-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setMemoryManagementOptions</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setMemoryManagementOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-setMemoryManagementOptions-param-memoryManagementOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-class">MapContextMemoryManagementOptions</a></span> <span class="parameter-name">memoryManagementOptions</span>, </span>
2.  <span id="sdk-for-flutter-explore-setMemoryManagementOptions-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcontextsetmemorymanagementoptionscallback">MapContextSetMemoryManagementOptionsCallback</a>?</span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Sets memory management options for controlling tile cache and video memory usage.

In <a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-class">MapContextMemoryManagementOptions</a> optional parameters with `null` or non positive values will be ignored, preserving their existing settings.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

- `memoryManagementOptions` The memory management options to set.

- `callback` Optional callback used upon completion to pass the return value to the caller. The callback is called from an arbitrary thread.

</div>

## Implementation

``` dart
void setMemoryManagementOptions(MapContextMemoryManagementOptions memoryManagementOptions, MapContextSetMemoryManagementOptionsCallback? callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

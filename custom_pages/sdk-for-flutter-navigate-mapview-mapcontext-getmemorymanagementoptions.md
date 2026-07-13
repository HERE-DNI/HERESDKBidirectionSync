---
title: "getMemoryManagementOptions method - MapContext class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcontext-getmemorymanagementoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getMemoryManagementOptions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapContext-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getMemoryManagementOptions</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class">MapContextMemoryManagementOptions</a></span> <span class="name">getMemoryManagementOptions</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Returns <a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class">MapContextMemoryManagementOptions</a>. Gets the current memory management options. Returns the actual applied memory limits. If the underlying system limits exceed int32_t max value (2,147,483,647 KiB or ~2 TiB), the returned value is clamped to int32_t max.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
MapContextMemoryManagementOptions getMemoryManagementOptions();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "ElectronicHorizonPosition constructor - ElectronicHorizonPosition - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizonposition-electronichorizonposition"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonPosition-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">ElectronicHorizonPosition</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">ElectronicHorizonPosition</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-pathIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">pathIndex</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-pathSegmentIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">pathSegmentIndex</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-pathSegmentOffsetInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">pathSegmentOffsetInMeters</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

Offline availability: This property is available online and offline.

- `pathIndex` The index of the current path in the list of <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizon-paths">ElectronicHorizon.paths</a>.
- `pathSegmentIndex` The index of the segment inside the <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-segments">ElectronicHorizonPath.segments</a>.
- `pathSegmentOffsetInMeters` The offset from the start of the segment in meters.

</div>

## Implementation

``` dart
ElectronicHorizonPosition(this.pathIndex, this.pathSegmentIndex, this.pathSegmentOffsetInMeters);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


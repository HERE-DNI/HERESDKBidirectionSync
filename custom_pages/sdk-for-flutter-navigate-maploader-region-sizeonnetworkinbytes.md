---
title: "sizeOnNetworkInBytes property - Region class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-region-sizeonnetworkinbytes"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/Region-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">sizeOnNetworkInBytes</span> property

</div>

<div class="section multi-line-signature">

int <span class="name">sizeOnNetworkInBytes</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Region size, for downloading/during network operations, in bytes. Regions are downloaded in compressed form and hence they have reduced size on network. Note: This value represents the theoretical maximum size required for the region during transfer. If overlapping data already exists, the actual size downloaded may be smaller due to map data reuse.

</div>

## Implementation

``` dart
int sizeOnNetworkInBytes;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


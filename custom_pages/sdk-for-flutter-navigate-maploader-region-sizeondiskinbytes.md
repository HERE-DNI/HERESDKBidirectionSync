---
title: "sizeOnDiskInBytes property - Region class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-region-sizeondiskinbytes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- sizeOnDiskInBytes.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/Region-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">sizeOnDiskInBytes</span> property

</div>

<div class="section multi-line-signature">

int <span class="name">sizeOnDiskInBytes</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Represents the total size of the region on disk in bytes, assuming no pre-existing data on the disk. This value is a theoretical maximum for the region's size allocation. Note: If overlapping regions exist or data is already present on the disk, the actual size occupied might be less than this value due to shared or reused map data.

</div>

## Implementation

``` dart
int sizeOnDiskInBytes;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

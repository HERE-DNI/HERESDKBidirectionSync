---
title: "temporaryDiskRequirementInBytes property - CatalogUpdateInfo class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-catalogupdateinfo-temporarydiskrequirementinbytes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- temporaryDiskRequirementInBytes.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/CatalogUpdateInfo-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">temporaryDiskRequirementInBytes</span> property

</div>

<div class="section multi-line-signature">

int <span class="name">temporaryDiskRequirementInBytes</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Performing an update requires additional storage on top of existing offline maps. This space is used to store intermittent copy of map content according to the specified <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy</a>. **Note** In order to estimate, if catalog update is feasible, given the amount of free space on the disk, application can compare amount of the free space on the disk with `disk_size_in_bytes + temporary_disk_requirement_in_bytes`.

</div>

## Implementation

``` dart
int temporaryDiskRequirementInBytes;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

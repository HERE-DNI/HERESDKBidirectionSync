---
title: "TileSourceDataVersion constructor - TileSourceDataVersion - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview-datasource-tilesourcedataversion-tilesourcedataversion"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/TileSourceDataVersion-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TileSourceDataVersion</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TileSourceDataVersion</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-majorVersion" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">majorVersion</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-minorVersion" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">minorVersion</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `majorVersion` Major version number. Describes changes in underlying data that would require a complete reload (e.g. geometry changes).
- `minorVersion` Minor version number. Describes changes in underlying data that would not require a complete reload (e.g. attributes changes).

</div>

## Implementation

``` dart
TileSourceDataVersion(this.majorVersion, this.minorVersion);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


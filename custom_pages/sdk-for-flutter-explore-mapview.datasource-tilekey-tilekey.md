---
title: "TileKey constructor - TileKey - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-tilekey-tilekey"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TileKey.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/TileKey-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TileKey</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TileKey</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-x" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">x</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-y" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">y</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-level" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">level</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `x` X coordinate of the tile. This ranges from 0 to 2^level − 1.
- `y` Y coordinate of the tile. This ranges from 0 to 2^level − 1.
- `level` Level of the tile. Supported range \[0, 31\].

</div>

## Implementation

``` dart
TileKey(this.x, this.y, this.level);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

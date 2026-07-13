---
title: "TileUrlProviderCallback typedef - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-tileurlprovidercallback"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">TileUrlProviderCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">TileUrlProviderCallback</span> = <span class="returntype">String Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-x" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">x</span>, </span><span id="sdk-for-flutter-navigate-param-y" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">y</span>, </span><span id="sdk-for-flutter-navigate-param-level" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">level</span></span>)</span></span>

</div>

<div class="section desc markdown">

Provides the URL as String for the given tile coordinates and storage level.

The first and second parameters correspond to the X and Y coordinates of the tile, respectively, and have values ranging from 0 to 2^level − 1. The third parameter indicates the level of the tile.

- `x` X coordinate of the tile. This ranges from 0 to 2^level − 1.

- `y` Y coordinate of the tile. This ranges from 0 to 2^level − 1.

- `level` Level of the tile.

Returns the URL.

</div>

## Implementation

``` dart
typedef TileUrlProviderCallback = String Function(int x, int y, int level);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


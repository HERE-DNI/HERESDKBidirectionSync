---
title: "mapContentCategoriesToBlock property - MapPolyline class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mappolyline-mapcontentcategoriestoblock"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolyline-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">mapContentCategoriesToBlock</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapcontentcategory">MapContentCategory</a></span>\></span></span> <span class="name">mapContentCategoriesToBlock</span>

</div>

<div class="section desc markdown">

List of map content categories this polyline should block. Gets list of map content categories this polyline should block.

Default value is an empty list meaning none of the map categories will be blocked.

</div>

## Implementation

``` dart
List<MapContentCategory> get mapContentCategoriesToBlock;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">mapContentCategoriesToBlock=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-mapContentCategoriesToBlock-param-value" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapcontentcategory">MapContentCategory</a></span>\></span></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

List of map content categories this polyline should block. Sets list of map content categories this polyline should block.

Map content categories overlapping the polyline geometry (progress and non-progress) will be discarded from being rendered.

Duplicate entries will be ignored and will have no additional effect.

</div>

## Implementation

``` dart
set mapContentCategoriesToBlock(List<MapContentCategory> value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


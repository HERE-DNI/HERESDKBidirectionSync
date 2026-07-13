---
title: "corridorArea property - CategoryQueryArea class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-categoryqueryarea-corridorarea"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/CategoryQueryArea-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">corridorArea</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a>? <span class="name">corridorArea</span>

<div class="features">

<span class="feature">final</span>

</div>

</div>

<div class="section desc markdown">

Geographic corridor area in which to provide the most relevant places. The contained polyline and half-width define the area that will be used in a search query.

When used with `SearchEngine`, the polyline is compressed and sent. More complex polylines with large amounts of coordinates and with smaller half-width may have the less relevant part removed, such as the one far away from the search center. This usually makes no difference, because there will be enough POIs near the search center. For use cases where it is important to search the entire polyline, half-width can be increased or not set. For example: Route between New York and Chicago with half-width 800 will be added to request without removing the far away part, but route of the same length (around 360km) between Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.

When <a href="sdk-for-flutter-explore-search-categoryqueryarea-corridorarea">CategoryQueryArea.corridorArea</a> is provided, <a href="sdk-for-flutter-explore-search-categoryqueryarea-areacenter">CategoryQueryArea.areaCenter</a> has to be within it, otherwise <a href="sdk-for-flutter-explore-search-categoryqueryarea-areacenter">CategoryQueryArea.areaCenter</a> is ignored when searching.

</div>

## Implementation

``` dart
final GeoCorridor? corridorArea;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


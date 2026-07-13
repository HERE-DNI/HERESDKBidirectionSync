---
title: "TextQueryArea.withCorridor constructor - TextQueryArea - search library - Dart API"
slug: "sdk-for-flutter-explore-search-textqueryarea-textqueryarea-withcorridor"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/TextQueryArea-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TextQueryArea.withCorridor</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TextQueryArea.withCorridor</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withCorridor-param-corridorArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a></span> <span class="parameter-name">corridorArea</span>, </span>
2.  <span id="sdk-for-flutter-explore-withCorridor-param-areaCenter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">areaCenter</span></span>

)

</div>

<div class="section desc markdown">

Constructs a new instance of this class from provided parameters.

The given corridor and center define the area that will be used in the search query.

When used with SearchEngine, the polyline is compressed and sent. More complex polylines with large amounts of coordinates and with smaller half-width may have the less relevant part removed, such as the one far away from the search center. This usually makes no difference, because there will be enough POIs near the search center. For use cases where it is important to search the entire polyline, half-width can be increased or not set. For example: Route between New York and Chicago with half-width 800 will be added to request without removing the far away part, but route of the same length (around 360km) between Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.

The area center has to be within the corridor, otherwise it is ignored.

For Offline Search, search in a given `GeoCorridor` restricts the results to only POIs.

- `corridorArea` Geographic corridor area in which to provide the most relevant places.

- `areaCenter` Geographic coordinates of the prioritized area center.

</div>

## Implementation

``` dart
factory TextQueryArea.withCorridor(GeoCorridor corridorArea, GeoCoordinates areaCenter) => $prototype.withCorridor(corridorArea, areaCenter);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


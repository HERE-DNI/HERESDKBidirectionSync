---
title: "MapMarkerCluster.WithCounter constructor - MapMarkerCluster - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmarkercluster-mapmarkercluster-withcounter"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarkerCluster-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMarkerCluster.WithCounter</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMarkerCluster.WithCounter</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-WithCounter-param-imageStyle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarkerclusterimagestyle-class">MapMarkerClusterImageStyle</a></span> <span class="parameter-name">imageStyle</span>, </span>
2.  <span id="sdk-for-flutter-explore-WithCounter-param-counterStyle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-class">MapMarkerClusterCounterStyle</a></span> <span class="parameter-name">counterStyle</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance of a map marker cluster which is represented as an image along with a counter showing how many markers are actually grouped under particular cluster icon.

Any modification to `imageStyle` or `counterStyle` after creation of `MapMarkerCluster` does not have any effect.

- `imageStyle` Describes the visual appearance of cluster icon.

- `counterStyle` Describes the appearance of marker count label.

</div>

## Implementation

``` dart
factory MapMarkerCluster.WithCounter(MapMarkerClusterImageStyle imageStyle, MapMarkerClusterCounterStyle counterStyle) => $prototype.WithCounter(imageStyle, counterStyle);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


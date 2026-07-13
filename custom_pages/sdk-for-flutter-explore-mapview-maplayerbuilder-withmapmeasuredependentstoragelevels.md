---
title: "withMapMeasureDependentStorageLevels method - MapLayerBuilder class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-maplayerbuilder-withmapmeasuredependentstoragelevels"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapLayerBuilder-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">withMapMeasureDependentStorageLevels</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a></span> <span class="name">withMapMeasureDependentStorageLevels</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withMapMeasureDependentStorageLevels-param-mapLayerMapMeasureDependentStorageLevels" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-maplayermapmeasuredependentstoragelevels-class">MapLayerMapMeasureDependentStorageLevels</a></span> <span class="parameter-name">mapLayerMapMeasureDependentStorageLevels</span></span>

)

</div>

<div class="section desc markdown">

Applies a mapping from the map measure to the storage level.

This mapping is used by the layer to request data for the specified storage level corresponding to the map measure from the datasource. This can be used for example to fine-tune the resolution of raster layers. Note: When the map camera is significantly tilted, the storage level is further reduced for data towards the horizon. Note: Mappings that request higher storage levels will lead to an increased number of requests to the raster tile service. Providing the map measure to storage level mapping is optional. If not provided, the default mapping will use a storage level that is for raster layers one and for others three levels lower than the zoom level, corresponding to an offset of -1 and -3.

- `mapLayerMapMeasureDependentStorageLevels` The map measure to storage level mapping that should be applied for the layer.

Returns <a href="sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a>. This class instance.

</div>

## Implementation

``` dart
MapLayerBuilder withMapMeasureDependentStorageLevels(MapLayerMapMeasureDependentStorageLevels mapLayerMapMeasureDependentStorageLevels);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


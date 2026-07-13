---
title: "withStorageLevelOffset method - MapLayerMapMeasureDependentStorageLevels class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-withstorageleveloffset"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withStorageLevelOffset.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapLayerMapMeasureDependentStorageLevels-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">withStorageLevelOffset</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-class">MapLayerMapMeasureDependentStorageLevels</a></span> <span class="name">withStorageLevelOffset</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withStorageLevelOffset-param-offset" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">offset</span></span>

)

</div>

<div class="section desc markdown">

Creates an instance of <a href="sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-class">MapLayerMapMeasureDependentStorageLevels</a> with the specified storage level offset.

This creates a map where the storage level is determined by applying an "offset" to the zoom level. A negative offset results in a storage level lower than the zoom level, while a positive offset increases it. For example, with an offset of 0, the storage level matches the zoom level directly. An offset of -1 makes the storage level one less than the zoom level, and so on. The offset value is clamped to the range of -3 to 3. Note: The generated mapping adjusts so that when the map camera is significantly tilted, the storage level is further reduced for data near the horizon.

- `offset` Defines an offset of storage level from the zoom level. The value will be clamped to a range of -3 to 3.

Returns <a href="sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-class">MapLayerMapMeasureDependentStorageLevels</a>. MapLayerMapMeasureDependentStorageLevels instance.

</div>

## Implementation

``` dart
static MapLayerMapMeasureDependentStorageLevels withStorageLevelOffset(int offset) => $prototype.withStorageLevelOffset(offset);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

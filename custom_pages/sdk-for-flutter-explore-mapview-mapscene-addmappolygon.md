---
title: "addMapPolygon method - MapScene class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscene-addmappolygon"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">addMapPolygon</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">addMapPolygon</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-addMapPolygon-param-mapPolygon" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mappolygon-class">MapPolygon</a></span> <span class="parameter-name">mapPolygon</span></span>

)

</div>

<div class="section desc markdown">

Adds a map polygon to this map scene.

**Note:** Due to technical limitations using the MapPolygon API to add a very large number of polygons (especially 1000+ also depending on their complexity) is not recommended. Adding this many polygons has a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the <a href="sdk-for-flutter-explore-mapview-mapscene-class">MapScene</a> class doc.

- `mapPolygon` The map polygon to be added to this map scene.

</div>

## Implementation

``` dart
void addMapPolygon(MapPolygon mapPolygon);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


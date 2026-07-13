---
title: "addMapPolylines method - MapScene class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscene-addmappolylines"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addMapPolylines.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">addMapPolylines</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">addMapPolylines</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-addMapPolylines-param-mapPolylines" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mappolyline-class">MapPolyline</a></span>\></span></span> <span class="parameter-name">mapPolylines</span></span>

)

</div>

<div class="section desc markdown">

Adds map polylines to this map scene.

**Note:** Due to technical limitations using the MapPolyline API to add a very large number of polylines (especially 1000+ also depending on their complexity) is not recommended. Adding this many polylines has a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the <a href="sdk-for-flutter-explore-mapview-mapscene-class">MapScene</a> class doc.

- `mapPolylines` The map polylines to be added to this map scene.

</div>

## Implementation

``` dart
void addMapPolylines(List<MapPolyline> mapPolylines);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

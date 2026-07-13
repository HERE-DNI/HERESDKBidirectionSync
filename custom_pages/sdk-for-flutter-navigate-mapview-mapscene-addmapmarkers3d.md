---
title: "addMapMarkers3d method - MapScene class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapscene-addmapmarkers3d"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addMapMarkers3d.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">addMapMarkers3d</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">addMapMarkers3d</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-addMapMarkers3d-param-markers" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmarker3d-class">MapMarker3D</a></span>\></span></span> <span class="parameter-name">markers</span></span>

)

</div>

<div class="section desc markdown">

Adds multiple 3D map markers to this map scene.

Adding the same 3D marker instances multiple times has no effect.

**Note:** Due to technical limitations, using the MapMarkers3D API to add a very large number of 3D markers (especially 500+) is not recommended. Adding this many markers will have a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the <a href="sdk-for-flutter-navigate-mapview-mapscene-class">MapScene</a> class doc.

- `markers` The list of 3D markers to be added to this map scene.

</div>

## Implementation

``` dart
void addMapMarkers3d(List<MapMarker3D> markers);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "addMapMarker3d method - MapScene class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscene-addmapmarker3d"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addMapMarker3d.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">addMapMarker3d</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">addMapMarker3d</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-addMapMarker3d-param-marker" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-class">MapMarker3D</a></span> <span class="parameter-name">marker</span></span>

)

</div>

<div class="section desc markdown">

Adds a 3D map marker to this map scene.

Does nothing if the marker instance was already added to the scene.

**Note:** Due to technical limitations using the MapMarker3D API to add a very large number of 3D markers (especially 500+ also depending on the complexity of the 3D object) is not recommended. Adding this many 3D markers has a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation add only map items which are in the current camera viewport. A guide on how to achieve this can be found towards the end of the <a href="sdk-for-flutter-explore-mapview-mapscene-class">MapScene</a> class doc.

- `marker` The marker to be added to this map scene.

</div>

## Implementation

``` dart
void addMapMarker3d(MapMarker3D marker);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

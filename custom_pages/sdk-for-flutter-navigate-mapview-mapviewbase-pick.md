---
title: "pick method - MapViewBase class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapviewbase-pick"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- pick.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapViewBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">pick</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">pick</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-pick-param-filter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenemappickfilter-class">MapSceneMapPickFilter</a>?</span> <span class="parameter-name">filter</span>, </span>
2.  <span id="sdk-for-flutter-navigate-pick-param-viewArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a></span> <span class="parameter-name">viewArea</span>, </span>
3.  <span id="sdk-for-flutter-navigate-pick-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbasemappickcallback">MapViewBaseMapPickCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Returns all map content located inside the specified pick area.

Content to be picked is specified by a pick content filter. The pick area is defined by a rectangle in map view coordinates in pixels, relative to the map view's origin at (0, 0) which indicates the top-left corner of the map view.

- `filter` Filter for the map content to be picked. When a filter is not set all of the pickable content will be picked.

- `viewArea` The rectangular pixel area of the view inside which map content will be picked. View area is relative to the map view's origin at (0, 0) at the top-left corner of the map view.

- `callback` Callback to call with the result. This will be called on a main thread when pick operation completes.

</div>

## Implementation

``` dart
void pick(MapSceneMapPickFilter? filter, Rectangle2D viewArea, MapViewBaseMapPickCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

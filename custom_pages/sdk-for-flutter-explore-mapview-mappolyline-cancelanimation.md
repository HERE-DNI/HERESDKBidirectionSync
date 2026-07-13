---
title: "cancelAnimation method - MapPolyline class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mappolyline-cancelanimation"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolyline-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">cancelAnimation</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">cancelAnimation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-cancelAnimation-param-animation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-mappolylineanimation-class">MapPolylineAnimation</a></span> <span class="parameter-name">animation</span></span>

)

</div>

<div class="section desc markdown">

Cancels single ongoing animation of this map polyline.

Does nothing if the specified animation is not currently in progress for this polyline. Does not affect other polylines that might be running this animation.

- `animation` The animation to cancel

</div>

## Implementation

``` dart
void cancelAnimation(MapPolylineAnimation animation);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


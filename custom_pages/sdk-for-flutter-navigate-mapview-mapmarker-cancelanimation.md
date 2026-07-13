---
title: "cancelAnimation method - MapMarker class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-cancelanimation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- cancelAnimation.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">cancelAnimation</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">cancelAnimation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-cancelAnimation-param-animation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-mapmarkeranimation-class">MapMarkerAnimation</a></span> <span class="parameter-name">animation</span></span>

)

</div>

<div class="section desc markdown">

Cancels single ongoing animation.

Does nothing if animation was not started for this map marker.

Does not cancel other animations if the same <a href="sdk-for-flutter-navigate-animation-mapmarkeranimation-class">MapMarkerAnimation</a> object was applied to multiple `MapMarker`s.

- `animation` The animation to cancel.

</div>

## Implementation

``` dart
void cancelAnimation(MapMarkerAnimation animation);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "setAreaCameraBehaviorGeobox method - AutomotiveCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorgeobox"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setAreaCameraBehaviorGeobox.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/AutomotiveCameraBehavior-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setAreaCameraBehaviorGeobox</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setAreaCameraBehaviorGeobox</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setAreaCameraBehaviorGeobox-param-geobox" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span> <span class="parameter-name">geobox</span></span>

)

</div>

<div class="section desc markdown">

Configures the Area camera to frame the specified geographic bounding box.

The camera automatically calculates the appropriate zoom level and center position to ensure the entire area is visible within the viewport.

This function does not change <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-activecameratype">AutomotiveCameraBehavior.activeCameraType</a>. To display the configured area view, set <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-activecameratype">AutomotiveCameraBehavior.activeCameraType</a> to <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype">AutomotiveCameraBehaviorActiveCameraType.area</a>.

Calling this function overrides any previously set visible points configured via <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorvisiblepoints">AutomotiveCameraBehavior.setAreaCameraBehaviorVisiblePoints</a>.

- `geobox` The geographic bounding box to display.

</div>

## Implementation

``` dart
void setAreaCameraBehaviorGeobox(GeoBox geobox);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

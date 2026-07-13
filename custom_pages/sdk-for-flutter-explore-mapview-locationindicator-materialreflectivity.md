---
title: "materialReflectivity property - LocationIndicator class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-locationindicator-materialreflectivity"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/LocationIndicator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">materialReflectivity</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-materialreflectivity-class">MaterialReflectivity</a>?</span> <span class="name">materialReflectivity</span>

</div>

<div class="section desc markdown">

The material reflectivity properties of the location indicator. Enables per‑pixel lighting for all internal markers (navigation, pedestrian, inactive variants) and the halo when assigned. While `materialReflectivity` is non‑null the markers are shaded by scene lights using the provided ambient / diffuse factors. When set back to `null`, lighting is disabled and markers revert to unlit (emissive) rendering.

Default value is `null`. Retrieves the material reflectivity applied to all markers of location indicator.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
MaterialReflectivity? get materialReflectivity;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">materialReflectivity=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-materialReflectivity-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-materialreflectivity-class">MaterialReflectivity</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The material reflectivity properties of the location indicator. Enables per‑pixel lighting for all internal markers (navigation, pedestrian, inactive variants) and the halo when assigned. While `materialReflectivity` is non‑null the markers are shaded by scene lights using the provided ambient / diffuse factors. When set back to `null`, lighting is disabled and markers revert to unlit (emissive) rendering.

Default value is `null`. Sets the material reflectivity properties for all markers of location indicator including its halo. This value affects also any custom markers set with `setMarker3dModel`.

</div>

## Implementation

``` dart
set materialReflectivity(MaterialReflectivity? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


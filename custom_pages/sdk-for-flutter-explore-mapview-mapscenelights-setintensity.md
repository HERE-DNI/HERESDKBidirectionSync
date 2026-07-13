---
title: "setIntensity method - MapSceneLights class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscenelights-setintensity"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapSceneLights-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setIntensity</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setIntensity</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-setIntensity-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapscenelightscategory">MapSceneLightsCategory</a></span> <span class="parameter-name">category</span>, </span>
2.  <span id="sdk-for-flutter-explore-setIntensity-param-intensity" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">intensity</span>, </span>
3.  <span id="sdk-for-flutter-explore-setIntensity-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapscenelightsattributesettingcallback">MapSceneLightsAttributeSettingCallback</a>?</span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Set a new intensity for the light based on its category.

- `category` The category of light for which the intensity is set.

- `intensity` The light intensity value must be inside the range \[0, 10\]. The intensity value is clamped to this range. If the value falls outside its supported range, it will be adjusted to stay within the range. Note: When the intensity value is big, 3D objects might turn completely white because all the color channels could go over the limit of 1.0.

- `callback` Optional callback that will receive the result of this operation.

</div>

## Implementation

``` dart
void setIntensity(MapSceneLightsCategory category, double intensity, MapSceneLightsAttributeSettingCallback? callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


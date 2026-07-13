---
title: "getIntensity method - MapSceneLights class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscenelights-getintensity"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapSceneLights-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getIntensity</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">double?</span> <span class="name">getIntensity</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-getIntensity-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapscenelightscategory">MapSceneLightsCategory</a></span> <span class="parameter-name">category</span></span>

)

</div>

<div class="section desc markdown">

Retrieves the current intensity of the light based on its category.

- `category` The category of light from which the intensity is retrieved.

Returns `double?`. The current intensity of the light, or `null` if the light is missing from the loaded scene or MapScene is not intitialized.

</div>

## Implementation

``` dart
double? getIntensity(MapSceneLightsCategory category);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


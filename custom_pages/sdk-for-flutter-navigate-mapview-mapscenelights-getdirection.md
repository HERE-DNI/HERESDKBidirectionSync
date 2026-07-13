---
title: "getDirection method - MapSceneLights class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapscenelights-getdirection"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapSceneLights-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getDirection</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-class">MapSceneLightsDirection</a>?</span> <span class="name">getDirection</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getDirection-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightscategory">MapSceneLightsCategory</a></span> <span class="parameter-name">category</span></span>

)

</div>

<div class="section desc markdown">

Retrieves the current direction of the light based on its category.

- `category` The category of light from which the direction is retrieved.

Returns <a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-class">MapSceneLightsDirection?</a>. The current direction of the light, or `null` if the light is missing from the loaded scene or MapScene is not intitialized.

</div>

## Implementation

``` dart
MapSceneLightsDirection? getDirection(MapSceneLightsCategory category);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


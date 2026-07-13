---
title: "setDirection method - MapSceneLights class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapscenelights-setdirection"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setDirection.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapSceneLights-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setDirection</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setDirection</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setDirection-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightscategory">MapSceneLightsCategory</a></span> <span class="parameter-name">category</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setDirection-param-direction" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-class">MapSceneLightsDirection</a></span> <span class="parameter-name">direction</span>, </span>
3.  <span id="sdk-for-flutter-navigate-setDirection-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsattributesettingcallback">MapSceneLightsAttributeSettingCallback</a>?</span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Set a new direction for the light based on its category.

- `category` The category of light for which the direction is set.

- `direction` The Direction contains azimuth and altitude angles in degrees.

- `callback` Optional callback that will receive the result of this operation.

</div>

## Implementation

``` dart
void setDirection(MapSceneLightsCategory category, MapSceneLightsDirection direction, MapSceneLightsAttributeSettingCallback? callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "setColor method - MapSceneLights class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscenelights-setcolor"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapSceneLights-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setColor</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setColor</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-setColor-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapscenelightscategory">MapSceneLightsCategory</a></span> <span class="parameter-name">category</span>, </span>
2.  <span id="sdk-for-flutter-explore-setColor-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span>, </span>
3.  <span id="sdk-for-flutter-explore-setColor-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapscenelightsattributesettingcallback">MapSceneLightsAttributeSettingCallback</a>?</span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Set a new color for the light based on its category.

- `category` The category of light for which the color is set.

- `color` The Color type includes red, green, blue, and alpha components. The value of these components must be inside the range \[0, 1\].

- `callback` Optional callback that will receive the result of this operation.

</div>

## Implementation

``` dart
void setColor(MapSceneLightsCategory category, ui.Color color, MapSceneLightsAttributeSettingCallback? callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "isDynamicFrameRateEnabled property - VisualNavigator class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-isdynamicframerateenabled"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isDynamicFrameRateEnabled.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/VisualNavigator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">isDynamicFrameRateEnabled</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">isDynamicFrameRateEnabled</span>

</div>

<div class="section desc markdown">

Flag used to enable or disable the dynamic frame rate. Controls whether the number of map updates is dynamically calculated based on the current zoom level. If the zoom level is low, i.e., the camera target distance is high, updates to LocationIndicator, MapCamera and MapPolylines representing the route progress will happen less frequent. It is on by default.

</div>

## Implementation

``` dart
bool get isDynamicFrameRateEnabled;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">isDynamicFrameRateEnabled=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-isDynamicFrameRateEnabled-param-value" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Flag used to enable or disable the dynamic frame rate. Controls whether the number of map updates is dynamically calculated based on the current zoom level. If the zoom level is low, i.e., the camera target distance is high, updates to LocationIndicator, MapCamera and MapPolylines representing the route progress will happen less frequent. It is on by default.

</div>

## Implementation

``` dart
set isDynamicFrameRateEnabled(bool value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

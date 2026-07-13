---
title: "MapSceneLightsAttributeSettingCallback typedef - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapscenelightsattributesettingcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapSceneLightsAttributeSettingCallback.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">MapSceneLightsAttributeSettingCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">MapSceneLightsAttributeSettingCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-setLightError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsattributesettingerror">MapSceneLightsAttributeSettingError</a>?</span> <span class="parameter-name">setLightError</span></span>)</span></span>

</div>

<div class="section desc markdown">

This callback function allows handling errors that occur during the setting of light attributes.

- `setLightError` The cause for the failure when setting the light attributes, or `null` if no error occurred.

Note: The error code `NO_LIGHTS` may be returned when attempting to set light attributes in map schemes that do not support lights, for instance `road.network` map scheme.

Please refer to the error code documentation for further details on error handling.

</div>

## Implementation

``` dart
typedef MapSceneLightsAttributeSettingCallback = void Function(MapSceneLightsAttributeSettingError? setLightError);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

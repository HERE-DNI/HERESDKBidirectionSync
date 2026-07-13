---
title: "startAngularPanning method - SpatialAudioCuePanning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-startangularpanning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startAngularPanning.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/SpatialAudioCuePanning-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">startAngularPanning</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">startAngularPanning</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-startAngularPanning-param-nextCustomPanningData" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-custompanningdata-class">CustomPanningData</a>?</span> <span class="parameter-name">nextCustomPanningData</span>, </span>
2.  <span id="sdk-for-flutter-navigate-startAngularPanning-param-azimuthCallback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-spatialaudiocuepanningspatialazimuthstarted">SpatialAudioCuePanningspatialAzimuthStarted</a></span> <span class="parameter-name">azimuthCallback</span></span>

)

</div>

<div class="section desc markdown">

This method will retrieve a stream of azimuth values to be passed onto the spatial audio renderer.

An optional custom value for <a href="sdk-for-flutter-navigate-navigation-custompanningdata-estimatedaudiocueduration">CustomPanningData.estimatedAudioCueDuration</a>, <a href="sdk-for-flutter-navigate-navigation-custompanningdata-initialazimuthindegrees">CustomPanningData.initialAzimuthInDegrees</a>, or its <a href="sdk-for-flutter-navigate-navigation-custompanningdata-sweepazimuthindegrees">CustomPanningData.sweepAzimuthInDegrees</a> can be here defined if the default data does not fully match the utilized Language or TTS engine or angle expectations. If startAngularPanning is called to spatialize the audio cue of a new maneuver before the full completion of a previous spatial audio trajectory, then <a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a> will retrieve the azimuth values of the new maneuver.

- `nextCustomPanningData` Defines a new set of values related to spatial audio panning. When <a href="sdk-for-flutter-navigate-navigation-custompanningdata-class">CustomPanningData</a> is initialized as `null`, the default set of values provided by HERE SDK will be used instead.

- `azimuthCallback` Callback that will signal the next azimuth required to complete a spatial audio trajectory once the angular panning has started. Azimuth angular values are retrieved individually until the full duration of the audio trajectory has been reached, or a new text message has started its angular panning.

</div>

## Implementation

``` dart
void startAngularPanning(CustomPanningData? nextCustomPanningData, SpatialAudioCuePanningspatialAzimuthStarted azimuthCallback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

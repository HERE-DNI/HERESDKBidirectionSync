---
title: "fadeDuration property - MapMarker class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-fadeduration"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">fadeDuration</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">Duration</span> <span class="name">fadeDuration</span>

</div>

<div class="section desc markdown">

Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene. Gets the current duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.

</div>

## Implementation

``` dart
Duration get fadeDuration;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">fadeDuration=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-fadeDuration-param-value" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene. Sets duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.

Provided value is clamped in range \[0.0, 10.0\] seconds. Default value is 0 seconds which means the effect is disabled and marker is added/removed immediately without any animation. Fade-in effect is also applied when marker leaves and then re-enters screen area.

Change to this property is made asynchronously and is not guaranteed to take effect on the next rendered frame. In particular, changing fade duration and removing the marker immediately after may result in the new value being ignored for this removal.

</div>

## Implementation

``` dart
set fadeDuration(Duration value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


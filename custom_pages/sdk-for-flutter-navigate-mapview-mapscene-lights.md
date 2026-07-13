---
title: "lights property - MapScene class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapscene-lights"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">lights</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-class">MapSceneLights</a></span> <span class="name">lights</span>

</div>

<div class="section desc markdown">

Controls lights present in the scene. Provides access to a MapSceneLights instance that controls the lights in the scene.

The behavior of the returned MapSceneLights instance depends on the state of the scene:

- If the scene is not loaded, the returned MapSceneLights instance will not contain any light settings, as lights are not loaded without a scene.
- If the scene is loaded, the returned MapSceneLights instance reflects the current light settings of the loaded scene.

Scene Change Behavior:

- If the scene changes, the MapSceneLights instance will be updated to reflect the light settings of the new scene.
- Any user-defined settings to MapSceneLights will be overridden by the new scene's light settings when the scene changes.

Error Handling:

- If the scene is loaded and the loaded scene does not utilize or specify light settings:
  - If the lights are not present, the error callback may return a NO_LIGHTS state. Gets a MapSceneLights instance that controls lights present in the scene.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
MapSceneLights get lights;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


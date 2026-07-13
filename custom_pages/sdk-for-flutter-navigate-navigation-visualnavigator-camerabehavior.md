---
title: "cameraBehavior property - VisualNavigator class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-camerabehavior"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/VisualNavigator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">cameraBehavior</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-class">CameraBehavior</a>?</span> <span class="name">cameraBehavior</span>

</div>

<div class="section desc markdown">

Camera behavior which defines how the <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> handles the camera. Setting `null` disables any camera behavior with the result that the camera does not follow the current location and keeps the last active camera state, i.e., current zoom and tilt. Furthermore, when `null` is set map gestures can be used again to freely pan and zoom the map. In opposition, when a camera behavior is defined, then the map cannot be panned and zoomed by the user. The default value is an instance of <a href="sdk-for-flutter-navigate-navigation-fixedcamerabehavior-class">FixedCameraBehavior</a>. Gets the currently set camera behavior.

</div>

## Implementation

``` dart
CameraBehavior? get cameraBehavior;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">cameraBehavior=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-cameraBehavior-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-class">CameraBehavior</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Camera behavior which defines how the <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> handles the camera. Setting `null` disables any camera behavior with the result that the camera does not follow the current location and keeps the last active camera state, i.e., current zoom and tilt. Furthermore, when `null` is set map gestures can be used again to freely pan and zoom the map. In opposition, when a camera behavior is defined, then the map cannot be panned and zoomed by the user. The default value is an instance of <a href="sdk-for-flutter-navigate-navigation-fixedcamerabehavior-class">FixedCameraBehavior</a>. Sets how the VisualNavigator handles the camera.

</div>

## Implementation

``` dart
set cameraBehavior(CameraBehavior? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


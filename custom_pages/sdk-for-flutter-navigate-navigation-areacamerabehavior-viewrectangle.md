---
title: "viewRectangle property - AreaCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-areacamerabehavior-viewrectangle"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/AreaCameraBehavior-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">viewRectangle</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a>?</span> <span class="name">viewRectangle</span>

</div>

<div class="section desc markdown">

The view rectangle for camera updates. Defines a sub-space of the screen that the behavior should consider for camera updates. Defaults to `null`. If not set, it uses the viewport bounds of the underlying map view. Gets the current view rectangle, if it's set.

</div>

## Implementation

``` dart
Rectangle2D? get viewRectangle;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">viewRectangle=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-viewRectangle-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The view rectangle for camera updates. Defines a sub-space of the screen that the behavior should consider for camera updates. Defaults to `null`. If not set, it uses the viewport bounds of the underlying map view. Sets view rectangle.

</div>

## Implementation

``` dart
set viewRectangle(Rectangle2D? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "measureDependentWidth property - VisualNavigator class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-measuredependentwidth"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/VisualNavigator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">measureDependentWidth</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span>, <span class="type-parameter">double</span>\></span></span> <span class="name">measureDependentWidth</span>

</div>

<div class="section desc markdown">

The `measureDependentWidth` that defines the route and maneuver arrows width. It is a dictionary that has keys that are <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s and values that are width in pixels at this <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s. This route and maneuver arrows width is multiplied by a pixel_scale <a href="sdk-for-flutter-navigate-mapview-mapviewbase-pixelscale">MapViewBase.pixelScale</a> before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with <a href="sdk-for-flutter-navigate-navigation-visualnavigator-maneuverarrowwidthfactor">VisualNavigator.maneuverArrowWidthFactor</a>; which by default equals one. The function defined by a dictionary is linearly interpolated between each successive pair of data points. For keys below the lowest <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>, its corresponding value width is used. For keys above the highest <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>, its corresponding value width is used. Only <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> of `sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL` type are supported. <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> of other unsupported types will be ignored. `measureDependentWidth` with a single entry is equivalent to use of the constant width value of this single entry for all <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s. Empty `measureDependentWidth` is ignored and existing dictionary of width is maintained. The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored. If route and maneuver arrows were not configured with this property, then `measureDependentWidth` contains predefined values chosen to be optimal for different route classes.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process. Gets the <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> dependent polyline and maneuver arrow width in pixels.

</div>

## Implementation

``` dart
Map<MapMeasure, double> get measureDependentWidth;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">measureDependentWidth=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-measureDependentWidth-param-value" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span>, <span class="type-parameter">double</span>\></span></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The `measureDependentWidth` that defines the route and maneuver arrows width. It is a dictionary that has keys that are <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s and values that are width in pixels at this <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s. This route and maneuver arrows width is multiplied by a pixel_scale <a href="sdk-for-flutter-navigate-mapview-mapviewbase-pixelscale">MapViewBase.pixelScale</a> before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with <a href="sdk-for-flutter-navigate-navigation-visualnavigator-maneuverarrowwidthfactor">VisualNavigator.maneuverArrowWidthFactor</a>; which by default equals one. The function defined by a dictionary is linearly interpolated between each successive pair of data points. For keys below the lowest <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>, its corresponding value width is used. For keys above the highest <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>, its corresponding value width is used. Only <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> of `sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL` type are supported. <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> of other unsupported types will be ignored. `measureDependentWidth` with a single entry is equivalent to use of the constant width value of this single entry for all <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s. Empty `measureDependentWidth` is ignored and existing dictionary of width is maintained. The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored. If route and maneuver arrows were not configured with this property, then `measureDependentWidth` contains predefined values chosen to be optimal for different route classes.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process. Sets the <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> dependent route and maneuver arrows width in pixels.

</div>

## Implementation

``` dart
set measureDependentWidth(Map<MapMeasure, double> value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "getHaloColor method - LocationIndicator class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-locationindicator-gethalocolor"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/LocationIndicator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getHaloColor</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">Color</span> <span class="name">getHaloColor</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getHaloColor-param-style" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-locationindicatorindicatorstyle">LocationIndicatorIndicatorStyle</a></span> <span class="parameter-name">style</span></span>

)

</div>

<div class="section desc markdown">

Retrieves the color of the accuracy indicator halo for the requested IndicatorStyle.

The default color is a translucent turquoise (rgba(0, 199, 194, 76)) for all IndicatorStyle settings.

- `style` The type of IndicatorStyle for which the color should be returned.

Returns `ui.Color`. The color of the halo for the specified IndicatorStyle. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
ui.Color getHaloColor(LocationIndicatorIndicatorStyle style);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


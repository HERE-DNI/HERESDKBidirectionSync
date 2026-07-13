---
title: "pinWidget method - HereMapController class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-heremapcontroller-pinwidget"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMapController-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">pinWidget</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-widgetpin-class">WidgetPin</a>?</span> <span class="name">pinWidget</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-pinWidget-param-widget" class="parameter"><span class="type-annotation">Widget</span> <span class="parameter-name">widget</span>, </span>
2.  <span id="sdk-for-flutter-explore-pinWidget-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, {</span>
3.  <span id="sdk-for-flutter-explore-pinWidget-param-anchor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a>?</span> <span class="parameter-name">anchor</span>, </span>

})

</div>

<div class="section desc markdown">

Pins a `Widget` to the MapView and returns a proxy object that can be used to control the pinning.

The altitude component of the coordinates, if set, is interpreted as above sea level. When not set, the coordinates are interpreted as at ground level.

`widget` Widget to pin

`coordinates` GeoCoordinates to pin the widget at

`anchor` The anchor point for the widget which specifies the position offset relative to the widget's coordinates.

Returns <a href="sdk-for-flutter-explore-mapview-widgetpin-class">WidgetPin</a> a pin proxy object

</div>

## Implementation

``` dart
WidgetPin? pinWidget(Widget widget, GeoCoordinates coordinates, {Anchor2D? anchor});
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


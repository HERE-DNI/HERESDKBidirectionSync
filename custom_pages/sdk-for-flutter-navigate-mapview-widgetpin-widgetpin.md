---
title: "WidgetPin constructor - WidgetPin - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-widgetpin-widgetpin"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WidgetPin.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/WidgetPin-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">WidgetPin</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">WidgetPin</span>(<wbr></wbr>{

1.  <span id="sdk-for-flutter-navigate-param-child" class="parameter">required <span class="type-annotation">Widget</span> <span class="parameter-name">child</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-coordinates" class="parameter">required <span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-anchor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a>?</span> <span class="parameter-name">anchor</span>, </span>
4.  <span id="sdk-for-flutter-navigate-param-onChange" class="parameter"><span class="type-annotation">dynamic</span> <span class="parameter-name">onChange</span>()?, </span>
5.  <span id="sdk-for-flutter-navigate-param-onUnpin" class="parameter"><span class="type-annotation">dynamic</span> <span class="parameter-name">onUnpin</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a></span></span>

    )?, </span>

})

</div>

<div class="section desc markdown">

Creates a <a href="sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a> displaying child `Widget` at coordinates location on the map Don't use this constructor directly. Instead use <a href="sdk-for-flutter-navigate-mapview-heremapcontroller-pinwidget">HereMapController.pinWidget</a> to create a <a href="sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a>.

</div>

## Implementation

``` dart
factory WidgetPin({
  required Widget child,
  required GeoCoordinates coordinates,
  Anchor2D? anchor,
  Function()? onChange,
  Function(WidgetPin)? onUnpin,
}) =>
    $prototype.make(
      child: child,
      coordinates: coordinates,
      anchor: anchor,
      onChange: onChange,
      onUnpin: onUnpin,
    );
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

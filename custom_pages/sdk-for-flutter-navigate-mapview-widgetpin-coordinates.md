---
title: "coordinates property - WidgetPin class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-widgetpin-coordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- coordinates.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/WidgetPin-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">coordinates</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="name">coordinates</span>

</div>

<div class="section desc markdown">

Gets geographical location of the <a href="sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a>.

</div>

## Implementation

``` dart
GeoCoordinates get coordinates;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">coordinates=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-coordinates-param-newCoords" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">newCoords</span></span>)</span>

</div>

<div class="section desc markdown">

Changes geographical location of the <a href="sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a>.

The altitude component of the coordinates, if set, is interpreted as above sea level. When not set, the coordinates are interpreted as at ground level.

</div>

## Implementation

``` dart
set coordinates(GeoCoordinates newCoords);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

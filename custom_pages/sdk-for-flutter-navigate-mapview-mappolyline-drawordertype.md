---
title: "drawOrderType property - MapPolyline class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolyline-drawordertype"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- drawOrderType.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolyline-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">drawOrderType</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType</a></span> <span class="name">drawOrderType</span>

</div>

<div class="section desc markdown">

The draw order type of the polyline. Gets the draw order type of the polyline.

The default value is <a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderDependent</a>.

</div>

## Implementation

``` dart
DrawOrderType get drawOrderType;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">drawOrderType=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-drawOrderType-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType</a></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The draw order type of the polyline. Sets the draw order type of the polyline.

For <a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderDependent</a>, map polylines with outlines having the same draw order are drawn as a whole in the order of addition to a map scene. There is no possibility that parts of another polyline, regardless of its draw order value, are drawn between outline and mainline of another polyline.

With <a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderDependent</a>, polylines are rendered one by one.

For <a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderIndependent</a>, for multiple polylines with outlines having the same draw order, all outlines are rendered first in an arbitrary order and then all mainlines are drawn on top of those polylines in an arbitrary order.

<a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderIndependent</a> allows speeding up the rendering process and keeping high frame rates when many similar polylines (with same styling attributes and <a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentation-class">MapPolylineRepresentation</a>) are present in a map scene.

</div>

## Implementation

``` dart
set drawOrderType(DrawOrderType value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

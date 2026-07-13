---
title: "drawOrder property - MapPolyline class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolyline-draworder"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolyline-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">drawOrder</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">int</span> <span class="name">drawOrder</span>

</div>

<div class="section desc markdown">

The draw order of the polyline. Gets the draw order of the polyline.

The default draw order is 0.

</div>

## Implementation

``` dart
int get drawOrder;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">drawOrder=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-drawOrder-param-value" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The draw order of the polyline. Sets the draw order of the polyline.

Polylines with a higher draw order are drawn on top of polylines with a lower draw order.

In case multiple polylines have the same draw order, they can be rendered in different ways depending on the <a href="sdk-for-flutter-navigate-mapview-mappolyline-drawordertype">MapPolyline.drawOrderType</a> set.

Supplied value is clamped to the range \[0; 1023\].

</div>

## Implementation

``` dart
set drawOrder(int value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


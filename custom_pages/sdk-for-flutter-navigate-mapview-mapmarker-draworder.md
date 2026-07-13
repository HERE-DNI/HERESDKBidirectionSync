---
title: "drawOrder property - MapMarker class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-draworder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- drawOrder.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">drawOrder</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">int</span> <span class="name">drawOrder</span>

</div>

<div class="section desc markdown">

The draw order of this marker relative to other markers. Gets draw order of this marker relative to other markers. The default value is 0.

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

The draw order of this marker relative to other markers. Sets draw order of this marker relative to other markers.

Markers with higher draw order value are drawn on top of markers with lower draw order. In case multiple markers have the same draw order value then the order in which they were added to the scene matters. Last added marker is drawn on top.

Allowed range is \[0, 1023\]. Values outside this range will be clamped. The default value is 0.

</div>

## Implementation

``` dart
set drawOrder(int value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

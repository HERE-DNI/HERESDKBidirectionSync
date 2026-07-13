---
title: "drawOrder property - MapImageOverlay class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapimageoverlay-draworder"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapImageOverlay-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">drawOrder</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">int</span> <span class="name">drawOrder</span>

</div>

<div class="section desc markdown">

Draw order of this `MapImageOverlay`. Gets draw order of this `MapImageOverlay`. The default value is 0.

</div>

## Implementation

``` dart
int get drawOrder;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">drawOrder=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-drawOrder-param-value" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Draw order of this `MapImageOverlay`. Sets draw order of this `MapImageOverlay`.

Overlays with higher draw order value are drawn on top of overlays with lower draw order.

In case multiple overlays have the same draw order value then the order in which they were added to the scene matters. Last added overlay is drawn on top.

Allowed range is \[0, 1023\]. Values outside this range will be clamped.

</div>

## Implementation

``` dart
set drawOrder(int value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


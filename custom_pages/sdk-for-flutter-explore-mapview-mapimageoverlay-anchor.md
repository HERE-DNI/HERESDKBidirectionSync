---
title: "anchor property - MapImageOverlay class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapimageoverlay-anchor"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapImageOverlay-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">anchor</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a></span> <span class="name">anchor</span>

</div>

<div class="section desc markdown">

The anchor point for the overlay image which specifies the position offset relative to the overlay's view coordinates. Gets current anchor point for the overlay image.

</div>

## Implementation

``` dart
Anchor2D get anchor;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">anchor=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-anchor-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The anchor point for the overlay image which specifies the position offset relative to the overlay's view coordinates. Sets anchor point of the overlay image which specifies the position offset relative to the overlay's view coordinates.

For example, (0, 0) places the top-left corner of the image at the overlay's view coordinates. (1, 1) would place the bottom-right corner of the image at the overlay's view coordinates. (0.5, 0.5) which is the default value would center the image at the overlay's view coordinates.

Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image centered horizontally with its bottom edge above the overlay's view coordinates at the distance in pixels that is equal to the height of the image.

</div>

## Implementation

``` dart
set anchor(Anchor2D value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


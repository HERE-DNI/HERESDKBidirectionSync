---
title: "selectedLevelIndex property - Venue class - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue-control-venue-selectedlevelindex"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/Venue-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">selectedLevelIndex</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">int</span> <span class="name">selectedLevelIndex</span>

</div>

<div class="section desc markdown">

The index of the <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> selected from the level array of the <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>. Unlike the Z index, it can't have a negative value. Gets the index of the currently selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> in the level array of the related <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>. The level array can be taken from <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-levels">VenueDrawing.levels</a>.

</div>

## Implementation

``` dart
int get selectedLevelIndex;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">selectedLevelIndex=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-selectedLevelIndex-param-value" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The index of the <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> selected from the level array of the <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>. Unlike the Z index, it can't have a negative value. Sets the <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> with the specified index from the level array of the <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> as selected.

</div>

## Implementation

``` dart
set selectedLevelIndex(int value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "selectedLevel property - Venue class - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue-control-venue-selectedlevel"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/Venue-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">selectedLevel</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a></span> <span class="name">selectedLevel</span>

</div>

<div class="section desc markdown">

The selected level. Only the selected level will be visible as active on the map. All others will be hidden or displayed without details, depending on a renderer implementation. If the level doesn't belong to the currently selected drawing, it can not be selected. Gets the currently selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> from the selected <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>.

</div>

## Implementation

``` dart
VenueLevel get selectedLevel;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">selectedLevel=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-selectedLevel-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The selected level. Only the selected level will be visible as active on the map. All others will be hidden or displayed without details, depending on a renderer implementation. If the level doesn't belong to the currently selected drawing, it can not be selected. Sets the selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> from the currently selected <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>.

</div>

## Implementation

``` dart
set selectedLevel(VenueLevel value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "onLevelSelected method - VenueLevelSelectionListener class - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue.control-venuelevelselectionlistener-onlevelselected"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/VenueLevelSelectionListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onLevelSelected</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onLevelSelected</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onLevelSelected-param-venue" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a></span> <span class="parameter-name">venue</span>, </span>
2.  <span id="sdk-for-flutter-navigate-onLevelSelected-param-drawing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a></span> <span class="parameter-name">drawing</span>, </span>
3.  <span id="sdk-for-flutter-navigate-onLevelSelected-param-deselectedLevel" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>?</span> <span class="parameter-name">deselectedLevel</span>, </span>
4.  <span id="sdk-for-flutter-navigate-onLevelSelected-param-selectedLevel" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a></span> <span class="parameter-name">selectedLevel</span>, </span>

)

</div>

<div class="section desc markdown">

Indicates that the selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> of a venue changed.

- `venue` The <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> where the selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> changed.

- `drawing` The <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> where the selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> changed.

- `deselectedLevel` The previously selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> or `null` if there was no selected level before.

- `selectedLevel` The new selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>.

</div>

## Implementation

``` dart
void onLevelSelected(Venue venue, VenueDrawing drawing, VenueLevel? deselectedLevel, VenueLevel selectedLevel);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


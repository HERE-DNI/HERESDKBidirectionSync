---
title: "onDrawingSelected method - VenueDrawingSelectionListener class - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue.control-venuedrawingselectionlistener-ondrawingselected"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/VenueDrawingSelectionListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onDrawingSelected</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onDrawingSelected</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onDrawingSelected-param-venue" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a></span> <span class="parameter-name">venue</span>, </span>
2.  <span id="sdk-for-flutter-navigate-onDrawingSelected-param-deselectedDrawing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>?</span> <span class="parameter-name">deselectedDrawing</span>, </span>
3.  <span id="sdk-for-flutter-navigate-onDrawingSelected-param-selectedDrawing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a></span> <span class="parameter-name">selectedDrawing</span></span>

)

</div>

<div class="section desc markdown">

Indicates that new <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> has been selected.

- `venue` The <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> where a selected drawing was changed.

- `deselectedDrawing` The previously selected <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> object or `null` if there was no selected drawing before.

- `selectedDrawing` The new selected <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> object.

</div>

## Implementation

``` dart
void onDrawingSelected(Venue venue, VenueDrawing? deselectedDrawing, VenueDrawing selectedDrawing);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


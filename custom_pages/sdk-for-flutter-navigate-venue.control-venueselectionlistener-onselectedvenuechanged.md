---
title: "onSelectedVenueChanged method - VenueSelectionListener class - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue.control-venueselectionlistener-onselectedvenuechanged"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/VenueSelectionListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onSelectedVenueChanged</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onSelectedVenueChanged</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onSelectedVenueChanged-param-deselectedVenue" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>?</span> <span class="parameter-name">deselectedVenue</span>, </span>
2.  <span id="sdk-for-flutter-navigate-onSelectedVenueChanged-param-selectedVenue" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>?</span> <span class="parameter-name">selectedVenue</span></span>

)

</div>

<div class="section desc markdown">

Indicates that the current selected <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> changed.

- `deselectedVenue` The <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> that was deselected or `null` if there was no selected venue before.

- `selectedVenue` The <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> that was selected or `null` if there was no new selected venue.

</div>

## Implementation

``` dart
void onSelectedVenueChanged(Venue? deselectedVenue, Venue? selectedVenue);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


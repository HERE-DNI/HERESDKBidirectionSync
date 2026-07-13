---
title: "match method - MapMatcher class - mapmatcher library - Dart API"
slug: "sdk-for-flutter-navigate-mapmatcher-mapmatcher-match"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- match.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapmatcher/MapMatcher-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">match</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation</a>?</span> <span class="name">match</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-match-param-location" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">location</span></span>

)

</div>

<div class="section desc markdown">

This method computes the map-matched location for the provided input location.

Currently, matching is performed within a 50-meter radius of the provided location. If no road network is found within that radius, `null` is returned.

It's required to set `time` field for each `Location` object for the `MapMatcher` to work properly. In case no time is provided, `null` is returned and an error message is logged. It is used to calculate the distance in time between consecutive matches. Together with `speed`, this allows to calculate how likely a match is consistent with a previous match. To improve matching accuracy, it is recommended to provide `bearing` and `speed` parameters for each `Location` object.

- `location` The input location.

Returns <a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation?</a>. map-matched location or `null` if the location could not be matched to a road network.

</div>

## Implementation

``` dart
MapMatchedLocation? match(Location location);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "NavigableLocation constructor - NavigableLocation - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigablelocation-navigablelocation"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigableLocation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">NavigableLocation</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">NavigableLocation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-originalLocation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">originalLocation</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-mapMatchedLocation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation</a>?</span> <span class="parameter-name">mapMatchedLocation</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `originalLocation` The original location that was passed in via <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a>.
- `mapMatchedLocation` The map-matched location on a road. It is calculated from the passed in <a href="sdk-for-flutter-navigate-navigation-navigablelocation-originallocation">NavigableLocation.originalLocation</a>.

</div>

## Implementation

``` dart
NavigableLocation(this.originalLocation, this.mapMatchedLocation);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


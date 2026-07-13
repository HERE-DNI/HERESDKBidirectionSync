---
title: "enable method - LocationIndicator class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-locationindicator-enable"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- enable.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/LocationIndicator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">enable</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">enable</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-enable-param-mapView" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapviewbase-class">MapViewBase</a></span> <span class="parameter-name">mapView</span></span>

)

</div>

<div class="section desc markdown">

Enables <a href="sdk-for-flutter-explore-mapview-locationindicator-class">LocationIndicator</a> for provided <a href="sdk-for-flutter-explore-mapview-mapviewbase-class">MapViewBase</a>.

If <a href="sdk-for-flutter-explore-mapview-locationindicator-class">LocationIndicator</a> is already enabled (added to map view) for passed map view, this function does nothing. If <a href="sdk-for-flutter-explore-mapview-locationindicator-class">LocationIndicator</a> is added to different <a href="sdk-for-flutter-explore-mapview-mapviewbase-class">MapViewBase</a>, this function removes first <a href="sdk-for-flutter-explore-mapview-locationindicator-class">LocationIndicator</a> from previous map view before adding to new one.

- `mapView` The <a href="sdk-for-flutter-explore-mapview-mapviewbase-class">MapViewBase</a> instance.

</div>

## Implementation

``` dart
void enable(MapViewBase mapView);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

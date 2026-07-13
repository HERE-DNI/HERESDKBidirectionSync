---
title: "description property - TrafficIncidentBase class - traffic library - Dart API"
slug: "sdk-for-flutter-navigate-traffic-trafficincidentbase-description"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/TrafficIncidentBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">description</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-localizedtext-class">LocalizedText</a></span> <span class="name">description</span>

</div>

<div class="section desc markdown">

The human readable description of the incident, possibly with location information. The description is currently not present in our map data. Therefore, when accessing the data from a picked carto POI via `TrafficIncidentResult`, then always an empty string is returned. This does not apply when using the `TrafficEngine`. Gets the human readable description of the incident, possibly with location information.

</div>

## Implementation

``` dart
LocalizedText get description;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


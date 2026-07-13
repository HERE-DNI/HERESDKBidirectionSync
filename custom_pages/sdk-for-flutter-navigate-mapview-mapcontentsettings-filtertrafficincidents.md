---
title: "filterTrafficIncidents method - MapContentSettings class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcontentsettings-filtertrafficincidents"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- filterTrafficIncidents.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapContentSettings-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">filterTrafficIncidents</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">filterTrafficIncidents</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-filterTrafficIncidents-param-trafficIncidents" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-traffic-trafficincidenttype">TrafficIncidentType</a></span>\></span></span> <span class="parameter-name">trafficIncidents</span></span>

)

</div>

<div class="section desc markdown">

Filters the displayed traffic incidents so that only the ones applicable to the specified criteria are shown when general display of traffic incidents is enabled.

The display of traffic incidents can be enabled using <a href="sdk-for-flutter-navigate-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> with <a href="sdk-for-flutter-navigate-mapview-mapfeatures-trafficincidents">MapFeatures.trafficIncidents</a>.

- `trafficIncidents` The traffic incidents to filter for, so that only applicable incidents are displayed. When the list is empty, then all traffic incidents will be displayed. If the `MapContentSettings.filterTrafficIncidents.trafficIncidents` contains <a href="sdk-for-flutter-navigate-traffic-trafficincidenttype">TrafficIncidentType.unknown</a>, then the traffic filter will be applied ignoring this element.

</div>

## Implementation

``` dart
static void filterTrafficIncidents(List<TrafficIncidentType> trafficIncidents) => $prototype.filterTrafficIncidents(trafficIncidents);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "originalId property - TrafficIncident class - traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-trafficincident-originalid"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/TrafficIncident-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">originalId</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">String</span> <span class="name">originalId</span>

</div>

<div class="section desc markdown">

The unique identifier of the first traffic incident. The original id remains the same whenever the traffic incident is updated and <a href="sdk-for-flutter-explore-traffic-trafficincident-id">TrafficIncident.id</a> is changed. Once an incident chain has been created, this value will never change. The traffic incident an be looked up by original id using <a href="sdk-for-flutter-explore-traffic-trafficengine-lookupincident">TrafficEngine.lookupIncident</a>. Gets the unique identifier of the first traffic incident.

</div>

## Implementation

``` dart
String get originalId;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


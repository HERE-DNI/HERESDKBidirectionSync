---
title: "confidence property - TrafficFlow class - traffic library - Dart API"
slug: "sdk-for-flutter-navigate-traffic-trafficflow-confidence"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/TrafficFlow-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">confidence</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">double?</span> <span class="name">confidence</span>

</div>

<div class="section desc markdown">

The confidence field indicates the proportion of real-time data included in the speed calculation. It is a normalized value between 0.0 and 1.0 with the following meaning:

- 0.7 \< confidence \<= 1.0 indicates real time speeds
- 0.5 \< confidence \<= 0.7 indicates historical speeds
- 0.0 \< confidence \<= 0.5 indicates speed limit

This field can be used to identify whether the data for a location is derived from real-time probe sources or historical information only. All confidence data 0.71 and above is based on real-time information, where a confidence value of 0.75 or greater indicates high confidence real-time information. A confidence value equal to 0.70 or lower means that the data is derived from historical data only. Gets the confidence field value which is normalized value between 0.0 and 1.0.

</div>

## Implementation

``` dart
double? get confidence;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


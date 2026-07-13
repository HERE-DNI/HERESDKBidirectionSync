---
title: "setTrafficRefreshPeriod method - MapContentSettings class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcontentsettings-settrafficrefreshperiod"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapContentSettings-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setTrafficRefreshPeriod</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setTrafficRefreshPeriod</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-setTrafficRefreshPeriod-param-value" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">value</span></span>

)

</div>

<div class="section desc markdown">

Sets the traffic data refresh period for both <a href="sdk-for-flutter-explore-mapview-mapfeatures-trafficflow">MapFeatures.trafficFlow</a> and <a href="sdk-for-flutter-explore-mapview-mapfeatures-trafficincidents">MapFeatures.trafficIncidents</a>.

By default, the traffic information validity time and the refresh period is derived from the refresh period of HERE's traffic server. The period set by this function will override the server's default setting for upcoming traffic data requests. Defaults to 60 seconds.

- `value` Traffic data refresh period in seconds. Valid range is \[60, 300\] seconds. The shortest refresh period that can be set is 60 seconds. This means that the traffic data shown on a map view will be refreshed every minute. The longest refresh period that can be set is 300 seconds. This means that the traffic data shown on the current map view will be refreshed every 5 minutes if the viewport does not change. Note that when a viewport change occurs, new traffic data may be requested regardless of the set refresh period. For example, during turn-by-turn navigation, frequent viewport changes can result in missing traffic data, causing new requests to be made more often.

Throws <a href="sdk-for-flutter-explore-mapview-mapcontentsettingstrafficrefreshperiodexceptionexception-class">MapContentSettingsTrafficRefreshPeriodExceptionException</a>. <a href="sdk-for-flutter-explore-mapview-mapcontentsettingstrafficrefreshperiodexceptionexception-class">MapContentSettingsTrafficRefreshPeriodExceptionException</a> indicates what went wrong.

</div>

## Implementation

``` dart
static void setTrafficRefreshPeriod(Duration value) => $prototype.setTrafficRefreshPeriod(value);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "languageCode property - TrafficIncidentsQueryOptions class - traffic library - Dart API"
slug: "sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-languagecode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- languageCode.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/TrafficIncidentsQueryOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">languageCode</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>? <span class="name">languageCode</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The language code of the query. It's the expected language of fields <a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-description">TrafficIncidentBase.description</a> and <a href="sdk-for-flutter-navigate-traffic-trafficincident-summary">TrafficIncident.summary</a> in the relevant response. However, the language code doesn't impact on <a href="sdk-for-flutter-navigate-traffic-trafficlocation-description">TrafficLocation.description</a>. If the language code is null or not supported then response fields are expected in the original language of the country that the incident belongs to.

</div>

## Implementation

``` dart
LanguageCode? languageCode;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

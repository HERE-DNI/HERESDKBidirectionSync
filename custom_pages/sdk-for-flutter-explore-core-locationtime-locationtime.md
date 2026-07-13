---
title: "LocationTime constructor - LocationTime - core library - Dart API"
slug: "sdk-for-flutter-explore-core-locationtime-locationtime"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationTime.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/LocationTime-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">LocationTime</span> constructor

</div>

<div class="section multi-line-signature">

const <span class="name">LocationTime</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-localTime" class="parameter"><span class="type-annotation">DateTime</span> <span class="parameter-name">localTime</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-utcTime" class="parameter"><span class="type-annotation">DateTime</span> <span class="parameter-name">utcTime</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-utcOffset" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">utcOffset</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `localTime` The time as observed in the tied location. For example, if a route is requested in Cracow, Poland, the local time is "2022-03-23T16:07:31" in CET, i.e. one hour ahead of the UTC time.
- `utcTime` The time as Coordinated Universal Time (UTC). For example, if a route is requested in Poland, the UTC time is "2022-03-23T15:07:31", i.e. one hour behind the local time.
- `utcOffset` The UTC offset is the difference between the local time and the Coordinated Universal Time (UTC) in seconds. For example, if the local time is UTC+01:00, it is +3600 and if the local time is UTC-05:00, it is -18000.

</div>

## Implementation

``` dart
const LocationTime(this.localTime, this.utcTime, this.utcOffset);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "timeZoneOffsetsInMinutes property - AdministrativeRules class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-administrativerules-timezoneoffsetsinminutes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- timeZoneOffsetsInMinutes.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/AdministrativeRules-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">timeZoneOffsetsInMinutes</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter">Duration</span>\></span> <span class="name">timeZoneOffsetsInMinutes</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The time zone offset from UTC of the country or state expressed in minutes. The value can also be negative (e.g.: Eastern Standard Time (EST) will be -360 minutes, Central European Time (CET) will be 60 minutes). Defaults to 0 minutes. **Note:** A time zone with a positive shift of 1 hour and 30 minutes will result in a time zone offset of 90 minutes. A time zone with a negative shift of 3 hour and 30 minutes will result in an time zone offset of -210 minutes. In order to properly calculate the time zone offset, the `AdministrativeRules.daylight_saving_period` should be taken into consideration and if the daylight savings time is observed at the time of the calculation, then a value of 60 minutes should be substracted from the time zone offset.

</div>

## Implementation

``` dart
List<Duration> timeZoneOffsetsInMinutes;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

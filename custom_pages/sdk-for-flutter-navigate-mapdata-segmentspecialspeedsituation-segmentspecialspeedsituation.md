---
title: "SegmentSpecialSpeedSituation constructor - SegmentSpecialSpeedSituation - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-segmentspecialspeedsituation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SegmentSpecialSpeedSituation.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/SegmentSpecialSpeedSituation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">SegmentSpecialSpeedSituation</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">SegmentSpecialSpeedSituation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-specialSpeedType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span> <span class="parameter-name">specialSpeedType</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-speedLimitInMetersPerSecond" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">speedLimitInMetersPerSecond</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-appliesDuring" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-timerule-class">TimeRule</a></span>\></span></span> <span class="parameter-name">appliesDuring</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance with default values.

- `specialSpeedType` Represents the speed situation type.
- `speedLimitInMetersPerSecond` Overrides normal speed limit for this situation.

May be 0 to indicate no special speed limit in the case of special_speed_type = SPEED_BUMPS_PRESENT and special_speed_type = LANE_DEPENDENT. Speed limit in meter per seconds.

- `appliesDuring` The times during which the condition applies. May be empty for all special_speed_type values except `TIME_DEPENDENT` and `APPROXIMATE_SEASONAL_TIME`.

</div>

## Implementation

``` dart
SegmentSpecialSpeedSituation(this.specialSpeedType, this.speedLimitInMetersPerSecond, this.appliesDuring);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

---
title: "startOffsetInMeters property - RailwayCrossing class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-railwaycrossing-startoffsetinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startOffsetInMeters.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/RailwayCrossing-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">startOffsetInMeters</span> property

</div>

<div class="section multi-line-signature">

int <span class="name">startOffsetInMeters</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The start offset, in meters, from the beginning of the segment.

If <a href="sdk-for-flutter-navigate-mapdata-railwaycrossing-endoffsetinmeters">RailwayCrossing.endOffsetInMeters</a> = 0, then <a href="sdk-for-flutter-navigate-mapdata-railwaycrossing-startoffsetinmeters">RailwayCrossing.startOffsetInMeters</a> approximately indicates a middle of a railway crossing. If <a href="sdk-for-flutter-navigate-mapdata-railwaycrossing-endoffsetinmeters">RailwayCrossing.endOffsetInMeters</a> \> 0, it means crossing consists of several rails, and <a href="sdk-for-flutter-navigate-mapdata-railwaycrossing-startoffsetinmeters">RailwayCrossing.startOffsetInMeters</a> and <a href="sdk-for-flutter-navigate-mapdata-railwaycrossing-endoffsetinmeters">RailwayCrossing.endOffsetInMeters</a> indicates starting and ending points of the crossing respectively. Default value is 0.

</div>

## Implementation

``` dart
int startOffsetInMeters;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

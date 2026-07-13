---
title: "boxArea property - TextQueryArea class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-textqueryarea-boxarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- boxArea.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/TextQueryArea-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">boxArea</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>? <span class="name">boxArea</span>

<div class="features">

<span class="feature">final</span>

</div>

</div>

<div class="section desc markdown">

Geographic rectangle area in which to provide the most relevant places. For Offline Search, one of <a href="sdk-for-flutter-navigate-search-textqueryarea-areacenter">TextQueryArea.areaCenter</a>, <a href="sdk-for-flutter-navigate-search-textqueryarea-boxarea">TextQueryArea.boxArea</a> and <a href="sdk-for-flutter-navigate-search-textqueryarea-circlearea">TextQueryArea.circleArea</a> has to be set, otherwise it will result in <a href="sdk-for-flutter-navigate-search-searcherror">SearchError.invalidArea</a>. Also, for Offline Search, search in a given `GeoBox` restricts the results to only POIs.

</div>

## Implementation

``` dart
final GeoBox? boxArea;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

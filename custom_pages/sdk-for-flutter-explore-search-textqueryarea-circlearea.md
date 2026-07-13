---
title: "circleArea property - TextQueryArea class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-textqueryarea-circlearea"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/TextQueryArea-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">circleArea</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a>? <span class="name">circleArea</span>

<div class="features">

<span class="feature">final</span>

</div>

</div>

<div class="section desc markdown">

Geographic circle area in which to provide the most relevant places. For Offline Search, one of <a href="sdk-for-flutter-explore-search-textqueryarea-areacenter">TextQueryArea.areaCenter</a>, <a href="sdk-for-flutter-explore-search-textqueryarea-boxarea">TextQueryArea.boxArea</a> and <a href="sdk-for-flutter-explore-search-textqueryarea-circlearea">TextQueryArea.circleArea</a> has to be set, otherwise it will result in <a href="sdk-for-flutter-explore-search-searcherror">SearchError.invalidArea</a>. Also, for Offline Search, search in a given `GeoCircle` restricts the results to only POIs.

</div>

## Implementation

``` dart
final GeoCircle? circleArea;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


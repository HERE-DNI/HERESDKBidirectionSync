---
title: "loadData method - ElectronicHorizonDataLoader class - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-loaddata"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonDataLoader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">loadData</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">loadData</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-loadData-param-electronicHorizonUpdate" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-class">ElectronicHorizonUpdate</a></span> <span class="parameter-name">electronicHorizonUpdate</span></span>

)

</div>

<div class="section desc markdown">

Requests data for all added segments and removes cached data for segments that are not part of the horizon anymore.

- `electronicHorizonUpdate` The update that contains the segments to add to the cache and the segments to remove from the cache.

</div>

## Implementation

``` dart
void loadData(ElectronicHorizonUpdate electronicHorizonUpdate);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "TileSourceListener constructor - TileSourceListener - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-tilesourcelistener"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/TileSourceListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TileSourceListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TileSourceListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-onDataVersionChangedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onDataVersionChangedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilesourcedataversion-class">TileSourceDataVersion</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Listener of <a href="sdk-for-flutter-explore-mapview-datasource-tilesource-class">TileSource</a> events.

</div>

## Implementation

``` dart
factory TileSourceListener(
  void Function(TileSourceDataVersion) onDataVersionChangedLambda,

) => TileSourceListener$Lambdas(
  onDataVersionChangedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


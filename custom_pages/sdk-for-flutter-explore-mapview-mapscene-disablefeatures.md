---
title: "disableFeatures method - MapScene class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscene-disablefeatures"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">disableFeatures</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">disableFeatures</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-disableFeatures-param-features" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">features</span></span>

)

</div>

<div class="section desc markdown">

Disables specified map features.

Those will become inactive after next map redraw, meaning that <a href="sdk-for-flutter-explore-mapview-mapscene-getactivefeatures">MapScene.getActiveFeatures</a> will return updated list of active features only after the redraw happens.

Does not affect features that were not specified. Unsupported features are ignored.

May cause the current map configuration to be reloaded.

See <a href="sdk-for-flutter-explore-mapview-mapfeatures-class">MapFeatures</a> for feature names.

- `features` The names of features to disable (see <a href="sdk-for-flutter-explore-mapview-mapfeatures-class">MapFeatures</a>).

</div>

## Implementation

``` dart
void disableFeatures(List<String> features);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


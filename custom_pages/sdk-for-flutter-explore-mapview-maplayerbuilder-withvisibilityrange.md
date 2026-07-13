---
title: "withVisibilityRange method - MapLayerBuilder class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-maplayerbuilder-withvisibilityrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withVisibilityRange.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapLayerBuilder-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">withVisibilityRange</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a></span> <span class="name">withVisibilityRange</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withVisibilityRange-param-visibilityRange" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-maplayervisibilityrange-class">MapLayerVisibilityRange</a></span> <span class="parameter-name">visibilityRange</span></span>

)

</div>

<div class="section desc markdown">

Configures the builder to set the layer visible in the given zoom levels range.

Values outside the map zoom level range (0, 24) will be ignored. Providing the visibility range is optional. If not provided, the layer will be visible on all zoom levels.

- `visibilityRange` Visibility range which should be applied to the layer.

Returns <a href="sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a>. This class instance.

</div>

## Implementation

``` dart
MapLayerBuilder withVisibilityRange(MapLayerVisibilityRange visibilityRange);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

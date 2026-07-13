---
title: "setPriority method - TranslucentMapLayerGroup class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-translucentmaplayergroup-setpriority"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setPriority.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/TranslucentMapLayerGroup-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setPriority</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setPriority</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-setPriority-param-priority" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-maplayerpriority-class">MapLayerPriority</a></span> <span class="parameter-name">priority</span></span>

)

</div>

<div class="section desc markdown">

Sets the render priority for the layer group which replaces any previously defined priority.

- `priority` The priority to position the group. The <a href="sdk-for-flutter-explore-mapview-maplayerpriority-class">MapLayerPriority</a> must contain only one priority and this priority must have no category and no group, i.e. <a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-ingroup">MapLayerPriorityBuilder.inGroup</a> and <a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-withcategory">MapLayerPriorityBuilder.withCategory</a> should not be used when building the <a href="sdk-for-flutter-explore-mapview-maplayerpriority-class">MapLayerPriority</a>. Example:

new MapLayerPriorityBuilder().renderedAfterLayer("water").build()

    MapLayerPriorityBuilder().renderedAfterLayer("water").build()

</p>

</div>

## Implementation

``` dart
void setPriority(MapLayerPriority priority);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

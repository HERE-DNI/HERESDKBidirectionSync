---
title: "inGroup method - MapLayerPriorityBuilder class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-maplayerprioritybuilder-ingroup"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapLayerPriorityBuilder-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">inGroup</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a></span> <span class="name">inGroup</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-inGroup-param-group" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">group</span></span>

)

</div>

<div class="section desc markdown">

Sets the group for which a priority could be defined with the next call to the functions `renderedFirst|Last|BeforeLayer|AfterLayer`.

When a group is set, the next defined priority is relative to the layers and layer categories inside this group. The references (i.e. 'referenceLayer' and 'referenceCategory') of the priority are only searched inside the group. Only one group or no group can be defined per layer priority and layer category priority, however, different layers can set priorities for the same group. After a priority is defined by calling one of the aforementioned functions, the current group is cleared and the builder refers again to the global layer list in the scene. Note that a group needs to exist when the built <a href="sdk-for-flutter-explore-mapview-maplayerpriority-class">MapLayerPriority</a> is used during a <a href="sdk-for-flutter-explore-mapview-maplayerbuilder-build">MapLayerBuilder.build</a> or <a href="sdk-for-flutter-explore-mapview-maplayer-setpriority">MapLayer.setPriority</a>, otherwise the priority cannot be applied and the layer will render nothing to the group. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

- `group` The name of the group. For instance the name of a <a href="sdk-for-flutter-explore-mapview-translucentmaplayergroup-class">TranslucentMapLayerGroup</a>.

Returns <a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a>. This class instance.

</div>

## Implementation

``` dart
MapLayerPriorityBuilder inGroup(String group);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


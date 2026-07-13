---
title: "renderedAfterLayerWithCategory method - MapLayerPriorityBuilder class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedafterlayerwithcategory"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapLayerPriorityBuilder-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">renderedAfterLayerWithCategory</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a></span> <span class="name">renderedAfterLayerWithCategory</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-renderedAfterLayerWithCategory-param-referenceLayer" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">referenceLayer</span>, </span>
2.  <span id="sdk-for-flutter-navigate-renderedAfterLayerWithCategory-param-referenceCategory" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">referenceCategory</span></span>

)

</div>

<div class="section desc markdown">

Sets the priority as rendered after the referenceCategory of the referenceLayer.

Applies to the layer itself or the category pointed to by the preceding call to <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-withcategory">MapLayerPriorityBuilder.withCategory</a>. Notice that the order of calls to the functions `renderedFirst|Last|Before|After` matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like

    withCategory("C").renderedAfterLayer("L").withCategory("C").renderedBeforeLayer("L")

</p>

The previously defined and prioritised categories can be used as reference. If the referenceLayer and/or the referenceCategory do not exist, then the function will set the priority as rendered after all layers and categories.

- `referenceLayer` The beforehand defined layer name which renders directly before the current layer.

- `referenceCategory` The beforehand defined category name which renders directly before the current layer.

Returns <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a>. This class instance.

</div>

## Implementation

``` dart
MapLayerPriorityBuilder renderedAfterLayerWithCategory(String referenceLayer, String referenceCategory);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


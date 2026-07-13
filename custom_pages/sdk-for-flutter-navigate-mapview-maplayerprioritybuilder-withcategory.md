---
title: "withCategory method - MapLayerPriorityBuilder class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-withcategory"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withCategory.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapLayerPriorityBuilder-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">withCategory</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a></span> <span class="name">withCategory</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withCategory-param-category" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">category</span></span>

)

</div>

<div class="section desc markdown">

Sets the layer category for which a priority could be defined with the next call to the functions `renderedFirst|Last|BeforeLayer|AfterLayer`.

After a priority is defined by calling one of the aforementioned functions, the current category is cleared and the builder refers again to the layer itself.

- `category` The name of the layer category.

Returns <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a>. This class instance.

</div>

## Implementation

``` dart
MapLayerPriorityBuilder withCategory(String category);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

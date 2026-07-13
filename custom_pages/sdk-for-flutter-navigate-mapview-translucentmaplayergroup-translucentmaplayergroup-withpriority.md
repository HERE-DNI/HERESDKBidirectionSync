---
title: "TranslucentMapLayerGroup.withPriority constructor - TranslucentMapLayerGroup - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-translucentmaplayergroup-translucentmaplayergroup-withpriority"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/TranslucentMapLayerGroup-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TranslucentMapLayerGroup.withPriority</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TranslucentMapLayerGroup.withPriority</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withPriority-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withPriority-param-aMap" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-heremapcontrollercore-class">HereMapControllerCore</a></span> <span class="parameter-name">aMap</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withPriority-param-priority" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-maplayerpriority-class">MapLayerPriority</a></span> <span class="parameter-name">priority</span></span>

)

</div>

<div class="section desc markdown">

Creates an instance of the group.

- `name` Name of the group. Must be unique across <a href="sdk-for-flutter-navigate-mapview-maplayer-class">MapLayer</a> and <a href="sdk-for-flutter-navigate-mapview-translucentmaplayergroup-class">TranslucentMapLayerGroup</a>.

- `aMap` The map to attach the group to.

- `priority` The <a href="sdk-for-flutter-navigate-mapview-maplayerpriority-class">MapLayerPriority</a> which should be applied to position the group. The <a href="sdk-for-flutter-navigate-mapview-maplayerpriority-class">MapLayerPriority</a> must contain only one priority and this priority must have no category and no group, i.e. <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-ingroup">MapLayerPriorityBuilder.inGroup</a> and <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-withcategory">MapLayerPriorityBuilder.withCategory</a> should not be used when building the <a href="sdk-for-flutter-navigate-mapview-maplayerpriority-class">MapLayerPriority</a>. Example:

new MapLayerPriorityBuilder().renderedAfterLayer("water").build()

    MapLayerPriorityBuilder().renderedAfterLayer("water").build()

</p>

Throws <a href="sdk-for-flutter-navigate-mapview-translucentmaplayergroupinstantiationexception-class">TranslucentMapLayerGroupInstantiationException</a>. In case of invalid input parameters.

</div>

## Implementation

``` dart
factory TranslucentMapLayerGroup.withPriority(String name, HereMapControllerCore aMap, MapLayerPriority priority) => $prototype.withPriority(name, aMap, priority);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


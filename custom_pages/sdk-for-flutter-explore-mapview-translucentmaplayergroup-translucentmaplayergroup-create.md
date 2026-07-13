---
title: "TranslucentMapLayerGroup.create constructor - TranslucentMapLayerGroup - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-translucentmaplayergroup-translucentmaplayergroup-create"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/TranslucentMapLayerGroup-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TranslucentMapLayerGroup.create</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TranslucentMapLayerGroup.create</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-create-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span>
2.  <span id="sdk-for-flutter-explore-create-param-aMap" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-class">HereMapControllerCore</a></span> <span class="parameter-name">aMap</span></span>

)

</div>

<div class="section desc markdown">

Creates an instance of the group.

- `name` Name of the group. Must be unique across <a href="sdk-for-flutter-explore-mapview-maplayer-class">MapLayer</a> and <a href="sdk-for-flutter-explore-mapview-translucentmaplayergroup-class">TranslucentMapLayerGroup</a>.

- `aMap` The map to attach the group to.

Throws <a href="sdk-for-flutter-explore-mapview-translucentmaplayergroupinstantiationexception-class">TranslucentMapLayerGroupInstantiationException</a>. In case of invalid input parameters.

</div>

## Implementation

``` dart
factory TranslucentMapLayerGroup.create(String name, HereMapControllerCore aMap) => $prototype.create(name, aMap);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "onAttach method - MapViewLifecycleListener class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-onattach"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapViewLifecycleListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onAttach</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onAttach</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-onAttach-param-mapView" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapviewbase-class">MapViewBase</a></span> <span class="parameter-name">mapView</span></span>

)

</div>

<div class="section desc markdown">

Called when adding <a href="sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a> to the map view.

If the map view does not have render target attached at the time of adding the listener, then this method will be called later, after render target is attached. This means that the map view it receives is always fully initialized.

Can be used to implement the logic to create and add visual components to the map view.

- `mapView` The map view to attach to.

</div>

## Implementation

``` dart
void onAttach(MapViewBase mapView);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


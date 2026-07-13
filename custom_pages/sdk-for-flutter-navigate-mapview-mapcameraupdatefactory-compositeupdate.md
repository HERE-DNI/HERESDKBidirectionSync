---
title: "compositeUpdate method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-compositeupdate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- compositeUpdate.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">compositeUpdate</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">compositeUpdate</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-compositeUpdate-param-mapCameraUpdates" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span>\></span></span> <span class="parameter-name">mapCameraUpdates</span></span>

)

</div>

<div class="section desc markdown">

Creates a composite camera update from a list of camera updates.

The result update will be equivalent to executing all given updates sequentially in the order they were provided.

MapCameraAnimation instances derived from the MapCameraAnimationFactory and a composite camera update are not supported. An AnimationListener will receive an AnimationState.Cancelled signal when trying to apply such animations.

- `mapCameraUpdates` List of MapCamera updates.

Returns <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

Throws <a href="sdk-for-flutter-navigate-mapview-mapcameraupdateinstantiationexception-class">MapCameraUpdateInstantiationException</a>. Indicates an instantiation issue.

</div>

## Implementation

``` dart
static MapCameraUpdate compositeUpdate(List<MapCameraUpdate> mapCameraUpdates) => $prototype.compositeUpdate(mapCameraUpdates);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

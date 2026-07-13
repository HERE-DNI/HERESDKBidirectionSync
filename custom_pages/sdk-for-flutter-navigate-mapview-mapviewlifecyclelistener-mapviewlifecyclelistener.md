---
title: "MapViewLifecycleListener constructor - MapViewLifecycleListener - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-mapviewlifecyclelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapViewLifecycleListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapViewLifecycleListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapViewLifecycleListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapViewLifecycleListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onAttachLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onAttachLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a></span></span>

    ), </span>
2.  <span id="sdk-for-flutter-navigate-param-onDetachLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onDetachLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a></span></span>

    ), </span>
3.  <span id="sdk-for-flutter-navigate-param-onPauseLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onPauseLambda</span>(), </span>
4.  <span id="sdk-for-flutter-navigate-param-onResumeLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onResumeLambda</span>(), </span>
5.  <span id="sdk-for-flutter-navigate-param-onDestroyLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onDestroyLambda</span>(), </span>

)

</div>

<div class="section desc markdown">

Provides a mechanism for observing a lifecycle of a map view and/or implementing components whose lifecycle needs to be linked with that of a map view.

A `MapView` is using a

<a href="https://developer.android.com/reference/android/view/SurfaceView">SurfaceView</a> for Android and <a href="https://developer.apple.com/documentation/quartzcore/cametallayer">CAMetalLayer</a> for iOS to render its content.

</div>

## Implementation

``` dart
factory MapViewLifecycleListener(
  void Function(MapViewBase) onAttachLambda,
  void Function(MapViewBase) onDetachLambda,
  void Function() onPauseLambda,
  void Function() onResumeLambda,
  void Function() onDestroyLambda,

) => MapViewLifecycleListener$Lambdas(
  onAttachLambda,
  onDetachLambda,
  onPauseLambda,
  onResumeLambda,
  onDestroyLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

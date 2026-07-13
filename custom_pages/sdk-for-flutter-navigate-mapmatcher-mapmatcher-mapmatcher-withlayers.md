---
title: "MapMatcher.withLayers constructor - MapMatcher - mapmatcher library - Dart API"
slug: "sdk-for-flutter-navigate-mapmatcher-mapmatcher-mapmatcher-withlayers"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMatcher.withLayers.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapmatcher/MapMatcher-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMatcher.withLayers</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMatcher.withLayers</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withLayers-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withLayers-param-useRenderingLayers" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">useRenderingLayers</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance of this class.

- `sdkEngine` A SDKEngine instance.

- `useRenderingLayers` When set to true, `LayerConfiguration.Feature.RENDERING` is used; otherwise, `LayerConfiguration.Feature.EHORIZON` is used to retrieve segment geometry data from the OCM map. Note: Ensure the corresponding layer is properly enabled in your `LayerConfiguration` to avoid incorrect results.

Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. Indicates what went wrong when the instantiation was attempted.

</div>

## Implementation

``` dart
factory MapMatcher.withLayers(SDKNativeEngine sdkEngine, bool useRenderingLayers) => $prototype.withLayers(sdkEngine, useRenderingLayers);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

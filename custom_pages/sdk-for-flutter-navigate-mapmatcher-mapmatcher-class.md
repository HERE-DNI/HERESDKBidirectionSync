---
title: "MapMatcher class - mapmatcher library - Dart API"
slug: "sdk-for-flutter-navigate-mapmatcher-mapmatcher-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMatcher-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapmatcher/mapmatcher-library-sidebar.html" data-below-sidebar="mapmatcher/MapMatcher-class-sidebar.html">

<div>

# <span class="kind-class">MapMatcher</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This class provides map-matching functionality.

It determines whether a location can be matched to a nearby road network and provides additional OCM map data for that location.

**Note:** This is a **beta** release of this feature. There may be bugs and unexpected behaviors. Related APIs may change in future releases without a deprecation process.

A `MapMatcher` maintains an internal state across location updates. This helps to check if the match is consistent with previous matches or if an unrealistic jump occurred due to low accuracy of the provided location.

A `MapMatcher` requires OCM tile data, either through caching, prefetching, or installed `Region` data. If the necessary tiles are not found, an online request is initiated. Note that in such cases, the download is triggered silently in the background, and `null` is returned immediately.

The `MapMatcher` supports two layer configurations for retrieving segment geometry data:

- **Rendering layer (`LayerConfiguration.Feature.RENDERING`)**: Enabled by default. If your application uses map rendering or `MapView` components, using this layer is recommended.

- **eHorizon layer (`LayerConfiguration.Feature.EHORIZON`)**: Not enabled by default. It encodes segment geometries outside the rendering layer groups to reduce the amount of downloaded data. Use the eHorizon layer when:

  - No `MapView` is used in your application.
  - Only the eHorizon layer is used in your application. In these cases, using the eHorizon layer will reduce the required data to download. If the rendering layer is enabled, it will increase the required data to download.

**Important**: If `useRenderingLayers` is set to `false` without properly enabling the eHorizon layer, it may produce incorrect results. Layer configuration is especially important when prefetching or installing region data. Missing data will be downloaded online automatically as needed.

If your hardware supports pitch and high precision altitude information and you want to use them in the `MapMatcher` to improve map-matching, then enable the `LayerConfiguration.Feature.ADAS` layer:

1.  Turn on the `ADAS` layer via `LayerConfiguration.enabledFeatures` (it will increase data consumption).
2.  If available, set `location.pitchInDegrees`, `location.coordinates.altitude` and `location.verticalAccuracyInMeters`.
3.  In case of issues, please contact your HERE representative.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-mapmatcher">MapMatcher</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-mapmatcher-withengine">MapMatcher.withEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-mapmatcher-withlayers">MapMatcher.withLayers</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withLayers-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span><span id="sdk-for-flutter-navigate-withLayers-param-useRenderingLayers" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">useRenderingLayers</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-match">match</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-match-param-location" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">location</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation</a>?</span> </span>  
This method computes the map-matched location for the provided input location.

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapmatcher-mapmatcher-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>

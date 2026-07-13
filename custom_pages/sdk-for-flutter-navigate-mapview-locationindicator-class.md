---
title: "LocationIndicator class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-locationindicator-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/LocationIndicator-class-sidebar.html">

<div>

# <span class="kind-class">LocationIndicator</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Graphical object to represent the location of the user on the map.

It is either a green dot for pedestrian style or a triangular arrow for vehicle navigation style. This style can be changed by <a href="sdk-for-flutter-navigate-mapview-locationindicator-locationindicatorstyle">LocationIndicator.locationIndicatorStyle</a>

The location is made available to an instance of this class by calling <a href="sdk-for-flutter-navigate-mapview-locationindicator-updatelocation">LocationIndicator.updateLocation</a> or <a href="sdk-for-flutter-navigate-mapview-locationindicator-updatelocationandcamera">LocationIndicator.updateLocationAndCamera</a>.

Use <a href="sdk-for-flutter-navigate-mapview-locationindicator-enable">LocationIndicator.enable</a> to add this object to the map and <a href="sdk-for-flutter-navigate-mapview-locationindicator-disable">LocationIndicator.disable</a> to remove it.

Note: The LocationIndicator is always rendered at a fixed altitude near 0. Changing the MapCamera to look at geographic coordinates with an altitude that is higher can cause the following behavior: If the MapCamera angle is tilted and altitude is too high, the LocationIndicator can unexpectedly disappear from the viewport due to the new perspective.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-locationindicator">LocationIndicator</a></span><span class="signature">()</span>  
Creates an instance of LocationIndicator.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-locationindicator-withmapview">LocationIndicator.withMapView</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withMapView-param-mapView" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a></span> <span class="parameter-name">mapView</span></span>)</span>  
Creates an instance of LocationIndicator and adds it to provided <a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-isaccuracyvisualized">isAccuracyVisualized</a></span> <span class="signature">↔ bool</span>  
Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo. Returns whether <a href="sdk-for-flutter-navigate-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a> is used to scale the accuracy indicator halo. Default is `false`, in which case the halo has a fixed and zoom level independent size.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-isactive">isActive</a></span> <span class="signature">↔ bool</span>  
A Boolean value that determines whether the active on inactive version of location indicator is shown. Returns `true` if active version of the location indicator is shown or `false` when inactive version is shown. By default, it is `true`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-locationindicatorstyle">locationIndicatorStyle</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-locationindicatorindicatorstyle">LocationIndicatorIndicatorStyle</a></span>  
The visual style of location indicator. By default, it is set to <a href="sdk-for-flutter-navigate-mapview-locationindicatorindicatorstyle">LocationIndicatorIndicatorStyle.navigation</a>. Returns visual style of location indicator.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-materialreflectivity">materialReflectivity</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-materialreflectivity-class">MaterialReflectivity</a>?</span>  
The material reflectivity properties of the location indicator. Enables per‑pixel lighting for all internal markers (navigation, pedestrian, inactive variants) and the halo when assigned. While `materialReflectivity` is non‑null the markers are shaded by scene lights using the provided ambient / diffuse factors. When set back to `null`, lighting is disabled and markers revert to unlit (emissive) rendering.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-opacity">opacity</a></span> <span class="signature">↔ double</span>  
The factor applied to the alpha channel of both the location indicator's texture and the accuracy indicator's halo color. Default value is 1.0 which means location indicator is displayed with the default alpha channel of the texture. Gets the current opacity of the location indicator.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-disable">disable</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
This function removes <a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a> from map view.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-enable">enable</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-enable-param-mapView" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a></span> <span class="parameter-name">mapView</span></span>) <span class="returntype parameter">→ void</span> </span>  
Enables <a href="sdk-for-flutter-navigate-mapview-locationindicator-class">LocationIndicator</a> for provided <a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-gethalocolor">getHaloColor</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getHaloColor-param-style" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-locationindicatorindicatorstyle">LocationIndicatorIndicatorStyle</a></span> <span class="parameter-name">style</span></span>) <span class="returntype parameter">→ Color</span> </span>  
Retrieves the color of the accuracy indicator halo for the requested IndicatorStyle.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-sethalocolor">setHaloColor</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setHaloColor-param-style" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-locationindicatorindicatorstyle">LocationIndicatorIndicatorStyle</a></span> <span class="parameter-name">style</span>, </span><span id="sdk-for-flutter-navigate-setHaloColor-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the color of the accuracy indicator halo for a given style.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-mapview-locationindicator-setmarker3dmodel" class="deprecated">setMarker3dModel</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setMarker3dModel-param-model" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a></span> <span class="parameter-name">model</span>, </span><span id="sdk-for-flutter-navigate-setMarker3dModel-param-scale" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">scale</span>, </span><span id="sdk-for-flutter-navigate-setMarker3dModel-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-locationindicatormarkertype">LocationIndicatorMarkerType</a></span> <span class="parameter-name">type</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the MapMarker3DModel asset to be displayed as location indicator for a specified type.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-setmarker3dmodelwithrendersizeunit">setMarker3dModelWithRenderSizeUnit</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setMarker3dModelWithRenderSizeUnit-param-model" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a></span> <span class="parameter-name">model</span>, </span><span id="sdk-for-flutter-navigate-setMarker3dModelWithRenderSizeUnit-param-scale" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">scale</span>, </span><span id="sdk-for-flutter-navigate-setMarker3dModelWithRenderSizeUnit-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-locationindicatormarkertype">LocationIndicatorMarkerType</a></span> <span class="parameter-name">type</span>, </span><span id="sdk-for-flutter-navigate-setMarker3dModelWithRenderSizeUnit-param-renderSizeUnit" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a></span> <span class="parameter-name">renderSizeUnit</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the <a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a> asset to be displayed as location indicator for a specified type.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-updatelocation">updateLocation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-updateLocation-param-location" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">location</span></span>) <span class="returntype parameter">→ void</span> </span>  
Updates the indicator to a new location.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-updatelocationandcamera">updateLocationAndCamera</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-updateLocationAndCamera-param-location" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">location</span>, </span><span id="sdk-for-flutter-navigate-updateLocationAndCamera-param-cameraUpdate" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="parameter-name">cameraUpdate</span></span>) <span class="returntype parameter">→ void</span> </span>  
Updates the indicator to a new location and applies a camera update at the same time.

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-locationindicator-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


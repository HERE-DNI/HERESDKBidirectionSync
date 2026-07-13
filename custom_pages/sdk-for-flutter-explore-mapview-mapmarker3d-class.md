---
title: "MapMarker3D class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmarker3d-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapMarker3D-class-sidebar.html">

<div>

# <span class="kind-class">MapMarker3D</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents a 3D shape drawn on the map at specified geodetic coordinates.

It can have a solid color or be textured, depending on the data from <a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-class">MapMarker3DModel</a>.

By default, a 3D marker is drawn on top of all map content, including 3D map elements like extruded buildings or 3D landmarks. This can be changed by enabling depth check using <a href="sdk-for-flutter-explore-mapview-mapmarker3d-isdepthcheckenabled">MapMarker3D.isDepthCheckEnabled</a>.

The display of a 3D marker is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects a 3D marker that is visually large and covers a sizeable part of the viewport.

# Sizing and scaling

Two aspects determine how big the `MapMarker3D` will be on the screen and how will it behave when the map is zoomed in and out.

The first, and most impactful is <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a>, which specifies how the vertex coordinates of the 3D model are interpreted. Most importantly, it specifies whether the 3D model is placed in world or screen coordinate space.

<a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.meters</a> will make the 3D model use world coordinate space, meaning that it will change size together with the map when it is zoomed in and out.

<a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.pixels</a> makes the 3D model use screen coordinate space, meaning that it will have constant size on the screen regardless of how the map zoom changes. So a simple 10 by 10 (in model space) rectangle will have a size of 10 by 10 pixels on the screen.

<a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.densityIndependentPixels</a> is similar to pixels, but the resulting size will take into account the pixel density of the display, meaning that physical size on the screen will be approximately the same regardless of the size or resolution of the display.

The second aspect that determines size of `MapMarker3D` is scale. It can be specified at construction time and can be changed later at any time using <a href="sdk-for-flutter-explore-mapview-mapmarker3d-scale">MapMarker3D.scale</a>.

# Modifying at runtime

A 3D marker can be moved around a map by updating its coordinates using <a href="sdk-for-flutter-explore-mapview-mapmarker3d-coordinates">MapMarker3D.coordinates</a>.

Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.

Its orientation is specified by bearing, pitch and roll and can be changed by using <a href="sdk-for-flutter-explore-mapview-mapmarker3d-bearing">MapMarker3D.bearing</a>, <a href="sdk-for-flutter-explore-mapview-mapmarker3d-pitch">MapMarker3D.pitch</a> and <a href="sdk-for-flutter-explore-mapview-mapmarker3d-roll">MapMarker3D.roll</a>.

# Flat marker

A flat marker is a special case of a 3D marker, where the 3D shape being drawn is a simple textured rectangle. In essence it's an image drawn "on the ground". Such 3D marker can be conveniently created using <a href="sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d-fromimage">MapMarker3D.fromImage</a> constructor. Of course, once created, it can be rotated to face any direction.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d">MapMarker3D</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-at" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">at</span>, </span><span id="sdk-for-flutter-explore-param-model" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-class">MapMarker3DModel</a></span> <span class="parameter-name">model</span></span>)</span>  
Creates an instance of a 3D marker.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d-fromimage">MapMarker3D.fromImage</a></span><span class="signature">(<span id="sdk-for-flutter-explore-fromImage-param-at" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">at</span>, </span><span id="sdk-for-flutter-explore-fromImage-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span>, </span><span id="sdk-for-flutter-explore-fromImage-param-scale" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">scale</span>, </span><span id="sdk-for-flutter-explore-fromImage-param-unit" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a></span> <span class="parameter-name">unit</span></span>)</span>  
Creates a flat marker from provided map image.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d-withscale">MapMarker3D.withScale</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withScale-param-at" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">at</span>, </span><span id="sdk-for-flutter-explore-withScale-param-model" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-class">MapMarker3DModel</a></span> <span class="parameter-name">model</span>, </span><span id="sdk-for-flutter-explore-withScale-param-scale" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">scale</span></span>)</span>  
Creates an instance of a 3D marker with scale factor.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d-withunit">MapMarker3D.withUnit</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withUnit-param-at" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">at</span>, </span><span id="sdk-for-flutter-explore-withUnit-param-model" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-class">MapMarker3DModel</a></span> <span class="parameter-name">model</span>, </span><span id="sdk-for-flutter-explore-withUnit-param-scale" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">scale</span>, </span><span id="sdk-for-flutter-explore-withUnit-param-unit" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a></span> <span class="parameter-name">unit</span></span>)</span>  
Creates a new 3D marker at given world coordinates, using the supplied 3D model.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-bearing">bearing</a></span> <span class="signature">↔ double</span>  
The bearing of the 3D model in degrees, from the true North in clockwise direction. The bearing axis is perpendicular to the ground and passes through the 3D marker's location. The Z-axis of the model is aligned with bearing axis. Gets the bearing of the 3D model in degrees.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-coordinates">coordinates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>  
The position of the 3D marker on the map corresponding to the origin of the 3D marker model coordinate system. The altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level. Gets the 3D marker's position on the map corresponding to the origin of the 3D marker model coordinate system.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-isdepthcheckenabled">isDepthCheckEnabled</a></span> <span class="signature">↔ bool</span>  
Determines whether the depth of the 3D marker's vertices is considered during rendering. If set to `false`, the 3D marker will always appear in front of any other map objects. If set to `true` the 3D marker might be occluded by other map objects like extruded buildings.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-isrenderinternalsenabled">isRenderInternalsEnabled</a></span> <span class="signature">↔ bool</span>  
Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons. Default value is `false`. Can be used with translucent 3D marker.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-metadata">metadata</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-metadata-class">Metadata</a>?</span>  
The <a href="sdk-for-flutter-explore-core-metadata-class">Metadata</a> instance attached to this 3D marker. Gets the <a href="sdk-for-flutter-explore-core-metadata-class">Metadata</a> instance attached to this 3D marker. The default value is `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-opacity">opacity</a></span> <span class="signature">↔ double</span>  
The opacity factor adjusting the opacity of a 3D marker. The factor is applied to the alpha channel of the resulting texture of the marker. Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the specified fill color specified in <a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-class">MapMarker3DModel</a>. Returns an opacity factor which specifies the translucency of a 3D map marker.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-pitch">pitch</a></span> <span class="signature">↔ double</span>  
The pitch of the 3D model in degrees. The pitch axis is parallel to the ground, passes through the location of the 3D marker and aligns with the longitude axis if the bearing is 0. However, this axis rotates with the 3D marker according to the bearing value. Negative values cause the top of the 3D marker to lean forward. The X-axis of the model is aligned with pitch axis. Gets the pitch of the 3D model in degrees.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-roll">roll</a></span> <span class="signature">↔ double</span>  
The roll angle of the 3D model in degrees. The roll axis is parallel to the ground, passes through the 3D marker's location and is aligned initially with the true North. However, when the bearing changes, it rotates around the bearing axis with the 3D marker. Positive/negative values cause a clockwise/counterclockwise rotation when viewing along the axis in the direction of the true North. The Y-axis of the model is aligned with the roll axis. Gets the roll of the 3D model in degrees.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-scale">scale</a></span> <span class="signature">↔ double</span>  
Scale factor applied to the 3D model before rendering. Gets the scale factor applied to the 3D model before rendering.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-visibilityranges">visibilityRanges</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapmeasurerange-class">MapMeasureRange</a></span>\></span></span>  
The list of visibility ranges. The 3D marker is visible only inside these map measure ranges. A range is half open - \<a href="sdk-for-flutter-explore-mapview-mapmarker3d-nosuchmethod">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name">[noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarker3d-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


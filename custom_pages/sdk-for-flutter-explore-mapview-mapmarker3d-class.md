---
title: "MapMarker3D class abstract"
slug: "sdk-for-flutter-explore-mapview-mapmarker3d-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3D-class.html -->


<div>
<h1>MapMarker3D class abstract</h1></div>

<p>Represents a 3D shape drawn on the map at specified geodetic coordinates.</p>
<p>It can have a solid color or be textured, depending on the data from
<a href="/sdk-for-flutter-explore-mapview-mapmarker3dmodel-class">MapMarker3DModel</a>.</p>
<p>By default, a 3D marker is drawn on top of all map content, including
3D map elements like extruded buildings or 3D landmarks. This can be
changed by enabling depth check using <a href="/sdk-for-flutter-explore-mapview-mapmarker3d-isdepthcheckenabled">MapMarker3D.isDepthCheckEnabled</a>.</p>
<p>The display of a 3D marker is only guaranteed in case its origin is within
the viewport. At the moment, this is a known limitation that mostly affects
a 3D marker that is visually large and covers a sizeable part of the viewport.</p>
<h1 id="sizing-and-scaling">Sizing and scaling</h1>
<p>Two aspects determine how big the <code>MapMarker3D</code> will be on the screen
and how will it behave when the map is zoomed in and out.</p>
<p>The first, and most impactful is <a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a>, which specifies
how the vertex coordinates of the 3D model are interpreted.
Most importantly, it specifies whether the 3D model is placed
in world or screen coordinate space.</p>
<p><a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.meters</a> will make the 3D model use world
coordinate space, meaning that it will change size together with the map
when it is zoomed in and out.</p>
<p><a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.pixels</a> makes the 3D model use screen coordinate space,
meaning that it will have constant size on the screen regardless
of how the map zoom changes. So a simple 10 by 10 (in model space) rectangle
will have a size of 10 by 10 pixels on the screen.</p>
<p><a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.densityIndependentPixels</a> is similar to pixels,
but the resulting size will take into account the pixel density of the
display, meaning that physical size on the screen will be approximately
the same regardless of the size or resolution of the display.</p>
<p>The second aspect that determines size of <code>MapMarker3D</code> is scale.
It can be specified at construction time and can be changed later
at any time using <a href="/sdk-for-flutter-explore-mapview-mapmarker3d-scale">MapMarker3D.scale</a>.</p>
<h1 id="modifying-at-runtime">Modifying at runtime</h1>
<p>A 3D marker can be moved around a map by updating its coordinates using
<a href="/sdk-for-flutter-explore-mapview-mapmarker3d-coordinates">MapMarker3D.coordinates</a>.</p>
<p>Altitude component of the coordinates, if set, controls 3D marker's elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
<p>Its orientation is specified by bearing, pitch and roll and can be changed
by using <a href="/sdk-for-flutter-explore-mapview-mapmarker3d-bearing">MapMarker3D.bearing</a>, <a href="/sdk-for-flutter-explore-mapview-mapmarker3d-pitch">MapMarker3D.pitch</a>
and <a href="/sdk-for-flutter-explore-mapview-mapmarker3d-roll">MapMarker3D.roll</a>.</p>
<h1 id="flat-marker">Flat marker</h1>
<p>A flat marker is a special case of a 3D marker, where the 3D shape being drawn
is a simple textured rectangle. In essence it's an image drawn "on the ground".
Such 3D marker can be conveniently created using
<a href="/sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d-fromimage">MapMarker3D.fromImage</a>
constructor. Of course, once created, it can be rotated to face any direction.</p>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d">MapMarker3D</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d-fromimage">MapMarker3D.fromImage</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d-withscale">MapMarker3D.withScale</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d-withunit">MapMarker3D.withUnit</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-bearing">bearing</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-coordinates">coordinates</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-isdepthcheckenabled">isDepthCheckEnabled</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-isrenderinternalsenabled">isRenderInternalsEnabled</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-metadata">metadata</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-opacity">opacity</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-pitch">pitch</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-roll">roll</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-runtimetype">runtimeType</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-scale">scale</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-visibilityranges">visibilityRanges</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapmarker3d-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>

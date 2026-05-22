---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapmarker3d-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3D-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapMarker3D class</li>
</ol>
<div class="self-name">MapMarker3D</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapMarker3D-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapMarker3D class abstract</h1></div>
<section class="desc markdown">
<p>Represents a 3D shape drawn on the map at specified geodetic coordinates.</p>
<p>It can have a solid color or be textured, depending on the data from
/sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class.</p>
<p>By default, a 3D marker is drawn on top of all map content, including
3D map elements like extruded buildings or 3D landmarks. This can be
changed by enabling depth check using /sdk-for-flutter-navigate-mapview-mapmarker3d-isdepthcheckenabled.</p>
<p>The display of a 3D marker is only guaranteed in case its origin is within
the viewport. At the moment, this is a known limitation that mostly affects
a 3D marker that is visually large and covers a sizeable part of the viewport.</p>
<h1 id="sizing-and-scaling">Sizing and scaling</h1>
<p>Two aspects determine how big the <code>MapMarker3D</code> will be on the screen
and how will it behave when the map is zoomed in and out.</p>
<p>The first, and most impactful is /sdk-for-flutter-navigate-mapview-rendersizeunit, which specifies
how the vertex coordinates of the 3D model are interpreted.
Most importantly, it specifies whether the 3D model is placed
in world or screen coordinate space.</p>
<p>/sdk-for-flutter-navigate-mapview-rendersizeunit will make the 3D model use world
coordinate space, meaning that it will change size together with the map
when it is zoomed in and out.</p>
<p>/sdk-for-flutter-navigate-mapview-rendersizeunit makes the 3D model use screen coordinate space,
meaning that it will have constant size on the screen regardless
of how the map zoom changes. So a simple 10 by 10 (in model space) rectangle
will have a size of 10 by 10 pixels on the screen.</p>
<p>/sdk-for-flutter-navigate-mapview-rendersizeunit is similar to pixels,
but the resulting size will take into account the pixel density of the
display, meaning that physical size on the screen will be approximately
the same regardless of the size or resolution of the display.</p>
<p>The second aspect that determines size of <code>MapMarker3D</code> is scale.
It can be specified at construction time and can be changed later
at any time using /sdk-for-flutter-navigate-mapview-mapmarker3d-scale.</p>
<h1 id="modifying-at-runtime">Modifying at runtime</h1>
<p>A 3D marker can be moved around a map by updating its coordinates using
/sdk-for-flutter-navigate-mapview-mapmarker3d-coordinates.</p>
<p>Altitude component of the coordinates, if set, controls 3D marker's elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
<p>Its orientation is specified by bearing, pitch and roll and can be changed
by using /sdk-for-flutter-navigate-mapview-mapmarker3d-bearing, /sdk-for-flutter-navigate-mapview-mapmarker3d-pitch
and /sdk-for-flutter-navigate-mapview-mapmarker3d-roll.</p>
<h1 id="flat-marker">Flat marker</h1>
<p>A flat marker is a special case of a 3D marker, where the 3D shape being drawn
is a simple textured rectangle. In essence it's an image drawn "on the ground".
Such 3D marker can be conveniently created using
/sdk-for-flutter-navigate-mapview-mapmarker3d-mapmarker3d-fromimage
constructor. Of course, once created, it can be rotated to face any direction.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapMarker3D">
/sdk-for-flutter-navigate-mapview-mapmarker3d-mapmarker3d(/sdk-for-flutter-navigate-core-geocoordinates-class at, /sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class model)
</dt>
<dd>
          Creates an instance of a 3D marker.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMarker3D.fromImage">
/sdk-for-flutter-navigate-mapview-mapmarker3d-mapmarker3d-fromimage(/sdk-for-flutter-navigate-core-geocoordinates-class at, /sdk-for-flutter-navigate-mapview-mapimage-class image, double scale, /sdk-for-flutter-navigate-mapview-rendersizeunit unit)
</dt>
<dd>
          Creates a flat marker from provided map image.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMarker3D.withScale">
/sdk-for-flutter-navigate-mapview-mapmarker3d-mapmarker3d-withscale(/sdk-for-flutter-navigate-core-geocoordinates-class at, /sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class model, double scale)
</dt>
<dd>
          Creates an instance of a 3D marker with scale factor.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMarker3D.withUnit">
/sdk-for-flutter-navigate-mapview-mapmarker3d-mapmarker3d-withunit(/sdk-for-flutter-navigate-core-geocoordinates-class at, /sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class model, double scale, /sdk-for-flutter-navigate-mapview-rendersizeunit unit)
</dt>
<dd>
          Creates a new 3D marker at given world coordinates, using the supplied 3D model.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="bearing">
/sdk-for-flutter-navigate-mapview-mapmarker3d-bearing
↔ double
</dt>
<dd>
  The bearing of the 3D model in degrees, from the true North in clockwise direction.
The bearing axis is perpendicular to the ground and passes through the 3D marker's location.
The Z-axis of the model is aligned with bearing axis.
Gets the bearing of the 3D model in degrees.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="coordinates">
/sdk-for-flutter-navigate-mapview-mapmarker3d-coordinates
↔ /sdk-for-flutter-navigate-core-geocoordinates-class
</dt>
<dd>
  The position of the 3D marker on the map corresponding to the origin of the 3D marker model coordinate system.
The altitude component of the coordinates, if set, controls 3D marker's elevation
above ground. If not set, the 3D marker is placed at ground level.
Gets the 3D marker's position on the map corresponding to the origin of the 3D marker model
coordinate system.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-mapmarker3d-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="isDepthCheckEnabled">
/sdk-for-flutter-navigate-mapview-mapmarker3d-isdepthcheckenabled
↔ bool
</dt>
<dd>
  Determines whether the depth of the 3D marker's vertices is considered during rendering.
If set to <code>false</code>, the 3D marker will always appear in front of any other map objects.
If set to <code>true</code> the 3D marker might be occluded by other map objects like extruded buildings.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isRenderInternalsEnabled">
/sdk-for-flutter-navigate-mapview-mapmarker3d-isrenderinternalsenabled
↔ bool
</dt>
<dd>
  Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons.
Default value is <code>false</code>. Can be used with translucent 3D marker.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="metadata">
/sdk-for-flutter-navigate-mapview-mapmarker3d-metadata
↔ /sdk-for-flutter-navigate-core-metadata-class?
</dt>
<dd>
  The /sdk-for-flutter-navigate-core-metadata-class instance attached to this 3D marker.
Gets the /sdk-for-flutter-navigate-core-metadata-class instance attached to this 3D marker.
The default value is <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="opacity">
/sdk-for-flutter-navigate-mapview-mapmarker3d-opacity
↔ double
</dt>
<dd>
  The opacity factor adjusting the opacity of a 3D marker.
The factor is applied to the alpha channel of the resulting texture of the marker.
Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the
specified fill color specified
in /sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class.
Returns an opacity factor which specifies the translucency of a 3D map marker.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="pitch">
/sdk-for-flutter-navigate-mapview-mapmarker3d-pitch
↔ double
</dt>
<dd>
  The pitch of the 3D model in degrees.
The pitch axis is parallel to the ground, passes through the location of the 3D marker
and aligns with the longitude axis if the bearing is 0. However, this axis rotates with
the 3D marker according to the bearing value. Negative values cause the top of the
3D marker to lean forward. The X-axis of the model is aligned with pitch axis.
Gets the pitch of the 3D model in degrees.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="roll">
/sdk-for-flutter-navigate-mapview-mapmarker3d-roll
↔ double
</dt>
<dd>
  The roll angle of the 3D model in degrees.
The roll axis is parallel to the ground, passes through the 3D marker's
location and is aligned initially with the true North. However, when the bearing changes,
it rotates around the bearing axis with the 3D marker.
Positive/negative values cause a clockwise/counterclockwise rotation when viewing along the axis
in the direction of the true North. The Y-axis of the model is aligned with the roll axis.
Gets the roll of the 3D model in degrees.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-mapmarker3d-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="scale">
/sdk-for-flutter-navigate-mapview-mapmarker3d-scale
↔ double
</dt>
<dd>
  Scale factor applied to the 3D model before rendering.
Gets the scale factor applied to the 3D model before rendering.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="visibilityRanges">
/sdk-for-flutter-navigate-mapview-mapmarker3d-visibilityranges
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-mapview-mapmeasurerange-class&gt;
</dt>
<dd>
  The list of visibility ranges. The 3D marker is visible only inside these map measure ranges.
A range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
is not contained in the range.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-mapmarker3d-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-mapmarker3d-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-mapview-mapmarker3d-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapMarker3D class</li>
</ol>
<h5>mapview library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>

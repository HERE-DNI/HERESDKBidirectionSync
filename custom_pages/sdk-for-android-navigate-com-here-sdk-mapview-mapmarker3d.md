---
title: "MapMarker3D (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapMarker3D.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapMarker3D</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapMarker3D</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents a 3D shape drawn on the map at specified geodetic coordinates.
 It can have a solid color or be textured, depending on the data from
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview"><code>MapMarker3DModel</code></a>.
 By default, a 3D marker is drawn on top of all map content, including
 3D map elements like extruded buildings or 3D landmarks. This can be
 changed by enabling depth check using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d#setDepthCheckEnabled(boolean)"><code>setDepthCheckEnabled(boolean)</code></a>.
 The display of a 3D marker is only guaranteed in case its origin is within
 the viewport. At the moment, this is a known limitation that mostly affects
 a 3D marker that is visually large and covers a sizeable part of the viewport.
 
Two aspects determine how big the <code>MapMarker3D</code> will be on the screen
 and how will it behave when the map is zoomed in and out.
 The first, and most impactful is <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a>, which specifies
 how the vertex coordinates of the 3D model are interpreted.
 Most importantly, it specifies whether the 3D model is placed
 in world or screen coordinate space.
 <a href="sdk-for-android-navigate-rendersize-unit#METERS"><code>RenderSize.Unit.METERS</code></a> will make the 3D model use world
 coordinate space, meaning that it will change size together with the map
 when it is zoomed in and out.
 <a href="sdk-for-android-navigate-rendersize-unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> makes the 3D model use screen coordinate space,
 meaning that it will have constant size on the screen regardless
 of how the map zoom changes. So a simple 10 by 10 (in model space) rectangle
 will have a size of 10 by 10 pixels on the screen.
 <a href="sdk-for-android-navigate-rendersize-unit#DENSITY_INDEPENDENT_PIXELS"><code>RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS</code></a> is similar to pixels,
 but the resulting size will take into account the pixel density of the
 display, meaning that physical size on the screen will be approximately
 the same regardless of the size or resolution of the display.
 The second aspect that determines size of <code>MapMarker3D</code> is scale.
 It can be specified at construction time and can be changed later
 at any time using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d#setScale(double)"><code>setScale(double)</code></a>.
 
A 3D marker can be moved around a map by updating its coordinates using
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d#setCoordinates(com.here.sdk.core.GeoCoordinates)"><code>setCoordinates(com.here.sdk.core.GeoCoordinates)</code></a>.
 Altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.
 Its orientation is specified by bearing, pitch and roll and can be changed
 by using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d#setBearing(double)"><code>setBearing(double)</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d#setPitch(double)"><code>setPitch(double)</code></a>
 and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d#setRoll(double)"><code>setRoll(double)</code></a>.
 
A flat marker is a special case of a 3D marker, where the 3D shape being drawn
 is a simple textured rectangle. In essence it's an image drawn "on the ground".
 Such 3D marker can be conveniently created using
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,double,com.here.sdk.mapview.RenderSize.Unit)"><code>MapMarker3D(GeoCoordinates, MapImage, double, RenderSize.Unit)</code></a>
 constructor. Of course, once created, it can be rotated to face any direction.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,double,com.here.sdk.mapview.RenderSize.Unit)">MapMarker3D</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image,
 double scale,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> unit)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a flat marker from provided map image.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel)">MapMarker3D</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates an instance of a 3D marker.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double)">MapMarker3D</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model,
 double scale)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates an instance of a 3D marker with scale factor.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.RenderSize.Unit)">MapMarker3D</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model,
 double scale,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> unit)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new 3D marker at given world coordinates, using the supplied 3D model.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel)">
<h3>MapMarker3D</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapMarker3D</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model)</span></div>
<div className="block"><p>Creates an instance of a 3D marker.
 The origin of the 3D model's local coordinate system is placed at the specified
 geographical coordinates.
 Altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>at</code> - <p>The geographical coordinates where the 3D marker is placed corresponding to origin of the
     3D model's local coordinate system.</p></dd>
<dd><code>model</code> - <p>The 3D model used to draw 3D marker.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,double,com.here.sdk.mapview.RenderSize.Unit)">
<h3>MapMarker3D</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapMarker3D</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image,
 double scale,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> unit)</span></div>
<div className="block"><p>Creates a flat marker from provided map image.
 Such map marker is a flat 3D marker of rectangular shape textured with given image.
 Aspect ratio of the flat marker is determined by aspect ratio of the image.
 Only bitmap images are supported, using a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview"><code>MapImage</code></a> created from SVG data
 will result in distorted rendering of the flat marker.
 Altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.
 Size of the rendered flat marker can be specified in either world or screen coordinate space.
 For <a href="sdk-for-android-navigate-rendersize-unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a>, the flat marker will cover <code>scale</code> * image's width pixels
 horizontally and <code>scale</code> * image's height pixels vertically. The size of the flat marker
 remains constant on the screen.
 For <a href="sdk-for-android-navigate-rendersize-unit#DENSITY_INDEPENDENT_PIXELS"><code>RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS</code></a> the flat marker will cover <code>scale</code> *
 image's width density independent pixels horizontally and <code>scale</code> * image's height
 density independent pixels vertically. The size of the flat marker remains constant on
 the screen.
 For <a href="sdk-for-android-navigate-rendersize-unit#METERS"><code>RenderSize.Unit.METERS</code></a> the flat marker will cover <code>scale</code> * image's width meters
 horizontally and <code>scale</code> * image's height meters vertically. Unlike with pixels or
 density independent pixels the size of the flat marker will grow and shrink together
 with regular map content like streets or buildings.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>at</code> - <p>The geographical coordinates where the flat marker is placed corresponding to center of the
     provided map image.</p></dd>
<dd><code>image</code> - <p>The MapImage containing the texture data of the flat marker. SVG images are not supported.</p></dd>
<dd><code>scale</code> - <p>Scale factor applied to the dimensions of the image.</p></dd>
<dd><code>unit</code> - <p>Determines whether the size of the flat marker is represented in world or in screen space.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double)">
<h3>MapMarker3D</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapMarker3D</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model,
 double scale)</span></div>
<div className="block"><p>Creates an instance of a 3D marker with scale factor.
 One unit of the 3D marker model will cover <code>scale</code> pixels.
 The size of the 3D marker remains constant on the screen.
 The origin of the 3D model's local coordinate system is placed at the specified
 geographical coordinates.
 Altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>at</code> - <p>The geographical coordinates where the 3D marker is placed corresponding to origin of the
     3D model's local coordinate system.</p></dd>
<dd><code>model</code> - <p>The 3D model used to render the 3D marker.</p></dd>
<dd><code>scale</code> - <p>Scale factor to apply to the 3D model.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.RenderSize.Unit)">
<h3>MapMarker3D</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapMarker3D</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model,
 double scale,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> unit)</span></div>
<div className="block"><p>Creates a new 3D marker at given world coordinates, using the supplied 3D model.
 The unit specifies how the 3D geometry of the model is interpreted (meters for world space,
 pixels or density independent pixels for screen space), while scale determines its relative size.
 For <a href="sdk-for-android-navigate-rendersize-unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> one unit of the 3D marker model will cover <code>scale</code> pixels.
 The size of the 3D marker remains constant on the screen.
 For <a href="sdk-for-android-navigate-rendersize-unit#DENSITY_INDEPENDENT_PIXELS"><code>RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS</code></a> one unit of the 3D marker model will
 cover <code>scale</code> density independent pixels. The size of the 3D marker remains constant on
 the screen.
 For <a href="sdk-for-android-navigate-rendersize-unit#METERS"><code>RenderSize.Unit.METERS</code></a> one unit of the 3D marker model will cover <code>scale</code> meters
 in the real world. Unlike with pixels or density-independent pixels the size of the
 3D marker will grow and shrink together with regular map content like streets or buildings.
 The origin of the 3D model's local coordinate system is placed at the specified
 geographical coordinates.
 Altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>at</code> - <p>The geographical coordinates where the 3D marker is placed corresponding to origin of the
     3D model's local coordinate system.</p></dd>
<dd><code>model</code> - <p>The 3D model used to render the 3D marker.</p></dd>
<dd><code>scale</code> - <p>Scale factor to apply to the 3D model.</p></dd>
<dd><code>unit</code> - <p>Determines the unit of the model vertices and whether the size of the 3D marker
     is expressed in world or screen space.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getCoordinates()">
<h3>getCoordinates</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">getCoordinates</span>()</div>
<div className="block"><p>Gets the 3D marker's position on the map corresponding to the origin of the 3D marker model
 coordinate system.
 The altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The position of the 3D marker on the map corresponding to the origin of the 3D marker model coordinate system.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>setCoordinates</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> value)</span></div>
<div className="block"><p>Sets the 3D marker's position on the map corresponding to the origin of the 3D marker model
 coordinate system.
 The altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The position of the 3D marker on the map corresponding to the origin of the 3D marker model coordinate system.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getMetadata()">
<h3>getMetadata</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-metadata" title="class in com.here.sdk.core">Metadata</a></span> <span className="element-name">getMetadata</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-core-metadata" title="class in com.here.sdk.core"><code>Metadata</code></a> instance attached to this 3D marker.
 The default value is <code>null</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-core-metadata" title="class in com.here.sdk.core"><code>Metadata</code></a> instance attached to this 3D marker.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setMetadata(com.here.sdk.core.Metadata)">
<h3>setMetadata</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setMetadata</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-metadata" title="class in com.here.sdk.core">Metadata</a> value)</span></div>
<div className="block"><p>Sets the <a href="sdk-for-android-navigate-com-here-sdk-core-metadata" title="class in com.here.sdk.core"><code>Metadata</code></a> instance attached to this 3D marker.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-core-metadata" title="class in com.here.sdk.core"><code>Metadata</code></a> instance attached to this 3D marker.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBearing()">
<h3>getBearing</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getBearing</span>()</div>
<div className="block"><p>Gets the bearing of the 3D model in degrees.
 The bearing axis is perpendicular to the ground and passes through the 3D marker's location.
 The Z-axis of the model is aligned with bearing axis.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The bearing of the 3D model in degrees, from the true North in clockwise direction.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setBearing(double)">
<h3>setBearing</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setBearing</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets the bearing of the 3D model in degrees.
 The bearing axis is perpendicular to the ground and passes through the 3D marker's location.
 The Z-axis of the model is aligned with bearing axis.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The bearing of the 3D model in degrees, from the true North in clockwise direction.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoll()">
<h3>getRoll</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getRoll</span>()</div>
<div className="block"><p>Gets the roll of the 3D model in degrees.
 The roll axis is parallel to the ground, passes through the 3D marker's
 location and is aligned initially with the true North. However, when the bearing changes,
 it rotates around the bearing axis with the 3D marker.
 Positive/negative values cause a clockwise/counterclockwise rotation when viewing along the axis
 in the direction of the true North. The Y-axis of the model is aligned with the roll axis.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The roll angle of the 3D model in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRoll(double)">
<h3>setRoll</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRoll</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets the roll of the 3D model in degrees.
 The roll axis is parallel to the ground, passes through the 3D marker's
 location and is aligned initially with the true North. However, when the bearing changes,
 it rotates around the bearing axis with the 3D marker.
 Positive/negative values cause a clockwise/counterclockwise rotation when viewing along the axis
 in the direction of the true North. The Y-axis of the model is aligned with the roll axis.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The roll angle of the 3D model in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPitch()">
<h3>getPitch</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getPitch</span>()</div>
<div className="block"><p>Gets the pitch of the 3D model in degrees.
 The pitch axis is parallel to the ground, passes through the location of the 3D marker
 and aligns with the longitude axis if the bearing is 0. However, this axis rotates with
 the 3D marker according to the bearing value. Negative values cause the top of the
 3D marker to lean forward. The X-axis of the model is aligned with pitch axis.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The pitch of the 3D model in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setPitch(double)">
<h3>setPitch</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setPitch</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets the pitch of the 3D model in degrees.
 The pitch axis is parallel to the ground, passes through the location of the 3D marker
 and aligns with the longitude axis if the bearing is 0. However, this axis rotates with
 the 3D marker according to the bearing value. Negative values cause the top of the
 3D marker to lean forward. The X-axis of the model is aligned with pitch axis.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The pitch of the 3D model in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getScale()">
<h3>getScale</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getScale</span>()</div>
<div className="block"><p>Gets the scale factor applied to the 3D model before rendering.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Scale factor applied to the 3D model before rendering.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setScale(double)">
<h3>setScale</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setScale</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets the scale factor, to be applied to the 3D model before rendering.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Scale factor applied to the 3D model before rendering.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isDepthCheckEnabled()">
<h3>isDepthCheckEnabled</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isDepthCheckEnabled</span>()</div>
<div className="block"><p>Returns <code>true</code> if depth check is enabled.
 If set to <code>false</code>, the 3D marker will always appear in front of any other map objects.
 If set to <code>true</code> the 3D marker might be occluded by other map objects like extruded buildings.
 By default depth check is set to <code>false</code>.
 Use the altitude of the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d#getCoordinates()"><code>getCoordinates()</code></a> to position the 3D marker sufficiently high above the
 surface. Setting depth check to <code>true</code> will fix visual glitches where components of the marker
 3D model unexpectedly shine through.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Determines whether the depth of the 3D marker's vertices is considered during rendering.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDepthCheckEnabled(boolean)">
<h3>setDepthCheckEnabled</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDepthCheckEnabled</span><wbr/><span className="parameters">(boolean value)</span></div>
<div className="block"><p>Set whether the depth of the 3D marker's vertices is considered during rendering.
 If set to <code>false</code>, the 3D marker will always appear in front of any other map objects.
 If set to <code>true</code> the 3D marker might be occluded by other map objects like extruded buildings.
 By default depth check is set to <code>false</code>.
 Use the altitude of the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d#getCoordinates()"><code>getCoordinates()</code></a> to position the 3D marker sufficiently high above the
 surface. Setting depth check to <code>true</code> will fix visual glitches where components of the marker
 3D model unexpectedly shine through.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Determines whether the depth of the 3D marker's vertices is considered during rendering.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isRenderInternalsEnabled()">
<h3>isRenderInternalsEnabled</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isRenderInternalsEnabled</span>()</div>
<div className="block"><p>Returns a flag indicating whether to render internal geometry of a 3D marker occluded by its front
 facing polygons. Default value is <code>false</code>.
 Default value is <code>false</code>. Can be used with translucent 3D marker.
 Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two
 passes: first pass with front-face, second pass with back-face culling enabled.
 With this flag enabled for 3D marker with depth check disabled rendering is performed in a
 single pass with back-face culling disabled.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setRenderInternalsEnabled(boolean)">
<h3>setRenderInternalsEnabled</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRenderInternalsEnabled</span><wbr/><span className="parameters">(boolean value)</span></div>
<div className="block"><p>Sets a flag indicating whether to render internal geometry of a 3D marker occluded by its front
 facing polygons.
 Default value is <code>false</code>. Can be used with translucent 3D marker.
 Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two
 passes: first pass with front-face, second pass with back-face culling enabled.
 With this flag enabled for 3D marker with depth check disabled rendering is performed in a
 single pass with back-face culling disabled.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOpacity()">
<h3>getOpacity</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getOpacity</span>()</div>
<div className="block"><p>Returns an opacity factor which specifies the translucency of a 3D map marker.
 The factor is applied to the alpha channel of the resulting texture of the marker.
 Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the
 specified fill color specified
 in <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview"><code>MapMarker3DModel</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The opacity factor adjusting the opacity of a 3D marker.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setOpacity(double)">
<h3>setOpacity</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setOpacity</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets an opacity factor which specifies the translucency of a 3D map marker.
 Provided value is clamped to the [0.0, 1.0] range.
 The factor is applied to the alpha channel of the resulting texture of the marker.
 Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the
 specified fill color specified
 in <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview"><code>MapMarker3DModel</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The opacity factor adjusting the opacity of a 3D marker.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVisibilityRanges()">
<h3>getVisibilityRanges</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt;</span> <span className="element-name">getVisibilityRanges</span>()</div>
<div className="block"><p>Gets the list of visibility ranges.
 A range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
 is not contained in the range.
 When empty (the default), the 3D marker is visible without map measure restrictions.
 Only <a href="sdk-for-android-navigate-s">MapMeasureRange</a> of <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> type are supported.
 <a href="sdk-for-android-navigate-s">MapMeasureRange</a> of other unsupported types will be ignored.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of visibility ranges. The 3D marker is visible only inside these map measure ranges.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setVisibilityRanges(java.util.List)">
<h3>setVisibilityRanges</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setVisibilityRanges</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt; value)</span></div>
<div className="block"><p>Sets visibility ranges for this 3D marker.
 A range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
 is not contained in the range.
 When empty (the default), the 3D marker is visible without map measure restrictions.
 Only <a href="sdk-for-android-navigate-s">MapMeasureRange</a> of <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> type are supported.
 <a href="sdk-for-android-navigate-s">MapMeasureRange</a> of other unsupported types will be ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The list of visibility ranges. The 3D marker is visible only inside these map measure ranges.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>

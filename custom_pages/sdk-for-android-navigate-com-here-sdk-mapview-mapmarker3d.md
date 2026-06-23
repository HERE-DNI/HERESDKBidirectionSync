---
title: "MapMarker3D (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapMarker3D.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapMarker3D</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapMarker3D</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Represents a 3D shape drawn on the map at specified geodetic coordinates.
 </p><p>It can have a solid color or be textured, depending on the data from
 <a href="sdk-for-android-navigate-mapmarker3dmodel" title="class in com.here.sdk.mapview"><code>MapMarker3DModel</code></a>.
 </p><p>By default, a 3D marker is drawn on top of all map content, including
 3D map elements like extruded buildings or 3D landmarks. This can be
 changed by enabling depth check using <a href="sdk-for-android-navigate-index#setDepthCheckEnabled(boolean)"><code>setDepthCheckEnabled(boolean)</code></a>.
 </p><p>The display of a 3D marker is only guaranteed in case its origin is within
 the viewport. At the moment, this is a known limitation that mostly affects
 a 3D marker that is visually large and covers a sizeable part of the viewport.
 
</p><p>Two aspects determine how big the <code>MapMarker3D</code> will be on the screen
 and how will it behave when the map is zoomed in and out.
 </p><p>The first, and most impactful is <a href="sdk-for-android-navigate-rendersize.unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a>, which specifies
 how the vertex coordinates of the 3D model are interpreted.
 Most importantly, it specifies whether the 3D model is placed
 in world or screen coordinate space.
 </p><p><a href="sdk-for-android-navigate-rendersize.unit#METERS"><code>RenderSize.Unit.METERS</code></a> will make the 3D model use world
 coordinate space, meaning that it will change size together with the map
 when it is zoomed in and out.
 </p><p><a href="sdk-for-android-navigate-rendersize.unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> makes the 3D model use screen coordinate space,
 meaning that it will have constant size on the screen regardless
 of how the map zoom changes. So a simple 10 by 10 (in model space) rectangle
 will have a size of 10 by 10 pixels on the screen.
 </p><p><a href="sdk-for-android-navigate-rendersize.unit#DENSITY_INDEPENDENT_PIXELS"><code>RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS</code></a> is similar to pixels,
 but the resulting size will take into account the pixel density of the
 display, meaning that physical size on the screen will be approximately
 the same regardless of the size or resolution of the display.
 </p><p>The second aspect that determines size of <code>MapMarker3D</code> is scale.
 It can be specified at construction time and can be changed later
 at any time using <a href="sdk-for-android-navigate-index#setScale(double)"><code>setScale(double)</code></a>.
 
</p><p>A 3D marker can be moved around a map by updating its coordinates using
 <a href="sdk-for-android-navigate-index#setCoordinates(com.here.sdk.core.GeoCoordinates)"><code>setCoordinates(com.here.sdk.core.GeoCoordinates)</code></a>.
 </p><p>Altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.
 </p><p>Its orientation is specified by bearing, pitch and roll and can be changed
 by using <a href="sdk-for-android-navigate-index#setBearing(double)"><code>setBearing(double)</code></a>, <a href="sdk-for-android-navigate-index#setPitch(double)"><code>setPitch(double)</code></a>
 and <a href="sdk-for-android-navigate-index#setRoll(double)"><code>setRoll(double)</code></a>.
 
</p><p>A flat marker is a special case of a 3D marker, where the 3D shape being drawn
 is a simple textured rectangle. In essence it's an image drawn "on the ground".
 Such 3D marker can be conveniently created using
 <a href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,double,com.here.sdk.mapview.RenderSize.Unit)"><code>MapMarker3D(GeoCoordinates, MapImage, double, RenderSize.Unit)</code></a>
 constructor. Of course, once created, it can be rotated to face any direction.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,double,com.here.sdk.mapview.RenderSize.Unit)">MapMarker3D</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 <a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image,
 double scale,
 <a href="sdk-for-android-navigate-rendersize.unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> unit)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a flat marker from provided map image.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel)">MapMarker3D</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 <a href="sdk-for-android-navigate-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates an instance of a 3D marker.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double)">MapMarker3D</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 <a href="sdk-for-android-navigate-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model,
 double scale)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an instance of a 3D marker with scale factor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.RenderSize.Unit)">MapMarker3D</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 <a href="sdk-for-android-navigate-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model,
 double scale,
 <a href="sdk-for-android-navigate-rendersize.unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> unit)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new 3D marker at given world coordinates, using the supplied 3D model.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getBearing()">getBearing</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the bearing of the 3D model in degrees.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getCoordinates()">getCoordinates</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the 3D marker's position on the map corresponding to the origin of the 3D marker model
 coordinate system.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-metadata" title="class in com.here.sdk.core">Metadata</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getMetadata()">getMetadata</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-metadata" title="class in com.here.sdk.core"><code>Metadata</code></a> instance attached to this 3D marker.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getOpacity()">getOpacity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns an opacity factor which specifies the translucency of a 3D map marker.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getPitch()">getPitch</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the pitch of the 3D model in degrees.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRoll()">getRoll</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the roll of the 3D model in degrees.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getScale()">getScale</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the scale factor applied to the 3D model before rendering.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getVisibilityRanges()">getVisibilityRanges</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of visibility ranges.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isDepthCheckEnabled()">isDepthCheckEnabled</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns <code>true</code> if depth check is enabled.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isRenderInternalsEnabled()">isRenderInternalsEnabled</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a flag indicating whether to render internal geometry of a 3D marker occluded by its front
 facing polygons.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setBearing(double)">setBearing</a><wbr/>(double value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the bearing of the 3D model in degrees.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setCoordinates(com.here.sdk.core.GeoCoordinates)">setCoordinates</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the 3D marker's position on the map corresponding to the origin of the 3D marker model
 coordinate system.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setDepthCheckEnabled(boolean)">setDepthCheckEnabled</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set whether the depth of the 3D marker's vertices is considered during rendering.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setMetadata(com.here.sdk.core.Metadata)">setMetadata</a><wbr/>(<a href="sdk-for-android-navigate-metadata" title="class in com.here.sdk.core">Metadata</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the <a href="sdk-for-android-navigate-metadata" title="class in com.here.sdk.core"><code>Metadata</code></a> instance attached to this 3D marker.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setOpacity(double)">setOpacity</a><wbr/>(double value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets an opacity factor which specifies the translucency of a 3D map marker.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setPitch(double)">setPitch</a><wbr/>(double value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the pitch of the 3D model in degrees.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRenderInternalsEnabled(boolean)">setRenderInternalsEnabled</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a flag indicating whether to render internal geometry of a 3D marker occluded by its front
 facing polygons.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setRoll(double)">setRoll</a><wbr/>(double value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the roll of the 3D model in degrees.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setScale(double)">setScale</a><wbr/>(double value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the scale factor, to be applied to the 3D model before rendering.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#setVisibilityRanges(java.util.List)">setVisibilityRanges</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets visibility ranges for this 3D marker.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel)">
<h3>MapMarker3D</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarker3D</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 @NonNull
 <a href="sdk-for-android-navigate-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model)</span></div>
<div class="block"><p>Creates an instance of a 3D marker.
 </p><p>The origin of the 3D model's local coordinate system is placed at the specified
 geographical coordinates.
 </p><p>Altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>at</code> - <p>The geographical coordinates where the 3D marker is placed corresponding to origin of the
     3D model's local coordinate system.</p></dd>
<dd><code>model</code> - <p>The 3D model used to draw 3D marker.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,double,com.here.sdk.mapview.RenderSize.Unit)">
<h3>MapMarker3D</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarker3D</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 @NonNull
 <a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image,
 double scale,
 @NonNull
 <a href="sdk-for-android-navigate-rendersize.unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> unit)</span></div>
<div class="block"><p>Creates a flat marker from provided map image.
 </p><p>Such map marker is a flat 3D marker of rectangular shape textured with given image.
 Aspect ratio of the flat marker is determined by aspect ratio of the image.
 </p><p>Only bitmap images are supported, using a <a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview"><code>MapImage</code></a> created from SVG data
 will result in distorted rendering of the flat marker.
 </p><p>Altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.
 </p><p>Size of the rendered flat marker can be specified in either world or screen coordinate space.
 </p><p>For <a href="sdk-for-android-navigate-rendersize.unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a>, the flat marker will cover <code>scale</code> * image's width pixels
 horizontally and <code>scale</code> * image's height pixels vertically. The size of the flat marker
 remains constant on the screen.
 </p><p>For <a href="sdk-for-android-navigate-rendersize.unit#DENSITY_INDEPENDENT_PIXELS"><code>RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS</code></a> the flat marker will cover <code>scale</code> *
 image's width density independent pixels horizontally and <code>scale</code> * image's height
 density independent pixels vertically. The size of the flat marker remains constant on
 the screen.
 </p><p>For <a href="sdk-for-android-navigate-rendersize.unit#METERS"><code>RenderSize.Unit.METERS</code></a> the flat marker will cover <code>scale</code> * image's width meters
 horizontally and <code>scale</code> * image's height meters vertically. Unlike with pixels or
 density independent pixels the size of the flat marker will grow and shrink together
 with regular map content like streets or buildings.</p></div>
<dl class="notes">
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double)">
<h3>MapMarker3D</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarker3D</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 @NonNull
 <a href="sdk-for-android-navigate-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model,
 double scale)</span></div>
<div class="block"><p>Creates an instance of a 3D marker with scale factor.
 </p><p>One unit of the 3D marker model will cover <code>scale</code> pixels.
 The size of the 3D marker remains constant on the screen.
 </p><p>The origin of the 3D model's local coordinate system is placed at the specified
 geographical coordinates.
 </p><p>Altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>at</code> - <p>The geographical coordinates where the 3D marker is placed corresponding to origin of the
     3D model's local coordinate system.</p></dd>
<dd><code>model</code> - <p>The 3D model used to render the 3D marker.</p></dd>
<dd><code>scale</code> - <p>Scale factor to apply to the 3D model.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.RenderSize.Unit)">
<h3>MapMarker3D</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarker3D</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> at,
 @NonNull
 <a href="sdk-for-android-navigate-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model,
 double scale,
 @NonNull
 <a href="sdk-for-android-navigate-rendersize.unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> unit)</span></div>
<div class="block"><p>Creates a new 3D marker at given world coordinates, using the supplied 3D model.
 </p><p>The unit specifies how the 3D geometry of the model is interpreted (meters for world space,
 pixels or density independent pixels for screen space), while scale determines its relative size.
 </p><p>For <a href="sdk-for-android-navigate-rendersize.unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> one unit of the 3D marker model will cover <code>scale</code> pixels.
 The size of the 3D marker remains constant on the screen.
 </p><p>For <a href="sdk-for-android-navigate-rendersize.unit#DENSITY_INDEPENDENT_PIXELS"><code>RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS</code></a> one unit of the 3D marker model will
 cover <code>scale</code> density independent pixels. The size of the 3D marker remains constant on
 the screen.
 </p><p>For <a href="sdk-for-android-navigate-rendersize.unit#METERS"><code>RenderSize.Unit.METERS</code></a> one unit of the 3D marker model will cover <code>scale</code> meters
 in the real world. Unlike with pixels or density-independent pixels the size of the
 3D marker will grow and shrink together with regular map content like streets or buildings.
 </p><p>The origin of the 3D model's local coordinate system is placed at the specified
 geographical coordinates.
 </p><p>Altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.</p></div>
<dl class="notes">
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
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="getCoordinates()">
<h3>getCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">getCoordinates</span>()</div>
<div class="block"><p>Gets the 3D marker's position on the map corresponding to the origin of the 3D marker model
 coordinate system.
 </p><p>The altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The position of the 3D marker on the map corresponding to the origin of the 3D marker model coordinate system.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>setCoordinates</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> value)</span></div>
<div class="block"><p>Sets the 3D marker's position on the map corresponding to the origin of the 3D marker model
 coordinate system.
 </p><p>The altitude component of the coordinates, if set, controls 3D marker's elevation
 above ground. If not set, the 3D marker is placed at ground level.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The position of the 3D marker on the map corresponding to the origin of the 3D marker model coordinate system.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetadata()">
<h3>getMetadata</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-metadata" title="class in com.here.sdk.core">Metadata</a></span> <span class="element-name">getMetadata</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-metadata" title="class in com.here.sdk.core"><code>Metadata</code></a> instance attached to this 3D marker.
 The default value is <code>null</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-metadata" title="class in com.here.sdk.core"><code>Metadata</code></a> instance attached to this 3D marker.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMetadata(com.here.sdk.core.Metadata)">
<h3>setMetadata</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMetadata</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-metadata" title="class in com.here.sdk.core">Metadata</a> value)</span></div>
<div class="block"><p>Sets the <a href="sdk-for-android-navigate-metadata" title="class in com.here.sdk.core"><code>Metadata</code></a> instance attached to this 3D marker.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The <a href="sdk-for-android-navigate-metadata" title="class in com.here.sdk.core"><code>Metadata</code></a> instance attached to this 3D marker.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBearing()">
<h3>getBearing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getBearing</span>()</div>
<div class="block"><p>Gets the bearing of the 3D model in degrees.
 </p><p>The bearing axis is perpendicular to the ground and passes through the 3D marker's location.
 The Z-axis of the model is aligned with bearing axis.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The bearing of the 3D model in degrees, from the true North in clockwise direction.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBearing(double)">
<h3>setBearing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBearing</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets the bearing of the 3D model in degrees.
 </p><p>The bearing axis is perpendicular to the ground and passes through the 3D marker's location.
 The Z-axis of the model is aligned with bearing axis.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The bearing of the 3D model in degrees, from the true North in clockwise direction.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoll()">
<h3>getRoll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getRoll</span>()</div>
<div class="block"><p>Gets the roll of the 3D model in degrees.
 </p><p>The roll axis is parallel to the ground, passes through the 3D marker's
 location and is aligned initially with the true North. However, when the bearing changes,
 it rotates around the bearing axis with the 3D marker.
 Positive/negative values cause a clockwise/counterclockwise rotation when viewing along the axis
 in the direction of the true North. The Y-axis of the model is aligned with the roll axis.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The roll angle of the 3D model in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRoll(double)">
<h3>setRoll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoll</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets the roll of the 3D model in degrees.
 </p><p>The roll axis is parallel to the ground, passes through the 3D marker's
 location and is aligned initially with the true North. However, when the bearing changes,
 it rotates around the bearing axis with the 3D marker.
 Positive/negative values cause a clockwise/counterclockwise rotation when viewing along the axis
 in the direction of the true North. The Y-axis of the model is aligned with the roll axis.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The roll angle of the 3D model in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPitch()">
<h3>getPitch</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getPitch</span>()</div>
<div class="block"><p>Gets the pitch of the 3D model in degrees.
 </p><p>The pitch axis is parallel to the ground, passes through the location of the 3D marker
 and aligns with the longitude axis if the bearing is 0. However, this axis rotates with
 the 3D marker according to the bearing value. Negative values cause the top of the
 3D marker to lean forward. The X-axis of the model is aligned with pitch axis.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The pitch of the 3D model in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPitch(double)">
<h3>setPitch</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPitch</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets the pitch of the 3D model in degrees.
 </p><p>The pitch axis is parallel to the ground, passes through the location of the 3D marker
 and aligns with the longitude axis if the bearing is 0. However, this axis rotates with
 the 3D marker according to the bearing value. Negative values cause the top of the
 3D marker to lean forward. The X-axis of the model is aligned with pitch axis.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The pitch of the 3D model in degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScale()">
<h3>getScale</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getScale</span>()</div>
<div class="block"><p>Gets the scale factor applied to the 3D model before rendering.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Scale factor applied to the 3D model before rendering.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setScale(double)">
<h3>setScale</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setScale</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets the scale factor, to be applied to the 3D model before rendering.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Scale factor applied to the 3D model before rendering.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDepthCheckEnabled()">
<h3>isDepthCheckEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDepthCheckEnabled</span>()</div>
<div class="block"><p>Returns <code>true</code> if depth check is enabled.
 </p><p>If set to <code>false</code>, the 3D marker will always appear in front of any other map objects.
 If set to <code>true</code> the 3D marker might be occluded by other map objects like extruded buildings.
 </p><p>By default depth check is set to <code>false</code>.
 </p><p>Use the altitude of the <a href="sdk-for-android-navigate-index#getCoordinates()"><code>getCoordinates()</code></a> to position the 3D marker sufficiently high above the
 surface. Setting depth check to <code>true</code> will fix visual glitches where components of the marker
 3D model unexpectedly shine through.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Determines whether the depth of the 3D marker's vertices is considered during rendering.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDepthCheckEnabled(boolean)">
<h3>setDepthCheckEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDepthCheckEnabled</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Set whether the depth of the 3D marker's vertices is considered during rendering.
 </p><p>If set to <code>false</code>, the 3D marker will always appear in front of any other map objects.
 If set to <code>true</code> the 3D marker might be occluded by other map objects like extruded buildings.
 </p><p>By default depth check is set to <code>false</code>.
 </p><p>Use the altitude of the <a href="sdk-for-android-navigate-index#getCoordinates()"><code>getCoordinates()</code></a> to position the 3D marker sufficiently high above the
 surface. Setting depth check to <code>true</code> will fix visual glitches where components of the marker
 3D model unexpectedly shine through.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Determines whether the depth of the 3D marker's vertices is considered during rendering.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRenderInternalsEnabled()">
<h3>isRenderInternalsEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRenderInternalsEnabled</span>()</div>
<div class="block"><p>Returns a flag indicating whether to render internal geometry of a 3D marker occluded by its front
 facing polygons. Default value is <code>false</code>.
 </p><p>Default value is <code>false</code>. Can be used with translucent 3D marker.
 </p><p>Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two
 passes: first pass with front-face, second pass with back-face culling enabled.
 With this flag enabled for 3D marker with depth check disabled rendering is performed in a
 single pass with back-face culling disabled.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRenderInternalsEnabled(boolean)">
<h3>setRenderInternalsEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRenderInternalsEnabled</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets a flag indicating whether to render internal geometry of a 3D marker occluded by its front
 facing polygons.
 </p><p>Default value is <code>false</code>. Can be used with translucent 3D marker.
 </p><p>Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two
 passes: first pass with front-face, second pass with back-face culling enabled.
 With this flag enabled for 3D marker with depth check disabled rendering is performed in a
 single pass with back-face culling disabled.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOpacity()">
<h3>getOpacity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getOpacity</span>()</div>
<div class="block"><p>Returns an opacity factor which specifies the translucency of a 3D map marker.
 </p><p>The factor is applied to the alpha channel of the resulting texture of the marker.
 Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the
 specified fill color specified
 in <a href="sdk-for-android-navigate-mapmarker3dmodel" title="class in com.here.sdk.mapview"><code>MapMarker3DModel</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The opacity factor adjusting the opacity of a 3D marker.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOpacity(double)">
<h3>setOpacity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOpacity</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets an opacity factor which specifies the translucency of a 3D map marker.
 </p><p>Provided value is clamped to the [0.0, 1.0] range.
 </p><p>The factor is applied to the alpha channel of the resulting texture of the marker.
 Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the
 specified fill color specified
 in <a href="sdk-for-android-navigate-mapmarker3dmodel" title="class in com.here.sdk.mapview"><code>MapMarker3DModel</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The opacity factor adjusting the opacity of a 3D marker.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibilityRanges()">
<h3>getVisibilityRanges</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt;</span> <span class="element-name">getVisibilityRanges</span>()</div>
<div class="block"><p>Gets the list of visibility ranges.
 </p><p>A range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
 is not contained in the range.
 </p><p>When empty (the default), the 3D marker is visible without map measure restrictions.
 Only <a href="sdk-for-android-navigate-s">MapMeasureRange</a> of <a href="sdk-for-android-navigate-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> type are supported.
 <a href="sdk-for-android-navigate-s">MapMeasureRange</a> of other unsupported types will be ignored.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of visibility ranges. The 3D marker is visible only inside these map measure ranges.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVisibilityRanges(java.util.List)">
<h3>setVisibilityRanges</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisibilityRanges</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt; value)</span></div>
<div class="block"><p>Sets visibility ranges for this 3D marker.
 </p><p>A range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
 is not contained in the range.
 </p><p>When empty (the default), the 3D marker is visible without map measure restrictions.
 Only <a href="sdk-for-android-navigate-s">MapMeasureRange</a> of <a href="sdk-for-android-navigate-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> type are supported.
 <a href="sdk-for-android-navigate-s">MapMeasureRange</a> of other unsupported types will be ignored.</p></div>
<dl class="notes">
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
`
}</HTMLBlock>

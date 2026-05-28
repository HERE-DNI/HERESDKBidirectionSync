---
title: "MapViewBase (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapviewbase"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapViewBase.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-..-..-..-..-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li><a href="#nested-class-summary">Nested</a> | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.mapview</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-explore-mapsurface" title="class in com.here.sdk.mapview">MapSurface</a></code>, <code><a href="sdk-for-android-explore-mapview" title="class in com.here.sdk.mapview">MapView</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">MapViewBase</span></div>
<div class="block"><p>Represents the available public API from  <code>MapView</code>.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-mapviewbase.mappickcallback" title="interface in com.here.sdk.mapview">MapViewBase.MapPickCallback</a></code></div>
<div class="col-last even-row-color">
<div class="block">Callback for a pick request.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)">addLifecycleListener</a><wbr/>(<a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview">MapViewLifecycleListener</a> lifecycleListener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds a <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> to this map view.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-explore-..-core-point2d" title="class in com.here.sdk.core">Point2D</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#geoToViewCoordinates(com.here.sdk.core.GeoCoordinates)">geoToViewCoordinates</a><wbr/>(<a href="sdk-for-android-explore-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoCoordinates)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Converts geographical coordinates to view coordinates (in pixels).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-explore-mapcamera" title="class in com.here.sdk.mapview">MapCamera</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCamera()">getCamera</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the camera to control the view for the map.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFrameRate()">getFrameRate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets maximum render frame rate in frames per second.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-explore-..-gestures-gestures" title="class in com.here.sdk.gestures">Gestures</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getGestures()">getGestures</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the gestures control object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-explore-heremap" title="class in com.here.sdk.mapview">HereMap</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getHereMap()">getHereMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the <a href="sdk-for-android-explore-heremap" title="class in com.here.sdk.mapview"><code>HereMap</code></a> associated with this map view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-explore-mapcontext" title="class in com.here.sdk.mapview">MapContext</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMapContext()">getMapContext</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the map context associated with this map view.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-explore-mapscene" title="class in com.here.sdk.mapview">MapScene</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMapScene()">getMapScene</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the map scene associated with this map view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPixelScale()">getPixelScale</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the pixel scale factor used by this <code>MapView</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-explore-..-core-size2d" title="class in com.here.sdk.core">Size2D</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getViewportSize()">getViewportSize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the size of this map view in physical pixels.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-explore-..-core-size2d" title="class in com.here.sdk.core">Size2D</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getWatermarkSize()">getWatermarkSize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the watermark size in physical pixels.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isValid()">isValid</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns <code>true</code> if this instance is valid, <code>false</code> otherwise.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback)">pick</a><wbr/>(<a href="sdk-for-android-explore-mapscene.mappickfilter" title="class in com.here.sdk.mapview">MapScene.MapPickFilter</a> filter,
 <a href="sdk-for-android-explore-..-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewArea,
 <a href="sdk-for-android-explore-mapviewbase.mappickcallback" title="interface in com.here.sdk.mapview">MapViewBase.MapPickCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns all map content located inside the specified pick area.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)">removeLifecycleListener</a><wbr/>(<a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview">MapViewLifecycleListener</a> lifecycleListener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes a <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> from this map view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setFrameRate(int)">setFrameRate</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets maximum render frame rate in frames per second.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D)">setWatermarkLocation</a><wbr/>(<a href="sdk-for-android-explore-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> anchor,
 <a href="sdk-for-android-explore-..-core-point2d" title="class in com.here.sdk.core">Point2D</a> offset)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the position of the HERE logo watermark within the map view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-explore-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#viewToGeoCoordinates(com.here.sdk.core.Point2D)">viewToGeoCoordinates</a><wbr/>(<a href="sdk-for-android-explore-..-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewCoordinates)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Converts view coordinates (in pixels) to geographical coordinates.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="viewToGeoCoordinates(com.here.sdk.core.Point2D)">
<h3>viewToGeoCoordinates</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-explore-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">viewToGeoCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-..-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewCoordinates)</span></div>
<div class="block"><p>Converts view coordinates (in pixels) to geographical coordinates.
 </p><p>An optional altitude component of the resulting geographical coordinate is not set.
 </p><p>If the view coordinates specify a point above a horizon, then the result
 is geographical coordinates of the point on a horizon below the specified
 view coordinates.
 </p><p>The fog effect is ignored for the calculation, meaning that for the view point
 within the area covered by the fog, the result is geographical coordinates
 that would be displayed at the specified point if the fog effect was
 not applied.
 </p><p>If the render surface is not attached, it will return <code>null</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>viewCoordinates</code> - <p>Point inside the view to convert.</p></dd>
<dt>Returns:</dt>
<dd><p>The geographical coordinates under specified view point or <code>null</code> if there is no render surface attached.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="geoToViewCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>geoToViewCoordinates</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-explore-..-core-point2d" title="class in com.here.sdk.core">Point2D</a></span> <span class="element-name">geoToViewCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoCoordinates)</span></div>
<div class="block"><p>Converts geographical coordinates to view coordinates (in pixels).
 </p><p>If specified, altitude of the input coordinates is interpreted as altitude above sea level.
 If not specified, the input coordinates are interpreted as being on ground elevation.
 The above distinction is only relevant when 3D terrain feature is enabled.
 </p><p>The resulting view coordinates might be outside of current viewport, i.e. result might contain values
 less than zero or greater than view's dimensions.
 </p><p>If the render surface is not attached, it will return <code>null</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoCoordinates</code> - <p>Geographical coordinates to convert.</p></dd>
<dt>Returns:</dt>
<dd><p>The view coordinates of the specified geographical point or <code>null</code>
     if there is no render surface attached.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D)">
<h3>setWatermarkLocation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setWatermarkLocation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> anchor,
 @NonNull
 <a href="sdk-for-android-explore-..-core-point2d" title="class in com.here.sdk.core">Point2D</a> offset)</span></div>
<div class="block"><p>Sets the position of the HERE logo watermark within the map view.
 </p><p>By default, the watermark is aligned to the bottom-right corner of the view:
 Anchor2D(1.0, 1.0) and Point2D(-watermarkSize.width / 2, -watermarkSize.height / 2).
 It is recommended to change the default position only if necessary to avoid overlapping UI elements.
 The watermark should always be fully visible within the view.
 The anchor point on the watermark is its center (width/2, height/2), around which it will be placed
 in the map view.
 For map views smaller than 250 dip in both width and height, the watermark will not be shown.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>anchor</code> - <p>Anchor point in normalized view coordinates [0, 1]. Map view's origin at (0, 0) indicates
     a top-left corner of the map view.
     Out of boundary anchor point values will be clamped to the [0, 1] range.</p></dd>
<dd><code>offset</code> - <p>A horizontal and vertical offset (expressed in positive/negative pixel coordinates) that
     allows shifting the watermark from the anchor point position in one or the other
     direction.
     For the quadrant of values expressing visible part of the map view negative offset shifts
     the watermark to the direction of the origin, positive - away from it.
     For example, the offset of (-10, 5) will shift the watermark 10px to the left and 5px to
     the bottom.
     If specified offset will result in watermark being completely or partially out-of-view
     the offset will be adjusted internally so that watermark is fully visible.
     Offset is not being scaled when the map view size changes.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)">
<h3>addLifecycleListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addLifecycleListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview">MapViewLifecycleListener</a> lifecycleListener)</span></div>
<div class="block"><p>Adds a <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> to this map view.
 Adding the same object multiple times has no effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lifecycleListener</code> - <p>An object to be notified of lifecycle events.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)">
<h3>removeLifecycleListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeLifecycleListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview">MapViewLifecycleListener</a> lifecycleListener)</span></div>
<div class="block"><p>Removes a <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> from this map view.
 Trying to remove an object that was not added or was removed before
 has no effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lifecycleListener</code> - <p>An object to stop being notified of lifecycle events.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback)">
<h3>pick</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">pick</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-explore-mapscene.mappickfilter" title="class in com.here.sdk.mapview">MapScene.MapPickFilter</a> filter,
 @NonNull
 <a href="sdk-for-android-explore-..-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewArea,
 @NonNull
 <a href="sdk-for-android-explore-mapviewbase.mappickcallback" title="interface in com.here.sdk.mapview">MapViewBase.MapPickCallback</a> callback)</span></div>
<div class="block"><p>Returns all map content located inside the specified pick area. Content to be picked is
 specified by a pick content filter.
 The pick area is defined by a rectangle in map view coordinates
 in pixels, relative to the map view's origin at (0, 0) which indicates the top-left corner
 of the map view.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filter</code> - <p>Filter for the map content to be picked. When a filter is not set all of the pickable content will be picked.</p></dd>
<dd><code>viewArea</code> - <p>The rectangular pixel area of the view inside which map content will be picked.
     View area is relative to the map view's origin at (0, 0) at the top-left corner
     of the map view.</p></dd>
<dd><code>callback</code> - <p>Callback to call with the result. This will be called on a main thread when pick operation
     completes.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isValid()">
<h3>isValid</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isValid</span>()</div>
<div class="block"><p>Returns <code>true</code> if this instance is valid, <code>false</code> otherwise. It will be made
 </p><p>It will be made invalid when the corresponding <code>SDKNativeEngine</code> is destroyed.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Indicates whether this instance is valid.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCamera()">
<h3>getCamera</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-explore-mapcamera" title="class in com.here.sdk.mapview">MapCamera</a></span> <span class="element-name">getCamera</span>()</div>
<div class="block"><p>Gets the camera to control the view for the map.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The camera to control the view for the map.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGestures()">
<h3>getGestures</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-explore-..-gestures-gestures" title="class in com.here.sdk.gestures">Gestures</a></span> <span class="element-name">getGestures</span>()</div>
<div class="block"><p>Gets the gestures control object.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The gestures control object for setting up the capture of gestures.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMapScene()">
<h3>getMapScene</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-explore-mapscene" title="class in com.here.sdk.mapview">MapScene</a></span> <span class="element-name">getMapScene</span>()</div>
<div class="block"><p>Gets the map scene associated with this map view.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Map scene associated with this map view.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMapContext()">
<h3>getMapContext</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-explore-mapcontext" title="class in com.here.sdk.mapview">MapContext</a></span> <span class="element-name">getMapContext</span>()</div>
<div class="block"><p>Gets the map context associated with this map view.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Map context associated with this map view.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHereMap()">
<h3>getHereMap</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-explore-heremap" title="class in com.here.sdk.mapview">HereMap</a></span> <span class="element-name">getHereMap</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-explore-heremap" title="class in com.here.sdk.mapview"><code>HereMap</code></a> associated with this map view.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Here Map associated with this map view.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getViewportSize()">
<h3>getViewportSize</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-explore-..-core-size2d" title="class in com.here.sdk.core">Size2D</a></span> <span class="element-name">getViewportSize</span>()</div>
<div class="block"><p>Gets the size of this map view in physical pixels.
 </p><p>If internally the map view's render surface is not attached yet
 (see: <a href="sdk-for-android-explore-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a>), or after the map view has been destroyed
 then a <code>Size2D</code> with zero width and height is returned.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The size of this map view in physical pixels.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFrameRate()">
<h3>getFrameRate</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getFrameRate</span>()</div>
<div class="block"><p>Gets maximum render frame rate in frames per second.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Maximum render frame rate in frames per second.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFrameRate(int)">
<h3>setFrameRate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setFrameRate</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block"><p>Sets maximum render frame rate in frames per second. Setting to 0 disables automatic rendering for this view.
 Setting negative values has no effect. The default value is 60 frames per second.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Maximum render frame rate in frames per second.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPixelScale()">
<h3>getPixelScale</h3>
<div class="member-signature"><span class="return-type">double</span> <span class="element-name">getPixelScale</span>()</div>
<div class="block"><p>Gets the pixel scale factor used by this <code>MapView</code>.
 </p><p>It is used to support screen resolution and size independence.
 This value is a derivative of the device's screen pixel density and is a direct analog of
 </p><p>pixel density from DisplayMetrics.
 </p><p>It can be used to translate between physical pixels and
 </p><p>density-independent pixels
 </p><p>according to the formula:
 </p><p>dp = px / pixelScale.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The pixel scale factor used by this <code>MapView</code>.
     </p><p>Pixel scale is 0.0 if the map view is not initialized.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWatermarkSize()">
<h3>getWatermarkSize</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-explore-..-core-size2d" title="class in com.here.sdk.core">Size2D</a></span> <span class="element-name">getWatermarkSize</span>()</div>
<div class="block"><p>Returns the watermark size in physical pixels.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Provides the size of the watermark in physical pixels.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
</div>
</div>



</div>
`
}</HTMLBlock>

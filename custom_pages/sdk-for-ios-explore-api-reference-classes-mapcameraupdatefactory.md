---
title: "MapCameraUpdateFactory"
slug: "sdk-for-ios-explore-api-reference-classes-mapcameraupdatefactory"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapCameraUpdateFactory"></a>
<a title="MapCameraUpdateFactory Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

        MapCameraUpdateFactory Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapCameraUpdateFactory</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapCameraUpdateFactory</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraUpdateFactory</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraUpdateFactory</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Factory for creating MapCameraUpdate to change map’s camera.</p>
<p>For some factory methods you can apply an additional padding in pixels by setting a
<code>viewRectangle</code> parameter based on the current size of the map view:</p>
<pre class="highlight swift"><code><span class="k">let</span> <span class="nv">leftPaddingInPixels</span> <span class="o">=</span> <span class="mi">5</span>
<span class="k">let</span> <span class="nv">rightPaddingInPixels</span> <span class="o">=</span> <span class="mi">5</span>
<span class="k">let</span> <span class="nv">topPaddingInPixels</span> <span class="o">=</span> <span class="mi">5</span>
<span class="k">let</span> <span class="nv">bottomPaddingInPixels</span> <span class="o">=</span> <span class="mi">5</span>
<span class="k">let</span> <span class="nv">horizontalPaddingInPixels</span> <span class="o">=</span> <span class="n">leftPaddingInPixels</span> <span class="o">+</span> <span class="n">rightPaddingInPixels</span>
<span class="k">let</span> <span class="nv">verticalPaddingInPixels</span> <span class="o">=</span> <span class="n">topPaddingInPixels</span> <span class="o">+</span> <span class="n">bottomPaddingInPixels</span>

<span class="k">let</span> <span class="nv">origin</span> <span class="o">=</span> <span class="kt">Point2D</span><span class="p">(</span><span class="n">leftPaddingInPixels</span><span class="p">,</span> <span class="n">topPaddingInPixels</span><span class="p">)</span>
<span class="k">let</span> <span class="nv">sizeInPixels</span> <span class="o">=</span> <span class="kt">Size2D</span><span class="p">(</span><span class="nv">width</span><span class="p">:</span> <span class="n">mapView</span><span class="o">.</span><span class="n">viewportSize</span><span class="o">.</span><span class="n">width</span> <span class="o">-</span> <span class="n">horizontalPaddingInPixels</span><span class="p">,</span> <span class="nv">height</span><span class="p">:</span> <span class="n">mapView</span><span class="o">.</span><span class="n">viewportSize</span><span class="o">.</span><span class="n">height</span> <span class="o">-</span> <span class="n">verticalPaddingInPixels</span><span class="p">)</span>
<span class="k">let</span> <span class="nv">paddedViewRectangle</span> <span class="o">=</span> <span class="kt">Rectangle2D</span><span class="p">(</span><span class="nv">origin</span><span class="p">:</span> <span class="n">origin</span><span class="p">,</span> <span class="nv">size</span><span class="p">:</span> <span class="n">sizeInPixels</span><span class="p">)</span>
</code></pre>
<p>The origin indicates the top-left corner of the rectangle. An origin of (0, 0) indicates
also the top-left corner of the map’s viewport.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC6lookAt5pointAA0bcD0CAA014GeoCoordinatesD0V_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(point:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC6lookAt5pointAA0bcD0CAA014GeoCoordinatesD0V_tFZ">lookAt(point:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to position the map camera to look at the given target,
preserving the current orientation at look-at target and map measure.</p>
<p>Any target sub-element value that is not finite will be excluded from the update.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">point</span> <span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>The look-at target position in geodetic coordinates, altitude is ignored,
the target is considered to be located on the ground.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC6lookAt5point11orientationAA0bcD0CAA014GeoCoordinatesD0V_AA0j11OrientationD0VtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(point:orientation:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC6lookAt5point11orientationAA0bcD0CAA014GeoCoordinatesD0V_AA0j11OrientationD0VtFZ">lookAt(point:<wbr/>orientation:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to position the map camera to look at the given target with the given
orientation preserving the current map measure (zoom level/distance/scale)
Any target or orientation sub-element value that is not finite will be excluded from the update.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">point</span> <span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a></span><span class="p">,</span> <span class="nv">orientation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>The look-at target position in geodetic coordinates.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>orientation</em>
</code>
</td>
<td>
<div>
<p>Geodetic orientation at look-at target.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC6lookAt5point7measureAA0bcD0CAA014GeoCoordinatesD0V_AA0B7MeasureVtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(point:measure:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC6lookAt5point7measureAA0bcD0CAA014GeoCoordinatesD0V_AA0B7MeasureVtFZ">lookAt(point:<wbr/>measure:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to position the map camera to look at the given target with the given
map measure preserving the current orientation at look-at target.
Any target sub-element value that is not finite will be excluded from the update.
If the map measure is not valid, the current map camera distance to the target point is preserved.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">point</span> <span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a></span><span class="p">,</span> <span class="nv">measure</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>The look-at target position in geodetic coordinates.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>measure</em>
</code>
</td>
<td>
<div>
<p>The desired map measure.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC6lookAt5point11orientation7measureAA0bcD0CAA014GeoCoordinatesD0V_AA0k11OrientationD0VAA0B7MeasureVtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(point:orientation:measure:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC6lookAt5point11orientation7measureAA0bcD0CAA014GeoCoordinatesD0V_AA0k11OrientationD0VAA0B7MeasureVtFZ">lookAt(point:<wbr/>orientation:<wbr/>measure:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to position the map camera to look at the given target with the given
orientation and map measure.
Any target or orientation sub-element value that is not finite will be excluded from the update.
If the map measure is not valid, the current map camera distance to the target point is preserved.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">point</span> <span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a></span><span class="p">,</span> <span class="nv">orientation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">,</span> <span class="nv">measure</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>The look-at target position in geodetic coordinates.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>orientation</em>
</code>
</td>
<td>
<div>
<p>Geodetic orientation at look-at target.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>measure</em>
</code>
</td>
<td>
<div>
<p>The desired map measure.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC11lookToMatch5point9viewPoint11orientation7measureAA0bcD0CAA14GeoCoordinatesV_AA7Point2DVAA0n11OrientationD0VAA0B7MeasureVtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookToMatch(point:viewPoint:orientation:measure:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC11lookToMatch5point9viewPoint11orientation7measureAA0bcD0CAA14GeoCoordinatesV_AA7Point2DVAA0n11OrientationD0VAA0B7MeasureVtFZ">lookToMatch(point:<wbr/>viewPoint:<wbr/>orientation:<wbr/>measure:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to position the map camera to look at the map with the given
orientation and map measure and with the given geo point located at the given view point.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
<p>Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookToMatch</span><span class="p">(</span><span class="n">point</span> <span class="nv">geoPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">viewPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-point2d">Point2D</a></span><span class="p">,</span> <span class="nv">orientation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">,</span> <span class="nv">measure</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoPoint</em>
</code>
</td>
<td>
<div>
<p>The geo point that will be matched to the given view point.
Note: the geo point will differ from the look at target of the camera. After this update the camera
will still look at the principal point and therefore the look at target will be different from the geo
point, since the geo point will correspond to the given view point and the look at target
will correspond to the principal point. Look at target and the geo point will be identical only
if the given view point is identical to the principal point.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>viewPoint</em>
</code>
</td>
<td>
<div>
<p>View point coordinates in pixels.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>orientation</em>
</code>
</td>
<td>
<div>
<p>Geodetic orientation at look-at target.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>measure</em>
</code>
</td>
<td>
<div>
<p>The desired map measure.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC11lookToMatch5point9viewPointAA0bcD0CAA14GeoCoordinatesV_AA7Point2DVtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookToMatch(point:viewPoint:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC11lookToMatch5point9viewPointAA0bcD0CAA14GeoCoordinatesV_AA7Point2DVtFZ">lookToMatch(point:<wbr/>viewPoint:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to position the map camera to look at the map
with the given geo point located at the given view point.
Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<p>The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookToMatch</span><span class="p">(</span><span class="n">point</span> <span class="nv">geoPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">viewPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-point2d">Point2D</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoPoint</em>
</code>
</td>
<td>
<div>
<p>The geo point that will be matched to the given view point.
Note: the geo point will differ from the look at target of the camera. After this update the camera
will still look at the principal point and therefore the look at target will be different from the geo
point, since the geo point will correspond to the given view point and the look at target
will correspond to the principal point. Look at target and the geo point will be identical only
if the given view point is identical to the principal point.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>viewPoint</em>
</code>
</td>
<td>
<div>
<p>View point coordinates in pixels.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC6lookAt_13viewRectangle11orientation12measureLimitAA0bcD0CSayAA14GeoCoordinatesVG_AA11Rectangle2DVAA0m11OrientationD0VAA0B7MeasureVtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(_:viewRectangle:orientation:measureLimit:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC6lookAt_13viewRectangle11orientation12measureLimitAA0bcD0CSayAA14GeoCoordinatesVG_AA11Rectangle2DVAA0m11OrientationD0VAA0B7MeasureVtFZ">lookAt(_:<wbr/>viewRectangle:<wbr/>orientation:<wbr/>measureLimit:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Create an update to look at the given geo locations and fit them inside the given rectangle,
in accordance with a map measure limit.</p>
<p>If the provided <code>MapCameraUpdateFactory.lookAt([GeoCoordinates], Rectangle2D, GeoOrientationUpdate, MapMeasure).points</code> list is empty, no update will be applied to the camera.</p>
<p>If the <code>MapCameraUpdateFactory.lookAt([GeoCoordinates], Rectangle2D, GeoOrientationUpdate, MapMeasure).viewRectangle</code> parameter is invalid, fully or partially outside the map view,
then the entire map viewport will be used as <code>MapCameraUpdateFactory.lookAt([GeoCoordinates], Rectangle2D, GeoOrientationUpdate, MapMeasure).viewRectangle</code>. Thus, no padding will be applied.
A <code>MapCameraUpdateFactory.lookAt([GeoCoordinates], Rectangle2D, GeoOrientationUpdate, MapMeasure).viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
coordinates (x, y) are invalid, when they are negative.</p>
<p>All <code>MapCameraUpdateFactory.lookAt([GeoCoordinates], Rectangle2D, GeoOrientationUpdate, MapMeasure).viewRectangle</code> values need to be finite to be considered as valid.
If measure limit is not valid, no update will be applied to the map camera.</p>
<p>The altitude of the target points is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">_</span> <span class="nv">points</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">],</span> <span class="nv">viewRectangle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-rectangle2d">Rectangle2D</a></span><span class="p">,</span> <span class="nv">orientation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">,</span> <span class="nv">measureLimit</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>points</em>
</code>
</td>
<td>
<div>
<p>Array of points in geodetic space that should be visible inside the given view rectangle.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>viewRectangle</em>
</code>
</td>
<td>
<div>
<p>View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>orientation</em>
</code>
</td>
<td>
<div>
<p>Geodetic orientation at the new calculated target point.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>measureLimit</em>
</code>
</td>
<td>
<div>
<p>Map measure limit:

<ul>
<li>as distance: the minimum distance from map camera to earth surface at the center of the view rectangle in meters.
The map camera should not be positioned closer to the center of view rectangle than this.</li>
<li>as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the center of view rectangle in meters. This is not the zoom level for
the calculated lookAt target point. Can be used to not zoom closer than a given level.</li>
<li>as scale: the minimum scale for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the center of view rectangle in meters. This is not the scale for
the calculated lookAt target point.</li>
</ul></p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC6lookAt_11orientation6points13viewRectangle10minMeasure03maxM0AA0bcD0CAA014GeoCoordinatesD0V_AA0o11OrientationD0VSayAA0oP0VGAA11Rectangle2DVAA0bM0VAVtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(_:orientation:points:viewRectangle:minMeasure:maxMeasure:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC6lookAt_11orientation6points13viewRectangle10minMeasure03maxM0AA0bcD0CAA014GeoCoordinatesD0V_AA0o11OrientationD0VSayAA0oP0VGAA11Rectangle2DVAA0bM0VAVtFZ">lookAt(_:<wbr/>orientation:<wbr/>points:<wbr/>viewRectangle:<wbr/>minMeasure:<wbr/>maxMeasure:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to position the camera to look at the given target with the given
orientation and obeying map measure limits, so that the given geo locations are inside the given rectangle.
Such position update can possibly not be found.</p>
<p>Any target or orientation sub-element value that is not finite will be excluded from the update.</p>
<p>If the provided <code>MapCameraUpdateFactory.lookAt(GeoCoordinatesUpdate, GeoOrientationUpdate, [GeoCoordinates], Rectangle2D, MapMeasure, MapMeasure).points</code> list is empty, no update will be applied to the map camera.</p>
<p>If the <code>MapCameraUpdateFactory.lookAt(GeoCoordinatesUpdate, GeoOrientationUpdate, [GeoCoordinates], Rectangle2D, MapMeasure, MapMeasure).viewRectangle</code> parameter is invalid, fully or partially outside the map view,
then the entire map viewport will be used as <code>MapCameraUpdateFactory.lookAt(GeoCoordinatesUpdate, GeoOrientationUpdate, [GeoCoordinates], Rectangle2D, MapMeasure, MapMeasure).viewRectangle</code>. Thus, no padding will be applied.
A <code>MapCameraUpdateFactory.lookAt(GeoCoordinatesUpdate, GeoOrientationUpdate, [GeoCoordinates], Rectangle2D, MapMeasure, MapMeasure).viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
coordinates (x, y) are invalid, when they are negative.</p>
<p>If map measures are not valid, no update will be applied to the map camera.</p>
<p>The altitude of the target points is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">_</span> <span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a></span><span class="p">,</span> <span class="nv">orientation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">,</span> <span class="nv">points</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">],</span> <span class="nv">viewRectangle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-rectangle2d">Rectangle2D</a></span><span class="p">,</span> <span class="nv">minMeasure</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="p">,</span> <span class="nv">maxMeasure</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>The look-at target position in geodetic coordinates.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>orientation</em>
</code>
</td>
<td>
<div>
<p>Geodetic orientation at look-at target.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>points</em>
</code>
</td>
<td>
<div>
<p>Array of points in geodetic space that should be visible inside the given view rectangle.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>viewRectangle</em>
</code>
</td>
<td>
<div>
<p>View rectangle in viewport pixel coordinates inside which the geographical points are displayed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>minMeasure</em>
</code>
</td>
<td>
<div>
<p>Minimum map measure:

<ul>
<li>as distance: the minimum distance from map camera to earth surface at the look-at target in meters.
The map camera should not be positioned closer to target than this.</li>
<li>as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the look-at target in meters.
Can be used to not zoom closer than a given level.</li>
<li>as scale: the minimum scale for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the look-at target in meters.</li>
</ul></p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>maxMeasure</em>
</code>
</td>
<td>
<div>
<p>Maximum map measure:

<ul>
<li>as distance: the maximum distance from map camera to earth surface at the look-at target in meters.
The map camera should not be positioned further from target than this.</li>
<li>as zoom level: the minimum zoom level for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the look-at target in meters.
Can be used to not zoom further than a given level.</li>
<li>as scale: the maximum scale for the new map camera state. Internally converted to minimum distance
from map camera to earth surface at the look-at target in meters.</li>
</ul></p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC6lookAt4area11orientation13viewRectangleAA0bcD0CAA6GeoBoxV_AA0l11OrientationD0VAA11Rectangle2DVtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(area:orientation:viewRectangle:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC6lookAt4area11orientation13viewRectangleAA0bcD0CAA6GeoBoxV_AA0l11OrientationD0VAA11Rectangle2DVtFZ">lookAt(area:<wbr/>orientation:<wbr/>viewRectangle:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Create an update to look at the given geo-box and fit it inside the given rectangle.</p>
<p>If geoBox is not valid, no update will be applied to the map camera.</p>
<p>If the <code>MapCameraUpdateFactory.lookAt(GeoBox, GeoOrientationUpdate, Rectangle2D).viewRectangle</code> parameter is invalid, fully or partially outside the map view,
then the entire map viewport will be used as <code>MapCameraUpdateFactory.lookAt(GeoBox, GeoOrientationUpdate, Rectangle2D).viewRectangle</code>. Thus, no padding will be applied.
A <code>MapCameraUpdateFactory.lookAt(GeoBox, GeoOrientationUpdate, Rectangle2D).viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
coordinates (x, y) are invalid, when they are negative.</p>
<p>All <code>MapCameraUpdateFactory.lookAt(GeoBox, GeoOrientationUpdate, Rectangle2D).viewRectangle</code> values need to be finite to be considered as valid.</p>
<p>In cases where it is not possible to find a solution for the given parameters,
the resulting MapCameraUpdate will not change the map camera.</p>
<p>The altitude of the target points is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">area</span> <span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geobox">GeoBox</a></span><span class="p">,</span> <span class="nv">orientation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">,</span> <span class="nv">viewRectangle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-rectangle2d">Rectangle2D</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>Geodetic box that should be visible inside the given view rectangle.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>orientation</em>
</code>
</td>
<td>
<div>
<p>Geodetic orientation at the target point.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>viewRectangle</em>
</code>
</td>
<td>
<div>
<p>View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC6lookAt4area13viewRectangleAA0bcD0CAA6GeoBoxV_AA11Rectangle2DVtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(area:viewRectangle:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC6lookAt4area13viewRectangleAA0bcD0CAA6GeoBoxV_AA11Rectangle2DVtFZ">lookAt(area:<wbr/>viewRectangle:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to look at the given geo-box and fit it inside the given rectangle,
preserving current orientation and zooming at the center of view rectangle.</p>
<p>If geoBox is not valid, no update will be applied to the map camera.</p>
<p>If the <code>MapCameraUpdateFactory.lookAt(GeoBox, Rectangle2D).viewRectangle</code> parameter is invalid, fully or partially outside the map view,
then the entire map viewport will be used as <code>MapCameraUpdateFactory.lookAt(GeoBox, Rectangle2D).viewRectangle</code>. Thus, no padding will be applied.
A <code>MapCameraUpdateFactory.lookAt(GeoBox, Rectangle2D).viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
coordinates (x, y) are invalid, when they are negative.</p>
<p>In cases where it is not possible to find a solution for the given parameters,
the resulting MapCameraUpdate will not change the map camera.</p>
<p>The altitude of the target points is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">area</span> <span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geobox">GeoBox</a></span><span class="p">,</span> <span class="nv">viewRectangle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-rectangle2d">Rectangle2D</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>Geodetic box that should be visible inside the given view rectangle.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>viewRectangle</em>
</code>
</td>
<td>
<div>
<p>View rectangle in viewport pixel coordinates.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC6lookAt4areaAA0bcD0CAA6GeoBoxV_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAt(area:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC6lookAt4areaAA0bcD0CAA6GeoBoxV_tFZ">lookAt(area:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to look at the given geo-box,
preserving current orientation and zooming at the center of viewport.</p>
<p>If geoBox is not valid, no update will be applied to the map camera.</p>
<p>The altitude of the target points is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookAt</span><span class="p">(</span><span class="n">area</span> <span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geobox">GeoBox</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>Geodetic box that should be visible inside the viewport rectangle.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC5panBy7xOffset01yH0AA0bcD0CSd_SdtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/panBy(xOffset:yOffset:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC5panBy7xOffset01yH0AA0bcD0CSd_SdtFZ">panBy(xOffset:<wbr/>yOffset:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to pan map camera over the map by the specified number of pixels
in the x and y direction starting from current principal point position.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">panBy</span><span class="p">(</span><span class="nv">xOffset</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">yOffset</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>xOffset</em>
</code>
</td>
<td>
<div>
<p>X offset in pixels</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>yOffset</em>
</code>
</td>
<td>
<div>
<p>Y offset in pixels</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC7orbitBy_6aroundAA0bcD0CAA014GeoOrientationD0V_AA7Point2DVtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/orbitBy(_:around:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC7orbitBy_6aroundAA0bcD0CAA014GeoOrientationD0V_AA7Point2DVtFZ">orbitBy(_:<wbr/>around:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to orbit map camera around a pixel origin by specified geodetic orientation delta.
If the origin cannot be converted to geo coordinates, no update will be applied to the map camera.</p>
<p>Orientation elements that are not valid will be excluded from the update.
Resulting bearing values are wrapped around degrees range [0, 360].
Resulting tilt values are clamped inside degrees range [0, 180].
Resulting roll values are wrapped around degrees range [-180, 180].</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">orbitBy</span><span class="p">(</span><span class="n">_</span> <span class="nv">delta</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">,</span> <span class="n">around</span> <span class="nv">origin</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-point2d">Point2D</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delta</em>
</code>
</td>
<td>
<div>
<p>Geodetic orientation delta update.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>origin</em>
</code>
</td>
<td>
<div>
<p>Screen pixel origin of rotation.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC8rotateByyAA0bcD0CAA014GeoOrientationD0VFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/rotateBy(_:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC8rotateByyAA0bcD0CAA014GeoOrientationD0VFZ">rotateBy(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to change map camera orientation by specified geodetic orientation delta.
Orientation elements that are not valid will be excluded from the update.
Resulting bearing values are wrapped around degrees range [0, 360].
Resulting tilt values are clamped inside degrees range [0, 180].
Resulting roll values are wrapped around degrees range [-180, 180].</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">rotateBy</span><span class="p">(</span><span class="n">_</span> <span class="nv">delta</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delta</em>
</code>
</td>
<td>
<div>
<p>Geodetic orientation delta update.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC6zoomBy_6aroundAA0bcD0CSd_AA7Point2DVtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/zoomBy(_:around:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC6zoomBy_6aroundAA0bcD0CSd_AA7Point2DVtFZ">zoomBy(_:<wbr/>around:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to zoom map camera by a given factor preserving a given focus point.</p>
<p>Values greater than 1 zoom in map camera, by moving it closer to the ground; less than 1 - zoom out,
which moves map camera further.</p>
<p>If factor is zero, negative or not finite, no update will be applied to the map camera.</p>
<p>If the focusPoint is not inside the viewport bounds, then the current principal point will be used.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">zoomBy</span><span class="p">(</span><span class="n">_</span> <span class="nv">factor</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="n">around</span> <span class="nv">origin</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-point2d">Point2D</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>factor</em>
</code>
</td>
<td>
<div>
<p>Zooming factor.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>origin</em>
</code>
</td>
<td>
<div>
<p>Pixel location on the screen to use as zoom origin.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC6zoomTo0F5LevelAA0bcD0CSd_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/zoomTo(zoomLevel:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC6zoomTo0F5LevelAA0bcD0CSd_tFZ">zoomTo(zoomLevel:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to move map camera’s viewpoint to a particular zoom level by adjusting its position.</p>
<p>If zoomLevel is not finite, no update will be applied to the map camera.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">zoomTo</span><span class="p">(</span><span class="nv">zoomLevel</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>zoomLevel</em>
</code>
</td>
<td>
<div>
<p>The desired zoom level.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC17setPrincipalPointyAA0bcD0CAA7Point2DVFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setPrincipalPoint(_:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC17setPrincipalPointyAA0bcD0CAA7Point2DVFZ">setPrincipalPoint(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to change the map camera’s principal point (where the view vector intersects
the image plane - default is the center of the view). Point values are in screen coordinates
and values that fall outside of the viewport, are clamped.
(0,0) is top left of the viewport.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">setPrincipalPoint</span><span class="p">(</span><span class="n">_</span> <span class="nv">principalPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-point2d">Point2D</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>principalPoint</em>
</code>
</td>
<td>
<div>
<p>Principal point in absolute viewport pixel coordinates.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC27setNormalizedPrincipalPointyAA0bcD0CAA8Anchor2DVFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setNormalizedPrincipalPoint(_:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC27setNormalizedPrincipalPointyAA0bcD0CAA8Anchor2DVFZ">setNormalizedPrincipalPoint(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to change the map camera’s principal point (where the view vector
intersects the image plane - default is (0.5, 0.5)). Point values are in normalized screen coordinates.</p>
<p>If the principalPoint is outside [0,1] interval, it is clamped.
(0,0) is top left of the viewport, (1,1) is bottom right.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">setNormalizedPrincipalPoint</span><span class="p">(</span><span class="n">_</span> <span class="nv">principalPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-anchor2d">Anchor2D</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>principalPoint</em>
</code>
</td>
<td>
<div>
<p>Principal point in normalized screen coordinates.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC22setVerticalFieldOfViewyAA0bcD0CSdFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setVerticalFieldOfView(_:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC22setVerticalFieldOfViewyAA0bcD0CSdFZ">setVerticalFieldOfView(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an update to change the vertical field of view of the map camera.</p>
<p>If verticalFieldOfView is not finite, no update will be applied to the map camera.</p>
<p>If the verticalFieldOfView is outside [1, 150] interval, it is clamped.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">setVerticalFieldOfView</span><span class="p">(</span><span class="n">_</span> <span class="nv">verticalFieldOfView</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>verticalFieldOfView</em>
</code>
</td>
<td>
<div>
<p>Vertical field of view in degrees.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC09compositeD0yAA0bcD0CSayAFGKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/compositeUpdate(_:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC09compositeD0yAA0bcD0CSayAFGKFZ">compositeUpdate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a composite camera update from a list of camera updates. The result update will be
equivalent to executing all given updates sequentially in the order they were provided.</p>
<p>MapCameraAnimation instances derived from the MapCameraAnimationFactory and a composite camera
update are not supported. An AnimationListener will receive an AnimationState.Cancelled signal
when trying to apply such animations.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapCameraUpdate.html#/s:7heresdk15MapCameraUpdateC18InstantiationErrora">MapCameraUpdate.InstantiationError</a></code> Indicates an instantiation issue.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">compositeUpdate</span><span class="p">(</span><span class="n">_</span> <span class="nv">mapCameraUpdates</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span><span class="p">])</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">MapCameraUpdate</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapCameraUpdates</em>
</code>
</td>
<td>
<div>
<p>List of MapCamera updates.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraUpdate instance.</p>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
}</HTMLBlock>

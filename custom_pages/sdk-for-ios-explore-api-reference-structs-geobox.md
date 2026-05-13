---
title: "GeoBox Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-geobox"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- GeoBox.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoBox"></a>
<a title="GeoBox Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-core">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        GeoBox Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct GeoBox : Hashable</code></pre>
</div>
</div>
<p>Represents a bounding rectangle aligned with latitude and longitude.
Geographic area represented by this would be visualised as a rectangle
when using a normal cylindrical projection (such as Mercator).
The box has a maximum span of 360 degrees in longitude and 180 degrees in latitude direction.
The box with equal values in longitude for the corners is considered as a span of 360 degrees.
The box is considered empty if the latitude of the <code><a href="../Structs/GeoBox.html#/s:7heresdk6GeoBoxV15southWestCornerAA0B11CoordinatesVvp">GeoBox.southWestCorner</a></code> is larger than the the
latitude of the <code><a href="../Structs/GeoBox.html#/s:7heresdk6GeoBoxV15northEastCornerAA0B11CoordinatesVvp">GeoBox.northEastCorner</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6GeoBoxV15southWestCornerAA0B11CoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/southWestCorner"></a>
<a class="token" href="#/s:7heresdk6GeoBoxV15southWestCornerAA0B11CoordinatesVvp">southWestCorner</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>South west corner coordinates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let southWestCorner: GeoCoordinates</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6GeoBoxV15northEastCornerAA0B11CoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/northEastCorner"></a>
<a class="token" href="#/s:7heresdk6GeoBoxV15northEastCornerAA0B11CoordinatesVvp">northEastCorner</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>North east corner coordinates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let northEastCorner: GeoCoordinates</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6GeoBoxV15southWestCorner09northEastF0AcA0B11CoordinatesV_AGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(southWestCorner:northEastCorner:)"></a>
<a class="token" href="#/s:7heresdk6GeoBoxV15southWestCorner09northEastF0AcA0B11CoordinatesV_AGtcfc">init(southWestCorner:<wbr/>northEastCorner:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(southWestCorner: GeoCoordinates, northEastCorner: GeoCoordinates)</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6GeoBoxV10containing14geoCoordinatesACSgSayAA0bF0VG_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/containing(geoCoordinates:)"></a>
<a class="token" href="#/s:7heresdk6GeoBoxV10containing14geoCoordinatesACSgSayAA0bF0VG_tFZ">containing(geoCoordinates:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a <code>GeoBox</code> which encompases all coordinates from the list.
The provided list must contain at least two points.
The altitude values of the input coordinates are not considered for the result.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static func containing(geoCoordinates: [GeoCoordinates]) -&gt; GeoBox?</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoCoordinates</em>
</code>
</td>
<td>
<div>
<p>List of coordinates to encompass inside bounding box.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code>GeoBox</code> containing all supplied coordinates, or <code>nil</code> if less than two coordinates were provided.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6GeoBoxV8envelope03geoC0A2C_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/envelope(geoBox:)"></a>
<a class="token" href="#/s:7heresdk6GeoBoxV8envelope03geoC0A2C_tF">envelope(geoBox:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Envelopes two <code>GeoBox</code> areas by returning the smallest <code>GeoBox</code> covering both this
GeoBox and the specified <code>GeoBox</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func envelope(geoBox: GeoBox) -&gt; GeoBox</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoBox</em>
</code>
</td>
<td>
<div>
<p>Another <code>GeoBox</code> to envelope with.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code>GeoBox</code> covering two<code>GeoBox</code> areas</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6GeoBoxV08envelopeB5Boxes03geoE0ACSgSayACG_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/envelopeGeoBoxes(geoBoxes:)"></a>
<a class="token" href="#/s:7heresdk6GeoBoxV08envelopeB5Boxes03geoE0ACSgSayACG_tFZ">envelopeGeoBoxes(geoBoxes:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Envelopes the list of <code>GeoBox</code> areas by returning the smallest
<code>GeoBox</code> covering all specified <code>GeoBox</code> objects.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static func envelopeGeoBoxes(geoBoxes: [GeoBox]) -&gt; GeoBox?</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoBoxes</em>
</code>
</td>
<td>
<div>
<p>List of <code>GeoBox</code> objects.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code>GeoBox</code> covering all <code>GeoBox</code> areas, or <code>nil</code>
if input is empty.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6GeoBoxV10intersects03geoC0SbAC_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/intersects(geoBox:)"></a>
<a class="token" href="#/s:7heresdk6GeoBoxV10intersects03geoC0SbAC_tF">intersects(geoBox:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Determines whether this <code>GeoBox</code> intersects with the passed <code>GeoBox</code>.
The altitude values are ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func intersects(geoBox: GeoBox) -&gt; Bool</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoBox</em>
</code>
</td>
<td>
<div>
<p>A <code>GeoBox</code> to check for intersection.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code>true</code> if intersects with the <code>GeoBox</code>, <code>false</code> otherwise.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6GeoBoxV12intersection03geoC0SayACGAC_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/intersection(geoBox:)"></a>
<a class="token" href="#/s:7heresdk6GeoBoxV12intersection03geoC0SayACGAC_tF">intersection(geoBox:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Computes the intersection with the passed <code>GeoBox</code>.
The altitude values are ignored.
Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func intersection(geoBox: GeoBox) -&gt; [GeoBox]</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoBox</em>
</code>
</td>
<td>
<div>
<p>Another geo box to check intersection with.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>It will be empty if there is no overlap.
Otherwise, 1 or more geo boxes covering common area by this and passed <code>GeoBox</code>.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6GeoBoxV12intersection8geoBoxesSayACGAF_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/intersection(geoBoxes:)"></a>
<a class="token" href="#/s:7heresdk6GeoBoxV12intersection8geoBoxesSayACGAF_tFZ">intersection(geoBoxes:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Computes intersection of list of <code>GeoBox</code> instances.
The altitude values are ignored.
Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static func intersection(geoBoxes: [GeoBox]) -&gt; [GeoBox]</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoBoxes</em>
</code>
</td>
<td>
<div>
<p>List of <code>GeoBox</code> instances.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>It will be empty if there is no overlap between all the passed <code>GeoBox</code> instances.
Otherwise, 1 or more geo boxes covering common area by all the passed <code>GeoBox</code> instances.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6GeoBoxV8contains03geoC0SbAC_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/contains(geoBox:)"></a>
<a class="token" href="#/s:7heresdk6GeoBoxV8contains03geoC0SbAC_tF">contains(geoBox:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Determines whether the specified <code>GeoBox</code> is covered entirely by this <code>GeoBox</code>.
The altitude values are ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func contains(geoBox: GeoBox) -&gt; Bool</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoBox</em>
</code>
</td>
<td>
<div>
<p>A <code>GeoBox</code> to check for containment within this <code>GeoBox</code>.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code>true</code> if covered by the <code>GeoBox</code>, <code>false</code> otherwise.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6GeoBoxV8contains14geoCoordinatesSbAA0bF0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/contains(geoCoordinates:)"></a>
<a class="token" href="#/s:7heresdk6GeoBoxV8contains14geoCoordinatesSbAA0bF0V_tF">contains(geoCoordinates:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Determines whether the specified GeoCoordinates is contained within this <code>GeoBox</code>.
The altitude values are ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func contains(geoCoordinates: GeoCoordinates) -&gt; Bool</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoCoordinates</em>
</code>
</td>
<td>
<div>
<p>A GeoCoordinates to check for containment within this <code>GeoBox</code>.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code>true</code> if contained within the <code>GeoBox</code>, <code>false</code> otherwise.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6GeoBoxV10expandedBy11southMeters04westG005northG004eastG0ACSd_S3dtKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/expandedBy(southMeters:westMeters:northMeters:eastMeters:)"></a>
<a class="token" href="#/s:7heresdk6GeoBoxV10expandedBy11southMeters04westG005northG004eastG0ACSd_S3dtKF">expandedBy(southMeters:<wbr/>westMeters:<wbr/>northMeters:<wbr/>eastMeters:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a <code>GeoBox</code> which is expanded by a fixed distance.
Throws an InstantiationError if it is not possible to create a valid
<code>GeoBox</code> with the given arguments.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Instantiation error.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func expandedBy(southMeters: Double, westMeters: Double, northMeters: Double, eastMeters: Double) throws -&gt; GeoBox</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>southMeters</em>
</code>
</td>
<td>
<div>
<p>Distance in the south direction in meters to expand the <code>GeoBox</code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>westMeters</em>
</code>
</td>
<td>
<div>
<p>Distance in the west direction in meters to expand the <code>GeoBox</code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>northMeters</em>
</code>
</td>
<td>
<div>
<p>Distance in the north direction in meters to expand the <code>GeoBox</code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>eastMeters</em>
</code>
</td>
<td>
<div>
<p>Distance in the east direction in meters to expand the <code>GeoBox</code>.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The expanded <code>GeoBox</code>.</p>
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



</div>
`
}</HTMLBlock>

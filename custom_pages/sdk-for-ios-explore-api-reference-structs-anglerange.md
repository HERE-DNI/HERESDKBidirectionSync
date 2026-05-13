---
title: "AngleRange Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-anglerange"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- AngleRange.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/AngleRange"></a>
<a title="AngleRange Structure Reference"></a>
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
        AngleRange Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct AngleRange : Hashable</code></pre>
</div>
</div>
<p>Represents angle ranges as a circular sector by using an absolute start angle
and a relative range angle called extent. They both define a sector on a
circle. All angles are in degrees and are clockwise-oriented.
By default, the AngleRange represents the entire circle, the value is in the range of [0, 360].
Values will be corrected during construction using normalization
for the start angle and clamping for the extent angle, ensuring a valid range
for all possible inputs.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10AngleRangeV5startSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/start"></a>
<a class="token" href="#/s:7heresdk10AngleRangeV5startSdvp">start</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Start angle, running clockwise, in degrees from north.
The value is in the range of [0, 360) degrees.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let start: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10AngleRangeV6extentSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/extent"></a>
<a class="token" href="#/s:7heresdk10AngleRangeV6extentSdvp">extent</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The angle range extent, running clockwise, in degrees from start.
The value is in the range of [0, 360] degrees.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let extent: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10AngleRangeV5start6extentACSd_Sdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(start:extent:)"></a>
<a class="token" href="#/s:7heresdk10AngleRangeV5start6extentACSd_Sdtcfc">init(start:<wbr/>extent:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs an AngleRange from the provided start and extent angles.
Corrects values if they exceed the ranges.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(start: Double, extent: Double)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>start</em>
</code>
</td>
<td>
<div>
<p>Start angle, running clockwise, in degrees from north.
The value will be normalized to [0.0, 360.0).</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>extent</em>
</code>
</td>
<td>
<div>
<p>The range’s extent, running clockwise, in degrees from start.
The value will be clamped to the range of [0, 360] degrees.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10AngleRangeVACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk10AngleRangeVACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a range covering a full circle.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init()</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10AngleRangeV26fromMinMaxDegreesClockwise3min3maxACSd_SdtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fromMinMaxDegreesClockwise(min:max:)"></a>
<a class="token" href="#/s:7heresdk10AngleRangeV26fromMinMaxDegreesClockwise3min3maxACSd_SdtFZ">fromMinMaxDegreesClockwise(min:<wbr/>max:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs an AngleRange from the provided minimum and maximum angles.
Corrects values if they exceed the ranges. The angles are always
interpreted in clockwise orientation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static func fromMinMaxDegreesClockwise(min: Double, max: Double) -&gt; AngleRange</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>min</em>
</code>
</td>
<td>
<div>
<p>Angle where to start the circular sector, running clockwise, in
degrees from north.
The value will be normalized to [0.0, 360.0).</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>max</em>
</code>
</td>
<td>
<div>
<p>Angle where the circular sector ends, running clockwise, in
degrees from north.
The value will be normalized to [0.0, 360.0).</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Created AngleRange from the provided minimum and maximum angles.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10AngleRangeV29fromDirectionDegreesClockwise6center6extentACSd_SdtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fromDirectionDegreesClockwise(center:extent:)"></a>
<a class="token" href="#/s:7heresdk10AngleRangeV29fromDirectionDegreesClockwise6center6extentACSd_SdtFZ">fromDirectionDegreesClockwise(center:<wbr/>extent:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs an AngleRange from the provided center angle defining the
direction and an angular width to extent the range by 50% clockwise and
50% counter-clockwise from its center angle.
Corrects values if they exceed the ranges.
Example: direction = 90, extent = 10 means the circle sector is pointing
east, with an extent of 5 degrees north-wards and 5 degrees south-wards.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static func fromDirectionDegreesClockwise(center: Double, extent: Double) -&gt; AngleRange</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>center</em>
</code>
</td>
<td>
<div>
<p>Start angle, running clockwise, in degrees from north.
The value will be normalized to [0.0, 360.0).</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>extent</em>
</code>
</td>
<td>
<div>
<p>The range’s extent, running clockwise, in degrees from start.
The value will be clamped to the range of [0, 360] degrees.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Created AngleRange from the provided center angle and the range’s extent.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10AngleRangeV02inC032angleClockwiseInDegreesFromNorthSbSd_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/inRange(angleClockwiseInDegreesFromNorth:)"></a>
<a class="token" href="#/s:7heresdk10AngleRangeV02inC032angleClockwiseInDegreesFromNorthSbSd_tF">inRange(angleClockwiseInDegreesFromNorth:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Check if a given angle in degrees, clockwise from north is in range or not.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func inRange(angleClockwiseInDegreesFromNorth: Double) -&gt; Bool</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>angleClockwiseInDegreesFromNorth</em>
</code>
</td>
<td>
<div>
<p>An angle in degrees from north. Will be normalized before testing.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code>True</code>, if an angle is in range, <code>false</code> otherwise.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10AngleRangeV09closestInC0014angleClockwiseE16DegreesFromNorthS2d_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/closestInRange(angleClockwiseInDegreesFromNorth:)"></a>
<a class="token" href="#/s:7heresdk10AngleRangeV09closestInC0014angleClockwiseE16DegreesFromNorthS2d_tF">closestInRange(angleClockwiseInDegreesFromNorth:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Get the angle that is closest to the given one and in range. If the
angle to both ends of the range is the same, the value in the clockwise
direction is returned. If the given angle is in range already,
it will be returned as normalized angle.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func closestInRange(angleClockwiseInDegreesFromNorth: Double) -&gt; Double</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>angleClockwiseInDegreesFromNorth</em>
</code>
</td>
<td>
<div>
<p>An angle in degrees from north. Will be normalized.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The closest, normalized in-range angle in degrees, clockwise from north.
If the given angle is in range already, the given angle will be returned as
normalized angle in degree, clockwise from north.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10AngleRangeV3maxSdyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/max()"></a>
<a class="token" href="#/s:7heresdk10AngleRangeV3maxSdyF">max()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Get the maximum angle defined by the range in degrees, clockwise from north,
normalized to [0,360).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func max() -&gt; Double</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Maximum angle of the range in degrees, clockwise from north, normalized to
[0,360).</p>
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

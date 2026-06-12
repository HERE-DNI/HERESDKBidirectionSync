---
title: "GeoCoordinates"
slug: "sdk-for-ios-explore-api-reference-structs-geocoordinates"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoCoordinates"></a>
<a title="GeoCoordinates Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-core">Core</a>

        GeoCoordinates Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>GeoCoordinates</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">GeoCoordinates</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents geographical coordinates in 3D space.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14GeoCoordinatesV8latitudeSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/latitude"></a>
<a class="token" href="#/s:7heresdk14GeoCoordinatesV8latitudeSdvp">latitude</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Latitude in degrees.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">latitude</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14GeoCoordinatesV9longitudeSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/longitude"></a>
<a class="token" href="#/s:7heresdk14GeoCoordinatesV9longitudeSdvp">longitude</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Longitude in degrees.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">longitude</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14GeoCoordinatesV8altitudeSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/altitude"></a>
<a class="token" href="#/s:7heresdk14GeoCoordinatesV8altitudeSdSgvp">altitude</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional altitude in meters.
By convention, on iOS devices, altitude is set as meters relative to the
mean sea level.
On Android devices, altitude is set as meters relative to the WGS 84
reference ellipsoid.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">altitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14GeoCoordinatesV8latitude9longitude8altitudeACSd_S2dtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(latitude:longitude:altitude:)"></a>
<a class="token" href="#/s:7heresdk14GeoCoordinatesV8latitude9longitude8altitudeACSd_S2dtcfc">init(latitude:<wbr/>longitude:<wbr/>altitude:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a GeoCoordinates from the provided latitude, longitude and altitude values.
Corrects values of lat and long if they exceed the ranges.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">latitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">longitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">altitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>latitude</em>
</code>
</td>
<td>
<div>
<p>Latitude in degrees. Positive value means Northern hemisphere.
If the value is out of range of [-90.0, 90.0] it’s clamped to that range.
NaN value is converted to 0.0.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>longitude</em>
</code>
</td>
<td>
<div>
<p>Longitude in degrees. Positive value means Eastern hemisphere.
If the value is out of range of [-180.0, 180.0] it’s replaced with a value
within the range, representing effectively the same meridian.
NaN value is converted to 0.0.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>altitude</em>
</code>
</td>
<td>
<div>
<p>Altitude in meters. NaN value is converted to <code>nil</code>.</p>
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
<a name="/s:7heresdk14GeoCoordinatesV8latitude9longitudeACSd_Sdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(latitude:longitude:)"></a>
<a class="token" href="#/s:7heresdk14GeoCoordinatesV8latitude9longitudeACSd_Sdtcfc">init(latitude:<wbr/>longitude:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a GeoCoordinates from the provided latitude and longitude values.
Corrects values of latitude and longitude if they exceed the ranges.
Altitude set to <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">latitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">longitude</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>latitude</em>
</code>
</td>
<td>
<div>
<p>Latitude in degrees. Positive value means Northern hemisphere.
If the value is out of range of [-90.0, 90.0] it’s clamped to that range.
NaN value is converted to 0.0.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>longitude</em>
</code>
</td>
<td>
<div>
<p>Longitude in degrees. Positive value means Eastern hemisphere.
If the value is out of range of [-180.0, 180.0] it’s replaced with a value
within the range, representing effectively the same meridian.
NaN value is converted to 0.0.</p>
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
<a name="/s:7heresdk14GeoCoordinatesV8distance2toSdAC_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/distance(to:)"></a>
<a class="token" href="#/s:7heresdk14GeoCoordinatesV8distance2toSdAC_tF">distance(to:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Computes distance (in meters) along the great circle between two coordinates.
This method ignores altitude of both points.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">distance</span><span class="p">(</span><span class="n">to</span> <span class="nv">point</span><span class="p">:</span> <span class="kt">GeoCoordinates</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Double</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>point</em>
</code>
</td>
<td>
<div>
<p>Coordinates of the point to which the distance is computed.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>distance in meters.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14GeoCoordinatesV11interpolate6toward2byA2C_SdtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/interpolate(toward:by:)"></a>
<a class="token" href="#/s:7heresdk14GeoCoordinatesV11interpolate6toward2byA2C_SdtF">interpolate(toward:<wbr/>by:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Computes the coordinates of the interpolated location along the great circle between
the two coordinates.</p>
<p>The interpolation factor is clamped to the range <code>[0.0, 1.0]</code> where <code>0.0</code> identifies this
<code>GeoCoordinates</code> and <code>1.0</code> indicates the other coordinates.</p>
<p>The ratio between the distance to the interpolated coordinates and the distance to the other
coordinates is approximately equal to the interpolation factor. When both coordinates have
the altitude, then the altitude is interpolated as well; <code>nil</code> otherwise.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">interpolate</span><span class="p">(</span><span class="n">toward</span> <span class="nv">towardCoords</span><span class="p">:</span> <span class="kt">GeoCoordinates</span><span class="p">,</span> <span class="n">by</span> <span class="nv">factor</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">GeoCoordinates</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>towardCoords</em>
</code>
</td>
<td>
<div>
<p>Coordinates of the point to which the interpolation is directed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>factor</em>
</code>
</td>
<td>
<div>
<p>The interpolation factor</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>interpolated coordinates</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14GeoCoordinatesV10fromString5inputACSgSS_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fromString(input:)"></a>
<a class="token" href="#/s:7heresdk14GeoCoordinatesV10fromString5inputACSgSS_tFZ">fromString(input:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs GeoCoordinates from the provided string in specified format.
Corrects values of lat and long if they exceed the ranges.
If the latitude value is out of range of [-90.0, 90.0] it’s clamped to that range.
If the longitude value is out of range of [-180.0, 180.0] it’s replaced with a value
within the range, representing effectively the same meridian.
Examples: <code>53.43762,-13.65468</code>.
<code>49°59'56.948"N, 15°48'22.989"E</code>
<code>50d4m17.698N 14d24m2.826E</code>
<code>49.9991522N, 150.8063858E</code>
<code>40°26′47″N 79°58′36″W</code></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">fromString</span><span class="p">(</span><span class="nv">input</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">GeoCoordinates</span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>input</em>
</code>
</td>
<td>
<div>
<p>String representing GeoCoordinates in one of supported formats.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Created GeoCoordinates, or ‘null’ if string was not in appropriate format.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14GeoCoordinatesV2eeoiySbAC_ACtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/==(_:_:)"></a>
<a class="token" href="#/s:7heresdk14GeoCoordinatesV2eeoiySbAC_ACtFZ">==(_:<wbr/>_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">static</span> <span class="kd">func</span> <span class="o">==</span> <span class="p">(</span><span class="nv">lhs</span><span class="p">:</span> <span class="kt">GeoCoordinates</span><span class="p">,</span> <span class="nv">rhs</span><span class="p">:</span> <span class="kt">GeoCoordinates</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
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
} </HTMLBlock>

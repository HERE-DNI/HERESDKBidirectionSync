---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-mapcameralimits"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapCameraLimits.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapCameraLimits"></a>
<a title="MapCameraLimits Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapCameraLimits Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapCameraLimits</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapCameraLimits</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraLimits</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraLimits</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Controls constraints on map camera parameters.</p>
<p>When constraints are set, they are enforced for current camera state
and for all future changes to the camera.</p>
<p>When setting, limits are applied on next rendering loop.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapCameraLimitsC7minTiltSdvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/minTilt"></a>
<a class="token" href="#/s:7heresdk15MapCameraLimitsC7minTiltSdvpZ">minTilt</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Absolute minimum possible value of tilt angle.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">minTilt</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapCameraLimitsC7maxTiltSdvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/maxTilt"></a>
<a class="token" href="#/s:7heresdk15MapCameraLimitsC7maxTiltSdvpZ">maxTilt</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Absolute maximum possible value of tilt angle.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">maxTilt</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapCameraLimitsC12minZoomLevelSdvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/minZoomLevel"></a>
<a class="token" href="#/s:7heresdk15MapCameraLimitsC12minZoomLevelSdvpZ">minZoomLevel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Absolute minimum possible value of zoom level.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">minZoomLevel</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapCameraLimitsC12maxZoomLevelSdvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/maxZoomLevel"></a>
<a class="token" href="#/s:7heresdk15MapCameraLimitsC12maxZoomLevelSdvpZ">maxZoomLevel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Absolute maximum possible value of zoom level.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">maxZoomLevel</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapCameraLimitsC9tiltRangeAA05AngleF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tiltRange"></a>
<a class="token" href="#/s:7heresdk15MapCameraLimitsC9tiltRangeAA05AngleF0Vvp">tiltRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The tilt range that can be applied to the camera.
The supported values fall inside <code><a href="../Classes/MapCameraLimits.html#/s:7heresdk15MapCameraLimitsC7minTiltSdvpZ">code&gt;</a></code> range.
Setting values outside the supported range will be ignored.</p>
<p>By default, a <code><a href="../Classes/MapCameraLimits.html#/s:7heresdk15MapCameraLimitsC7minTiltSdvpZ">code&gt;</a></code> tilt range is set during initialization.</p>
<p>If the current camera tilt exceeds the new limit range, it will immediately be set to minimum or maximum,
depending on which is closest.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tiltRange</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-anglerange">AngleRange</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapCameraLimitsC12bearingRangeAA05AngleF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/bearingRange"></a>
<a class="token" href="#/s:7heresdk15MapCameraLimitsC12bearingRangeAA05AngleF0Vvp">bearingRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The bearing range within which the camera can be rotated.
If the current camera bearing exceeds the limit range, it will immediately be set to minimum or
maximum, depending on which is closest.</p>
<p>By default, a full circle is set during initialization.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">bearingRange</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-anglerange">AngleRange</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapCameraLimitsC9zoomRangeAA0b7MeasureF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/zoomRange"></a>
<a class="token" href="#/s:7heresdk15MapCameraLimitsC9zoomRangeAA0b7MeasureF0Vvp">zoomRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The zoom range that can be applied to the camera.
The supported values fall inside <code><a href="../Classes/MapCameraLimits.html#/s:7heresdk15MapCameraLimitsC12minZoomLevelSdvpZ">code&gt;</a></code> range.
Values outside the supported zoom range are ignored.</p>
<p>By default, a <code><a href="../Classes/MapCameraLimits.html#/s:7heresdk15MapCameraLimitsC12minZoomLevelSdvpZ">code&gt;</a></code> zoom range is set during initialization.</p>
<p>If the current camera zoom exceeds the limit range, it will immediately be set to minimum or maximum, depending on which is closest.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">zoomRange</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasurerange">MapMeasureRange</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapCameraLimitsC10targetAreaAA6GeoBoxVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/targetArea"></a>
<a class="token" href="#/s:7heresdk15MapCameraLimitsC10targetAreaAA6GeoBoxVSgvp">targetArea</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geographical area to which the camera target is limited.
Absence of a value means that there is no limit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">targetArea</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geobox">GeoBox</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapCameraLimitsC21setBearingRangeAtZoom_07bearingG0yAA0B7MeasureV_AA05AngleG0VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setBearingRangeAtZoom(_:bearingRange:)"></a>
<a class="token" href="#/s:7heresdk15MapCameraLimitsC21setBearingRangeAtZoom_07bearingG0yAA0B7MeasureV_AA05AngleG0VtF">setBearingRangeAtZoom(_:<wbr/>bearingRange:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the bearing range within which the camera can rotate at a given zoom.</p>
<p>The resulting camera bearing at a zoom is an interpolated value of the ranges set for closest matching zoom values.
When no bearing range is specified for <code><a href="../Classes/MapCameraLimits.html#/s:7heresdk15MapCameraLimitsC12minZoomLevelSdvpZ">MapCameraLimits.minZoomLevel</a></code>, the bearing range set through
<code><a href="../Classes/MapCameraLimits.html#/s:7heresdk15MapCameraLimitsC12bearingRangeAA05AngleF0Vvp">MapCameraLimits.bearingRange</a></code> is used for interpolation.</p>
<p>Zoom values outside the supported zoom range are ignored.
By default, the maximum bearing range for all zoom values is set during initialization.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setBearingRangeAtZoom</span><span class="p">(</span><span class="n">_</span> <span class="nv">zoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasure">MapMeasure</a></span><span class="p">,</span> <span class="nv">bearingRange</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-anglerange">AngleRange</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>zoom</em>
</code>
</td>
<td>
<div>
<p>Zoom at which the range is set.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>bearingRange</em>
</code>
</td>
<td>
<div>
<p>Bearing range.</p>
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
<a name="/s:7heresdk15MapCameraLimitsC18clearBearingRangesyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/clearBearingRanges()"></a>
<a class="token" href="#/s:7heresdk15MapCameraLimitsC18clearBearingRangesyyF">clearBearingRanges()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Clears bearing ranges for all zoom values and resets <code><a href="../Classes/MapCameraLimits.html#/s:7heresdk15MapCameraLimitsC12bearingRangeAA05AngleF0Vvp">MapCameraLimits.bearingRange</a></code>
to default.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">clearBearingRanges</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapCameraLimitsC18setTiltRangeAtZoom_04tiltG0yAA0B7MeasureV_AA05AngleG0VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setTiltRangeAtZoom(_:tiltRange:)"></a>
<a class="token" href="#/s:7heresdk15MapCameraLimitsC18setTiltRangeAtZoom_04tiltG0yAA0B7MeasureV_AA05AngleG0VtF">setTiltRangeAtZoom(_:<wbr/>tiltRange:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets tilt ranges that can be set on the camera at given zoom.</p>
<p>The resulting camera tilt at a zoom is an interpolated value of the ranges set for closest matching zoom values.
When no tilt range is specified for <code><a href="../Classes/MapCameraLimits.html#/s:7heresdk15MapCameraLimitsC12minZoomLevelSdvpZ">MapCameraLimits.minZoomLevel</a></code>, the tilt range set through <code><a href="../Classes/MapCameraLimits.html#/s:7heresdk15MapCameraLimitsC9tiltRangeAA05AngleF0Vvp">MapCameraLimits.tiltRange</a></code> is used for interpolation.</p>
<p>Zoom or tilt values outside the supported zoom and tilt range are ignored.
By default, the maximum tilt range for all zoom values is set during initialization.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setTiltRangeAtZoom</span><span class="p">(</span><span class="n">_</span> <span class="nv">zoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmeasure">MapMeasure</a></span><span class="p">,</span> <span class="nv">tiltRange</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-anglerange">AngleRange</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>zoom</em>
</code>
</td>
<td>
<div>
<p>Zoom at which the range is set.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>tiltRange</em>
</code>
</td>
<td>
<div>
<p>Tilt range.</p>
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
<a name="/s:7heresdk15MapCameraLimitsC15clearTiltRangesyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/clearTiltRanges()"></a>
<a class="token" href="#/s:7heresdk15MapCameraLimitsC15clearTiltRangesyyF">clearTiltRanges()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Clears tilt ranges for all zoom values and resets <code><a href="../Classes/MapCameraLimits.html#/s:7heresdk15MapCameraLimitsC9tiltRangeAA05AngleF0Vvp">MapCameraLimits.tiltRange</a></code>  to default.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">clearTiltRanges</span><span class="p">()</span></code></pre>
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

</div>
`
}</HTMLBlock>

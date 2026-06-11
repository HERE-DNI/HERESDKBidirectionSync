---
title: "Calculation"
slug: "sdk-for-ios-navigate-api-reference-structs-isolineoptions-calculation"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Calculation"></a>
<a title="Calculation Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

<a href="sdk-for-ios-navigate-api-reference-structs-isolineoptions">IsolineOptions</a>

        Calculation Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Calculation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Calculation</span></code></pre>
</div>
</div>
<p>Specifies isoline parameters.
Setting at least one limit to <code><a href="../../Structs/IsolineOptions/Calculation.html#/s:7heresdk14IsolineOptionsV11CalculationV11rangeValuesSays5Int32VGvp">IsolineOptions.Calculation.rangeValues</a></code> is mandatory or the calculation will fail.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV11CalculationV9rangeTypeAA0b5RangeF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/rangeType"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV11CalculationV9rangeTypeAA0b5RangeF0Ovp">rangeType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the range of values to be included in the isoline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">rangeType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-isolinerangetype">IsolineRangeType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV11CalculationV11rangeValuesSays5Int32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/rangeValues"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV11CalculationV11rangeValuesSays5Int32VGvp">rangeValues</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A list of ranges. The unit is defined by the type parameter.
Each range defines the maximum allowed value to reach a destination.
For each value an <code><a href="sdk-for-ios-navigate-api-reference-classes-isoline">Isoline</a></code> is calculated indicating the reachable area.
If empty, <code><a href="sdk-for-ios-navigate-api-reference-structs-isolineoptions">IsolineOptions</a></code> object is considered invalid.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">rangeValues</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV11CalculationV07isolineD4ModeAA0bdF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isolineCalculationMode"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV11CalculationV07isolineD4ModeAA0bdF0Ovp">isolineCalculationMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies how isoline calculation is optimized.
The default waypoint type is <code><a href="../../Enums/IsolineCalculationMode.html#/s:7heresdk22IsolineCalculationModeO8balancedyA2CmF">IsolineCalculationMode.balanced</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isolineCalculationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-isolinecalculationmode">IsolineCalculationMode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV11CalculationV9maxPointss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxPoints"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV11CalculationV9maxPointss5Int32VSgvp">maxPoints</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Limits the number of points in the resulting isoline polygon. If the
isoline consists of multiple polygons, the sum of points from all
polygons is considered. Note that this parameter does not affect the calculation,
but the shape of the polygon. Look at <code><a href="sdk-for-ios-navigate-api-reference-enums-isolinecalculationmode">IsolineCalculationMode</a></code> parameter
to optimize performance.
A higher value will result in a more accurate polygon shape. Rendering a polygon
with a high number of points can negatively impact rendering performance.
The minimum allowed value is 30, lower values will be ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxPoints</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV11CalculationV16isolineDirectionAA010RoutePlaceF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isolineDirection"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV11CalculationV16isolineDirectionAA010RoutePlaceF0Ovp">isolineDirection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies if calculations will be from or to a specific point.
The default isoline direction is <code><a href="../../Enums/RoutePlaceDirection.html#/s:7heresdk19RoutePlaceDirectionO9departureyA2CmF">RoutePlaceDirection.departure</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isolineDirection</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-routeplacedirection">RoutePlaceDirection</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV11CalculationV9rangeType0E6ValuesAeA0b5RangeF0O_Says5Int32VGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(rangeType:rangeValues:)"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV11CalculationV9rangeType0E6ValuesAeA0b5RangeF0O_Says5Int32VGtcfc">init(rangeType:<wbr/>rangeValues:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">rangeType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-isolinerangetype">IsolineRangeType</a></span><span class="p">,</span> <span class="nv">rangeValues</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>rangeType</em>
</code>
</td>
<td>
<div>
<p>The range type.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>rangeValues</em>
</code>
</td>
<td>
<div>
<p>Range values.</p>
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
<a name="/s:7heresdk14IsolineOptionsV11CalculationV9rangeType0E6Values16isolineDirectionAeA0b5RangeF0O_Says5Int32VGAA010RoutePlaceI0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(rangeType:rangeValues:isolineDirection:)"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV11CalculationV9rangeType0E6Values16isolineDirectionAeA0b5RangeF0O_Says5Int32VGAA010RoutePlaceI0Otcfc">init(rangeType:<wbr/>rangeValues:<wbr/>isolineDirection:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">rangeType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-isolinerangetype">IsolineRangeType</a></span><span class="p">,</span> <span class="nv">rangeValues</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">],</span> <span class="nv">isolineDirection</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-routeplacedirection">RoutePlaceDirection</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>rangeType</em>
</code>
</td>
<td>
<div>
<p>The range type.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>rangeValues</em>
</code>
</td>
<td>
<div>
<p>Range values.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>isolineDirection</em>
</code>
</td>
<td>
<div>
<p>The isoline direction.</p>
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
<a name="/s:7heresdk14IsolineOptionsV11CalculationV9rangeType0E6Values07isolineD4ModeAeA0b5RangeF0O_Says5Int32VGAA0bdI0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(rangeType:rangeValues:isolineCalculationMode:)"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV11CalculationV9rangeType0E6Values07isolineD4ModeAeA0b5RangeF0O_Says5Int32VGAA0bdI0Otcfc">init(rangeType:<wbr/>rangeValues:<wbr/>isolineCalculationMode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">rangeType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-isolinerangetype">IsolineRangeType</a></span><span class="p">,</span> <span class="nv">rangeValues</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">],</span> <span class="nv">isolineCalculationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-isolinecalculationmode">IsolineCalculationMode</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>rangeType</em>
</code>
</td>
<td>
<div>
<p>The range type.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>rangeValues</em>
</code>
</td>
<td>
<div>
<p>Range values.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>isolineCalculationMode</em>
</code>
</td>
<td>
<div>
<p>The isoline calculation mode.</p>
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
<a name="/s:7heresdk14IsolineOptionsV11CalculationV9rangeType0E6Values07isolineD4Mode9maxPoints0H9DirectionAeA0b5RangeF0O_Says5Int32VGAA0bdI0OANSgAA010RoutePlaceL0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(rangeType:rangeValues:isolineCalculationMode:maxPoints:isolineDirection:)"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV11CalculationV9rangeType0E6Values07isolineD4Mode9maxPoints0H9DirectionAeA0b5RangeF0O_Says5Int32VGAA0bdI0OANSgAA010RoutePlaceL0Otcfc">init(rangeType:<wbr/>rangeValues:<wbr/>isolineCalculationMode:<wbr/>maxPoints:<wbr/>isolineDirection:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">rangeType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-isolinerangetype">IsolineRangeType</a></span><span class="p">,</span> <span class="nv">rangeValues</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">],</span> <span class="nv">isolineCalculationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-isolinecalculationmode">IsolineCalculationMode</a></span><span class="p">,</span> <span class="nv">maxPoints</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?,</span> <span class="nv">isolineDirection</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-routeplacedirection">RoutePlaceDirection</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>rangeType</em>
</code>
</td>
<td>
<div>
<p>The range type.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>rangeValues</em>
</code>
</td>
<td>
<div>
<p>Range values.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>isolineCalculationMode</em>
</code>
</td>
<td>
<div>
<p>The isoline calculation mode.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>maxPoints</em>
</code>
</td>
<td>
<div>
<p>The max points number.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>isolineDirection</em>
</code>
</td>
<td>
<div>
<p>The isoline direction.</p>
</div>
</td>
</tr>
</tbody>
</table>
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

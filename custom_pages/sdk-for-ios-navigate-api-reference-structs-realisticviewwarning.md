---
title: "RealisticViewWarning"
slug: "sdk-for-ios-navigate-api-reference-structs-realisticviewwarning"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RealisticViewWarning"></a>
<a title="RealisticViewWarning Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        RealisticViewWarning Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RealisticViewWarning</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RealisticViewWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A realistic view notification. This notification is given for complex junctions and it includes a visual
representation of that junction, in order to help the user to better navigate it. When
<code><a href="../Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV12distanceTypeAA08DistanceF0Ovp">RealisticViewWarning.distanceType</a></code> is <code><a href="../Enums/DistanceType.html#/s:7heresdk12DistanceTypeO5aheadyA2CmF">DistanceType.ahead</a></code>, the <code><a href="../Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">RealisticViewWarning.realisticViewVectorImage</a></code> object
will be provided with the junction view and the signpost representations. For <code><a href="../Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV12distanceTypeAA08DistanceF0Ovp">RealisticViewWarning.distanceType</a></code>
with value <code><a href="../Enums/DistanceType.html#/s:7heresdk12DistanceTypeO6passedyA2CmF">DistanceType.passed</a></code>, the <code><a href="../Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">RealisticViewWarning.realisticViewVectorImage</a></code> object will be null.
Use <code>RealisticViewWarningListener</code> to get notifications about the realistic views of the upcoming junctions.</p>
<p>Realistic view notifications require an online connection in order to function properly, or that the
junction or signpost map layer data is cached, installed or preloaded as part of a <code><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></code>.
This can be enabled via feature configurations.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RealisticViewWarningV2ids5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk20RealisticViewWarningV2ids5Int32Vvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unique identifier for this specific realistic view warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RealisticViewWarningV010distanceTobC8InMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceToRealisticViewInMeters"></a>
<a class="token" href="#/s:7heresdk20RealisticViewWarningV010distanceTobC8InMetersSdvp">distanceToRealisticViewInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance to the junction, for which the realistic view is given, expressed in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceToRealisticViewInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/realisticViewVectorImage"></a>
<a class="token" href="#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">realisticViewVectorImage</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The realistic view object for which the warning is given.
Image resources are stored as vector graphics.
Within <code>RealisticViewWarning</code>, only one type of image, either raster or vector, will be provided.
If this property is not <code>nil</code>, then <code><a href="../Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV09realisticC11RasterImageAA0bcfG0VSgvp">RealisticViewWarning.realisticViewRasterImage</a></code> will be <code>nil</code>.</p>
<p><strong>Note:</strong> The realistic views for most of the countries are stored as vector images.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">realisticViewVectorImage</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-realisticviewvectorimage">RealisticViewVectorImage</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RealisticViewWarningV09realisticC11RasterImageAA0bcfG0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/realisticViewRasterImage"></a>
<a class="token" href="#/s:7heresdk20RealisticViewWarningV09realisticC11RasterImageAA0bcfG0VSgvp">realisticViewRasterImage</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The realistic view object for which the warning is given.
Image resources are stored as raster graphics.
Within <code>RealisticViewWarning</code>, only one type of image, either raster or vector, will be provided.
If this property is not <code>nil</code>, then <code><a href="../Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">RealisticViewWarning.realisticViewVectorImage</a></code> will be <code>nil</code>.
<strong>Note:</strong> Certain countries support only raster images as realistic views. Currently, this is the case
only for Japan, but in the future, more countries might support this type of realistic views.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">realisticViewRasterImage</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-realisticviewrasterimage">RealisticViewRasterImage</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RealisticViewWarningV12distanceTypeAA08DistanceF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceType"></a>
<a class="token" href="#/s:7heresdk20RealisticViewWarningV12distanceTypeAA08DistanceF0Ovp">distanceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance type for the warning, e.g. a warning for a new realistic view ahead or a warning
for passing a realistic view. Since the realistic view warning is given relative to a single
position on the route, <code><a href="../Enums/DistanceType.html#/s:7heresdk12DistanceTypeO7reachedyA2CmF">DistanceType.reached</a></code> will never be given for this warning.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RealisticViewWarningV2id010distanceTobC8InMeters09realisticC11VectorImage0jc6RasterL00F4TypeACs5Int32V_SdAA0bckL0VSgAA0bcmL0VSgAA08DistanceN0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:distanceToRealisticViewInMeters:realisticViewVectorImage:realisticViewRasterImage:distanceType:)"></a>
<a class="token" href="#/s:7heresdk20RealisticViewWarningV2id010distanceTobC8InMeters09realisticC11VectorImage0jc6RasterL00F4TypeACs5Int32V_SdAA0bckL0VSgAA0bcmL0VSgAA08DistanceN0Otcfc">init(id:<wbr/>distanceToRealisticViewInMeters:<wbr/>realisticViewVectorImage:<wbr/>realisticViewRasterImage:<wbr/>distanceType:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>id: Unique identifier for this specific realistic view warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.</li>
<li>distanceToRealisticViewInMeters: Distance to the junction, for which the realistic view is given, expressed in meters.</li>
<li>realisticViewVectorImage: The realistic view object for which the warning is given.
Image resources are stored as vector graphics.
Within <code>RealisticViewWarning</code>, only one type of image, either raster or vector, will be provided.
If this property is not <code>nil</code>, then <code><a href="../Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV09realisticC11RasterImageAA0bcfG0VSgvp">RealisticViewWarning.realisticViewRasterImage</a></code> will be <code>nil</code>.</li>
</ul>
<p><strong>Note:</strong> The realistic views for most of the countries are stored as vector images.</p>
<ul>
<li>realisticViewRasterImage: The realistic view object for which the warning is given.
Image resources are stored as raster graphics.
Within <code>RealisticViewWarning</code>, only one type of image, either raster or vector, will be provided.
If this property is not <code>nil</code>, then <code><a href="../Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">RealisticViewWarning.realisticViewVectorImage</a></code> will be <code>nil</code>.
<strong>Note:</strong> Certain countries support only raster images as realistic views. Currently, this is the case
only for Japan, but in the future, more countries might support this type of realistic views.</li>
<li>distanceType: The distance type for the warning, e.g. a warning for a new realistic view ahead or a warning
for passing a realistic view. Since the realistic view warning is given relative to a single
position on the route, <code><a href="../Enums/DistanceType.html#/s:7heresdk12DistanceTypeO7reachedyA2CmF">DistanceType.reached</a></code> will never be given for this warning.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">distanceToRealisticViewInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">realisticViewVectorImage</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-realisticviewvectorimage">RealisticViewVectorImage</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">realisticViewRasterImage</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-realisticviewrasterimage">RealisticViewRasterImage</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span><span class="p">)</span></code></pre>
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
}</HTMLBlock>

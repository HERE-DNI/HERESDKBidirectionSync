---
title: "RealisticViewWarningOptions"
slug: "sdk-for-ios-navigate-structs-realisticviewwarningoptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RealisticViewWarningOptions"></a>
<a title="RealisticViewWarningOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-navigation">Navigation</a>

        RealisticViewWarningOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RealisticViewWarningOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RealisticViewWarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Realistic view warning options. Set the options for filtering the realistic view notifications and
setting the realistic view notification distances based on the road type.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27RealisticViewWarningOptionsV11aspectRatioAA06AspectG0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/aspectRatio"></a>
<a class="token" href="#/s:7heresdk27RealisticViewWarningOptionsV11aspectRatioAA06AspectG0Ovp">aspectRatio</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The aspect ratio of the images which will be given in the realistic view warning. This option is applicable only
to the <code><a href="../Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">RealisticViewWarning.realisticViewVectorImage</a></code>. For <code><a href="../Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV09realisticC11RasterImageAA0bcfG0VSgvp">RealisticViewWarning.realisticViewRasterImage</a></code>
the aspect ratio is always portrait.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">aspectRatio</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-aspectratio">AspectRatio</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27RealisticViewWarningOptionsV9darkThemeSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/darkTheme"></a>
<a class="token" href="#/s:7heresdk27RealisticViewWarningOptionsV9darkThemeSbvp">darkTheme</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies whether the images included in the realistic view warning will be optimized for the light or dark color
scheme. This option is applicable only to the <code><a href="../Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">RealisticViewWarning.realisticViewVectorImage</a></code>. For
<code><a href="../Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV09realisticC11RasterImageAA0bcfG0VSgvp">RealisticViewWarning.realisticViewRasterImage</a></code> the dark theme is always <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">darkTheme</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27RealisticViewWarningOptionsV11aspectRatio9darkThemeAcA06AspectG0O_Sbtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(aspectRatio:darkTheme:)"></a>
<a class="token" href="#/s:7heresdk27RealisticViewWarningOptionsV11aspectRatio9darkThemeAcA06AspectG0O_Sbtcfc">init(aspectRatio:<wbr/>darkTheme:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">aspectRatio</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-aspectratio">AspectRatio</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-aspectratio">AspectRatio</a></span><span class="o">.</span><span class="n">aspectRatio3X4</span><span class="p">,</span> <span class="nv">darkTheme</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
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

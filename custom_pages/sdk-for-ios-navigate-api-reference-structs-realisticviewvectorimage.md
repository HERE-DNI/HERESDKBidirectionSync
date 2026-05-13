---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-structs-realisticviewvectorimage"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- RealisticViewVectorImage.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RealisticViewVectorImage"></a>
<a title="RealisticViewVectorImage Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        RealisticViewVectorImage Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RealisticViewVectorImage</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RealisticViewVectorImage</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A realistic view of a junction. The fields describing the realistic view are
<code><a href="../Structs/RealisticViewVectorImage.html#/s:7heresdk24RealisticViewVectorImageV08junctionc3SvgE7ContentSSvp">RealisticViewVectorImage.junctionViewSvgImageContent</a></code> contains a SVG image of the junction view
represented as a string.
<code><a href="../Structs/RealisticViewVectorImage.html#/s:7heresdk24RealisticViewVectorImageV011signpostSvgE7ContentSSvp">RealisticViewVectorImage.signpostSvgImageContent</a></code> contains an SVG image of the signpost corresponding
to the junction, also represented as a string.
A valid realistic view contains a non-empty <code><a href="../Structs/RealisticViewVectorImage.html#/s:7heresdk24RealisticViewVectorImageV08junctionc3SvgE7ContentSSvp">RealisticViewVectorImage.junctionViewSvgImageContent</a></code> and a
non-empty <code><a href="../Structs/RealisticViewVectorImage.html#/s:7heresdk24RealisticViewVectorImageV011signpostSvgE7ContentSSvp">RealisticViewVectorImage.signpostSvgImageContent</a></code>.
Use <code>RealisticViewWarningListener</code> to get notifications with the realistic views of the upcoming junctions.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RealisticViewVectorImageV08junctionc3SvgE7ContentSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/junctionViewSvgImageContent"></a>
<a class="token" href="#/s:7heresdk24RealisticViewVectorImageV08junctionc3SvgE7ContentSSvp">junctionViewSvgImageContent</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The full content of the junction view vector image as a string.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">junctionViewSvgImageContent</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RealisticViewVectorImageV011signpostSvgE7ContentSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/signpostSvgImageContent"></a>
<a class="token" href="#/s:7heresdk24RealisticViewVectorImageV011signpostSvgE7ContentSSvp">signpostSvgImageContent</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The full content of the signpost vector image as a string.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">signpostSvgImageContent</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RealisticViewVectorImageV08junctionc3SvgE7Content08signpostgeH0ACSS_SStcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(junctionViewSvgImageContent:signpostSvgImageContent:)"></a>
<a class="token" href="#/s:7heresdk24RealisticViewVectorImageV08junctionc3SvgE7Content08signpostgeH0ACSS_SStcfc">init(junctionViewSvgImageContent:<wbr/>signpostSvgImageContent:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">junctionViewSvgImageContent</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">signpostSvgImageContent</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
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

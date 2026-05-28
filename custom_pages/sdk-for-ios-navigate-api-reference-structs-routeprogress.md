---
title: "Navigation / RouteProgress"
slug: "sdk-for-ios-navigate-api-reference-structs-routeprogress"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RouteProgress"></a>
<a title="RouteProgress Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        RouteProgress Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RouteProgress</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteProgress</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains all the relevant information on the user’s progress along a route.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RouteProgressV12sectionIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sectionIndex"></a>
<a class="token" href="#/s:7heresdk13RouteProgressV12sectionIndexs5Int32Vvp">sectionIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Index of the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-section">Section</a></code> in the route.
Note that this section index does not point to the current <code><a href="sdk-for-ios-navigate-api-reference-..-structs-sectionprogress">SectionProgress</a></code>
but to the route <code><a href="sdk-for-ios-navigate-api-reference-..-classes-section">Section</a></code> that you can access via <code>route</code>
and <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8sectionsSayAA7SectionCGvp">Route.sections</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.27.0. Use <code>RouteProgress.routeMatchedLocation</code> instead.")</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">sectionIndex</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RouteProgressV9spanIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/spanIndex"></a>
<a class="token" href="#/s:7heresdk13RouteProgressV9spanIndexs5Int32Vvp">spanIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Index of the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-span">Span</a></code> in the route section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.27.0. Use <code>RouteProgress.routeMatchedLocation</code> instead.")</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">spanIndex</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RouteProgressV07sectionC0SayAA07SectionC0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sectionProgress"></a>
<a class="token" href="#/s:7heresdk13RouteProgressV07sectionC0SayAA07SectionC0VGvp">sectionProgress</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The progress for each <code><a href="sdk-for-ios-navigate-api-reference-..-classes-section">Section</a></code> from the current one to the last one.
Note that the progress information is accumulated successively, therefore information relative
to the final destination is in the last item of the list. The list is guaranteed to be non-empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">sectionProgress</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-sectionprogress">SectionProgress</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RouteProgressV08maneuverC0SayAA08ManeuverC0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverProgress"></a>
<a class="token" href="#/s:7heresdk13RouteProgressV08maneuverC0SayAA08ManeuverC0VGvp">maneuverProgress</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The progress for next and next-next maneuvers (see <code><a href="sdk-for-ios-navigate-api-reference-..-classes-maneuver">Maneuver</a></code>). Note that the list
can contain at maximum two items (for next and next-next maneuvers) and one or zero when approaching the
destination.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maneuverProgress</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-maneuverprogress">ManeuverProgress</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RouteProgressV20routeMatchedLocationAA0beF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeMatchedLocation"></a>
<a class="token" href="#/s:7heresdk13RouteProgressV20routeMatchedLocationAA0beF0Vvp">routeMatchedLocation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route matched location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">routeMatchedLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-routematchedlocation">RouteMatchedLocation</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RouteProgressV07sectionC008maneuverC020routeMatchedLocationACSayAA07SectionC0VG_SayAA08ManeuverC0VGAA0bgH0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sectionProgress:maneuverProgress:routeMatchedLocation:)"></a>
<a class="token" href="#/s:7heresdk13RouteProgressV07sectionC008maneuverC020routeMatchedLocationACSayAA07SectionC0VG_SayAA08ManeuverC0VGAA0bgH0Vtcfc">init(sectionProgress:<wbr/>maneuverProgress:<wbr/>routeMatchedLocation:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sectionProgress</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-sectionprogress">SectionProgress</a></span><span class="p">],</span> <span class="nv">maneuverProgress</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-maneuverprogress">ManeuverProgress</a></span><span class="p">],</span> <span class="nv">routeMatchedLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-routematchedlocation">RouteMatchedLocation</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-routematchedlocation">RouteMatchedLocation</a></span><span class="p">())</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RouteProgressV12sectionIndex04spanE00dC008maneuverC020routeMatchedLocationACs5Int32V_AJSayAA07SectionC0VGSayAA08ManeuverC0VGAA0biJ0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sectionIndex:spanIndex:sectionProgress:maneuverProgress:routeMatchedLocation:)"></a>
<a class="token" href="#/s:7heresdk13RouteProgressV12sectionIndex04spanE00dC008maneuverC020routeMatchedLocationACs5Int32V_AJSayAA07SectionC0VGSayAA08ManeuverC0VGAA0biJ0Vtcfc">init(sectionIndex:<wbr/>spanIndex:<wbr/>sectionProgress:<wbr/>maneuverProgress:<wbr/>routeMatchedLocation:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated)</span>
<span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sectionIndex</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">spanIndex</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">sectionProgress</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-sectionprogress">SectionProgress</a></span><span class="p">],</span> <span class="nv">maneuverProgress</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-maneuverprogress">ManeuverProgress</a></span><span class="p">],</span> <span class="nv">routeMatchedLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-routematchedlocation">RouteMatchedLocation</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-routematchedlocation">RouteMatchedLocation</a></span><span class="p">())</span></code></pre>
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

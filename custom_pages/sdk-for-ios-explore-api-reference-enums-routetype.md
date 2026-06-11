---
title: "sdk-for-ios-explore-api-reference-enums-routetype"
slug: "sdk-for-ios-explore-api-reference-enums-routetype"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RouteType"></a>
<a title="RouteType Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-core">Core</a>
<img alt="" id="carat" src="/carat.png"/>
        RouteType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RouteType</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RouteType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Indicates the level of significance of a route in a range from 1 to 6. A value of 1 stands for
the most major route and 6 the most minor. The route type indicates that the road’s name is
actually a route number and in many countries is displayed in a shield symbol (e.g., Interstate
and State routes in the U.S.).
See <a href="https://developer.here.com/documentation/here-map-content-schema/dev_guide/topics_schema/streetname.routetype.html">https://developer.here.com/documentation/here-map-content-schema/dev_guide/topics_schema/streetname.routetype.html</a></p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9RouteTypeO11typeUnknownyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/typeUnknown"></a>
<a class="token" href="#/s:7heresdk9RouteTypeO11typeUnknownyA2CmF">typeUnknown</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unknown</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">typeUnknown</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9RouteTypeO10level1RoadyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/level1Road"></a>
<a class="token" href="#/s:7heresdk9RouteTypeO10level1RoadyA2CmF">level1Road</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>International / European road</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">level1Road</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9RouteTypeO10level2RoadyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/level2Road"></a>
<a class="token" href="#/s:7heresdk9RouteTypeO10level2RoadyA2CmF">level2Road</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>National road</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">level2Road</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9RouteTypeO10level3RoadyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/level3Road"></a>
<a class="token" href="#/s:7heresdk9RouteTypeO10level3RoadyA2CmF">level3Road</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Primary road</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">level3Road</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9RouteTypeO10level4RoadyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/level4Road"></a>
<a class="token" href="#/s:7heresdk9RouteTypeO10level4RoadyA2CmF">level4Road</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Secondary road</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">level4Road</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9RouteTypeO10level5RoadyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/level5Road"></a>
<a class="token" href="#/s:7heresdk9RouteTypeO10level5RoadyA2CmF">level5Road</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Minor road</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">level5Road</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9RouteTypeO10level6RoadyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/level6Road"></a>
<a class="token" href="#/s:7heresdk9RouteTypeO10level6RoadyA2CmF">level6Road</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Avenue</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">level6Road</span></code></pre>
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

---
title: "RouteType Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-routetype"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- RouteType.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/RouteType"></a>
<a title="RouteType Enumeration Reference"></a>
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
        RouteType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum RouteType : UInt32, CaseIterable, Codable</code></pre>
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
<pre><code>case typeUnknown</code></pre>
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
<pre><code>case level1Road</code></pre>
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
<pre><code>case level2Road</code></pre>
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
<pre><code>case level3Road</code></pre>
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
<pre><code>case level4Road</code></pre>
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
<pre><code>case level5Road</code></pre>
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
<pre><code>case level6Road</code></pre>
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



</div>
`
}</HTMLBlock>

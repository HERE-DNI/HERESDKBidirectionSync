---
title: "TilingScheme Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-tilingscheme"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TilingScheme.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/TilingScheme"></a>
<a title="TilingScheme Enumeration Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Maps.html">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TilingScheme Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum TilingScheme : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>List of available data tiling schemes.
X axis has the origin at -180 longitude and is increasing in east direction.
Y axis has the origin at max latitude and is increasing in south direction.
For half quad tree schemes, only the uppper half of the tree is used.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12TilingSchemeO20halfQuadTreeIdentityyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/halfQuadTreeIdentity"></a>
<a class="token" href="#/s:7heresdk12TilingSchemeO20halfQuadTreeIdentityyA2CmF">halfQuadTreeIdentity</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case halfQuadTreeIdentity</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12TilingSchemeO20halfQuadTreeMercatoryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/halfQuadTreeMercator"></a>
<a class="token" href="#/s:7heresdk12TilingSchemeO20halfQuadTreeMercatoryA2CmF">halfQuadTreeMercator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.
The coordinates of the tile’s corners are transformed through the web-mercator projection.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case halfQuadTreeMercator</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12TilingSchemeO27halfQuadTreeEquirectangularyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/halfQuadTreeEquirectangular"></a>
<a class="token" href="#/s:7heresdk12TilingSchemeO27halfQuadTreeEquirectangularyA2CmF">halfQuadTreeEquirectangular</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.
The coordinates of the tile’s corners are transformed through the equirectangular (plate carree) projection.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case halfQuadTreeEquirectangular</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12TilingSchemeO16quadTreeIdentityyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/quadTreeIdentity"></a>
<a class="token" href="#/s:7heresdk12TilingSchemeO16quadTreeIdentityyA2CmF">quadTreeIdentity</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A tiling scheme that splits each level tile into 4 equal-sized subtiles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case quadTreeIdentity</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12TilingSchemeO16quadTreeMercatoryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/quadTreeMercator"></a>
<a class="token" href="#/s:7heresdk12TilingSchemeO16quadTreeMercatoryA2CmF">quadTreeMercator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A tiling scheme that splits each level tile into 4 equal-sized subtiles.
The coordinates of the tile’s corners are transformed through the web-mercator projection.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case quadTreeMercator</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12TilingSchemeO23quadTreeEquirectangularyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/quadTreeEquirectangular"></a>
<a class="token" href="#/s:7heresdk12TilingSchemeO23quadTreeEquirectangularyA2CmF">quadTreeEquirectangular</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A tiling scheme that splits each level tile into 4 equal-sized subtiles.
The coordinates of the tile’s corners are transformed through the equirectangular (plate carree) projection.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case quadTreeEquirectangular</code></pre>
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

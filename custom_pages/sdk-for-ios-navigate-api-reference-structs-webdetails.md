---
title: "sdk-for-ios-navigate-api-reference-structs-webdetails"
slug: "sdk-for-ios-navigate-api-reference-structs-webdetails"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/WebDetails"></a>
<a title="WebDetails Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-search">Search</a>
<img alt="" id="carat" src="/carat.png"/>
        WebDetails Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>WebDetails</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">WebDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains information about images, editorials, rating and a urls to them.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10WebDetailsV6imagesSayAA0B5ImageVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/images"></a>
<a class="token" href="#/s:7heresdk10WebDetailsV6imagesSayAA0B5ImageVGvp">images</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of images associated with the place.
The images are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">images</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-webimage">WebImage</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10WebDetailsV10editorialsSayAA0B9EditorialVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/editorials"></a>
<a class="token" href="#/s:7heresdk10WebDetailsV10editorialsSayAA0B9EditorialVGvp">editorials</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of editorials associated with the place.
The editorials are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">editorials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-webeditorial">WebEditorial</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10WebDetailsV7ratingsSayAA0B6RatingVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ratings"></a>
<a class="token" href="#/s:7heresdk10WebDetailsV7ratingsSayAA0B6RatingVGvp">ratings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of ratings associated with the place.
The ratings are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">ratings</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-webrating">WebRating</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10WebDetailsV6images10editorials7ratingsACSayAA0B5ImageVG_SayAA0B9EditorialVGSayAA0B6RatingVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(images:editorials:ratings:)"></a>
<a class="token" href="#/s:7heresdk10WebDetailsV6images10editorials7ratingsACSayAA0B5ImageVG_SayAA0B9EditorialVGSayAA0B6RatingVGtcfc">init(images:<wbr/>editorials:<wbr/>ratings:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">images</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-webimage">WebImage</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">editorials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-webeditorial">WebEditorial</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">ratings</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-webrating">WebRating</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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

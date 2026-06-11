---
title: "sdk-for-ios-navigate-api-reference-structs-w3wsquare"
slug: "sdk-for-ios-navigate-api-reference-structs-w3wsquare"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/W3WSquare"></a>
<a title="W3WSquare Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-search">Search</a>
<img alt="" id="carat" src="/carat.png"/>
        W3WSquare Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>W3WSquare</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">W3WSquare</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains information about one of the squares in the what3words geocode system.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9W3WSquareV6squareAA6GeoBoxVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/square"></a>
<a class="token" href="#/s:7heresdk9W3WSquareV6squareAA6GeoBoxVvp">square</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A 3-by-3-metre square defined by the what3words geocode system.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">square</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geobox">GeoBox</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9W3WSquareV11coordinatesAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk9W3WSquareV11coordinatesAA14GeoCoordinatesVvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The center of the square.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9W3WSquareV5wordsSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/words"></a>
<a class="token" href="#/s:7heresdk9W3WSquareV5wordsSSvp">words</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>3 word address of the square, for example “///wage.mere.heap”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">words</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9W3WSquareV12languageCodeSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/languageCode"></a>
<a class="token" href="#/s:7heresdk9W3WSquareV12languageCodeSSvp">languageCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The language code of the words as an ISO 639-1 2 letter code.
Each supported language has its own set of words for each of the squares in
the what3words geocode system.
For Bosnian-Croatian-Montenegrin-Serbian, a special code “oo” is used.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">languageCode</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9W3WSquareV11countryCodeSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/countryCode"></a>
<a class="token" href="#/s:7heresdk9W3WSquareV11countryCodeSSSgvp">countryCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Country that contains the square.
Not set if the square is in an area not governed by a specific country, such as
international waters, Antarctica, some uninhabited islands etc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">countryCode</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9W3WSquareV6square11coordinates5words12languageCode07countryH0AcA6GeoBoxV_AA0J11CoordinatesVS3SSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(square:coordinates:words:languageCode:countryCode:)"></a>
<a class="token" href="#/s:7heresdk9W3WSquareV6square11coordinates5words12languageCode07countryH0AcA6GeoBoxV_AA0J11CoordinatesVS3SSgtcfc">init(square:<wbr/>coordinates:<wbr/>words:<wbr/>languageCode:<wbr/>countryCode:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">square</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geobox">GeoBox</a></span><span class="p">,</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">words</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">languageCode</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">countryCode</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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

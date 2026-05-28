---
title: "Maps / AssetsManager"
slug: "sdk-for-ios-explore-api-reference-classes-assetsmanager"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/AssetsManager"></a>
<a title="AssetsManager Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        AssetsManager Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>AssetsManager</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">AssetsManager</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AssetsManager</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AssetsManager</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Assets manager interface. Can be used to make assets available to the SDK.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13AssetsManagerCyAcA10MapContextCcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk13AssetsManagerCyAcA10MapContextCcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of AssetsManager.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">context</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcontext">MapContext</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>context</em>
</code>
</td>
<td>
<div>
<p>MapContext to which the assets belong.</p>
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
<a name="/s:7heresdk13AssetsManagerC12registerFont8fontName0F4PathySS_SStF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/registerFont(fontName:fontPath:)"></a>
<a class="token" href="#/s:7heresdk13AssetsManagerC12registerFont8fontName0F4PathySS_SStF">registerFont(fontName:<wbr/>fontPath:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Registers a font under a font name.
After registration, the font name can be used in</p>
<ul>
<li>the SVG <code>text</code> tag as <code>font-family</code> attribute parameter when creating a <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapimage">MapImage</a></code> with <code>ImageFormat.SVG</code>.</li>
<li><code><a href="sdk-for-ios-explore-api-reference-..-classes-mapmarker-textstyle">MapMarker.TextStyle</a></code></li>
</ul>
<p>Repeated registration with the same font name is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">registerFont</span><span class="p">(</span><span class="nv">fontName</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">fontPath</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>fontName</em>
</code>
</td>
<td>
<div>
<p>A font name.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>fontPath</em>
</code>
</td>
<td>
<div>
<p>A font file path. TTF, OTF and WOFF formats are supported.
Can be an absolute file path or a resolved bundle resource path.</p>
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
<a name="/s:7heresdk13AssetsManagerC24registerFontWithFallback8fontName0H4Path08fallbackE9FilePathsySS_SSSaySSGtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/registerFontWithFallback(fontName:fontPath:fallbackFontFilePaths:)"></a>
<a class="token" href="#/s:7heresdk13AssetsManagerC24registerFontWithFallback8fontName0H4Path08fallbackE9FilePathsySS_SSSaySSGtF">registerFontWithFallback(fontName:<wbr/>fontPath:<wbr/>fallbackFontFilePaths:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Registers a font set under a font name.
After registration, the font name can be used in</p>
<ul>
<li>the SVG <code>text</code> tag as <code>font-family</code> attribute parameter when creating a <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapimage">MapImage</a></code> with <code>ImageFormat.SVG</code>.</li>
<li><code><a href="sdk-for-ios-explore-api-reference-..-classes-mapmarker-textstyle">MapMarker.TextStyle</a></code></li>
</ul>
<p>Repeated registration with the same font name is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">registerFontWithFallback</span><span class="p">(</span><span class="nv">fontName</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">fontPath</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">fallbackFontFilePaths</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>fontName</em>
</code>
</td>
<td>
<div>
<p>A font name.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>fontPath</em>
</code>
</td>
<td>
<div>
<p>A font file path. TTF, OTF and WOFF formats are supported.
Can be an absolute file path or a resolved bundle resource path.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>fallbackFontFilePaths</em>
</code>
</td>
<td>
<div>
<p>Additional font files are intended to be used if main font
does not contain required character symbol and shall be sorted starting from most useful.</p>
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

---
title: "AssetsManager Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-assetsmanager"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- AssetsManager.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/AssetsManager"></a>
<a title="AssetsManager Class Reference"></a>
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
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        AssetsManager Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class AssetsManager</code></pre>
<pre><code>extension AssetsManager: NativeBase</code></pre>
<pre><code>extension AssetsManager: Hashable</code></pre>
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
<pre><code>public init(_ context: MapContext)</code></pre>
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
<pre><code>public func registerFont(fontName: String, fontPath: String)</code></pre>
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
<pre><code>public func registerFontWithFallback(fontName: String, fontPath: String, fallbackFontFilePaths: [String])</code></pre>
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



</div>
`
}</HTMLBlock>

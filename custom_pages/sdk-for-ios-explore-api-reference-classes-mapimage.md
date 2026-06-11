---
title: "sdk-for-ios-explore-api-reference-classes-mapimage"
slug: "sdk-for-ios-explore-api-reference-classes-mapimage"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapImage"></a>
<a title="MapImage Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>
<img alt="" id="carat" src="/carat.png"/>
        MapImage Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapImage</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapImage</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapImage</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapImage</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a drawable resource that can be used by a <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code>, <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker3d">MapMarker3D</a></code> or <code><a href="sdk-for-ios-explore-api-reference-classes-mapimageoverlay">MapImageOverlay</a></code> to be shown on the map.
Supported formats are listed in <code><a href="sdk-for-ios-explore-api-reference-enums-imageformat">ImageFormat</a></code>.
SVG format allows custom fonts in text using font-family attribute by prior registration via <code>AssetsManager.registerFont</code>.</p>
<p>It is recommended to associate a resource with a single <code>MapImage</code> instance in order to enable
resource sharing and reduce the amount of needed memory.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapImageC9pixelData11imageFormatAC10Foundation0E0V_AA0cG0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(pixelData:imageFormat:)"></a>
<a class="token" href="#/s:7heresdk8MapImageC9pixelData11imageFormatAC10Foundation0E0V_AA0cG0Otcfc">init(pixelData:<wbr/>imageFormat:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new map image from the provided image data. Currently only <code><a href="../Enums/ImageFormat.html#/s:7heresdk11ImageFormatO3pngyA2CmF">ImageFormat.png</a></code>
is accepted.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">pixelData</span><span class="p">:</span> <span class="kt">Data</span><span class="p">,</span> <span class="nv">imageFormat</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-imageformat">ImageFormat</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>pixelData</em>
</code>
</td>
<td>
<div>
<p>Data to be used for the image. The bytes of a PNG image datastream are expected as
defined in <a href="https://www.w3.org/TR/PNG">https://www.w3.org/TR/PNG</a></p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>imageFormat</em>
</code>
</td>
<td>
<div>
<p>The format of the image data to be used.</p>
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
<a name="/s:7heresdk8MapImageC9imageData0D6Format5width6heightAC10Foundation0E0V_AA0cF0Os6UInt32VANtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(imageData:imageFormat:width:height:)"></a>
<a class="token" href="#/s:7heresdk8MapImageC9imageData0D6Format5width6heightAC10Foundation0E0V_AA0cF0Os6UInt32VANtcfc">init(imageData:<wbr/>imageFormat:<wbr/>width:<wbr/>height:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new map image from the provided image data.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">imageData</span><span class="p">:</span> <span class="kt">Data</span><span class="p">,</span> <span class="nv">imageFormat</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-imageformat">ImageFormat</a></span><span class="p">,</span> <span class="nv">width</span><span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="nv">height</span><span class="p">:</span> <span class="kt">UInt32</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>imageData</em>
</code>
</td>
<td>
<div>
<p>Data to be used for the image. For image format <code><a href="../Enums/ImageFormat.html#/s:7heresdk11ImageFormatO3svgyA2CmF">ImageFormat.svg</a></code> the bytes
of a UTF-8 encoded string in SVG Tiny format are expected. For the format specification
see <a href="https://www.w3.org/TR/SVGTiny12">https://www.w3.org/TR/SVGTiny12</a></p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>imageFormat</em>
</code>
</td>
<td>
<div>
<p>The format of the image data to be used.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>width</em>
</code>
</td>
<td>
<div>
<p>The width of the image in pixels.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>height</em>
</code>
</td>
<td>
<div>
<p>The height of the image in pixels.</p>
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
<a name="/s:7heresdk8MapImageC8filePath5width6heightACSS_s6UInt32VAHtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(filePath:width:height:)"></a>
<a class="token" href="#/s:7heresdk8MapImageC8filePath5width6heightACSS_s6UInt32VAHtKcfc">init(filePath:<wbr/>width:<wbr/>height:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new map image from the provided path to the SVG Tiny or PNG image.</p>
<p>Will throw an error if either the height or width equals zero or the path is empty.</p>
<p>Trying to load a file that is not compliant with SVG Tiny or PNG results
in an undefined behavior. In particular, loading SVG that exceeds Tiny SVG
specification may result in an image that exhibits unexpected artifacts.</p>
<p>The caller must ensure that the file remains accessible for the entire duration of its usage by the
SDK. If that cannot be ensured, then it is recommended to either copy the file to a location that
remains accessible for the entire duration of its usage by the SDK or load and pass the file content
to one of the <code>MapImage</code> constructors that creates instances out of image data
(<code>MapImage.init(Data, ImageFormat)</code>, <code>MapImage.init(Data, ImageFormat, UInt32, UInt32)</code>).}</p>
<p>Please note that file paths that originate, for example from a file picker (like <code>UIDocumentPickerViewController</code>)
can be deleted by the system while the application is still running.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">filePath</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">width</span><span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="nv">height</span><span class="p">:</span> <span class="kt">UInt32</span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>filePath</em>
</code>
</td>
<td>
<div>
<p>The path to image file.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>width</em>
</code>
</td>
<td>
<div>
<p>The width of image in pixels.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>height</em>
</code>
</td>
<td>
<div>
<p>The height of image in pixels.</p>
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
<a name="/s:7heresdk8MapImageC4fromACSgSo7UIImageC_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(from:)"></a>
<a class="token" href="#/s:7heresdk8MapImageC4fromACSgSo7UIImageC_tKcfc">init(from:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a map image object from the supplied <code>UIImage</code> object.
Throws an error if the supplied <code>UIImage</code> does not represent
a regular image (for example, when it represents a mask).</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code>MapImage.InstantiationError</code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="n">convenience</span> <span class="nf">init</span><span class="p">?(</span><span class="n">from</span> <span class="nv">uiImage</span><span class="p">:</span> <span class="kt">UIImage</span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>uiImage</em>
</code>
</td>
<td>
<div>
<p>The image to use as source data.</p>
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
<a name="/s:7heresdk8MapImageC5named5width6height2inACSS_s5Int32VAISo8NSBundleCSgtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(named:width:height:in:)"></a>
<a class="token" href="#/s:7heresdk8MapImageC5named5width6height2inACSS_s5Int32VAISo8NSBundleCSgtKcfc">init(named:<wbr/>width:<wbr/>height:<wbr/>in:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a map image object using a named image asset from the application’s main bundle or another
bundle which can optionally be passed in. Currently only PNG or SVG Tiny image resources are supported.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code>MapImage.InstantiationError</code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="n">convenience</span> <span class="nf">init</span><span class="p">(</span><span class="n">named</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">width</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">height</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="k">in</span> <span class="nv">bundle</span><span class="p">:</span> <span class="kt">Bundle</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>name</em>
</code>
</td>
<td>
<div>
<p>The name of the image asset.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>width</em>
</code>
</td>
<td>
<div>
<p>Width of image in pixels</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>height</em>
</code>
</td>
<td>
<div>
<p>Height of image in pixels</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>bundle</em>
</code>
</td>
<td>
<div>
<p>The bundle in which the asset resides. The main application bundle is used if not specified.</p>
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

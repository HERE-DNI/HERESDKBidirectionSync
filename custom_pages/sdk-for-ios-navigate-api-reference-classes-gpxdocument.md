---
title: "Navigation / GPXDocument"
slug: "sdk-for-ios-navigate-api-reference-classes-gpxdocument"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/GPXDocument"></a>
<a title="GPXDocument Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        GPXDocument Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>GPXDocument</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">GPXDocument</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">GPXDocument</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">GPXDocument</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use the GPXDocument to load the GPX file.
Only track data is used from the GPX file format
(see trkType at <a href="https://www.topografix.com/GPX/1/1/#type_trkType">https://www.topografix.com/GPX/1/1/#type_trkType</a>).
Any unknown elements in the file are ignored.
Any known element with an invalid value returns an error.
Elevation values are ignored.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GPXDocumentC11gpxFilePath7optionsACSS_AA10GPXOptionsVtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(gpxFilePath:options:)"></a>
<a class="token" href="#/s:7heresdk11GPXDocumentC11gpxFilePath7optionsACSS_AA10GPXOptionsVtKcfc">init(gpxFilePath:<wbr/>options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Create a GPX document from a file.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">gpxFilePath</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-gpxoptions">GPXOptions</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>gpxFilePath</em>
</code>
</td>
<td>
<div>
<p>The path to the GPX file.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>The options to customize reading.</p>
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
<a name="/s:7heresdk11GPXDocumentC6tracksACSayAA8GPXTrackCG_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(tracks:)"></a>
<a class="token" href="#/s:7heresdk11GPXDocumentC6tracksACSayAA8GPXTrackCG_tcfc">init(tracks:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Create a GPX document from a list of GPX tracks.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">tracks</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-gpxtrack">GPXTrack</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tracks</em>
</code>
</td>
<td>
<div>
<p>The list of tracks.</p>
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
<a name="/s:7heresdk11GPXDocumentC6tracksSayAA8GPXTrackCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tracks"></a>
<a class="token" href="#/s:7heresdk11GPXDocumentC6tracksSayAA8GPXTrackCGvp">tracks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The tracks stored in this GPX document.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tracks</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-gpxtrack">GPXTrack</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GPXDocumentC10fromString7content7optionsACSS_AA10GPXOptionsVtKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fromString(content:options:)"></a>
<a class="token" href="#/s:7heresdk11GPXDocumentC10fromString7content7optionsACSS_AA10GPXOptionsVtKFZ">fromString(content:<wbr/>options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Create a GPX document from a string.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">fromString</span><span class="p">(</span><span class="nv">content</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-gpxoptions">GPXOptions</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt">GPXDocument</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>content</em>
</code>
</td>
<td>
<div>
<p>The content of a GPX file as string.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>The options to customize reading.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>An <code>GPXDocument</code> instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GPXDocumentC4save11gpxFilePathSbSS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/save(gpxFilePath:)"></a>
<a class="token" href="#/s:7heresdk11GPXDocumentC4save11gpxFilePathSbSS_tF">save(gpxFilePath:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Saves the document to a file.
For saving the <code><a href="../Classes/GPXDocument.html#/s:7heresdk11GPXDocumentC6tracksSayAA8GPXTrackCGvp">GPXDocument.tracks</a></code> modification before writing to a file, use <code><a href="sdk-for-ios-navigate-api-reference-..-classes-gpxtrackwriter">GPXTrackWriter</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">save</span><span class="p">(</span><span class="nv">gpxFilePath</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>gpxFilePath</em>
</code>
</td>
<td>
<div>
<p>The file path where the GPX document will be saved.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code>True</code> if the document has been saved successfully.
<code>False</code> if an error has been happened during saving.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GPXDocumentC8addTrack10trackToAddyAA8GPXTrackC_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addTrack(trackToAdd:)"></a>
<a class="token" href="#/s:7heresdk11GPXDocumentC8addTrack10trackToAddyAA8GPXTrackC_tF">addTrack(trackToAdd:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Add track to GPX document.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addTrack</span><span class="p">(</span><span class="nv">trackToAdd</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-gpxtrack">GPXTrack</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>trackToAdd</em>
</code>
</td>
<td>
<div>
<p>track to add to GPX document</p>
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

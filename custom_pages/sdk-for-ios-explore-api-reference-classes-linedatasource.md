---
title: "sdk-for-ios-explore-api-reference-classes-linedatasource"
slug: "sdk-for-ios-explore-api-reference-classes-linedatasource"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataSource"></a>
<a title="LineDataSource Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maploader">MapLoader</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LineDataSource Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LineDataSource</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LineDataSource</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineDataSource</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineDataSource</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Polyline data source allows the rendering engine access to the user provided
polylines geometry and their attributes.</p>
<p>Polyline segments are rendered following the shortest path between their end vertices.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LineDataSourceC0bC9Processora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/LineDataProcessor"></a>
<a class="token" href="#/s:7heresdk14LineDataSourceC0bC9Processora">LineDataProcessor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called for each line, allowing inspection, removal or update of coordinates and attributes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">LineDataProcessor</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">lineAccessor</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-linedataaccessor">LineDataAccessor</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>lineAccessor</em>
</code>
</td>
<td>
<div>
<p>the line data accessor.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>value indicating the result of the processing.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LineDataSourceC3addyyAA0bC0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/add(_:)"></a>
<a class="token" href="#/s:7heresdk14LineDataSourceC3addyyAA0bC0CF">add(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a new line to the data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">add</span><span class="p">(</span><span class="n">_</span> <span class="nv">line</span><span class="p">:</span> <span class="kt"><a href="../MapLoader.html#/s:7heresdk8LineDataC">LineData</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>line</em>
</code>
</td>
<td>
<div>
<p>Line to add.</p>
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
<a name="/s:7heresdk14LineDataSourceC3addyySayAA0bC0CGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/add(_:)"></a>
<a class="token" href="#/s:7heresdk14LineDataSourceC3addyySayAA0bC0CGF">add(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds new lines to the data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">add</span><span class="p">(</span><span class="n">_</span> <span class="nv">lines</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="../MapLoader.html#/s:7heresdk8LineDataC">LineData</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>lines</em>
</code>
</td>
<td>
<div>
<p>Lines to add.</p>
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
<a name="/s:7heresdk14LineDataSourceC9removeAllyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeAll()"></a>
<a class="token" href="#/s:7heresdk14LineDataSourceC9removeAllyyF">removeAll()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all lines from the data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeAll</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LineDataSourceC7forEachyySbAA0bC8AccessorCcF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/forEach(_:)"></a>
<a class="token" href="#/s:7heresdk14LineDataSourceC7forEachyySbAA0bC8AccessorCcF">forEach(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Iterates through all the lines from the data source and passes them to the
given processor, one by one. The processor can update the line data.
The iteration stops after all lines have been processed or the processor returns false
from the process call.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">forEach</span><span class="p">(</span><span class="n">_</span> <span class="nv">processor</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt">LineDataSource</span><span class="o">.</span><span class="kt"><a href="../Classes/LineDataSource.html#/s:7heresdk14LineDataSourceC0bC9Processora">LineDataProcessor</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>processor</em>
</code>
</td>
<td>
<div>
<p>Line processor.</p>
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
<a name="/s:7heresdk14LineDataSourceC8removeIfyySbAA0bC8AccessorCcF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeIf(_:)"></a>
<a class="token" href="#/s:7heresdk14LineDataSourceC8removeIfyySbAA0bC8AccessorCcF">removeIf(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Iterates through all the lines from the data source and passes them to the
given inspector, one by one. All lines for which the inspector returns <code>true</code> get removed from the data source.
The inspector cannot update the line data.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeIf</span><span class="p">(</span><span class="n">_</span> <span class="nv">inspector</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt">LineDataSource</span><span class="o">.</span><span class="kt"><a href="../Classes/LineDataSource.html#/s:7heresdk14LineDataSourceC0bC9Processora">LineDataProcessor</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>inspector</em>
</code>
</td>
<td>
<div>
<p>Line data processor.</p>
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

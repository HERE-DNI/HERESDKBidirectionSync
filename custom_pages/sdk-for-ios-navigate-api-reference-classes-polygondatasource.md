---
title: "Maps / PolygonDataSource"
slug: "sdk-for-ios-navigate-api-reference-classes-polygondatasource"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/PolygonDataSource"></a>
<a title="PolygonDataSource Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        PolygonDataSource Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PolygonDataSource</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PolygonDataSource</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonDataSource</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonDataSource</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Polygon data source allows the rendering engine access to the user provided
polygons geometry and their attributes.</p>
<p>Polygon segments are rendered following the shortest path between their end points.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PolygonDataSourceC0bC9Processora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/PolygonDataProcessor"></a>
<a class="token" href="#/s:7heresdk17PolygonDataSourceC0bC9Processora">PolygonDataProcessor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called for each polygon, allowing inspection, removal or update of coordinates and attributes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">PolygonDataProcessor</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">polygonAccessor</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-polygondataaccessor">PolygonDataAccessor</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>polygonAccessor</em>
</code>
</td>
<td>
<div>
<p>the polygon data accessor.</p>
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
<a name="/s:7heresdk17PolygonDataSourceC3addyyAA0bC0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/add(_:)"></a>
<a class="token" href="#/s:7heresdk17PolygonDataSourceC3addyyAA0bC0CF">add(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a new polygon to the data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">add</span><span class="p">(</span><span class="n">_</span> <span class="nv">polygon</span><span class="p">:</span> <span class="kt"><a href="../Maps.html#/s:7heresdk11PolygonDataC">PolygonData</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>polygon</em>
</code>
</td>
<td>
<div>
<p>Polygon to add.</p>
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
<a name="/s:7heresdk17PolygonDataSourceC3addyySayAA0bC0CGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/add(_:)"></a>
<a class="token" href="#/s:7heresdk17PolygonDataSourceC3addyySayAA0bC0CGF">add(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds new polygons to the data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">add</span><span class="p">(</span><span class="n">_</span> <span class="nv">polygons</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="../Maps.html#/s:7heresdk11PolygonDataC">PolygonData</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>polygons</em>
</code>
</td>
<td>
<div>
<p>Polygons to add.</p>
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
<a name="/s:7heresdk17PolygonDataSourceC9removeAllyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeAll()"></a>
<a class="token" href="#/s:7heresdk17PolygonDataSourceC9removeAllyyF">removeAll()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all polygons from the data source.</p>
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
<a name="/s:7heresdk17PolygonDataSourceC7forEachyySbAA0bC8AccessorCcF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/forEach(_:)"></a>
<a class="token" href="#/s:7heresdk17PolygonDataSourceC7forEachyySbAA0bC8AccessorCcF">forEach(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Iterates through all the polygons from the data source and passes them to the
given processor, one by one. The processor can update the polygon data.</p>
<p>The iteration stops after all polygons have been processed or the processor returns false
from the process call.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">forEach</span><span class="p">(</span><span class="n">_</span> <span class="nv">processor</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt">PolygonDataSource</span><span class="o">.</span><span class="kt"><a href="../Classes/PolygonDataSource.html#/s:7heresdk17PolygonDataSourceC0bC9Processora">PolygonDataProcessor</a></span><span class="p">)</span></code></pre>
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
<p>Polygon processor.</p>
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
<a name="/s:7heresdk17PolygonDataSourceC8removeIfyySbAA0bC8AccessorCcF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeIf(_:)"></a>
<a class="token" href="#/s:7heresdk17PolygonDataSourceC8removeIfyySbAA0bC8AccessorCcF">removeIf(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Iterates through all the polygons from the data source and passes them to the
given inspector, one by one. All polygons for which the inspector returns <code>true</code> get removed from the data source.
The inspector cannot update the polygon data.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeIf</span><span class="p">(</span><span class="n">_</span> <span class="nv">inspector</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt">PolygonDataSource</span><span class="o">.</span><span class="kt"><a href="../Classes/PolygonDataSource.html#/s:7heresdk17PolygonDataSourceC0bC9Processora">PolygonDataProcessor</a></span><span class="p">)</span></code></pre>
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
<p>Polygon data processor.</p>
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

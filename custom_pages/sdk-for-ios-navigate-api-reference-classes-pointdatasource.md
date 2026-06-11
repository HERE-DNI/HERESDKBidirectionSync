---
title: "sdk-for-ios-navigate-api-reference-classes-pointdatasource"
slug: "sdk-for-ios-navigate-api-reference-classes-pointdatasource"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/PointDataSource"></a>
<a title="PointDataSource Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>
<img alt="" id="carat" src="/carat.png"/>
        PointDataSource Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PointDataSource</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PointDataSource</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointDataSource</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointDataSource</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Point data source allows the rendering engine access to the user provided
geographical locations and their attributes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15PointDataSourceC0bC9Processora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/PointDataProcessor"></a>
<a class="token" href="#/s:7heresdk15PointDataSourceC0bC9Processora">PointDataProcessor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called for each point, allowing inspection, removal or update of coordinates and attributes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">PointDataProcessor</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">pointAccessor</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-pointdataaccessor">PointDataAccessor</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>pointAccessor</em>
</code>
</td>
<td>
<div>
<p>the point data accessor.</p>
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
<a name="/s:7heresdk15PointDataSourceC3addyyAA0bC0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/add(_:)"></a>
<a class="token" href="#/s:7heresdk15PointDataSourceC3addyyAA0bC0CF">add(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a new point to the data source.
Altitude of the point coordinates is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">add</span><span class="p">(</span><span class="n">_</span> <span class="nv">point</span><span class="p">:</span> <span class="kt"><a href="../Maps.html#/s:7heresdk9PointDataC">PointData</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>point</em>
</code>
</td>
<td>
<div>
<p>Point to be added.</p>
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
<a name="/s:7heresdk15PointDataSourceC3addyySayAA0bC0CGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/add(_:)"></a>
<a class="token" href="#/s:7heresdk15PointDataSourceC3addyySayAA0bC0CGF">add(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds new points to the data source.
Altitude of the points coordinates is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">add</span><span class="p">(</span><span class="n">_</span> <span class="nv">points</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="../Maps.html#/s:7heresdk9PointDataC">PointData</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>points</em>
</code>
</td>
<td>
<div>
<p>Point positions.</p>
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
<a name="/s:7heresdk15PointDataSourceC9removeAllyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeAll()"></a>
<a class="token" href="#/s:7heresdk15PointDataSourceC9removeAllyyF">removeAll()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all points from the data source.</p>
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
<a name="/s:7heresdk15PointDataSourceC7forEachyySbAA0bC8AccessorCcF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/forEach(_:)"></a>
<a class="token" href="#/s:7heresdk15PointDataSourceC7forEachyySbAA0bC8AccessorCcF">forEach(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Iterates through all the points from the data source and passes them to the
given processor, one by one. The processor can update the point data.</p>
<p>The iteration stops after all points have been processed or the processor returns false
from the process call.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">forEach</span><span class="p">(</span><span class="n">_</span> <span class="nv">processor</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt">PointDataSource</span><span class="o">.</span><span class="kt"><a href="../Classes/PointDataSource.html#/s:7heresdk15PointDataSourceC0bC9Processora">PointDataProcessor</a></span><span class="p">)</span></code></pre>
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
<p>Point data processor.</p>
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
<a name="/s:7heresdk15PointDataSourceC8removeIfyySbAA0bC8AccessorCcF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeIf(_:)"></a>
<a class="token" href="#/s:7heresdk15PointDataSourceC8removeIfyySbAA0bC8AccessorCcF">removeIf(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Iterates through all the points from the data source and passes them to the
given inspector, one by one. All points for which the inspector returns <code>true</code> get removed from the data source.
The inspector cannot update the point data.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeIf</span><span class="p">(</span><span class="n">_</span> <span class="nv">processor</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt">PointDataSource</span><span class="o">.</span><span class="kt"><a href="../Classes/PointDataSource.html#/s:7heresdk15PointDataSourceC0bC9Processora">PointDataProcessor</a></span><span class="p">)</span></code></pre>
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
<p>Point data processor.</p>
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

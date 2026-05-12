---
title: "PointDataSource Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-pointdatasource"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- PointDataSource.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/PointDataSource"></a>
<a title="PointDataSource Class Reference"></a>
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
        PointDataSource Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class PointDataSource</code></pre>
<pre><code>extension PointDataSource: NativeBase</code></pre>
<pre><code>extension PointDataSource: Hashable</code></pre>
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
<pre><code>public typealias PointDataProcessor = (_ pointAccessor: PointDataAccessor) -&gt; Bool</code></pre>
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
<pre><code>public func add(_ point: PointData)</code></pre>
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
<pre><code>public func add(_ points: [PointData])</code></pre>
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
<pre><code>public func removeAll()</code></pre>
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
<pre><code>public func forEach(_ processor: @escaping PointDataSource.PointDataProcessor)</code></pre>
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
<pre><code>public func removeIf(_ processor: @escaping PointDataSource.PointDataProcessor)</code></pre>
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



</div>
`
}</HTMLBlock>

---
title: "LineDataSource Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-linedatasource"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- LineDataSource.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataSource"></a>
<a title="LineDataSource Class Reference"></a>
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
<a href="sdk-for-ios-explore-api-reference-..-maploader">MapLoader</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LineDataSource Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class LineDataSource</code></pre>
<pre><code>extension LineDataSource: NativeBase</code></pre>
<pre><code>extension LineDataSource: Hashable</code></pre>
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
<pre><code>public typealias LineDataProcessor = (_ lineAccessor: LineDataAccessor) -&gt; Bool</code></pre>
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
<pre><code>public func add(_ line: LineData)</code></pre>
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
<pre><code>public func add(_ lines: [LineData])</code></pre>
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
<pre><code>public func removeAll()</code></pre>
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
<pre><code>public func forEach(_ processor: @escaping LineDataSource.LineDataProcessor)</code></pre>
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
<pre><code>public func removeIf(_ inspector: @escaping LineDataSource.LineDataProcessor)</code></pre>
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



</div>
`
}</HTMLBlock>

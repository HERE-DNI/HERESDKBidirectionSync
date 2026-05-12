---
title: "LineDataSourceBuilder Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-linedatasourcebuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- LineDataSourceBuilder.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataSourceBuilder"></a>
<a title="LineDataSourceBuilder Class Reference"></a>
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
<a href="../MapLoader.html">MapLoader</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LineDataSourceBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class LineDataSourceBuilder</code></pre>
<pre><code>extension LineDataSourceBuilder: NativeBase</code></pre>
<pre><code>extension LineDataSourceBuilder: Hashable</code></pre>
</div>
</div>
<p>Builder of lines data source.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LineDataSourceBuilderCyAcA10MapContextCcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk21LineDataSourceBuilderCyAcA10MapContextCcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a data source builder instance in the given context.</p>
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
<p>Map context to associate the data source with.</p>
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
<a name="/s:7heresdk21LineDataSourceBuilderC8withNameyACSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withName(_:)"></a>
<a class="token" href="#/s:7heresdk21LineDataSourceBuilderC8withNameyACSSF">withName(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to use the given name for data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withName(_ dataSourceName: String) -&gt; LineDataSourceBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>dataSourceName</em>
</code>
</td>
<td>
<div>
<p>Name of the created data source. Must be unique.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This data source builder instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LineDataSourceBuilderC12withPolylineyAcA0bC0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withPolyline(_:)"></a>
<a class="token" href="#/s:7heresdk21LineDataSourceBuilderC12withPolylineyAcA0bC0CF">withPolyline(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to insert the given polyline in the data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withPolyline(_ polyline: LineData) -&gt; LineDataSourceBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>polyline</em>
</code>
</td>
<td>
<div>
<p>Polyline to add.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This data source builder instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LineDataSourceBuilderC13withPolylinesyACSayAA0bC0CGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withPolylines(_:)"></a>
<a class="token" href="#/s:7heresdk21LineDataSourceBuilderC13withPolylinesyACSayAA0bC0CGF">withPolylines(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to insert the given polylines in the data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withPolylines(_ polylines: [LineData]) -&gt; LineDataSourceBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>polylines</em>
</code>
</td>
<td>
<div>
<p>Polylines to add.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This data source builder instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LineDataSourceBuilderC5buildAA0bcD0CyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk21LineDataSourceBuilderC5buildAA0bcD0CyF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builds instance of LineDataSource.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func build() -&gt; LineDataSource</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Instance of the data source created with given polylines and attributes.</p>
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

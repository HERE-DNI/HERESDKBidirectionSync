---
title: "PolygonDataSourceBuilder Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-polygondatasourcebuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- PolygonDataSourceBuilder.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/PolygonDataSourceBuilder"></a>
<a title="PolygonDataSourceBuilder Class Reference"></a>
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
        PolygonDataSourceBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class PolygonDataSourceBuilder</code></pre>
<pre><code>extension PolygonDataSourceBuilder: NativeBase</code></pre>
<pre><code>extension PolygonDataSourceBuilder: Hashable</code></pre>
</div>
</div>
<p>Builder of the polygons data source.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PolygonDataSourceBuilderCyAcA10MapContextCcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk24PolygonDataSourceBuilderCyAcA10MapContextCcfc">init(_:<wbr/>)</a>
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
<a name="/s:7heresdk24PolygonDataSourceBuilderC8withNameyACSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withName(_:)"></a>
<a class="token" href="#/s:7heresdk24PolygonDataSourceBuilderC8withNameyACSSF">withName(_:<wbr/>)</a>
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
<pre><code>public func withName(_ dataSourceName: String) -&gt; PolygonDataSourceBuilder</code></pre>
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
<a name="/s:7heresdk24PolygonDataSourceBuilderC04withB0yAcA0bC0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withPolygon(_:)"></a>
<a class="token" href="#/s:7heresdk24PolygonDataSourceBuilderC04withB0yAcA0bC0CF">withPolygon(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to insert the given polygon in the data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withPolygon(_ polygon: PolygonData) -&gt; PolygonDataSourceBuilder</code></pre>
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
<p>The polygon to add.</p>
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
<a name="/s:7heresdk24PolygonDataSourceBuilderC12withPolygonsyACSayAA0bC0CGF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withPolygons(_:)"></a>
<a class="token" href="#/s:7heresdk24PolygonDataSourceBuilderC12withPolygonsyACSayAA0bC0CGF">withPolygons(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to insert the given polygons in the data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withPolygons(_ polygon: [PolygonData]) -&gt; PolygonDataSourceBuilder</code></pre>
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
<p>The polygons to add.</p>
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
<a name="/s:7heresdk24PolygonDataSourceBuilderC5buildAA0bcD0CyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk24PolygonDataSourceBuilderC5buildAA0bcD0CyF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builds a PolygonDataSource instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func build() -&gt; PolygonDataSource</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Instance of the data source created with given polygons and attributes.</p>
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

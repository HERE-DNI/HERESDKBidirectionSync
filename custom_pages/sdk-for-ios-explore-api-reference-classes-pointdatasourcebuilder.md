---
title: "PointDataSourceBuilder Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-pointdatasourcebuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- PointDataSourceBuilder.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/PointDataSourceBuilder"></a>
<a title="PointDataSourceBuilder Class Reference"></a>
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
        PointDataSourceBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class PointDataSourceBuilder</code></pre>
<pre><code>extension PointDataSourceBuilder: NativeBase</code></pre>
<pre><code>extension PointDataSourceBuilder: Hashable</code></pre>
</div>
</div>
<p>Builder of points data source.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22PointDataSourceBuilderCyAcA10MapContextCcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk22PointDataSourceBuilderCyAcA10MapContextCcfc">init(_:<wbr/>)</a>
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
<a name="/s:7heresdk22PointDataSourceBuilderC8withNameyACSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withName(_:)"></a>
<a class="token" href="#/s:7heresdk22PointDataSourceBuilderC8withNameyACSSF">withName(_:<wbr/>)</a>
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
<pre><code>public func withName(_ dataSourceName: String) -&gt; PointDataSourceBuilder</code></pre>
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
<a name="/s:7heresdk22PointDataSourceBuilderC04withB0yAcA0bC0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withPoint(_:)"></a>
<a class="token" href="#/s:7heresdk22PointDataSourceBuilderC04withB0yAcA0bC0CF">withPoint(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to insert the given point in the data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withPoint(_ point: PointData) -&gt; PointDataSourceBuilder</code></pre>
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
<a name="/s:7heresdk22PointDataSourceBuilderC10withPoints6pointsACSayAA0bC0CG_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withPoints(points:)"></a>
<a class="token" href="#/s:7heresdk22PointDataSourceBuilderC10withPoints6pointsACSayAA0bC0CG_tF">withPoints(points:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to insert the given points in the data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withPoints(points: [PointData]) -&gt; PointDataSourceBuilder</code></pre>
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
<p>Points to be added.</p>
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
<a name="/s:7heresdk22PointDataSourceBuilderC5buildAA0bcD0CyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk22PointDataSourceBuilderC5buildAA0bcD0CyF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builds a PointDataSource instance and resets the builder instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func build() -&gt; PointDataSource</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Instance of the data source created with given points and attributes.</p>
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

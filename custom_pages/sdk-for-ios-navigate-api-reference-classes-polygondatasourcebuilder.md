---
title: "PolygonDataSourceBuilder"
slug: "sdk-for-ios-navigate-api-reference-classes-polygondatasourcebuilder"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/PolygonDataSourceBuilder"></a>
<a title="PolygonDataSourceBuilder Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

        PolygonDataSourceBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PolygonDataSourceBuilder</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PolygonDataSourceBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonDataSourceBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonDataSourceBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">context</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapcontext">MapContext</a></span><span class="p">)</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withName</span><span class="p">(</span><span class="n">_</span> <span class="nv">dataSourceName</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">PolygonDataSourceBuilder</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withPolygon</span><span class="p">(</span><span class="n">_</span> <span class="nv">polygon</span><span class="p">:</span> <span class="kt"><a href="../Maps.html#/s:7heresdk11PolygonDataC">PolygonData</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">PolygonDataSourceBuilder</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withPolygons</span><span class="p">(</span><span class="n">_</span> <span class="nv">polygon</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="../Maps.html#/s:7heresdk11PolygonDataC">PolygonData</a></span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kt">PolygonDataSourceBuilder</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">build</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-polygondatasource">PolygonDataSource</a></span></code></pre>
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
</body>
</html>

`
}</HTMLBlock>

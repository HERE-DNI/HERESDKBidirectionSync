---
title: "Maps / RasterDataSource"
slug: "sdk-for-ios-explore-api-reference-classes-rasterdatasource"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/RasterDataSource"></a>
<a title="RasterDataSource Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        RasterDataSource Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RasterDataSource</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">RasterDataSource</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RasterDataSource</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RasterDataSource</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Data source to load map layers using a raster image format (jpg, png).
The example below illustrates how to create a raster data source and how to link it to
a newly created map layer.</p>
<pre class="highlight swift"><code>  <span class="k">let</span> <span class="nv">rasterDataSource</span> <span class="o">=</span> <span class="kt">RasterDataSource</span><span class="p">(</span><span class="n">mapContext</span><span class="p">,</span> <span class="n">rasterDataSourceConfig</span><span class="p">)</span>

  <span class="k">let</span> <span class="nv">layer</span> <span class="o">=</span> <span class="kt">MapLayerBuilder</span><span class="p">()</span>
     <span class="c1">// The name and the type of the data source have to be provided.</span>
     <span class="c1">// In our case, the name of the raster data source is in rasterDataSourceConfig.</span>
     <span class="o">.</span><span class="nf">withDataSource</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="n">rasterDataSourceConfig</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="nv">contentType</span><span class="p">:</span> <span class="kt">MapContentType</span><span class="o">.</span><span class="n">rasterImage</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">forMap</span><span class="p">(</span><span class="n">map</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withName</span><span class="p">(</span><span class="s">"rasterLayer"</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">();</span>
</code></pre>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RasterDataSourceC7context13configurationAcA10MapContextC_AA0bcD13ConfigurationVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(context:configuration:)"></a>
<a class="token" href="#/s:7heresdk16RasterDataSourceC7context13configurationAcA10MapContextC_AA0bcD13ConfigurationVtcfc">init(context:<wbr/>configuration:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a RasterDataSource instance with the provided data source configuration.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">context</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcontext">MapContext</a></span><span class="p">,</span> <span class="nv">configuration</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-rasterdatasourceconfiguration">RasterDataSourceConfiguration</a></span><span class="p">)</span></code></pre>
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
<p>The map context to associate the data source with.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>configuration</em>
</code>
</td>
<td>
<div>
<p>The data source configuration object to use.</p>
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
<a name="/s:7heresdk16RasterDataSourceC7context13configuration8delegateAcA10MapContextC_AA0bcD13ConfigurationVAA0bcD8Delegate_ptcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(context:configuration:delegate:)"></a>
<a class="token" href="#/s:7heresdk16RasterDataSourceC7context13configuration8delegateAcA10MapContextC_AA0bcD13ConfigurationVAA0bcD8Delegate_ptcfc">init(context:<wbr/>configuration:<wbr/>delegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a RasterDataSource instance with the provided data source configuration and
registers a delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">context</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcontext">MapContext</a></span><span class="p">,</span> <span class="nv">configuration</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-rasterdatasourceconfiguration">RasterDataSourceConfiguration</a></span><span class="p">,</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-rasterdatasourcedelegate">RasterDataSourceDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The map context to associate the data source with.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>configuration</em>
</code>
</td>
<td>
<div>
<p>The data source configuration object to use.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The initial delegate to be registered for receiving state notifications.
Due to the asynchronous nature of the data source initialization, the delegates
registered later might miss some notifications. This delegate is guaranteed to
receive all notifications.</p>
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
<a name="/s:7heresdk16RasterDataSourceC7context4name04tileD0AcA10MapContextC_SSAA0b4TileD0_ptcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(context:name:tileSource:)"></a>
<a class="token" href="#/s:7heresdk16RasterDataSourceC7context4name04tileD0AcA10MapContextC_SSAA0b4TileD0_ptcfc">init(context:<wbr/>name:<wbr/>tileSource:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a RasterDataSource instance with the provided raster tile source.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">context</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcontext">MapContext</a></span><span class="p">,</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">tileSource</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-rastertilesource">RasterTileSource</a></span><span class="p">)</span></code></pre>
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
<p>The map context to associate the data source with.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>name</em>
</code>
</td>
<td>
<div>
<p>The unique name of the data source.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>tileSource</em>
</code>
</td>
<td>
<div>
<p>The raster tile source.</p>
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
<a name="/s:7heresdk16RasterDataSourceC7context4name04tileD08delegateAcA10MapContextC_SSAA0b4TileD0_pAA0bcD8Delegate_ptcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(context:name:tileSource:delegate:)"></a>
<a class="token" href="#/s:7heresdk16RasterDataSourceC7context4name04tileD08delegateAcA10MapContextC_SSAA0b4TileD0_pAA0bcD8Delegate_ptcfc">init(context:<wbr/>name:<wbr/>tileSource:<wbr/>delegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a RasterDataSource instance with the provided raster tile source and registers
a delegate.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">context</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcontext">MapContext</a></span><span class="p">,</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">tileSource</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-rastertilesource">RasterTileSource</a></span><span class="p">,</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-rasterdatasourcedelegate">RasterDataSourceDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The map context to associate the data source with.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>name</em>
</code>
</td>
<td>
<div>
<p>The unique name of the data source.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>tileSource</em>
</code>
</td>
<td>
<div>
<p>The raster tile source.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The initial delegate to be registered for receiving state notifications.
Due to the asynchronous nature of the data source initialization, the delegates
registered later might miss some notifications. This delegate is guaranteed to
receive all notifications.</p>
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
<a name="/s:7heresdk16RasterDataSourceC19changeConfigurationyyAA0bcdF6UpdateVF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/changeConfiguration(_:)"></a>
<a class="token" href="#/s:7heresdk16RasterDataSourceC19changeConfigurationyyAA0bcdF6UpdateVF">changeConfiguration(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Applies the configuration update to the data source.
An example for a configuration update is the update
to a new bearer token for authentication.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">changeConfiguration</span><span class="p">(</span><span class="n">_</span> <span class="nv">configuration</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-rasterdatasourceconfigurationupdate">RasterDataSourceConfigurationUpdate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>configuration</em>
</code>
</td>
<td>
<div>
<p>The data source configuration update to apply.</p>
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
<a name="/s:7heresdk16RasterDataSourceC11addDelegateyyAA0bcdF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk16RasterDataSourceC11addDelegateyyAA0bcdF0_pF">addDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Add delegate for receiving state notifications. The new delegate is
appended to the set of data source delegates as a strong reference and will receive only
the notifications occurring after the registration. Caller is responsible for releasing
the strong reference by calling <code><a href="../Classes/RasterDataSource.html#/s:7heresdk16RasterDataSourceC14removeDelegateyyAA0bcdF0_pF">RasterDataSource.removeDelegate(...)</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">listener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-rasterdatasourcedelegate">RasterDataSourceDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>listener</em>
</code>
</td>
<td>
<div>
<p>Delegate to be added for receiving state notifications.</p>
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
<a name="/s:7heresdk16RasterDataSourceC14removeDelegateyyAA0bcdF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk16RasterDataSourceC14removeDelegateyyAA0bcdF0_pF">removeDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Remove a delegate from receiving state notifications.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">listener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-rasterdatasourcedelegate">RasterDataSourceDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>listener</em>
</code>
</td>
<td>
<div>
<p>Delegate to be removed from receiving state notifications.</p>
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
<a name="/s:7heresdk16RasterDataSourceC15removeDelegatesyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeDelegates()"></a>
<a class="token" href="#/s:7heresdk16RasterDataSourceC15removeDelegatesyyF">removeDelegates()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Remove all delegates from receiving state notifications.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeDelegates</span><span class="p">()</span></code></pre>
</div>
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

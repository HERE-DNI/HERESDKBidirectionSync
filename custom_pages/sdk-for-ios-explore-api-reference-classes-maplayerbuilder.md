---
title: "MapLayerBuilder"
slug: "sdk-for-ios-explore-api-reference-classes-maplayerbuilder"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapLayerBuilder"></a>
<a title="MapLayerBuilder Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

        MapLayerBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapLayerBuilder</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapLayerBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayerBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayerBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>MapLayerBuilder is used to add layers to a map to visualise a dataset in a
programmatic way without defining it upfront in the configuration files.</p>
<p>For example, after loading a scene configuration file, the renderer is setup to draw layers in the
following order:</p>
<ul>
<li>background</li>
<li>water</li>
<li>roads:outline</li>
<li>roads</li>
<li>labels</li>
</ul>
<p>Rendering order of elements in
a single map layer can be controlled with categories. Layer names are unique, and category names have
to be unique within a layer. The layer’s default, main category is unnamed.</p>
<p>The concept of ‘category’ is tightly linked to styling. The idea behind category is that
one should be able to style separately elements in a map layer. Take, for instance, roads.
If one wants to style separately the bridges it will create a category ‘bridges’ and style
it accordingly in the style file. If the user does not intend to or cannot style elements of
the layer differently then it should opt for a layer with only the default category (e.g.
for a raster layer, only the default category makes sense, since the layer has no other
stylable elements apart from the raster image).</p>
<p>A new layer called ‘zone’ and its category ‘background’ can be added dynamically so that the
rendering order gets modified in the following way:</p>
<ul>
<li>background</li>
<li>water</li>
<li>zone:background</li>
<li>zone</li>
<li>roads:outline</li>
<li>roads</li>
<li>labels</li>
</ul>
<p>This could be achieved with the help of the MapLayerPriorityBuilder and the MapLayerBuilder as in the
following example:</p>
<pre class="highlight swift"><code>  <span class="k">let</span> <span class="nv">layerPriority</span> <span class="o">=</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">()</span>
     <span class="o">.</span><span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"water"</span><span class="p">)</span> <span class="c1">// places main category after 'water'</span>
     <span class="o">.</span><span class="nf">withCategory</span><span class="p">(</span><span class="s">"background"</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"water"</span><span class="p">)</span> <span class="c1">// places 'background' category after 'water' and before the</span>
                                         <span class="c1">// layer's main category.</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">();</span>

  <span class="k">let</span> <span class="nv">layer</span> <span class="o">=</span> <span class="kt">MapLayerBuilder</span><span class="p">()</span>
     <span class="o">.</span><span class="nf">withDataSource</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"DataSourceName"</span><span class="p">,</span> <span class="nv">contentType</span><span class="p">:</span> <span class="kt">MapContentType</span><span class="o">.</span><span class="n">line</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">forMap</span><span class="p">(</span><span class="n">map</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withName</span><span class="p">(</span><span class="s">"zone"</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withPriority</span><span class="p">(</span><span class="n">layerPriority</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">();</span>
</code></pre>
<p>In case no layer priority or an empty one is provided, or if a reference layer-category pair is not
present in the rendering order, the layer is going to be rendered last with respect to the rendering
order at the time of its creation.</p>
<p>Due to current limitations, the MapLayerPriority assignment is not implemented for point map layers.
All labels will be rendered within the “labels” layer, defined in the scene configuration file.
By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed.
The following categories can be used to have a different behaviour:</p>
<ul>
<li>‘custom-labels’ A label should be rendered first, is allowed to overlap with other labels of
the same category and block map labels.</li>
<li>‘custom-labels-no-self-overlap’ A label should be rendered after ‘custom-labels’, is not allowed
to overlap with other labels of the same categoty and block map labels.</li>
<li>‘custom-labels-overlap-all’ A label should be rendered last, is allowed to overlap all
predefined categories, also map labels.
These categories are configured accordingly in the basic map
scene configurations.
Category assignment to features can be done in the style based on data attributes. The category
assignment can be done for all types of content: point, line, polygon.</li>
</ul>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderC18InstantiationErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InstantiationError"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderC18InstantiationErrora">InstantiationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Thrown when failing to build a <code><a href="sdk-for-ios-explore-api-reference-classes-maplayer">MapLayer</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">InstantiationError</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-maplayerbuilder-instantiationerrordetails">InstantiationErrorDetails</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of the layer builder interface.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderC22InstantiationErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderC22InstantiationErrorCodeO">InstantiationErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes a reason for failing to build a <code><a href="sdk-for-ios-explore-api-reference-classes-maplayer">MapLayer</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-maplayerbuilder-instantiationerrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderC25InstantiationErrorDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/InstantiationErrorDetails"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderC25InstantiationErrorDetailsV">InstantiationErrorDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes the reason for failing to build a <code><a href="sdk-for-ios-explore-api-reference-classes-maplayer">MapLayer</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-maplayerbuilder-instantiationerrordetails">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">InstantiationErrorDetails</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-maplayerbuilder">MapLayerBuilder</a></span><span class="o">.</span><span class="kt">InstantiationErrorDetails</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderC8withNameyACSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withName(_:)"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderC8withNameyACSSF">withName(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures builder to use the given name as a layer name.
The name is a mandatory layer creation parameter.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withName</span><span class="p">(</span><span class="n">_</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>name</em>
</code>
</td>
<td>
<div>
<p>Name of the layer. Must be unique.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderC14withDataSource5named11contentTypeACSS_AA0b7ContentJ0OtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withDataSource(named:contentType:)"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderC14withDataSource5named11contentTypeACSS_AA0b7ContentJ0OtF">withDataSource(named:<wbr/>contentType:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to use a data source with the given name as the source
of data for the layer.
The datasource name and content type are mandatory layer creation parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withDataSource</span><span class="p">(</span><span class="n">named</span> <span class="nv">dataSourceName</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">contentType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-mapcontenttype">MapContentType</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerBuilder</span></code></pre>
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
<p>Name of the data source.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>contentType</em>
</code>
</td>
<td>
<div>
<p>The renderable content type supplied by the data source.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderC9withStyleyAcA0F0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withStyle(_:)"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderC9withStyleyAcA0F0CF">withStyle(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to use a style.
Providing a style during layer creation is not mandatory. The style can also be set/updated after the layer creation.
For more details see Custom Layer Style Reference in the documentation.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withStyle</span><span class="p">(</span><span class="n">_</span> <span class="nv">style</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-style">Style</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>style</em>
</code>
</td>
<td>
<div>
<p>Style for the layer.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderC03forB0yAcA04HereB0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/forMap(_:)"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderC03forB0yAcA04HereB0CF">forMap(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to display a layer in the given map.
The map is a mandatory layer creation parameter.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">forMap</span><span class="p">(</span><span class="n">_</span> <span class="nv">targetMap</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-heremap">HereMap</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>targetMap</em>
</code>
</td>
<td>
<div>
<p>The map.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderC12withPriorityyAcA0bcF0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withPriority(_:)"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderC12withPriorityyAcA0bcF0CF">withPriority(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to set the MapLayerPriority to be used by the layer.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withPriority</span><span class="p">(</span><span class="n">_</span> <span class="nv">priority</span><span class="p">:</span> <span class="kt"><a href="../Maps.html#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>priority</em>
</code>
</td>
<td>
<div>
<p>MapLayerPriority which should be applied to the layer.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderC19withVisibilityRangeyAcA0bcfG0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withVisibilityRange(_:)"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderC19withVisibilityRangeyAcA0bcfG0VF">withVisibilityRange(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to set the layer visible in the given zoom levels range.
Values outside the map zoom level range (0, 24) will be ignored.
Providing the visibility range is optional. If not provided, the layer will be visible
on all zoom levels.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withVisibilityRange</span><span class="p">(</span><span class="n">_</span> <span class="nv">visibilityRange</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-maplayervisibilityrange">MapLayerVisibilityRange</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>visibilityRange</em>
</code>
</td>
<td>
<div>
<p>Visibility range which should be applied to the layer.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderC04withB29MeasureDependentStorageLevelsyAcA0bcbfghI0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withMapMeasureDependentStorageLevels(_:)"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderC04withB29MeasureDependentStorageLevelsyAcA0bcbfghI0CF">withMapMeasureDependentStorageLevels(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Applies a mapping from the map measure to the storage level. This mapping is used by the layer to request data
for the specified storage level corresponding to the map measure from the datasource.
This can be used for example to fine-tune the resolution of raster layers.
Note: When the map camera is significantly tilted, the storage level is further reduced for data towards the horizon.
Note: Mappings that request higher storage levels will lead to an increased number
of requests to the raster tile service.
Providing the map measure to storage level mapping is optional. If not provided, the default mapping will
use a storage level that is for raster layers one and for others three levels lower than the zoom level,
corresponding to an offset of -1 and -3.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withMapMeasureDependentStorageLevels</span><span class="p">(</span><span class="n">_</span> <span class="nv">mapLayerMapMeasureDependentStorageLevels</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-maplayermapmeasuredependentstoragelevels">MapLayerMapMeasureDependentStorageLevels</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapLayerMapMeasureDependentStorageLevels</em>
</code>
</td>
<td>
<div>
<p>The map measure to storage level mapping that should be applied for the layer.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderC16withLoadPriorityyACSdF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withLoadPriority(_:)"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderC16withLoadPriorityyACSdF">withLoadPriority(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to set the layer load priority.
Higher load priority values lead to layer being scheduled for loading before layers with lesser values.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withLoadPriority</span><span class="p">(</span><span class="n">_</span> <span class="nv">loadPriority</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapLayerBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>loadPriority</em>
</code>
</td>
<td>
<div>
<p>Load priority for layer.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderC5buildAA0bC0CyKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderC5buildAA0bC0CyKF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs, registers and configures a new map layer showing specified content type
according to the configured parameters.
After this call this instance is reset to the initial state. It could be used to build another
map layer, but will not keep any previously configured properties.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapLayerBuilder.html#/s:7heresdk15MapLayerBuilderC18InstantiationErrora">MapLayerBuilder.InstantiationError</a></code> Indicates an instantiation issue.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">build</span><span class="p">()</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-maplayer">MapLayer</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>A new MapLayer instance.</p>
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

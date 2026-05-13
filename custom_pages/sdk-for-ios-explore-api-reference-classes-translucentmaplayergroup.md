---
title: "Maps / TranslucentMapLayerGroup"
slug: "sdk-for-ios-explore-api-reference-classes-translucentmaplayergroup"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/TranslucentMapLayerGroup"></a>
<a title="TranslucentMapLayerGroup Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TranslucentMapLayerGroup Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TranslucentMapLayerGroup</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TranslucentMapLayerGroup</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TranslucentMapLayerGroup</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TranslucentMapLayerGroup</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A translucent layer group that can be the target for <code><a href="../Classes/MapLayerPriorityBuilder.html#/s:7heresdk23MapLayerPriorityBuilderC7inGroupyACSSF">MapLayerPriorityBuilder.inGroup(...)</a></code>.
Currently, only custom line layers can be added to a translucent layer group.
Custom line layers in a translucent layer group are rendered in an offscreen translucent pass so
that overlapping translucent line geometry is not alpha blended with itself.
At creation, the layer group gets added to a map. The layer group gets removed from the map upon
instance destruction and any layer (categories) still in the group are not rendered anymore,
therefore it is recommended to keep a group alive as long as layers using the group are alive and
in use.</p>
<p>Conceptual example to place line layers into a translucent group:</p>
<pre class="highlight swift"><code> <span class="c1">// Create a translucent group with a unique name and a render priority</span>
 <span class="k">let</span> <span class="nv">groupPriority</span> <span class="o">=</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">()</span><span class="o">.</span><span class="nf">renderedLast</span><span class="p">()</span><span class="o">.</span><span class="nf">build</span><span class="p">()</span>
 <span class="k">let</span> <span class="nv">group</span> <span class="o">=</span> <span class="kt">TranslucentMapLayerGroup</span><span class="p">(</span><span class="nv">name</span><span class="p">:</span> <span class="s">"TranslucentGroupName"</span><span class="p">,</span> <span class="n">map</span><span class="p">,</span> <span class="n">groupPriority</span><span class="p">)</span>

 <span class="c1">// Create a line layer to be rendered as part of the translucent group</span>
 <span class="k">let</span> <span class="nv">lineLayerPriority</span> <span class="o">=</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">()</span>
     <span class="o">.</span><span class="nf">inGroup</span><span class="p">(</span><span class="s">"TranslucentGroupName"</span><span class="p">)</span> <span class="c1">// places the line layer into the group</span>
     <span class="o">.</span><span class="nf">renderedFirst</span><span class="p">()</span>                 <span class="c1">// to be rendered first when the group is rendered</span>
     <span class="o">.</span><span class="nf">withCategory</span><span class="p">(</span><span class="s">"SomeCategory"</span><span class="p">)</span>    <span class="c1">// places the line layer category 'SomeCategory'</span>
     <span class="o">.</span><span class="nf">inGroup</span><span class="p">(</span><span class="s">"TranslucentGroupName"</span><span class="p">)</span> <span class="c1">// into the group</span>
     <span class="o">.</span><span class="nf">renderedLast</span><span class="p">()</span>                  <span class="c1">// to be rendered last when the group is rendered</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">()</span>

 <span class="k">let</span> <span class="nv">lineLayer</span> <span class="o">=</span> <span class="kt">MapLayerBuilder</span><span class="p">()</span>
     <span class="o">.</span><span class="nf">withDataSource</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"DataSourceName"</span><span class="p">,</span> <span class="nv">contentType</span><span class="p">:</span> <span class="kt">MapContentType</span><span class="o">.</span><span class="n">line</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">forMap</span><span class="p">(</span><span class="n">map</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withName</span><span class="p">(</span><span class="s">"LineLayerName"</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withPriority</span><span class="p">(</span><span class="n">lineLayerPriority</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withStyle</span><span class="p">(</span><span class="n">translucentLineStyle</span><span class="p">)</span> <span class="c1">// E.g. "technique": "line" ... "color": "#FFFFFF80"</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">()</span>

 <span class="c1">// Create a second line layer to be rendered as part of the translucent group</span>
 <span class="k">let</span> <span class="nv">secondLineLayerPriority</span> <span class="o">=</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">()</span>
     <span class="o">.</span><span class="nf">inGroup</span><span class="p">(</span><span class="s">"TranslucentGroupName"</span><span class="p">)</span>      <span class="c1">// places the second line layer into the group</span>
     <span class="o">.</span><span class="nf">renderedBeforeLayer</span><span class="p">(</span><span class="s">"LineLayerName"</span><span class="p">)</span> <span class="c1">// to be rendered before first layer</span>
                                           <span class="c1">// when the group is rendered</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">()</span>

 <span class="k">let</span> <span class="nv">secondLineLayer</span> <span class="o">=</span> <span class="kt">MapLayerBuilder</span><span class="p">()</span>
     <span class="o">.</span><span class="nf">withDataSource</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"SecondDataSourceName"</span><span class="p">,</span> <span class="nv">contentType</span><span class="p">:</span> <span class="kt">MapContentType</span><span class="o">.</span><span class="n">line</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">forMap</span><span class="p">(</span><span class="n">map</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withName</span><span class="p">(</span><span class="s">"SecondLineLayerName"</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withPriority</span><span class="p">(</span><span class="n">secondLineLayerPriority</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withStyle</span><span class="p">(</span><span class="n">secondTranslucentLineStyle</span><span class="p">)</span> <span class="c1">// E.g. "technique": "line" ... "color": "#FFFFFF80"</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">()</span>
</code></pre>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24TranslucentMapLayerGroupC18InstantiationErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InstantiationError"></a>
<a class="token" href="#/s:7heresdk24TranslucentMapLayerGroupC18InstantiationErrora">InstantiationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Thrown when failing to build the group.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">InstantiationError</span> <span class="o">=</span> <span class="kt">TranslucentMapLayerGroup</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-translucentmaplayergroup-errordetails">ErrorDetails</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24TranslucentMapLayerGroupC4name01aC0ACSS_AA04HereC0CtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(name:aMap:)"></a>
<a class="token" href="#/s:7heresdk24TranslucentMapLayerGroupC4name01aC0ACSS_AA04HereC0CtKcfc">init(name:<wbr/>aMap:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of the group.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/TranslucentMapLayerGroup.html#/s:7heresdk24TranslucentMapLayerGroupC18InstantiationErrora">TranslucentMapLayerGroup.InstantiationError</a></code> In case of invalid input parameters.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">aMap</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-heremap">HereMap</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<p>Name of the group. Must be unique across <code><a href="sdk-for-ios-explore-api-reference-..-classes-maplayer">MapLayer</a></code> and <code>TranslucentMapLayerGroup</code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>aMap</em>
</code>
</td>
<td>
<div>
<p>The map to attach the group to.</p>
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
<a name="/s:7heresdk24TranslucentMapLayerGroupC4name01aC0_ACSS_AA04HereC0CAA0cD8PriorityCtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(name:aMap:_:)"></a>
<a class="token" href="#/s:7heresdk24TranslucentMapLayerGroupC4name01aC0_ACSS_AA04HereC0CAA0cD8PriorityCtKcfc">init(name:<wbr/>aMap:<wbr/>_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of the group.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<p><code><a href="../Classes/TranslucentMapLayerGroup.html#/s:7heresdk24TranslucentMapLayerGroupC18InstantiationErrora">TranslucentMapLayerGroup.InstantiationError</a></code> In case of invalid input parameters.</p>
</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">aMap</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-heremap">HereMap</a></span><span class="p">,</span> <span class="n">_</span> <span class="nv">priority</span><span class="p">:</span> <span class="kt"><a href="../Maps.html#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<p>Name of the group. Must be unique across <code><a href="sdk-for-ios-explore-api-reference-..-classes-maplayer">MapLayer</a></code> and <code>TranslucentMapLayerGroup</code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>aMap</em>
</code>
</td>
<td>
<div>
<p>The map to attach the group to.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>priority</em>
</code>
</td>
<td>
<div>
<p>The <code><a href="../Maps.html#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a></code> which should be applied to position the group.
The <code><a href="../Maps.html#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a></code> must contain only one priority and this priority must have no
category and no group, i.e. <code><a href="../Classes/MapLayerPriorityBuilder.html#/s:7heresdk23MapLayerPriorityBuilderC7inGroupyACSSF">MapLayerPriorityBuilder.inGroup(...)</a></code> and
<code><a href="../Classes/MapLayerPriorityBuilder.html#/s:7heresdk23MapLayerPriorityBuilderC12withCategoryyACSSF">MapLayerPriorityBuilder.withCategory(...)</a></code> should not be used when building the
<code><a href="../Maps.html#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a></code>.
Example:</p>
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
<a name="/s:7heresdk24TranslucentMapLayerGroupC9ErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ErrorCode"></a>
<a class="token" href="#/s:7heresdk24TranslucentMapLayerGroupC9ErrorCodeO">ErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Error codes for creating the group.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-translucentmaplayergroup-errorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24TranslucentMapLayerGroupC12ErrorDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ErrorDetails"></a>
<a class="token" href="#/s:7heresdk24TranslucentMapLayerGroupC12ErrorDetailsV">ErrorDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes the reason for failing to create the group.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-translucentmaplayergroup-errordetails">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ErrorDetails</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-translucentmaplayergroup">TranslucentMapLayerGroup</a></span><span class="o">.</span><span class="kt">ErrorDetails</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24TranslucentMapLayerGroupC11setPriorityyyAA0cdG0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setPriority(_:)"></a>
<a class="token" href="#/s:7heresdk24TranslucentMapLayerGroupC11setPriorityyyAA0cdG0CF">setPriority(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the render priority for the layer group which replaces any previously defined priority.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setPriority</span><span class="p">(</span><span class="n">_</span> <span class="nv">priority</span><span class="p">:</span> <span class="kt"><a href="../Maps.html#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a></span><span class="p">)</span></code></pre>
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
<p>The priority to position the group.
The <code><a href="../Maps.html#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a></code> must contain only one priority and this priority must have no
category and no group, i.e. <code><a href="../Classes/MapLayerPriorityBuilder.html#/s:7heresdk23MapLayerPriorityBuilderC7inGroupyACSSF">MapLayerPriorityBuilder.inGroup(...)</a></code> and
<code><a href="../Classes/MapLayerPriorityBuilder.html#/s:7heresdk23MapLayerPriorityBuilderC12withCategoryyACSSF">MapLayerPriorityBuilder.withCategory(...)</a></code> should not be used when building the
<code><a href="../Maps.html#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a></code>.
Example:</p>
<p>new MapLayerPriorityBuilder().renderedAfterLayer(“water”).build()
<code>MapLayerPriorityBuilder().renderedAfterLayer(named: "water").build()</code></p>
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

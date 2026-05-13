---
title: "TranslucentMapLayerGroup Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-translucentmaplayergroup"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TranslucentMapLayerGroup.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/TranslucentMapLayerGroup"></a>
<a title="TranslucentMapLayerGroup Class Reference"></a>
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
        TranslucentMapLayerGroup Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class TranslucentMapLayerGroup</code></pre>
<pre><code>extension TranslucentMapLayerGroup: NativeBase</code></pre>
<pre><code>extension TranslucentMapLayerGroup: Hashable</code></pre>
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
<pre><code>// Create a translucent group with a unique name and a render priority
let groupPriority = MapLayerPriorityBuilder().renderedLast().build()
let group = TranslucentMapLayerGroup(name: "TranslucentGroupName", map, groupPriority)
// Create a line layer to be rendered as part of the translucent group
let lineLayerPriority = MapLayerPriorityBuilder()
.inGroup("TranslucentGroupName") // places the line layer into the group
.renderedFirst() // to be rendered first when the group is rendered
.withCategory("SomeCategory") // places the line layer category 'SomeCategory'
.inGroup("TranslucentGroupName") // into the group
.renderedLast() // to be rendered last when the group is rendered
.build()
let lineLayer = MapLayerBuilder()
.withDataSource(named: "DataSourceName", contentType: MapContentType.line)
.forMap(map)
.withName("LineLayerName")
.withPriority(lineLayerPriority)
.withStyle(translucentLineStyle) // E.g. "technique": "line" ... "color": "#FFFFFF80"
.build()
// Create a second line layer to be rendered as part of the translucent group
let secondLineLayerPriority = MapLayerPriorityBuilder()
.inGroup("TranslucentGroupName") // places the second line layer into the group
.renderedBeforeLayer("LineLayerName") // to be rendered before first layer
// when the group is rendered
.build()
let secondLineLayer = MapLayerBuilder()
.withDataSource(named: "SecondDataSourceName", contentType: MapContentType.line)
.forMap(map)
.withName("SecondLineLayerName")
.withPriority(secondLineLayerPriority)
.withStyle(secondTranslucentLineStyle) // E.g. "technique": "line" ... "color": "#FFFFFF80"
.build()</code></pre>
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
<pre><code>public typealias InstantiationError = TranslucentMapLayerGroup.ErrorDetails</code></pre>
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
<pre><code>public init(name: String, aMap: HereMap) throws</code></pre>
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
<pre><code>public init(name: String, aMap: HereMap, _ priority: MapLayerPriority) throws</code></pre>
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
<pre><code>public enum ErrorCode : UInt32, CaseIterable, Codable</code></pre>
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
<pre><code>public struct ErrorDetails</code></pre>
<pre><code>extension TranslucentMapLayerGroup.ErrorDetails : Error</code></pre>
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
<pre><code>public func setPriority(_ priority: MapLayerPriority)</code></pre>
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



</div>
`
}</HTMLBlock>

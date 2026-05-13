---
title: "DataAttributesBuilder Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-dataattributesbuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- DataAttributesBuilder.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/DataAttributesBuilder"></a>
<a title="DataAttributesBuilder Class Reference"></a>
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
        DataAttributesBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class DataAttributesBuilder</code></pre>
<pre><code>extension DataAttributesBuilder: NativeBase</code></pre>
<pre><code>extension DataAttributesBuilder: Hashable</code></pre>
</div>
</div>
<p>Data attributes collection builder.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21DataAttributesBuilderCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk21DataAttributesBuilderCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a data attributes builder instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init()</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21DataAttributesBuilderC4with4name5valueACSS_SStF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/with(name:value:)"></a>
<a class="token" href="#/s:7heresdk21DataAttributesBuilderC4with4name5valueACSS_SStF">with(name:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to add the given attribute.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func with(name: String, value: String) -&gt; DataAttributesBuilder</code></pre>
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
<p>Attribute name.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Attribute value.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This data attributes builder instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21DataAttributesBuilderC4with4name5valueACSS_s5Int64VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/with(name:value:)"></a>
<a class="token" href="#/s:7heresdk21DataAttributesBuilderC4with4name5valueACSS_s5Int64VtF">with(name:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to add the given attribute.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func with(name: String, value: Int64) -&gt; DataAttributesBuilder</code></pre>
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
<p>Attribute name.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Attribute value.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This data attributes builder instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21DataAttributesBuilderC4with4name5valueACSS_SftF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/with(name:value:)"></a>
<a class="token" href="#/s:7heresdk21DataAttributesBuilderC4with4name5valueACSS_SftF">with(name:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to add the given attribute.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func with(name: String, value: Float) -&gt; DataAttributesBuilder</code></pre>
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
<p>Attribute name.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Attribute value.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This data attributes builder instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21DataAttributesBuilderC4with4name5valueACSS_SdtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/with(name:value:)"></a>
<a class="token" href="#/s:7heresdk21DataAttributesBuilderC4with4name5valueACSS_SdtF">with(name:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to add the given attribute.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func with(name: String, value: Double) -&gt; DataAttributesBuilder</code></pre>
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
<p>Attribute name.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Attribute value.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This data attributes builder instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21DataAttributesBuilderC4with4name5valueACSS_SbtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/with(name:value:)"></a>
<a class="token" href="#/s:7heresdk21DataAttributesBuilderC4with4name5valueACSS_SbtF">with(name:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to add the given attribute.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func with(name: String, value: Bool) -&gt; DataAttributesBuilder</code></pre>
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
<p>Attribute name.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Attribute value.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This data attributes builder instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21DataAttributesBuilderC4with4name5valueACSS_AA0B14AttributeValueCtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/with(name:value:)"></a>
<a class="token" href="#/s:7heresdk21DataAttributesBuilderC4with4name5valueACSS_AA0B14AttributeValueCtF">with(name:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder to add the given attribute.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func with(name: String, value: DataAttributeValue) -&gt; DataAttributesBuilder</code></pre>
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
<p>Attribute name.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Attribute value.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This data attributes builder instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21DataAttributesBuilderC5buildAA0bC0CyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk21DataAttributesBuilderC5buildAA0bC0CyF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builds instance of DataAttributes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func build() -&gt; DataAttributes</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Instance of the data attributes created with the given attributes.</p>
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

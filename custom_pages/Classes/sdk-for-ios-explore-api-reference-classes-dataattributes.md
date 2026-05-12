---
title: "DataAttributes Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-dataattributes"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- DataAttributes.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/DataAttributes"></a>
<a title="DataAttributes Class Reference"></a>
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
<a href="../Maps.html">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        DataAttributes Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class DataAttributes : DataAttributesBase</code></pre>
<pre><code>extension DataAttributes: NativeBase</code></pre>
<pre><code>extension DataAttributes: Hashable</code></pre>
</div>
</div>
<p>Data attributes collection.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DataAttributesC17getAttributeNamesSaySSGyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getAttributeNames()"></a>
<a class="token" href="#/s:7heresdk14DataAttributesC17getAttributeNamesSaySSGyF">getAttributeNames()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a list of attribute names.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getAttributeNames() -&gt; [String]</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The list of attribute names.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DataAttributesC12getValueTypeyAA0b9AttributeE0C0eF0OSgSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getValueType(_:)"></a>
<a class="token" href="#/s:7heresdk14DataAttributesC12getValueTypeyAA0b9AttributeE0C0eF0OSgSSF">getValueType(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the value type of an attribute or <code>nil</code> if it is not contained.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getValueType(_ name: String) -&gt; DataAttributeValue.ValueType?</code></pre>
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
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value type or <code>nil</code> if it is not contained.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DataAttributesC11getAsStringySSSgSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getAsString(_:)"></a>
<a class="token" href="#/s:7heresdk14DataAttributesC11getAsStringySSSgSSF">getAsString(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the value of an attribute as a string or <code>nil</code> if it is not contained.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getAsString(_ name: String) -&gt; String?</code></pre>
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
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DataAttributesC9getStringySSSgSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getString(_:)"></a>
<a class="token" href="#/s:7heresdk14DataAttributesC9getStringySSSgSSF">getString(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the value of a string attribute or <code>nil</code> if it is not contained or the type doesn’t match.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getString(_ name: String) -&gt; String?</code></pre>
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
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DataAttributesC8getInt64ys0E0VSgSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getInt64(_:)"></a>
<a class="token" href="#/s:7heresdk14DataAttributesC8getInt64ys0E0VSgSSF">getInt64(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the value of a 64-bits integer attribute or <code>nil</code> if it is not contained or the type doesn’t match.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getInt64(_ name: String) -&gt; Int64?</code></pre>
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
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DataAttributesC8getFloatySfSgSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getFloat(_:)"></a>
<a class="token" href="#/s:7heresdk14DataAttributesC8getFloatySfSgSSF">getFloat(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the value of a single precision floating decimal attribute or <code>nil</code> if it is not contained or the type doesn’t match.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getFloat(_ name: String) -&gt; Float?</code></pre>
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
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DataAttributesC9getDoubleySdSgSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getDouble(_:)"></a>
<a class="token" href="#/s:7heresdk14DataAttributesC9getDoubleySdSgSSF">getDouble(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the value of a double precision floating decimal attribute or <code>nil</code> if it is not contained or the type doesn’t match.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getDouble(_ name: String) -&gt; Double?</code></pre>
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
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DataAttributesC10getBooleanySbSgSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getBoolean(_:)"></a>
<a class="token" href="#/s:7heresdk14DataAttributesC10getBooleanySbSgSSF">getBoolean(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the value of a boolean attribute or <code>nil</code> if it is not contained or the type doesn’t match.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getBoolean(_ name: String) -&gt; Bool?</code></pre>
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
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DataAttributesC8getValueyAA0b9AttributeE0CSgSSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getValue(_:)"></a>
<a class="token" href="#/s:7heresdk14DataAttributesC8getValueyAA0b9AttributeE0CSgSSF">getValue(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the DataAttributeValue or <code>nil</code> if it is not contained.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getValue(_ name: String) -&gt; DataAttributeValue?</code></pre>
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
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Attribute value.</p>
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

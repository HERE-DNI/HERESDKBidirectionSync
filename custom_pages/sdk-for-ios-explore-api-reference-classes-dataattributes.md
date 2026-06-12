---
title: "DataAttributes"
slug: "sdk-for-ios-explore-api-reference-classes-dataattributes"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/DataAttributes"></a>
<a title="DataAttributes Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

        DataAttributes Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>DataAttributes</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">DataAttributes</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-dataattributesbase">DataAttributesBase</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DataAttributes</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DataAttributes</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getAttributeNames</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getValueType</span><span class="p">(</span><span class="n">_</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-dataattributevalue">DataAttributeValue</a></span><span class="o">.</span><span class="kt">ValueType</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getAsString</span><span class="p">(</span><span class="n">_</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">String</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getString</span><span class="p">(</span><span class="n">_</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">String</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getInt64</span><span class="p">(</span><span class="n">_</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Int64</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getFloat</span><span class="p">(</span><span class="n">_</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Float</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getDouble</span><span class="p">(</span><span class="n">_</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getBoolean</span><span class="p">(</span><span class="n">_</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getValue</span><span class="p">(</span><span class="n">_</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-dataattributevalue">DataAttributeValue</a></span><span class="p">?</span></code></pre>
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
</body>
</html>

`
} </HTMLBlock>

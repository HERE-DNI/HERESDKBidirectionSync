---
title: "Metadata"
slug: "sdk-for-ios-explore-classes-metadata"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/Metadata"></a>
<a title="Metadata Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-index">heresdk</a>

<a href="sdk-for-ios-explore-core">Core</a>

        Metadata Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Metadata</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Metadata</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Metadata</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Metadata</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Holds metadata on behalf of a map item.
An instance of this class can contain metadata items of varying types, such as
String, Integer, Double, GeoCoordinates etc. and can also hold arbitrary metadata
types by the use of the CustomMetadataValue protocol.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MetadataCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk8MetadataCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of this class.</p>
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
<a name="/s:7heresdk8MetadataC14getCustomValue3keyAA0dbE0_pSgSS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getCustomValue(key:)"></a>
<a class="token" href="#/s:7heresdk8MetadataC14getCustomValue3keyAA0dbE0_pSgSS_tF">getCustomValue(key:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Obtains an instance of the CustomMetadataValue class associated with a given key.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getCustomValue</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-protocols-custommetadatavalue">CustomMetadataValue</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>The name of the key for which to obtain the value.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The value associated with the key.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MetadataC9getDouble3keySdSgSS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getDouble(key:)"></a>
<a class="token" href="#/s:7heresdk8MetadataC9getDouble3keySdSgSS_tF">getDouble(key:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Obtains a Double value associated with a given key.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getDouble</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>The name of the key for which to obtain the value.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The value associated with the key.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MetadataC17getGeoCoordinates3keyAA0dE0VSgSS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getGeoCoordinates(key:)"></a>
<a class="token" href="#/s:7heresdk8MetadataC17getGeoCoordinates3keyAA0dE0VSgSS_tF">getGeoCoordinates(key:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Obtains a GeoCoordinates value associated with a given key.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getGeoCoordinates</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>The name of the key for which to obtain the value.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The value associated with the key.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MetadataC10getInteger3keys5Int32VSgSS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getInteger(key:)"></a>
<a class="token" href="#/s:7heresdk8MetadataC10getInteger3keys5Int32VSgSS_tF">getInteger(key:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Obtains an Integer value associated with a given key.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getInteger</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>The name of the key for which to obtain the value.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The value associated with the key.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MetadataC9getString3keySSSgSS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getString(key:)"></a>
<a class="token" href="#/s:7heresdk8MetadataC9getString3keySSSgSS_tF">getString(key:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Obtains a String value associated with a given key.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getString</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>The name of the key for which to obtain the value.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The value associated with the key.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MetadataC7getType3keyAA0bD0OSgSS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getType(key:)"></a>
<a class="token" href="#/s:7heresdk8MetadataC7getType3keyAA0bD0OSgSS_tF">getType(key:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Determines the type of a metadata value.
If the type of a metadata value associated with a key is not known, this
method will enable the type to be queried, in order to know which get method
to call. i.e. getDouble(), getInteger() etc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getType</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-enums-metadatatype">MetadataType</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>The name of the key for which to obtain the type.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>An enumeration describing the type of the value associated with the key.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MetadataC11removeValue3keyySS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeValue(key:)"></a>
<a class="token" href="#/s:7heresdk8MetadataC11removeValue3keyySS_tF">removeValue(key:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a metadata key and its associated value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeValue</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>The name of the key to be removed.</p>
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
<a name="/s:7heresdk8MetadataC14setCustomValue3key5valueySS_AA0dbE0_ptF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setCustomValue(key:value:)"></a>
<a class="token" href="#/s:7heresdk8MetadataC14setCustomValue3key5valueySS_AA0dbE0_ptF">setCustomValue(key:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a key:value pair, where the value is a type derived from CustomMetadataValue.
If the given key already exists, its value will be replaced by the new one.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setCustomValue</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-protocols-custommetadatavalue">CustomMetadataValue</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>The name of the key to be created or replaced.</p>
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
<p>The value to be assigned to the key.</p>
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
<a name="/s:7heresdk8MetadataC9setDouble3key5valueySS_SdtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setDouble(key:value:)"></a>
<a class="token" href="#/s:7heresdk8MetadataC9setDouble3key5valueySS_SdtF">setDouble(key:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a key:value pair, where the value is of type Double.
If the given key already exists, its value will be replaced by the new one.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setDouble</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>The name of the key to be created or replaced.</p>
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
<p>The value to be assigned to the key.</p>
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
<a name="/s:7heresdk8MetadataC17setGeoCoordinates3key5valueySS_AA0dE0VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setGeoCoordinates(key:value:)"></a>
<a class="token" href="#/s:7heresdk8MetadataC17setGeoCoordinates3key5valueySS_AA0dE0VtF">setGeoCoordinates(key:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a key:value pair, where the value is of type GeoCoordinates.
If the given key already exists, its value will be replaced by the new one.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setGeoCoordinates</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>The name of the key to be created or replaced.</p>
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
<p>The value to be assigned to the key.</p>
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
<a name="/s:7heresdk8MetadataC10setInteger3key5valueySS_s5Int32VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setInteger(key:value:)"></a>
<a class="token" href="#/s:7heresdk8MetadataC10setInteger3key5valueySS_s5Int32VtF">setInteger(key:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a key:value pair, where the value is of type Integer.
If the given key already exists, its value will be replaced by the new one.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setInteger</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>The name of the key to be created or replaced.</p>
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
<p>The value to be assigned to the key.</p>
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
<a name="/s:7heresdk8MetadataC9setString3key5valueySS_SStF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setString(key:value:)"></a>
<a class="token" href="#/s:7heresdk8MetadataC9setString3key5valueySS_SStF">setString(key:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a key:value pair, where the value is of type String.
If the given key already exists, its value will be replaced by the new one.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setString</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>The name of the key to be created or replaced.</p>
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
<p>The value to be assigned to the key.</p>
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
} </HTMLBlock>

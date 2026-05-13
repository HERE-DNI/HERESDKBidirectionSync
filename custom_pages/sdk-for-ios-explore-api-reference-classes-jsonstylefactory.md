---
title: "Maps / JsonStyleFactory"
slug: "sdk-for-ios-explore-api-reference-classes-jsonstylefactory"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/JsonStyleFactory"></a>
<a title="JsonStyleFactory Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        JsonStyleFactory Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>JsonStyleFactory</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">JsonStyleFactory</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">JsonStyleFactory</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">JsonStyleFactory</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A factory of <code><a href="sdk-for-ios-explore-api-reference-..-classes-style">Style</a></code> objects from styles defined in JSON format.
For more details see Custom Layer Style Reference in the documentation.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16JsonStyleFactoryC18InstantiationErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InstantiationError"></a>
<a class="token" href="#/s:7heresdk16JsonStyleFactoryC18InstantiationErrora">InstantiationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Thrown when failing to create a <code><a href="sdk-for-ios-explore-api-reference-..-classes-style">Style</a></code> from a JSON source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">InstantiationError</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-jsonstylefactory-instantiationerrordetails">InstantiationErrorDetails</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16JsonStyleFactoryC22InstantiationErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a class="token" href="#/s:7heresdk16JsonStyleFactoryC22InstantiationErrorCodeO">InstantiationErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes reasons for failing to create a <code><a href="sdk-for-ios-explore-api-reference-..-classes-style">Style</a></code> from a JSON source.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-jsonstylefactory-instantiationerrorcode">See more</a>
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
<a name="/s:7heresdk16JsonStyleFactoryC25InstantiationErrorDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/InstantiationErrorDetails"></a>
<a class="token" href="#/s:7heresdk16JsonStyleFactoryC25InstantiationErrorDetailsV">InstantiationErrorDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes the reason for failing to create a <code><a href="sdk-for-ios-explore-api-reference-..-classes-style">Style</a></code> from a JSON source.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-jsonstylefactory-instantiationerrordetails">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">InstantiationErrorDetails</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-jsonstylefactory">JsonStyleFactory</a></span><span class="o">.</span><span class="kt">InstantiationErrorDetails</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16JsonStyleFactoryC16createFromStringyAA0C0CSSKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/createFromString(_:)"></a>
<a class="token" href="#/s:7heresdk16JsonStyleFactoryC16createFromStringyAA0C0CSSKFZ">createFromString(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of Style from a JSON string.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/JsonStyleFactory.html#/s:7heresdk16JsonStyleFactoryC18InstantiationErrora">JsonStyleFactory.InstantiationError</a></code> Indicates failure to create <code><a href="sdk-for-ios-explore-api-reference-..-classes-style">Style</a></code> from JSON string.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">createFromString</span><span class="p">(</span><span class="n">_</span> <span class="nv">styleString</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-style">Style</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>styleString</em>
</code>
</td>
<td>
<div>
<p>JSON style string.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Style instance.</p>
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

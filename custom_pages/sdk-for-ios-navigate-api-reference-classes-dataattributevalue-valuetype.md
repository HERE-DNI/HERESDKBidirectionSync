---
title: "sdk-for-ios-navigate-api-reference-classes-dataattributevalue-valuetype"
slug: "sdk-for-ios-navigate-api-reference-classes-dataattributevalue-valuetype"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ValueType"></a>
<a title="ValueType Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-classes-dataattributevalue">DataAttributeValue</a>
<img alt="" id="carat" src="/carat.png"/>
        ValueType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ValueType</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ValueType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Supported types of the data attribute values.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC0D4TypeO6stringyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/string"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC0D4TypeO6stringyA2EmF">string</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Value of string type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">string</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC0D4TypeO5int64yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/int64"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC0D4TypeO5int64yA2EmF">int64</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Value of 64-bit integer type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">int64</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC0D4TypeO5floatyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/float"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC0D4TypeO5floatyA2EmF">float</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Value of single precision float type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">float</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC0D4TypeO6doubleyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/double"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC0D4TypeO6doubleyA2EmF">double</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Value of double precision float type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC0D4TypeO7booleanyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/boolean"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC0D4TypeO7booleanyA2EmF">boolean</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Value of boolean type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">boolean</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC0D4TypeO5coloryA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/color"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC0D4TypeO5coloryA2EmF">color</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Value of color type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">color</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC0D4TypeO5arrayyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/array"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC0D4TypeO5arrayyA2EmF">array</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Value of array type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">array</span></code></pre>
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

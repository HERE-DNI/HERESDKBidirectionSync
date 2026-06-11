---
title: "sdk-for-ios-navigate-api-reference-structs-localizedtexts"
slug: "sdk-for-ios-navigate-api-reference-structs-localizedtexts"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LocalizedTexts"></a>
<a title="LocalizedTexts Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-core">Core</a>
<img alt="" id="carat" src="/carat.png"/>
        LocalizedTexts Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LocalizedTexts</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LocalizedTexts</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The list of multiple names or titles for the same entity, possibly in different languages.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocalizedTextsV5itemsSayAA0B4TextVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/items"></a>
<a class="token" href="#/s:7heresdk14LocalizedTextsV5itemsSayAA0B4TextVGvp">items</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of text items.
Recommended to use helper methods instead of directly accessing the items.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">items</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocalizedTextsV5itemsACSayAA0B4TextVG_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(items:)"></a>
<a class="token" href="#/s:7heresdk14LocalizedTextsV5itemsACSayAA0B4TextVG_tcfc">init(items:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">items</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocalizedTextsV14preferredValue3forSSSgSay10Foundation6LocaleVG_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/preferredValue(for:)"></a>
<a class="token" href="#/s:7heresdk14LocalizedTextsV14preferredValue3forSSSgSay10Foundation6LocaleVG_tF">preferredValue(for:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns best name or title to be presented to the user according to specified
locales. The locales are expected to be ordered by priority.
If no matching locale found - the default is returned.
In case of empty list returns <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">preferredValue</span><span class="p">(</span><span class="k">for</span> <span class="nv">locales</span><span class="p">:</span> <span class="p">[</span><span class="kt">Locale</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locales</em>
</code>
</td>
<td>
<div>
<p>Locales that will be used to translate name or title.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Returns best name or title to be presented to the user according to specified locales.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocalizedTextsV12defaultValueSSSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/defaultValue()"></a>
<a class="token" href="#/s:7heresdk14LocalizedTextsV12defaultValueSSSgyF">defaultValue()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the default value.
In case of empty list return <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">defaultValue</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Returns the default value.</p>
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

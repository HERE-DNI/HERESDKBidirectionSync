---
title: "Search / Suggestion"
slug: "sdk-for-ios-navigate-api-reference-classes-suggestion"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/Suggestion"></a>
<a title="Suggestion Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        Suggestion Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Suggestion</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Suggestion</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Suggestion</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Suggestion</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Suggestion is meant to provide relevant suggestions to partial queries, like “restaur”, “starbu”, “eiffel”.
Represents a relevant response to user queries.
Suggestions (please check <code><a href="sdk-for-ios-navigate-api-reference-..-enums-suggestiontype">SuggestionType</a></code>) are either:
Place: <code><a href="../Enums/SuggestionType.html#/s:7heresdk14SuggestionTypeO5placeyA2CmF">SuggestionType.place</a></code>
Query: <code><a href="../Enums/SuggestionType.html#/s:7heresdk14SuggestionTypeO5chainyA2CmF">SuggestionType.chain</a></code> or <code><a href="../Enums/SuggestionType.html#/s:7heresdk14SuggestionTypeO8categoryyA2CmF">SuggestionType.category</a></code></p>
<p>With “Place” you get data for a concrete place in the world.
With “Query” something to follow-up, a way to perform more focused search.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SuggestionC5titleSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/title"></a>
<a class="token" href="#/s:7heresdk10SuggestionC5titleSSvp">title</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The localized title for the suggestion.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">title</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SuggestionC4typeAA0B4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk10SuggestionC4typeAA0B4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of the suggestion.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-suggestiontype">SuggestionType</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SuggestionC5placeAA5PlaceCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/place"></a>
<a class="token" href="#/s:7heresdk10SuggestionC5placeAA5PlaceCSgvp">place</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The suggested place.
Available only for <code><a href="../Enums/SuggestionType.html#/s:7heresdk14SuggestionTypeO5placeyA2CmF">SuggestionType.place</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">place</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-place">Place</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SuggestionC2idSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk10SuggestionC2idSSSgvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The unique id of suggested item. It can be used to query further information.
For online search, suggestion of type <code><a href="../Enums/SuggestionType.html#/s:7heresdk14SuggestionTypeO5placeyA2CmF">SuggestionType.place</a></code>
will have Suggestion.id same as Place.id.
For offline search, only suggestion of type <code><a href="../Enums/SuggestionType.html#/s:7heresdk14SuggestionTypeO5chainyA2CmF">SuggestionType.chain</a></code>,
will have this property filled with identifier number of an associated chain.
For example, the chain ID “8778” corresponds to the chain name “ABC Shop”.
For other types, <code><a href="../Enums/SuggestionType.html#/s:7heresdk14SuggestionTypeO5placeyA2CmF">SuggestionType.place</a></code> and <code><a href="../Enums/SuggestionType.html#/s:7heresdk14SuggestionTypeO8categoryyA2CmF">SuggestionType.category</a></code>
this property will be null.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SuggestionC4hrefSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/href"></a>
<a class="token" href="#/s:7heresdk10SuggestionC4hrefSSSgvp">href</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Direct URL for precise query.
Available only for <code><a href="../Enums/SuggestionType.html#/s:7heresdk14SuggestionTypeO5chainyA2CmF">SuggestionType.chain</a></code> and <code><a href="../Enums/SuggestionType.html#/s:7heresdk14SuggestionTypeO8categoryyA2CmF">SuggestionType.category</a></code>.
This is not supported in offline search.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">href</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SuggestionC13getHighlightsSDyAA13HighlightTypeOSayAA10IndexRangeCGGyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getHighlights()"></a>
<a class="token" href="#/s:7heresdk10SuggestionC13getHighlightsSDyAA13HighlightTypeOSayAA10IndexRangeCGGyF">getHighlights()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The text slices matching the input query.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getHighlights</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-highlighttype">HighlightType</a></span> <span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-indexrange">IndexRange</a></span><span class="p">]]</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Associated container where <code><a href="sdk-for-ios-navigate-api-reference-..-enums-highlighttype">HighlightType</a></code> is a key and list of <code><a href="sdk-for-ios-navigate-api-reference-..-classes-indexrange">IndexRange</a></code> value.</p>
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

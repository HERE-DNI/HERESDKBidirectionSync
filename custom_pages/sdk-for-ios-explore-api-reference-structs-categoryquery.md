---
title: "sdk-for-ios-explore-api-reference-structs-categoryquery"
slug: "sdk-for-ios-explore-api-reference-structs-categoryquery"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CategoryQuery"></a>
<a title="CategoryQuery Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        CategoryQuery Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>CategoryQuery</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CategoryQuery</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The options to specify a query by categories.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV10categoriesSayAA05PlaceB0CGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/categories"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV10categoriesSayAA05PlaceB0CGvp">categories</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of categories to be included.
A place can be assigned multiple categories. If any of them is in <code>CategoryQuery.categories</code>,
but none are in <code><a href="../Structs/CategoryQuery.html#/s:7heresdk13CategoryQueryV17excludeCategoriesSayAA05PlaceB0CGvp">CategoryQuery.excludeCategories</a></code>, that place will be included in the response.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">categories</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-placecategory">PlaceCategory</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV17excludeCategoriesSayAA05PlaceB0CGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/excludeCategories"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV17excludeCategoriesSayAA05PlaceB0CGvp">excludeCategories</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of categories and subcategories to be excluded.
A place can be assigned multiple categories. If any of them is in <code>CategoryQuery.excludeCategories</code>,
that place will not be included in the response, regardless of whether any of its assigned
categories have been included in <code><a href="../Structs/CategoryQuery.html#/s:7heresdk13CategoryQueryV10categoriesSayAA05PlaceB0CGvp">CategoryQuery.categories</a></code>.
In short, an exclusion will always win over an inclusion.
This is especially useful for excluding specific subcategories from the main category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">excludeCategories</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-placecategory">PlaceCategory</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV13includeChainsSayAA10PlaceChainVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/includeChains"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV13includeChainsSayAA10PlaceChainVGvp">includeChains</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of chains to be included.
A place can be assigned multiple chains. If any of them is in <code>CategoryQuery.includeChains</code>,
but none are in <code><a href="../Structs/CategoryQuery.html#/s:7heresdk13CategoryQueryV13excludeChainsSayAA10PlaceChainVGvp">CategoryQuery.excludeChains</a></code>, that place will be included in the response.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">includeChains</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-placechain">PlaceChain</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV13excludeChainsSayAA10PlaceChainVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/excludeChains"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV13excludeChainsSayAA10PlaceChainVGvp">excludeChains</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of chains to be excluded.
A place can be assigned multiple chains. If any of them is in <code>CategoryQuery.excludeChains</code>,
that place will not be included in the response, regardless of whether any of its assigned
chains have been included in <code><a href="../Structs/CategoryQuery.html#/s:7heresdk13CategoryQueryV13includeChainsSayAA10PlaceChainVGvp">CategoryQuery.includeChains</a></code>.
In short, an exclusion will always win over an inclusion.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">excludeChains</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-placechain">PlaceChain</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV16includeFoodTypesSayAA05PlaceE4TypeVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/includeFoodTypes"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV16includeFoodTypesSayAA05PlaceE4TypeVGvp">includeFoodTypes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of food types to be included.
A place can be assigned multiple food types. If any of them is in <code>CategoryQuery.includeFoodTypes</code>,
but none are in <code><a href="../Structs/CategoryQuery.html#/s:7heresdk13CategoryQueryV16excludeFoodTypesSayAA05PlaceE4TypeVGvp">CategoryQuery.excludeFoodTypes</a></code>, that place will be included in the response.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">includeFoodTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-placefoodtype">PlaceFoodType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV16excludeFoodTypesSayAA05PlaceE4TypeVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/excludeFoodTypes"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV16excludeFoodTypesSayAA05PlaceE4TypeVGvp">excludeFoodTypes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of food types to be excluded.
A place can be assigned multiple food types. If any of them is in <code>CategoryQuery.excludeFoodTypes</code>,
that place will not be included in the response, regardless of whether any of its assigned
food types have been included in <code><a href="../Structs/CategoryQuery.html#/s:7heresdk13CategoryQueryV16includeFoodTypesSayAA05PlaceE4TypeVGvp">CategoryQuery.includeFoodTypes</a></code>.
In short, an exclusion will always win over an inclusion.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">excludeFoodTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-placefoodtype">PlaceFoodType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV6filterSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/filter"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV6filterSSSgvp">filter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Full-text filter on POI names/titles.
Results with a partial match are included in the response.
By default the value is set to null
and results will be based on other parameters provided.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">filter</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV11placeFilterAA05PlaceE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/placeFilter"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV11placeFilterAA05PlaceE0Vvp">placeFilter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The filter options to specify a place in query.
Consists of fuel and truck options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">placeFilter</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-placefilter">PlaceFilter</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV4areaAC4AreaVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/area"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV4areaAC4AreaVvp">area</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Area in which to provide the most relevant places.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">area</span><span class="p">:</span> <span class="kt">CategoryQuery</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-categoryquery-area">Area</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV_4areaAcA05PlaceB0C_AC4AreaVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:area:)"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV_4areaAcA05PlaceB0C_AC4AreaVtcfc">init(_:<wbr/>area:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a new instance of this class from provided parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">category</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-placecategory">PlaceCategory</a></span><span class="p">,</span> <span class="nv">area</span><span class="p">:</span> <span class="kt">CategoryQuery</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-categoryquery-area">Area</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>category</em>
</code>
</td>
<td>
<div>
<p>Category for query</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>area</em>
</code>
</td>
<td>
<div>
<p>Area in which to provide the most relevant places.</p>
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
<a name="/s:7heresdk13CategoryQueryV_4areaACSayAA05PlaceB0CG_AC4AreaVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:area:)"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV_4areaACSayAA05PlaceB0CG_AC4AreaVtcfc">init(_:<wbr/>area:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a new instance of this class from provided parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">categories</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-placecategory">PlaceCategory</a></span><span class="p">],</span> <span class="nv">area</span><span class="p">:</span> <span class="kt">CategoryQuery</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-categoryquery-area">Area</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>categories</em>
</code>
</td>
<td>
<div>
<p>List of categories.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>area</em>
</code>
</td>
<td>
<div>
<p>Area in which to provide the most relevant places.</p>
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
<a name="/s:7heresdk13CategoryQueryV_6filter4areaAcA05PlaceB0C_SSAC4AreaVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:filter:area:)"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV_6filter4areaAcA05PlaceB0C_SSAC4AreaVtcfc">init(_:<wbr/>filter:<wbr/>area:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a new instance of this class from provided parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">category</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-placecategory">PlaceCategory</a></span><span class="p">,</span> <span class="nv">filter</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">area</span><span class="p">:</span> <span class="kt">CategoryQuery</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-categoryquery-area">Area</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>category</em>
</code>
</td>
<td>
<div>
<p>Category for query</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>filter</em>
</code>
</td>
<td>
<div>
<p>Full-text filter on POI names/titles.
Results with a partial match are included in the response.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>area</em>
</code>
</td>
<td>
<div>
<p>Area in which to provide the most relevant places.</p>
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
<a name="/s:7heresdk13CategoryQueryV_6filter4areaACSayAA05PlaceB0CG_SSAC4AreaVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:filter:area:)"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV_6filter4areaACSayAA05PlaceB0CG_SSAC4AreaVtcfc">init(_:<wbr/>filter:<wbr/>area:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a new instance of this class from provided parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">categories</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-placecategory">PlaceCategory</a></span><span class="p">],</span> <span class="nv">filter</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">area</span><span class="p">:</span> <span class="kt">CategoryQuery</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-categoryquery-area">Area</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>categories</em>
</code>
</td>
<td>
<div>
<p>List of categories.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>filter</em>
</code>
</td>
<td>
<div>
<p>Full-text filter on POI names/titles.
Results with a partial match are included in the response.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>area</em>
</code>
</td>
<td>
<div>
<p>Area in which to provide the most relevant places.</p>
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
<a name="/s:7heresdk13CategoryQueryV4AreaV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Area"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV4AreaV">Area</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Area to perform search on.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-structs-categoryquery-area">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Area</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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

---
title: "sdk-for-ios-explore-api-reference-structs-structuredquery"
slug: "sdk-for-ios-explore-api-reference-structs-structuredquery"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/StructuredQuery"></a>
<a title="StructuredQuery Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-search">Search</a>
<img alt="" id="carat" src="/carat.png"/>
        StructuredQuery Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>StructuredQuery</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">StructuredQuery</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The options to specify a structured query.
Only supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15StructuredQueryV5querySSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/query"></a>
<a class="token" href="#/s:7heresdk15StructuredQueryV5querySSvp">query</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Desired query to search.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">query</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15StructuredQueryV10areaCenterAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/areaCenter"></a>
<a class="token" href="#/s:7heresdk15StructuredQueryV10areaCenterAA14GeoCoordinatesVvp">areaCenter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geographic coordinates of the prioritized area center.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">areaCenter</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15StructuredQueryV15addressElementsAC07AddressE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/addressElements"></a>
<a class="token" href="#/s:7heresdk15StructuredQueryV15addressElementsAC07AddressE0Vvp">addressElements</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Query address elements to get the results from a specific geographical area.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">addressElements</span><span class="p">:</span> <span class="kt">StructuredQuery</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-structuredquery-addresselements">AddressElements</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15StructuredQueryV10resultTypeAC06ResultE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/resultType"></a>
<a class="token" href="#/s:7heresdk15StructuredQueryV10resultTypeAC06ResultE0OSgvp">resultType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An optional field to indicates the type of result expected.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">resultType</span><span class="p">:</span> <span class="kt">StructuredQuery</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-structuredquery-resulttype">ResultType</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15StructuredQueryV5query10areaCenter15addressElements10resultTypeACSS_AA14GeoCoordinatesVAC07AddressH0VAC06ResultJ0OSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(query:areaCenter:addressElements:resultType:)"></a>
<a class="token" href="#/s:7heresdk15StructuredQueryV5query10areaCenter15addressElements10resultTypeACSS_AA14GeoCoordinatesVAC07AddressH0VAC06ResultJ0OSgtcfc">init(query:<wbr/>areaCenter:<wbr/>addressElements:<wbr/>resultType:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">query</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">areaCenter</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">addressElements</span><span class="p">:</span> <span class="kt">StructuredQuery</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-structuredquery-addresselements">AddressElements</a></span> <span class="o">=</span> <span class="kt">StructuredQuery</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-structuredquery-addresselements">AddressElements</a></span><span class="p">(),</span> <span class="nv">resultType</span><span class="p">:</span> <span class="kt">StructuredQuery</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-structuredquery-resulttype">ResultType</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15StructuredQueryV10ResultTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ResultType"></a>
<a class="token" href="#/s:7heresdk15StructuredQueryV10ResultTypeO">ResultType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies expected result type.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-structuredquery-resulttype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ResultType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15StructuredQueryV15AddressElementsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/AddressElements"></a>
<a class="token" href="#/s:7heresdk15StructuredQueryV15AddressElementsV">AddressElements</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines query address elements which will be used to build address hierarchy during searches.
It is advised to provide at least one intermediate address element when a large address element is provided
for small admin area searches.
For example if a user is building a query for a street and providing only country as an address element,
consider providing city along with it.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-structuredquery-addresselements">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AddressElements</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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

---
title: "SearchOptions Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-searchoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- SearchOptions.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/SearchOptions"></a>
<a title="SearchOptions Structure Reference"></a>
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
<a href="../Search.html">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SearchOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct SearchOptions : Hashable</code></pre>
</div>
</div>
<p>Encapsulates options that control the behavior of search and suggest operations.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13SearchOptionsV12languageCodeAA08LanguageE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/languageCode"></a>
<a class="token" href="#/s:7heresdk13SearchOptionsV12languageCodeAA08LanguageE0OSgvp">languageCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The preferred language of the result. When unset or unsupported language is chosen,
results will be returned in their local language.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var languageCode: LanguageCode?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13SearchOptionsV8maxItemss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxItems"></a>
<a class="token" href="#/s:7heresdk13SearchOptionsV8maxItemss5Int32VSgvp">maxItems</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The maximum number of items in the response. It should be in the range [1, 100].
When not set, results will be limited to 20.
For location search (reverse geocode) by default results limited to 1.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var maxItems: Int32?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13SearchOptionsV26highDensityEncodingEnabledSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/highDensityEncodingEnabled"></a>
<a class="token" href="#/s:7heresdk13SearchOptionsV26highDensityEncodingEnabledSbvp">highDensityEncodingEnabled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Allows enabling high density encoding of relevant parameters.
For now, it only affects input parameters of type <code><a href="../Structs/GeoCorridor.html">GeoCorridor</a></code>.
Only supported for search in <code><a href="../Classes/SearchEngine.html">SearchEngine</a></code>, otherwise it is ignored.
<strong>Note:</strong> This is a closed-alpha release of this feature, so there could be a few bugs and
unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
Only participants of the closed-alpha group can get access from HERE to use this feature,
otherwise, a <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">SearchError.forbidden</a></code> will be propagated in callbacks.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var highDensityEncodingEnabled: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13SearchOptionsV18distributedResultsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distributedResults"></a>
<a class="token" href="#/s:7heresdk13SearchOptionsV18distributedResultsSbvp">distributedResults</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if search along the route should produce well-distributed results.
It is only supported for:</p>
<ul>
<li><code>searchByCategory</code> API with <code><a href="../Structs/CategoryQuery/Area.html#/s:7heresdk13CategoryQueryV4AreaV08corridorD0AA11GeoCorridorVSgvp">CategoryQuery.Area.corridorArea</a></code> set</li>
<li><code>searchByText</code> API with <code><a href="../Structs/TextQuery/Area.html#/s:7heresdk9TextQueryV4AreaV08corridorD0AA11GeoCorridorVSgvp">TextQuery.Area.corridorArea</a></code> set
Otherwise, this value is ignored.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var distributedResults: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13SearchOptionsV12languageCode8maxItems26highDensityEncodingEnabled18distributedResultsAcA08LanguageE0OSg_s5Int32VSgS2btcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(languageCode:maxItems:highDensityEncodingEnabled:distributedResults:)"></a>
<a class="token" href="#/s:7heresdk13SearchOptionsV12languageCode8maxItems26highDensityEncodingEnabled18distributedResultsAcA08LanguageE0OSg_s5Int32VSgS2btcfc">init(languageCode:<wbr/>maxItems:<wbr/>highDensityEncodingEnabled:<wbr/>distributedResults:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an Options object. If no parameters are passed, uses default values
(see fields description).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(languageCode: LanguageCode? = nil, maxItems: Int32? = nil, highDensityEncodingEnabled: Bool = false, distributedResults: Bool = false)</code></pre>
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



</div>
`
}</HTMLBlock>

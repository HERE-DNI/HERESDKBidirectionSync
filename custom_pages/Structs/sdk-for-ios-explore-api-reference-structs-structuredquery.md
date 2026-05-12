---
title: "StructuredQuery Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-structuredquery"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- StructuredQuery.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/StructuredQuery"></a>
<a title="StructuredQuery Structure Reference"></a>
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
        StructuredQuery Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct StructuredQuery : Hashable</code></pre>
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
<pre><code>public var query: String</code></pre>
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
<pre><code>public var areaCenter: GeoCoordinates</code></pre>
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
<pre><code>public var addressElements: StructuredQuery.AddressElements</code></pre>
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
<pre><code>public var resultType: StructuredQuery.ResultType?</code></pre>
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
<pre><code>public init(query: String, areaCenter: GeoCoordinates, addressElements: StructuredQuery.AddressElements = StructuredQuery.AddressElements(), resultType: StructuredQuery.ResultType? = nil)</code></pre>
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
<a class="slightly-smaller" href="../Structs/StructuredQuery/ResultType.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum ResultType : UInt32, CaseIterable, Codable</code></pre>
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
<a class="slightly-smaller" href="../Structs/StructuredQuery/AddressElements.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct AddressElements : Hashable</code></pre>
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

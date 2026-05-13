---
title: "AddressElements Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-structuredquery-addresselements"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- AddressElements.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/AddressElements"></a>
<a title="AddressElements Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-search">Search</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-structs-structuredquery">StructuredQuery</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        AddressElements Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct AddressElements : Hashable</code></pre>
</div>
</div>
<p>Defines query address elements which will be used to build address hierarchy during searches.
It is advised to provide at least one intermediate address element when a large address element is provided
for small admin area searches.
For example if a user is building a query for a street and providing only country as an address element,
consider providing city along with it.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15StructuredQueryV15AddressElementsV7countrySSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/country"></a>
<a class="token" href="#/s:7heresdk15StructuredQueryV15AddressElementsV7countrySSSgvp">country</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An optional field of country name or code, which will be used to get the results only from the given country.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var country: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15StructuredQueryV15AddressElementsV4citySSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/city"></a>
<a class="token" href="#/s:7heresdk15StructuredQueryV15AddressElementsV4citySSSgvp">city</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An optional field of city name, which will be used to get the results only from the given city.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var city: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15StructuredQueryV15AddressElementsV10postalCodeSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/postalCode"></a>
<a class="token" href="#/s:7heresdk15StructuredQueryV15AddressElementsV10postalCodeSSSgvp">postalCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An optional field of postal code, which will be used to get the results only within the given postal code.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var postalCode: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15StructuredQueryV15AddressElementsV8districtSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/district"></a>
<a class="token" href="#/s:7heresdk15StructuredQueryV15AddressElementsV8districtSSSgvp">district</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An optional field of district, which will be used to get the results only from the given district.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var district: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15StructuredQueryV15AddressElementsV7country4city10postalCode8districtAESSSg_A3Jtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(country:city:postalCode:district:)"></a>
<a class="token" href="#/s:7heresdk15StructuredQueryV15AddressElementsV7country4city10postalCode8districtAESSSg_A3Jtcfc">init(country:<wbr/>city:<wbr/>postalCode:<wbr/>district:<wbr/>)</a>
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
<pre><code>public init(country: String? = nil, city: String? = nil, postalCode: String? = nil, district: String? = nil)</code></pre>
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

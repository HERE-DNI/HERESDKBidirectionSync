---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-structs-addressquery"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- AddressQuery.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/AddressQuery"></a>
<a title="AddressQuery Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        AddressQuery Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>AddressQuery</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AddressQuery</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The options to specify an address query. A <code><a href="../Structs/AddressQuery.html#/s:7heresdk12AddressQueryV5querySSvp">AddressQuery.query</a></code> can consist of parts of an address or full addresses,
optionally comma separated. <code>AddressQuery</code> should only be used to search for parts of the address,
excluding the POI name. For example, “Invalidenstraße 116, Berlin, Germany” is appropriate, whereas
“HERE, Invalidenstraße 116, Berlin, Germany” is not. To be able to include the POI name, use
<code><a href="sdk-for-ios-explore-api-reference-..-structs-textquery">TextQuery</a></code> instead. <code><a href="../Structs/SearchOptions.html#/s:7heresdk13SearchOptionsV12languageCodeAA08LanguageE0OSgvp">SearchOptions.languageCode</a></code> specifies the language of the
<code><a href="../Structs/AddressQuery.html#/s:7heresdk12AddressQueryV5querySSvp">AddressQuery.query</a></code> and determines the preferred language of the results.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12AddressQueryV5querySSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/query"></a>
<a class="token" href="#/s:7heresdk12AddressQueryV5querySSvp">query</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Desired address query to search.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">query</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12AddressQueryV10areaCenterAA14GeoCoordinatesVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/areaCenter"></a>
<a class="token" href="#/s:7heresdk12AddressQueryV10areaCenterAA14GeoCoordinatesVSgvp">areaCenter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geographical coordinates of the center around which to provide the most relevant places.
For Offline Search null value will result in <code><a href="../Enums/SearchError.html#/s:7heresdk11SearchErrorO11invalidAreayA2CmF">SearchError.invalidArea</a></code></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">areaCenter</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12AddressQueryV9countriesSayAA11CountryCodeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/countries"></a>
<a class="token" href="#/s:7heresdk12AddressQueryV9countriesSayAA11CountryCodeOGvp">countries</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A list of countries that the query is applied in.
Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">countries</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-countrycode">CountryCode</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12AddressQueryV_4nearACSS_AA14GeoCoordinatesVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:near:)"></a>
<a class="token" href="#/s:7heresdk12AddressQueryV_4nearACSS_AA14GeoCoordinatesVtcfc">init(_:<wbr/>near:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs an AddressQuery from the provided text query and geographical coordinates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="n">near</span> <span class="nv">areaCenter</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>query</em>
</code>
</td>
<td>
<div>
<p>Desired query to search.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>areaCenter</em>
</code>
</td>
<td>
<div>
<p>Geographical coordinates of the center around which to provide the most relevant places.</p>
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
<a name="/s:7heresdk12AddressQueryV_4near11inCountriesACSS_AA14GeoCoordinatesVSayAA11CountryCodeOGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:near:inCountries:)"></a>
<a class="token" href="#/s:7heresdk12AddressQueryV_4near11inCountriesACSS_AA14GeoCoordinatesVSayAA11CountryCodeOGtcfc">init(_:<wbr/>near:<wbr/>inCountries:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs an AddressQuery from the provided text query, geographical coordinates and the
list of countries the query is applied in.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="n">near</span> <span class="nv">areaCenter</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="n">inCountries</span> <span class="nv">countries</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-countrycode">CountryCode</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>query</em>
</code>
</td>
<td>
<div>
<p>Desired query to search.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>areaCenter</em>
</code>
</td>
<td>
<div>
<p>Geographical coordinates of the center around which to provide the most relevant places.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>countries</em>
</code>
</td>
<td>
<div>
<p>A list of countries that the query is applied in.</p>
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
<a name="/s:7heresdk12AddressQueryVyACSScfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk12AddressQueryVyACSScfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs an AddressQuery from the provided text query.
Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">query</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>query</em>
</code>
</td>
<td>
<div>
<p>Desired query to search.</p>
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

</div>
`
}</HTMLBlock>

---
title: "Address"
slug: "sdk-for-ios-explore-api-reference-structs-address"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Address"></a>
<a title="Address Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-search">Search</a>

        Address Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Address</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Address</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Information about the address of a location.</p>
<p>Used in <code><a href="../Classes/Place.html#/s:7heresdk5PlaceC7addressAA7AddressVvp">Place.address</a></code>.</p>
<p>Note that while <code>OfflineSearchEngine.suggest</code> and <code>OfflineSearchEngine.suggestByText</code> set all available details,
<code>SearchEngine.suggest</code> and <code>SearchEngine.suggestByText</code> set only <code><a href="../Structs/Address.html#/s:7heresdk7AddressV11addressTextSSvp">Address.addressText</a></code>.
Complete address details can be obtained by searching with <code><a href="sdk-for-ios-explore-api-reference-structs-placeidquery">PlaceIdQuery</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV4citySSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/city"></a>
<a class="token" href="#/s:7heresdk7AddressV4citySSvp">city</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The city name for the address, for example, “Brooklyn”.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">city</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV11countryCodeSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/countryCode"></a>
<a class="token" href="#/s:7heresdk7AddressV11countryCodeSSvp">countryCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An ISO-3166-1 (3-letter) country code for the address, for example, “USA”.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">countryCode</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV7countrySSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/country"></a>
<a class="token" href="#/s:7heresdk7AddressV7countrySSvp">country</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The country name for the address, for example, “United States”.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">country</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV8districtSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/district"></a>
<a class="token" href="#/s:7heresdk7AddressV8districtSSvp">district</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The district name for the address.
It is a division of city, typically an administrative unit within a larger city or
a customary name of a city’s neighborhood, for example, “Bedford-Stuyvesant”.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">district</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV11subdistrictSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/subdistrict"></a>
<a class="token" href="#/s:7heresdk7AddressV11subdistrictSSvp">subdistrict</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The subdistrict name for the address.
It is a subdivision of a district.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">subdistrict</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV14houseNumOrNameSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/houseNumOrName"></a>
<a class="token" href="#/s:7heresdk7AddressV14houseNumOrNameSSvp">houseNumOrName</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The house name or number for the address, for example, “347”.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">houseNumOrName</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV10postalCodeSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/postalCode"></a>
<a class="token" href="#/s:7heresdk7AddressV10postalCodeSSvp">postalCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The postal code for the address.
It is an alphanumeric string included in a postal address to facilitate mail sorting, known locally
in various countries throughout the world as a postcode, post code, PIN or ZIP Code, for example, “11233”.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">postalCode</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV5stateSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/state"></a>
<a class="token" href="#/s:7heresdk7AddressV5stateSSvp">state</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The state name for the address.
It is the name of the state division of a country, for example, “New York”.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">state</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV6countySSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/county"></a>
<a class="token" href="#/s:7heresdk7AddressV6countySSvp">county</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The county name for the address.
It is a division of a state, typically a secondary-level administrative division of a country or equivalent,
for example, “Kings”.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">county</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV6streetSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/street"></a>
<a class="token" href="#/s:7heresdk7AddressV6streetSSvp">street</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The street name for the address, for example, “Lewis Ave”.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">street</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV5blockSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/block"></a>
<a class="token" href="#/s:7heresdk7AddressV5blockSSvp">block</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The block number for the address. It is part of Japanese addressing system.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">block</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV8subBlockSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/subBlock"></a>
<a class="token" href="#/s:7heresdk7AddressV8subBlockSSvp">subBlock</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The sub-block number for the address. It is part of Japanese addressing system.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">subBlock</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV11addressTextSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/addressText"></a>
<a class="token" href="#/s:7heresdk7AddressV11addressTextSSvp">addressText</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The text for the address, for example, “Secret Garden, 347 Lewis Ave, Brooklyn, NY 11233, United States”.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">addressText</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV4typeAA0B4TypeOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk7AddressV4typeAA0B4TypeOSgvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the address type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-addresstype">AddressType</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV9stateCodeSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/stateCode"></a>
<a class="token" href="#/s:7heresdk7AddressV9stateCodeSSvp">stateCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The state code for the address.
It is code/abbreviation of the state division of a country, for example, “NY”.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">stateCode</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7AddressV4city11countryCode0D08district11subdistrict14houseNumOrName06postalE05state6county6street5block8subBlock11addressText4type0mE0ACSS_S12SAA0B4TypeOSgSStcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(city:countryCode:country:district:subdistrict:houseNumOrName:postalCode:state:county:street:block:subBlock:addressText:type:stateCode:)"></a>
<a class="token" href="#/s:7heresdk7AddressV4city11countryCode0D08district11subdistrict14houseNumOrName06postalE05state6county6street5block8subBlock11addressText4type0mE0ACSS_S12SAA0B4TypeOSgSStcfc">init(city:<wbr/>countryCode:<wbr/>country:<wbr/>district:<wbr/>subdistrict:<wbr/>houseNumOrName:<wbr/>postalCode:<wbr/>state:<wbr/>county:<wbr/>street:<wbr/>block:<wbr/>subBlock:<wbr/>addressText:<wbr/>type:<wbr/>stateCode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">city</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">countryCode</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">country</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">district</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">subdistrict</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">houseNumOrName</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">postalCode</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">state</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">county</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">street</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">block</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">subBlock</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">addressText</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-addresstype">AddressType</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">stateCode</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">)</span></code></pre>
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
} </HTMLBlock>

---
title: "GeoPlace Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-geoplace"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- GeoPlace.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoPlace"></a>
<a title="GeoPlace Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        GeoPlace Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct GeoPlace : Hashable</code></pre>
</div>
</div>
<p>GeoPlace struct represents a location object:
such as a country, a city, a point of interest (POI) etc.
It can be used for PersonalPlace creation, in order to provide search on custom places.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GeoPlaceV5titleSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/title"></a>
<a class="token" href="#/s:7heresdk8GeoPlaceV5titleSSvp">title</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The localized title for the resource.
Note: This String can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var title: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GeoPlaceV11externalIDsSayAA10ExternalIDVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/externalIDs"></a>
<a class="token" href="#/s:7heresdk8GeoPlaceV11externalIDsSayAA10ExternalIDVGvp">externalIDs</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Allows the client to set the id in their own system.
The list of supplier references to this place.
The references are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var externalIDs: [ExternalID]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GeoPlaceV4typeAA0C4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk8GeoPlaceV4typeAA0C4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies place type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var type: PlaceType</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GeoPlaceV10categoriesSayAA0C8CategoryCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/categories"></a>
<a class="token" href="#/s:7heresdk8GeoPlaceV10categoriesSayAA0C8CategoryCGvp">categories</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of corresponding categories
Note: This list can be empty when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var categories: [PlaceCategory]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GeoPlaceV7addressAA7AddressVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/address"></a>
<a class="token" href="#/s:7heresdk8GeoPlaceV7addressAA7AddressVvp">address</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Address of the place
Note: Address can have default value when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var address: Address</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GeoPlaceV8locationAA15LocationDetailsVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/location"></a>
<a class="token" href="#/s:7heresdk8GeoPlaceV8locationAA15LocationDetailsVSgvp">location</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geographical details
Note: Can be <code>nil</code> when retrieved from a suggestion’s place property.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var location: LocationDetails?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GeoPlaceV8businessAA15BusinessDetailsVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/business"></a>
<a class="token" href="#/s:7heresdk8GeoPlaceV8businessAA15BusinessDetailsVvp">business</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Business details
Note: BusinessDetails can have default value when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var business: BusinessDetails</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GeoPlaceV3webAA10WebDetailsVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/web"></a>
<a class="token" href="#/s:7heresdk8GeoPlaceV3webAA10WebDetailsVvp">web</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains info and direct web links to corresponding items.
Note: WebDetails can have default value when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var web: WebDetails</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GeoPlaceV5title11externalIDs4type10categories7address8location8business3webACSS_SayAA10ExternalIDVGAA0C4TypeOSayAA0C8CategoryCGAA7AddressVAA15LocationDetailsVSgAA08BusinessS0VAA03WebS0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(title:externalIDs:type:categories:address:location:business:web:)"></a>
<a class="token" href="#/s:7heresdk8GeoPlaceV5title11externalIDs4type10categories7address8location8business3webACSS_SayAA10ExternalIDVGAA0C4TypeOSayAA0C8CategoryCGAA7AddressVAA15LocationDetailsVSgAA08BusinessS0VAA03WebS0Vtcfc">init(title:<wbr/>externalIDs:<wbr/>type:<wbr/>categories:<wbr/>address:<wbr/>location:<wbr/>business:<wbr/>web:<wbr/>)</a>
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
<pre><code>public init(title: String = "", externalIDs: [ExternalID] = [], type: PlaceType = PlaceType.unknown, categories: [PlaceCategory] = [], address: Address = Address(), location: LocationDetails? = nil, business: BusinessDetails = BusinessDetails(), web: WebDetails = WebDetails())</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GeoPlaceV06makeMyC05title11coordinatesACSS_AA0B11CoordinatesVtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/makeMyPlace(title:coordinates:)"></a>
<a class="token" href="#/s:7heresdk8GeoPlaceV06makeMyC05title11coordinatesACSS_AA0B11CoordinatesVtFZ">makeMyPlace(title:<wbr/>coordinates:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class. All other properties will keep their default value
and all properties containing lists will contain empty lists.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static func makeMyPlace(title: String, coordinates: GeoCoordinates) -&gt; GeoPlace</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>title</em>
</code>
</td>
<td>
<div>
<p>The title.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>coordinates</em>
</code>
</td>
<td>
<div>
<p>The coordinates.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>An instance of <code>GeoPlace</code>.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GeoPlaceV5getIDSSyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getID()"></a>
<a class="token" href="#/s:7heresdk8GeoPlaceV5getIDSSyF">getID()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Allow the client to access GeoPlace id.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getID() -&gt; String</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The place id.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GeoPlaceV04isMyC0SbyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/isMyPlace()"></a>
<a class="token" href="#/s:7heresdk8GeoPlaceV04isMyC0SbyF">isMyPlace()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Allow the client to access info about is it my place or not.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func isMyPlace() -&gt; Bool</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p><code>True</code> if it is my place, <code>false</code> otherwise.</p>
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

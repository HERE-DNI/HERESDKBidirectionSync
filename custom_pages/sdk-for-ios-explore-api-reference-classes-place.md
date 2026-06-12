---
title: "Place"
slug: "sdk-for-ios-explore-api-reference-classes-place"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/Place"></a>
<a title="Place Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-search">Search</a>

        Place Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Place</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Place</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Place</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Place</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a location object, such as a country, a city, a point of interest (POI) etc.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC5titleSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/title"></a>
<a class="token" href="#/s:7heresdk5PlaceC5titleSSvp">title</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The localized title for the resource.</p>
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
<a name="/s:7heresdk5PlaceC2idSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk5PlaceC2idSSvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The unique id of this resource. It can be used to query further information.
When returned from <code>OfflineSearchEngine</code>, <code>id</code> is valid only for <code>Place</code> objects whose
<code>place_type</code> is <code>POI</code>. Otherwise, it is empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC9placeTypeAA0bD0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/placeType"></a>
<a class="token" href="#/s:7heresdk5PlaceC9placeTypeAA0bD0Ovp">placeType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The place type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">placeType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-placetype">PlaceType</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC8areaTypeAA04AreaD0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/areaType"></a>
<a class="token" href="#/s:7heresdk5PlaceC8areaTypeAA04AreaD0OSgvp">areaType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The area type. It is available only when the <code><a href="../Classes/Place.html#/s:7heresdk5PlaceC9placeTypeAA0bD0Ovp">Place.placeType</a></code> is <code><a href="../Enums/PlaceType.html#/s:7heresdk9PlaceTypeO4areayA2CmF">PlaceType.area</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">areaType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-areatype">AreaType</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC7addressAA7AddressVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/address"></a>
<a class="token" href="#/s:7heresdk5PlaceC7addressAA7AddressVvp">address</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The address of the place.</p>
<p>Note that while <code>OfflineSearchEngine.suggest</code> and <code>OfflineSearchEngine.suggestByText</code> set all available details,
<code>SearchEngine.suggest</code> and <code>SearchEngine.suggestByText</code> set only <code><a href="../Structs/Address.html#/s:7heresdk7AddressV11addressTextSSvp">Address.addressText</a></code>.
Complete address details can be obtained by searching with <code><a href="sdk-for-ios-explore-api-reference-structs-placeidquery">PlaceIdQuery</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">address</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-address">Address</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC7detailsAA7DetailsVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/details"></a>
<a class="token" href="#/s:7heresdk5PlaceC7detailsAA7DetailsVvp">details</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The place’s detailed information.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">details</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-details">Details</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC14geoCoordinatesAA03GeoD0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/geoCoordinates"></a>
<a class="token" href="#/s:7heresdk5PlaceC14geoCoordinatesAA03GeoD0VSgvp">geoCoordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geographic coordinates of the place.
Can be <code>nil</code> when retrieved from a suggestion’s place property.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">geoCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC25isCoordinatesInterpolatedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isCoordinatesInterpolated"></a>
<a class="token" href="#/s:7heresdk5PlaceC25isCoordinatesInterpolatedSbvp">isCoordinatesInterpolated</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A property that says whether the coordinates of the house number were interpolated or not.
This property is valid only for house number results retrieved using online search.
When false, it means <code><a href="../Classes/Place.html#/s:7heresdk5PlaceC14geoCoordinatesAA03GeoD0VSgvp">Place.geoCoordinates</a></code> point to an accurate position of the house. Otherwise
coordinates are slightly less accurate, but are based on a highly optimized interpolation algorithm.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isCoordinatesInterpolated</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC12accessPointsSayAA14GeoCoordinatesVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/accessPoints"></a>
<a class="token" href="#/s:7heresdk5PlaceC12accessPointsSayAA14GeoCoordinatesVGvp">accessPoints</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The access points to the place, such as the points on a road or in a parking lot.
A place can have multiple access points. For example, a large warehouse can have
multiple entrances, while the center of the warehouse may not be directly reachable.
Note that access points are meant to be reachable by vehicles.
For routes it is recommended to navigate to one of the available access points (if any),
whereas the <code>sideOfStreetHint</code> should be set to the geographic coordinates of the place.
The list is empty when no access points are known or when the place is directly reachable.
A place can have multiple access points. For example, a large warehouse can have
multiple entrances, while the center of the warehouse may not be directly reachable.
Note that access points are meant to be reachable by vehicles.
For routes it is recommended to navigate to one of the available access points (if any),
whereas the <code>sideOfStreetHint</code> should be set to the geographic coordinates of the place.
The list is empty when no access points are known or when the place is directly reachable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">accessPoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC11boundingBoxAA03GeoD0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/boundingBox"></a>
<a class="token" href="#/s:7heresdk5PlaceC11boundingBoxAA03GeoD0VSgvp">boundingBox</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geographic coordinates of the map bounding box containing the place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">boundingBox</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geobox">GeoBox</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC16distanceInMeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceInMeters"></a>
<a class="token" href="#/s:7heresdk5PlaceC16distanceInMeterss5Int32VSgvp">distanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance from the search center to the place in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC13politicalViewSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/politicalView"></a>
<a class="token" href="#/s:7heresdk5PlaceC13politicalViewSSSgvp">politicalView</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geopolitical view, defined as a three letter country code, each disputed territory has international and alternative views.
Populated when the geopolitical view parameter is set in the <code><a href="sdk-for-ios-explore-api-reference-structs-sdkoptions">SDKOptions</a></code>
and passed to <code><a href="sdk-for-ios-explore-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code> on instantiation,
but only if it is an alternative view.
For more details refer to <code><a href="sdk-for-ios-explore-api-reference-structs-sdkoptions">SDKOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">politicalView</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC16serializeCompactSSyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/serializeCompact()"></a>
<a class="token" href="#/s:7heresdk5PlaceC16serializeCompactSSyF">serializeCompact()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Serializes <code>Place</code> to persist or transfer. Preserves limited amount of data:</p>
<ul>
<li><code><a href="../Classes/Place.html#/s:7heresdk5PlaceC5titleSSvp">Place.title</a></code></li>
<li><code><a href="../Classes/Place.html#/s:7heresdk5PlaceC2idSSvp">Place.id</a></code></li>
<li><code><a href="../Classes/Place.html#/s:7heresdk5PlaceC14geoCoordinatesAA03GeoD0VSgvp">Place.geoCoordinates</a></code></li>
<li><code><a href="../Classes/Place.html#/s:7heresdk5PlaceC12accessPointsSayAA14GeoCoordinatesVGvp">Place.accessPoints</a></code></li>
<li><code><a href="../Classes/Place.html#/s:7heresdk5PlaceC9placeTypeAA0bD0Ovp">Place.placeType</a></code></li>
<li><code><a href="../Classes/Place.html#/s:7heresdk5PlaceC11boundingBoxAA03GeoD0VSgvp">Place.boundingBox</a></code></li>
<li><code><a href="../Structs/Details.html#/s:7heresdk7DetailsV20getPrimaryCategoriesSayAA13PlaceCategoryCGyF">Details.getPrimaryCategories(...)</a></code></li>
<li><code><a href="../Structs/Address.html#/s:7heresdk7AddressV11addressTextSSvp">Address.addressText</a></code></li>
<li><code><a href="../Structs/Address.html#/s:7heresdk7AddressV11countryCodeSSvp">Address.countryCode</a></code></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">serializeCompact</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">String</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The serialized place</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5PlaceC11deserialize010serializedB0ACSS_tKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/deserialize(serializedPlace:)"></a>
<a class="token" href="#/s:7heresdk5PlaceC11deserialize010serializedB0ACSS_tKFZ">deserialize(serializedPlace:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a <code>Place</code> created from serialized string.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Search.html#/s:7heresdk27PlaceSerializationExceptiona">PlaceSerializationException</a></code> Indicates what went wrong during deserialization attempt.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">deserialize</span><span class="p">(</span><span class="nv">serializedPlace</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt">Place</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>serializedPlace</em>
</code>
</td>
<td>
<div>
<p>The serialized place</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>A <code>Place</code> created from serialized string.</p>
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

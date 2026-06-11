---
title: "PickedPlace"
slug: "sdk-for-ios-navigate-api-reference-structs-pickedplace"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PickedPlace"></a>
<a title="PickedPlace Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-core">Core</a>

        PickedPlace Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PickedPlace</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PickedPlace</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Carries the result of picking a Carto POI (point of interest) object.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PickedPlaceV4nameSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/name"></a>
<a class="token" href="#/s:7heresdk11PickedPlaceV4nameSSvp">name</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The name of the POI localized in the currently selected map language.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PickedPlaceV11coordinatesAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk11PickedPlaceV11coordinatesAA14GeoCoordinatesVvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geographic coordinates of the POI.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PickedPlaceV15placeCategoryIdSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/placeCategoryId"></a>
<a class="token" href="#/s:7heresdk11PickedPlaceV15placeCategoryIdSSvp">placeCategoryId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The place category ID of the POI.
This is the same String value as <code><a href="../Classes/PlaceCategory.html#/s:7heresdk13PlaceCategoryC2idSSvp">PlaceCategory.id</a></code> that can be obtained from the
<code><a href="sdk-for-ios-navigate-api-reference-classes-searchengine">SearchEngine</a></code> and the <code><a href="sdk-for-ios-navigate-api-reference-classes-offlinesearchengine">OfflineSearchEngine</a></code>. Note that not all editions include the
<code><a href="sdk-for-ios-navigate-api-reference-classes-offlinesearchengine">OfflineSearchEngine</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">placeCategoryId</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PickedPlaceV15offlineSearchIdSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offlineSearchId"></a>
<a class="token" href="#/s:7heresdk11PickedPlaceV15offlineSearchIdSSvp">offlineSearchId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The place ID to query an offline search to obtain additional data about this POI with
the <code><a href="sdk-for-ios-navigate-api-reference-classes-offlinesearchengine">OfflineSearchEngine</a></code>. Note that not all editions include the <code><a href="sdk-for-ios-navigate-api-reference-classes-offlinesearchengine">OfflineSearchEngine</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">offlineSearchId</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PickedPlaceV4name11coordinates15placeCategoryId013offlineSearchH0ACSS_AA14GeoCoordinatesVS2Stcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(name:coordinates:placeCategoryId:offlineSearchId:)"></a>
<a class="token" href="#/s:7heresdk11PickedPlaceV4name11coordinates15placeCategoryId013offlineSearchH0ACSS_AA14GeoCoordinatesVS2Stcfc">init(name:<wbr/>coordinates:<wbr/>placeCategoryId:<wbr/>offlineSearchId:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">placeCategoryId</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">offlineSearchId</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">)</span></code></pre>
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

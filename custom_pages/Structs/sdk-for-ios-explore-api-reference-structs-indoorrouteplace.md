---
title: "IndoorRoutePlace Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-indoorrouteplace"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- IndoorRoutePlace.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/IndoorRoutePlace"></a>
<a title="IndoorRoutePlace Structure Reference"></a>
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
<a href="../Other%20Structs.html">Other Structures</a>
<img alt="" id="carat" src="../img/carat.png"/>
        IndoorRoutePlace Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct IndoorRoutePlace : Hashable</code></pre>
</div>
</div>
<p>Represents a place within an indoor route.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRoutePlaceV4typeAA0cD4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk16IndoorRoutePlaceV4typeAA0cD4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The type of the route place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var type: RoutePlaceType</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRoutePlaceV11coordinatesAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk16IndoorRoutePlaceV11coordinatesAA14GeoCoordinatesVvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geographic coordinates of the place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var coordinates: GeoCoordinates</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRoutePlaceV11levelZIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/levelZIndex"></a>
<a class="token" href="#/s:7heresdk16IndoorRoutePlaceV11levelZIndexs5Int32Vvp">levelZIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The vertical level index of this indoor location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var levelZIndex: Int32</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRoutePlaceV7venueIdSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/venueId"></a>
<a class="token" href="#/s:7heresdk16IndoorRoutePlaceV7venueIdSSvp">venueId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The venue identifier of this indoor location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var venueId: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRoutePlaceV7levelIdSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/levelId"></a>
<a class="token" href="#/s:7heresdk16IndoorRoutePlaceV7levelIdSSvp">levelId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The level identifier of this indoor location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var levelId: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16IndoorRoutePlaceV4type11coordinates11levelZIndex7venueId0gJ0AcA0cD4TypeO_AA14GeoCoordinatesVs5Int32VS2Stcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(type:coordinates:levelZIndex:venueId:levelId:)"></a>
<a class="token" href="#/s:7heresdk16IndoorRoutePlaceV4type11coordinates11levelZIndex7venueId0gJ0AcA0cD4TypeO_AA14GeoCoordinatesVs5Int32VS2Stcfc">init(type:<wbr/>coordinates:<wbr/>levelZIndex:<wbr/>venueId:<wbr/>levelId:<wbr/>)</a>
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
<pre><code>public init(type: RoutePlaceType, coordinates: GeoCoordinates, levelZIndex: Int32, venueId: String, levelId: String)</code></pre>
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

---
title: "Area Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-categoryquery-area"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- Area.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/Area"></a>
<a title="Area Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../../index.html">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Search.html">Search</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Structs/CategoryQuery.html">CategoryQuery</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        Area Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct Area : Hashable</code></pre>
</div>
</div>
<p>Area to perform search on.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV4AreaV10areaCenterAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/areaCenter"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV4AreaV10areaCenterAA14GeoCoordinatesVvp">areaCenter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geographic coordinates of the center around which to provide the most relevant places.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let areaCenter: GeoCoordinates</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV4AreaV03boxD0AA6GeoBoxVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/boxArea"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV4AreaV03boxD0AA6GeoBoxVSgvp">boxArea</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geographic rectangle area in which to provide the most relevant places.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let boxArea: GeoBox?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV4AreaV06circleD0AA9GeoCircleVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/circleArea"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV4AreaV06circleD0AA9GeoCircleVSgvp">circleArea</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geographic circle area in which to provide the most relevant places.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let circleArea: GeoCircle?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV4AreaV08corridorD0AA11GeoCorridorVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/corridorArea"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV4AreaV08corridorD0AA11GeoCorridorVSgvp">corridorArea</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geographic corridor area in which to provide the most relevant places.
The contained polyline and half-width define the area that will be used in a search query.</p>
<p>When used with <code><a href="../../Classes/SearchEngine.html">SearchEngine</a></code>, the polyline is compressed and sent.
More complex polylines with large amounts of coordinates and with smaller
half-width may have the less relevant part removed, such as the one far away from the
search center. This usually makes no difference, because there will be enough POIs near
the search center. For use cases where it is important to search the entire polyline,
half-width can be increased or not set.
For example: Route between New York and Chicago with half-width 800 will be added to request
without removing the far away part, but route of the same length (around 360km) between
Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.</p>
<p>When <code>CategoryQuery.Area.corridorArea</code> is provided,
<code><a href="../../Structs/CategoryQuery/Area.html#/s:7heresdk13CategoryQueryV4AreaV10areaCenterAA14GeoCoordinatesVvp">CategoryQuery.Area.areaCenter</a></code> has to be within it, otherwise
<code><a href="../../Structs/CategoryQuery/Area.html#/s:7heresdk13CategoryQueryV4AreaV10areaCenterAA14GeoCoordinatesVvp">CategoryQuery.Area.areaCenter</a></code> is ignored when searching.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let corridorArea: GeoCorridor?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CategoryQueryV4AreaV10areaCenterAeA14GeoCoordinatesV_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(areaCenter:)"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV4AreaV10areaCenterAeA14GeoCoordinatesV_tcfc">init(areaCenter:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a new instance of this class from provided parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(areaCenter: GeoCoordinates)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>areaCenter</em>
</code>
</td>
<td>
<div>
<p>Geographic coordinates of the center around which to provide the most relevant places.</p>
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
<a name="/s:7heresdk13CategoryQueryV4AreaV4near5inBoxAeA14GeoCoordinatesV_AA0hG0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(near:inBox:)"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV4AreaV4near5inBoxAeA14GeoCoordinatesV_AA0hG0Vtcfc">init(near:<wbr/>inBox:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a new instance of this class from provided parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(near areaCenter: GeoCoordinates, inBox boxArea: GeoBox)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>areaCenter</em>
</code>
</td>
<td>
<div>
<p>Geographic coordinates of the center around which to provide the most relevant places.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>boxArea</em>
</code>
</td>
<td>
<div>
<p>Geographic rectangle area in which to provide the most relevant places.</p>
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
<a name="/s:7heresdk13CategoryQueryV4AreaV4near8inCircleAeA14GeoCoordinatesV_AA0hG0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(near:inCircle:)"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV4AreaV4near8inCircleAeA14GeoCoordinatesV_AA0hG0Vtcfc">init(near:<wbr/>inCircle:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a new instance of this class from provided parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(near areaCenter: GeoCoordinates, inCircle circleArea: GeoCircle)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>areaCenter</em>
</code>
</td>
<td>
<div>
<p>Geographic coordinates of the center around which to provide the most relevant places.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>circleArea</em>
</code>
</td>
<td>
<div>
<p>Geographic circle area in which to provide the most relevant places.</p>
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
<a name="/s:7heresdk13CategoryQueryV4AreaV10inCorridor4nearAeA03GeoF0V_AA0H11CoordinatesVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(inCorridor:near:)"></a>
<a class="token" href="#/s:7heresdk13CategoryQueryV4AreaV10inCorridor4nearAeA03GeoF0V_AA0H11CoordinatesVtcfc">init(inCorridor:<wbr/>near:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a new instance of this class from provided parameters.
The given corridor and center define the area that will be used in the search query.</p>
<p>When used with <code><a href="../../Classes/SearchEngine.html">SearchEngine</a></code>, the polyline is compressed and sent.
More complex polylines with large amounts of coordinates and with smaller
half-width may have the less relevant part removed, such as the one far away from the
search center. This usually makes no difference, because there will be enough POIs near
the search center. For use cases where it is important to search the entire polyline,
half-width can be increased or not set.
For example: Route between New York and Chicago with half-width 800 will be added to request
without removing the far away part, but route of the same length (around 360km) between
Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.</p>
<p>The area center has to be within the corridor, otherwise it is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(inCorridor corridorArea: GeoCorridor, near areaCenter: GeoCoordinates)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>corridorArea</em>
</code>
</td>
<td>
<div>
<p>Geographic corridor area in which to provide the most relevant places.</p>
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
<p>Geographic coordinates of the prioritized area center.</p>
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



</div>
`
}</HTMLBlock>

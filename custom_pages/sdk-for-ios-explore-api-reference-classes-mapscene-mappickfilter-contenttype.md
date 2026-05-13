---
title: "ContentType Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-classes-mapscene-mappickfilter-contenttype"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ContentType.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/ContentType"></a>
<a title="ContentType Enumeration Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-..-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-..-maps">Maps</a>
<img alt="" id="carat" src="../../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-..-classes-mapscene">MapScene</a>
<img alt="" id="carat" src="../../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-..-classes-mapscene-mappickfilter">MapPickFilter</a>
<img alt="" id="carat" src="../../../img/carat.png"/>
        ContentType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum ContentType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Type of the map content to be picked.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC0B10PickFilterC11ContentTypeO8mapItemsyA2GmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/mapItems"></a>
<a class="token" href="#/s:7heresdk8MapSceneC0B10PickFilterC11ContentTypeO8mapItemsyA2GmF">mapItems</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map items added through a <code><a href="sdk-for-ios-explore-api-reference-..-..-..-classes-mapscene">MapScene</a></code> like <code><a href="sdk-for-ios-explore-api-reference-..-..-..-classes-mapmarker">MapMarker</a></code>, <code><a href="sdk-for-ios-explore-api-reference-..-..-..-classes-mappolyline">MapPolyline</a></code>, <code><a href="sdk-for-ios-explore-api-reference-..-..-..-classes-mappolygon">MapPolygon</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case mapItems = 0</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC0B10PickFilterC11ContentTypeO03mapF0yA2GmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/mapContent"></a>
<a class="token" href="#/s:7heresdk8MapSceneC0B10PickFilterC11ContentTypeO03mapF0yA2GmF">mapContent</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Pickable map content currently consists of:</p>
<ul>
<li>Embedded carto POI markers that by default are available on the map.</li>
<li>Traffic incidents that are visible when they are enabled using <code><a href="../../../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code>
with <code><a href="../../../Structs/MapFeatures.html#/s:7heresdk11MapFeaturesV16trafficIncidentsSSvpZ">MapFeatures.trafficIncidents</a></code>.</li>
<li>Vehicle restrictions are only available for the Navigate license.
Vehicle restrictions are enabled using <code><a href="../../../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code> with
<code>MapFeatures.VEHICLE_RESTRICTIONS</code>. Please note that the vehicle restriction line marking the
affected street is pickable and not the restriction icon itself.
Only visible POIs, traffic incidents and vehicle restrictions lines can be picked, i.e. only
those categories that are not hidden and those that are not covered by any custom marker.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case mapContent</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC0B10PickFilterC11ContentTypeO15customLayerDatayA2GmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/customLayerData"></a>
<a class="token" href="#/s:7heresdk8MapSceneC0B10PickFilterC11ContentTypeO15customLayerDatayA2GmF">customLayerData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Custom user map content added using custom datasources e.g. <code><a href="sdk-for-ios-explore-api-reference-..-..-..-classes-linedatasource">LineDataSource</a></code>,
<code><a href="sdk-for-ios-explore-api-reference-..-..-..-classes-polygondatasource">PolygonDataSource</a></code> and layers.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case customLayerData</code></pre>
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

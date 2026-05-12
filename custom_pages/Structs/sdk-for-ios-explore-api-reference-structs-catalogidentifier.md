---
title: "CatalogIdentifier Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-catalogidentifier"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- CatalogIdentifier.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/CatalogIdentifier"></a>
<a title="CatalogIdentifier Structure Reference"></a>
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
<a href="../Core.html">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        CatalogIdentifier Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct CatalogIdentifier : Hashable</code></pre>
</div>
</div>
<p>This class is used to identify any catalog in the HERE platform.</p>
<p>A catalog is a storage-representation to store map data on the HERE platform.
The data inside a catalog is divided into layers, where each layer consists
of datasets with similar functional attributes in the physical world.
For example, there can be a layer for road-topology, a layer for
road-attributes (such as speed limits) and a layer for places and business
addresses. All these layers, in different geographic regions, can be grouped together into a
catalog to create a representation of the world we live in, called HERE map.
It can be also used to render a <code><a href="../Classes/MapView.html">MapView</a></code>. Each geographic region is cut into geospatial
tiles for efficient search, map display, routing, map matching, and driver warnings.
Each tile partitions the map data (in one or more layers, depending on the product)
in the geolocation of that specific tile.
The data inside a catalog is logically managed and access controlled
as a single set. If you have any data that you want to bring to the HERE
platform, you need a catalog to contain it.
For additional information about catalogs, and related concepts of data representation
on the HERE platform, refer to
<a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/catalogs.html">the Data API</a>
and <a href="https://www.here.com/docs/bundle/introduction-to-mapping-concepts-user-guide/page/topics/maps-layers-tiles.html">Introduction to Mapping Concepts</a></p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CatalogIdentifierV3hrnSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hrn"></a>
<a class="token" href="#/s:7heresdk17CatalogIdentifierV3hrnSSvp">hrn</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A HERE Resource Name (HRN) for this catalog. This is a unique string returned by the HERE platform when you add a new
catalog to your project. For information about catalog creation process refer to
<a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/creating-a-catalog.html">the Data API</a>
By default, this field points to a default catalog on HERE platform, which contains data for the whole world excluding the region of Japan.
Use <code><a href="../Structs/CatalogConfiguration.html#/s:7heresdk20CatalogConfigurationV10getDefault11catalogTypeAcA0bG0O_tFZ">CatalogConfiguration.getDefault(...)</a></code> to get the default HRN value for use with the HERE platform.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var hrn: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CatalogIdentifierV7versions5Int64VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/version"></a>
<a class="token" href="#/s:7heresdk17CatalogIdentifierV7versions5Int64VSgvp">version</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A version number for a catalog. When accessing a catalog, this version must be specified.
Set <code>nil</code> to automatically get the latest version for a catalog.
The field defaults to <code>nil</code>.
Since the data inside a catalog can be updated, each published modification needs to correlate
to a specific version number.
Note: when <code>CatalogIdentifier</code> created with <code><a href="../Structs/DesiredCatalog.html">DesiredCatalog</a></code> then:</p>
<ul>
<li>numerical <code>-1</code> corresponds to <code><a href="../Classes/CatalogVersionHint.html#/s:7heresdk18CatalogVersionHintC6latest16ignoreCachedDataACSb_tFZ">CatalogVersionHint.latest(...)</a></code> with <code>ignoreCachedData</code> set to <code>true</code>;</li>
<li><code>nil</code> corresponds to <code><a href="../Classes/CatalogVersionHint.html#/s:7heresdk18CatalogVersionHintC6latest16ignoreCachedDataACSb_tFZ">CatalogVersionHint.latest(...)</a></code> with <code>ignoreCachedData</code> set to <code>false</code>;</li>
<li>other numerical values correspond to <code>version</code> passed to <code><a href="../Classes/CatalogVersionHint.html#/s:7heresdk18CatalogVersionHintC8specific7versionACs5Int64V_tFZ">CatalogVersionHint.specific(...)</a></code>.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var version: Int64?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CatalogIdentifierV3hrn7versionACSS_s5Int64VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(hrn:version:)"></a>
<a class="token" href="#/s:7heresdk17CatalogIdentifierV3hrn7versionACSS_s5Int64VSgtcfc">init(hrn:<wbr/>version:<wbr/>)</a>
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
<pre><code>public init(hrn: String = "hrn:here:data::olp-here:ocm", version: Int64? = nil)</code></pre>
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

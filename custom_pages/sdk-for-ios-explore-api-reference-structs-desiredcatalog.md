---
title: "sdk-for-ios-explore-api-reference-structs-desiredcatalog"
slug: "sdk-for-ios-explore-api-reference-structs-desiredcatalog"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DesiredCatalog"></a>
<a title="DesiredCatalog Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-core">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        DesiredCatalog Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>DesiredCatalog</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DesiredCatalog</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access.
The user can specify the HERE Resource Name (HRN) for the catalog along with a hint for the desired version.
If the desired version is not available, the HERE platform will determine the best version to use for a specific catalog or result in error logs.
For information on how to specify the catalog version, see <code><a href="sdk-for-ios-explore-api-reference-..-classes-catalogversionhint">CatalogVersionHint</a></code>.
For information about catalogs and related concepts see <code><a href="sdk-for-ios-explore-api-reference-..-structs-catalogidentifier">CatalogIdentifier</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DesiredCatalogV2idAA0C10IdentifierVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk14DesiredCatalogV2idAA0C10IdentifierVvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The identifier for the catalog to be accessed on the HERE platform.
See <code><a href="sdk-for-ios-explore-api-reference-..-structs-catalogidentifier">CatalogIdentifier</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-catalogidentifier">CatalogIdentifier</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DesiredCatalogV3hrn7versionACSS_AA0C11VersionHintCtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(hrn:version:)"></a>
<a class="token" href="#/s:7heresdk14DesiredCatalogV3hrn7versionACSS_AA0C11VersionHintCtcfc">init(hrn:<wbr/>version:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">hrn</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">version</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-catalogversionhint">CatalogVersionHint</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>hrn</em>
</code>
</td>
<td>
<div>
<p>A HERE Resource Name (HRN) for this catalog. This is a unique string returned by the HERE platform when you add a new
catalog to your project. For more information, see <code><a href="../Structs/CatalogIdentifier.html#/s:7heresdk17CatalogIdentifierV3hrnSSvp">CatalogIdentifier.hrn</a></code></p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>version</em>
</code>
</td>
<td>
<div>
<p>The version to use for this Catalog’s data.
You should use either <code><a href="../Classes/CatalogVersionHint.html#/s:7heresdk18CatalogVersionHintC8specific7versionACs5Int64V_tFZ">CatalogVersionHint.specific(...)</a></code> to specify a specific version of the catalog or
<code><a href="../Classes/CatalogVersionHint.html#/s:7heresdk18CatalogVersionHintC6latest16ignoreCachedDataACSb_tFZ">CatalogVersionHint.latest(...)</a></code> to access the latest version of the catalog available on the HERE platform.
Based on the value in this field, the HERE platform will determine the best version to use for this catalog
or result in error logs if the desired version is not available.</p>
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

`
}</HTMLBlock>

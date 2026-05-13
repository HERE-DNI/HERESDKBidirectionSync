---
title: "Evse Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-evse"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- Evse.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/Evse"></a>
<a title="Evse Structure Reference"></a>
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
        Evse Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct Evse : Hashable</code></pre>
</div>
</div>
<p>Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4EvseV2idSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk4EvseV2idSSSgvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>HERE ID of the EVSE.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var id: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4EvseV5cpoIdSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cpoId"></a>
<a class="token" href="#/s:7heresdk4EvseV5cpoIdSSSgvp">cpoId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The unique ID of an EVSE in the system of the CPO.
This ID is unique in the system of the CPO but not necessarily globally unique.
The format will differ between different CPOs.
This ID is always provided.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var cpoId: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4EvseV03cpoB6Emi3IdSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cpoEvseEmi3Id"></a>
<a class="token" href="#/s:7heresdk4EvseV03cpoB6Emi3IdSSSgvp">cpoEvseEmi3Id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifier in Emi3 format of the EVSE within the Charge Point Operator (CPO) platform.
This id is not always present.
Example of ID format: <code>DE*ICT*E0001897</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var cpoEvseEmi3Id: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4EvseV6statusAA10EVSEStatusOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/status"></a>
<a class="token" href="#/s:7heresdk4EvseV6statusAA10EVSEStatusOSgvp">status</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EVSE status.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var status: EVSEStatus?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4EvseV11lastUpdated10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastUpdated"></a>
<a class="token" href="#/s:7heresdk4EvseV11lastUpdated10Foundation4DateVSgvp">lastUpdated</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Last update of the dynamic connector availability information.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var lastUpdated: Date?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4EvseV10connectorsSayAA13EVSEConnectorVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectors"></a>
<a class="token" href="#/s:7heresdk4EvseV10connectorsSayAA13EVSEConnectorVGvp">connectors</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of connectors of this EVSE.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var connectors: [EVSEConnector]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4EvseV2id5cpoId0db4Emi3E06status11lastUpdated10connectorsACSSSg_A2jA10EVSEStatusOSg10Foundation4DateVSgSayAA13EVSEConnectorVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:cpoId:cpoEvseEmi3Id:status:lastUpdated:connectors:)"></a>
<a class="token" href="#/s:7heresdk4EvseV2id5cpoId0db4Emi3E06status11lastUpdated10connectorsACSSSg_A2jA10EVSEStatusOSg10Foundation4DateVSgSayAA13EVSEConnectorVGtcfc">init(id:<wbr/>cpoId:<wbr/>cpoEvseEmi3Id:<wbr/>status:<wbr/>lastUpdated:<wbr/>connectors:<wbr/>)</a>
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
<pre><code>public init(id: String? = nil, cpoId: String? = nil, cpoEvseEmi3Id: String? = nil, status: EVSEStatus? = nil, lastUpdated: Date? = nil, connectors: [EVSEConnector] = [])</code></pre>
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

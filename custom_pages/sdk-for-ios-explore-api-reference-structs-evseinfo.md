---
title: "EVSEInfo"
slug: "sdk-for-ios-explore-api-reference-structs-evseinfo"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVSEInfo"></a>
<a title="EVSEInfo Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-search">Search</a>

        EVSEInfo Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVSEInfo</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVSEInfo</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents an EVSE at the charging point.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8EVSEInfoV3uidSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/uid"></a>
<a class="token" href="#/s:7heresdk8EVSEInfoV3uidSSvp">uid</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Uniquely identifies the EVSE within the CPOs platform (and suboperator platforms).
For example a database ID or the actual “EVSE ID”. This field can never be changed, modified or renamed.
This is the ‘technical’ identification of the EVSE, not to be used as ‘human readable’ identification, use the field <code><a href="../Structs/EVSEInfo.html#/s:7heresdk8EVSEInfoV2idSSSgvp">EVSEInfo.id</a></code> for that.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">uid</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8EVSEInfoV2idSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk8EVSEInfoV2idSSSgvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Human-readable globally unique identifier for the EVSE.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8EVSEInfoV6evseIDSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evseID"></a>
<a class="token" href="#/s:7heresdk8EVSEInfoV6evseIDSSSgvp">evseID</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifier compliant with the EVSE ID from eMI3 standard version V1.0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">evseID</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8EVSEInfoV6statusAA9EVSEStateOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/status"></a>
<a class="token" href="#/s:7heresdk8EVSEInfoV6statusAA9EVSEStateOvp">status</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Status of the EVSE.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">status</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-evsestate">EVSEState</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8EVSEInfoV11lastUpdated10Foundation4DateVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastUpdated"></a>
<a class="token" href="#/s:7heresdk8EVSEInfoV11lastUpdated10Foundation4DateVvp">lastUpdated</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Timestamp when the status of this EVSE was last updated.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lastUpdated</span><span class="p">:</span> <span class="kt">Date</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8EVSEInfoV10connectorsSayAA19EVChargingConnectorVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectors"></a>
<a class="token" href="#/s:7heresdk8EVSEInfoV10connectorsSayAA19EVChargingConnectorVGvp">connectors</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of available connectors on the EVSE. An operational EVSE should have at least one connector.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">connectors</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evchargingconnector">EVChargingConnector</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8EVSEInfoV12capabilitiesSayAA14EVSECapabilityOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/capabilities"></a>
<a class="token" href="#/s:7heresdk8EVSEInfoV12capabilitiesSayAA14EVSECapabilityOGvp">capabilities</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Capabilities of the EVSE.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">capabilities</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-evsecapability">EVSECapability</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8EVSEInfoV10floorLevelSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/floorLevel"></a>
<a class="token" href="#/s:7heresdk8EVSEInfoV10floorLevelSSSgvp">floorLevel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Floor level on which the EVSE is located.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">floorLevel</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8EVSEInfoV17physicalReferenceSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/physicalReference"></a>
<a class="token" href="#/s:7heresdk8EVSEInfoV17physicalReferenceSSSgvp">physicalReference</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A number or string printed on the outside of the EVSE for visual identification.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">physicalReference</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8EVSEInfoV11coordinatesAA14GeoCoordinatesVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk8EVSEInfoV11coordinatesAA14GeoCoordinatesVSgvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geographic coordinates of the EVSE.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8EVSEInfoV15paymentSupportsSayAA18EVSEPaymentSupportOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/paymentSupports"></a>
<a class="token" href="#/s:7heresdk8EVSEInfoV15paymentSupportsSayAA18EVSEPaymentSupportOGvp">paymentSupports</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of payment support functionalities on EVSE for ad-hoc customers (without pre-registration).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">paymentSupports</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-evsepaymentsupport">EVSEPaymentSupport</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8EVSEInfoV3uid2id6evseID6status11lastUpdated10connectors12capabilities10floorLevel17physicalReference11coordinates15paymentSupportsACSS_SSSgAoA9EVSEStateO10Foundation4DateVSayAA19EVChargingConnectorVGSayAA14EVSECapabilityOGA2oA14GeoCoordinatesVSgSayAA18EVSEPaymentSupportOGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(uid:id:evseID:status:lastUpdated:connectors:capabilities:floorLevel:physicalReference:coordinates:paymentSupports:)"></a>
<a class="token" href="#/s:7heresdk8EVSEInfoV3uid2id6evseID6status11lastUpdated10connectors12capabilities10floorLevel17physicalReference11coordinates15paymentSupportsACSS_SSSgAoA9EVSEStateO10Foundation4DateVSayAA19EVChargingConnectorVGSayAA14EVSECapabilityOGA2oA14GeoCoordinatesVSgSayAA18EVSEPaymentSupportOGtcfc">init(uid:<wbr/>id:<wbr/>evseID:<wbr/>status:<wbr/>lastUpdated:<wbr/>connectors:<wbr/>capabilities:<wbr/>floorLevel:<wbr/>physicalReference:<wbr/>coordinates:<wbr/>paymentSupports:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">uid</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">evseID</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">status</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-evsestate">EVSEState</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-evsestate">EVSEState</a></span><span class="o">.</span><span class="n">unknown</span><span class="p">,</span> <span class="nv">lastUpdated</span><span class="p">:</span> <span class="kt">Date</span> <span class="o">=</span> <span class="kt">Date</span><span class="p">(</span><span class="nv">timeIntervalSince1970</span><span class="p">:</span> <span class="mi">0</span><span class="p">),</span> <span class="nv">connectors</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evchargingconnector">EVChargingConnector</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">capabilities</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-evsecapability">EVSECapability</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">floorLevel</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">physicalReference</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">paymentSupports</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-evsepaymentsupport">EVSEPaymentSupport</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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

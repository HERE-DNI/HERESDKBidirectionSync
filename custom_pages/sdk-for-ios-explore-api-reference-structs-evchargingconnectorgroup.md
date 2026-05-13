---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-structs-evchargingconnectorgroup"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVChargingConnectorGroup.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingConnectorGroup"></a>
<a title="EVChargingConnectorGroup Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVChargingConnectorGroup Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVChargingConnectorGroup</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingConnectorGroup</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents the connector group at the charging location.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24EVChargingConnectorGroupV13connectorTypeSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectorType"></a>
<a class="token" href="#/s:7heresdk24EVChargingConnectorGroupV13connectorTypeSSvp">connectorType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The standard (type) of the connectors belonging to this group.
Should be one of the constants defined in <code><a href="sdk-for-ios-explore-api-reference-..-structs-evchargingconnectortype">EVChargingConnectorType</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">connectorType</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24EVChargingConnectorGroupV15maxPowerInWattss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxPowerInWatts"></a>
<a class="token" href="#/s:7heresdk24EVChargingConnectorGroupV15maxPowerInWattss5Int32Vvp">maxPowerInWatts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum power that can be delivered by the connectors, in watts (W).
Connectors without max power are not grouped.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxPowerInWatts</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24EVChargingConnectorGroupV10connectorsSayAA0bC9ReferenceVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectors"></a>
<a class="token" href="#/s:7heresdk24EVChargingConnectorGroupV10connectorsSayAA0bC9ReferenceVGvp">connectors</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Array of EVSE + connector(s) pairs that belong to the group.
Provides access to EVSE statuses and more detailed connector characteristics.
Available only if <code>EVChargingLocationFeature.EVSES</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">connectors</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-evchargingconnectorreference">EVChargingConnectorReference</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24EVChargingConnectorGroupV14connectorCounts5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectorCount"></a>
<a class="token" href="#/s:7heresdk24EVChargingConnectorGroupV14connectorCounts5Int32Vvp">connectorCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of connectors in the group. If an EVSE has multiple identical
connectors they are counted as one as only one is accessible at a time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">connectorCount</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24EVChargingConnectorGroupV09availableC5Counts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/availableConnectorCount"></a>
<a class="token" href="#/s:7heresdk24EVChargingConnectorGroupV09availableC5Counts5Int32VSgvp">availableConnectorCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of connectors available for use at the time of query.
The field is not present if the availability is not known.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">availableConnectorCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24EVChargingConnectorGroupV13tariffIndexesSays5Int32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tariffIndexes"></a>
<a class="token" href="#/s:7heresdk24EVChargingConnectorGroupV13tariffIndexesSays5Int32VGvp">tariffIndexes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tariffs for the connector group, represented by indexes to the charging station’s tariffs-list.
Available only if <code>EVChargingLocationFeature.TARIFFS</code> is included in
<code>EVSearchOptions.additional_features</code>, otherwise empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tariffIndexes</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24EVChargingConnectorGroupV13connectorType15maxPowerInWatts10connectors0E5Count09availablecL013tariffIndexesACSS_s5Int32VSayAA0bC9ReferenceVGA2KSgSayAKGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(connectorType:maxPowerInWatts:connectors:connectorCount:availableConnectorCount:tariffIndexes:)"></a>
<a class="token" href="#/s:7heresdk24EVChargingConnectorGroupV13connectorType15maxPowerInWatts10connectors0E5Count09availablecL013tariffIndexesACSS_s5Int32VSayAA0bC9ReferenceVGA2KSgSayAKGtcfc">init(connectorType:<wbr/>maxPowerInWatts:<wbr/>connectors:<wbr/>connectorCount:<wbr/>availableConnectorCount:<wbr/>tariffIndexes:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">connectorType</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">maxPowerInWatts</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="nv">connectors</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-evchargingconnectorreference">EVChargingConnectorReference</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">connectorCount</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="nv">availableConnectorCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">tariffIndexes</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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

</div>
`
}</HTMLBlock>

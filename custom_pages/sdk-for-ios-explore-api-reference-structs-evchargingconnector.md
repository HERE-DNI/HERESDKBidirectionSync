---
title: "Search / EVChargingConnector"
slug: "sdk-for-ios-explore-api-reference-structs-evchargingconnector"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingConnector"></a>
<a title="EVChargingConnector Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVChargingConnector Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVChargingConnector</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingConnector</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a connector at the charging point.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19EVChargingConnectorV2idSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk19EVChargingConnectorV2idSSvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifier of the connector within the EVSE.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19EVChargingConnectorV13connectorTypeSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectorType"></a>
<a class="token" href="#/s:7heresdk19EVChargingConnectorV13connectorTypeSSvp">connectorType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standardized type of the connector.
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
<a name="/s:7heresdk19EVChargingConnectorV6formatAA0bC6FormatOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/format"></a>
<a class="token" href="#/s:7heresdk19EVChargingConnectorV6formatAA0bC6FormatOvp">format</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Format of the connector, whether it is a socket or a cable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">format</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-evchargingconnectorformat">EVChargingConnectorFormat</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19EVChargingConnectorV9powerTypeAA05PowerE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/powerType"></a>
<a class="token" href="#/s:7heresdk19EVChargingConnectorV9powerTypeAA05PowerE0Ovp">powerType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of electrical power used by the connector.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">powerType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-powertype">PowerType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19EVChargingConnectorV17maxVoltageInVoltss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxVoltageInVolts"></a>
<a class="token" href="#/s:7heresdk19EVChargingConnectorV17maxVoltageInVoltss5Int32Vvp">maxVoltageInVolts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Max voltage (in volts) of the connector.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxVoltageInVolts</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19EVChargingConnectorV19maxCurrentInAmperess5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxCurrentInAmperes"></a>
<a class="token" href="#/s:7heresdk19EVChargingConnectorV19maxCurrentInAmperess5Int32Vvp">maxCurrentInAmperes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Max current (in amperes) of the connector.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxCurrentInAmperes</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19EVChargingConnectorV15maxPowerInWattss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxPowerInWatts"></a>
<a class="token" href="#/s:7heresdk19EVChargingConnectorV15maxPowerInWattss5Int32VSgvp">maxPowerInWatts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Max power (in watts) of the connector, if available.
This should be set when the maximum electric power is lower than the calculated value from
voltage and amperage.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxPowerInWatts</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19EVChargingConnectorV21termsAndConditionsUrlSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/termsAndConditionsUrl"></a>
<a class="token" href="#/s:7heresdk19EVChargingConnectorV21termsAndConditionsUrlSSSgvp">termsAndConditionsUrl</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>URL to the operator’s terms and conditions, if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">termsAndConditionsUrl</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19EVChargingConnectorV13tariffIndexesSays5Int32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tariffIndexes"></a>
<a class="token" href="#/s:7heresdk19EVChargingConnectorV13tariffIndexesSays5Int32VGvp">tariffIndexes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tariffs for the connector, presented by indexes to the charging station’s tariffs-list.
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
<a name="/s:7heresdk19EVChargingConnectorV2id13connectorType6format05powerF017maxVoltageInVolts0i7CurrentK7Amperes0i5PowerK5Watts21termsAndConditionsUrl13tariffIndexesACSS_SSAA0bC6FormatOAA0oF0Os5Int32VA2RSgSSSgSayARGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:connectorType:format:powerType:maxVoltageInVolts:maxCurrentInAmperes:maxPowerInWatts:termsAndConditionsUrl:tariffIndexes:)"></a>
<a class="token" href="#/s:7heresdk19EVChargingConnectorV2id13connectorType6format05powerF017maxVoltageInVolts0i7CurrentK7Amperes0i5PowerK5Watts21termsAndConditionsUrl13tariffIndexesACSS_SSAA0bC6FormatOAA0oF0Os5Int32VA2RSgSSSgSayARGtcfc">init(id:<wbr/>connectorType:<wbr/>format:<wbr/>powerType:<wbr/>maxVoltageInVolts:<wbr/>maxCurrentInAmperes:<wbr/>maxPowerInWatts:<wbr/>termsAndConditionsUrl:<wbr/>tariffIndexes:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">connectorType</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">format</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-evchargingconnectorformat">EVChargingConnectorFormat</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-evchargingconnectorformat">EVChargingConnectorFormat</a></span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="nv">powerType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-powertype">PowerType</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-powertype">PowerType</a></span><span class="o">.</span><span class="n">ac1phase</span><span class="p">,</span> <span class="nv">maxVoltageInVolts</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">maxCurrentInAmperes</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">maxPowerInWatts</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">termsAndConditionsUrl</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">tariffIndexes</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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

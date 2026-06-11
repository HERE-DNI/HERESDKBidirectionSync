---
title: "sdk-for-ios-explore-api-reference-structs-placefilter-ev"
slug: "sdk-for-ios-explore-api-reference-structs-placefilter-ev"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Ev"></a>
<a title="Ev Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-search">Search</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-structs-placefilter">PlaceFilter</a>
<img alt="" id="carat" src="/carat.png"/>
        Ev Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Ev</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Ev</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Constraints that are applicable on the places of category EV station.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PlaceFilterV2EvV13supplierNamesSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/supplierNames"></a>
<a class="token" href="#/s:7heresdk11PlaceFilterV2EvV13supplierNamesSaySSGvp">supplierNames</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets a constraint on the charge point operator name of the EV station.</p>
<p>Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">supplierNames</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PlaceFilterV2EvV16connectorTypeIDsSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectorTypeIDs"></a>
<a class="token" href="#/s:7heresdk11PlaceFilterV2EvV16connectorTypeIDsSaySSGvp">connectorTypeIDs</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Filter to retrieve EV charging stations with at least one of the connector type IDs.
For more information on the current connector types, see
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html</a></p>
<p>Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">connectorTypeIDs</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PlaceFilterV2EvV19minPowerInKilowattsSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/minPowerInKilowatts"></a>
<a class="token" href="#/s:7heresdk11PlaceFilterV2EvV19minPowerInKilowattsSdSgvp">minPowerInKilowatts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Filter to retrieve EV charging stations with the given minimum charging power in KW
delivered by at least one of the station EVSE.
Not supported for <code>suggestByText</code> in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">minPowerInKilowatts</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PlaceFilterV2EvV34eMobilityServiceProviderPartnerIDsSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/eMobilityServiceProviderPartnerIDs"></a>
<a class="token" href="#/s:7heresdk11PlaceFilterV2EvV34eMobilityServiceProviderPartnerIDsSaySSGvp">eMobilityServiceProviderPartnerIDs</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Filter to retrieve EV charging stations with at least one matching e-Mobility Service Provider Partner ID.</p>
<p>Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">eMobilityServiceProviderPartnerIDs</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PlaceFilterV2EvV11currentTypeAA07CurrentF0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currentType"></a>
<a class="token" href="#/s:7heresdk11PlaceFilterV2EvV11currentTypeAA07CurrentF0OSgvp">currentType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Filter to retrieve EV charging stations with the given current type
provided at one of the station EVSE. Accepted is either AC or DC.
Not supported for <code>suggestByText</code> in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">currentType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-currenttype">CurrentType</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PlaceFilterV2EvV13supplierNames16connectorTypeIDs19minPowerInKilowatts031eMobilityServiceProviderPartnerI007currentH0AESaySSG_AKSdSgAkA07CurrentH0OSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(supplierNames:connectorTypeIDs:minPowerInKilowatts:eMobilityServiceProviderPartnerIDs:currentType:)"></a>
<a class="token" href="#/s:7heresdk11PlaceFilterV2EvV13supplierNames16connectorTypeIDs19minPowerInKilowatts031eMobilityServiceProviderPartnerI007currentH0AESaySSG_AKSdSgAkA07CurrentH0OSgtcfc">init(supplierNames:<wbr/>connectorTypeIDs:<wbr/>minPowerInKilowatts:<wbr/>eMobilityServiceProviderPartnerIDs:<wbr/>currentType:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>supplierNames: Sets a constraint on the charge point operator name of the EV station.</li>
</ul>
<p>Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
<ul>
<li>connectorTypeIDs: Filter to retrieve EV charging stations with at least one of the connector type IDs.
For more information on the current connector types, see
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html</a></li>
</ul>
<p>Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
<ul>
<li>minPowerInKilowatts: Filter to retrieve EV charging stations with the given minimum charging power in KW
delivered by at least one of the station EVSE.
Not supported for <code>suggestByText</code> in <code>OfflineSearchEngine</code> (only available for the Navigate license).</li>
<li>eMobilityServiceProviderPartnerIDs: Filter to retrieve EV charging stations with at least one matching e-Mobility Service Provider Partner ID.</li>
</ul>
<p>Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
<ul>
<li>currentType: Filter to retrieve EV charging stations with the given current type
provided at one of the station EVSE. Accepted is either AC or DC.
Not supported for <code>suggestByText</code> in <code>OfflineSearchEngine</code> (only available for the Navigate license).</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">supplierNames</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">connectorTypeIDs</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">minPowerInKilowatts</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">eMobilityServiceProviderPartnerIDs</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">currentType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-currenttype">CurrentType</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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

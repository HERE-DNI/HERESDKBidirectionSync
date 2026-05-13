---
title: "EngineBaseURL Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-enginebaseurl"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EngineBaseURL.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/EngineBaseURL"></a>
<a title="EngineBaseURL Enumeration Reference"></a>
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
<a href="sdk-for-ios-explore-api-reference-..-core">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EngineBaseURL Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum EngineBaseURL : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EngineBaseURLO06searchB0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/searchEngine"></a>
<a class="token" href="#/s:7heresdk13EngineBaseURLO06searchB0yA2CmF">searchEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates a <code><a href="sdk-for-ios-explore-api-reference-..-classes-searchengine">SearchEngine</a></code> endpoint.
Note that the provided string value will replace the base URL.
The endpoint names for this engine are “v1/discover”, “v1/geocode”, “v1/revgeocode”,
“v1/autosuggest”, “v1/lookup” and “v1/browse”. A valid base string value
could look like “<a href="http://www.my-company.com">www.my-company.com</a>”. An example of the resulting URL for the first
endpoint looks like this: “<a href="https://www.my-company.com/v1/discover">https://www.my-company.com/v1/discover</a>” appended with
query data. You need to ensure that the provided base URL supports all required endpoints.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case searchEngine</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EngineBaseURLO07routingB0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/routingEngine"></a>
<a class="token" href="#/s:7heresdk13EngineBaseURLO07routingB0yA2CmF">routingEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates a <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code> endpoint.
Note that the provided string value will replace the base URL.
The endpoint names for this engine are “v8/routes”, “v8/import”. A valid base string value
could look like “<a href="http://www.my-company.com">www.my-company.com</a>”. An example of the resulting URL for the first
endpoint looks like this: “<a href="https://www.my-company.com/v8/routes">https://www.my-company.com/v8/routes</a>” appended with
query data. You need to ensure that the provided base URL supports all required endpoints.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case routingEngine</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EngineBaseURLO14authenticationyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/authentication"></a>
<a class="token" href="#/s:7heresdk13EngineBaseURLO14authenticationyA2CmF">authentication</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates base url for <code><a href="sdk-for-ios-explore-api-reference-..-classes-authentication">Authentication</a></code>.
Note that the provided string value will replace the base URL.
The endpoint name for this base url is “oauth2/token”. A valid base string value
could look like “<a href="http://www.my-company.com">www.my-company.com</a>”. An example of the resulting URL for the
endpoint looks like this: “<a href="https://www.my-company.com/oauth2/token">https://www.my-company.com/oauth2/token</a>” appended with
query data. You need to ensure that the provided base URL supports required endpoint.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case authentication</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EngineBaseURLO7dsProxyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/dsProxy"></a>
<a class="token" href="#/s:7heresdk13EngineBaseURLO7dsProxyyA2CmF">dsProxy</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the endpoint URL for a map catalog. This is only relevant for the Navigate license that uses
OCM based map data when a custom catalog configuration
should be loaded.
By default, the data Service proxy, in short <code>EngineBaseURL.dsProxy</code>, is set to “<a href="https://direct.data.api.platform.here.com/direct/v1">https://direct.data.api.platform.here.com/direct/v1</a>”.
When a custom catalog should be used, then the HERE SDK will internally do a lookup request
to find out which URL to use to access catalog. In order to bypass this extra request, we
recommend to set the URL upfront when initializing the HERE SDK.
For example, a valid <code>EngineBaseURL.dsProxy</code> for a custom catalog may look like this:
“<a href="https://data.api.platform.yourcompany.com/direct/v1">https://data.api.platform.yourcompany.com/direct/v1</a>”.
Note that this is not a network proxy setting.
If you do not load a custom catalog configuration, you can ignore this setting.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case dsProxy</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EngineBaseURLO11trafficDatayA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/trafficData"></a>
<a class="token" href="#/s:7heresdk13EngineBaseURLO11trafficDatayA2CmF">trafficData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates a <code>Traffic Data</code> endpoint.
Note that the provided string value will replace the base URL.
This is only relevant for TrafficEngine. For traffic incident and flow presented in the map view,
please use <code><a href="../Enums/EngineBaseURL.html#/s:7heresdk13EngineBaseURLO24trafficVectorTileServiceyA2CmF">EngineBaseURL.trafficVectorTileService</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case trafficData</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EngineBaseURLO24trafficVectorTileServiceyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/trafficVectorTileService"></a>
<a class="token" href="#/s:7heresdk13EngineBaseURLO24trafficVectorTileServiceyA2CmF">trafficVectorTileService</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates a <code>Traffic Vector Tile API</code> endpoint.
Note that the provided string value will replace the base URL.
This is only relevant for traffic presented in the map view. For the TrafficEngine, please use <code><a href="../Enums/EngineBaseURL.html#/s:7heresdk13EngineBaseURLO11trafficDatayA2CmF">EngineBaseURL.trafficData</a></code>.</p>
<p>The service needs to comply with <a href="https://www.here.com/docs/bundle/traffic-vector-tile-api-v2-api-reference/page/index.html">https://www.here.com/docs/bundle/traffic-vector-tile-api-v2-api-reference/page/index.html</a>
The endpoint name for this engine is “v2/traffictiles”. A valid base string value
could look like “<a href="http://www.my-company.com">www.my-company.com</a>”. The resulting URL looks like this:
“<a href="https://www.my-company.com/v2/traffictiles/%7Blayer%7D/mc/%7Bz%7D/%7Bx%7D/%7By%7D/omv">https://www.my-company.com/v2/traffictiles/{layer}/mc/{z}/{x}/{y}/omv</a>”, with concrete tile
IDs in {x}, {y}, {z} and {layers} in (flow, incidents).
You need to ensure that the provided base URL supports all required endpoints.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case trafficVectorTileService</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EngineBaseURLO17rasterTileServiceyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rasterTileService"></a>
<a class="token" href="#/s:7heresdk13EngineBaseURLO17rasterTileServiceyA2CmF">rasterTileService</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates a <code>Raster Tile API</code> endpoint.
Note that the provided string value will replace the URL template. A valid URL template value
could look like:
“<a href="https://www.my-company.com/satellite.day/%7Bz%7D/%7Bx%7D/%7By%7D/512/jpg">https://www.my-company.com/satellite.day/{z}/{x}/{y}/512/jpg</a>”</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rasterTileService</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EngineBaseURLO014isolineRoutingB0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/isolineRoutingEngine"></a>
<a class="token" href="#/s:7heresdk13EngineBaseURLO014isolineRoutingB0yA2CmF">isolineRoutingEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates a <code><a href="sdk-for-ios-explore-api-reference-..-classes-isolineroutingengine">IsolineRoutingEngine</a></code> endpoint.
Note that the provided string value will replace the base URL.
The endpoint names for this engine are “v8/isolines”. A valid base string value
could look like “<a href="http://www.my-company.com">www.my-company.com</a>”. An example of the resulting URL for the first
endpoint looks like this: “<a href="https://www.my-company.com/v8/isolines">https://www.my-company.com/v8/isolines</a>” appended with
query data. You need to ensure that the provided base URL supports all required endpoints.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case isolineRoutingEngine</code></pre>
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

---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-enums-searcherror"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- SearchError.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/SearchError"></a>
<a title="SearchError Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SearchError Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SearchError</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">SearchError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Specifies possible errors that may result from a search query.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO20authenticationFailedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/authenticationFailed"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO20authenticationFailedyA2CmF">authenticationFailed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Search operation is not authenticated. Check your credentials.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">authenticationFailed</span> <span class="o">=</span> <span class="mi">1</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO18maxItemsOutOfRangeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/maxItemsOutOfRange"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO18maxItemsOutOfRangeyA2CmF">maxItemsOutOfRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Should be in the range [1, 100].</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">maxItemsOutOfRange</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO07parsingC0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/parsingError"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO07parsingC0yA2CmF">parsingError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Error while parsing response data.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">parsingError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO14noResultsFoundyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noResultsFound"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO14noResultsFoundyA2CmF">noResultsFound</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>No results found.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noResultsFound</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO04httpC0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/httpError"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO04httpC0yA2CmF">httpError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Network request error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">httpError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO17serverUnreachableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/serverUnreachable"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO17serverUnreachableyA2CmF">serverUnreachable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Server unreachable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">serverUnreachable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO9forbiddenyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/forbidden"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">forbidden</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The credentials given do not provide access to the resource requested.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">forbidden</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO18exceededUsageLimityA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/exceededUsageLimit"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO18exceededUsageLimityA2CmF">exceededUsageLimit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Credentials exceeded the allowed requests limit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">exceededUsageLimit</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO15operationFailedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/operationFailed"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO15operationFailedyA2CmF">operationFailed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Operation failed due to an internal error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">operationFailed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO18operationCancelledyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/operationCancelled"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO18operationCancelledyA2CmF">operationCancelled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Operation cancelled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">operationCancelled</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO8timedOutyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/timedOut"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO8timedOutyA2CmF">timedOut</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The request timed out.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">timedOut</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO7offlineyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/offline"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO7offlineyA2CmF">offline</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The device does not have an internet connection.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">offline</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO12queryTooLongyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/queryTooLong"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO12queryTooLongyA2CmF">queryTooLong</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Query is too long, max. size is 300 characters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">queryTooLong</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO13filterTooLongyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/filterTooLong"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO13filterTooLongyA2CmF">filterTooLong</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Filter is too long, max. size is 300 characters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">filterTooLong</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO25proxyAuthenticationFailedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/proxyAuthenticationFailed"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO25proxyAuthenticationFailedyA2CmF">proxyAuthenticationFailed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Proxy is not authenticated. Check your proxy credentials.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">proxyAuthenticationFailed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO22proxyServerUnreachableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/proxyServerUnreachable"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO22proxyServerUnreachableyA2CmF">proxyServerUnreachable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Proxy server unreachable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">proxyServerUnreachable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO10queryEmptyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/queryEmpty"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO10queryEmptyyA2CmF">queryEmpty</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Empty query</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">queryEmpty</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO11invalidAreayA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidArea"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO11invalidAreayA2CmF">invalidArea</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Box or circle area of query is invalid</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">invalidArea</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO11filterEmptyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/filterEmpty"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO11filterEmptyyA2CmF">filterEmpty</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Filter is empty</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">filterEmpty</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO23invalidCorridorPolylineyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidCorridorPolyline"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO23invalidCorridorPolylineyA2CmF">invalidCorridorPolyline</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Corridor area polyline size is less than 2 points</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">invalidCorridorPolyline</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO10invalidUrlyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidUrl"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO10invalidUrlyA2CmF">invalidUrl</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Url is invalid</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">invalidUrl</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO25invalidCustomOptionFormatyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidCustomOptionFormat"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO25invalidCustomOptionFormatyA2CmF">invalidCustomOptionFormat</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Custom options are set in an invalid format in the query</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">invalidCustomOptionFormat</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO17invalidTruckClassyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidTruckClass"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO17invalidTruckClassyA2CmF">invalidTruckClass</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Light truck class is passed in the filter</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">invalidTruckClass</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO10badRequestyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/badRequest"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO10badRequestyA2CmF">badRequest</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Bad network request</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">badRequest</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO11mapNotReadyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/mapNotReady"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO11mapNotReadyyA2CmF">mapNotReady</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Offline map data is incomplete for the requested operation.
Regions are not downloaded or are in the <code>Pending</code> state.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">mapNotReady</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SearchErrorO19layersNotDownloadedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/layersNotDownloaded"></a>
<a class="token" href="#/s:7heresdk11SearchErrorO19layersNotDownloadedyA2CmF">layersNotDownloaded</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Downloaded regions missing <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO19offlineSearchGlobalyA2EmF">LayerConfiguration.Feature.offlineSearchGlobal</a></code>
feature. Update or redownload regions with enabled feature.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">layersNotDownloaded</span></code></pre>
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

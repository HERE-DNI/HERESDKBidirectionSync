---
title: "PassThroughFeature Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-passthroughfeature"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- PassThroughFeature.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/PassThroughFeature"></a>
<a title="PassThroughFeature Enumeration Reference"></a>
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
        PassThroughFeature Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum PassThroughFeature : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Represents features that are allowed to consume online data when the HERE SDK’s offline mode
is activated via <code><a href="../Classes/SDKNativeEngine.html#/s:7heresdk15SDKNativeEngineC13isOfflineModeSbvp">SDKNativeEngine.isOfflineMode</a></code> and/or
<code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV11offlineModeSbvp">SDKOptions.offlineMode</a></code>.</p>
<p>Note: This is a beta release of this feature,
so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PassThroughFeatureO11trafficDatayA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/trafficData"></a>
<a class="token" href="#/s:7heresdk18PassThroughFeatureO11trafficDatayA2CmF">trafficData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>When set, then the <code><a href="../Classes/TrafficEngine.html">TrafficEngine</a></code> is not blocked from initiating online connections to search for
traffic data such as incidents.</p>
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
<a name="/s:7heresdk18PassThroughFeatureO16trafficTilesFlowyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/trafficTilesFlow"></a>
<a class="token" href="#/s:7heresdk18PassThroughFeatureO16trafficTilesFlowyA2CmF">trafficTilesFlow</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>When set, then the corresponding <code>MapFeature</code> will not be blocked and online connections can be
initiated by the HERE SDK to retrieve traffic flow data.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case trafficTilesFlow</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PassThroughFeatureO21trafficTilesIncidentsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/trafficTilesIncidents"></a>
<a class="token" href="#/s:7heresdk18PassThroughFeatureO21trafficTilesIncidentsyA2CmF">trafficTilesIncidents</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>When set, then the corresponding <code>MapFeature</code> will not be blocked and online connections can be
initiated by the HERE SDK to retrieve traffic incident data.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case trafficTilesIncidents</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PassThroughFeatureO13onlineRoutingyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/onlineRouting"></a>
<a class="token" href="#/s:7heresdk18PassThroughFeatureO13onlineRoutingyA2CmF">onlineRouting</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>When set, online routing can be performed by the HERE SDK, allowing the retrieval of up-to-date
routing information from online services even when offline mode is enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case onlineRouting</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PassThroughFeatureO12onlineSearchyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/onlineSearch"></a>
<a class="token" href="#/s:7heresdk18PassThroughFeatureO12onlineSearchyA2CmF">onlineSearch</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>When set, online search can be performed by the HERE SDK, allowing the retrieval of up-to-date
search information from online services even when offline mode is enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case onlineSearch</code></pre>
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

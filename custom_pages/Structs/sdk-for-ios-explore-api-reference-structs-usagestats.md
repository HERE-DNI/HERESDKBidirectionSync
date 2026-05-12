---
title: "UsageStats Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-usagestats"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- UsageStats.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/UsageStats"></a>
<a title="UsageStats Structure Reference"></a>
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
        UsageStats Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct UsageStats</code></pre>
</div>
</div>
<p>A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV07networkC0SayAC07NetworkC0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/networkStats"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV07networkC0SayAC07NetworkC0VGvp">networkStats</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides network statistics.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var networkStats: [UsageStats.NetworkStats]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7featureAC7FeatureOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/feature"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7featureAC7FeatureOvp">feature</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the HERE SDK feature associated with the gathered usage statistics.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var feature: UsageStats.Feature</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV07networkC07featureACSayAC07NetworkC0VG_AC7FeatureOtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(networkStats:feature:)"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV07networkC07featureACSayAC07NetworkC0VG_AC7FeatureOtcfc">init(networkStats:<wbr/>feature:<wbr/>)</a>
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
<pre><code>public init(networkStats: [UsageStats.NetworkStats], feature: UsageStats.Feature)</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/Feature"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO">Feature</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the feature enum associated with the gathered usage stats.</p>
<a class="slightly-smaller" href="../Structs/UsageStats/Feature.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum Feature : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV07NetworkC0V"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/NetworkStats"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV07NetworkC0V">NetworkStats</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides network statistics in bytes per method.</p>
<a class="slightly-smaller" href="../Structs/UsageStats/NetworkStats.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct NetworkStats</code></pre>
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

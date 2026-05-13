---
title: "Routing / Toll"
slug: "sdk-for-ios-explore-api-reference-structs-toll"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Toll"></a>
<a title="Toll Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        Toll Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Toll</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Toll</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This struct presents all the data for a toll.</p>
<p><strong>Note</strong>: If you’re using the <code>OfflineRoutingEngine</code>, be aware that this feature is
currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors.
Additionally, this feature and related APIs may be updated in future releases
without going through the deprecation process. Note that the <code>OfflineRoutingEngine</code>
is only available for the Navigate license. If you’re using the
<code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code>, this feature is considered to be stable.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4TollV11countryCodeSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/countryCode"></a>
<a class="token" href="#/s:7heresdk4TollV11countryCodeSSvp">countryCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The country in which the toll is to be paid in ISO-3166-1 alpha-3 format, e.g. “USA”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">countryCode</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4TollV11tollSystemsSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollSystems"></a>
<a class="token" href="#/s:7heresdk4TollV11tollSystemsSaySSGvp">tollSystems</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Names of the multiple toll systems which are associated with the toll, e.g. [“ATLANDES“, "ASF”, “COFIROUTE”].
When the toll information covers several toll roads and the toll system of the each road is different,
all toll system names are listed here and the last element will be one of the exit toll booth.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tollSystems</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4TollV5faresSayAA0B4FareVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/fares"></a>
<a class="token" href="#/s:7heresdk4TollV5faresSayAA0B4FareVGvp">fares</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of toll fares possible for the toll which may depend on time of day, payment method, vehicle
characteristics, etc. If there are multiple toll fares that the router cannot disambiguate, then the
list will contain more than one toll fare. Note that this list contains at least one element, i.e. it
is never empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">fares</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-tollfare">TollFare</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4TollV11countryCode11tollSystems5faresACSS_SaySSGSayAA0B4FareVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(countryCode:tollSystems:fares:)"></a>
<a class="token" href="#/s:7heresdk4TollV11countryCode11tollSystems5faresACSS_SaySSGSayAA0B4FareVGtcfc">init(countryCode:<wbr/>tollSystems:<wbr/>fares:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">countryCode</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">tollSystems</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">],</span> <span class="nv">fares</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-tollfare">TollFare</a></span><span class="p">])</span></code></pre>
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

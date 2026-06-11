---
title: "sdk-for-ios-explore-api-reference-structs-tollfare"
slug: "sdk-for-ios-explore-api-reference-structs-tollfare"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TollFare"></a>
<a title="TollFare Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        TollFare Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TollFare</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollFare</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This struct presents all the fare data for a toll.</p>
<p><strong>Note</strong>: If you’re using the <code>OfflineRoutingEngine</code>, be aware that this feature is
currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors.
Additionally, this feature and related APIs may be updated in future releases
without going through the deprecation process. Note that the <code>OfflineRoutingEngine</code>
is only available for the Navigate license. If you’re using the
<code><a href="sdk-for-ios-explore-api-reference-classes-routingengine">RoutingEngine</a></code>, this feature is considered to be stable.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollFareV8currencySSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currency"></a>
<a class="token" href="#/s:7heresdk8TollFareV8currencySSvp">currency</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The currency in which the toll is to be paid in ISO 4217 format, e.g. “USD”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">currency</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollFareV5priceSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/price"></a>
<a class="token" href="#/s:7heresdk8TollFareV5priceSdvp">price</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The amount of the toll be paid.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">price</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollFareV14paymentMethodsSayAA13PaymentMethodOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/paymentMethods"></a>
<a class="token" href="#/s:7heresdk8TollFareV14paymentMethodsSayAA13PaymentMethodOGvp">paymentMethods</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of accepted payment methods like cash and credit card.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">paymentMethods</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-paymentmethod">PaymentMethod</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollFareV8timeRuleAA04TimeE0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timeRule"></a>
<a class="token" href="#/s:7heresdk8TollFareV8timeRuleAA04TimeE0CSgvp">timeRule</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time domain when this fare is valid.
If this field is missing, it means the fare is always valid.
For a detailed description of the Time Domain specification and usage in routing services, please refer to
the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timeRule</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-timerule">TimeRule</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollFareV12transpondersSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/transponders"></a>
<a class="token" href="#/s:7heresdk8TollFareV12transpondersSaySSGvp">transponders</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of available transponders.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">transponders</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollFareV4passAA0bC4PassVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pass"></a>
<a class="token" href="#/s:7heresdk8TollFareV4passAA0bC4PassVSgvp">pass</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies whether this <code>TollFare</code> is a multi-travel pass, and its characteristics.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pass</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-tollfarepass">TollFarePass</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollFareV8currency5price14paymentMethods8timeRule12transponders4passACSS_SdSayAA13PaymentMethodOGAA04TimeI0CSgSaySSGAA0bC4PassVSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(currency:price:paymentMethods:timeRule:transponders:pass:)"></a>
<a class="token" href="#/s:7heresdk8TollFareV8currency5price14paymentMethods8timeRule12transponders4passACSS_SdSayAA13PaymentMethodOGAA04TimeI0CSgSaySSGAA0bC4PassVSgtcfc">init(currency:<wbr/>price:<wbr/>paymentMethods:<wbr/>timeRule:<wbr/>transponders:<wbr/>pass:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">currency</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">price</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">paymentMethods</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-paymentmethod">PaymentMethod</a></span><span class="p">],</span> <span class="nv">timeRule</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-timerule">TimeRule</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">transponders</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">pass</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-tollfarepass">TollFarePass</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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

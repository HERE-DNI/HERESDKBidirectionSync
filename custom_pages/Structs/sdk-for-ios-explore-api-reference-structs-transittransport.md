---
title: "TransitTransport Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-transittransport"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TransitTransport.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/TransitTransport"></a>
<a title="TransitTransport Structure Reference"></a>
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
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TransitTransport Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct TransitTransport : Hashable</code></pre>
</div>
</div>
<p>Holds all the transit transport information.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitTransportV4modeAA0B4ModeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/mode"></a>
<a class="token" href="#/s:7heresdk16TransitTransportV4modeAA0B4ModeOvp">mode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Transit mode of transport in the route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var mode: TransitMode</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitTransportV4nameSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/name"></a>
<a class="token" href="#/s:7heresdk16TransitTransportV4nameSSSgvp">name</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Transit line name.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var name: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitTransportV8headsignSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/headsign"></a>
<a class="token" href="#/s:7heresdk16TransitTransportV8headsignSSSgvp">headsign</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Transit line headsign.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var headsign: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitTransportV8categorySSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/category"></a>
<a class="token" href="#/s:7heresdk16TransitTransportV8categorySSSgvp">category</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Human readable transport category (such as Bus, Gondola, Tram, Train, …)</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var category: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitTransportV5colorSo7UIColorCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/color"></a>
<a class="token" href="#/s:7heresdk16TransitTransportV5colorSo7UIColorCSgvp">color</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Color of the transport polyline and background for the transport name.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var color: UIColor?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitTransportV9textColorSo7UIColorCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textColor"></a>
<a class="token" href="#/s:7heresdk16TransitTransportV9textColorSo7UIColorCSgvp">textColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Color of the transport name.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var textColor: UIColor?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransitTransportV4mode4name8headsign8category5color9textColorAcA0B4ModeO_SSSgA2LSo7UIColorCSgAOtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(mode:name:headsign:category:color:textColor:)"></a>
<a class="token" href="#/s:7heresdk16TransitTransportV4mode4name8headsign8category5color9textColorAcA0B4ModeO_SSSgA2LSo7UIColorCSgAOtcfc">init(mode:<wbr/>name:<wbr/>headsign:<wbr/>category:<wbr/>color:<wbr/>textColor:<wbr/>)</a>
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
<pre><code>public init(mode: TransitMode, name: String? = nil, headsign: String? = nil, category: String? = nil, color: UIColor? = nil, textColor: UIColor? = nil)</code></pre>
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

---
title: "TransportType"
slug: "sdk-for-ios-navigate-api-reference-enums-transporttype"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TransportType"></a>
<a title="TransportType Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-transport">Transport</a>

        TransportType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TransportType</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TransportType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Specifies types of transportation for which access/restriction rules apply.</p>
<p><strong>Note:</strong> This is a beta release of this feature.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportTypeO11automobilesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/automobiles"></a>
<a class="token" href="#/s:7heresdk13TransportTypeO11automobilesyA2CmF">automobiles</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Cars.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">automobiles</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportTypeO5busesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/buses"></a>
<a class="token" href="#/s:7heresdk13TransportTypeO5busesyA2CmF">buses</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Buses.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">buses</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportTypeO5taxisyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/taxis"></a>
<a class="token" href="#/s:7heresdk13TransportTypeO5taxisyA2CmF">taxis</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Taxis.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">taxis</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportTypeO8carpoolsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/carpools"></a>
<a class="token" href="#/s:7heresdk13TransportTypeO8carpoolsyA2CmF">carpools</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Car pools.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">carpools</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportTypeO11pedestriansyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/pedestrians"></a>
<a class="token" href="#/s:7heresdk13TransportTypeO11pedestriansyA2CmF">pedestrians</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Pedestrians.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">pedestrians</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportTypeO6trucksyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/trucks"></a>
<a class="token" href="#/s:7heresdk13TransportTypeO6trucksyA2CmF">trucks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Trucks.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">trucks</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportTypeO14throughTrafficyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/throughTraffic"></a>
<a class="token" href="#/s:7heresdk13TransportTypeO14throughTrafficyA2CmF">throughTraffic</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Through traffic.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">throughTraffic</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportTypeO10deliveriesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/deliveries"></a>
<a class="token" href="#/s:7heresdk13TransportTypeO10deliveriesyA2CmF">deliveries</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Deliveries.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">deliveries</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportTypeO17emergencyVehiclesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/emergencyVehicles"></a>
<a class="token" href="#/s:7heresdk13TransportTypeO17emergencyVehiclesyA2CmF">emergencyVehicles</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Emergency vehicles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">emergencyVehicles</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportTypeO11motorcyclesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/motorcycles"></a>
<a class="token" href="#/s:7heresdk13TransportTypeO11motorcyclesyA2CmF">motorcycles</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Motorcycles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">motorcycles</span></code></pre>
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

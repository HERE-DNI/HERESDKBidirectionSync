---
title: "EVChargingConnectorType"
slug: "sdk-for-ios-navigate-api-reference-structs-evchargingconnectortype"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingConnectorType"></a>
<a title="EVChargingConnectorType Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-ev">EV</a>

        EVChargingConnectorType Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVChargingConnectorType</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingConnectorType</span></code></pre>
</div>
</div>
<p>Represents the standardized type of the installed connector.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV7chademoSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/chademo"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV7chademoSSvpZ">chademo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The connector type is CHAdeMO, DC.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">chademo</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV6chaojiSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/chaoji"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV6chaojiSSvpZ">chaoji</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The ChaoJi connector. The new generation charging connector, harmonized between CHAdeMO and GB/T. DC.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">chaoji</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticASSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticA"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticASSvpZ">domesticA</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “A”, NEMA 1-15, 2 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticA</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticBSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticB"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticBSSvpZ">domesticB</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “B”, NEMA 5-15, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticB</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticCSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticC"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticCSSvpZ">domesticC</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “C”, CEE 7/17, 2 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticC</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticDSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticD"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticDSSvpZ">domesticD</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “D”, 3 pin.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticD</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticESSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticE"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticESSvpZ">domesticE</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “E”, CEE 7/5 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticE</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticFSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticF"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticFSSvpZ">domesticF</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “F”, CEE 7/4, Schuko, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticF</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticGSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticG"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticGSSvpZ">domesticG</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “G”, BS 1363, Commonwealth, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticG</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticHSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticH"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticHSSvpZ">domesticH</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “H”, SI-32, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticH</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticISSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticI"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticISSvpZ">domesticI</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “I”, AS 3112, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticI</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticJSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticJ"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticJSSvpZ">domesticJ</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “J”, SEV 1011, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticJ</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticKSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticK"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticKSSvpZ">domesticK</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “K”, DS 60884-2-D1, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticK</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticLSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticL"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticLSSvpZ">domesticL</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “L”, CEI 23-16-VII, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticL</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticMSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticM"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticMSSvpZ">domesticM</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “M”, BS 546, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticM</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticNSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticN"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticNSSvpZ">domesticN</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “N”, NBR 14136, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticN</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV9domesticOSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/domesticO"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV9domesticOSSvpZ">domesticO</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Standard/Domestic household, type “O”, TIS 166-2549, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">domesticO</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV5gbtAcSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/gbtAc"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV5gbtAcSSvpZ">gbtAc</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Guobiao GB/T 20234.2 AC socket/connector.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">gbtAc</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV5gbtDcSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/gbtDc"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV5gbtDcSSvpZ">gbtDc</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Guobiao GB/T 20234.3 DC connector.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">gbtDc</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV17iec603092Single16SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/iec603092Single16"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV17iec603092Single16SSvpZ">iec603092Single16</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>IEC 60309-2 Industrial connector single phase 16 amperes (usually blue).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">iec603092Single16</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV16iec603092Three16SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/iec603092Three16"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV16iec603092Three16SSvpZ">iec603092Three16</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>IEC 60309-2 Industrial connector three phase 16 amperes (usually red).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">iec603092Three16</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV16iec603092Three32SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/iec603092Three32"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV16iec603092Three32SSvpZ">iec603092Three32</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>IEC 60309-2 Industrial connector three phase 32 amperes (usually red).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">iec603092Three32</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV16iec603092Three64SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/iec603092Three64"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV16iec603092Three64SSvpZ">iec603092Three64</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>IEC 60309-2 Industrial connector three phase 64 amperes (usually red).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">iec603092Three64</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV10iec62196T1SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/iec62196T1"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV10iec62196T1SSvpZ">iec62196T1</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>IEC 62196 Type 1 “SAE J1772”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">iec62196T1</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV15iec62196T1ComboSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/iec62196T1Combo"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV15iec62196T1ComboSSvpZ">iec62196T1Combo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Combo Type 1 based, DC.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">iec62196T1Combo</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV10iec62196T2SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/iec62196T2"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV10iec62196T2SSvpZ">iec62196T2</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>IEC 62196 Type 2 “Mennekes”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">iec62196T2</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV15iec62196T2ComboSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/iec62196T2Combo"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV15iec62196T2ComboSSvpZ">iec62196T2Combo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Combo Type 2 based, DC.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">iec62196T2Combo</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV11iec62196T3aSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/iec62196T3a"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV11iec62196T3aSSvpZ">iec62196T3a</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>IEC 62196 Type 3A.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">iec62196T3a</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV11iec62196T3cSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/iec62196T3c"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV11iec62196T3cSSvpZ">iec62196T3c</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>IEC 62196 Type 3C “Scame”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">iec62196T3c</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV7nema520SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/nema520"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV7nema520SSvpZ">nema520</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>NEMA 5-20, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">nema520</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV7nema630SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/nema630"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV7nema630SSvpZ">nema630</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>NEMA 6-30, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">nema630</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV7nema650SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/nema650"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV7nema650SSvpZ">nema650</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>NEMA 6-50, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">nema650</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV8nema1030SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/nema1030"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV8nema1030SSvpZ">nema1030</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>NEMA 10-30, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">nema1030</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV8nema1050SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/nema1050"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV8nema1050SSvpZ">nema1050</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>NEMA 10-50, 3 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">nema1050</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV8nema1430SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/nema1430"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV8nema1430SSvpZ">nema1430</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>NEMA 14-30, 4 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">nema1430</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV8nema1450SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/nema1450"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV8nema1450SSvpZ">nema1450</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>NEMA 14-50, 4 pins.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">nema1450</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV18pantographBottomUpSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/pantographBottomUp"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV18pantographBottomUpSSvpZ">pantographBottomUp</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>On-board Bottom-up-Pantograph typically for bus charging.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">pantographBottomUp</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV17pantographTopDownSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/pantographTopDown"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV17pantographTopDownSSvpZ">pantographTopDown</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Top-down-Pantograph typically for bus charging.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">pantographTopDown</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV6teslaRSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/teslaR"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV6teslaRSSvpZ">teslaR</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tesla connector “Roadster”-type (round, 4 pin).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">teslaR</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV8saeJ3400SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/saeJ3400"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV8saeJ3400SSvpZ">saeJ3400</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tesla connector “Model-S”-type (oval, 5 pin), standardized as NACS SAE J3400.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">saeJ3400</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23EVChargingConnectorTypeV3mcsSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/mcs"></a>
<a class="token" href="#/s:7heresdk23EVChargingConnectorTypeV3mcsSSvpZ">mcs</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Megawatt Charging System (MCS) connector.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">mcs</span><span class="p">:</span> <span class="kt">String</span></code></pre>
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

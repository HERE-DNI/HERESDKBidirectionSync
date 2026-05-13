---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-structs-tmcdata"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TMCData.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TMCData"></a>
<a title="TMCData Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-trafficradio">TrafficRadio</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TMCData Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TMCData</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TMCData</span></code></pre>
</div>
</div>
<p>Represents the traffic events in RDS-TMC format.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7TMCDataV14numberOfGroupss5UInt8Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/numberOfGroups"></a>
<a class="token" href="#/s:7heresdk7TMCDataV14numberOfGroupss5UInt8Vvp">numberOfGroups</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of groups (1 to 5).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">numberOfGroups</span><span class="p">:</span> <span class="kt">UInt8</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7TMCDataV6extents5UInt8Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/extent"></a>
<a class="token" href="#/s:7heresdk7TMCDataV6extents5UInt8Vvp">extent</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Extent.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">extent</span><span class="p">:</span> <span class="kt">UInt8</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7TMCDataV9directions5UInt8Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/direction"></a>
<a class="token" href="#/s:7heresdk7TMCDataV9directions5UInt8Vvp">direction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Street direction.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">direction</span><span class="p">:</span> <span class="kt">UInt8</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7TMCDataV15diversionAdvices5UInt8Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/diversionAdvice"></a>
<a class="token" href="#/s:7heresdk7TMCDataV15diversionAdvices5UInt8Vvp">diversionAdvice</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Diversion advice.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">diversionAdvice</span><span class="p">:</span> <span class="kt">UInt8</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7TMCDataV19durationPersistences5UInt8Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/durationPersistence"></a>
<a class="token" href="#/s:7heresdk7TMCDataV19durationPersistences5UInt8Vvp">durationPersistence</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Duration persitence.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">durationPersistence</span><span class="p">:</span> <span class="kt">UInt8</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7TMCDataV5events5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/event"></a>
<a class="token" href="#/s:7heresdk7TMCDataV5events5Int32Vvp">event</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic event data.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">event</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7TMCDataV8locations6UInt32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/location"></a>
<a class="token" href="#/s:7heresdk7TMCDataV8locations6UInt32Vvp">location</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic event location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">location</span><span class="p">:</span> <span class="kt">UInt32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7TMCDataV16additionalEventsSays5Int32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/additionalEvents"></a>
<a class="token" href="#/s:7heresdk7TMCDataV16additionalEventsSays5Int32VGvp">additionalEvents</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Additional traffic events.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">additionalEvents</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7TMCDataV19additionalLocationsSays6UInt32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/additionalLocations"></a>
<a class="token" href="#/s:7heresdk7TMCDataV19additionalLocationsSays6UInt32VGvp">additionalLocations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Additional traffic locations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">additionalLocations</span><span class="p">:</span> <span class="p">[</span><span class="kt">UInt32</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7TMCDataV14numberOfGroups6extent9direction15diversionAdvice19durationPersistence5event8location16additionalEvents0N9LocationsACs5UInt8V_A4Ns5Int32Vs6UInt32VSayAPGSayARGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(numberOfGroups:extent:direction:diversionAdvice:durationPersistence:event:location:additionalEvents:additionalLocations:)"></a>
<a class="token" href="#/s:7heresdk7TMCDataV14numberOfGroups6extent9direction15diversionAdvice19durationPersistence5event8location16additionalEvents0N9LocationsACs5UInt8V_A4Ns5Int32Vs6UInt32VSayAPGSayARGtcfc">init(numberOfGroups:<wbr/>extent:<wbr/>direction:<wbr/>diversionAdvice:<wbr/>durationPersistence:<wbr/>event:<wbr/>location:<wbr/>additionalEvents:<wbr/>additionalLocations:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">numberOfGroups</span><span class="p">:</span> <span class="kt">UInt8</span><span class="p">,</span> <span class="nv">extent</span><span class="p">:</span> <span class="kt">UInt8</span><span class="p">,</span> <span class="nv">direction</span><span class="p">:</span> <span class="kt">UInt8</span><span class="p">,</span> <span class="nv">diversionAdvice</span><span class="p">:</span> <span class="kt">UInt8</span><span class="p">,</span> <span class="nv">durationPersistence</span><span class="p">:</span> <span class="kt">UInt8</span><span class="p">,</span> <span class="nv">event</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">location</span><span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="nv">additionalEvents</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">],</span> <span class="nv">additionalLocations</span><span class="p">:</span> <span class="p">[</span><span class="kt">UInt32</span><span class="p">])</span></code></pre>
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

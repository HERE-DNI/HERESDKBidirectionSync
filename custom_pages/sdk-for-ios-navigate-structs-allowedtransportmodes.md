---
title: "AllowedTransportModes"
slug: "sdk-for-ios-navigate-structs-allowedtransportmodes"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/AllowedTransportModes"></a>
<a title="AllowedTransportModes Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-mapdata">MapData</a>

        AllowedTransportModes Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>AllowedTransportModes</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AllowedTransportModes</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Specifies which transport modes are allowed in a particular direction.</p>
<p><strong>Note:</strong> This struct specifies a general restriction to that transport mode,
but additional restriction are possible.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21AllowedTransportModesV07bicycleB0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/bicycleAllowed"></a>
<a class="token" href="#/s:7heresdk21AllowedTransportModesV07bicycleB0Sbvp">bicycleAllowed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code>True</code> if bicycles can access the segment in the given direction</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">bicycleAllowed</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21AllowedTransportModesV03busB0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/busAllowed"></a>
<a class="token" href="#/s:7heresdk21AllowedTransportModesV03busB0Sbvp">busAllowed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code>True</code> if buses can access the segment in the given direction</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">busAllowed</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21AllowedTransportModesV03carB0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/carAllowed"></a>
<a class="token" href="#/s:7heresdk21AllowedTransportModesV03carB0Sbvp">carAllowed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code>True</code> if cars can access the segment in the given direction</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">carAllowed</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21AllowedTransportModesV010pedestrianB0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pedestrianAllowed"></a>
<a class="token" href="#/s:7heresdk21AllowedTransportModesV010pedestrianB0Sbvp">pedestrianAllowed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code>True</code> if pedestrians can access the segment in the given direction</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pedestrianAllowed</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21AllowedTransportModesV07scooterB0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/scooterAllowed"></a>
<a class="token" href="#/s:7heresdk21AllowedTransportModesV07scooterB0Sbvp">scooterAllowed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code>True</code> if scooters can access the segment in the given direction</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">scooterAllowed</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21AllowedTransportModesV04taxiB0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/taxiAllowed"></a>
<a class="token" href="#/s:7heresdk21AllowedTransportModesV04taxiB0Sbvp">taxiAllowed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code>True</code> if taxis can access the segment in the given direction</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">taxiAllowed</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21AllowedTransportModesV05truckB0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckAllowed"></a>
<a class="token" href="#/s:7heresdk21AllowedTransportModesV05truckB0Sbvp">truckAllowed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code>True</code> if trucks can access the segment in the given direction</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckAllowed</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21AllowedTransportModesV07bicycleB003busB003carB0010pedestrianB007scooterB004taxiB005truckB0ACSb_S6btcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(bicycleAllowed:busAllowed:carAllowed:pedestrianAllowed:scooterAllowed:taxiAllowed:truckAllowed:)"></a>
<a class="token" href="#/s:7heresdk21AllowedTransportModesV07bicycleB003busB003carB0010pedestrianB007scooterB004taxiB005truckB0ACSb_S6btcfc">init(bicycleAllowed:<wbr/>busAllowed:<wbr/>carAllowed:<wbr/>pedestrianAllowed:<wbr/>scooterAllowed:<wbr/>taxiAllowed:<wbr/>truckAllowed:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance with default values.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">bicycleAllowed</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">busAllowed</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">carAllowed</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">pedestrianAllowed</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">scooterAllowed</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">taxiAllowed</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">truckAllowed</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
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
} </HTMLBlock>

---
title: "VenueTopology"
slug: "sdk-for-ios-navigate-api-reference-classes-venuetopology"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueTopology"></a>
<a title="VenueTopology Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-venues">Venues</a>

        VenueTopology Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VenueTopology</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueTopology</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueTopology</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueTopology</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents routing topologies inside the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuelevel">VenueLevel</a></code>. The topologies can be paths
used for enabling routing services.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueTopologyC25AccessCharacteristicsLista"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/AccessCharacteristicsList"></a>
<a class="token" href="#/s:7heresdk13VenueTopologyC25AccessCharacteristicsLista">AccessCharacteristicsList</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">AccessCharacteristicsList</span> <span class="o">=</span> <span class="p">[</span><span class="kt">VenueTopology</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuetopology-accesscharacteristics">AccessCharacteristics</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueTopologyC10identifierSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/identifier"></a>
<a class="token" href="#/s:7heresdk13VenueTopologyC10identifierSSvp">identifier</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code>id</code> of the topology.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">identifier</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueTopologyC5levelAA0B5LevelCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/level"></a>
<a class="token" href="#/s:7heresdk13VenueTopologyC5levelAA0B5LevelCvp">level</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The parent level of the topology.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">level</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuelevel">VenueLevel</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueTopologyC13accessibilitySayAC21AccessCharacteristicsCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/accessibility"></a>
<a class="token" href="#/s:7heresdk13VenueTopologyC13accessibilitySayAC21AccessCharacteristicsCGvp">accessibility</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of <code><a href="sdk-for-ios-navigate-api-reference-classes-venuetopology-accesscharacteristics">VenueTopology.AccessCharacteristics</a></code></p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">accessibility</span><span class="p">:</span> <span class="kt">VenueTopology</span><span class="o">.</span><span class="kt"><a href="../Classes/VenueTopology.html#/s:7heresdk13VenueTopologyC25AccessCharacteristicsLista">AccessCharacteristicsList</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueTopologyC21AccessCharacteristicsC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/AccessCharacteristics"></a>
<a class="token" href="#/s:7heresdk13VenueTopologyC21AccessCharacteristicsC">AccessCharacteristics</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the access characreisticas of a topology.
Access characteristics is a combination of <code><a href="sdk-for-ios-navigate-api-reference-enums-venuetransportmode">VenueTransportMode</a></code> which is suppoted on this topology
and the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuetopology-topologydirectionality">VenueTopology.TopologyDirectionality</a></code> towards which it is allowed.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-venuetopology-accesscharacteristics">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">AccessCharacteristics</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuetopology">VenueTopology</a></span><span class="o">.</span><span class="kt">AccessCharacteristics</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuetopology">VenueTopology</a></span><span class="o">.</span><span class="kt">AccessCharacteristics</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueTopologyC0C14DirectionalityO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TopologyDirectionality"></a>
<a class="token" href="#/s:7heresdk13VenueTopologyC0C14DirectionalityO">TopologyDirectionality</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Available directions.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-venuetopology-topologydirectionality">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TopologyDirectionality</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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

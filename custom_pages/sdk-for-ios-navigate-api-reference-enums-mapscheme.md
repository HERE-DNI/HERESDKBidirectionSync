---
title: "MapScheme"
slug: "sdk-for-ios-navigate-api-reference-enums-mapscheme"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MapScheme"></a>
<a title="MapScheme Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

        MapScheme Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapScheme</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MapScheme</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Represents the preconfigured map schemes bundled with the SDK.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO9normalDayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/normalDay"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO9normalDayyA2CmF">normalDay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Normal map for day.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">normalDay</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO11normalNightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/normalNight"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO11normalNightyA2CmF">normalNight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Normal map for night.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">normalNight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO9satelliteyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/satellite"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO9satelliteyA2CmF">satellite</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Satellite imagery.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">satellite</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO9hybridDayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/hybridDay"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO9hybridDayyA2CmF">hybridDay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Day version of hybrid scheme combining satellite data with vector street network, map labels and POI information.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">hybridDay</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO11hybridNightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/hybridNight"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO11hybridNightyA2CmF">hybridNight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Night version of hybrid scheme combining satellite data with vector street network, map labels and POI information.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">hybridNight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO7liteDayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/liteDay"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO7liteDayyA2CmF">liteDay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The day version of lite scheme is a simplified version of the <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9normalDayyA2CmF">MapScheme.normalDay</a></code>,
featuring fewer map elements and a more limited color palette.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">liteDay</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO9liteNightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/liteNight"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO9liteNightyA2CmF">liteNight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The night version of lite scheme is a simplified version of the <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO11normalNightyA2CmF">MapScheme.normalNight</a></code>,
featuring fewer map elements and a more limited color palette.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">liteNight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO13liteHybridDayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/liteHybridDay"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO13liteHybridDayyA2CmF">liteHybridDay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The day version of lite hybrid scheme is a simplified version of the <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9hybridDayyA2CmF">MapScheme.hybridDay</a></code>,
featuring fewer map elements and a more limited color palette.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">liteHybridDay</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO15liteHybridNightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/liteHybridNight"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO15liteHybridNightyA2CmF">liteHybridNight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The night version of lite hybrid scheme is a simplified version of the <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO11hybridNightyA2CmF">MapScheme.hybridNight</a></code>,
featuring fewer map elements and a more limited color palette.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">liteHybridNight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO12logisticsDayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/logisticsDay"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO12logisticsDayyA2CmF">logisticsDay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The day version of the logistics map scheme catering to the needs of dispatchers,
fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">logisticsDay</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO14logisticsNightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/logisticsNight"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO14logisticsNightyA2CmF">logisticsNight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The night version of the logistics map scheme catering to the needs of dispatchers,
fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">logisticsNight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO18logisticsHybridDayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/logisticsHybridDay"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO18logisticsHybridDayyA2CmF">logisticsHybridDay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The day version of the logistics hybrid map scheme catering to the needs of dispatchers,
fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">logisticsHybridDay</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO20logisticsHybridNightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/logisticsHybridNight"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO20logisticsHybridNightyA2CmF">logisticsHybridNight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The night version of the logistics hybrid map scheme catering to the needs of dispatchers,
fleet managers and delivery drivers, highlighting and featuring map elements relevant to logistics use cases.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">logisticsHybridNight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/roadNetworkDay"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">roadNetworkDay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The day version of a scheme highlighting roads without showing other content such as labels
or buildings. It is designed for usage as an additional zoomed-in mini-maps display to help
drivers to orientate during navigation and to focus on the maneuver arrows which can be
highlighted on top of this map scheme.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">roadNetworkDay</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/roadNetworkNight"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">roadNetworkNight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The night version of a scheme highlighting roads without showing other content such as labels
or buildings. It is designed for usage as an additional zoomed-in mini-maps display to help
drivers to orientate during navigation and to focus on the maneuver arrows which can be
highlighted on top of this map scheme.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">roadNetworkNight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO7topoDayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/topoDay"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO7topoDayyA2CmF">topoDay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The day version of a scheme highlighting geographic features such as elevation, landforms
and natural landscapes to provide a clear representation of the terrain. It is best suited
for applications related to hiking, biking, skiing or any outdoor activities.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">topoDay</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO9topoNightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/topoNight"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO9topoNightyA2CmF">topoNight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The night version of a scheme highlighting geographic features such as elevation, landforms
and natural landscapes to provide a clear representation of the terrain. It is best suited
for applications related to hiking, biking, skiing or any outdoor activities.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">topoNight</span></code></pre>
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

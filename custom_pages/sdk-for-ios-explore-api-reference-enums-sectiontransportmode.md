---
title: "SectionTransportMode"
slug: "sdk-for-ios-explore-api-reference-enums-sectiontransportmode"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/SectionTransportMode"></a>
<a title="SectionTransportMode Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>

        SectionTransportMode Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SectionTransportMode</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">SectionTransportMode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Specifies the <code><a href="sdk-for-ios-explore-api-reference-classes-section">Section</a></code> mode of transport. A <code><a href="sdk-for-ios-explore-api-reference-classes-section">Section</a></code> may have a different
transport mode than the one specified for route calculation. For example, a car route may have a
section having ferry transport mode.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20SectionTransportModeO3caryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/car"></a>
<a class="token" href="#/s:7heresdk20SectionTransportModeO3caryA2CmF">car</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Car mode of transport.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">car</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20SectionTransportModeO5truckyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/truck"></a>
<a class="token" href="#/s:7heresdk20SectionTransportModeO5truckyA2CmF">truck</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Truck mode of transport.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">truck</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20SectionTransportModeO10pedestrianyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/pedestrian"></a>
<a class="token" href="#/s:7heresdk20SectionTransportModeO10pedestrianyA2CmF">pedestrian</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Pedestrian mode of transport.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">pedestrian</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20SectionTransportModeO5ferryyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/ferry"></a>
<a class="token" href="#/s:7heresdk20SectionTransportModeO5ferryyA2CmF">ferry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Ferry mode of transport.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">ferry</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20SectionTransportModeO15carShuttleTrainyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/carShuttleTrain"></a>
<a class="token" href="#/s:7heresdk20SectionTransportModeO15carShuttleTrainyA2CmF">carShuttleTrain</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Mode of transport representing a shuttle train for cars.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">carShuttleTrain</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20SectionTransportModeO7scooteryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/scooter"></a>
<a class="token" href="#/s:7heresdk20SectionTransportModeO7scooteryA2CmF">scooter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Scooter mode of transport.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">scooter</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20SectionTransportModeO7bicycleyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/bicycle"></a>
<a class="token" href="#/s:7heresdk20SectionTransportModeO7bicycleyA2CmF">bicycle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Bicycle mode of transport.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">bicycle</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20SectionTransportModeO13publicTransityA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/publicTransit"></a>
<a class="token" href="#/s:7heresdk20SectionTransportModeO13publicTransityA2CmF">publicTransit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A section with this mode is part of a public transit route. The actual transport mode can be
obtained from <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14transitDetailsAA07TransitbD0VSgvp">Section.transitDetails</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">publicTransit</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20SectionTransportModeO4taxiyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/taxi"></a>
<a class="token" href="#/s:7heresdk20SectionTransportModeO4taxiyA2CmF">taxi</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Taxi mode of transport.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">taxi</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20SectionTransportModeO3busyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/bus"></a>
<a class="token" href="#/s:7heresdk20SectionTransportModeO3busyA2CmF">bus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Bus mode of transport.
Denotes those vehicles operated by public transport provider.
This transport mode has the access to the bus-only lane/road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">bus</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20SectionTransportModeO10privateBusyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/privateBus"></a>
<a class="token" href="#/s:7heresdk20SectionTransportModeO10privateBusyA2CmF">privateBus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Private bus mode of transport.
Denotes those vehicles operated by private transport company.
This transport mode does not have the access to the bus-only lane/road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">privateBus</span></code></pre>
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

---
title: "TransportMode Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-transportmode"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TransportMode.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/TransportMode"></a>
<a title="TransportMode Enumeration Reference"></a>
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
<a href="../Transport.html">Transport</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TransportMode Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum TransportMode : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Specifies the mode of transport used for route calculalation.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportModeO3caryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/car"></a>
<a class="token" href="#/s:7heresdk13TransportModeO3caryA2CmF">car</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The calculated route is optimized for cars.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case car</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportModeO5truckyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/truck"></a>
<a class="token" href="#/s:7heresdk13TransportModeO5truckyA2CmF">truck</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The calculated route is optimized for trucks. This mode considers truck restrictions
and uses truck specific speed assumptions when calculating the route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case truck</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportModeO10pedestrianyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/pedestrian"></a>
<a class="token" href="#/s:7heresdk13TransportModeO10pedestrianyA2CmF">pedestrian</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The calculated route is optimized for pedestrians. As one effect, maneuvers will be
optimized for walking, i.e. segments will consider actions relevant for pedestrians
and maneuver instructions will contain texts suitable for a walking person. This mode
disregards any traffic information.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case pedestrian</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportModeO7scooteryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/scooter"></a>
<a class="token" href="#/s:7heresdk13TransportModeO7scooteryA2CmF">scooter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The calculated route is optimized for scooters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case scooter</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportModeO7bicycleyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/bicycle"></a>
<a class="token" href="#/s:7heresdk13TransportModeO7bicycleyA2CmF">bicycle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route calculation for bicycles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case bicycle</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportModeO13publicTransityA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/publicTransit"></a>
<a class="token" href="#/s:7heresdk13TransportModeO13publicTransityA2CmF">publicTransit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The calculated route is optimized for public transit. Note that this transport mode is available
only for some versions of the HERE SDK. Check <code><a href="../Classes/SDKBuildInformation.html">SDKBuildInformation</a></code> and consult your HERE
representative if necessary.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case publicTransit</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportModeO4taxiyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/taxi"></a>
<a class="token" href="#/s:7heresdk13TransportModeO4taxiyA2CmF">taxi</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The taxi transport mode takes into account tax restricted streets as well as streets reserved for
exclusive taxi access. Note that roads that are restricted or reserved for taxis are avoided, unless
a waypoint is set on such a road - as this may indicate to pick-up or to drop-off a passenger.</p>
<p><strong>Note:</strong> This is a beta release of this transport mode, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases or even become unsupported, without a
deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case taxi</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportModeO3busyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/bus"></a>
<a class="token" href="#/s:7heresdk13TransportModeO3busyA2CmF">bus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route calculation for buses.
Denotes those vehicles operated by public transport provider.
This transport mode has the access to the bus-only lane/road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case bus</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportModeO10privateBusyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/privateBus"></a>
<a class="token" href="#/s:7heresdk13TransportModeO10privateBusyA2CmF">privateBus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Route calculation for private buses.
Denotes those vehicles operated by private transport company.
This transport mode does not have the access to the bus-only lane/road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case privateBus</code></pre>
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

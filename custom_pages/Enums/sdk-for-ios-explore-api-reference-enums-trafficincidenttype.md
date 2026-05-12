---
title: "TrafficIncidentType Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-trafficincidenttype"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TrafficIncidentType.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/TrafficIncidentType"></a>
<a title="TrafficIncidentType Enumeration Reference"></a>
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
<a href="../Traffic.html">Traffic</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TrafficIncidentType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum TrafficIncidentType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Category of a traffic incident.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentTypeO8accidentyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/accident"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentTypeO8accidentyA2CmF">accident</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic accident.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case accident</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentTypeO10congestionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/congestion"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentTypeO10congestionyA2CmF">congestion</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic congestion.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case congestion</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentTypeO12constructionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/construction"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentTypeO12constructionyA2CmF">construction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Construction work.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case construction</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentTypeO15disabledVehicleyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/disabledVehicle"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentTypeO15disabledVehicleyA2CmF">disabledVehicle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Overturned or broken down vehicle(s) on the road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case disabledVehicle</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentTypeO11massTransityA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/massTransit"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentTypeO11massTransityA2CmF">massTransit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Incident involving mass transit such as rail or subway.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case massTransit</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentTypeO12plannedEventyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/plannedEvent"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentTypeO12plannedEventyA2CmF">plannedEvent</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Incident involving activities such as sport events or festivals.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case plannedEvent</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentTypeO10roadHazardyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/roadHazard"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentTypeO10roadHazardyA2CmF">roadHazard</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Dangerous obstruction on the road such as downed tree or traffic light out.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case roadHazard</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentTypeO7weatheryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/weather"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentTypeO7weatheryA2CmF">weather</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adverse weather conditions.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case weather</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentTypeO11roadClosureyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/roadClosure"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentTypeO11roadClosureyA2CmF">roadClosure</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Road closure.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case roadClosure</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentTypeO15laneRestrictionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/laneRestriction"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentTypeO15laneRestrictionyA2CmF">laneRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Lane restriction.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case laneRestriction</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentTypeO5otheryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/other"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentTypeO5otheryA2CmF">other</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The incident is known but it does’t fit into any of the other categories.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case other</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentTypeO7unknownyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unknown"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentTypeO7unknownyA2CmF">unknown</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The incident type is not provided by the traffic incidents supplier or not recognized by HERE SDK.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case unknown</code></pre>
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

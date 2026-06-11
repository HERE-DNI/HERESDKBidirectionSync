---
title: "TransitSectionDetails"
slug: "sdk-for-ios-navigate-api-reference-structs-transitsectiondetails"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TransitSectionDetails"></a>
<a title="TransitSectionDetails Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

        TransitSectionDetails Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TransitSectionDetails</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TransitSectionDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Gives the details of a transit section.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TransitSectionDetailsV9transportAA0B9TransportVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/transport"></a>
<a class="token" href="#/s:7heresdk21TransitSectionDetailsV9transportAA0B9TransportVSgvp">transport</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Transit transport information.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">transport</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transittransport">TransitTransport</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TransitSectionDetailsV17intermediateStopsSayAA0B4StopVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/intermediateStops"></a>
<a class="token" href="#/s:7heresdk21TransitSectionDetailsV17intermediateStopsSayAA0B4StopVGvp">intermediateStops</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All the intermediate stops between departure and destination of this section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">intermediateStops</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transitstop">TransitStop</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TransitSectionDetailsV6agencyAA6AgencyVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/agency"></a>
<a class="token" href="#/s:7heresdk21TransitSectionDetailsV6agencyAA6AgencyVvp">agency</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains information about a particular agency.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">agency</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-agency">Agency</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TransitSectionDetailsV12attributionsSayAA11AttributionVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/attributions"></a>
<a class="token" href="#/s:7heresdk21TransitSectionDetailsV12attributionsSayAA11AttributionVGvp">attributions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of required attributions to display.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">attributions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-attribution">Attribution</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TransitSectionDetailsV5faresSayAA4FareVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/fares"></a>
<a class="token" href="#/s:7heresdk21TransitSectionDetailsV5faresSayAA4FareVGvp">fares</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of tickets to pay for this section of the route.</p>
<p><strong>Note:</strong> Currently, fare information is not supported and the list will be always empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">fares</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-fare">Fare</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TransitSectionDetailsV9incidentsSayAA0B8IncidentVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/incidents"></a>
<a class="token" href="#/s:7heresdk21TransitSectionDetailsV9incidentsSayAA0B8IncidentVGvp">incidents</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A list of all incidents that apply to the section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">incidents</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transitincident">TransitIncident</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TransitSectionDetailsV9transport17intermediateStops6agency12attributions5fares9incidentsAcA0B9TransportVSg_SayAA0B4StopVGAA6AgencyVSayAA11AttributionVGSayAA4FareVGSayAA0B8IncidentVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(transport:intermediateStops:agency:attributions:fares:incidents:)"></a>
<a class="token" href="#/s:7heresdk21TransitSectionDetailsV9transport17intermediateStops6agency12attributions5fares9incidentsAcA0B9TransportVSg_SayAA0B4StopVGAA6AgencyVSayAA11AttributionVGSayAA4FareVGSayAA0B8IncidentVGtcfc">init(transport:<wbr/>intermediateStops:<wbr/>agency:<wbr/>attributions:<wbr/>fares:<wbr/>incidents:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>transport: Transit transport information.</li>
<li>intermediateStops: All the intermediate stops between departure and destination of this section.</li>
<li>agency: Contains information about a particular agency.</li>
<li>attributions: List of required attributions to display.</li>
<li>fares: List of tickets to pay for this section of the route.</li>
</ul>
<p><strong>Note:</strong> Currently, fare information is not supported and the list will be always empty.</p>
<ul>
<li>incidents: A list of all incidents that apply to the section.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">transport</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transittransport">TransitTransport</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">intermediateStops</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transitstop">TransitStop</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">agency</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-agency">Agency</a></span><span class="p">,</span> <span class="nv">attributions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-attribution">Attribution</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">fares</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-fare">Fare</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">incidents</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transitincident">TransitIncident</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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

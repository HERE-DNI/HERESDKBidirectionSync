---
title: "TrafficIncidentsQueryOptions"
slug: "sdk-for-ios-navigate-structs-trafficincidentsqueryoptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficIncidentsQueryOptions"></a>
<a title="TrafficIncidentsQueryOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-traffic">Traffic</a>

        TrafficIncidentsQueryOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficIncidentsQueryOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficIncidentsQueryOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The options to specify how incidents should be queried.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28TrafficIncidentsQueryOptionsV10typeFilterSayAA0B12IncidentTypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/typeFilter"></a>
<a class="token" href="#/s:7heresdk28TrafficIncidentsQueryOptionsV10typeFilterSayAA0B12IncidentTypeOGvp">typeFilter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of incident types to be queried. If the list is empty, all types will be queried.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">typeFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-trafficincidenttype">TrafficIncidentType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28TrafficIncidentsQueryOptionsV12impactFilterSayAA0B14IncidentImpactOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/impactFilter"></a>
<a class="token" href="#/s:7heresdk28TrafficIncidentsQueryOptionsV12impactFilterSayAA0B14IncidentImpactOGvp">impactFilter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of incident impacts to be queried. If the list is empty, all incident impacts will be queried.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">impactFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-trafficincidentimpact">TrafficIncidentImpact</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28TrafficIncidentsQueryOptionsV17earliestStartTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/earliestStartTime"></a>
<a class="token" href="#/s:7heresdk28TrafficIncidentsQueryOptionsV17earliestStartTime10Foundation4DateVSgvp">earliestStartTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The earliest start time of incidents to be queried.
If the value is null filtering by the earliest start time is not applied.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">earliestStartTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28TrafficIncidentsQueryOptionsV13latestEndTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/latestEndTime"></a>
<a class="token" href="#/s:7heresdk28TrafficIncidentsQueryOptionsV13latestEndTime10Foundation4DateVSgvp">latestEndTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The latest end time of incidents to be queried.
If the value is null filtering by the latest end time is not applied.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">latestEndTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28TrafficIncidentsQueryOptionsV12languageCodeAA08LanguageG0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/languageCode"></a>
<a class="token" href="#/s:7heresdk28TrafficIncidentsQueryOptionsV12languageCodeAA08LanguageG0OSgvp">languageCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The language code of the query.
It’s the expected language of fields <code>description</code> and <code><a href="../Classes/TrafficIncident.html#/s:7heresdk15TrafficIncidentC7summaryAA13LocalizedTextVvp">TrafficIncident.summary</a></code> in the relevant response.
However, the language code doesn’t impact on <code><a href="../Structs/TrafficLocation.html#/s:7heresdk15TrafficLocationV11descriptionSSvp">TrafficLocation.description</a></code>.
If the language code is null or not supported then response fields are expected in the original language of the country that the incident belongs to.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">languageCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-languagecode">LanguageCode</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28TrafficIncidentsQueryOptionsV10typeFilter06impactG017earliestStartTime09latestEndK012languageCodeACSayAA0B12IncidentTypeOG_SayAA0bP6ImpactOG10Foundation4DateVSgArA08LanguageO0OSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(typeFilter:impactFilter:earliestStartTime:latestEndTime:languageCode:)"></a>
<a class="token" href="#/s:7heresdk28TrafficIncidentsQueryOptionsV10typeFilter06impactG017earliestStartTime09latestEndK012languageCodeACSayAA0B12IncidentTypeOG_SayAA0bP6ImpactOG10Foundation4DateVSgArA08LanguageO0OSgtcfc">init(typeFilter:<wbr/>impactFilter:<wbr/>earliestStartTime:<wbr/>latestEndTime:<wbr/>languageCode:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">typeFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-trafficincidenttype">TrafficIncidentType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">impactFilter</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-trafficincidentimpact">TrafficIncidentImpact</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">earliestStartTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">latestEndTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">languageCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-languagecode">LanguageCode</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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

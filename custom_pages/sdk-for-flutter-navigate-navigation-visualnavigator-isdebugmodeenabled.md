---
title: "isDebugModeEnabled property"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-isdebugmodeenabled"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isDebugModeEnabled.html -->


<div>
<h1>isDebugModeEnabled property</h1></div>
<section id="getter">

bool
isDebugModeEnabled


<p>When enabled, it shows useful information for debugging purposes.</p>
<ul>
<li>A semi-transparent location marker indicating the map-matched location.</li>
<li>A gray, semi-transparent location marker indicating the raw (or original) input location.</li>
<li>A red polyline indicating the most probable path.</li>
<li>A SVG overlay, on the middle-left of the screen, showing the following:
<ul>
<li>IN - Input location: coordinates [bearing] [speed] [accuracy]</li>
<li>RM - Route-matched location: coordinates bearing (distance-to-raw-location)</li>
<li>MM - Map-Matched location: coordinates bearing (distance-to-raw-location)</li>
<li>RM-MM - distance-between-route-and-map-matched-locations</li>
<li>RP - Route progress: remaining-duration remaining-distance</li>
<li>SP - Section progress: section-index/sections-count remaining-duration remaining-distance</li>
<li>MP - Maneuver progress: maneuver-index remaining-duration remaining-distance</li>
<li>CPU - CPU usage: cpu-usage current-date-time</li>
<li>MS - Milestone status: section-index MISSED|REACHED when</li>
<li>RD - Route deviation: last-traveled-section-index last-traveled-section-distance when</li>
<li>FPS - Frames per second: frames-per-second</li>
</ul>
</li>
</ul>
<p>Fields between brackets ([]'s) are omitted if not available.</p>
<p>Example:</p>
<pre class="language-dart">IN: 53.96880,14.77903 167° 8m/s
RM: 53.96880,14.77903 167° (0.0m)
MM: 53.96879,14.77903 167° (0.5m)
RM-MM: 0.5m
RP: 49h0m3s 4302km
SP: 0/16 1h2m20s 58km
MP: 1 5s 25m
CPU: 7% 2024-01-01 13:21:59
MS: 1 REACHED 12:34:22
RD: 2 345m 11:13:55
FPS: 30.0
</pre>
<p><strong>Note:</strong> This API should be used for debugging purposes only.
Gets the current debug mode state.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isDebugModeEnabled;</code></pre>

</section>
<section id="setter">

void
isDebugModeEnabled=(bool value)


<p>When enabled, it shows useful information for debugging purposes.</p>
<ul>
<li>A semi-transparent location marker indicating the map-matched location.</li>
<li>A gray, semi-transparent location marker indicating the raw (or original) input location.</li>
<li>A red polyline indicating the most probable path.</li>
<li>A SVG overlay, on the middle-left of the screen, showing the following:
<ul>
<li>IN - Input location: coordinates [bearing] [speed] [accuracy]</li>
<li>RM - Route-matched location: coordinates bearing (distance-to-raw-location)</li>
<li>MM - Map-Matched location: coordinates bearing (distance-to-raw-location)</li>
<li>RM-MM - distance-between-route-and-map-matched-locations</li>
<li>RP - Route progress: remaining-duration remaining-distance</li>
<li>SP - Section progress: section-index/sections-count remaining-duration remaining-distance</li>
<li>MP - Maneuver progress: maneuver-index remaining-duration remaining-distance</li>
<li>CPU - CPU usage: cpu-usage current-date-time</li>
<li>MS - Milestone status: section-index MISSED|REACHED when</li>
<li>RD - Route deviation: last-traveled-section-index last-traveled-section-distance when</li>
<li>FPS - Frames per second: frames-per-second</li>
</ul>
</li>
</ul>
<p>Fields between brackets ([]'s) are omitted if not available.</p>
<p>Example:</p>
<pre class="language-dart">IN: 53.96880,14.77903 167° 8m/s
RM: 53.96880,14.77903 167° (0.0m)
MM: 53.96879,14.77903 167° (0.5m)
RM-MM: 0.5m
RP: 49h0m3s 4302km
SP: 0/16 1h2m20s 58km
MP: 1 5s 25m
CPU: 7% 2024-01-01 13:21:59
MS: 1 REACHED 12:34:22
RD: 2 345m 11:13:55
FPS: 30.0
</pre>
<p><strong>Note:</strong> This API should be used for debugging purposes only.
Sets whether to enable debug mode or not.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isDebugModeEnabled(bool value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>

---
title: "VisualNavigatorColors"
slug: "sdk-for-ios-navigate-api-reference-classes-visualnavigatorcolors"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/VisualNavigatorColors"></a>
<a title="VisualNavigatorColors Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        VisualNavigatorColors Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VisualNavigatorColors</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VisualNavigatorColors</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VisualNavigatorColors</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VisualNavigatorColors</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class contains colors used by <code><a href="sdk-for-ios-navigate-api-reference-classes-visualnavigator">VisualNavigator</a></code> to render
the route and the maneuver arrow visualization.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21VisualNavigatorColorsC18maneuverArrowColorSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverArrowColor"></a>
<a class="token" href="#/s:7heresdk21VisualNavigatorColorsC18maneuverArrowColorSo7UIColorCvp">maneuverArrowColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maneuver arrow color.
The object containing color used to draw maneuver arrows on the route to highlight lane directions at the end of a street.
The alpha channel is ignored. The color is interpreted as fully opaque.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maneuverArrowColor</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21VisualNavigatorColorsC014trafficOnRouteD0AA07TrafficfgD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficOnRouteColors"></a>
<a class="token" href="#/s:7heresdk21VisualNavigatorColorsC014trafficOnRouteD0AA07TrafficfgD0Vvp">trafficOnRouteColors</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Colors used to visualize traffic conditions on the route ahead of the current location, for segments with a jam factor of 4.0 or higher.
For route segments with a jam factor below 4.0 and those behind the current location, <code><a href="sdk-for-ios-navigate-api-reference-structs-routeprogresscolors">RouteProgressColors</a></code> are used instead.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficOnRouteColors</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-trafficonroutecolors">TrafficOnRouteColors</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21VisualNavigatorColorsC016setRouteProgressD020sectionTransportMode05routegD0yAA07SectioniJ0O_AA0fgD0VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setRouteProgressColors(sectionTransportMode:routeProgressColors:)"></a>
<a class="token" href="#/s:7heresdk21VisualNavigatorColorsC016setRouteProgressD020sectionTransportMode05routegD0yAA07SectioniJ0O_AA0fgD0VtF">setRouteProgressColors(sectionTransportMode:<wbr/>routeProgressColors:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets route color for visualization.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setRouteProgressColors</span><span class="p">(</span><span class="nv">sectionTransportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-sectiontransportmode">SectionTransportMode</a></span><span class="p">,</span> <span class="nv">routeProgressColors</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-routeprogresscolors">RouteProgressColors</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sectionTransportMode</em>
</code>
</td>
<td>
<div>
<p>The section transport mode.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routeProgressColors</em>
</code>
</td>
<td>
<div>
<p>The route progress colors.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21VisualNavigatorColorsC016getRouteProgressD020sectionTransportModeAA0fgD0VAA07SectioniJ0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getRouteProgressColors(sectionTransportMode:)"></a>
<a class="token" href="#/s:7heresdk21VisualNavigatorColorsC016getRouteProgressD020sectionTransportModeAA0fgD0VAA07SectioniJ0O_tF">getRouteProgressColors(sectionTransportMode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets route color for visualization.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getRouteProgressColors</span><span class="p">(</span><span class="nv">sectionTransportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-sectiontransportmode">SectionTransportMode</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-routeprogresscolors">RouteProgressColors</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sectionTransportMode</em>
</code>
</td>
<td>
<div>
<p>The section transport mode.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The route color for visualization.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21VisualNavigatorColorsC03dayD0ACyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/dayColors()"></a>
<a class="token" href="#/s:7heresdk21VisualNavigatorColorsC03dayD0ACyFZ">dayColors()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Retrieves HERE day color presets for route and maneuver arrow visualization.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">dayColors</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">VisualNavigatorColors</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>HERE day color presets for route and maneuver arrow visualization.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21VisualNavigatorColorsC05nightD0ACyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/nightColors()"></a>
<a class="token" href="#/s:7heresdk21VisualNavigatorColorsC05nightD0ACyFZ">nightColors()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Retrieves HERE night color presets for route and maneuver arrow visualization.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">nightColors</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">VisualNavigatorColors</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>HERE night color presets for route and maneuver arrow visualization.</p>
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

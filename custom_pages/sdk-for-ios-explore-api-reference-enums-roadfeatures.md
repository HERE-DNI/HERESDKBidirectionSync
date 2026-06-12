---
title: "RoadFeatures"
slug: "sdk-for-ios-explore-api-reference-enums-roadfeatures"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RoadFeatures"></a>
<a title="RoadFeatures Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>

        RoadFeatures Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RoadFeatures</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RoadFeatures</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Road features or states.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadFeaturesO15seasonalClosureyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/seasonalClosure"></a>
<a class="token" href="#/s:7heresdk12RoadFeaturesO15seasonalClosureyA2CmF">seasonalClosure</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route is subject to seasonal closure.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">seasonalClosure</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadFeaturesO04tollB0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tollRoad"></a>
<a class="token" href="#/s:7heresdk12RoadFeaturesO04tollB0yA2CmF">tollRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Access to this part of the route is restricted with a fee or toll.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">tollRoad</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadFeaturesO23controlledAccessHighwayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/controlledAccessHighway"></a>
<a class="token" href="#/s:7heresdk12RoadFeaturesO23controlledAccessHighwayyA2CmF">controlledAccessHighway</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route is a controlled-access highway, i.e. high-speed
and highly controlled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">controlledAccessHighway</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadFeaturesO5ferryyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/ferry"></a>
<a class="token" href="#/s:7heresdk12RoadFeaturesO5ferryyA2CmF">ferry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route is for transit with a ferry.</p>
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
<a name="/s:7heresdk12RoadFeaturesO15carShuttleTrainyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/carShuttleTrain"></a>
<a class="token" href="#/s:7heresdk12RoadFeaturesO15carShuttleTrainyA2CmF">carShuttleTrain</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route is for transit with a car shuttle train.</p>
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
<a name="/s:7heresdk12RoadFeaturesO6tunnelyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tunnel"></a>
<a class="token" href="#/s:7heresdk12RoadFeaturesO6tunnelyA2CmF">tunnel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route is a tunnel.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">tunnel</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadFeaturesO04dirtB0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/dirtRoad"></a>
<a class="token" href="#/s:7heresdk12RoadFeaturesO04dirtB0yA2CmF">dirtRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route has an un-paved surface.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">dirtRoad</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadFeaturesO6uTurnsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/uTurns"></a>
<a class="token" href="#/s:7heresdk12RoadFeaturesO6uTurnsyA2CmF">uTurns</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This part of the route has a u-turns. Note that this feature is valid
only for cars, trucks, taxis and buses.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">uTurns</span></code></pre>
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

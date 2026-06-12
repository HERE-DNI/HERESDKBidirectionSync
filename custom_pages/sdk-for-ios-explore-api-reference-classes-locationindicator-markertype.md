---
title: "MarkerType"
slug: "sdk-for-ios-explore-api-reference-classes-locationindicator-markertype"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MarkerType"></a>
<a title="MarkerType Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

<a href="sdk-for-ios-explore-api-reference-classes-locationindicator">LocationIndicator</a>

        MarkerType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MarkerType</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MarkerType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Enum to identify different types of markers of the location indicator.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC10MarkerTypeO10pedestrianyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/pedestrian"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC10MarkerTypeO10pedestrianyA2EmF">pedestrian</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Pedestrian navigation represented by a green dot by default.</p>
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
<a name="/s:7heresdk17LocationIndicatorC10MarkerTypeO18pedestrianInactiveyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/pedestrianInactive"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC10MarkerTypeO18pedestrianInactiveyA2EmF">pedestrianInactive</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Pedestrian navigation in inactive state, represented by a gray dot by default.
It is used when the indicator was set to inactive using <code><a href="../../Classes/LocationIndicator.html#/s:7heresdk17LocationIndicatorC8isActiveSbvp">LocationIndicator.isActive</a></code>
in pedestrian mode.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">pedestrianInactive</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC10MarkerTypeO10navigationyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/navigation"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC10MarkerTypeO10navigationyA2EmF">navigation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle navigation represented by a green triangular arrow by default.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">navigation</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC10MarkerTypeO18navigationInactiveyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/navigationInactive"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC10MarkerTypeO18navigationInactiveyA2EmF">navigationInactive</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle navigation in inactive state, represented by a gray triangular arrow by default.
It is used when the indicator was set to inactive using <code><a href="../../Classes/LocationIndicator.html#/s:7heresdk17LocationIndicatorC8isActiveSbvp">LocationIndicator.isActive</a></code>
in navigation mode.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">navigationInactive</span></code></pre>
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

---
title: "sdk-for-ios-navigate-api-reference-enums-electronichorizonerrorcode"
slug: "sdk-for-ios-navigate-api-reference-enums-electronichorizonerrorcode"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ElectronicHorizonErrorCode"></a>
<a title="ElectronicHorizonErrorCode Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-electronichorizon">ElectronicHorizon</a>
<img alt="" id="carat" src="/carat.png"/>
        ElectronicHorizonErrorCode Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectronicHorizonErrorCode</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ElectronicHorizonErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Represents error codes that describe the result of the <code><a href="../Classes/ElectronicHorizonEngine.html#/s:7heresdk23ElectronicHorizonEngineC6update18mapMatchedLocationyAA03MapgH0V_tF">ElectronicHorizonEngine.update(...)</a></code> method.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<p>Offline availability: This property is available online and offline.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26ElectronicHorizonErrorCodeO18engineNotAvailableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/engineNotAvailable"></a>
<a class="token" href="#/s:7heresdk26ElectronicHorizonErrorCodeO18engineNotAvailableyA2CmF">engineNotAvailable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Electronic horizon engine state is not available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">engineNotAvailable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26ElectronicHorizonErrorCodeO16positionNotFoundyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/positionNotFound"></a>
<a class="token" href="#/s:7heresdk26ElectronicHorizonErrorCodeO16positionNotFoundyA2CmF">positionNotFound</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Current position cannot be resolved in the current electronic horizon tree.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">positionNotFound</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26ElectronicHorizonErrorCodeO15positionOffRoadyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/positionOffRoad"></a>
<a class="token" href="#/s:7heresdk26ElectronicHorizonErrorCodeO15positionOffRoadyA2CmF">positionOffRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Current position cannot be matched to a road segment.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">positionOffRoad</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26ElectronicHorizonErrorCodeO20pathTreeInconsistentyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/pathTreeInconsistent"></a>
<a class="token" href="#/s:7heresdk26ElectronicHorizonErrorCodeO20pathTreeInconsistentyA2CmF">pathTreeInconsistent</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Path tree is inconsistent.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">pathTreeInconsistent</span></code></pre>
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

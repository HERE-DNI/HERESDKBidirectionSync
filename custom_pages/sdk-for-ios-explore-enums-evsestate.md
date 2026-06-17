---
title: "EVSEState"
slug: "sdk-for-ios-explore-enums-evsestate"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EVSEState"></a>
<a title="EVSEState Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-index">heresdk</a>

<a href="sdk-for-ios-explore-ev">EV</a>

        EVSEState Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVSEState</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EVSEState</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Indicates the current short-term status of the EVSE at the time given in the modified property.
There are no separate statuses available for individual connectors.
A single EVSE can only be used by a single car, so same statuses apply to other connectors as well.
So, if one connector is in use, the whole EVSE has status charging, and other connectors cannot be used at the same time, hence they should be considered in-use as well.
If an EVSE can allow multiple connectors to be used at the same time, it is basically multiple EVSEs merged into a single physical box or device.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EVSEStateO7unknownyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unknown"></a>
<a class="token" href="#/s:7heresdk9EVSEStateO7unknownyA2CmF">unknown</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>No status information available or the EVSE/connector is offline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">unknown</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EVSEStateO9availableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/available"></a>
<a class="token" href="#/s:7heresdk9EVSEStateO9availableyA2CmF">available</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The EVSE/connector is able to start a new charging session.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">available</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EVSEStateO7blockedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/blocked"></a>
<a class="token" href="#/s:7heresdk9EVSEStateO7blockedyA2CmF">blocked</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The EVSE/connector is not accessible because of a physical barrier, i.e. a car.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">blocked</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EVSEStateO8chargingyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/charging"></a>
<a class="token" href="#/s:7heresdk9EVSEStateO8chargingyA2CmF">charging</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The EVSE/connector is in use.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">charging</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EVSEStateO11inoperativeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/inoperative"></a>
<a class="token" href="#/s:7heresdk9EVSEStateO11inoperativeyA2CmF">inoperative</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The EVSE/connector is temporarily not available for use, but not broken or defect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">inoperative</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EVSEStateO10outOfOrderyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/outOfOrder"></a>
<a class="token" href="#/s:7heresdk9EVSEStateO10outOfOrderyA2CmF">outOfOrder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The EVSE/connector is currently out of order.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">outOfOrder</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EVSEStateO8reservedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/reserved"></a>
<a class="token" href="#/s:7heresdk9EVSEStateO8reservedyA2CmF">reserved</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The EVSE/connector is reserved for a particular EV driver and is unavailable for other drivers.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">reserved</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EVSEStateO11operationalyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/operational"></a>
<a class="token" href="#/s:7heresdk9EVSEStateO11operationalyA2CmF">operational</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The EVSE/connector was operational when checked the last time, but the actual latest status is not available at the moment.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">operational</span></code></pre>
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

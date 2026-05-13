---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-enums-evsecapability"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVSECapability.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EVSECapability"></a>
<a title="EVSECapability Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-ev">EV</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVSECapability Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVSECapability</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EVSECapability</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Represents the administrative functionality that an EVSE is capable of.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVSECapabilityO15chargingProfileyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/chargingProfile"></a>
<a class="token" href="#/s:7heresdk14EVSECapabilityO15chargingProfileyA2CmF">chargingProfile</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The EVSE supports charging profiles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">chargingProfile</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVSECapabilityO19chargingPreferencesyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/chargingPreferences"></a>
<a class="token" href="#/s:7heresdk14EVSECapabilityO19chargingPreferencesyA2CmF">chargingPreferences</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The EVSE supports charging preferences.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">chargingPreferences</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVSECapabilityO15remoteStartStopyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/remoteStartStop"></a>
<a class="token" href="#/s:7heresdk14EVSECapabilityO15remoteStartStopyA2CmF">remoteStartStop</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The EVSE can remotely be started/stopped.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">remoteStartStop</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVSECapabilityO10reservableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/reservable"></a>
<a class="token" href="#/s:7heresdk14EVSECapabilityO10reservableyA2CmF">reservable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The EVSE can be reserved.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">reservable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVSECapabilityO10tokenGroupyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tokenGroup"></a>
<a class="token" href="#/s:7heresdk14EVSECapabilityO10tokenGroupyA2CmF">tokenGroup</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This EVSE supports token groups, two or more tokens work as one, so that a session can be started with one token and stopped with another.
This is handy when a card and key-fob are given to the EV-driver.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">tokenGroup</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVSECapabilityO6unlockyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unlock"></a>
<a class="token" href="#/s:7heresdk14EVSECapabilityO6unlockyA2CmF">unlock</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Connectors have mechanical lock that can be requested by the eMSP to be unlocked.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">unlock</span></code></pre>
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

</div>
`
}</HTMLBlock>

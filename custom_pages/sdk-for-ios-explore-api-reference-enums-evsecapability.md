---
title: "EVSECapability Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-evsecapability"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVSECapability.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/EVSECapability"></a>
<a title="EVSECapability Enumeration Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-ev">EV</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVSECapability Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum EVSECapability : UInt32, CaseIterable, Codable</code></pre>
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
<pre><code>case chargingProfile</code></pre>
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
<pre><code>case chargingPreferences</code></pre>
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
<pre><code>case remoteStartStop</code></pre>
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
<pre><code>case reservable</code></pre>
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
<pre><code>case tokenGroup</code></pre>
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
<pre><code>case unlock</code></pre>
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

---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-enums-locationenginestatus"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- LocationEngineStatus.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LocationEngineStatus"></a>
<a title="LocationEngineStatus Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-positioning">Positioning</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LocationEngineStatus Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LocationEngineStatus</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">LocationEngineStatus</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Indicates the status of the LocationEngine.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO13engineStartedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/engineStarted"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO13engineStartedyA2CmF">engineStarted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>LocationEngine successfully started.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">engineStarted</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO14alreadyStartedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/alreadyStarted"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO14alreadyStartedyA2CmF">alreadyStarted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tried to start LocationEngine that is already started.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">alreadyStarted</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO13engineStoppedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/engineStopped"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO13engineStoppedyA2CmF">engineStopped</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>LocationEngine has been stopped.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">engineStopped</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO11startFailedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/startFailed"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO11startFailedyA2CmF">startFailed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Start failed due to an internal error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">startFailed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO21userConsentNotHandledyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/userConsentNotHandled"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO21userConsentNotHandledyA2CmF">userConsentNotHandled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>User consent has not been handled yet.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">userConsentNotHandled</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO18missingPermissionsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/missingPermissions"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO18missingPermissionsyA2CmF">missingPermissions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Missing one or more user permissions.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">missingPermissions</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO20authenticationFailedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/authenticationFailed"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO20authenticationFailedyA2CmF">authenticationFailed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authentication failed. Check your credentials.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">authenticationFailed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO12notSupportedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/notSupported"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO12notSupportedyA2CmF">notSupported</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Request is not supported.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">notSupported</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO10notAllowedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/notAllowed"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO10notAllowedyA2CmF">notAllowed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Request is not supported in current region.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">notAllowed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO8notReadyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/notReady"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO8notReadyyA2CmF">notReady</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Engine is not ready for the requested action.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">notReady</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO24locationServicesDisabledyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/locationServicesDisabled"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO24locationServicesDisabledyA2CmF">locationServicesDisabled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Location services are disabled in the system settings.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">locationServicesDisabled</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO24privacyNoticeUnconfirmedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/privacyNoticeUnconfirmed"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO24privacyNoticeUnconfirmedyA2CmF">privacyNoticeUnconfirmed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Method confirmHEREPrivacyNoticeInclusion() (or alternatively confirmHEREPrivacyNoticeException())
was not called before starting the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-locationengine">LocationEngine</a></code> or HERE privacy notice exception was not
permitted.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">privacyNoticeUnconfirmed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO2okyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/ok"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO2okyA2CmF">ok</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Requested operation succeeded.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">ok</span></code></pre>
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

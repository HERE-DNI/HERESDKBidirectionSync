---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-enums-safetycameratype"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- SafetyCameraType.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/SafetyCameraType"></a>
<a title="SafetyCameraType Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SafetyCameraType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SafetyCameraType</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">SafetyCameraType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Indicates the type of the safety camera.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SafetyCameraTypeO7busLaneyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/busLane"></a>
<a class="token" href="#/s:7heresdk16SafetyCameraTypeO7busLaneyA2CmF">busLane</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Safety camera for checking drive on bus lane violation</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">busLane</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SafetyCameraTypeO8distanceyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/distance"></a>
<a class="token" href="#/s:7heresdk16SafetyCameraTypeO8distanceyA2CmF">distance</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Safety camera for checking safe distance violation</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">distance</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SafetyCameraTypeO8redLightyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/redLight"></a>
<a class="token" href="#/s:7heresdk16SafetyCameraTypeO8redLightyA2CmF">redLight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Safety camera for checking red light violation</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">redLight</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SafetyCameraTypeO16redLightAndSpeedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/redLightAndSpeed"></a>
<a class="token" href="#/s:7heresdk16SafetyCameraTypeO16redLightAndSpeedyA2CmF">redLightAndSpeed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Safety camera for checking red light violation and overspeed</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">redLightAndSpeed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SafetyCameraTypeO10sectionEndyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sectionEnd"></a>
<a class="token" href="#/s:7heresdk16SafetyCameraTypeO10sectionEndyA2CmF">sectionEnd</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Safety camera for checking section end</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">sectionEnd</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SafetyCameraTypeO12sectionStartyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sectionStart"></a>
<a class="token" href="#/s:7heresdk16SafetyCameraTypeO12sectionStartyA2CmF">sectionStart</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Safety camera for checking section start</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">sectionStart</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SafetyCameraTypeO5speedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/speed"></a>
<a class="token" href="#/s:7heresdk16SafetyCameraTypeO5speedyA2CmF">speed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Safety camera for checking overspeed</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">speed</span></code></pre>
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

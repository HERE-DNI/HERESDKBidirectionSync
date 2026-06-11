---
title: "sdk-for-ios-explore-api-reference-structs-textusageoptions"
slug: "sdk-for-ios-explore-api-reference-structs-textusageoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TextUsageOptions"></a>
<a title="TextUsageOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        TextUsageOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TextUsageOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TextUsageOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Specify whether the text should be used when generating notification.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TextUsageOptionsV10streetNameAA09LocalizedB10PreferenceOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/streetName"></a>
<a class="token" href="#/s:7heresdk16TextUsageOptionsV10streetNameAA09LocalizedB10PreferenceOvp">streetName</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An option whether street name should be used when generating notification.
Defaults to <code><a href="../Enums/LocalizedTextPreference.html#/s:7heresdk23LocalizedTextPreferenceO9useAlwaysyA2CmF">LocalizedTextPreference.useAlways</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">streetName</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-localizedtextpreference">LocalizedTextPreference</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TextUsageOptionsV10roadNumberAA09LocalizedB10PreferenceOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadNumber"></a>
<a class="token" href="#/s:7heresdk16TextUsageOptionsV10roadNumberAA09LocalizedB10PreferenceOvp">roadNumber</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An option whether road number should be used when generating notification.
Defaults to <code><a href="../Enums/LocalizedTextPreference.html#/s:7heresdk23LocalizedTextPreferenceO9useAlwaysyA2CmF">LocalizedTextPreference.useAlways</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roadNumber</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-localizedtextpreference">LocalizedTextPreference</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TextUsageOptionsV17signpostDirectionAA09LocalizedB10PreferenceOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/signpostDirection"></a>
<a class="token" href="#/s:7heresdk16TextUsageOptionsV17signpostDirectionAA09LocalizedB10PreferenceOvp">signpostDirection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An option whether signpost direction should be used when generating notification.
Defaults to <code><a href="../Enums/LocalizedTextPreference.html#/s:7heresdk23LocalizedTextPreferenceO9useAlwaysyA2CmF">LocalizedTextPreference.useAlways</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">signpostDirection</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-localizedtextpreference">LocalizedTextPreference</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TextUsageOptionsV10streetName10roadNumber17signpostDirectionAcA09LocalizedB10PreferenceO_A2Htcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(streetName:roadNumber:signpostDirection:)"></a>
<a class="token" href="#/s:7heresdk16TextUsageOptionsV10streetName10roadNumber17signpostDirectionAcA09LocalizedB10PreferenceO_A2Htcfc">init(streetName:<wbr/>roadNumber:<wbr/>signpostDirection:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">streetName</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-localizedtextpreference">LocalizedTextPreference</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-localizedtextpreference">LocalizedTextPreference</a></span><span class="o">.</span><span class="n">useAlways</span><span class="p">,</span> <span class="nv">roadNumber</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-localizedtextpreference">LocalizedTextPreference</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-localizedtextpreference">LocalizedTextPreference</a></span><span class="o">.</span><span class="n">useAlways</span><span class="p">,</span> <span class="nv">signpostDirection</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-localizedtextpreference">LocalizedTextPreference</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-localizedtextpreference">LocalizedTextPreference</a></span><span class="o">.</span><span class="n">useAlways</span><span class="p">)</span></code></pre>
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

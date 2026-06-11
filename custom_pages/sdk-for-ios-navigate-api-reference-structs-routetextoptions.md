---
title: "sdk-for-ios-navigate-api-reference-structs-routetextoptions"
slug: "sdk-for-ios-navigate-api-reference-structs-routetextoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RouteTextOptions"></a>
<a title="RouteTextOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        RouteTextOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RouteTextOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteTextOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Specify how textual output should be provided.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RouteTextOptionsV8languageAA12LanguageCodeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/language"></a>
<a class="token" href="#/s:7heresdk16RouteTextOptionsV8languageAA12LanguageCodeOvp">language</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The language for all textual information. When the specified language is not supported,
the default language is used, which is English (United States).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">language</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-languagecode">LanguageCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RouteTextOptionsV10unitSystemAA04UnitF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/unitSystem"></a>
<a class="token" href="#/s:7heresdk16RouteTextOptionsV10unitSystemAA04UnitF0Ovp">unitSystem</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the measurement system used in instruction text. When imperial is selected,
units used are based on the language specified in the request. Defaults to metric.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">unitSystem</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-unitsystem">UnitSystem</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RouteTextOptionsV09textUsageD0AA0cfD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textUsageOptions"></a>
<a class="token" href="#/s:7heresdk16RouteTextOptionsV09textUsageD0AA0cfD0Vvp">textUsageOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An option whether street name, road number and sign post direction should be used when generating notification.
Defaults to each attribute as <code><a href="../Enums/LocalizedTextPreference.html#/s:7heresdk23LocalizedTextPreferenceO9useAlwaysyA2CmF">LocalizedTextPreference.useAlways</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">textUsageOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-textusageoptions">TextUsageOptions</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RouteTextOptionsV8language10unitSystem09textUsageD0AcA12LanguageCodeO_AA04UnitG0OAA0ciD0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(language:unitSystem:textUsageOptions:)"></a>
<a class="token" href="#/s:7heresdk16RouteTextOptionsV8language10unitSystem09textUsageD0AcA12LanguageCodeO_AA04UnitG0OAA0ciD0Vtcfc">init(language:<wbr/>unitSystem:<wbr/>textUsageOptions:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">language</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-languagecode">LanguageCode</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-languagecode">LanguageCode</a></span><span class="o">.</span><span class="n">enUs</span><span class="p">,</span> <span class="nv">unitSystem</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-unitsystem">UnitSystem</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-unitsystem">UnitSystem</a></span><span class="o">.</span><span class="n">metric</span><span class="p">,</span> <span class="nv">textUsageOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-textusageoptions">TextUsageOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-textusageoptions">TextUsageOptions</a></span><span class="p">())</span></code></pre>
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

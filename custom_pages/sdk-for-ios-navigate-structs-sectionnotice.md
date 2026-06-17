---
title: "SectionNotice"
slug: "sdk-for-ios-navigate-structs-sectionnotice"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SectionNotice"></a>
<a title="SectionNotice Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-routing">Routing</a>

        SectionNotice Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SectionNotice</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SectionNotice</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Explains an issue encountered in a <code><a href="sdk-for-ios-navigate-classes-section">Section</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13SectionNoticeV4codeAA0bC4CodeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/code"></a>
<a class="token" href="#/s:7heresdk13SectionNoticeV4codeAA0bC4CodeOvp">code</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The notice code.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">code</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-sectionnoticecode">SectionNoticeCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13SectionNoticeV8severityAA0C8SeverityOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/severity"></a>
<a class="token" href="#/s:7heresdk13SectionNoticeV8severityAA0C8SeverityOvp">severity</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The notice severity.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">severity</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-noticeseverity">NoticeSeverity</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13SectionNoticeV20violatedRestrictionsSayAA19ViolatedRestrictionVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/violatedRestrictions"></a>
<a class="token" href="#/s:7heresdk13SectionNoticeV20violatedRestrictionsSayAA19ViolatedRestrictionVGvp">violatedRestrictions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The following property <code>violated_restrictions</code> contains the notice detail information.
Only three types of restrictions can have notice details: time dependent restriction, vehicle restriction and transport mode restriction.
There is no one-to-one match of the <code><a href="../Structs/SectionNotice.html#/s:7heresdk13SectionNoticeV4codeAA0bC4CodeOvp">SectionNotice.code</a></code> and these three restriction types. For example, if <code><a href="../Structs/SectionNotice.html#/s:7heresdk13SectionNoticeV4codeAA0bC4CodeOvp">SectionNotice.code</a></code> is
<code><a href="../Enums/SectionNoticeCode.html#/s:7heresdk17SectionNoticeCodeO26violatedVehicleRestrictionyA2CmF">SectionNoticeCode.violatedVehicleRestriction</a></code>, then it can be either vehicle restriction or transport mode restriction. If <code><a href="../Structs/SectionNotice.html#/s:7heresdk13SectionNoticeV4codeAA0bC4CodeOvp">SectionNotice.code</a></code> is
<code><a href="../Enums/SectionNoticeCode.html#/s:7heresdk17SectionNoticeCodeO15seasonalClosureyA2CmF">SectionNoticeCode.seasonalClosure</a></code>, then it is time dependent restriction.
If the section notice is none of the above-mentioned three types, then this will be an empty list.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">violatedRestrictions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-violatedrestriction">ViolatedRestriction</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13SectionNoticeV4code8severity20violatedRestrictionsAcA0bC4CodeO_AA0C8SeverityOSayAA19ViolatedRestrictionVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(code:severity:violatedRestrictions:)"></a>
<a class="token" href="#/s:7heresdk13SectionNoticeV4code8severity20violatedRestrictionsAcA0bC4CodeO_AA0C8SeverityOSayAA19ViolatedRestrictionVGtcfc">init(code:<wbr/>severity:<wbr/>violatedRestrictions:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">code</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-sectionnoticecode">SectionNoticeCode</a></span><span class="p">,</span> <span class="nv">severity</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-noticeseverity">NoticeSeverity</a></span><span class="p">,</span> <span class="nv">violatedRestrictions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-violatedrestriction">ViolatedRestriction</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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

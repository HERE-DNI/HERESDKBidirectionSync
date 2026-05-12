---
title: "SectionNotice Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-sectionnotice"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- SectionNotice.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/SectionNotice"></a>
<a title="SectionNotice Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SectionNotice Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct SectionNotice : Hashable</code></pre>
</div>
</div>
<p>Explains an issue encountered in a <code><a href="../Classes/Section.html">Section</a></code>.</p>
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
<pre><code>public var code: SectionNoticeCode</code></pre>
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
<pre><code>public var severity: NoticeSeverity</code></pre>
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
<pre><code>public var violatedRestrictions: [ViolatedRestriction]</code></pre>
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
<pre><code>public init(code: SectionNoticeCode, severity: NoticeSeverity, violatedRestrictions: [ViolatedRestriction] = [])</code></pre>
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

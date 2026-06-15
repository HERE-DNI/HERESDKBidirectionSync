---
title: "ViolatedRestriction"
slug: "sdk-for-ios-navigate-api-reference-structs-violatedrestriction"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ViolatedRestriction"></a>
<a title="ViolatedRestriction Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

        ViolatedRestriction Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ViolatedRestriction</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ViolatedRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p><code>ViolatedRestriction</code> contains all the violated restriction details for the planned trip.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV5causeSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cause"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV5causeSSvp">cause</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Cause of the notice. Human readable description of the notice, for example “Route violates vehicle restriction”. It will be EN-US text only.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">cause</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV13timeDependentSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timeDependent"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV13timeDependentSbvp">timeDependent</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates that restriction depends on time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timeDependent</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7detailsAC7DetailsVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/details"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7detailsAC7DetailsVSgvp">details</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The detailed information of restriction depending on the specific violation.
For time dependent restriction or transport mode restriction, this property will be null.
For vehicle restriction, the corresponding member will be set, for example, if the vehicle violates the maximum
allowed gross weight for a specific route, the max_gross_weight_in_kilograms will be set with the maximum allowed
gross weight for this route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">details</span><span class="p">:</span> <span class="kt">ViolatedRestriction</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-violatedrestriction-details">Details</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV5cause13timeDependent7detailsACSS_SbAC7DetailsVSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(cause:timeDependent:details:)"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV5cause13timeDependent7detailsACSS_SbAC7DetailsVSgtcfc">init(cause:<wbr/>timeDependent:<wbr/>details:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">cause</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">timeDependent</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">details</span><span class="p">:</span> <span class="kt">ViolatedRestriction</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-violatedrestriction-details">Details</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Details"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV">Details</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set.
For example, if the vehicle violates the maximum allowed height during the trip, then the member <code>max_height_in_centimeters</code> will
be set with the maximum allowed height value.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-violatedrestriction-details">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Details</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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

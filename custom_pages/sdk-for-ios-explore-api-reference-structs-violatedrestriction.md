---
title: "ViolatedRestriction Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-violatedrestriction"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ViolatedRestriction.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/ViolatedRestriction"></a>
<a title="ViolatedRestriction Structure Reference"></a>
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
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        ViolatedRestriction Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct ViolatedRestriction : Hashable</code></pre>
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
<pre><code>public var cause: String</code></pre>
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
<pre><code>public var timeDependent: Bool</code></pre>
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
<pre><code>public var details: ViolatedRestriction.Details?</code></pre>
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
<pre><code>public init(cause: String, timeDependent: Bool, details: ViolatedRestriction.Details? = nil)</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-structs-violatedrestriction-details">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Details : Hashable</code></pre>
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

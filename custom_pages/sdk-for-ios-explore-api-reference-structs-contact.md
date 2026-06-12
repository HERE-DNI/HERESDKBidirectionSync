---
title: "Contact"
slug: "sdk-for-ios-explore-api-reference-structs-contact"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Contact"></a>
<a title="Contact Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-search">Search</a>

        Contact Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Contact</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Contact</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents contact information.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7ContactV14landlinePhonesSayAA13LandlinePhoneVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/landlinePhones"></a>
<a class="token" href="#/s:7heresdk7ContactV14landlinePhonesSayAA13LandlinePhoneVGvp">landlinePhones</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of landline phone numbers with associated categories.
This data is not available in offline search.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">landlinePhones</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-landlinephone">LandlinePhone</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7ContactV12mobilePhonesSayAA11MobilePhoneVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/mobilePhones"></a>
<a class="token" href="#/s:7heresdk7ContactV12mobilePhonesSayAA11MobilePhoneVGvp">mobilePhones</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of mobile phones numbers with associated categories.
This data is not available in offline search.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">mobilePhones</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-mobilephone">MobilePhone</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7ContactV6emailsSayAA12EmailAddressVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/emails"></a>
<a class="token" href="#/s:7heresdk7ContactV6emailsSayAA12EmailAddressVGvp">emails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of email addresses with associated categories.
This data is not available in offline search.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">emails</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-emailaddress">EmailAddress</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7ContactV8websitesSayAA14WebsiteAddressVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/websites"></a>
<a class="token" href="#/s:7heresdk7ContactV8websitesSayAA14WebsiteAddressVGvp">websites</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of website addresses with associated categories.
This data is not available in offline search.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">websites</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-websiteaddress">WebsiteAddress</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7ContactVACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk7ContactVACycfc">init()</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7ContactV14landlinePhones06mobileD06emails8websitesACSayAA13LandlinePhoneVG_SayAA06MobileI0VGSayAA12EmailAddressVGSayAA07WebsiteL0VGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(landlinePhones:mobilePhones:emails:websites:)"></a>
<a class="token" href="#/s:7heresdk7ContactV14landlinePhones06mobileD06emails8websitesACSayAA13LandlinePhoneVG_SayAA06MobileI0VGSayAA12EmailAddressVGSayAA07WebsiteL0VGtcfc">init(landlinePhones:<wbr/>mobilePhones:<wbr/>emails:<wbr/>websites:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">landlinePhones</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-landlinephone">LandlinePhone</a></span><span class="p">],</span> <span class="nv">mobilePhones</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-mobilephone">MobilePhone</a></span><span class="p">],</span> <span class="nv">emails</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-emailaddress">EmailAddress</a></span><span class="p">],</span> <span class="nv">websites</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-websiteaddress">WebsiteAddress</a></span><span class="p">])</span></code></pre>
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

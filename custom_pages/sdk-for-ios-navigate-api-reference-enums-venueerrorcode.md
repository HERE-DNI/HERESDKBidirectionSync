---
title: "VenueErrorCode"
slug: "sdk-for-ios-navigate-api-reference-enums-venueerrorcode"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/VenueErrorCode"></a>
<a title="VenueErrorCode Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-venues">Venues</a>

        VenueErrorCode Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VenueErrorCode</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">VenueErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
<p>Specifies possible errors that may occur during loading of indoor maps</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO9noNetworkyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noNetwork"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO9noNetworkyA2CmF">noNetwork</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>No network</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noNetwork</span> <span class="o">=</span> <span class="mi">1</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO15noMetaDataFoundyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noMetaDataFound"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO15noMetaDataFoundyA2CmF">noMetaDataFound</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Meta data missing error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noMetaDataFound</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO10hrnMissingyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/hrnMissing"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO10hrnMissingyA2CmF">hrnMissing</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>HRN not provided</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">hrnMissing</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO11hrnMismatchyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/hrnMismatch"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO11hrnMismatchyA2CmF">hrnMismatch</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>HRN missmatch.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">hrnMismatch</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO19noDefaultCollectionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noDefaultCollection"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO19noDefaultCollectionyA2CmF">noDefaultCollection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Default collection missing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noDefaultCollection</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO13mapIdNotFoundyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/mapIdNotFound"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO13mapIdNotFoundyA2CmF">mapIdNotFound</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map ID not found.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">mapIdNotFound</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO16mapDataIncorrectyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/mapDataIncorrect"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO16mapDataIncorrectyA2CmF">mapDataIncorrect</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data incorrect</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">mapDataIncorrect</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO17noMapInCollectionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noMapInCollection"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO17noMapInCollectionyA2CmF">noMapInCollection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>No map available in collection</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noMapInCollection</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO10badRequestyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/badRequest"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO10badRequestyA2CmF">badRequest</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Bad request.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">badRequest</span> <span class="o">=</span> <span class="mi">400</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO12tokenInvalidyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tokenInvalid"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO12tokenInvalidyA2CmF">tokenInvalid</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Invalid authentication token</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">tokenInvalid</span> <span class="o">=</span> <span class="mi">401</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO8notFoundyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/notFound"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO8notFoundyA2CmF">notFound</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Requested resource not found.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">notFound</span> <span class="o">=</span> <span class="mi">404</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO014internalServerC0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/internalServerError"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO014internalServerC0yA2CmF">internalServerError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Internal Server error</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">internalServerError</span> <span class="o">=</span> <span class="mi">500</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO18serviceUnavailableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/serviceUnavailable"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO18serviceUnavailableyA2CmF">serviceUnavailable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Service unavailable</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">serviceUnavailable</span> <span class="o">=</span> <span class="mi">502</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO15payloadTooLargeyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/payloadTooLarge"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO15payloadTooLargeyA2CmF">payloadTooLarge</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Payload too large.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">payloadTooLarge</span> <span class="o">=</span> <span class="mi">513</span></code></pre>
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

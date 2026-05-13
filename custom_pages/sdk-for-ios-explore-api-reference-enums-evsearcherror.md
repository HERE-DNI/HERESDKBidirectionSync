---
title: "EVSearchError Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-evsearcherror"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVSearchError.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/EVSearchError"></a>
<a title="EVSearchError Enumeration Reference"></a>
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
<a href="sdk-for-ios-explore-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVSearchError Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum EVSearchError : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Specifies possible errors that <code><a href="sdk-for-ios-explore-api-reference-..-classes-evsearchengine">EVSearchEngine</a></code> may report.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO8emptyIdsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/emptyIds"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO8emptyIdsyA2CmF">emptyIds</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Empty list of IDs passed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case emptyIds</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO9invalidIdyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidId"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO9invalidIdyA2CmF">invalidId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>At least one empty or invalid ID passed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case invalidId</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO10badRequestyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/badRequest"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO10badRequestyA2CmF">badRequest</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Something wrong or missing in the request.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case badRequest</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO07parsingC0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/parsingError"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO07parsingC0yA2CmF">parsingError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EVCP3 backend returns result with unexpected json schema.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case parsingError</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO08internalC0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/internalError"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO08internalC0yA2CmF">internalError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Generic internal error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case internalError</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO17serverUnreachableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/serverUnreachable"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO17serverUnreachableyA2CmF">serverUnreachable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EVCP3 server is unreachable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case serverUnreachable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO04httpC0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/httpError"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO04httpC0yA2CmF">httpError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A general network request error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case httpError</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO20authenticationFailedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/authenticationFailed"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO20authenticationFailedyA2CmF">authenticationFailed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EVCP3 operation is not authenticated. Check your credentials.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case authenticationFailed</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO18exceededUsageLimityA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/exceededUsageLimit"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO18exceededUsageLimityA2CmF">exceededUsageLimit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Credentials exceeded the allowed requests limit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case exceededUsageLimit</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO8timedOutyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/timedOut"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO8timedOutyA2CmF">timedOut</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The request timed out.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case timedOut</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO7offlineyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/offline"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO7offlineyA2CmF">offline</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The device has no internet connection.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case offline</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO18operationCancelledyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/operationCancelled"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO18operationCancelledyA2CmF">operationCancelled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The request was cancelled (usually by the user).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case operationCancelled</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO25proxyAuthenticationFailedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/proxyAuthenticationFailed"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO25proxyAuthenticationFailedyA2CmF">proxyAuthenticationFailed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Proxy is not authenticated. Check your proxy credentials.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case proxyAuthenticationFailed</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO22proxyServerUnreachableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/proxyServerUnreachable"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO22proxyServerUnreachableyA2CmF">proxyServerUnreachable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Proxy server unreachable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case proxyServerUnreachable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO14noResultsFoundyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noResultsFound"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO14noResultsFoundyA2CmF">noResultsFound</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>No results found.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case noResultsFound</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EVSearchErrorO15operationFailedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/operationFailed"></a>
<a class="token" href="#/s:7heresdk13EVSearchErrorO15operationFailedyA2CmF">operationFailed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Search operation failed due to some reason.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case operationFailed</code></pre>
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

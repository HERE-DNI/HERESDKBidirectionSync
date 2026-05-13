---
title: "Routing / IndoorRoutingError"
slug: "sdk-for-ios-navigate-api-reference-enums-indoorroutingerror"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/IndoorRoutingError"></a>
<a title="IndoorRoutingError Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        IndoorRoutingError Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>IndoorRoutingError</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">IndoorRoutingError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Specifies possible errors that may result from the calculation of a indoor route.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRoutingErrorO02noD0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noError"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO02noD0yA2CmF">noError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Default</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noError</span> <span class="o">=</span> <span class="mi">0</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRoutingErrorO9noNetworkyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noNetwork"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO9noNetworkyA2CmF">noNetwork</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>No network.</p>
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
<a name="/s:7heresdk18IndoorRoutingErrorO12noRouteFoundyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/noRouteFound"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO12noRouteFoundyA2CmF">noRouteFound</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>No route found.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">noRouteFound</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRoutingErrorO19couldNotMatchOriginyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/couldNotMatchOrigin"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO19couldNotMatchOriginyA2CmF">couldNotMatchOrigin</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Could not match origin.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">couldNotMatchOrigin</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRoutingErrorO24couldNotMatchDestinationyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/couldNotMatchDestination"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO24couldNotMatchDestinationyA2CmF">couldNotMatchDestination</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Could not match destination.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">couldNotMatchDestination</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRoutingErrorO11mapNotFoundyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/mapNotFound"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO11mapNotFoundyA2CmF">mapNotFound</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Venue ID not found.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">mapNotFound</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRoutingErrorO07parsingD0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/parsingError"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO07parsingD0yA2CmF">parsingError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Response output not as expected.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">parsingError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRoutingErrorO07unknownD0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unknownError"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO07unknownD0yA2CmF">unknownError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unknown error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">unknownError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRoutingErrorO10badRequestyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/badRequest"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO10badRequestyA2CmF">badRequest</a>
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
<a name="/s:7heresdk18IndoorRoutingErrorO18unauthorizedAccessyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unauthorizedAccess"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO18unauthorizedAccessyA2CmF">unauthorizedAccess</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unauthorized access.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">unauthorizedAccess</span> <span class="o">=</span> <span class="mi">401</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRoutingErrorO9forbiddenyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/forbidden"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO9forbiddenyA2CmF">forbidden</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Forbidden.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">forbidden</span> <span class="o">=</span> <span class="mi">403</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRoutingErrorO8notFoundyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/notFound"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO8notFoundyA2CmF">notFound</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Resource unavailable</p>
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
<a name="/s:7heresdk18IndoorRoutingErrorO15tooManyRequestsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tooManyRequests"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO15tooManyRequestsyA2CmF">tooManyRequests</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Too many requests.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">tooManyRequests</span> <span class="o">=</span> <span class="mi">429</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRoutingErrorO014internalServerD0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/internalServerError"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO014internalServerD0yA2CmF">internalServerError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Internal server error.</p>
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
<a name="/s:7heresdk18IndoorRoutingErrorO10badGatewayyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/badGateway"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO10badGatewayyA2CmF">badGateway</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Bad Gateway.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">badGateway</span> <span class="o">=</span> <span class="mi">502</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18IndoorRoutingErrorO18serviceUnavailableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/serviceUnavailable"></a>
<a class="token" href="#/s:7heresdk18IndoorRoutingErrorO18serviceUnavailableyA2CmF">serviceUnavailable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Service unavailable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">serviceUnavailable</span> <span class="o">=</span> <span class="mi">503</span></code></pre>
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

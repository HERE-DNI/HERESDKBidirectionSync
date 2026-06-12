---
title: "Authentication"
slug: "sdk-for-ios-explore-api-reference-classes-authentication"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/Authentication"></a>
<a title="Authentication Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-core">Core</a>

        Authentication Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Authentication</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Authentication</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Authentication</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Authentication</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use the authentication class to authenticate and retrieve a secure token that
can be used with other HERE services.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14AuthenticationC12authenticate15sdkNativeEngine8callbackyAA09SDKNativeF0C_yAA0B5ErrorOSg_AA0B4DataVSgtctFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/authenticate(sdkNativeEngine:callback:)"></a>
<a class="token" href="#/s:7heresdk14AuthenticationC12authenticate15sdkNativeEngine8callbackyAA09SDKNativeF0C_yAA0B5ErrorOSg_AA0B4DataVSgtctFZ">authenticate(sdkNativeEngine:<wbr/>callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Uses the authentication service that is connected to the given SDK engine to authenticate and
retrieve a secure token. This method operates asynchronously.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">authenticate</span><span class="p">(</span><span class="nv">sdkNativeEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">callback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Core.html#/s:7heresdk31AuthenticationCompletionHandlera">AuthenticationCompletionHandler</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sdkNativeEngine</em>
</code>
</td>
<td>
<div>
<p>The SDK engine instance.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>callback</em>
</code>
</td>
<td>
<div>
<p>Protocol to retrieve an authentication token on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14AuthenticationC12authenticate15sdkNativeEngineAA0B4DataVAA09SDKNativeF0C_tKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/authenticate(sdkNativeEngine:)"></a>
<a class="token" href="#/s:7heresdk14AuthenticationC12authenticate15sdkNativeEngineAA0B4DataVAA09SDKNativeF0C_tKFZ">authenticate(sdkNativeEngine:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Uses the authentication service that is connected to the given SDK engine to authenticate and
retrieve a secure token. This method operates synchronously.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk23AuthenticationExceptiona">AuthenticationException</a></code> Authentication exception that describes the error.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">authenticate</span><span class="p">(</span><span class="nv">sdkNativeEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-authenticationdata">AuthenticationData</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sdkNativeEngine</em>
</code>
</td>
<td>
<div>
<p>The SDK engine instance.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Authentication data.</p>
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

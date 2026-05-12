---
title: "AuthenticationMode Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-authenticationmode"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- AuthenticationMode.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/AuthenticationMode"></a>
<a title="AuthenticationMode Class Reference"></a>
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
<a href="../Core.html">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        AuthenticationMode Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class AuthenticationMode</code></pre>
<pre><code>extension AuthenticationMode: NativeBase</code></pre>
<pre><code>extension AuthenticationMode: Hashable</code></pre>
</div>
</div>
<p>This is a bearer authentication mode which adds or does not add a
header (“Authorization”, “Bearer $Token”) to each online request of the
module the object is added to. The token (if used) can be provided or is
retrieved via key/secret from a dedicated backend.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AuthenticationModeC19AccessTokenProvidera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/AccessTokenProvider"></a>
<a class="token" href="#/s:7heresdk18AuthenticationModeC19AccessTokenProvidera">AccessTokenProvider</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This lambda is used to retrieve access token in synchronous manner.
It returns the access token or null if it is not set.
The lambda is called each time the access token is needed and it is executed
on the main thread of the application.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias AccessTokenProvider = () -&gt; String?</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Access token in case it is set or null otherwise.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AuthenticationModeC9withToken06accessE0ACSS_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withToken(accessToken:)"></a>
<a class="token" href="#/s:7heresdk18AuthenticationModeC9withToken06accessE0ACSS_tFZ">withToken(accessToken:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>SDK will pass access token as a Bearer.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static func withToken(accessToken: String) -&gt; AuthenticationMode</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>accessToken</em>
</code>
</td>
<td>
<div>
<p>Access token</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Instance of <code>AuthenticationMode</code> configured to use token</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AuthenticationModeC17withTokenProvider05tokenF0ACSSSgyc_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withTokenProvider(tokenProvider:)"></a>
<a class="token" href="#/s:7heresdk18AuthenticationModeC17withTokenProvider05tokenF0ACSSSgyc_tFZ">withTokenProvider(tokenProvider:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>SDK will use access token provider to retrieve access token.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static func withTokenProvider(tokenProvider: @escaping AuthenticationMode.AccessTokenProvider) -&gt; AuthenticationMode</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tokenProvider</em>
</code>
</td>
<td>
<div>
<p>Access token provider</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Instance of <code>AuthenticationMode</code> configured to use token provider</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AuthenticationModeC12withExternalACyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withExternal()"></a>
<a class="token" href="#/s:7heresdk18AuthenticationModeC12withExternalACyFZ">withExternal()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Assumes the authentication is provided by the client.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static func withExternal() -&gt; AuthenticationMode</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Instance of <code>AuthenticationMode</code> configured to use externally provided authentication</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AuthenticationModeC13withKeySecret06accessE2Id0geF0ACSS_SStFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withKeySecret(accessKeyId:accessKeySecret:)"></a>
<a class="token" href="#/s:7heresdk18AuthenticationModeC13withKeySecret06accessE2Id0geF0ACSS_SStFZ">withKeySecret(accessKeyId:<wbr/>accessKeySecret:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>SDK will authenticate with access key id access key secret to obtain authentication token.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static func withKeySecret(accessKeyId: String, accessKeySecret: String) -&gt; AuthenticationMode</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>accessKeyId</em>
</code>
</td>
<td>
<div>
<p>The access key id</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>accessKeySecret</em>
</code>
</td>
<td>
<div>
<p>The access key secret</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Instance of <code>AuthenticationMode</code> configured to use key ID and secret</p>
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

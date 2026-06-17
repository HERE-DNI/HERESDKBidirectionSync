---
title: "ExternalMapDataSourceServer"
slug: "sdk-for-ios-navigate-classes-externalmapdatasourceserver"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/ExternalMapDataSourceServer"></a>
<a title="ExternalMapDataSourceServer Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-maploader">MapLoader</a>

        ExternalMapDataSourceServer Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ExternalMapDataSourceServer</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">ExternalMapDataSourceServer</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ExternalMapDataSourceServer</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ExternalMapDataSourceServer</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ExternalMapDataSourceServerCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk27ExternalMapDataSourceServerCACyKcfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span> <span class="k">throws</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ExternalMapDataSourceServerC5start3url6engine17serviceCredential8callbackySS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/start(url:engine:serviceCredential:callback:)"></a>
<a class="token" href="#/s:7heresdk27ExternalMapDataSourceServerC5start3url6engine17serviceCredential8callbackySS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF">start(url:<wbr/>engine:<wbr/>serviceCredential:<wbr/>callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Exposes map data source as GRPC service on given url for <code><a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a></code>.
The exposed service can be consumed with the help of <code><a href="../Classes/ExternalMapDataSourceClient.html#/s:7heresdk27ExternalMapDataSourceClientC30configureRemoteConnectionAsync3url6engine11credentials8callbackAA10TaskHandle_pSS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF">ExternalMapDataSourceClient.configureRemoteConnectionAsync(...)</a></code>.
It is a non-blocking function, and the result will be returned via a callback. <code><a href="../MapLoader.html#/s:7heresdk19ServerStartedHandlea">ServerStartedHandle</a></code>.</p>
<p>Note: This is a beta release of this feature,
so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">start</span><span class="p">(</span><span class="nv">url</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">engine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">serviceCredential</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-sslservercredentialsoptions">SslServerCredentialsOptions</a></span><span class="p">?,</span> <span class="nv">callback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../MapLoader.html#/s:7heresdk19ServerStartedHandlea">ServerStartedHandle</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>url</em>
</code>
</td>
<td>
<div>
<p>URL in the ‘ip_address:port’ format. Address will be used to bind to the GRPC server.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>engine</em>
</code>
</td>
<td>
<div>
<p>Instance of an existing <code><a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a></code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>serviceCredential</em>
</code>
</td>
<td>
<div>
<p>Instance of <code><a href="sdk-for-ios-navigate-structs-sslservercredentialsoptions">SslServerCredentialsOptions</a></code></p>
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
<p>Protocol to retrieve an operation status on the main thread.</p>
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
<a name="/s:7heresdk27ExternalMapDataSourceServerC4stopyyKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/stop()"></a>
<a class="token" href="#/s:7heresdk27ExternalMapDataSourceServerC4stopyyKF">stop()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Stops the exposed map data source GRPC service started using <code><a href="../Classes/ExternalMapDataSourceServer.html#/s:7heresdk27ExternalMapDataSourceServerC5start3url6engine17serviceCredential8callbackySS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF">ExternalMapDataSourceServer.start(...)</a></code>.</p>
<p>Note: This is a beta release of this feature,
so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../MapLoader.html#/s:7heresdk35ExternalMapDataSourceExceptionErrora">ExternalMapDataSourceExceptionError</a></code> Indicates what went wrong when trying to stop exposed external map data source service.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">stop</span><span class="p">()</span> <span class="k">throws</span></code></pre>
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

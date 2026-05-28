---
title: "MapLoader / ExternalMapDataSourceClient"
slug: "sdk-for-ios-navigate-api-reference-classes-externalmapdatasourceclient"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/ExternalMapDataSourceClient"></a>
<a title="ExternalMapDataSourceClient Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-maploader">MapLoader</a>
<img alt="" id="carat" src="../img/carat.png"/>
        ExternalMapDataSourceClient Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ExternalMapDataSourceClient</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">ExternalMapDataSourceClient</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ExternalMapDataSourceClient</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ExternalMapDataSourceClient</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
<a name="/s:7heresdk27ExternalMapDataSourceClientCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk27ExternalMapDataSourceClientCACyKcfc">init()</a>
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
<a name="/s:7heresdk27ExternalMapDataSourceClientC30configureRemoteConnectionAsync3url6engine11credentials8callbackAA10TaskHandle_pSS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/configureRemoteConnectionAsync(url:engine:credentials:callback:)"></a>
<a class="token" href="#/s:7heresdk27ExternalMapDataSourceClientC30configureRemoteConnectionAsync3url6engine11credentials8callbackAA10TaskHandle_pSS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF">configureRemoteConnectionAsync(url:<wbr/>engine:<wbr/>credentials:<wbr/>callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Initialize <code><a href="sdk-for-ios-navigate-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></code> with URL of the remote map data source gRPC server.
Newly injected map data source replaces exiting one if <code><a href="sdk-for-ios-navigate-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></code> was already connected.
Suggested configuration is taken from <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV21catalogConfigurationsSayAA20CatalogConfigurationVGvp">SDKOptions.catalogConfigurations</a></code>, actual catalog
versions are queried from the remote connection in order to be in sync.
It is a non-blocking function, and the result will be returned via a callback <code><a href="../MapLoader.html#/s:7heresdk25ConfigureConnectionHandlea">ConfigureConnectionHandle</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">configureRemoteConnectionAsync</span><span class="p">(</span><span class="nv">url</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">engine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">credentials</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-sslclientcredentialsoptions">SslClientCredentialsOptions</a></span><span class="p">?,</span> <span class="nv">callback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../MapLoader.html#/s:7heresdk25ConfigureConnectionHandlea">ConfigureConnectionHandle</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>URL to connect with the remote map data source gRPC server.
The remote map data source gRPC server could be self managed service created with help OCM Access Manager (OCM AM) or
service exposed using <code><a href="../Classes/ExternalMapDataSourceServer.html#/s:7heresdk27ExternalMapDataSourceServerC5start3url6engine17serviceCredential8callbackySS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF">ExternalMapDataSourceServer.start(...)</a></code></p>
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
<p>Instance of an existing <code><a href="sdk-for-ios-navigate-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>credentials</em>
</code>
</td>
<td>
<div>
<p>Instance of <code><a href="sdk-for-ios-navigate-api-reference-..-structs-sslclientcredentialsoptions">SslClientCredentialsOptions</a></code></p>
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.
NOTE: Cancelation functionality has not implemented yet!</p>
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

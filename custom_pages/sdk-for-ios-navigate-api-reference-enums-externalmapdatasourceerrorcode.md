---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-enums-externalmapdatasourceerrorcode"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ExternalMapDataSourceErrorCode.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ExternalMapDataSourceErrorCode"></a>
<a title="ExternalMapDataSourceErrorCode Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-maploader">MapLoader</a>
<img alt="" id="carat" src="../img/carat.png"/>
        ExternalMapDataSourceErrorCode Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ExternalMapDataSourceErrorCode</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ExternalMapDataSourceErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ExternalMapDataSourceErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
<p>Describes the reason for failing to configure <code><a href="sdk-for-ios-navigate-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></code> with external map data source.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30ExternalMapDataSourceErrorCodeO08internalF0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/internalError"></a>
<a class="token" href="#/s:7heresdk30ExternalMapDataSourceErrorCodeO08internalF0yA2CmF">internalError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Internal error occurred.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">internalError</span> <span class="o">=</span> <span class="mi">1</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30ExternalMapDataSourceErrorCodeO010addCatalogF0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/addCatalogError"></a>
<a class="token" href="#/s:7heresdk30ExternalMapDataSourceErrorCodeO010addCatalogF0yA2CmF">addCatalogError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Error while adding catalog to <code>DataStoreClient</code>.
Verify the same catalogs are added to the <code>DataStoreServer</code> instance on the server side.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">addCatalogError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30ExternalMapDataSourceErrorCodeO18invalidCredentialsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidCredentials"></a>
<a class="token" href="#/s:7heresdk30ExternalMapDataSourceErrorCodeO18invalidCredentialsyA2CmF">invalidCredentials</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Error while checking credentials. E.g. some field is empty but expected not empty</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">invalidCredentials</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30ExternalMapDataSourceErrorCodeO015serviceRegisterF0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/serviceRegisterError"></a>
<a class="token" href="#/s:7heresdk30ExternalMapDataSourceErrorCodeO015serviceRegisterF0yA2CmF">serviceRegisterError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Error while attempting to register OCM AM service</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">serviceRegisterError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30ExternalMapDataSourceErrorCodeO014clientDisposedF0yA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/clientDisposedError"></a>
<a class="token" href="#/s:7heresdk30ExternalMapDataSourceErrorCodeO014clientDisposedF0yA2CmF">clientDisposedError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>While attempting to register the connection, the client was being disposed</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">clientDisposedError</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30ExternalMapDataSourceErrorCodeO17serverUnavailableyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/serverUnavailable"></a>
<a class="token" href="#/s:7heresdk30ExternalMapDataSourceErrorCodeO17serverUnavailableyA2CmF">serverUnavailable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This means that server is not launched or configuration settings is wrong.
Make sense only on client side</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">serverUnavailable</span></code></pre>
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

</div>
`
}</HTMLBlock>

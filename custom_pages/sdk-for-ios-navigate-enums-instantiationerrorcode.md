---
title: "InstantiationErrorCode"
slug: "sdk-for-ios-navigate-enums-instantiationerrorcode"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a title="InstantiationErrorCode Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-core">Core</a>

        InstantiationErrorCode Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>InstantiationErrorCode</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
<p>Instantiation error.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO16illegalArgumentsyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/illegalArguments"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO16illegalArgumentsyA2CmF">illegalArguments</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Illegal arguments.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">illegalArguments</span> <span class="o">=</span> <span class="mi">1</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO6failedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/failed"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO6failedyA2CmF">failed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Instantiation attempt failed. Please check log for error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">failed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO30sharedSdkEngineNotInstantiatedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sharedSdkEngineNotInstantiated"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO30sharedSdkEngineNotInstantiatedyA2CmF">sharedSdkEngineNotInstantiated</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Instantiation attempt failed because the shared SDK engine is not instantiated.
Please initialise the SDK.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">sharedSdkEngineNotInstantiated</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO23cacheFolderAccessDeniedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cacheFolderAccessDenied"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO23cacheFolderAccessDeniedyA2CmF">cacheFolderAccessDenied</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Access to the specified cache folder is denied</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cacheFolderAccessDenied</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO38persistentMapStorageFolderAccessDeniedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/persistentMapStorageFolderAccessDenied"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO38persistentMapStorageFolderAccessDeniedyA2CmF">persistentMapStorageFolderAccessDenied</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Access to the specified persistent map storage folder is denied</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">persistentMapStorageFolderAccessDenied</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO23failedToLockCacheFolderyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/failedToLockCacheFolder"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO23failedToLockCacheFolderyA2CmF">failedToLockCacheFolder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The cache folder for given access key id is locked by other instance of SDKNativeEngine</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">failedToLockCacheFolder</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO30failedToCreateAnalyticsServiceyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/failedToCreateAnalyticsService"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO30failedToCreateAnalyticsServiceyA2CmF">failedToCreateAnalyticsService</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Analytics service can not be created</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">failedToCreateAnalyticsService</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO30accessKeyContainsIllegalSymbolyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/accessKeyContainsIllegalSymbol"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO30accessKeyContainsIllegalSymbolyA2CmF">accessKeyContainsIllegalSymbol</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Access key contains illegal symbols.
The below characters are not supported:
A. ‘(single quote)
B. “(double quote)</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">accessKeyContainsIllegalSymbol</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO36accessKeySecretContainsIllegalSymbolyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/accessKeySecretContainsIllegalSymbol"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO36accessKeySecretContainsIllegalSymbolyA2CmF">accessKeySecretContainsIllegalSymbol</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Access key secret contains illegal symbols.
The below characters are not supported:
A. ‘(single quote)
B. “(double quote)</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">accessKeySecretContainsIllegalSymbol</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO26layerConfigurationMismatchyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/layerConfigurationMismatch"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO26layerConfigurationMismatchyA2CmF">layerConfigurationMismatch</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Please check SDKOptions.layerConfiguration against SDK modules configuration.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">layerConfigurationMismatch</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO24sdkEngineAlreadyDisposedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sdkEngineAlreadyDisposed"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO24sdkEngineAlreadyDisposedyA2CmF">sdkEngineAlreadyDisposed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Instantiation attempt failed because the <code>dispose()</code> method from <code><a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a></code>
was called already.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">sdkEngineAlreadyDisposed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO27invalidCatalogConfigurationyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/invalidCatalogConfiguration"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO27invalidCatalogConfigurationyA2CmF">invalidCatalogConfiguration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="sdk-for-ios-navigate-structs-catalogconfiguration">CatalogConfiguration</a></code> contains invalid parameters.
Check the corectness of HRNs and versions.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">invalidCatalogConfiguration</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO22dataFolderAccessDeniedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/dataFolderAccessDenied"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO22dataFolderAccessDeniedyA2CmF">dataFolderAccessDenied</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Access to the specified data folder is denied</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">dataFolderAccessDenied</span></code></pre>
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

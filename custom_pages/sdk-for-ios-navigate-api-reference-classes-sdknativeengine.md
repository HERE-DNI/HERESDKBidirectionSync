---
title: "SDKNativeEngine"
slug: "sdk-for-ios-navigate-api-reference-classes-sdknativeengine"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/SDKNativeEngine"></a>
<a title="SDKNativeEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-core">Core</a>

        SDKNativeEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SDKNativeEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SDKNativeEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SDKNativeEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SDKNativeEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Holds internal services and configurations needed by various HERE SDK modules.</p>
<p>You can initialize the HERE SDK in two ways:</p>
<ul>
<li>Create a shared instance of the <code>SDKNativeEngine</code> with <code>SDKNativeEngine.makeSharedInstance()</code>.</li>
<li>Create individual instances of the <code>SDKNativeEngine</code> via <code>SDKNativeEngine()</code>. Note that this does not automatically set a shared instance.</li>
</ul>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SDKNativeEngineC7optionsAcA10SDKOptionsV_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(options:)"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC7optionsAcA10SDKOptionsV_tKcfc">init(options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Makes a new instance of SDKNativeEngine using supplied options.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-sdkoptions">SDKOptions</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>The options for the new engine.</p>
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
<a name="/s:7heresdk15SDKNativeEngineC7optionsAA10SDKOptionsVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/options"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC7optionsAA10SDKOptionsVvp">options</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options used by this instance of <code>SDKNativeEngine</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-sdkoptions">SDKOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SDKNativeEngineC14sharedInstanceACSgvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/sharedInstance"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC14sharedInstanceACSgvpZ">sharedInstance</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Shared instance of this SDK engine that can be accessed by any HERE SDK module as the default
engine.
This is automatically set as a part of the SDK initialization process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">var</span> <span class="nv">sharedInstance</span><span class="p">:</span> <span class="kt">SDKNativeEngine</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SDKNativeEngineC13isOfflineModeSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isOfflineMode"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC13isOfflineModeSbvp">isOfflineMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The offline mode.
Sets offline mode for the HERE SDK to offline or online.
Defaults to false, which means the HERE SDK uses an online connection.
When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set.
See <code><a href="../Classes/SDKNativeEngine.html#/s:7heresdk15SDKNativeEngineC19passThroughFeaturesShyAA04PassE7FeatureOGSgvp">SDKNativeEngine.passThroughFeatures</a></code>.
Note that the flag does not cancel pending requests.
The mode can be enabled or disabled at any time. In order to fully operate offline, the mode
needs to be enabled via <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV11offlineModeSbvp">SDKOptions.offlineMode</a></code>.
Initialization of the HERE SDK itself does not require an internet connection.
Returns <code>true</code> if the HERE SDK uses offline connection mode, otherwise returns <code>false</code>.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isOfflineMode</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SDKNativeEngineC19passThroughFeaturesShyAA04PassE7FeatureOGSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/passThroughFeatures"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC19passThroughFeaturesShyAA04PassE7FeatureOGSgvp">passThroughFeatures</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The pass through features.
Sets pass through features which are allowed to use online data when HERE SDK is in offline mode.
Pass through features can be updated at any time.
When offline mode is disabled, existing pass through features will be removed.
These needs to be set again when you enable offline mode next time.
By default, reporting of HERE SDK <code><a href="sdk-for-ios-navigate-api-reference-structs-usagestats">UsageStats</a></code> will be enabled when at least one pass-through feature is set.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">passThroughFeatures</span><span class="p">:</span> <span class="kt">Set</span><span class="o">&lt;</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-passthroughfeature">PassThroughFeature</a></span><span class="o">&gt;</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SDKNativeEngineC15parameterConfigAA22ParameterConfigurationVvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/parameterConfig"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC15parameterConfigAA22ParameterConfigurationVvpZ">parameterConfig</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configuration for default values of parameters used in the HERE SDK.
<strong>Note:</strong> This feature is in beta state and thus there can be bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">var</span> <span class="nv">parameterConfig</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-parameterconfiguration">ParameterConfiguration</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SDKNativeEngineC13proxySettingsAA05ProxyE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/proxySettings"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC13proxySettingsAA05ProxyE0VSgvp">proxySettings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Proxy settings of this SDK engine that will be used by HERE SDK network for all requests.
Defaults to (<code>nil</code>), which indicates proxy is not enabled.
When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings.
Pass (<code>nil</code>) to indicate that proxy should be disabled.
If proxy is necessary from the start then it’s recommended to use <code><a href="../Structs/NetworkSettings.html#/s:7heresdk15NetworkSettingsV05proxyC0AA05ProxyC0VSgvp">NetworkSettings.proxySettings</a></code> in <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV15networkSettingsAA07NetworkD0Vvp">SDKOptions.networkSettings</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">proxySettings</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-proxysettings">ProxySettings</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SDKNativeEngineC13sdkUsageStatsSayAA0eF0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sdkUsageStats"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC13sdkUsageStatsSayAA0eF0VGvp">sdkUsageStats</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets a list of usage statistics for all available HERE SDK features.
<code><a href="sdk-for-ios-navigate-api-reference-structs-usagestats">UsageStats</a></code> has cache and persistent storage. Reads from the persistent storage happen on <code>SDKNativeEngine</code> creation step.
Writes to persistent storage happen by reaching internal limit (amount of upload bytes, by default is 50KB).</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">sdkUsageStats</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-usagestats">UsageStats</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SDKNativeEngineC19PurgeMemoryStrategyO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/PurgeMemoryStrategy"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC19PurgeMemoryStrategyO">PurgeMemoryStrategy</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enum representing a strategy to flush memory caches.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine-purgememorystrategy">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">PurgeMemoryStrategy</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SDKNativeEngineC18setAccessKeySecret06accessfG0ySS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setAccessKeySecret(accessKeySecret:)"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC18setAccessKeySecret06accessfG0ySS_tF">setAccessKeySecret(accessKeySecret:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Overrides HERE SDK access key secret with new value.
The new credentials will be used for new requests.</p>
<p><strong>Note:</strong>
This method can be called from any thread.
Access key ID can be set with constructor of SDKNativeEngine.
New instance of SDKNativeEngine should be used if a new access key ID is required.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setAccessKeySecret</span><span class="p">(</span><span class="nv">accessKeySecret</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>accessKeySecret</em>
</code>
</td>
<td>
<div>
<p>New access key secret.</p>
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
<a name="/s:7heresdk15SDKNativeEngineC14setAccessScope5scopeySS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setAccessScope(scope:)"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC14setAccessScope5scopeySS_tF">setAccessScope(scope:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Overrides the token scope of the HERE SDK with new value.
A new token will be fetched with the set scope and used for future requests.
Setting an empty string will fetch a token for the global scope.</p>
<p>This method can be called from any thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setAccessScope</span><span class="p">(</span><span class="nv">scope</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>scope</em>
</code>
</td>
<td>
<div>
<p>New scope for token</p>
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
<a name="/s:7heresdk15SDKNativeEngineC16enableUsageStats7enabledySb_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/enableUsageStats(enabled:)"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC16enableUsageStats7enabledySb_tF">enableUsageStats(enabled:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enable or disable <code><a href="sdk-for-ios-navigate-api-reference-structs-usagestats">UsageStats</a></code> for the HERE SDK. Defaults to disabled (false). When enabled, <code>SDKNativeEngine.getSdkUsageStats()</code>
returns actual online data consumption. Note that the flag does not cancel pending requests.
<code><a href="sdk-for-ios-navigate-api-reference-structs-usagestats">UsageStats</a></code> can be enabled or disabled at any time.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">enableUsageStats</span><span class="p">(</span><span class="nv">enabled</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>enabled</em>
</code>
</td>
<td>
<div>
<p>True, if UsageStats are enabled.</p>
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
<a name="/s:7heresdk15SDKNativeEngineC18makeSharedInstance7optionsyAA10SDKOptionsV_tKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/makeSharedInstance(options:)"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC18makeSharedInstance7optionsyAA10SDKOptionsV_tKFZ">makeSharedInstance(options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Makes a new instance of SDKNativeEngine using supplied options and stores it as shared instance
see <code><a href="../Classes/SDKNativeEngine.html#/s:7heresdk15SDKNativeEngineC14sharedInstanceACSgvpZ">SDKNativeEngine.sharedInstance</a></code>. If there was previously shared instance
then  it’s destroyed
before new instance is created.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">makeSharedInstance</span><span class="p">(</span><span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-sdkoptions">SDKOptions</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>The options for the new engine.</p>
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
<a name="/s:7heresdk15SDKNativeEngineC25clearPersistentUsageStatsyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/clearPersistentUsageStats()"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC25clearPersistentUsageStatsyyF">clearPersistentUsageStats()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Clear persistent storage for the HERE SDK <code><a href="sdk-for-ios-navigate-api-reference-structs-usagestats">UsageStats</a></code>.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">clearPersistentUsageStats</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SDKNativeEngineC20clearUsageStatsCacheyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/clearUsageStatsCache()"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC20clearUsageStatsCacheyyF">clearUsageStatsCache()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Clear cache for the HERE SDK <code><a href="sdk-for-ios-navigate-api-reference-structs-usagestats">UsageStats</a></code>.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">clearUsageStatsCache</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SDKNativeEngineC17purgeMemoryCaches8strategyyAC05PurgeE8StrategyO_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/purgeMemoryCaches(strategy:)"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC17purgeMemoryCaches8strategyyAC05PurgeE8StrategyO_tF">purgeMemoryCaches(strategy:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Releases memory occupied by internal caches.
Purging caches reduces memory footprint of application and may temporary reduce performance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">purgeMemoryCaches</span><span class="p">(</span><span class="nv">strategy</span><span class="p">:</span> <span class="kt">SDKNativeEngine</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine-purgememorystrategy">PurgeMemoryStrategy</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>strategy</em>
</code>
</td>
<td>
<div>
<p>Option to control how much memory caches will be purged.</p>
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
<a name="/s:7heresdk15SDKNativeEngineC11getDeviceId10completionyySSc_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getDeviceId(completion:)"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC11getDeviceId10completionyySSc_tF">getDeviceId(completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The unique identifier assigned to the device for this application.
This device ID is primarily used for tracking Monthly Active Users (MAUs).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getDeviceId</span><span class="p">(</span><span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Core.html#/s:7heresdk14DeviceIdHandlea">DeviceIdHandle</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
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

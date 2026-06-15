---
title: "proxySettings property"
slug: "sdk-for-flutter-navigate-core-engine-sdknativeengine-proxysettings"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- proxySettings.html -->


<div>
<h1>proxySettings property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-core-engine-proxysettings-class">ProxySettings</a>?
proxySettings


<p>Proxy settings of this SDK engine that will be used by HERE SDK network for all requests.
Defaults to (<code>null</code>), which indicates proxy is not enabled.
When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings.
Pass (<code>null</code>) to indicate that proxy should be disabled.
If proxy is necessary from the start then it's recommended to use <a href="sdk-for-flutter-navigate-core-engine-networksettings-proxysettings">NetworkSettings.proxySettings</a> in <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-networksettings">SDKOptions.networkSettings</a>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
Gets the current proxy settings.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ProxySettings? get proxySettings;</code></pre>

</section>
<section id="setter">

void
proxySettings=(<a href="sdk-for-flutter-navigate-core-engine-proxysettings-class">ProxySettings</a>? value)


<p>Proxy settings of this SDK engine that will be used by HERE SDK network for all requests.
Defaults to (<code>null</code>), which indicates proxy is not enabled.
When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings.
Pass (<code>null</code>) to indicate that proxy should be disabled.
If proxy is necessary from the start then it's recommended to use <a href="sdk-for-flutter-navigate-core-engine-networksettings-proxysettings">NetworkSettings.proxySettings</a> in <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-networksettings">SDKOptions.networkSettings</a>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
Sets the proxy settings.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set proxySettings(ProxySettings? value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>

---
title: "isOfflineMode property"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-isofflinemode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isOfflineMode.html -->


<div>
<h1>isOfflineMode property</h1></div>
<section id="getter">

bool
isOfflineMode


<p>The offline mode.
Sets offline mode for the HERE SDK to offline or online.
Defaults to false, which means the HERE SDK uses an online connection.
When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set.
See <a href="/sdk-for-flutter-explore-core-engine-sdknativeengine-passthroughfeatures">SDKNativeEngine.passThroughFeatures</a>.
Note that the flag does not cancel pending requests.
The mode can be enabled or disabled at any time. In order to fully operate offline, the mode
needs to be enabled via <a href="/sdk-for-flutter-explore-core-engine-sdkoptions-offlinemode">SDKOptions.offlineMode</a>.
Initialization of the HERE SDK itself does not require an internet connection.
Returns <code>true</code> if the HERE SDK uses offline connection mode, otherwise returns <code>false</code>.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
Gets the current offline mode.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isOfflineMode;</code></pre>

</section>
<section id="setter">

void
isOfflineMode=(bool value)


<p>The offline mode.
Sets offline mode for the HERE SDK to offline or online.
Defaults to false, which means the HERE SDK uses an online connection.
When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set.
See <a href="/sdk-for-flutter-explore-core-engine-sdknativeengine-passthroughfeatures">SDKNativeEngine.passThroughFeatures</a>.
Note that the flag does not cancel pending requests.
The mode can be enabled or disabled at any time. In order to fully operate offline, the mode
needs to be enabled via <a href="/sdk-for-flutter-explore-core-engine-sdkoptions-offlinemode">SDKOptions.offlineMode</a>.
Initialization of the HERE SDK itself does not require an internet connection.
Returns <code>true</code> if the HERE SDK uses offline connection mode, otherwise returns <code>false</code>.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
Sets the offline mode.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isOfflineMode(bool value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>

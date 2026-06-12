---
title: "passThroughFeatures property"
slug: "sdk-for-flutter-navigate-core-engine-sdknativeengine-passthroughfeatures"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- passThroughFeatures.html -->


<div>
<h1>passThroughFeatures property</h1></div>
<section id="getter">

Set&lt;<a href="/sdk-for-flutter-navigate-core-engine-passthroughfeature">PassThroughFeature</a>&gt;?
passThroughFeatures


<p>The pass through features.
Sets pass through features which are allowed to use online data when HERE SDK is in offline mode.
Pass through features can be updated at any time.
When offline mode is disabled, existing pass through features will be removed.
These needs to be set again when you enable offline mode next time.
By default, reporting of HERE SDK <a href="/sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a> will be enabled when at least one pass-through feature is set.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
Gets the pass through features.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Set&lt;PassThroughFeature&gt;? get passThroughFeatures;</code></pre>

</section>
<section id="setter">

void
passThroughFeatures=(Set&lt;<a href="/sdk-for-flutter-navigate-core-engine-passthroughfeature">PassThroughFeature</a>&gt;? value)


<p>The pass through features.
Sets pass through features which are allowed to use online data when HERE SDK is in offline mode.
Pass through features can be updated at any time.
When offline mode is disabled, existing pass through features will be removed.
These needs to be set again when you enable offline mode next time.
By default, reporting of HERE SDK <a href="/sdk-for-flutter-navigate-core-engine-usagestats-class">UsageStats</a> will be enabled when at least one pass-through feature is set.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
Sets the pass through features.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set passThroughFeatures(Set&lt;PassThroughFeature&gt;? value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>

---
title: "LayerConfiguration constructor"
slug: "sdk-for-flutter-navigate-core-engine-layerconfiguration-layerconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LayerConfiguration.html -->


<div>
<h1>LayerConfiguration constructor</h1></div>

LayerConfiguration(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a>&gt; enabledFeatures</li>
</ol>)
    

<p>Initializes both, <code>enabled_features</code> and <code>implicitly_prefetched_features</code> with value passed to constructor.</p>
<ul>
<li><code>enabledFeatures</code> List of map features to downloader through <code>MapDownloader</code>, and implicitly prefetch when using <code>MapView</code></li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LayerConfiguration(List&lt;LayerConfigurationFeature&gt; enabledFeatures) =&gt; $prototype.$init(enabledFeatures);</code></pre>

 



</div>
`
}</HTMLBlock>

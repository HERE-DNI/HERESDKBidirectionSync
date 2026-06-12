---
title: "MapMatcher.withLayers constructor"
slug: "sdk-for-flutter-navigate-mapmatcher-mapmatcher-mapmatcher-withlayers"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMatcher.withLayers.html -->


<div>
<h1>MapMatcher.withLayers constructor</h1></div>

MapMatcher.withLayers(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> sdkEngine, </li>
<li>bool useRenderingLayers</li>
</ol>)
    

<p>Creates a new instance of this class.</p>
<ul>
<li>
<p><code>sdkEngine</code> A SDKEngine instance.</p>
</li>
<li>
<p><code>useRenderingLayers</code> When set to true, <code>LayerConfiguration.Feature.RENDERING</code> is used;
otherwise, <code>LayerConfiguration.Feature.EHORIZON</code> is used to retrieve segment geometry data from the OCM map.
Note: Ensure the corresponding layer is properly enabled in your <code>LayerConfiguration</code> to avoid incorrect results.</p>
</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. Indicates what went wrong when the instantiation was attempted.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMatcher.withLayers(SDKNativeEngine sdkEngine, bool useRenderingLayers) =&gt; $prototype.withLayers(sdkEngine, useRenderingLayers);</code></pre>

 



</div>
`
}</HTMLBlock>

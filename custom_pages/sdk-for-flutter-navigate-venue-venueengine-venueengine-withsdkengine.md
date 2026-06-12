---
title: "VenueEngine.withSdkEngine constructor"
slug: "sdk-for-flutter-navigate-venue-venueengine-venueengine-withsdkengine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueEngine.withSdkEngine.html -->


<div>
<h1>VenueEngine.withSdkEngine constructor</h1></div>

VenueEngine.withSdkEngine(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> sdkEngine, </li>
<li><a href="/sdk-for-flutter-navigate-venue-venueengineinitcallback">VenueEngineInitCallback</a>? callback</li>
</ol>)
    

<p>Creates a new instance of this class.</p>
<ul>
<li>
<p><code>sdkEngine</code> Instance of existing SDKEngine.</p>
</li>
<li>
<p><code>callback</code> The optional callback that will be triggered when a venue engine initialization
will be completed. After the initialization, the <a href="/sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a> should
be started using one of its methods or using <a href="/sdk-for-flutter-navigate-venue-venueengine-startwithtoken">VenueEngine.startWithToken</a>.</p>
</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. Indicates what went wrong when the instantiation was attempted.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueEngine.withSdkEngine(SDKNativeEngine sdkEngine, VenueEngineInitCallback? callback) =&gt; $prototype.withSdkEngine(sdkEngine, callback);</code></pre>

 



</div>
`
}</HTMLBlock>

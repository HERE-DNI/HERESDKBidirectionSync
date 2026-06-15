---
title: "VenueEngine constructor"
slug: "sdk-for-flutter-navigate-venue-venueengine-venueengine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueEngine.html -->


<div>
<h1>VenueEngine constructor</h1></div>

VenueEngine(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-venue-venueengineinitcallback">VenueEngineInitCallback</a>? callback</li>
</ol>)
    

<p>Creates a new instance of this class.</p>
<ul>
<li><code>callback</code> The optional callback that will be triggered when a venue engine initialization
will be completed. After the initialization, the <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a> should
be started using one of its methods or using <a href="sdk-for-flutter-navigate-venue-venueengine-startwithtoken">VenueEngine.startWithToken</a>.</li>
</ul>
<p>Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. Indicates what went wrong when the instantiation was attempted.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueEngine(VenueEngineInitCallback? callback) =&gt; $prototype.$init(callback);</code></pre>

 



</div>
`
}</HTMLBlock>

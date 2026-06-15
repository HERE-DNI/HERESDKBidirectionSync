---
title: "onFeaturesNotAvailable abstract method"
slug: "sdk-for-flutter-navigate-location-locationstatuslistener-onfeaturesnotavailable"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onFeaturesNotAvailable.html -->


<div>
<h1>onFeaturesNotAvailable abstract method</h1></div>

void
onFeaturesNotAvailable(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-location-locationfeature">LocationFeature</a>&gt; features</li>
</ol>)

      

    

<p>Called after start() if any requested location feature is not available
for the application.</p>
<p>Typically all features are enabled by default, but in
certain variants some features may be disabled, e.g. to reduce binary size.
If a feature that you need is not available, contact your HERE representative
for more information.</p>
<ul>
<li><code>features</code> List of unavailable location features.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onFeaturesNotAvailable(List&lt;LocationFeature&gt; features);</code></pre>

 



</div>
`
}</HTMLBlock>

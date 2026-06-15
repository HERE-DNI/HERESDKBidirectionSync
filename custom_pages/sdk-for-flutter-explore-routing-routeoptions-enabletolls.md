---
title: "enableTolls property"
slug: "sdk-for-flutter-explore-routing-routeoptions-enabletolls"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- enableTolls.html -->


<div>
<h1>enableTolls property</h1></div>

        
        bool
        enableTolls
<div class="features">getter/setter pair</div>


<p>A flag that indicates whether the resulting route <a href="sdk-for-flutter-explore-routing-section-tolls">Section.tolls</a> properties should contain
tolls data. Defaults to <code>false</code>.</p>
<p><strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
Consult your HERE representative to get more information on the related pricing schemes.</p>
<p><strong>Note:</strong> For users of the <code>OfflineRoutingEngine</code> this is a beta release of this feature,
so there could be a few bugs and unexpected behaviors. The <code>OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code>RoutingEngine</code> the feature is stable.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool enableTolls;</code></pre>

 



</div>
`
}</HTMLBlock>

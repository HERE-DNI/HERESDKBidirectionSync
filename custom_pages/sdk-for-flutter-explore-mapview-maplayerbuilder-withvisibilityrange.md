---
title: "withVisibilityRange abstract method"
slug: "sdk-for-flutter-explore-mapview-maplayerbuilder-withvisibilityrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withVisibilityRange.html -->


<div>
<h1>withVisibilityRange abstract method</h1></div>

<a href="/sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a>
withVisibilityRange(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-mapview-maplayervisibilityrange-class">MapLayerVisibilityRange</a> visibilityRange</li>
</ol>)

      

    

<p>Configures the builder to set the layer visible in the given zoom levels range.</p>
<p>Values outside the map zoom level range (0, 24) will be ignored.
Providing the visibility range is optional. If not provided, the layer will be visible
on all zoom levels.</p>
<ul>
<li><code>visibilityRange</code> Visibility range which should be applied to the layer.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a>. This class instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapLayerBuilder withVisibilityRange(MapLayerVisibilityRange visibilityRange);</code></pre>

 



</div>
`
}</HTMLBlock>

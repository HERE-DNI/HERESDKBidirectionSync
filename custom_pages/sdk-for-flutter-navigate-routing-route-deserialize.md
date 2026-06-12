---
title: "deserialize static method"
slug: "sdk-for-flutter-navigate-routing-route-deserialize"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- deserialize.html -->


<div>
<h1>deserialize static method</h1></div>

<a href="/sdk-for-flutter-navigate-routing-route-class">Route</a>?
deserialize(<ol class="parameter-list single-line"> <li>Uint8List routeData</li>
</ol>)

      

    

<p>Creates route from the given binary data.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>routeData</code> The binary of a serialized route.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-routing-route-class">Route?</a>. The route object restored from the binary data.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static Route? deserialize(Uint8List routeData) =&gt; $prototype.deserialize(routeData);</code></pre>

 



</div>
`
}</HTMLBlock>

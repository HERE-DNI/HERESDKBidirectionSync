---
title: "WarnerEngine.WithEngine constructor"
slug: "sdk-for-flutter-navigate-warner-warnerengine-warnerengine-withengine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WarnerEngine.WithEngine.html -->


<div>
<h1>WarnerEngine.WithEngine constructor</h1></div>

WarnerEngine.WithEngine(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> sdkEngine, </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a>&gt; enabledWarnings</li>
</ol>)
    

<p>Creates a new instance of this class.</p>
<ul>
<li>
<p><code>sdkEngine</code> A <code>SDKEngine</code> instance.</p>
</li>
<li>
<p><code>enabledWarnings</code> The list of warning types that should be monitored and processed
by the engine. Only warnings of these types will be generated.</p>
</li>
</ul>
<p>Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. Indicates what went wrong when the instantiation was attempted.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory WarnerEngine.WithEngine(SDKNativeEngine sdkEngine, List&lt;WarningType&gt; enabledWarnings) =&gt; $prototype.WithEngine(sdkEngine, enabledWarnings);</code></pre>

 



</div>
`
}</HTMLBlock>

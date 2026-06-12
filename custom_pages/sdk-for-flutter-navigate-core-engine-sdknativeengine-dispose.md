---
title: "dispose abstract method"
slug: "sdk-for-flutter-navigate-core-engine-sdknativeengine-dispose"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- dispose.html -->


<div>
<h1>dispose abstract method</h1></div>

Future&lt;void&gt;
dispose()

      

    

<p>Stops pending requests and closes open files and databases in main thread.</p>
<p>Dispose signal is sent to dependent modules.
Usage of engine, or dependent modules after calling dispose leads to undefined behavior.
Please be aware that this method does not clean any type of storage.
<strong>Note:</strong>
This method should be called from main thread.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Future&lt;void&gt; dispose();</code></pre>

 



</div>
`
}</HTMLBlock>

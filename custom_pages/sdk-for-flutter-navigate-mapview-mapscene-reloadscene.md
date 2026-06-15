---
title: "reloadScene abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapscene-reloadscene"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- reloadScene.html -->


<div>
<h1>reloadScene abstract method</h1></div>

void
reloadScene()

      

    

<p>Asynchronously reloads the current map scene from file.</p>
<p>This skips any cached data used internally and reloads the
scene including any changes made to the (custom) map styles in JSON.</p>
<p><code>MapFeature</code> settings will be preserved.</p>
<p>Internal optimization checks will be skipped to ensure all custom style changes are loaded. Therefore,
calling this method may take slightly longer than calling one of the <code>loadScene(..)</code> overloads.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void reloadScene();</code></pre>

 



</div>
`
}</HTMLBlock>

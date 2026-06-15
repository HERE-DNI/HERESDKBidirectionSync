---
title: "setAccessScope abstract method"
slug: "sdk-for-flutter-navigate-core-engine-sdknativeengine-setaccessscope"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setAccessScope.html -->


<div>
<h1>setAccessScope abstract method</h1></div>

void
setAccessScope(<ol class="parameter-list single-line"> <li>String scope</li>
</ol>)

      

    

<p>Overrides the token scope of the HERE SDK with new value.</p>
<p>A new token will be fetched with the set scope and used for future requests.
Setting an empty string will fetch a token for the global scope.</p>
<p>This method can be called from any thread.</p>
<ul>
<li><code>scope</code> New scope for token</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setAccessScope(String scope);</code></pre>

 



</div>
`
}</HTMLBlock>

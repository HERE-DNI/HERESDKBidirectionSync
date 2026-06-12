---
title: "setAccessKeySecret abstract method"
slug: "sdk-for-flutter-navigate-core-engine-sdknativeengine-setaccesskeysecret"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setAccessKeySecret.html -->


<div>
<h1>setAccessKeySecret abstract method</h1></div>

void
setAccessKeySecret(<ol class="parameter-list single-line"> <li>String accessKeySecret</li>
</ol>)

      

    

<p>Overrides HERE SDK access key secret with new value.</p>
<p>The new credentials will be used for new requests.</p>
<p><strong>Note:</strong>
This method can be called from any thread.
Access key ID can be set with constructor of SDKNativeEngine.
New instance of SDKNativeEngine should be used if a new access key ID is required.</p>
<ul>
<li><code>accessKeySecret</code> New access key secret.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setAccessKeySecret(String accessKeySecret);</code></pre>

 



</div>
`
}</HTMLBlock>

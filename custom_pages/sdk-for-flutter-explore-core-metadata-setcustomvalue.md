---
title: "setCustomValue abstract method"
slug: "sdk-for-flutter-explore-core-metadata-setcustomvalue"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setCustomValue.html -->


<div>
<h1>setCustomValue abstract method</h1></div>

void
setCustomValue(<ol class="parameter-list single-line"> <li>String key, </li>
<li><a href="/sdk-for-flutter-explore-core-custommetadatavalue-class">CustomMetadataValue</a> value</li>
</ol>)

      

    

<p>Creates a key:value pair, where the value is a type derived from CustomMetadataValue.</p>
<p>If the given key already exists, its value will be replaced by the new one.</p>
<ul>
<li>
<p><code>key</code> The name of the key to be created or replaced.</p>
</li>
<li>
<p><code>value</code> The value to be assigned to the key.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setCustomValue(String key, CustomMetadataValue value);</code></pre>

 



</div>
`
}</HTMLBlock>

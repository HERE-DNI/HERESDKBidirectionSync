---
title: "getType abstract method"
slug: "sdk-for-flutter-navigate-core-metadata-gettype"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getType.html -->


<div>
<h1>getType abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-core-metadatatype">MetadataType</a>?
getType(<ol class="parameter-list single-line"> <li>String key</li>
</ol>)

      

    

<p>Determines the type of a metadata value.</p>
<p>If the type of a metadata value associated with a key is not known, this
method will enable the type to be queried, in order to know which get method
to call. i.e. getDouble(), getInteger() etc.</p>
<ul>
<li><code>key</code> The name of the key for which to obtain the type.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-metadatatype">MetadataType?</a>. An enumeration describing the type of the value associated with the key.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MetadataType? getType(String key);</code></pre>

 



</div>
`
}</HTMLBlock>
